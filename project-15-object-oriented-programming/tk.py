import os
import tkinter

# Suppress the deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Print Tk version
print(tkinter.TkVersion)

# Alternatively, for Tcl version
print(tkinter.Tcl().eval('info patchlevel'))