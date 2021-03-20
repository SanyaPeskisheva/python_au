import requests
import json

TASK_PREFIXES = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS', 'ITERATOR']
GROUPS = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Fixed', 'Moved']
TOKEN = 'acb64973e90e06d2a448e194c3a64c5fae4cc066'

def prepare_headers ():
    return {'Authorization': 'Token {}'.format(TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"}

def get_all_user_prs (user_login, repos_name, pr_state):
    url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repos_name, pr_state)
    all_prs = requests.get(url, headers = prepare_headers())
    return all_prs

def get_all_pr_commits (pr):
    url = pr['commits_url']
    all_cs = requests.get(pr['commits_url'], headers = prepare_headers())
    return all_cs

def check_prefixes (title):
    title = title.split()
    prefix = title[0].split('-')
    if len(prefix) == 2:
        group = prefix[1]
        prefix = prefix[0]
        if group in GROUPS:
            if prefix in TASK_PREFIXES:
                return 'everythings is ok'
            else:
                return 'wrong prefix'
        else:
            return 'wrong group'
    else:
        return 'everythings is wrong' 

def send_pr_comment (pr, message_error):
    intelligence = {'body': message_error,
                    'path': requests.get(pr['url'] + '/files', headers = prepare_headers()).json()[0]['filename'],
                    'position': 1,
                    'commit_id': pr['head']['sha']}
    r = requests.post(pr['url'] + '/comments', headers = prepare_headers(), json = intelligence)
    print(r.json())

def verify_pr (pr):
    comments = []
    if len(comments) != 0:
        send_pr_comment(pr, '/n/n'.json(comments))
    if len(check_prefixes(pr['title'])) > 3:
        comment = check_prefixes(pr['title']) + 'in pull request title'
        comments.append(comment)
    for commit in (get_all_pr_commits(pr)):
        if len(check_prefixes(commit['message'])) > 3:
            comment = check_prefixes(commit['message']) + 'in commit message'
            comments.append(comment)
  
def main ():
    user_login = 'SanyaPeskisheva'
    repos_name = 'python_au'
    pr_state = 'open'
    for pr in (get_all_user_prs(user_login, repos_name, pr_state)).json():
        verify_pr (pr)
