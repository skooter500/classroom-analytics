import csv
from pathlib import Path

class Assignment:
    """Represents a classroom assignment"""
    def __init__(self, organisation, roster_filename, prefix):
        self.roster_path = Path(roster_filename)
        self.prefix = prefix
        self.organisation = organisation

    def roster(self):
        with self.roster_path.open('r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = row['identifier']
                github_username = row['github_username']
                if github_username:
                    repo_name = f"{self.prefix}-{github_username}"
                    yield student, github_username, self.organisation.repo(repo_name)
                else:
                    yield student, github_username, None
