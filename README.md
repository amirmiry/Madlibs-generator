## 🧩 Story Template Filler (Python, No Regex)

This project reads a story from a text file and looks for placeholders inside
`< >` symbols. It then asks the user to type words that replace those placeholders
and prints the completed story.

The code uses **simple manual parsing** (no regular expressions) and is written
using clean, easy-to-understand methods.

---

### ✨ Example

`story.txt`:

### The <adjective> fox likes to <verb> every <time>.

```lua
Program output:
```
- Enter a word for <adjective>: quick
- Enter a word for <verb>: jump
- Enter a word for <time>: morning

  
### --- Your Story ---
The quick fox likes to jump every morning.
```yaml
## 🚀 How It Works

1. The script loads the content of `story.txt`
2. It scans the text character by character to find placeholders:
   - A placeholder starts with `<`  
   - And ends with `>`
3. Each placeholder is stored once (even if it appears multiple times in the story)
4. The user is prompted to provide a word for each placeholder
5. The script replaces the placeholders and prints the final story

```
### 🧠 Project Structure

### main.py The main Python script
### story.txt # The story template with <placeholders>
### README.md # Documentation

```yaml
## ▶️ Running the Program
Make sure `story.txt` is in the same folder as `main.py`.
```
```bash
python main.py
```
Enter the words when asked, and your custom story will appear.
---


### 🧩 Code Overview

The logic is split into simple, readable methods:

  - load_story() – reads the story from a file

  - extract_placeholders() – manually finds <placeholders>

  - fill_story() – asks the user for words and replaces placeholders

  - main() – combines everything

No regex and no advanced libraries — perfect for beginners learning logic and flow control.


### 🌱 Ideas for Improvement

These are optional enhancements you can add later:

- Save the completed story to a new file

- Allow different placeholder styles, like {word}

- Add command-line options for choosing the story file

- Build a GUI (Tkinter, PyQt, or web version)


