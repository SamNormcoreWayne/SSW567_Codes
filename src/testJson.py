import json
import os


def read_json_in_docs(filename):
    path = os.path.join(os.getcwd(), 'docs')
    with open(os.path.join(path, filename)) as js:
        print(filename, ": \n", json.load(js))

def main():
    repo_name = "GitRepoResponse.json"
    cmt_name = "GitCommitResponse.json"
    read_json_in_docs(repo_name)
    os.system('pause')
    read_json_in_docs(cmt_name)

main()