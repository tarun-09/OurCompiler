import Sansam.Values.Value as val


class Dictionary(val.Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def copy(self):
        copy = Dictionary(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.elements).replace(':', '~')
