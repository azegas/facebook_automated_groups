# Preparation

In terminal:

For mouse control
* **sudo apt install python3-tk python3-dev**

Find mouse location
* **sudo apt install xdotool**

For pyperclip to work
* **sudo apt-get install xsel**

For screenshots to work 
* **sudo apt install scrot**

For mouse coordinates. Type this whenever needed. Ctrl+c to exit.
* **watch -t -n 0.0001 xdotool getmouselocation**

Create virtualenv:

* python3 -m venv env            # create virtual environment
* source env/bin/activate         # activate virtual env

Install needed libraries:
* pip install pyautogui           # install the automation library
* pip install openpyxl            # for opening xlsx filesx

sadly you are unable to use your pc while the script is runnig, since it needs your keyboard and mouse.

Would be nice to:
- [x] 2022-01-08 paimti grupiu info is excelio failo
- [ ] jei cant open page - (popup confirmation window) - open new tab and continue
- [ ] take screenshot of the end result to confirm the post was published
- [ ] if "Write something" doesnt exist - find "create a public post"

# Automated Posting to Facebook groups

Smuti Fruti freeze dried smoothies needed a solution for a free commercial.

I created a script that posts their posts into the choosen facebook groups that are stored into the excel file. If more groups are added, the script can automatically detect that and add them to the next operation.

First successful full revolution - 2022-01-09

Time per one group : ~1min (shoud be improved)

Groups posted to : 31

![Alt text](https://github.com/arvydasg/python/blob/main/facebook_automated_groups/resources/1st.png)
