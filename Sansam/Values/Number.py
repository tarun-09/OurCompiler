import Values.Boolean as boolean
import Error.Errors as error


class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def addition(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    def subtraction(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

    def multiplication(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, error.RunTimeError(
                    other.pos_start, other.pos_end, "विभाजन सह शून्य दोष", self.context
                )

            return Number(self.value / other.value).set_context(self.context), None

    def exponential(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value == other.value).set_context(self.context), None

    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value != other.value).set_context(self.context), None

    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value < other.value).set_context(self.context), None

    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value > other.value).set_context(self.context), None

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value <= other.value).set_context(self.context), None

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value >= other.value).set_context(self.context), None

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(self.value and other.value).set_context(self.context), None

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(self.value or other.value).set_context(self.context), None

    def notted(self):
        return boolean.Boolean(1 if self.value == 0 else 0).set_context(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.value)
