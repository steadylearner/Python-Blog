# 1.

# https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-a-specific-content-file

from settings import GITHUB_TOKEN
from github import Github
import sys

# print("This is the name of the python script: {}".format(sys.argv[0]))
# print("The total number of CLI arguments is {}".format(len(sys.argv)))
# print("They are: {}".format(str(sys.argv)))

g = Github(GITHUB_TOKEN)

# https://github.com/steadylearner/posts
repo = g.get_repo("steadylearner/blog")
filepath = sys.argv[1]

byte = repo.get_contents(filepath).decoded_content # class byte
print(byte.decode("utf-8")) # class str
