from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent

START_2026_REGULAR_SEASON = pd.Timestamp(year=2025, month=10, day=1)
END_2026_REGULAR_SEASON = pd.Timestamp(year=2026, month=4, day=30)
