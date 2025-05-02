import requests


code_print = "9a17aa22687349195fe69a5855cc4f5c53e38624fcad4c2099290215bac4fa74"

def search_github_code(query, token):
    url = "https://api.github.com/search/code"
    headers = { 
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {"q": query}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 422:
        print("Error 422: Query is invalid or improperly formatted.")
    else:
        print(f"GitHub API error: {response.status_code}")
    return None

def search_github_code1(query, token):
    url = "https://api.github.com/search/code"
    headers = { 
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {"q": query}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 422:
        print("Error 422: Query is invalid or improperly formatted.")
    else:
        print(f"GitHub API error: {response.status_code}")
    return None

def search_github_code2(query, token):
    url = "https://api.github.com/search/code"
    headers = { 
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {"q": query}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 422:
        print("Error 422: Query is invalid or improperly formatted.")
    else:
        print(f"GitHub API error: {response.status_code}")
    return None

if __name__ == "__main__":
    search_github_code()
