from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=None, id=None, fabric="Unknown"):
        super().__init__(condition=condition, id=id)
        self.fabric = fabric

    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."
