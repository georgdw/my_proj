import pytest


@pytest.mark.parametrize("test_in_valid", [-100.0,-1.0,0.0,1.0,100.0])
                        
def check_parity_val(test_in_valid):
    try:
        assert test_in_invalid % 2 == 1
        return test_in_invalid
    except ZeroDivisionError:
        pass

