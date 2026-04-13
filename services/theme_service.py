from PySide6.QtWidgets import QApplication, QMenu, QPushButton
from PySide6.QtGui import QPalette, QColor

class ThemeService:
    @staticmethod
    def set_theme(theme: str):
        app = QApplication.instance()  # Берем существующий QApplication
        if app is None:
            return  # Если вдруг нет приложения, ничего не делаем
        
        if theme == "dark":
            # темная тема
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.Button, QColor(43, 43, 43))
            palette.setColor(QPalette.Light, QColor(120, 120, 120))
            palette.setColor(QPalette.Midlight, QColor(90, 90, 90))
            palette.setColor(QPalette.Dark, QColor(30, 30, 30))
            palette.setColor(QPalette.Mid, QColor(40, 40, 40))
            palette.setColor(QPalette.Text, QColor(255, 255, 255))
            palette.setColor(QPalette.BrightText, QColor(65, 80, 148))
            palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.Base, QColor(45, 45, 45))
            palette.setColor(QPalette.Window, QColor(30, 30, 30))
            palette.setColor(QPalette.Shadow, QColor(0, 0, 0))
            palette.setColor(QPalette.Highlight, QColor(39, 47, 88))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
            palette.setColor(QPalette.Link, QColor(65, 80, 148))
            palette.setColor(QPalette.LinkVisited, QColor(54, 67, 123))
            palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255, 15))
            palette.setColor(QPalette.ToolTipBase, QColor(60, 60, 60))
            palette.setColor(QPalette.ToolTipText, QColor(212, 212, 212))
            palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 128))
            palette.setColor(QPalette.Accent, QColor(54, 67, 123))
        else:
            # светлая тема
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
            palette.setColor(QPalette.Button, QColor(222, 222, 222))
            palette.setColor(QPalette.Light, QColor(255, 255, 255))
            palette.setColor(QPalette.Midlight, QColor(255, 255, 255))
            palette.setColor(QPalette.Dark, QColor(120, 120, 120))
            palette.setColor(QPalette.Mid, QColor(160, 160, 160))
            palette.setColor(QPalette.Text, QColor(0, 0, 0))
            palette.setColor(QPalette.BrightText, QColor(31, 38, 70))
            palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
            palette.setColor(QPalette.Base, QColor(222, 222, 222))
            palette.setColor(QPalette.Window, QColor(243, 243, 243))
            palette.setColor(QPalette.Shadow, QColor(0, 0, 0))
            palette.setColor(QPalette.Highlight, QColor(31, 38, 70))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
            palette.setColor(QPalette.Link, QColor(23, 28, 53))
            palette.setColor(QPalette.LinkVisited, QColor(12, 15, 28))
            palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255, 9))
            palette.setColor(QPalette.ToolTipBase, QColor(243, 243, 243))
            palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0, 228))
            palette.setColor(QPalette.PlaceholderText, QColor(0, 0, 0, 128))
            palette.setColor(QPalette.Accent, QColor(31, 38, 70))
        
        app.setPalette(palette)
        buttons = None
        # Обновляем все виджеты
        for widget in app.allWidgets():
            widget.update()
            # сохраняем виджет с кнопками слева
            if widget.objectName() == "buttons":
                buttons = widget
            # отдельно применяем стиль к меню-бару
            if isinstance(widget, QMenu):
                widget.setStyleSheet(
                    MENUBAR_STYLE.format(
                        bg_color=palette.color(QPalette.Window).name(),
                        wt_color=palette.color(QPalette.WindowText).name(),
                        bg_hover = palette.color(QPalette.Mid).name()
                    )
                )
            # перерисовываем кнопки, чтобы синхронизировался цвет
            if isinstance(widget, QPushButton):
                if buttons and buttons.isAncestorOf(widget):
                    widget.setStyleSheet("")
                widget.setStyleSheet(
                    BUTTONS.format(
                        bg_color_btn=palette.color(QPalette.Button).name()
                    )
                )

        if buttons:
            child_buttons = buttons.findChildren(QPushButton)

            for btn in child_buttons:
                btn.setStyleSheet(
                    BUTTON_STYLE_LEFTMENU.format(
                        btn_color=palette.color(QPalette.ButtonText).name(),
                        bg_hover=palette.color(QPalette.Mid).name(),
                        bg_checked=palette.color(QPalette.Highlight).name(),
                        txt_checked=palette.color(QPalette.HighlightedText).name()
                    )
                )


BUTTONS = """
QPushButton {{
    background-color: {bg_color_btn};
}}
"""

BUTTON_STYLE_LEFTMENU = """
QPushButton {{
    text-align: left;
    border-radius: 6px;
    padding: 4px;
    padding-right: 15px;
    color: {btn_color};
}}
QPushButton:hover {{
    background-color: {bg_hover};   
}}
QPushButton:checked {{
    background-color: {bg_checked};
    color: {txt_checked};
}}
"""

MENUBAR_STYLE = """
QMenu {{
    background-color: {bg_color};
    color: {wt_color};
}}
QMenu::item {{
    background-color: {bg_color};
    color: {wt_color};
}}
QMenu::item:selected {{
    background-color: {bg_color};
    color: {wt_color};
}}
QMenu:hover {{
    background-color: {bg_hover}
}}
"""