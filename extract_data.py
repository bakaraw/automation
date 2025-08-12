import pyautogui
import pytesseract
from PIL import Image
import time

# Path to Tesseract executable (adjust for your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

time.sleep(3)  # Give time to open old system

for _ in range(3):  # Process 3 records as a test
    # Step 1: Take screenshot of the data field in OLD system
    field_region = (300, 200, 200, 30)  # x, y, width, height (adjust these)
    screenshot = pyautogui.screenshot(region=field_region)

    # Step 2: Extract text with OCR
    extracted_text = pytesseract.image_to_string(screenshot).strip()
    print("Extracted:", extracted_text)

    # Step 3: Switch to NEW system
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.5)

    # Step 4: Type the extracted text
    pyautogui.typewrite(extracted_text)
    pyautogui.press("tab")  # Move to next field

    # Step 5: Switch back to OLD system & move to next record
    pyautogui.hotkey("alt", "tab")
    pyautogui.press("down")  # If navigating a table
