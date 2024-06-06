from main import TITLE


def open_window(title: str = TITLE) -> None:
    """
    This function opens the specified window. Minimizes it, restores it, and activates it.

    Parameters:
    title (str): The title of the specified window. Default is the value of the global constant 'TITLE'.

    Returns:
    None: This function does not return any value. It only performs actions on the specified window.
    """
    import pyautogui

    [
        window
        for window in pyautogui.getWindowsWithTitle(title)
        if window.title == title
    ][0].minimize()
    [
        window
        for window in pyautogui.getWindowsWithTitle(title)
        if window.title == title
    ][0].restore()
    [
        window
        for window in pyautogui.getWindowsWithTitle(title)
        if window.title == title
    ][0].activate()
