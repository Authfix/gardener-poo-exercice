from src.gardener.models import Tomato, LifeSteps

class TestTomato:

    def test_water_level_updated_when_grow(_):
        water_to_add = 8

        tomato = Tomato()
        tomato.grow(water_to_add)

        assert tomato.water_level == water_to_add

    def test_is_seed_when_instantiate(_):
        tomato = Tomato()

        assert tomato.is_seed == True

    def test_is_no_more_seed_when_enough_water(_):
        tomato = Tomato()
        tomato.grow(99999)

        assert tomato.is_seed == False

    def test_step_2_when_grow_two_times_with_engough_water(_):
        tomato = Tomato()
        tomato.grow(99999)

        assert tomato.current_step == LifeSteps(1)

        tomato.grow(999999)

        assert tomato.current_step == LifeSteps(2)

    def test_step_1_when_grow_two_times_with_enough_water_one_time(_):
        tomato = Tomato()
        tomato.grow(99999)

        assert tomato.current_step == LifeSteps(1)

        tomato.grow(1)

        assert tomato.current_step == LifeSteps(1)