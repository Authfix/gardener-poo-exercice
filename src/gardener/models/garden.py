from typing import List

from .vegetables.vegetable import Vegetable


class Garden():
    """
    Représente un jarin
    """
    
    def __init__(self) -> None:
        self._parcels: List[Vegetable] = []

    @property
    def parcels(self):
        return self._parcels.copy()

    def plant_seed(self, seed: Vegetable) -> bool:

        if seed.is_seed:
            self._parcels.append(seed)
            return True
            
        return False