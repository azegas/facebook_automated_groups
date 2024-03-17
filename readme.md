# Automated Posting to Facebook groups

Smuti Fruti freeze dried smoothies needed a solution for a free commercial.

I created a script that posts their posts into the choosen facebook groups that are stored into the excel file. If more groups are added, the script can automatically detect that and add them to the next operation.


  | Revolution    | Groups           | Average duration  | comment |	   
  | ------------- |:-------------:| -----:|-------:|	 
  | 2022-01-09      | 31 | ~60sec | comme
  | 2022-01-13      | 31      |   ~60sec |
| 2022-01-16      |   68    |   ~23sec | got blocked after this 68.|
|2022-01-17 |	  73+21(later) |~24 sec | facebook message - too many actions|
|2022-01-18 |	  66+53 |~24 sec | smooth two runs. GOT BANNED. |


![Alt text](https://github.com/arvydasg/facebook_automated_groups/blob/master/resources/1st.png)

# Preparation

## In terminal:

For mouse control:
`sudo apt install python3-tk python3-dev`

Find mouse location:
`sudo apt install xdotool`

For pyperclip to work:
`sudo apt-get install xsel`

For screenshots to work:
`sudo apt install scrot

For mouse coordinates. Type this whenever needed. Ctrl+c to exit:
`watch -t -n 0.0001 xdotool getmouselocation`

## Create virtualenv:

Create virtual environment:
`python3 -m venv env`

Activate virtual env:
`source env/bin/activate`

## Install needed libraries:

Install the automation library:
`pip install pyautogui`

For opening xlsx filesx:
`pip install openpyxl`

Sadly you are unable to use your pc while the script is runnig, since it needs your keyboard and mouse.

# Would be nice to:
- [x] 2022-01-08 paimti grupiu info is excelio failo
- [x] 2022-01-13 if "Write something" doesnt exist - find "create a public post"
- [ ] jei cant open page - (popup confirmation window) - open new tab and continue
- [ ] take screenshot of the end result to confirm the post was published





# README UPDATE:

![image](https://github.com/azegas/facebook_automated_groups/assets/78803192/9c20f76b-bf24-4826-a8a1-e25271f55763)


* Intro

A Django web app that posts your desired content to the chosen Facebook groups
for you!

* What is it for

A recently started smoothie drink powder business that is testing itself out in
the field. Instead of purchasing ads on facebook, the client first wanted to
post their content to various facebook groups to see the engagement. Over time
this tasks proved to be too tedious, since it requires a lot of manual
clicking.

I have decided to help them out by creating this automation bot that posts to
various facebook groups by itself, with client needing to click only a few
clicks. There were various facebook bots on the internet, but you had to pay
fro those. It was interesting for me to see if I can create something like it
myself.

* How it works

All the user need is a link to the facebook post and a call to action message.
He then needs to input these two into the browser window and click start.
Application does the rest. Taking the data from the groups file, going through
each and every one of them and posting the choosen content (link, ad
description and a call to action message). Leave it running, come back after a
white - inspect the terminal windows - see how many successful group posts this
app has done.

* Cons

There are a few cons of using this script.

- You can not really use the computer while it runs since it occupiesyour mouse
  and you shouldn’t be clicking on other windows while it is running. You can
  run this script while you are having a break, step away from your computer
  for 15min or so and come back with having your post shared to 30 or so
  groups.

- Your facebook account gets restricted. Often. If you are posting to too many
  groups at a time. 20 or so is fine, but more than that (in one sitting) and
  you are risking to get a temporary ban by facebook.

* What to fix

- if the script breaks - take a screenshot of the whole screen (easier to debug
  what happened)
- when the script finishes posting to one group - take a screenshot (easier to
  track the activity)
- If group has pending posts - stop the for loop, run next group
- Rebuild facebook_django app with modules
