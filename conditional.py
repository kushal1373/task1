#conditional statement in python


name= input("Whats your name please? ")
age= int(input("Whats your age please? "))

if age < 0:
    print(f"Invalid Age")

elif age==15:
    print(f"Dear {name}, Your ticket price is: 100 ")
    
elif age>15:
        print(f"Dear {name}, Your ticket price is: 150")

else:
            print(f"Dear {name}, Your ticket price is: 50")


def calc_weight(m,g=10):
    print(f"your weight is: {m*g}N ")

mass = int(input("Please enter your mass:"))
print(calc_weight(mass))


