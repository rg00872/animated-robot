#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
import pyperclip, sys

text = pyperclip.paste()

# TODO: Separate lines and add stars.

pyperclip.copy(text) 