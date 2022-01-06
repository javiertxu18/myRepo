import pytest

from src.main.scripts.objects.Objective import Objective


@pytest.mark.parametrize('classinfo, inputName, expectedOutput', [
    (Objective, 'peter come pan', '***** **** ***'),
    (Objective, 'buenas tardes', '****** ******')])
def test_setShadow(classinfo, inputName, expectedOutput):
    print(f"test_setShadow(class {classinfo.__name__}, {inputName}, {expectedOutput})")
    obj = classinfo()  # Instanciamos el objeto
    obj._target = inputName  # Preparamos el target
    obj._setShadow()  # Ejecutamos la función
    assert obj._shadow == expectedOutput  # Hacemos el assert
    print("ok")


@pytest.mark.parametrize('classinfo, inputName, expectedOutput', [
    (Objective, 'peter come pan', '***** **** ***'),
    (Objective, 'buenas tardes', '****** ******')])
def test_setTarget(classinfo, inputName, expectedOutput):
    print(f"test_setTarget(class {classinfo.__name__}, {inputName}, {expectedOutput})")
    obj = classinfo()  # Instanciamos el objeto
    obj._setTarget(inputName)  # Ejecutamos la función
    assert obj._target == inputName  # Hacemos el assert del target
    assert obj._shadow == expectedOutput  # Hacemos el assert del shadow
    print("ok")


@pytest.mark.parametrize('classinfo, inputName, expectedOutput', [
    (Objective, 'peter come pan', ['peter', 'come', 'pan']),
    (Objective, 'buenas tardes', ['buenas', 'tardes'])])
def test_getSplitTarget(classinfo, inputName, expectedOutput):
    print(f"test_getSplitTarget(class {classinfo.__name__}, {inputName}, {expectedOutput})")
    obj = classinfo()  # Instanciamos el objeto
    obj._setTarget(inputName)  # Preparamos el target
    res = obj.getSplitTarget()  # Ejecutamos la función
    assert res == expectedOutput  # Hacemos el assert
    print("ok")


@pytest.mark.parametrize('classinfo, inputName', [
    (Objective, 'peter come pan'),
    (Objective, 'buenas tardes')])
def test_isAccomplished(classinfo, inputName):
    print(f"test_isAccomplished(class {classinfo.__name__}, {inputName})")
    obj = classinfo()  # Instanciamos el objeto
    obj._target = inputName  # Preparamos el target
    obj._shadow = inputName  # Preparamos el shadow
    assert obj.isAccomplished()  # Hacemos el assert
    print("ok")

