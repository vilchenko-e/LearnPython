class Element:
    def __init__(self):
        self.name = None
        self.reactions = {}  # {other_element_name: result_class}
    
    def __add__(self, other):
        result_class = self.reactions.get(other.name)
        if result_class:
            return result_class()
        return None


class Earth(Element):
    def __init__(self):
        super().__init__()
        self.name = "Earth"
        self.reactions = {
            "Fire": Lava,      # Earth + Fire = Lava
            "Water": Mud,      # Earth + Water = Mud
        }

class Fire(Element):
    def __init__(self):
        super().__init__()
        self.name = "Fire"
        self.reactions = {
            "Earth": Stone,    # Fire + Earth = Stone
            "Water": Steam,    # Fire + Water = Steam
            "Air": Energy,     # Fire + Air = Energy
        }

class Water(Element):
    def __init__(self):
        super().__init__()
        self.name = "Water"
        self.reactions = {
            "Fire": Steam,     # Water + Fire = Steam
            "Earth": Mud,      # Water + Earth = Mud
        }

class Air(Element):
    def __init__(self):
        super().__init__()
        self.name = "Air"
        self.reactions = {
            "Fire": Energy,    # Air + Fire = Energy
            "Water": Cloud,    # Air + Water = Cloud
        }


# DERIVED ELEMENTS (4)
class Lava(Element):
    def __init__(self):
        super().__init__()
        self.name = "Lava"
        self.reactions = {
            "Water": Stone,    # Lava + Water = Stone
            "Air": Obsidian,   # Lava + Air = Obsidian
        }

class Stone(Element):
    def __init__(self):
        super().__init__()
        self.name = "Stone"
        self.reactions = {}    # No further reactions

class Mud(Element):
    def __init__(self):
        super().__init__()
        self.name = "Mud"
        self.reactions = {}    # No further reactions

class Steam(Element):
    def __init__(self):
        super().__init__()
        self.name = "Steam"
        self.reactions = {}    # No further reactions

class Energy(Element):
    def __init__(self):
        super().__init__()
        self.name = "Energy"
        self.reactions = {}    # No further reactions

class Cloud(Element):
    def __init__(self):
        super().__init__()
        self.name = "Cloud"
        self.reactions = {}    # No further reactions

class Obsidian(Element):
    def __init__(self):
        super().__init__()
        self.name = "Obsidian"
        self.reactions = {}    # No further reactions
fire = Fire()
water = Water()
print((fire+water).name)
