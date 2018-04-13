"""Classes for melon orders."""
class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, tax, country_code='USA'):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.tax = tax

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        christmas_melons = 7.5
        flat_fee = 0
        if self.species == "Christmas Melon":
            total = (1 + self.tax) * self.qty * christmas_melons + flat_fee
        else:
            total = (1 + self.tax) * self.qty * base_price + flat_fee

        return total
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self,species, qty, country_code):
        super(DomesticMelonOrder, self).__init__(species, qty, .08, country_code)
        order_type = "domestic"
    # tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, 0.17, country_code)
        # self.tax = tax
        order_type = "international"
    
        if qty < 10:
            flat_fee = 3
        else:
            flat_fee = 0

    
