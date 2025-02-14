from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=None, id=None, width=0, length=0):
        super().__init__(condition=condition, id=id)
        self.width = width
        self.length = length


    def __str__(self):
        return f"{super().__str__()} It takes up a {self.width} by {self.length} sized space."
