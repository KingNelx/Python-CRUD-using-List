items = []


def display_items():
    if len(items) == 0:
        print(" NO ITEMS FOUND IN THE LIST ")
    else:
        for index, item in enumerate(items):
            print(f"{index + 1}.{item}")
