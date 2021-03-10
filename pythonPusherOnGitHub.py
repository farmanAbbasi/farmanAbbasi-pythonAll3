import github3

import gzip
with open('githubPass.txt','r') as ghp:
    pwd=ghp.read()

gh = github3.login(username='farmanAbbasi', password=pwd)
sigmavirus24 = gh.me()
print(sigmavirus24.name)

file_info='C:/Users/moabbasi/Desktop/testing/export_file_1.zip'


repository = gh.repository('farmanAbbasi', 'testGithubPush')
with gzip.GzipFile(file_info) as f:
    text = f.read()
repository.create_file(
path=file_info,
message='Start tracking',
content=text)



