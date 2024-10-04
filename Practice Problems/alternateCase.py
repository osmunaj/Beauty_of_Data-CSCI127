def alternate_case (sentence, start = 0):
    result = ""
    upper = True
    for i in range(len(sentence)):
        if i < start:
            result = result + sentence[i]
        elif upper:
            result = result + sentence[i].upper()
        else:
            result = result + sentence[i].lower()
        upper = not upper
    return result

print(alternate_case("abcdefghij"))
print(alternate_case("abcdefghij", 2))
print(alternate_case("abcdefghij", 3))

print(alternate_case("ABCDEFGHIJ"))
print(alternate_case("ABCDEFGHIJ", 3))
print(alternate_case("ABCDEFGHIJ", 4))