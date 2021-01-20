from typing import List

from .vegetables.vegetable import Vegetable

class Garden():
    """
    Représente un jardin
    """
    
    def __init__(self) -> None:
        self._parcels: List[Vegetable] = []

    @property
    def parcels(self):
        """
        Retourne l'occupation des parcels
        """
        return self._parcels.copy()

    def plant_seed(self, vegetable_to_plant: Vegetable) -> bool:
        """
        Plante un legume à l'état de graine dans une parcelle
        """
        if vegetable_to_plant.is_seed:
            self._parcels.append(vegetable_to_plant)
            return True
            
        return False