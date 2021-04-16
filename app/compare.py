from Signatur import Signatur
import shelve
import storage


# Ueberprueft zwei Signaturen miteinander
def toOne(textone, texttwo):
    # Prueft ob beide Inputs Signaturen sind
    if type(textone) is Signatur and type(texttwo) is Signatur:
        # Wenn je wird Formel ausgerechnet
        return round((abs(textone.DWL - texttwo.DWL) * 11) + (abs(textone.TTR - texttwo.TTR) * 33) + \
               (abs(textone.HLR - texttwo.HLR) * 50) + (abs(textone.DSL - texttwo.DSL) * 0.4) + \
               (abs(textone.DDS - texttwo.DDS) * 4), 2)
    else:
        raise TypeError("Beide Objekte muessen Signaturen sein")


def toAll(textsignatur):
    smallestComparement = 1000
    smallestSignatur = Signatur()

    with shelve.open('storage') as sto:
        for key in sto.keys():
            comparement = toOne(textsignatur, storage.getbytitel(key))
            if comparement < smallestComparement and (textsignatur.Titel != key and textsignatur.Author !=
                storage.getbytitel(key).Author):
                smallestComparement = comparement
                smallestSignatur = storage.getbytitel(key)

    print("Der Text \"%s\" von \"%s\" ist in unserem Archiv der Signatur von dem Text \"%s\" von \"%s\" "
          "mit einem Ähnlichkeitsfaktor von %.2f am ähnlichsten." % (textsignatur.Titel, textsignatur.Author,
                                                                     smallestSignatur.Titel, smallestSignatur.Author,
                                                                     smallestComparement))

    return smallestSignatur


