import subprocess as sp

class ScreenClearer:
    def clear_screen(self):
        sp.call('cls' if sp.os.name == 'nt' else 'clear', shell=True)
