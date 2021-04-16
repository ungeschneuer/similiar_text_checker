from re import sub


def better(text):
    # Abkuerzungen
    text = abbreviations(text)
    # Datum
    text = sub(r"(\d+)\.\s?(\w+)\.?\s?(\d+)", r"\1/\2/\3", text)
    # Saetze mit einem Buchstaben (andere Abkuerzungen)
    text = sub(r"\.\s(\w+)\.\s", r"\1", text)

    return text


def abbreviations(text):
    abbrevdic = {'a. a. O.': 'am angegegbenen Ort',
                  'Abb.': 'Abbildung',
                  'Abh.': 'Abhandlung',
                  'Abk.': 'Abkürzung',
                  'Abs.': 'Absatz',
                  'Adv.': 'Adverb',
                  'afrik.': 'afrikanisch',
                  'ahd.': 'althochdeutsch',
                  'amerik.': 'amerikanisch',
                  'Anat.': 'Anatomie',
                  'Akk.': 'Akkusativ',
                  'allg.': 'allgemein',
                  'Archit.': 'Architektur',
                  'argent.': 'argentinisch',
                  'Astrol.': 'Astrologie',
                  'Astron.': 'Astronomie',
                  'Bankw.': 'Bankwesen',
                  'bayr,': 'bayrisch',
                  'Bd.': 'Bande',
                  'bes.': 'besonders',
                  'Bez.': 'Bezeichnung',
                  'Bf.': 'Bahnhof',
                  'Bgb.': 'Bergbau',
                  'Biol.': 'Biologie',
                  'Bot.': 'Botanik',
                  'bspw.': 'beispielsweise',
                  'B.A.': 'Bachelor of Arts',
                  'B. A.': 'Bachelor of Arts',
                  'B.S.': 'Bachelor of Science',
                  'B. S.': 'Bachelor of Science',
                  'B.Sc.': 'Bachelor of Science',
                  'B. Sc.': 'Bachelor of Science',
                  'Buchw.': 'Buchwesen',
                  'bzw.': 'beziehungsweise',
                  'ca.': 'circa',
                  'Chem.': 'Chemie',
                  'chin.': 'chinesisch',
                  'd.h.': 'das heißt',
                  'd. h.': 'das heißt',
                  'd. i.': 'das ist',
                  'Dat.': 'Dativ',
                  'Dipl.': 'Diplom',
                  'Dr.': 'Doktor',
                  'dt.': 'deutsch',
                  'Dtschl.': 'Deutschland',
                  'dän.': 'dänisch',
                  'eigtl': 'eigentlich',
                  'Elektr.': 'Elektrotechnik',
                  'elektr.': 'elektrische',
                  'engl.': 'englisch',
                  'etc.': 'etcetera',
                  'europ.': 'europäisch',
                  'evtl.': 'eventuell',
                  'e.V.': 'eigetragener Verein',
                  'e. V.': 'eigetragener Verein',
                  'engl': 'englisch',
                  'evang.': 'evangelisch',
                  'Ez.': 'Einzahl',
                  'f.': 'folgende',
                  'ff.': 'fortfolgende',
                  'Fr.': 'Frau',
                  'franz.': 'französisch',
                  'Frk.': 'Frankreich',
                  'frz.': 'französisch',
                  'Forstw.': 'Forstwesen',
                  'Fot.': 'Fotografie',
                  'geb.': 'geboren',
                  'gegr': 'gegründet',
                  'Gen.': 'Genitiv',
                  'Geol.': 'Geologie',
                  'Ggs.': 'Gegensatz',
                  'ggf.': 'gegebenfalls',
                  'gleichbed.': 'gleichbedeutend',
                  'got.': 'gotisch',
                  'goth.': 'gotisch',
                  'grch.': 'griechisch',
                  'Hbf.': 'Hbf.',
                  'Hdt.': 'Hundert',
                  'hebr.': 'hebräisch',
                  'Hr.': 'Herr',
                  'Hrsg.': 'Herausgeber',
                  'Hst.': 'Hauptstadt',
                  'i. Allg.': 'im Allgemeinen',
                  'i. Bes.': 'im Besonderen',
                  'i. d. R.': 'in der Regel',
                  'i. e. S.': 'im engeren Sinne',
                  'i. e. F.': 'im erweiteter Fassung',
                  'i. w. S.': 'im weiteren Sinne',
                  'idg.': 'indogermanisch',
                  'intr.': 'intransitiv',
                  'it.': 'italienisch',
                  'jap.': 'japanisch',
                  'jmd.': 'jemand',
                  'jmdm.': 'jemandem',
                  'jmdn.': 'jemanden',
                  'jmds.': 'jemandes',
                  'Jh.': 'Jahrhundert',
                  'jahrh.': 'Jahrhundert',
                  'jh.': 'Jahrhundert',
                  'k. W.': 'kommende Woche',
                  'kath.': 'katholisch',
                  'Konj.': 'Konjunktiv',
                  'Kunstw.': 'Kunstwort',
                  'Kurzw.': 'Kurzwort',
                  'Landw.': 'Landwirtschaft',
                  'lat.': 'lateinisch',
                  'lfd. J.': 'laufendes Jahr',
                  'Lit.': 'Literatur',
                  'luth.': 'lutherisch',
                  'm. M. n.': 'meiner Meinung nach',
                  'M.A.': 'Master of Arts',
                  'M. A.': 'Master of Arts',
                  'M.S.': 'Master of Science',
                  'M. S.': 'Master of Science',
                  'Math.': 'Mathematik',
                  'Med.': 'Medizin',
                  'mhd.': 'mittelhochdeutsch',
                  'mind.': 'mindestens',
                  'Mio.': 'Millionen',
                  'Mitgl.': 'Mitgl',
                  'Mr.': 'Mister',
                  'Mrs.': 'Missus',
                  'Ms.': 'Miss',
                  'MwSt.': 'Mehrwertsteuer',
                  'Mwst.': 'Mehrwertsteuer',
                  'Myth.': 'Mythologisch',
                  'Mz.': 'Mehrzahl',
                  'n. Chr.': 'nach Christus',
                  'n.Chr.': 'nach Christus',
                  'n. V.': 'nach Vereinbarung',
                  'nachm.': 'nachmittags',
                  'natsoz.': 'nationalsozialistisch',
                  'nddt.': 'niederdeutsch',
                  'ndrl.': 'niederländisch',
                  'norw.': 'norwegisch',
                  'Nom.': 'Nominativ',
                  'Nr.': 'Nummer',
                  'o. Ä.': 'oder Ähnliches',
                  'o.Ä.': 'oder Ähnliches',
                  'österr.': 'österreichisch',
                  'Österr.': 'Österreich',
                  'Part. II': 'Partizip II',
                  'Philos.': 'Philosophie',
                  'Phys.': 'Physik',
                  'Pl.': 'Plural',
                  'Plur.': 'Plural',
                  'port.': 'portugiesisch',
                  'portug.': 'portugiesisch',
                  'Präp.': 'Präposition',
                  'Pron': 'Pronomen',
                  'Psych.': 'Psychologie',
                  'Rechtsw.': 'Rechtswesen',
                  'refl.': 'reflexiv',
                  'relig.': 'religiös',
                  'Relig.': 'Religion',
                  'S.': 'Seite ',
                  's. a.': 'siehe auch',
                  's.a.': 'siehe auch',
                  's. o.': 'siehe oben',
                  's.o.': 'siehe oben',
                  's. u.': 'siehe unten',
                  's.u.': 'siehe unten',
                  'scherzh.': 'scherzhaft',
                  'schw.': 'schweizerisch',
                  'Seew.': 'Seewesen',
                  'skand.': 'skandinavisch',
                  'Sing.': 'Singular',
                  'Soziol.': 'Soziologie',
                  'Sprachw.': 'Sprachwissenschaft',
                  'Std.': 'Stunden',
                  'tägl.': 'täglich',
                  'tschech.': 'tschechisch',
                  'Tsd.': 'Tausend',
                  'Theol.': 'Theologie',
                  'u.': 'und',
                  'u.a.': 'unter anderem',
                  'u.na.': 'unter anderem',
                  'u.Ä.': 'und Ähnliches',
                  'u. Ä.': 'und Ähnliches',
                  'u.dgl.': 'und dergleichen',
                  'u. dgl.': 'und dergleichen',
                  'ugs.': 'umgangssprachlich',
                  'urspr.': 'ursprünglich',
                  'übertr': 'übertragen',
                  'U.S.A.': 'United States of America',
                  'USA': 'United States of America',
                  'usw.': 'und so weiter',
                  'v. Chr.': 'vor Christus',
                  'v.Chr.': 'vor Christus',
                  'vgl.': 'vergleiche',
                  'Vgl.': 'Vergleiche',
                  'vorm.': 'vormittags',
                  'Wirtsch.': 'Wirtschaft',
                  'Wiss.': 'Wissenschaft',
                  'z.B.': 'zum Beispiel',
                  'z. B.': 'zum Beispiel',
                  'z.T.': 'zum Teil',
                  'z. T.': 'zum Teil',
                  'z.Zt.': 'zur Zeit',
                  'z. Zt.': 'zur Zeit',
                  'zz.': 'zur Zeit',
                  'zzt.': 'zur Zeit',
                  'Zool.': 'Zoologie',
                  }

    for key in abbrevdic.keys():
        if key in text:
            text = str.replace(text, key, abbrevdic[key])

    return text


# Formatiert Dialoge, um als einzelne Saetze gesehen zu werden
def dialog(text):
    dialog = ['.\n\n\n', '\n\n\n', '.\n', '!\"\n', '?\"\n', '.\"\n', '!«\n', '?«\n', '.«\n', '!\'\n', '?\'\n', '.\'\n', ']\n']
    for dia in dialog:
        text = str.replace(text, dia, '. ')

    return text


# Formatiert direkte Rede, um weiter verarbeitet zu werden
def direchtspeech(text):

    directspeechone = ['!",', '?",', '.",', '!«,', '?«,', '.«,', '!\',', '?\',', '\'.,', '!_,', '?_,', '._,', ]
    for dirspe in directspeechone:
        text = str.replace(text, dirspe, ',')

    directspeechtwo = ['!"', '?"', '."', '!«', '?«', '.«', '!\'', '?\'', '\'.', '_.', '._']
    for dirspetwo in directspeechtwo:
        text = str.replace(text, dirspetwo, '.')

    return text


# Formatiert Saetze, sodass nur noch essentielle Satzzeichen vorhanden sind
def simplepunctuation(text):

    charactersone = [' ... ', '...', '\a', '\b', '\f', '\n', '\r', '\t', '\v', '--', '´ ', ' - ', '  ', '\xa0']
    for chaone in charactersone:
        text = str.replace(text, chaone, ' ')

    characterstwo = ['*', '#', '`', '´', '~', '=', '+', '_', '<SC>', '</SC>']
    for chatwo in characterstwo:
        text = str.replace(text, chatwo, '')

    charactersthree = ['?', '!']
    for chathree in charactersthree:
        text = str.replace(text, chathree, '.')

    return text


# Formatiert Saetze, sodass gar keine Satzzeichen mehr vorhanden sind
def nopunctuation(text):

    charactersone = [' --', ' - ' ' _', '_ ']
    for chaone in charactersone:
        text = str.replace(text, chaone, ' ')

    characterstwo = ['--', ' -', '(_', '_)', '^-', ',', ';', ':', '"', '[', ']',
                     '»', '«', '<', '>', '\'', '(', ')']
    for chatwo in characterstwo:
        text = str.replace(text, chatwo, '')

    punctuations = ['?', '!', '.']
    for punc in punctuations:
        text = str.replace(text, punc, '')
    # Now, Punc is dead

    return text
