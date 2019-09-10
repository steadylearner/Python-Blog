# 2. https://pygithub.readthedocs.io/en/latest/examples/Repository.html#create-a-new-file-in-the-repository

from settings import GITHUB_TOKEN
from github import Github

import sys

g = Github(GITHUB_TOKEN)

# https://github.com/steadylearner/posts
repo = g.get_repo("steadylearner/blog")

filepath = sys.argv[1]

print(f"Do you really want to create {colored(filepath, attrs=['bold'])}?(n if you don't want it)")

response = input()

# Verify the repository folder exist here?

if response.startswith("n"):
    print(f"\nIt won't create {filepath}.")
else:
    f = open(filepath, "r")
    if f.mode == "r":
        contents = f.read()
        if len(contents) == 0:
            print("The filepaths shouldn't be empty. Verify it has some codes in it first.")
            # Otherwise, it will show
            # The update filepath is {new}
        else:
            repo.create_file(filepath, f"create {filepath}", contents, branch = "master")
            print(f"You submitted {filepath} to GitHub\n")
            print(f"The contents is \n {contents}")

# repo.CRUD(<filepath>, <commit>, <contents>, <branch>)
# filepath is from sys.argv from CLI and commit part will use it also
# contents will be from the file with the same name
# branch will be master normally and static.



