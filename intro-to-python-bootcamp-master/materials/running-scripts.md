![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)


# Setup

## Install Programs

1. Make sure you have downloaded and installed [Sublime Text 3](https://www.sublimetext.com/3).
2. Make sure you have downloaded and installed [Python 3](https://www.python.org/downloads/)

## Using the Command Line To Create a File

3. Open you terminal:
  - > A terminal / console / command line (all the same thing) is a text interface for running commands. These terminals are somewhat different between different operating systems, but after you run the step below, we will be referring to whatever program you opened as the "terminal.
  - **MacOS**: press `CMD + Space`, and in **Spotlight Search**, type in `terminal` and press `Enter` to open it.
  - **Windows 10**: go to your **Start Menu** and type in `Command Prompt` to find the `Command Prompt` app and open it.
  - **Linux / Unix**: open whichever terminal you use.
4. In your terminal, navigate to you home directory:
  - > You can always return to this directory in your terminal by running the command below. `cd` simply stands for "change directory' and the text after it is a OS-specific shortcut to your user's home directory on the computer. You can also view the contents of this or any directory you are in on the terminal by running `ls` (**MacOS / Linux / Unix**) or `dir` (**Windows 10**). Here are more command line commands for [MacOS](https://gist.github.com/poopsplat/7195274) or [Windows 10](http://simplyadvanced.net/blog/cheat-sheet-for-windows-command-prompt/) (if you are on Linux\Unix, you must already know quite a few of these!)
  - **MacOS / Linux / Unix**: in your terminal, type `cd ~/` and press `Enter`.
  - **Windows 10**: in your terminal, type `cd %USERPROFILE%/` and press `Enter`.
5. Make a new empty python file:
  - > All Python files are of the format `<file name>.py`, ie they all have the `.py` suffix. You will create this file right from your terminal and open it from there as well.
  - **MacOS / Linux / Unix**: in your terminal, type `touch exercise.py` and press `Enter`.
  - **Windows 10**: in your terminal, type `echo $null >> exercise.py` and press `Enter`.

## Opening the File in Sublime Text

6. We will open the file by using a terminal command `subl`. Type `subl exercise.py` into your terminal and **Sublime Text** will run with your file already opened!
> If you are having trouble getting **Sublime Text** to open, ask your Instructor or TA for assistance.

## Writing and Running a Simple Script

7. In **Sublime Text**, add the following to the top of your empty `exercise.py` file and save it:

```python
console.log('hello world')
```

8. Go back to your terminal and run `python exercise.py` to run the file. You should see `"hello world"` in your terminal.
> When you run the `python` interpreter followed by a file name, it will attempt to read the script file from top to bottom and run each line of code. If you are having trouble getting `"hello world"` to show up in your terminal, ask your Instructor or TA for assistance.

### From now on, whenever you make changes to `exercise.py` and save it, you can see how your new code runs simply by doing step **8** again!

# The Difference Between Running `python` and `python <script file>.py`

- When we simply run the `python` command, Python will open up the **Python REPL** ([more on the REPL here](./README.md#hello-world)), allowing you to enter and run Python commands one line at a time.
  - This usage allows you to quickly try out a few commands without having to create a new file, but is more cumbersome for writing / editing long blocks of code. You also cannot save your commands to a file for later use.
- When we run `python <script file>.py`,  Python will run each line of your script file and then when it reaches the end, it will exit. 
  - This usage allows you to easily write / edit and save python commands and manage long blocks of code.