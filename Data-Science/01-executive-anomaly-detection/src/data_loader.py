from pathlib import Path
import pandas as pd


def load_yellow_taxi_data(
    raw_data_dir: Path,
    columns: list[str] | None = None,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Load and concatenate NYC Yellow Taxi parquet files.
    """

    files = sorted(raw_data_dir.glob("yellow_tripdata*.parquet"))

    if not files:
        raise FileNotFoundError(
            f"No files matching 'yellow_tripdata*.parquet' found in {raw_data_dir}"
        )

    if verbose:
        print("Loading the following files:")
        for f in files:
            print(" -", f.name)

    df = pd.concat(
        [pd.read_parquet(f, columns=columns) for f in files],
        ignore_index=True
    )

    if verbose:
        print(f"\nTotal rows loaded: {len(df):,}")

    return df
