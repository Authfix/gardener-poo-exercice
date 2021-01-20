from abc import ABC, abstractmethod

class Vegetable(ABC):
    
    def __init__(self) -> None:
        super().__init__()

        self._water_level = 0
        self._is_seed = True

    @property
    def is_seed(self) -> bool:
        return self._is_seed

    @property
    @abstractmethod
    def _water_level_before_next_step(_) -> int:
        """
        Niveau d'eau requis pour ne plus être une graine
        """
        raise NotImplementedError

    def grow(self, number_of_liters: int):
        """
        Permet au légume de grandir
        """
        self._water_level += number_of_liters

        if self._water_level > self._water_level_before_next_step:
            self._is_seed = False

