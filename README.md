# hex_to_clipboard

This copies the hex code of the pixel the mouse is pointing at whenever a key combination (shift+z+x) is pressed.

## Packages used:
pynput, PIL, pyperclip, pyautogui

## Working:
1. Listens for keyboard input. 
2. When shift+z+x key combination is detected, takes a screenshot of the screen and stores mouse pointer coordinates.
3. Takes the rgb value of the pixel at those coordinates in the screenshot.
4. Converts rgb value to hex code.
5. Copies hex code to clipboard.

## Other info:
1. The key combination can be changed from COMBINATIONS variable within the main() function.
2. The program exits when it scans a white pixel (hex code #ffffff). This can be turned off as instructed in the beginning of program.

## Disclaimer:
The part inside the main funtion is copied from a website. Will be happy to mention it here but not able to find it again.
