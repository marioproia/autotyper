import pyperclip
import pyautogui
import keyboard
import time

def autotype_from_clipboard(delay=0.1):
    # Wait a brief moment to ensure the keyboard shortcut doesn't interfere with the typing
    time.sleep(delay)
    
    # Fetch the text from the clipboard
    text = pyperclip.paste()
    
    # Type out the text
    pyautogui.write(text, interval=0.01)

def on_triggered(event):
    print("Key combination pressed, starting autotype...")
    autotype_from_clipboard()

if __name__ == "__main__":
    # Listen for the specific key combination (Ctrl+Shift+V)
    keyboard.add_hotkey('ctrl+shift+t', on_triggered)
    
    print("Listening for Ctrl+Shift+T. Press ESC to stop.")
    keyboard.wait('esc')
