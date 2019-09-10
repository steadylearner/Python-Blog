# 4. https://pygithub.readthedocs.io/en/latest/examples/Repository.html#delete-a-file-in-the-repository

from settings import GITHUB_TOKEN
from github import Github

import sys
import os

g = Github(GITHUB_TOKEN)

# https://github.com/steadylearner/posts
repo = g.get_repo("steadylearner/blog")

filepath = sys.argv[1]

print(f"Do you really want to delete {colored(filepath, attrs=['bold'])}?(n if you don't want it)")
response = input()

if response.startswith("n"):
    print(f"\nIt won't delete {colored(filepath, attrs=['bold'])}.")
else:
    os.remove(filepath)
    print(f"{colored(filepath, attrs=['bold'])} removed")
    contents = repo.get_contents(filepath, ref="master")
    repo.delete_file(contents.path, f"remove {filepath}", contents.sha, branch="master")
    print("It is also removed from the GitHub")
