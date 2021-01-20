from src.gardener.models.garden import Garden

class TestGarden():

    def test_parcels_are_empty_when_instantiate(_):
        garden = Garden()

        assert len(garden.parcels) == 0

    def test_update_parcels_len_when_add_seed(_):
        garden = Garden()
        garden.plant_seed('X')

        assert len(garden.parcels) == 1
        
