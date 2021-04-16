import shelve
from Signatur import Signatur


def save(textsignatur):
    with shelve.open('storage') as sto:
        sto[textsignatur.Titel] = {'author': textsignatur.Author, 'dwl': textsignatur.DWL,
                                   'ttr': textsignatur.TTR, 'hlr': textsignatur.HLR, 'dsl': textsignatur.DSL,
                                   'dds': textsignatur.DDS}


def read():
    with shelve.open('storage') as sto:
        for keys, values in sto.items():
            print(keys, values)


def getbytitel(titel):
    with shelve.open('storage') as sto:
        if titel in sto.keys():
            return Signatur(titel, sto[titel]['author'], sto[titel]['dwl'], sto[titel]['ttr'], sto[titel]['hlr'],
                            sto[titel]['dsl'], sto[titel]['dds'])
        else:
            print("Diese Signatur existiert noch nicht")


def showauthor(author):
    with shelve.open('storage.db') as sto:
        for x in sto.keys():
            savedauthor = sto[x]['author']
            if author == savedauthor:
                print(sto[x])
            else:
                print('Dieser Titel wurde noch nicht verarbeitet.')

