from io import StringIO
def count_lines(stream):
    lines = 0
    for s in stream:
        lines += 1
    return lines 
string_stream = StringIO("first\nsecond\nthird")
print(count_lines(string_stream))
