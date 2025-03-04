import csv
from pathlib import Path
from datetime import datetime

# from github_classroom import get_weeks
from github_classroom.config import assignment_from_config
from github_classroom import get_weeks

# setup some configuration
output_path = Path('weekly_commits.csv')

assignment = assignment_from_config('config.ini')

# We are fixing the range of dates in this example
start = datetime(2021, 10, 4).date()
weeks = get_weeks(start, 23)

defaults = {week : 0 for week in weeks}

with output_path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['identifier', 'github_username', *weeks], extrasaction='ignore')
    writer.writeheader()

    for identifier, github_username, repo in assignment.roster():
        print(identifier + "\t")
        
        row = defaults.copy()
        row['identifier'] = identifier
        row['github_username'] = github_username
        if repo:
            print("All commits by week:\n")
            print(str(repo.all_commits_by_week()) + "\n\n")
            print("All commits:\n")

            print(str(repo.all_commits())  + "\n\n")
            print("Commit Count By Week:\n")
            print(str(repo.commit_count_by_week()) + "\n\n")
            
            print("Weeks:\n")            
            print(str(repo.commit_weeks())  + "\n\n")
            row.update(dict(repo.commit_count_by_week()))
        writer.writerow(row)