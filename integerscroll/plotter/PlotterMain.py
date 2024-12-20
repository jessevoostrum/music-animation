
from matplotlib import rc

from integerscroll.plotter.PlotterNotes import PlotterNotes
from integerscroll.plotter.PlotterChords import PlotterChords
from integerscroll.plotter.PlotterBarLines import PlotterBarLines
from integerscroll.plotter.PlotterMetadata import PlotterMetadata


class PlotterMain:

    def __init__(self, streamObj, Settings, LocationFinder, axs):

        self.streamObj = streamObj
        self.Settings = Settings

        self.LocationFinder = LocationFinder

        self.axs = axs

        self.PlotterNotes = PlotterNotes(self.streamObj, self.Settings, self.LocationFinder, self.axs)
        self.PlotterChords = PlotterChords(self.streamObj, self.Settings, self.LocationFinder, self.axs)
        self.PlotterBarLines = PlotterBarLines(self.streamObj, self.Settings, self.LocationFinder, self.axs)
        self.PlotterMetadata = PlotterMetadata(self.streamObj, self.Settings, self.LocationFinder, self.axs)

    def plot(self):

        # self.PlotterMetadata.plotMetadata()
        # rc('text.latex', preamble=r'\usepackage{amssymb}')
        if self.Settings.plotMelody:
            self.PlotterNotes.plotNotes()
        if self.Settings.plotChordTones:
            self.PlotterNotes.plotChordNotes()
        self.PlotterChords.plotChords()
        self.PlotterBarLines.plotBarLines()

