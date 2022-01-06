import pytest

@pytest.fixture(autouse=True)
def separador():
    print("\nInicio de test de función\t----------------------------------\n")
    yield
    print("\nFin de test de función\t\t----------------------------------")