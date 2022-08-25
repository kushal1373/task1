

'''
Iam currently learning 

'''

f_name=input("Firstname")   
s_name=input("Secondname")

def full_name_generator(first_name,second_name):
    full_name = f"{first_name} {second_name}"
    return full_name

print("Your full name is:", full_name_generator(f_name,s_name))


#string formatting
first=1
second=0
third=1
fourth=4
print(f"My {first}  name {second} is {third}  def {fourth}")

phone_num = 998343898
print(f"Your phone number is {phone_num}")

#len function
length_of_this = len("Education")
print(length_of_this)