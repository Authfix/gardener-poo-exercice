from abc import ABC, abstractmethod

from .life_step import LifeSteps

class Vegetable(ABC):
    
    def __init__(self) -> None:
        super().__init__()

        self._current_step = LifeSteps.Seed
        self._water_level = 0

    @property
    def is_seed(self) -> bool:
        return self._current_step == LifeSteps.Seed

    @property
    def water_level(self) -> int:
        return self._water_level

    @property
    def current_step(self) -> LifeSteps:
        return self._current_step

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
            self._water_level = 0
            self._current_step = LifeSteps(self._current_step.value + 1)

