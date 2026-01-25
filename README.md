# Github-Commit-Art
- Make your empty years on github have a commit art!! yippee for lazy people.
- Use this to also decorate your github contribution history with little art snippets 
- the ~7x53 ish canvas size for github contributions can have fun things drawn on

### Requirements:
- Python interpreter that supports pillow
- Pillow (Install with `pip install pillow` or `conda install anaconda::pillow` on a anaconda environment)  


### Usage:
- will take in an image that is 7x53 (h * w), will not work for larger images and may have undefined behavior for smaller images
- specify an input image with `-i  `or it'll default to the given `input_image.png`  
- specific an output image or it will default to creating a txt file in the local directory
- you can either initialize the repo yourself or let the program do it by passing the `--init` flag.
- you can either pass `-r` or `--remote` [remote link] to an empty repo initialized in github to let the program automatically initialize and push to that destination (make sure you have valid git credentials)

```bash
# basic usage
python gh-cart.py [year] -[optional] [flags]

# print help
python gh-cart.py -h

# Make it read from 2020 with the default arguments
python gh-cart.py 2020 
# change output to be a folder next to the folder gh-cart.py is currently in
# also initialize and push the repo to a remote of given link
python gh-cart.py 2006 -of ../newfolder/text.txt -i fun.png --remote some_remote_repository_link 

# make max commits a day 30 (defaulted at one)
python gh-cart.py 2025 -mc 30 
```
## Why did I make this?
- So apparently, you can make commits in the future and past using git, and github does use those timestamps to well, show those commits on your account.  
- I unfortunately don't spend all my time coding so my commit history looks very sad on github, so to liven it up I decided what if I made some python code that does that for me?  
- I realized you could use that space to make little art drawings or some text, so I decided to use that to my advantage too do that
- Anything for commit history padding plsz plzspzllpslzsz 
