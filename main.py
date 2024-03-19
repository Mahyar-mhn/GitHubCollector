import requests
from pprint import pprint


def get_repositories(language, num_repo):
    repositories = []
    page = 1
    while len(repositories) < num_repo:
        url = f"https://github.com/search?q={language}&type=repositories&s=stars&o=desc&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            page_repos = data['payload']['results'][:num_repo]
            repositories.extend(page_repos)
            pprint(page_repos)
            page += 1
        else:
            print(f"Error: {response.status_code}")
            return []
        return repositories


language = input("Please enter your desired language: ")

num_repo = int(input("Please enter number of repositories: "))

repositories = get_repositories(language, num_repo)

