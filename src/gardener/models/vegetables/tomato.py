from .vegetable import Vegetable


class Tomato(Vegetable):
    
    def __init__(_) -> None:
        super().__init__()

    @property
    def _water_level_before_next_step(_) -> int:
        """
        Nombre de litres d'eau nécessaires pour évoluer
        """
        return 10