import requests


def get_repositories(language, num_repo):
    """
    Fetch repositories from GitHub based on language and number specified.

    Args:
    language (str): Desired programming language.
    num_repo (int): Number of repositories to retrieve.

    Returns:
    list: List of dictionaries containing repository information.
    """
    repositories = []
    page = 1
    while len(repositories) < num_repo:
        url = f"https://github.com/search?q={language}&type=repositories&s=stars&o=desc&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            page_repos = data['payload']['results'][:num_repo]
            repositories.extend(page_repos)
            page += 1
        else:
            print(f"Error: {response.status_code}")
            return []

    return repositories


# Main program execution starts here
language = input("Please enter your desired language: ")
num_repo = int(input("Please enter number of repositories: "))

repositories = get_repositories(language, num_repo)
if repositories:
    output = f"{language}_repositories.txt"
    with open(output, mode="w", encoding="utf-8") as file:
        file.write(f"Top {num_repo} repositories:\n")
        file.write(50 * "*" + "\n")

        for i, repo in enumerate(repositories, start=1):
            file.write(
                f"#{i} {repo['hl_name']} - {repo['hl_trunc_description']}\n"
                f"URL: https://github.com/{repo['repo']['repository']['owner_login']}/{repo['repo']['repository']['name']}\n"
                + 50 * "-" + "\n"
            )
        print(f"Results saved to '{output}'")
else:
    print("No repositories found!")
