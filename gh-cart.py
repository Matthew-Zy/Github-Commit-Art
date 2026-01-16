from datetime import datetime, timedelta
from typing import List, Dict
import random, argparse, subprocess, io
from pathlib import Path
from math import floor

from PIL import Image



Random_commit_msg: List[str] = [
    "Pikachu", "Obama", "Sussy AMogus"
]
Random_content_msg: List[str] = [
    "wow", "I love", "The mona", "AMONGUS", "I LOVE AMONGUS"
]

def get_random_phrase(Phrases: List[str]) -> str:
    # not needed but i might want users to give files as random texts n stuff
    if len(Phrases) == 0:
        return "bro"
    r = random.randint(0, len(Phrases)-1)
    return Phrases[r]

def make_commit(date: datetime, file_path: Path):
    dateStr = date.strftime("%a %b %d %I:%M %Y")
    print(dateStr)
    with open(file_path, 'a+') as f:
        f.write(get_random_phrase(Random_content_msg) + '\n')
        
    subprocess.run(["git", "add", file_path], cwd=file_path.parent)
    # subprocess.run(["git", "commit", file_name, f'{days_ago} day ago', "-m", "random"]) # both should theoretically work
    subprocess.run(
        ["git", "commit", "--amend", "-m", get_random_phrase(Random_commit_msg), f'--date="{dateStr}"'],
        cwd = file_path.parent)


def make_commits_for_year(year: int, days_to_commit: Dict[int, int], file_path):
    for day in days_to_commit:
        commit_day: datetime = datetime(year=year, month=1, day=1)
        # peak engineering this line below like literally the most goated engineering ever to exist
        # because my engineering is so peak in days_to_commit dict 0 is january 1st and everything is pushed back 1 day
        commit_day = commit_day + timedelta(days=day)
        for i in range(days_to_commit[day]):
            commit_day = commit_day + timedelta(minutes=2)
            # make_commit(commit_day, file_path)
            pass
        
# returns a flattened array of the grayscale values of in "sort of" the chronological order for github commits
def open_image(file_path: str) -> List[int]:
    img = Image.open(file_path, mode='r')
    img = img.convert('L')
    # height, width = 7, 53

    # print(img.width, img.height)
    gs_arr: int = []
    for x in range(0, img.width):
        for y in range(0, img.height):
            gs_arr.append(img.getpixel((x, y)))
    return gs_arr

def calculate_commits(pixels: List[int], max_commit_a_day):
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


'''
ima = open_image("input_image.png")
c = calculate_commits(ima)

print(len( create_days_to_commit(2024, c)))
'''
def create_commit_dict(img_path: str, year: int, max_commit_per_day: int) -> dict[int, int]:
    img = open_image(img_path)
    img = calculate_commits(img, max_commit_per_day)
    return create_days_to_commit(year, img)
    

def parse_args():
    write_fp = "amongla.txt"
    img_path = "zy.png"
    year = None

    parser = argparse.ArgumentParser(
        prog='Commit art maker',
        usage='python gh-cart.py [year] [option flags]',
        description='Command line tool that gets you more contributions on github',
        epilog='why are you here'
    )
    parser.add_argument('year', type=int)
    parser.add_argument('-mc', '--maxcommits', type=int, default=1, help='max commits a day')
    parser.add_argument('-of', '--outfile', type=str, default="amongla.txt", help='What file to write random commits to')
    parser.add_argument('-i', '--image', type=str, default="input_image.png", help='Input image to base commits off of')
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    args = parse_args()
    print(args)

    c_dict = create_commit_dict(args['image'], args['year'], args['maxcommits'])
    file_path: Path = Path(args['outfile'])
    file_path.parent.mkdir(exist_ok=True, parents=True)

    make_commits_for_year(args['year'], c_dict, file_path)
    print("Successfully made our commits for the year :smiley:")
