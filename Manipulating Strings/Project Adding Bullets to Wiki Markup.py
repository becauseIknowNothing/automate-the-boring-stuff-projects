#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

texts=text.split("\n")
for i in  range(len(texts)):
    texts[i]="* " + texts[i]
text="\n".join(texts)
pyperclip.copy(text)
