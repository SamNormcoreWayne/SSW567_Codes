import requests
import json


class GithubReader():
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.repos = dict()
        self.repo_url = "https://api.github.com/users/{}/repos".format(self.user)
        self.url_respond = str()
        self.repo_commits_num = dict()
        self.get_repos()

    @staticmethod
    def git_repo_api_decoder_id_reponame(git_json_dic):
        try:
            tp = (git_json_dic["id"], git_json_dic["name"])
        except KeyError:
            pass
        else:
            return tp

    def get_respond(self, url):
        try:
            req = requests.get(url, auth=(self.user, self.pwd))
        except requests.exceptions.MissingSchema:
            print("URL wrong")
            self.url_respond = None
            url = input("Please input the right url: ")
            return False
        else:
            self.url_respond = req
            return True

    def get_repos(self):
        while(self.get_respond(self.repo_url)):
            break
        # print(self.url_respond.status_code)
        # print(self.url_respond.encoding)
        rep_js = self.url_respond.text
        # print(rep_js)
        repo_lst = json.loads(rep_js, object_hook=GithubReader.git_repo_api_decoder_id_reponame)
        for repo_id, repo_name in repo_lst:
            # print(repo_id, repo_name)
            self.repos[repo_id] = repo_name

    def get_commits(self):
        for repo_name in self.repos.values():
            commits_url = "https://api.github.com/repos/{id}/{repo}/commits".format(id=self.user, repo=repo_name)
            while(self.get_respond(commits_url)):
                break

            cmt_js = self.url_respond.json()
            com_num = len(cmt_js)
            # print(repo_name, len(cmt_js))
            self.repo_commits_num[repo_name] = com_num
        return self.repo_commits_num

def main():
    username = input("Input user name: ")
    pwd = input("Input password: ")

    sam_repo = GithubReader(user=username, pwd=pwd) 
    com_dic = sam_repo.get_commits()
    print(list(com_dic.items()))
    for repo_name, com_num in com_dic.items():
        print("Repository name: {}, commits number: {}".format(repo_name, com_num))

if __name__ == '__main__':
    main()