from main import Visualiser


dirOutput = "/Users/jvo/Downloads/output"
pathSong = "/Users/jvo/Downloads/8bars.musicxml"

settings = {}
settings["measuresPerLine"] = 4
settings["subdivision"] = 0
settings["lyrics"] = True

vis = Visualiser(pathSong, settings)
vis.saveFig(dirName=dirOutput)
