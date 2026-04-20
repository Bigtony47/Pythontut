EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
print(elapsed_time_in_minutes(3, 20))
"""Calculate the elapsed cooking time.              
        :param number_of_layers: int - the number of layers in the lasagna.
        :param elapsed_bake_time: int - elapsed cooking time.
        :return: int - total time elapsed (in minutes) preparing and cooking.
        this Function takes two integers representing the number of lasagna
layers and the
````````time already spent baking and calculates the total elapsed minutes
spent cooking the
        lasagna.
       """ 
print("Bake time remainig dor 30 mins:")
print(bake_time_remaining(30))

print("Prep time for 3 layers:")
print(preparation_time_in_minutes(3))

print("Total time for 3 layers:")
print(preparation_time_in_minutes(3))

print("Total elapsed time (3 layers, 20 mins in oven):")
print(elapsed_time_in_minutes(3, 20))

# I really hope i could make you proud, big bro.