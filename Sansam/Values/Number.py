import math

import Sansam.Values.Boolean as boolean
import Sansam.Error.Errors as error
import Sansam.Values.Value as val


class Number(val.Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def addition(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def subtraction(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def multiplication(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, error.RunTimeError(
                    other.pos_start, other.pos_end, "विभाजन सह शून्य दोष", self.context
                )

            return Number(self.value / other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def factorial(self):
        return Number(math.factorial(self.value)).set_context(self.context), None

    def modulus(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, error.RunTimeError(
                    other.pos_start, other.pos_end, "विभाजन सह शून्य दोष", self.context
                )

            return Number(self.value % other.value).set_context(self.context), None

    def exponential(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value == other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value != other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value < other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value > other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value <= other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return boolean.Boolean(self.value >= other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(self.value and other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(self.value or other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def notted(self):
        return boolean.Boolean(1 if self.value == 0 else 0).set_context(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


null = Number(0)
false = Number(0)
true = Number(1)
# math_PI = Number(math.pi)
