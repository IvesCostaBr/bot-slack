from github import Github


class GitHubManager:
    def __inti__(self, token=None, login=None, password=None):
        self.__token = token
        self.__login = login
        self.__password = password
    
    def get_pull_list(self, repos):
        pass


github = Github("YOU TOKEN")

for c in github.get_user().get_repos():
    print(c.get_pulls)
