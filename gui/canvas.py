from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.apply_theme()  # при создании можно применить текущую тему

    def apply_theme(self):
        # берём цвета из текущей палитры приложения
        palette = QApplication.instance().palette()
        bg = palette.color(QPalette.Window).name()
        text = palette.color(QPalette.WindowText).name()
        grid = palette.color(QPalette.Mid).name()

        # фон фигуры и осей
        self.fig.patch.set_facecolor(bg)
        self.ax.set_facecolor(bg)

        # подписи и оси
        self.ax.tick_params(colors=text)
        for spine in self.ax.spines.values():
            spine.set_color(text)
        self.ax.xaxis.label.set_color(text)
        self.ax.yaxis.label.set_color(text)

        # сетка
        self.ax.grid(True, color=grid)

        # легенда
        legend = self.ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(bg)
            legend.get_frame().set_edgecolor(text)
            for t in legend.get_texts():
                t.set_color(text)

        # перерисовать Canvas
        self.draw()

class CDFPlot(MplCanvas):
    def plot(self, values1, cdf1, ks=None, ksx=None,
             values2=None, cdf2=None,
             label1='Трасса 1', label2='Трасса 2'):

        self.ax.clear()

        self.apply_theme()

        # графики
        self.ax.step(values1, cdf1, where='post', label=label1)

        if values2 is not None and cdf2 is not None:
            self.ax.step(values2, cdf2, where='post', label=label2)

        # подписи
        self.ax.set_xlabel("k", color=self.text)
        self.ax.set_ylabel("F(k)", color=self.text)

        # сетка
        self.ax.grid()

        # KS линия
        if ks is not None and ksx is not None:
            self.ax.axvline(
                ksx,
                color='white' if self.dark else 'black',
                linestyle="--",
                label=f"KS-distance = {ks:4f}"
            )

        # легенда
        legend = self.ax.legend()
        if legend:
            legend.get_frame().set_facecolor(self.bg)
            legend.get_frame().set_edgecolor(self.text)
            for t in legend.get_texts():
                t.set_color(self.text)

        self.draw()

class CDFPlot(MplCanvas):
    def plot(self, values1, cdf1, ks=None, ksx=None, values2=None, cdf2=None,
             label1='Трасса 1', label2='Трасса 2'):

        self.ax.clear()

        # --- цвета из палитры приложения ---
        palette = QApplication.instance().palette()
        bg = palette.color(QPalette.Window).name()
        text = palette.color(QPalette.WindowText).name()
        grid = palette.color(QPalette.Mid).name()

        self.fig.patch.set_facecolor(bg)
        self.ax.set_facecolor(bg)

        # графики
        self.ax.step(values1, cdf1, where='post', label=label1)
        if values2 is not None and cdf2 is not None:
            self.ax.step(values2, cdf2, where='post', label=label2)

        # подписи и оси
        self.ax.set_xlabel("k", color=text)
        self.ax.set_ylabel("F(k)", color=text)
        self.ax.tick_params(colors=text)
        for spine in self.ax.spines.values():
            spine.set_color(text)

        # сетка
        self.ax.grid(True, color=grid)

        # KS линия
        if ks is not None and ksx is not None:
            self.ax.axvline(ksx, color=text, linestyle="--",
                            label=f"KS-distance = {ks:4f}")

        # легенда
        legend = self.ax.legend()
        if legend:
            legend.get_frame().set_facecolor(bg)
            legend.get_frame().set_edgecolor(text)
            for t in legend.get_texts():
                t.set_color(text)

        self.draw()