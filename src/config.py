"""Project configuration."""

from dataclasses import dataclass


@dataclass
class Paths:
    raw_data: str = "data/raw/fake_news.csv"
    processed_data: str = "data/processed/cleaned.csv"
    results_dir: str = "results"
    charts_dir: str = "results/charts"


@dataclass
class TrainingConfig:
    test_size: float = 0.2
    random_state: int = 42
    max_features: int = 50000
    max_len: int = None 
    num_words: int = 50000


PATHS = Paths()
CFG = TrainingConfig()
