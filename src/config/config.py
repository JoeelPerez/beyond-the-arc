from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent

START_2026_REGULAR_SEASON = pd.Timestamp(year=2025, month=10, day=20)
END_2026_REGULAR_SEASON = pd.Timestamp(year=2026, month=4, day=13)

ALL_STARS_TEAMS = [
    "Stars",
    "Stripes",
    "Team Austin",
    "Team Melo",
    "Team T-Mac",
    "Team Vince",
    "World"
]
