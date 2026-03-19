



print("-"*45)
print("Social media profile narrator / reviewer 😊")#welcome
print("-"*45)

choices = ["1.github","2.instagram","3.linkedin"] #options user can choose only from these
print("Select the platform You want to continue with")
for choice in choices:
    print(choice)

user_input = input("Enter the platform you  want to continue with [1-3]")#user"s choice to continue
if user_input not in ["1","2","3"]:
    print("You have filled wrong information")
else:
    print("let's continue")


# calling the  function
if user_input == "1":
    user_username = input("Enter git hub user name here [correct!!] : ")
    #we will fetch data from git hub
elif user_input== "2":
    user_username = input("Enter instagram profile name here : ")
    user_bio= input("Write your instagram bio for getting reviewed if not press [q]")
    if user_bio == "q":
        print("skip")
    else:
        print("Nice bio lets review it ")
    # have to add jpg file [profile photo]to get reviewed but this much for now ,or tips to upgrade
    u
elif user_input == "3":
    user_username = input("Enter linkedin username here : ")
    user_bio = input("Enter your linkedin bio here [press q for quit] :")
    if user_bio == "q":
        print("skip")
    else:
        print("Nice bio let's review it ")
    # have to add something like about bio or education details or tips to upgrade


    




    

