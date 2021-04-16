from Signatur import Signatur
import split
import format


def signatur(titel, author, text):

    # Hebt Abkuerzungen auf
    text = format.better(text)
    
    # Einmalige Berechnung von Listen für weitere Verwendung
    wordlist = split.towords((text + '.')[:-1])
    sentencelist = split.tosentence((text + '.')[:-1])

    DWL = dwl(wordlist)
    print("Durchschnittliche Wortlaenge: " + str(DWL))
    TTR = ttr(wordlist)
    print("Anzahl verschiedener Woerter im Verhaeltnis zu allen Woertern: " + str(TTR))
    HLR = hlr(wordlist)
    print("Anzahl einzelner Woerter im Verhaeltnis zu allen Woertern: " + str(HLR))
    DSL = dsl(sentencelist, wordlist)
    print("Durchschnittliche Anzahl von Woertern pro Satz: " + str(DSL))
    DSS = dss(sentencelist)
    print("Durchschnittliche Anzahl von Satzteilen pro Satz: " + str(DSS))

    return Signatur(titel, author, DWL, TTR, HLR, DSL, DSS)


# Durschnittliche Wortlänge
def dwl(wordlist):
    anzahlzeichen = 0

    for x in wordlist:
        y = len(x)
        anzahlzeichen += y

    return round((anzahlzeichen/len(wordlist)), 1)


# Anzahl verschiedener Woerter im Verhaeltnis zu Wortanzahl im Text
def ttr(wordlist):
    # Liste erzeugen um Woerter aufzuzeichen
    words = []

    # Wenn Wort in Liste dann weiter machen sonst in Liste hinzufuegen
    for x in wordlist:
        if x in words:
            continue
        else:
            words.append(x)

    # Laenge der Liste durch Laenge des Wortarrays
    return round(float(len(words) / len(wordlist)), 1)


# Wortanzahl die nur einmal vorkommt im Vergleich zu allen Woertern
def hlr(wordlist):
    words = {}

    for x in wordlist:
        if x in words:
            words[x] = words[x] + 1
        else:
            words[x] = 1

    singlewords = []
    for d in words:
        if words[d] == 1:
            singlewords.append(d)

    return round(float(len(singlewords) / len(wordlist)), 2)


# Durschschnittliche Anzahl Woerter pro Satz
def dsl(sentencelist, wordlist):
    return len(wordlist) // len(sentencelist)


# Durchschnittliche Anzahl von Satzteilen pro Satz
def dss(sentencelist):

    sentenceparts = 0
    seperatorchar = [',', ';', ':', ')', ' - ', ']', ' -- ']

    # Satzzeichen zaehlen
    # Mit jedem Satzzeichen wir der Satz geteilt
    for x in sentencelist:
        sentenceparts += 1  # Ein Satz besteht aus mindestens einem Satzteil
        for sep in seperatorchar:
            sentenceparts += x.count(sep)

    return sentenceparts // len(sentencelist)

