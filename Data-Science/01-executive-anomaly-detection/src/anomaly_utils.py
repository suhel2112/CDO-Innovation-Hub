from __future__ import annotations

import pandas as pd


def rolling_anomaly_scores(
    df: pd.DataFrame,
    date_col: str,
    value_col: str,
    window: int = 21,
    z_threshold: float = 3.0,
    center: bool = False,
) -> pd.DataFrame:
    """
    Compute rolling baseline + z-score style anomaly score for a time series.

    Returns df with:
      - baseline_mean
      - baseline_std
      - z_score
      - is_anomaly

    Notes:
    - Uses rolling mean/std; for more robustness you can swap mean->median.
    - Expects one row per date; if multiple, aggregate before calling.
    """
    out = df.copy()
    out[date_col] = pd.to_datetime(out[date_col])
    out = out.sort_values(date_col)

    # Rolling stats
    roll = out[value_col].rolling(window=window, min_periods=max(5, window // 3), center=center)
    out["baseline_mean"] = roll.mean()
    out["baseline_std"] = roll.std(ddof=0)

    # Avoid divide-by-zero
    out["baseline_std"] = out["baseline_std"].replace(0, pd.NA)

    out["z_score"] = (out[value_col] - out["baseline_mean"]) / out["baseline_std"]
    out["z_score"] = out["z_score"].astype("float")

    out["is_anomaly"] = out["z_score"].abs() >= z_threshold
    return out

