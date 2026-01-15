from datetime import datetime, timedelta
from typing import List, Dict
import random, copy
import sys, os, subprocess
from pathlib import Path
from PIL import Image
from math import floor

file_name: str = "amongla.txt"
path = Path("hey")
path.parent.mkdir(exist_ok=True, parents=True)

Random_commit_msg: List[str] = [
    "Pikachu", "Obama", "Sussy AMogus"
]
Random_content_msg: List[str] = [
    "wow", "I love", "The mona"
]

def make_commit(date: datetime):
    # date = datetime.today()
    dateStr = date.strftime("%a %b %d %I:%M %Y")
    print(dateStr)
    with open(file_name, "a+") as f:
        f.write("soy")
    subprocess.run(["git", "add", file_name])
    # subprocess.run(["git", "commit", file_name, f'{days_ago} day ago', "-m", "random"]) # both should theoretically work
    subprocess.run(["git", "commit", "--amend", "-m", "some stuff", f'--date="{dateStr}"',])

# 

def make_commits_for_year(year: int, days_to_commit: Dict[int, int]):
    first_day_of_year: datetime = datetime(year=year, month=1,day=1)
    print(first_day_of_year.isoweekday()) # 1 for monday and 7 for sunday

    # commit_day: datetime = copy.deepcopy(first_day_of_year)
    for day in days_to_commit:
        commit_day: datetime = datetime(year=year, month=1, day=1)
        # peak engineering this line below like literally the most goated engineering ever to exist
        # because my engineering is so peak in days_to_commit dict 0 is january 1st and everything is pushed back 1 day
        commit_day = commit_day + timedelta(days=day)
        for i in range(days_to_commit[day]):
            commit_day = commit_day + timedelta(minutes=2)
            # make_commit(commit_day)
            pass
        
    print(first_day_of_year)


# returns a flattened array of the grayscale values of in "sort of" the chronological order for github commits
def open_image(file_path: str) -> List[int]:
    img = Image.open(file_path, mode='r')
    img = img.convert('L')
    # height, width = 7, 53

    print(img.width, img.height)
    gs_arr: int = []
    for x in range(0, img.width):
        for y in range(0, img.height):
            #print(img_arr[y, x])
            gs_arr.append(img.getpixel((x, y)))
    return gs_arr

def calculate_commits(pixels: List[int], max_commit_a_day: int = 10):
    commit_arr: List[int] = []

    for p in pixels:
        normalized = p * (max_commit_a_day / 256) + 1
        # adding the one to prevent divide by 0 and also cause i cant make a proper math equation
        value = max_commit_a_day / normalized
        commit_arr.append(floor(value))
    
    return commit_arr

def create_days_to_commit(year: int, commit_arr: List[int] = None):
    if commit_arr is None:
        return
    first_day_of_year = datetime(year=year, month=1, day=1)
    last_day_of_year = datetime(year=year, month=12, day=31)
    day_week: int  = first_day_of_year.isoweekday() % 7 # make sunday day 0 instead
    last_day_week: int = abs(last_day_of_year.isoweekday()%7 - 6) #saturday = 0, and sunday = 6
    commit_arr = commit_arr[day_week: len(commit_arr) - last_day_week] 
    
    # convert to a dict and then filter out key value pairs where the value is 0
    b = {index: value for index, value in enumerate(commit_arr)}
    b = {k: v for k, v in b.items() if (lambda val: val != 0)(v)}
    return b

ima = open_image("zy.png")
c = calculate_commits(ima)

print(len( create_days_to_commit(2024, c)))
