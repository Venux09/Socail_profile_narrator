import requests#request module 




def fetch_github_profile(user_username):
    """
    Fetches GitHub profile data using GitHub API.
    Called from main.py with the username entered by user.
    
    Args:
        username (str): GitHub username e.g. 'torvalds'
    """
    response = requests.get(f"https://api.github.com/users/{user_username}")
    #checking if user has put wrong user_username
    if response.status_code == 404:#it is status of code for error
        print("user not found")
        return None#nothisng return
    elif response.status_code == 200:#it is status of code for error
        print("user founded ")
        data = response.json()#converting data to dictionary so it can be readed 
        name = data["name"]
        bio = data["bio"]
        location = data["location"]
        repository = data["public_repos"]
    
        return {
    "name": name,
    "bio": bio,
    "location": location,
    "repos": repository
}

        
    elif response.status_code == 500:#it is status of code for error
        print("code is not working ")
        return None
