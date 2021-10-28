batch = int(input())

for n in range(1, batch + 1):
    has_flour = False
    has_eggs = False
    has_sugar = False

    while True:
        product = input()

        if product == 'flour':
            has_flour = True
        elif product == 'eggs':
            has_eggs = True
        elif product == 'sugar':
            has_sugar = True

        if product == 'Bake!':
            if has_flour and has_eggs and has_sugar:
                print(f"Baking batch number {n}...")
                break
            else:
                print(f'The batter should contain flour, eggs and sugar!')


