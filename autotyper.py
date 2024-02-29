import pyperclip
import pyautogui
import keyboard
import time

def type_special_character(char):
    # Add more elif clauses here for other special characters if needed.
    if char == '@':
        pyperclip.copy("@")
        pyautogui.hotkey("ctrl", "v")
    else:
        pyautogui.typewrite(char, interval=0.05)  # Fallback for characters that don't need special handling

def autotype_from_clipboard(delay=0.3):
    time.sleep(delay)  # Brief delay
    text = pyperclip.paste()  # Fetch clipboard content

    for char in text:
        type_special_character(char)

def on_triggered():
    print("Key combination pressed, starting autotype...")
    autotype_from_clipboard()

if __name__ == "__main__":
    # Setup hotkey
    keyboard.add_hotkey('ctrl+alt+v', on_triggered)

    print("Press Ctrl+Alt+V to autotype. Press ESC to stop.")
    keyboard.wait('esc')