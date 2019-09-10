# 3. https://pygithub.readthedocs.io/en/latest/examples/Repository.html#update-a-file-in-the-repository

from settings import GITHUB_TOKEN
from github import Github

import sys
import os

g = Github(GITHUB_TOKEN)

# https://github.com/steadylearner/posts
repo = g.get_repo("steadylearner/blog")

filepath = sys.argv[1]

print(f"Do you really want to update {colored(filepath, attrs=['bold'])} in GitHub?(n if you don't want it)")

response = input()

if response.startswith("n"):
    print("\nIt won't update {}.".format(filepath))
else:
    f = open(filepath, "r")
    if f.mode == "r":
        new = f.read()

        old = repo.get_contents(filepath).decoded_content

        # print(type(old)) => byte
        # print(type(new)) => str

        if old == str.encode(new):
            print("The contents is not updated. Edit it first.")
        else:
            contents = repo.get_contents(filepath, ref="master")
            repo.update_file(contents.path, f"update {filepath}", new, contents.sha, branch="master")
            print(f"GitHub updated {filepath}\n")
            print(f"The updated file is \n {new}")

# use for to update all the contents