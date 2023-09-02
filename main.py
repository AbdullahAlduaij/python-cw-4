def my_name():
    print("My name is Fatima")

my_name()

def my_meal(food, drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal("pizza", "cola")

def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

result1 = by_three(6) 
print(result1) 

result2 = by_three(7)  
print(result2) 



