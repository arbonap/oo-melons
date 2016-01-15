from random import randint
"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    """Serves as a base class and refractor for class DomesticMelonOrder 
    and class InternationalMelonOrder"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = randint(5, 9)
        # self.tax = 0


    def get_total(self):
        """Calculate price."""

        # self.base_price = 5

        if self.species == "Christmas":
            # Christmas = 1.5 * base_price
            total = (1 + self.tax) * self.qty * (self.base_price * 1.5)
        else:
            total = (1 + self.tax) * self.qty * self.base_price
        return total


# DO WE IMPORT RANDOM 

    # def get_base_price(self):
    # #     """Splurge pricing"""
    #     base_price = 5 
    # #     self.base_price = randint(5, 9)

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True 


class DomesticMelonOrder(object):
    """A domestic (in the US) melon order."""

    # def __init__(self, species, qty):
    def __init__(self):
        """Initialize melon order attributes"""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True


class InternationalMelonOrder(object):
    """An international (non-US) melon order."""


    def __init__(self, country_code):
    # def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17


    # def __init__(self, name):
    #     return super ()

    def get_total(self):
    #     """Calculate price."""

        if self.qty < 10:
            # Christmas = 1.5 * base_price
            # total = ((1 + self.tax) * self.qty * base_price) + 3
            total = super(InternationalMelonOrder, self).get_total() + 3
        else:
            total = super(InternationalMelonOrder, self).get_total()

        return total 

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True 

    def get_country_code(self):
        """Return the country code."""

        return self.country_code





class GovernmentMelonOrder(AbstractMelonOrder):



    def __init__(self, country_code):
    # def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # self.species = species
        # self.qty = qty
        self.passed = False
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0


    def inspect_melons(self,passed):
        """Set shipped to true."""

        self.passed = passed

     # self.passed = True 
