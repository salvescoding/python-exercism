def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1 and char != " " and char != "-":
            return False
    return True

