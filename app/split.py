import format


def tosentence(text):

    # Formatiert Dialoge, um als einzelne Saetze gesehen zu werden
    text = format.dialog(text)

    # Formatiert direkte Rede, um las einzelne Saetze verarbeitet zu werden
    text = format.direchtspeech(text)

    # Formatiert Saetze, sodass nur noch essentielle Satzzeichen vorhanden sind
    text = format.simplepunctuation(text)

    # Texte werden zusammen gerückt
    text = ' '.join(text.split())

    # Text wird in Saetze gesplittet
    newtext = str.split(text, '. ')

    # Entfernt leere Eintraege
    for x in newtext:
        x.strip(' \t\n\r')
        x.strip('- ')
        x.strip('-')
        x.strip('  ')
        x.strip(' ')

    return newtext


def towords(text):
    # Formatiert Dialoge, um als einzelne Saetze gesehen zu werden
    text = format.dialog(text)

    # Formatiert direkte Rede, um las einzelne Saetze verarbeitet zu werden
    text = format.direchtspeech(text)

    # Formatiert Saetze, sodass nur noch essentielle Satzzeichen vorhanden sind
    text = format.simplepunctuation(text)

    # Entfernt alle weiteren Satzzeichen
    text = format.nopunctuation(text)

    # Texte werden zusammen gerückt
    text = ' '.join(text.split())

    return str.split(text)
