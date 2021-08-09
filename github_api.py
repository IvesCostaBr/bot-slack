
from github import Github


class GitHubManager:
    def __inti__(self, token=None, login=None, password=None):
        self.__token = token
        self.__login = login
        self.__password = password
    
    def get_pull_list(self, repos):
        pass


github = Github("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")

for c in github.get_user().get_repos():
    print(c.get_pulls)