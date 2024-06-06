class Clicks:
    from main import TITLE

    
    def __click__(x: int, y: int, title: str = TITLE) -> None:
        """
        Simulates a mouse click at the specified coordinates within the specified window.

        Parameters:
        x (int): The x-coordinate of the mouse click.
        y (int): The y-coordinate of the mouse click.
        title (str): The title of the window where the mouse click will be simulated.
                    Default is the value of the global constant 'TITLE'.

        Returns:
        None: This function does not return any value. It only performs a mouse click action.

        Raises:
        SystemExit: If the specified window is not active, the function will exit the program.
        """
        import pyautogui

        pyautogui.PAUSE = 0.3

        pyautogui.sleep(
            0.2
        )  # Pause for 0.2 seconds to allow the window to become active
        if not pyautogui.getWindowsWithTitle(title)[0].isActive:
            exit()  # Exit the code if the specified window is not active
        pyautogui.click(x=x, y=y)  # Simulate a mouse click at the specified coordinates

    
    def clickABS(*coord: int):
        """
        Simulates a series of mouse clicks at the specified absolute coordinates within the screen.

        Parameters:
        *coord (int): Variable length argument list of integers representing the x and y coordinates of the mouse clicks.
                    If the number of coordinates is less than 6, the function will use default coordinates.

        Returns:
        None: This function does not return any value. It only performs mouse click actions.

        Raises:
        TypeError: If any of the provided coordinates are not integers, a TypeError will be raised.
        """
        import pyautogui

        for value in coord:
            if not isinstance(value, int):
                raise TypeError("The values for the coordinates must be integers")

        if len(coord) != 6:
            coord = (290, 610, 460, 650, 820, 720) # Default values

        for i in range(0, 6, 2):
            Clicks.__click__(x=coord[i], y=coord[i + 1])

        pyautogui.sleep(1.3)  # Pause for 1.3 seconds before the next set of clicks

    
    def clickREL(title: str = TITLE, *coord: int) -> None:
        """
        Simulates a series of mouse clicks at the specified relative coordinates within the specified window.

        Parameters:
        title (str): The title of the window where the mouse click will be simulated.
                    Default is the value of the global constant 'TITLE'.
        *coord (int): Variable length argument list of integers representing the x and y coordinates of the mouse clicks.
                    If the number of coordinates is less than 6, the function will use default coordinates.

        Returns:
        None: This function does not return any value. It only performs mouse click actions.

        Raises:
        TypeError: If any of the provided coordinates are not integers, a TypeError will be raised.
        """
        import pyautogui

        for value in coord:
            if not isinstance(value, int):
                raise TypeError("The values for the coordinates must be integers")

        if len(coord) != 6:
            coord = (110, 550, 350, 590, 660, 650) # Default values

        for i in range(0, 6, 2):
            Clicks.__click__(
                pyautogui.getWindowsWithTitle(title)[0].topleft.x + coord[i],
                pyautogui.getWindowsWithTitle(title)[0].topleft.y + coord[i + 1],
            )

        pyautogui.sleep(1.3)  # Pause for 1.3 seconds before the next set of clicks
