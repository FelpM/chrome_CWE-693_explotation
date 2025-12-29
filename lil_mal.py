import time
import sys
import subprocess
import pyautogui
import platform

INTERVAL = 15

def get_active_window_title():
    system = platform.system()
    if system == "Windows":
        try:
            import pygetwindow as gw
            win = gw.getActiveWindow()
            return win.title if win else ""
        except ImportError:
            return "Erro: instale pygetwindow"
    elif system == "Linux":
        try:
            result = subprocess.run(
                ['xdotool', 'getactivewindow', 'getwindowname'],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL, 
                text=True
            )
            return result.stdout.strip()
        except Exception:
            return ""
    else:
        return ""

def is_chrome_window(title):
    return "chrome" in title.lower()

def do_actions():
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.1)
    pyautogui.write("javascript")
    time.sleep(0.1)
    pyautogui.write(":alert(document.domain)")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(5.0)
    pyautogui.press("enter")

def main():
    while True:
        title = get_active_window_title()
        if is_chrome_window(title):
            do_actions()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
