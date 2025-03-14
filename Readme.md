## zfind for all platforms 
The Idea came into the mind when I worked for cargo-cult

This is an implementation that works in the same idea but this time it also works on windows 

# How it works
well both zsh and bash all support storing history in .zsh_history or .bash_history file
(if you have time stamps enabled this should ignore those)

for windows: - there is a file that stores it similar to zsh and bash but only for powershell
there is no option afaik

you'd open these files find snippets and give options

the selected option would be copied to clipboard 

**This is written in Python for easier understanding of the code compared to Rust where for the beginner developer or average user would fail to understand anything and also should provide an easier installation as Python is installed in most Linux-based systems by default and is also very lightweight.**

# Features 
- Easy to use
- Good looking TUI
- Copy commands to clipboard
- Cross platform (macOS, Linux, Windows XD)

# Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd zfind
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python main.py
    ```

# Platform-Specific Features
- On macOS and Linux, you can switch between zsh and bash history files using the command palette.
- On Windows, the history file switching feature is not available.

# Common Bugs
If you have a non-UTF-8 character the program crashes so I included zshhist.py by xkikeg
check the code and run it it's in the first lines of code (line 14 in zshhist.py)

**Written with love in Python**
