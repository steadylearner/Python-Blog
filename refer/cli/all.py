# 5.

# https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-all-of-the-contents-of-the-repository-recursively

from settings import GITHUB_TOKEN
from github import Github
import sys

g = Github(GITHUB_TOKEN)

# https://github.com/steadylearner/posts
repo = g.get_repo("steadylearner/blog")
filepath = sys.argv[1] # posts/Rust

contents = repo.get_contents(filepath)

# help(contents) or IPython

while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        payload = file_content.path
        name = payload.split("/")[-1] # split(".")[0] for list.html and use - for paths in templates
        print(name)
