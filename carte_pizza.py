from pizza import Pizza
from drink import Drink
from dessert import Dessert


class CartePizzeria:
    def __init__(self):
        self.pizzas = []
        self.drinks = []
        self.desserts = []

    def is_empty(self):
        return (len(self.pizzas) == 0 and len(self.drinks) == 0
                and len(self.desserts) == 0)

    def nb_pizzas(self):
        return len(self.pizzas)

    def nb_drinks(self):
        return len(self.drinks)

    def nb_desserts(self):
        return len(self.desserts)

    def add(self, element):
        if isinstance(element, Pizza):
            for pizza in self.pizzas:
                if pizza.name == element.name:
                    if (pizza.ingredients == element.ingredients
                            and pizza.base == element.base):
                        raise CartePizzeriaException("La pizza existe déjà")
            self.pizzas.append(element)
        elif isinstance(element, Drink):
            for drink in self.drinks:
                if drink.name == element.name:
                    if drink.size == element.size:
                        raise CartePizzeriaException("La boisson existe déjà")
            self.drinks.append(element)
        elif isinstance(element, Dessert):
            for dessert in self.desserts:
                if dessert.name == element.name:
                    if dessert.size == element.size:
                        raise CartePizzeriaException("Le dessert existe déjà")
            self.desserts.append(element)

    def remove(self, element):
        if isinstance(element, Pizza):
            for pizza in self.pizzas:
                if pizza.name == element.name:
                    self.pizzas.remove(pizza)
                    return
            raise CartePizzeriaException("La pizza n'existe pas")
        elif isinstance(element, Drink):
            for drink in self.drinks:
                if drink.name == element.name:
                    self.drinks.remove(drink)
                    return
            raise CartePizzeriaException("La boisson n'existe pas")
        elif isinstance(element, Dessert):
            for dessert in self.desserts:
                if dessert.name == element.name:
                    self.desserts.remove(dessert)
                    return
            raise CartePizzeriaException("Le dessert n'existe pas")
        raise CartePizzeriaException(
            "L'élément n'est pas une pizza, une boisson ou un dessert")


class CartePizzeriaException(Exception):
    pass
