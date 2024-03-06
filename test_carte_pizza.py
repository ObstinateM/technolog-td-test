import pytest
from carte_pizza import CartePizzeria, CartePizzeriaException
from mock import Mock


def test_carte_pizzeria_is_empty():
    carte = CartePizzeria()
    assert carte.is_empty()


def test_carte_pizzeria_nb_pizzas():
    carte = CartePizzeria()
    assert carte.nb_pizzas() == 0

    pizza = Mock()
    pizza.name = "Margherita"
    carte.add_pizza(pizza)
    assert carte.nb_pizzas() == 1


def test_carte_pizzeria_add_pizza():
    carte = CartePizzeria()
    pizza = Mock()
    pizza.name = "Margherita"
    carte.add_pizza(pizza)
    assert not carte.is_empty()


def test_carte_pizzeria_remove_pizza():
    carte = CartePizzeria()
    pizza = Mock()
    pizza.name = "Margherita"
    carte.add_pizza(pizza)
    carte.remove_pizza("Margherita")
    assert carte.is_empty()
    with pytest.raises(CartePizzeriaException):
        carte.remove_pizza("hfjdsqk")
