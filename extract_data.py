import pyautogui
import time

pyautogui.PAUSE = 0.5  # Delay between actions

time.sleep(3)  # Time to switch to old system

for _ in range(5):  # Repeat for 5 records
    # --- OLD SYSTEM ---
    # Click on first field
    pyautogui.click(300, 200)
    pyautogui.hotkey("ctrl", "a")  # Select text
    pyautogui.hotkey("ctrl", "c")  # Copy text

    # Switch to NEW system
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")  # Paste
    pyautogui.press("tab")  # Next field

    # (Repeat the above for more fields...)

    pyautogui.press("enter")  # Submit form

    # Switch back to OLD system and move to next record
    pyautogui.hotkey("alt", "tab")
    pyautogui.press("down")  # Move to next row in old system
