import Sansam.Error.Errors as error
import Sansam.Interpreter.RunTimeResult as rtr


class Value:
    def __init__(self):
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
        return None, self.illegal_operation(other)

    def subtraction(self, other):
        return None, self.illegal_operation(other)

    def multiplication(self, other):
        return None, self.illegal_operation(other)

    def division(self, other):
        return None, self.illegal_operation(other)

    def exponential(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other):
        return None, self.illegal_operation(other)

    def anded_by(self, other):
        return None, self.illegal_operation(other)

    def ored_by(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_bitand(self,other):
        return None, self.illegal_operation(other)

    def get_comparison_bitor(self,other):
        return None, self.illegal_operation(other)

    def notted(self):
        return None, self.illegal_operation()
    def bitnotted(self):
        return None, self.illegal_operation()

    def execute(self, args):
        return rtr.RunTimeResult().failure(self.illegal_operation())

    def copy(self):
        raise Exception('No copy method defined')

    def is_true(self):
        return False

    def illegal_operation(self, other=None):
        if not other:
            other = self
        return error.RunTimeError(
            self.pos_start, other.pos_end,
            'Illegal operation',
            self.context
        )


