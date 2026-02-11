# Executive Insights — Anomaly Detection

## Summary
This analysis monitors daily NYC Yellow Taxi trip volumes to identify unusual deviations from expected operational throughput.

Using rolling baselines and volatility analysis, we distinguish structural patterns (e.g. weekends) from genuinely unusual operational behaviour.

## Key Observations
- Daily trip volumes exhibit strong weekday/weekend seasonality.
- A small number of days show unusually large deviations from the rolling baseline.
- Volatility increases during specific periods, indicating operational instability even when averages appear normal.

## What This Means for Leadership
- Not all drops represent incidents — some are structural and predictable.
- Monitoring volatility alongside volume provides earlier warning signals.
- Ranked “unusual days” enable targeted investigation rather than blanket alerts.

## Recommended Actions
1. Monitor deviation *and* volatility, not just absolute volumes.
2. Prioritise investigation on the top-ranked unusual days.
3. Apply minimum-volume guardrails to avoid false alerts.

## Measurement of Success
- Reduced time to detect operational issues
- Fewer false-positive alerts
- Faster root-cause investigation
