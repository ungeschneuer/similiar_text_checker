from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from platform import system


def getfilename():
    # Hauptfenster verstecken, nur File Selecter anzeigen
    root = Tk()
    root.withdraw()

    # Soll Fenster nach vorne bringen
    root.lift()
    root.focus_force()

    # Mac spezifisches Nach vorne Bringen
    # Aufrufen eines Applescripts
    if system() == 'Darwin':
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

    # Damit Fenster richtig geschlossen wird
    root.update()
    filename = askopenfilename()

    root.quit()

    return filename
