import pytest
from carte_pizza import CartePizzeria, CartePizzeriaException
from mock import Mock
from pizza import Pizza
from drink import Drink
from dessert import Dessert


def test_carte_pizzeria_is_empty():
    carte = CartePizzeria()
    carte.pizzas = []
    carte.drinks = []
    carte.desserts = []
    assert carte.is_empty()
    carte.pizzas = [Mock(name="Margherita")]
    assert not carte.is_empty()


def test_carte_pizzeria_nb_pizzas():
    carte = CartePizzeria()
    carte.pizzas = [Mock(name="Margherita")]
    assert carte.nb_pizzas() == 1


def test_carte_pizzeria_add_pizza():
    carte = CartePizzeria()
    carte.pizzas = []
    carte.add(Mock(spec=Pizza))
    assert len(carte.pizzas) == 1


def test_carte_pizzeria_remove_pizza():
    carte = CartePizzeria()
    pizza = Mock(spec=Pizza)
    setattr(pizza, "name", "Margherita")
    carte.pizzas = [pizza]
    carte.remove(pizza)
    assert len(carte.pizzas) == 0
    with pytest.raises(CartePizzeriaException):
        carte.remove(pizza)


def test_carte_pizzeria_add_drink():
    carte = CartePizzeria()
    carte.drinks = []
    drink = Mock(spec=Drink)
    setattr(drink, "name", "Coca")
    carte.add(drink)
    assert len(carte.drinks) == 1


def test_carte_pizzeria_remove_drink():
    carte = CartePizzeria()
    drink = Mock(spec=Drink)
    setattr(drink, "name", "Coca")
    carte.drinks = [drink]
    carte.remove(drink)
    assert len(carte.drinks) == 0
    with pytest.raises(CartePizzeriaException):
        carte.remove(drink)


def test_carte_pizzeria_add_dessert():
    carte = CartePizzeria()
    carte.desserts = []
    dessert = Mock(spec=Dessert)
    setattr(dessert, "name", "Tiramisu")
    carte.add(dessert)
    assert len(carte.desserts) == 1


def test_carte_pizzeria_remove_dessert():
    carte = CartePizzeria()
    dessert = Mock(spec=Dessert)
    setattr(dessert, "name", "Tiramisu")
    carte.desserts = [dessert]
    carte.remove(dessert)
    assert len(carte.desserts) == 0
    with pytest.raises(CartePizzeriaException):
        carte.remove(dessert)
