import requests
import json

def get_user_info(username):
    if username == "":
        print("Username cannot be empty.")
        return
    
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data = response.json()
        return {
            "login": data.get("login"),
            "public_repos": data.get("public_repos")
        }


user_data = get_user_info("octocat")
if user_data is not None:
    with open("us_info.json", "w") as f:
        json.dump(user_data, f, indent=4)