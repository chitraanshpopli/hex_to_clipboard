from pynput import keyboard
from PIL import Image
import pyperclip
import pyautogui



def rgb_to_hex(r,g,b):
	#Converts individual rgb values (decimal) to individual rgb values (hex). 
	Hr = hex(r)[2:]
	Hg = hex(g)[2:]
	Hb = hex(b)[2:]
	return Hr,Hg,Hb

def get_hex_value():
	#Returns hex code of the color of pixel the mouse is pointing.
	
	#Take Screenshot of whole screen
	sshot = pyautogui.screenshot()

	#Stores current mouse position in (x,y) tuple
	mouse_position = pyautogui.position()

	#Convert the Screenshot to RGB type
	image = sshot.convert('RGB')

	#Store RGB values of the current position of mouse pointer
	r,g,b = image.getpixel((mouse_position))

	#Convert to hex.
	Hr, Hg, Hb = rgb_to_hex(r,g,b)
	
	#If hex value is single digit, add 0 in start
	if len(Hr) == 1:
		Hr = '0' + str(Hr)
	if len(Hb) == 1:
		Hb = '0' + str(Hb)
	if len(Hg) == 1:
		Hg = '0' + str(Hg)
	

	#Create final Hex Value
	hex_value = Hr+Hg+Hb
	
	#Exit the program by scanning white pixel (hex -- 'ffffff') 
	global exit_value
	if exit_value != '1':
		if hex_value == 'ffffff':
			print('\nWhite pixel. Quiting.')
			exit()
	print('Hex value copied to clipboard - ' + hex_value)
	return hex_value
	
	
def main():

	#Keyboard key combinations to trigger the execute block.
	COMBINATIONS = [
		{keyboard.Key.shift, keyboard.KeyCode(char='x'),keyboard.KeyCode(char='z')},
		{keyboard.Key.shift, keyboard.KeyCode(char='Z'),keyboard.KeyCode(char='X')}
	]

	current = set()
	#Executes when COMBINATION is triggered.
	def execute():
		pyperclip.copy(get_hex_value())
		pyperclip.paste()
		#print(a)

	def on_press(key):
		if any([key in COMBO for COMBO in COMBINATIONS])and not key in current:
			current.add(key)
			if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
				execute()

	def on_release(key):
		if any([key in COMBO for COMBO in COMBINATIONS]):
			current.remove(key)

	# Collect events until released
	with keyboard.Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()

print('''
Press shift+z+x to get hex code of pixel pointed by mouse pointer.
To exit, either close this window or scan a white pixel (hex ffffff).
''')
exit_value = str(input('''To disable white pixel exit feature, type 1 and press enter. 
To keep this enabled, just press enter.
'''))

print('Program started')
main()

