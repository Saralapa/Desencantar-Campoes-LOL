from main import TITLE


def detect_coordinates(title: str = TITLE) -> None:
    """
    This function detects the current mouse position and calculates the relative position
    within the specified window.

    Parameters:
    title (str): The title of the window to be used for relative position calculation.
                 Default is the value of the global constant 'TITLE'.

    Returns:
    None: This function does not return any value. It only prints the coordinates.
    """
    import pyautogui

    x, y = pyautogui.position()  # Get the current mouse position

    # Calculate the relative position within the specified window
    relative_x = x - pyautogui.getWindowsWithTitle(title)[0].topleft.x
    relative_y = y - pyautogui.getWindowsWithTitle(title)[0].topleft.y

    # Print the coordinates
    print(f"Coordenadas: ({x}, {y})")
    print(f"Coordenadas relativas: ({relative_x}, {relative_y})")
