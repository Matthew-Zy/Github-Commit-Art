from datetime import datetime, timedelta
from typing import List, Dict
import random, argparse, subprocess
from pathlib import Path
from math import floor
from PIL import Image



Random_commit_msg: List[str] = [
    "Pikachu", "Obama", "Sussy AMogus", "this is a commit of all time", "im really funny guys...", "Im voiding it so HARD i love VOIding IT", 
    "sigma skiidi ohio", "god I am so skibidi", "ohio rizzler mew", "MY TOWER BATTLES", "stand ready for my conquesting it"
]
Random_content_msg: List[str] = [
    "wow", "I love", "The mona lisa", "AMONGUS", "I LOVE AMONGUS", "This is... my tower battles", "That's reeftastic", "what the sigma",
    "This is... my epic adventure", "can I get uhhh number 9", "are you sure", "I am marking it so good it feels so good to be marking it"
]

def get_random_phrase(Phrases: List[str]) -> str:
    # not needed but i might want users to give files as random texts n stuff
    if len(Phrases) == 0:
        return "bro"
    r = random.randint(0, len(Phrases)-1)
    return Phrases[r]

def make_commit(date: datetime, file_path: Path):
    dateStr = date.strftime("%a %b %d %I:%M %Y")
    # print(dateStr)
    with open(file_path, 'a+') as f:
        f.write(get_random_phrase(Random_content_msg) + '\n')
    
    repo_dir = file_path.parent
    file_name = file_path.name
    subprocess.run(["git", "add", file_name], cwd=repo_dir)
    # subprocess.run(["git", "commit", file_name, f'{days_ago} day ago', "-m", "random"]) # both should theoretically work
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", get_random_phrase(Random_commit_msg), f'--date="{dateStr}"'],
        cwd = repo_dir)


def make_commits_for_year(year: int, days_to_commit: Dict[int, int], file_path):
    for day in days_to_commit:
        commit_day: datetime = datetime(year=year, month=1, day=1)
        # peak engineering this line below like literally the most goated engineering ever to exist
        # because my engineering is so peak in days_to_commit dict 0 is january 1st and everything is pushed back 1 day
        commit_day = commit_day + timedelta(days=day)
        for i in range(days_to_commit[day]):
            commit_day = commit_day + timedelta(minutes=2)
            make_commit(commit_day, file_path)
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

def calculate_commits(pixels: List[int], max_commit_a_day, randomCommit: bool):
    commit_arr: List[int] = []

    for p in pixels:
        normalized = p * (max_commit_a_day / 256) + 1
        # adding the one to prevent divide by 0 and also cause i cant make a proper math equation
        value = floor(max_commit_a_day / normalized)

        if randomCommit == True:
            value = random.randint(0, value)

        commit_arr.append(value)
    
    return commit_arr

# returns a dictionary of stuff 
def create_days_to_commit(year: int, commit_arr: List[int] = None) -> Dict[int, int]:
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


def create_commit_dict(img_path: str, year: int, max_commit_per_day: int, randomCommit: bool) -> dict[int, int]:
    img = open_image(img_path)
    img = calculate_commits(img, max_commit_per_day, randomCommit)
    return create_days_to_commit(year, img)
    

def parse_args():

    parser = argparse.ArgumentParser(
        prog='Commit art maker',
        usage='python gh-cart.py [year] [option flags]',
        description='Command line tool that gets you more contributions on github',
        epilog='why are you here',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('year', type=int)
    parser.add_argument('-mc', '--maxcommits', type=int, default=2, help='max commits a day')
    parser.add_argument('-of', '--outfile', type=str, default="output.txt", help='What file to write random commits to')
    parser.add_argument('-i', '--image', type=str, default="helloworld.png", help='Input image to base commits off of')
    parser.add_argument('--random', action=argparse.BooleanOptionalAction, default=False, help='makes random commits [0, maxcommits] (highly recommend setting max commits to > 5 for a more realistic outcome)')
    parser.add_argument('--init', action=argparse.BooleanOptionalAction, default=False, help='specify whether to let the program initialize your repo')
    parser.add_argument('-r', '--remote', type=str, default=None, help='Automatically push newly created repo')
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    args = parse_args()

    c_dict = create_commit_dict(args['image'], args['year'], args['maxcommits'], args['random'])
    file_path: Path = Path(args['outfile'])
    file_path.parent.mkdir(exist_ok=True, parents=True)
    
    if args['init'] == True or args['remote'] != None:
        subprocess.run(['git', 'init'], cwd=file_path.parent)
    
    make_commits_for_year(args['year'], c_dict, file_path)
    print("Successfully made our commits for the year :smiley:")

    if args['remote'] != None:
        subprocess.run(['git', 'branch', '-M', 'main'], cwd=file_path.parent)
        subprocess.run(['git', 'remote', 'add', 'origin', args['push']], cwd=file_path.parent)
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=file_path.parent)
        print("Pushed stuff")
