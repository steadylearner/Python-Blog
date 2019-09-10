# Use __init__.py for the file name if you want to publish the package.

from github import Github
from settings import GITHUB_TOKEN

from termcolor import colored

# print(GITHUB_TOKEN)

## 3. help(enumerate)
g = Github(GITHUB_TOKEN)

you =  g.get_user()
repos = you.get_repos()
number_of_repos = repos.totalCount

colored_user_name = colored(you.name, attrs=['bold'])
colored_number_of_repos = colored(number_of_repos, "green")

print(f"\nYou({colored_user_name}) have {colored_number_of_repos} GitHub repositories.\n")

for num, repo in enumerate(repos, start = 1):
    print(
        colored(f"{str(num)}. {repo.name}", "blue")
    )

rust = g.get_repo("steadylearner/Rust-Full-Stack")

colored_rust_repo_star = colored(rust.stargazers_count, "yellow", attrs=['bold'])
colored_rust_repo_total_views = rust.get_views_traffic().get("count", "none")

# help(dict.get)
print(f"\n{colored_rust_repo_star} stars in Rust-Full-Stack repository with {colored_rust_repo_total_views} views in total.")

# 2.
## print("You have {} GitHub repositories.\n".format(number_of_repos))

## print("They are\n")
## for repo in repos:
##    print(repo.name)

## 1.
## for repo in g.get_user().get_repos():
##    print(repo.name)
