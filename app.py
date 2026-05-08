from gui.window import window
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import multiprocessing
from resources import resources_rc

def main():
    app = QApplication()
    win = window()
    app.setWindowIcon(QIcon(":/icon.ico"))
    win.setWindowIcon(QIcon(":/icon.ico"))
    win.show()
    app.exec()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()