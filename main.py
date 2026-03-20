from PLATFORMS.github import fetch_github_profile #importing function from github.py
from narrator import generate_summary,generate_audio
from PLATFORMS.instagram import fetch_instagram_profile 
from PLATFORMS.linkedin import fetch_linkedin_profile
import webbrowser

print("-"*45)
print("Social media profile narrator / reviewer 😊")#welcome
print("-"*45)

choices = ["1.github","2.instagram","3.linkedin"] #options user can choose only from these
print("Select the platform You want to continue with")
for choice in choices:
    print(choice)

user_input = input("Enter the platform you  want to continue with [1-3] : ")#user"s choice to continue
if user_input not in ["1","2","3"]:
    print("You have filled wrong information")
else:
    print("let's continue")


# calling the  function
if user_input == "1":
    user_username = input("Enter git hub user name here [correct!!] : ")
    profile = fetch_github_profile(user_username)
    #we will fetch data from git hub
    summary = generate_summary(profile)
    generate_audio(summary)
    exit()

elif user_input== "2":
    user_username = input("Enter instagram profile name here (correct!!)[instruction:- program will not run if you will  add wrong username ] : ")
    
    print("go to your instagram profile and copy your bio and paste it here for better review")
    url = f"https://www.instagram.com/{user_username}/?hl=en"
    webbrowser.open(url)
    if not user_username:
        print("You have entered wrong username")
        exit()
    


    
    user_input = input("press enter when you are back here :  ")
    user_bio= input("Write your instagram bio for getting reviewed if not press [q] : ")

    if user_bio == "q":
        print("skip")
        None
     

    else:
        print("Nice bio lets review it ")

    profile = fetch_instagram_profile(user_username,user_bio)
    summary = generate_summary(profile)
    generate_audio(summary)
    exit()

    
elif user_input == "3":
    user_username = input("Enter linkedin username here : ")
    print("go to your linkedin proifile and copy your bio and other details and paste it here to get reviewed your profile better .")
    url = f"https//www.linkedin.com/in/{user_username}/"
    webbrowser.open(url)
    if not user_username:
        print("You have entered wrong username")
        exit()
    
    user_input = input ("press enter when you are back here : ")
    user_bio = input("Enter your linkedin bio here [press q for quit] :")
    if user_bio == "q":
        print("skip")
    else:
        print("Nice bio let's review it ")
    user_aim = input("What is the aim of your linkedin profile ? [e.g. looking for job, looking for connections, sharing knowledge etc.]  ")
    profile = fetch_linkedin_profile(user_username,user_bio,user_aim)

    summary = generate_summary(profile)
    generate_audio(summary)
    exit()



    




    

