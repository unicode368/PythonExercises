from Calculator import Calculator
import pytest as pytest

# !!test names are numbers


class TestCalculator:

    params = [[2, 6, 8], [3, 4, 7], [10, -3, 7],]

    # def get_test_name(self):

    #@staticmethod
    #def id_func(val):
    #    return f""

    @fixture
    def namer(request):
        request.node.name = 'test_foo'

    @pytest.mark.parametrize("x, y, z", argvalues=params)
    def test_add(self, x, y, z):
        assert Calculator.add(x, y) == z
        #,
        #   f"{x} plus {y} equals {z}"