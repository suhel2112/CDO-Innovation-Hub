import os
import json
from datetime import datetime, timezone, timedelta 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import feedparser
from dotenv import load_dotenv

load_dotenv()

FEED_URL = "https://medium.com/feed/tag/agentic-ai"
STATE_FILE = "state.json"

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")
FROM_EMAIL = os.getenv("FROM_EMAIL", TO_EMAIL)


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"last_published": None}
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def parse_published(entry):
    """
    Converts RSS published date to a datetime object in UTC.
    Falls back to now if something is weird.
    """
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    return datetime.now(tz=timezone.utc)

'''
def fetch_new_articles(last_published_iso: str | None):
    feed = feedparser.parse(FEED_URL)

    if feed.bozo:
        # bozo flag means parse error; we’ll just bail quietly
        print("Warning: problem parsing feed:", feed.bozo_exception)
        return [], last_published_iso

    entries = feed.entries

    # Convert saved ISO timestamp to datetime (if exists)
    if last_published_iso:
        last_published = datetime.fromisoformat(last_published_iso)
    else:
        last_published = None

    new_articles = []
    newest_seen = last_published

    for entry in entries:
        pub_dt = parse_published(entry)

        # Track latest publish time
        if (newest_seen is None) or (pub_dt > newest_seen):
            newest_seen = pub_dt

        # If we've never run before, don't blast you with the entire history.
        # We'll only start tracking from "now".
        if last_published is None:
            # Just skip adding anything this first run
            continue

        if pub_dt > last_published:
            new_articles.append(
                {
                    "title": entry.title,
                    "link": entry.link,
                    "published": pub_dt,
                    "summary": getattr(entry, "summary", ""),
                }
            )

    # If first run, set newest_seen but return no articles
    if last_published is None and newest_seen is not None:
        return [], newest_seen.isoformat()

    # For subsequent runs, return new ones + updated timestamp
    new_iso = newest_seen.isoformat() if newest_seen else last_published_iso
    return new_articles, new_iso
'''

def fetch_recent_articles(days: int = 7):
    """
    Fetch Medium 'agentic-ai' articles from the last N days.
    This works well in stateless environments like GitHub Actions.
    """
    feed = feedparser.parse(FEED_URL)

    if feed.bozo:
        print("Warning: problem parsing feed:", feed.bozo_exception)
        return []

    now_utc = datetime.now(tz=timezone.utc)
    cutoff = now_utc - timedelta(days=days)

    recent_articles = []

    for entry in feed.entries:
        pub_dt = parse_published(entry)

        if pub_dt >= cutoff:
            recent_articles.append(
                {
                    "title": entry.title,
                    "link": entry.link,
                    "published": pub_dt,
                    "summary": getattr(entry, "summary", ""),
                }
            )

    return recent_articles

def build_email_body(new_articles):
    if not new_articles:
        return "No new Agentic AI articles on Medium since last check."

    lines = [
        "Here are new Agentic AI articles on Medium since your last update:",
        "",
    ]
    for art in sorted(new_articles, key=lambda a: a["published"]):
        date_str = art["published"].strftime("%Y-%m-%d %H:%M UTC")
        lines.append(f"- {art['title']}  ({date_str})")
        lines.append(f"  {art['link']}")
        lines.append("")
    return "\n".join(lines)


def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

'''
def main():
    state = load_state()
    last_published_iso = state.get("last_published")

    new_articles, new_last_published_iso = fetch_new_articles(last_published_iso)

    if new_last_published_iso and new_last_published_iso != last_published_iso:
        state["last_published"] = new_last_published_iso
        save_state(state)

    if not new_articles:
        print("No new articles. Nothing to email.")
        return

    subject = f"[Agentic AI] {len(new_articles)} new Medium article(s)"
    body = build_email_body(new_articles)

    send_email(subject, body)
    print(f"Sent email with {len(new_articles)} articles.")
'''

def main():
    new_articles = fetch_recent_articles(days=7)

    if not new_articles:
        print("No recent articles. Nothing to email.")
        return

    subject = f"[Agentic AI] {len(new_articles)} Medium article(s) this week"
    body = build_email_body(new_articles)

    send_email(subject, body)
    print(f"Sent email with {len(new_articles)} articles.")


if __name__ == "__main__":
    main()
