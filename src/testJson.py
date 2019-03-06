import json
import os


def read_json_in_docs(filename):
    path = os.path.join(os.getcwd(), 'docs')
    with open(os.path.join(path, filename)) as js:
        k = json.load(js)
        print(filename, ": \n", k)
        return k

def main():
    repo_name = "GitRepoResponse.json"
    cmt_name = "GitCommitResponse.json"
    # a = read_json_in_docs(repo_name)
    # os.system('pause')
    b = read_json_in_docs(cmt_name)
    # print(json.dumps(a))
    os.system('pause')
    print(str(b).replace('\n', '').replace(' ', ''))

main()