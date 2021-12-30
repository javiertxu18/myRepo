import pytest

@pytest.fixture(autouse=True)
def separador():
    print("\n\t-------------------------------")
    yield
    print("\n\t-------------------------------")