
#returns middle letter in word
def mid(middle):
    if len(middle) % 2 == 0:
        return ""
    else:
        index = len(middle) // 2
        letter = middle[index]
        return letter

#tests
mid("Dog")
mid("Kelvin")
mid("Cat")


