############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

    def __repr__(self):
        return self.code


def make_melon_types():
    """Returns a list of current melon types."""

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")

    pairing_dict = {musk: 'mint', cas: ['strawberries', 'mint'],
                  cren: 'prosciutto', yw: 'ice cream'}
    
    all_melon_types = []
    
    # now we can call musk.pairings and it should have "mint".
    for melon in pairing_dict:
        melon.add_pairing(pairing_dict[melon])
        all_melon_types.append(melon)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        if type(melon.pairings[0]) == list:
            for food in melon.pairings[0]:
                print(f"- {food}")
        else:
            print(f"- {melon.pairings[0]}")
        print()



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # {"musk": musk, "cas": cas, "cren": cren, "yw": yw}
    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    return melon_dict

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
