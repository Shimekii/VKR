from gui.window import window
from PySide6.QtWidgets import QApplication
import multiprocessing

def main():
    app = QApplication()
    win = window()
    win.show()
    app.exec()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()