# Automated Posting to Facebook groups

Smuti Fruti freeze dried smoothies needed a solution for a free commercial.

I created a script that posts their posts into the choosen facebook groups that are stored into the excel file. If more groups are added, the script can automatically detect that and add them to the next operation.


  | Revolution    | Groups           | Average duration  |
  | ------------- |:-------------:| -----:|
  | 2022-01-09      | 31 | ~60sec |
  | 2022-01-13      | 31      |   ~60sec |

![Alt text](https://github.com/arvydasg/facebook_automated_groups/blob/master/resources/1st.png)

# Preparation

## In terminal:

For mouse control:
* **sudo apt install python3-tk python3-dev**

Find mouse location:
* **sudo apt install xdotool**

For pyperclip to work:
* **sudo apt-get install xsel**

For screenshots to work:
* **sudo apt install scrot**

For mouse coordinates. Type this whenever needed. Ctrl+c to exit:
* **watch -t -n 0.0001 xdotool getmouselocation**

## Create virtualenv:

Create virtual environment:
* **python3 -m venv env**

Activate virtual env:
* **source env/bin/activate**

## Install needed libraries:

Install the automation library:
* **pip install pyautogui**

For opening xlsx filesx:
* **pip install openpyxl**

Sadly you are unable to use your pc while the script is runnig, since it needs your keyboard and mouse.

# Would be nice to:
- [x] 2022-01-08 paimti grupiu info is excelio failo
- [x] 2022-01-13 if "Write something" doesnt exist - find "create a public post"
- [ ] jei cant open page - (popup confirmation window) - open new tab and continue
- [ ] take screenshot of the end result to confirm the post was published

