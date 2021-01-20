from src.gardener.models import Tomato

class TestTomato:

    def test_water_level_updated_when_grow(_):
        water_to_add = 50

        tomato = Tomato()
        tomato.grow(water_to_add)

        assert tomato._water_level == water_to_add

    def test_is_seed_when_instantiate(_):
        tomato = Tomato()

        assert tomato.is_seed == True

    def test_is_no_more_seed_when_enough_water(_):
        tomato = Tomato()
        tomato.grow(99999)

        assert tomato.is_seed == False