def Error_String_With_Arrows(text, pos_start, pos_end):
    result = ''

    # Calculate indices
    index_start = max(text.rfind('\n', 0, pos_start.index), 0)
    index_end = text.find('\n', index_start + 1)
    if index_end < 0: index_end = len(text)

    # Generate each line
    line_count = pos_end.line - pos_start.line + 1
    for i in range(line_count):
        # Calculate line columns
        lin = text[index_start:index_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(lin) - 1

        # Append to result
        result += lin + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        # Re-calculate indices
        index_start = index_end
        index_end = text.find('\n', index_start + 1)
        if index_end < 0: index_end = len(text)

    return result.replace('\t', '')
