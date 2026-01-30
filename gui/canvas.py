from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

class CDFPlot(MplCanvas):
    def plot(self, values1, cdf1, ks=None, ksx=None, values2 = None, cdf2 = None, label1='Трасса 1', label2='Трасса2'):
        self.ax.clear()

        self.ax.step(values1, cdf1, where='post', label=label1)
        if values2 is not None and cdf2 is not None:
            self.ax.step(values2, cdf2, where='post', label=label2)

        self.ax.set_xlabel("k")
        self.ax.set_ylabel("F(k)")
        self.ax.set_title("Эмпирическая функция распределения N(T)")
        if ks is not None and ksx is not None:
            self.ax.axvline(ksx, color='black', linestyle="--", label=f"KS-distance = {ks:4f}")
        self.ax.legend()
        self.ax.grid(True)

        self.draw()