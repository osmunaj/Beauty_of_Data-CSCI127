def blend(stuff, time):
    if stuff != [] and time > 0:
        result = (stuff, " blended for ", time, " seconds")
    else:
        result = "problem with blending..."
    return result

def main():
    ingredients1 = ['berries', 'milk', 'ice']
    smoothie = blend(ingredients1, 60)
    print(smoothie)

    ingredients2 = ['cookies', 'milk','ice cream']
    milkshake = blend(ingredients2, 30)
    print(milkshake)

main()