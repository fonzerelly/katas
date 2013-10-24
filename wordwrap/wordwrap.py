class OutOfBounds(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))

def WordWrap (text, column_width):
    if column_width < 1:
        raise OutOfBounds("Can not keep text in a column of size 0");
    if len(text) < column_width:
        return text + "\n"
    else:
        line = text[:column_width]
        if text[column_width] not in [" ", "\t"]:
            line_last_space = ""
            line_last_tab = ""
            try:
                line_last_space = line[:line.rindex(" ")]
            except:
                pass
            try:
                line_last_tab = line[:line.rindex("\t")]
            except:
                pass
            if line_last_space == line_last_tab == "":
                raise OutOfBounds("doof")
            if len(line_last_space) > len(line_last_tab):
                return line_last_space + "\n" + WordWrap(text[len(line_last_space):], column_width)
            else:
                return line_last_tab + "\n" + WordWrap(text[len(line_last_tab):], column_width)
        else:
            return line + "\n" + WordWrap(text[len(line):], column_width)
    raise OutOfBounds
