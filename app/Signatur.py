class Signatur:
    # Deklarierung eines Objektes
    def __init__(self, Titel='', Author='', DWL=0, TTR=0, HLR=0, DSL=0, DDS=0):
        self.Titel = Titel
        self.Author = Author
        self.DWL = DWL
        self.TTR = TTR
        self.HLR = HLR
        self.DSL = DSL
        self.DDS = DDS

    # Ausgabe eines Objektes
    # Titel und Author als String, Rest als Zahlen
    def __str__(self):
        return "'{0}', '{1}', {2}, {3}, {4}, {5}, {6}".format(
            self.Titel,
            self.Author,
            self.DWL,
            self.TTR,
            self.HLR,
            self.DSL,
            self.DDS)
