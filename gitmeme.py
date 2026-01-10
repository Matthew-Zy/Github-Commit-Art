from datetime import datetime, timedelta

from typing import List
import random
import subprocess
import sys

file_name: str = "amongla.txt"
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

def make_commit(days_ago: int):
    with open(file_name, "a"):
        