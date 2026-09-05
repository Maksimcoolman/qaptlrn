import requests
import json
from getpass import getpass
# res = requests.get("https://api.github.com/users/octocat")
# # print(res.text)
# print(res.headers)
# query = {'q': 'Forest', 'order': 'popular', 'min_width': '1000', 'min_height': '800'}
# url = "https://pixabay.com/en/photos/"
# req = requests.get(url, params=query)
# print(req.url)

# resp = requests.get("https://api.github.com/user", auth=('username', getpass()))
# print(resp.json())

def get_github_user_info(username):
    if username == "":
        print("Username cannot be empty.")
        return

    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data = response.json()
        return {
            "login": data.get("login"),
            "id": data.get("id"),
            "public_repos": data.get("public_repos"),
            "created_at": data.get("created_at")
        }
        
    elif response.status_code == 404 or response.status_code == 401:
        print("User not found or access forbidden.")

user_data = get_github_user_info("d")
if user_data is not None:
    with open("user_info.json", "w") as f:
        json.dump(user_data, f, indent=4)




