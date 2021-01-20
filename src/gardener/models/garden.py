from typing import List


class Garden():
    """
    Représente un jarin
    """
    
    def __init__(self) -> None:
        self._parcels: List[str] = []

    @property
    def parcels(self):
        return self._parcels.copy()

    def plant_seed(self, seed: str) -> None:
        self._parcels.append(seed)