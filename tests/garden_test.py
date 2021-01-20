from src.gardener.models.vegetables.tomato import Tomato
from src.gardener.models.garden import Garden

class TestGarden():

    def test_parcels_are_empty_when_instantiate(_):
        garden = Garden()

        assert len(garden.parcels) == 0

    def test_update_parcels_len_when_add_seed(_):
        garden = Garden()
        garden.plant_seed(Tomato())

        assert len(garden.parcels) == 1

    def test_not_add_tomato_when_adult(_):
        garden = Garden()

        tomato = Tomato()
        tomato.grow(99999)

        success = garden.plant_seed(tomato)

        assert success == False
        assert tomato.is_seed == False
        assert len(garden.parcels) == 0
        
