
print("pälä pälä")

def do_nothing():
    pass

do_nothing()


def print_list_of_numbers(start, end):
    print(f"Tulostettava väli: {start}, {end}")
    for i in range(start, end, 1):
        print(i)

print_list_of_numbers(1, 5)
print_list_of_numbers(7, 11)