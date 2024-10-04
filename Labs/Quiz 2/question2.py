def main():
    inventory = {"coffee cups":112, "tea pots":37, "sugar bowls":17 }
    inventory["tea pots"] -= 2
    print(inventory["coffee cups"])

    inventory.pop("coffee cups")
    print(inventory)
    inventory["spoons"] = 456
    print(inventory)
    merchandise = inventory.keys()
    print(merchandise)

main()