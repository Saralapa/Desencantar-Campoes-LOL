import pyautogui

TITLE = "League of Legends"


if __name__ == "__main__":
    from utils.Clicks import Clicks
    from utils.open_window import open_window

    # from utils.detect_coordinates import detect_coordinates

    open_window(TITLE)
    for _ in range(2):
        pyautogui.hotkey("ctrl", "=")
    while True:
        Clicks.clickREL(TITLE)
