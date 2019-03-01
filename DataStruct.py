from dataclasses import dataclass
from typing import Tuple


@dataclass
class Compartment:
    range: Tuple[float, float]
    letter: str

    def set_range(self, value: Tuple[float, float]) -> None:
        self.range = value
