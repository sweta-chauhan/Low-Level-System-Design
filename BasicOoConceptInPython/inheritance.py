"""
In Python, getters and setters are not the same as those in other object-oriented programming languages.
"""

'''
Type 1: Normal Setter and Getter
'''


class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


'''
Type 1: Setter and Getter using property decorator 
'''


class Person_With_Property_Decor:
    def __init__(self, name):
        self.name: str = name
        self.age: int = 0

    @property
    def get_name(self):
        return self.name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age


"""
Inheritance: Inheritance is an important aspect of the object-oriented paradigm. 
-----------  Inheritance provides code reusability to the program because we can use an 
existing class to create a new class instead of creating it from scratch.
"""
'''
Multilevel Inheritance
'''


class Officer(Person):
    """
        Officer IS-A Person
    """

    def __init__(self, name, age, posting_location, experience_year):
        self.__posting_location = posting_location
        self.__experience_year = experience_year

        Person.__init__(name, age)

    @property
    def can_rule(self):
        return True


class IAS(Officer):
    """
        IAS IS-A Officer
    """

    def __init__(self, name, age, posting_location, experience_year, designation):
        self.__designation = designation

        Officer.__init__(name, age, posting_location, experience_year)


class Organisation:
    """
    It has owner which is object of class Person so it is carrying `HAS-A-RELATION`
    """

    def __init__(self, name, owner):
        self.name: str = name
        self.owner: Person = owner

    def ruled_by(self):
        return f"Owned by {self.owner}."


'''
Multiple Inheritance
'''


class GlassProd:
    def __init__(self, name, price, size):
        self.g_name = name
        self.g_price = price
        self.g_size = size


class SteelProd:
    def __init__(self, name, price, size):
        self.s_name = name
        self.s_price = price
        self.s_size = size


class Window(GlassProd, SteelProd):
    def __init__(self, window_name, glass_name, glass_price, g_size, steel_name, steel_price, s_size):
        self.__window_name = window_name

        GlassProd.__init__(self, glass_name, glass_price, g_size)
        SteelProd.__init__(self, steel_name, steel_price, s_size)

    def build_one(self):
        if self.__window_name == "GLASS":
            return f"GLASS window price {self.g_size*self.g_price}"

        if self.__window_name == "STEEL":
            return f"STEEL window price {self.s_size * self.s_price}"

        else:
            return f"STEEL and GLASS window price is {self.s_size//2 * self.s_price + self.g_size//2 * self.g_price}"


