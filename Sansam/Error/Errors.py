import Sansam.Error.Error_String_With_Arrows as error_str


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}--> {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.line + 1}'
        result += '\n\n' + error_str.Error_String_With_Arrows(self.pos_start.ftext, self.pos_start,
                                                                             self.pos_end)
        return result


class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'अवैध अक्षर', details)


class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'क्रमभङ्ग', details)


class RunTimeError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, 'चलनकालिकदोष', details)
        self.context = context

    def as_string(self):
        result = self.generate_traceback()
        result += f'{self.error_name}: {self.details}'
        result += '\n\n' + error_str.Error_String_With_Arrows(self.pos_start.ftext, self.pos_start,
                                                                             self.pos_end)
        return result

    def generate_traceback(self):
        result = ''
        pos = self.pos_start
        ctx = self.context

        while ctx:
            result = f' सञ्चिका {pos.fn}, पङ्क्ति {str(pos.line + 1)}, in {ctx.display_name}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent

        return 'Traceback (अधिकतम अपूर्व आहू गत):\n' + result
        # (most recent call last)
