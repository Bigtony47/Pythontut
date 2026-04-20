EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

elapsed = int(input("How many minutes has it been baking? "))
layers = int(input("How many layers? "))
remaining = bake_time_remaining(elapsed)
prep = preparation_time_in_minutes(layers)
total = elapsed_time_in_minutes(layers, elapsed)

print("Time left:", remaining)
print("Prep time:", prep)
print("Total time:", total)