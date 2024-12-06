class Stopwatch:
    def __init__(self):
        self._is_running = False  # Initialize as not running

    def click(self):
        if self._is_running:
            self._is_running = False
            print("Stopped")
        else:
            self._is_running = True
            print("Running")
