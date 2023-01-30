import git
repo = git.Repo('https://github.com/shkim-secure/crawler')
repo.remotes.origin.pull()

#바뀐거확인
current = repo.head.commit
repo.remotes.origin.pull()
if current != repo.head.commit:
    print("It changed")

