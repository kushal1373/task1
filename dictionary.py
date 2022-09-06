"""

It is always represent in the form of:

my_dictionary = {"key":"Value"}
"""

#why we need dictionary?
#--> To overcome the problem exist in list.
#for eg:
#user_detail=["kushal","Thapa",20,["English","Nepali","Spanish"],9999999999,["jpani","teipani"]]

user_details={
     "first_name":"Kushal",
      "last_name":"Thapa",
      "language_spoken":["English","Nepali","Chinese"],
      "contact":9810061707


}
print(user_details["first_name"])

for key,value in user_details.items():
    print(f"The key is:{key} and its value is: {value}")

for key in user_details.items():
    print(f"The key is:{key}")

for value in user_details.items():
    print(f"The value is:{value}")
    
