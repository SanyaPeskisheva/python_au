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

def check_author(comment):
    author = comment['user']['login']
    return author

def compare_dates(d1, d2):
    if d1[0] > d2[0]:
        return d1
    elif d1[0] == d2[0]:
        if d1[1] > d2[1]:
            return d1
        elif d1[1] == d2[1]:
            if d1[2] > d2[2]:
                return d1
            elif d1[2] == d2[2]:
                if d1[3] > d2[3]:
                    return d1
                elif d1[3] == d2[3]:
                    if d1[4] > d2[4]:
                        return d1
                    elif d1[4] == d2[4]:
                        if d1[5] > d2[5]:
                            return d1
                        elif d1[5] == d2[5]:
                            return 0 
    return d2

def VERIFICATION_RESULT(comment):
    message = comment['body']
    return (message.startswith('VERIFICATION RESULT'))

def get_time_commit(commit):
    date = commit['commit']['author']['date']
    return date

def get_time_last_comment(all_prs):
    x = ['0', '0', '0', '0', '0', '0']
    for pr in (all_prs):
        comments = requests.get(pr['review_comments_url']).json()
        for comment in comments:
            if comment['user']['login'] == LOGIN:
                new_d = comment['created_at']
                new_d = new_date.split('-')
                new_d.append(new_date[2][:2])
                new_d.append(new_date[2][3:-7])
                new_d.append(new_date[2][6:-4])
                new_d.append(new_date[2][9:-1])
                new_d.pop(2)
                x = compare_dates(x, new_d)
                print(x)

def main ():
    user_login = 'SanyaPeskisheva'
    repos_name = 'python_au'
    pr_state = 'open'
    for pr in (get_all_user_prs(user_login, repos_name, pr_state)).json():
        verify_pr (pr)
