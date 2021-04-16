import shelve
import calculate
import storage
import compare
import window


def start():
    while True:
        # Oeffnet Tkinter Operation um Textdatei zu bekommen
        filename = window.getfilename()

        # Wenn gecancelt wird gefragt, ob das Programm beendet werden soll.
        if filename == '':
            askabort = input("Moechtest du das Programm beenden? (Y/N) ")
            if askabort is 'N':
                continue
            else:
                print("Auf Wiedersehen.")
                break

        with open(filename, 'r') as f:
            text = f.read()

        # Titel und Autor werden nochmal einzelnd eingeben
        # Erwingt Eingabe
        while True:
            titel = input("Bitte gebe den Titel des Textes ein: ")
            if titel == '':
                continue
            else:
                break
        while True:
            author = input("Bitte gebe den Autor des Textes ein: ")
            if author == '':
                continue
            else:
                break


        # Werte werden errechnet
        print("Bitte warten...")
        textsignatur = calculate.signatur(titel, author, text)
        print(textsignatur)

        # Text und Werte werden abgespeichert, um spaeter mit anderen Texten veglichen zu werden
        storage.save(textsignatur)

        # Abfrage, ob nur Signatur errechnet werden sollte, ob jetzt verglichen werden soll oder neuer Text eingescannt.
        answer = input("Aehnlichen Autoren finden? (Y/N) ")
        if answer == 'Y':
            with shelve.open('storage') as sto:
                if len(sto) < 2:
                    print("Leider gibt es noch keine vorigen Texte")
                else:
                    compare.toAll(textsignatur)

        answertwo = input("Weiteren Text erfassen? (Y/N) ")
        if answertwo == 'Y':
            continue
        else:
            print("Auf Wiedersehen")
            break


if __name__ == '__main__':
    start()
