# Executive Anomaly Detection (Time Series)

## Problem Statement
Operational metrics can “drift” or break suddenly (missing scans, failed transactions, delays). Leaders need early warning signals and clear explanations.

## What this project delivers
- Automated anomaly detection on a daily metric (e.g., scan compliance %, volume, latency)
- Clear visuals highlighting anomaly windows
- A ranked table of anomaly dates and severity

## Visual Outputs
> Add generated images to `outputs/figures/` and link here.

- **Metric trend with anomalies highlighted**
- **Rolling baseline vs actual**
- **Top anomaly dates table (severity-ranked)**

## Approach (simple, defensible)
- Baseline: rolling median/mean + rolling std (robust option available)
- Anomaly score: z-score style deviation from baseline
- Guardrails: min history window, missing-data handling

## How to run
1. Open the notebook: `notebooks/anomaly_detection.ipynb`
2. Run all cells
3. Outputs saved to:
   - `outputs/figures/`
   - `outputs/tables/`

## Why this matters to leadership
- Faster detection of process breakdowns
- Better targeting of investigation effort
- Reduced time-to-response for operational risk

## Tech
Python, pandas, matplotlib
