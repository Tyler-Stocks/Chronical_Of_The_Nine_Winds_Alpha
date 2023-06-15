import time

class Console:

    def __init__(self) -> None:
        # Lookin' at the Devil and the Angel on my shoulder.
        pass

    def clear(self, delay: int | float = 0):
        time.sleep(delay)
        print("\033[H\033[J", end = '')

    def color_text(self, text: str, r: int = 255, g: int = 255, b: int = 255) -> str:
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
