import matplotlib.font_manager as font_manager
from matplotlib import rcParams

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.transforms import Bbox
from matplotlib.figure import Figure

class CanvasCreator:
    def __init__(self, Settings, numMeasures):

        self.Settings = Settings

        rcParams['mathtext.fontset'] = 'cm'

        self.yMin = self.Settings.yMin
        self.yMax = self.Settings.yMax

        self.figs = []
        self.axs = []

        self.numA4Widths = numMeasures / self.Settings.measuresPerLine

        self._createCanvas()

    def saveFig(self, pathName, maxXPos):

        yPosLowest = 1 - (self.yMax - self.yMin + 2 * self.Settings.vMarginLineTop)
        heightStart = self.Settings.heightA4 * yPosLowest

        xPosHighest = maxXPos + 2 * 0.01
        widthEnd = self.Settings.widthA4 * xPosHighest

        bbox = Bbox([[0, heightStart], [widthEnd, self.Settings.heightA4]])

        self.figs[0].savefig(pathName, dpi=1000, bbox_inches=bbox)

        # with PdfPages(pathName) as pdf:
        #     for fig in self.figs:
        #         pdf.savefig(fig)

    def _createCanvas(self):

        fig = Figure(figsize=(self.numA4Widths * self.Settings.widthA4, self.Settings.heightA4))
        ax = fig.subplots()
        ax = self._formatAx(ax)
        self.figs.append(fig)
        self.axs.append(ax)

    def _formatAx(self, ax):
        ax.set_ylim(0, 1)
        ax.set_xlim(0, self.numA4Widths)
        ax.axis('off')
        ax.set_position([0, 0, 1, 1])
        return ax

    def getAxs(self):
        return self.axs

    def getFigs(self):
        return self.figs

