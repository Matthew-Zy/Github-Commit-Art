from datetime import datetime, timedelta

from typing import List
import random
import subprocess
import sys, os
from pathlib import Path

file_name: str = "amongla.txt"
path = Path("hey")
path.parent.mkdir(exist_ok=True, parents=True)

Random_commit_msg: List[str] = [
    "Pikachu", "Obama", "Sussy AMogus"
]
Random_content_msg: List[str] = [
    "wow", "I love", "The mona"
]


today = datetime.today()
print(today.day)
print(today)

print(timedelta(days=today.weekday()))

def make_commit(date: datetime):
    # date = datetime.today()
    dateStr = date.strftime("%a %b %d %I:%M %Y")
    print(dateStr)
    with open(file_name, "a+") as f:
        f.write("soy")
    # subprocess.run(["git", "add", file_name])
    # subprocess.run(["git", "commit", file_name, f'{days_ago} day ago', "-m", "random"]) # both should theoretically work
    # subprocess.run(["git", "commit", "--amend", "-m", "some stuff", f'--date="{dateStr}"',])


def make_commits_for_year(year: int, days_to_commit: List[int], total_commits_to_do: int = 400):
    days = 365
    if year % 4 == 0:
        days = 366
    first_day_of_year = datetime(year=year, month=1,day=1)
    print(first_day_of_year.isoweekday()) # 1 for monday and 7 for sunday
    first_day_of_year = first_day_of_year + timedelta(minutes=1)

    commit_each_day = total_commits_to_do // len(days_to_commit)
    for day in range(1, days+1):
        if day in days_to_commit:
            # do like 10 commits or something
            pass
    print(first_day_of_year)
make_commits_for_year(2024)