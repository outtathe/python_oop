from validate import *


class Property:

    properties_count = 0

    def __init__(self, owner, price, rent_term, utilities, mortgage, for_rent=True):
        self._owner = validate_owner(owner)
        self._price = validate_price(price)
        self._rent_term = validate_term(rent_term)
        self._utilities = validate_money(utilities)
        self._mortgage = validate_money(mortgage)
        self._for_rent = validate_bool(for_rent)
        self._rented = False
        Property.properties_count += 1

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = validate_owner(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = validate_price(value)

    @property
    def rent_term(self):
        return self._rent_term

    @rent_term.setter
    def rent_term(self, value):
        self._rent_term = validate_term(value)

    @property
    def utilities(self):
        return self._utilities

    @utilities.setter
    def utilities(self, value):
        self._utilities = validate_money(value)

    @property
    def mortgage(self):
        return self._mortgage

    @mortgage.setter
    def mortgage(self, value):
        self._mortgage = validate_money(value)

    @property
    def mortgage_active(self):
        return self._mortgage > 0

    @property
    def has_debt(self):
        return self._utilities > 0

    @property
    def rented(self):
        return self._rented

    def check_utilities(self):
        return self._utilities

    def check_mortgage(self):
        return self._mortgage

    def owner_info(self):
        return self._owner

    def pay_utilities(self, amount):
        amount = validate_money(amount)
        if amount > self._utilities:
            raise ValueError("payment exceeds debt")
        self._utilities -= amount

    def pay_mortgage(self, amount):
        amount = validate_money(amount)
        if amount > self._mortgage:
            raise ValueError("payment exceeds mortgage")
        self._mortgage -= amount

    def rental_contract(self):
        if not self._for_rent:
            raise ValueError("property not for rent")
        if self._rented:
            raise ValueError("already rented")
        self._rented = True

    def close_contract(self):
        if not self._rented:
            raise ValueError("not rented")
        self._rented = False

    def is_available(self):
        return not self._rented

    def total_rent_price(self):
        return self._price * self._rent_term + self._utilities

    def sell_price(self):
        return self._price

    def __eq__(self, other):
        return isinstance(other, Property) and self._owner == other._owner and self._price == other._price

    def __str__(self):
        status = "yes" if self._rented else "no"
        return f"Owner: {self._owner} | Price: {self._price:.2f} | Rented: {status}"

    def __repr__(self):
        return f"Property(owner='{self._owner}', price={self._price}, rent_term={self._rent_term})"
    
#

p = Property('asdfghj', 123456, 6543, 1234567890, 3456789, False)

print(p._owner)
print(p.owner)

