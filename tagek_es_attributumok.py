# -*- coding: utf-8 -*-
# Használat: be kell másolni a szkriptet a feldogozandó fájl mellé.
# Parancssorban el kell indítani, meg kell adni a fájlnevet, valamint azt, hogy az attribútumok értékeire is szükség van-e.

# meghívja az XML-feldolgozáshoz szükséges könyvtárat
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
# bekéri a fájlnevet
print('Melyik fájlt dolgozzam fel?')
filename = input()
# előállítja az XML-fát
tree = ET.parse(filename)
root = tree.getroot()
# listába rakja az összes elemet
tags = list(root.iter())
taglista = list('')
# megkérdezi, hogy az attribútumértékek is kellenek-e
print('Az attribútumok értékeit is kiírjam? (I/N)')
x = input()
# előállítja a kívánt listát
for elem in tags:
   if x == 'i':
      uj = elem.tag + ' ' + str(elem.items())
   else:
      uj = elem.tag + ' ' + str(elem.keys())
   taglista.append(uj)
# kiszedi a duplikátumokat
taglista = set(taglista)
# kiírja a listát névtér nélkül
for mind in taglista:
    mind = mind.split('}',1)
    print(mind[1].replace('{http://www.w3.org/XML/1998/namespace}','xml:'))
# új komment
