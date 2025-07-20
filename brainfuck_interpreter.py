#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brainfuck Interpreter
Autor: timyx
"""

def pronadji_odgovarajucu_zagradu(kod, pozicija, smer):
    """
    Trazi odgovarajucu zagradu u kodu
    """
    brojac = 0
    i = pozicija
    
    while 0 <= i < len(kod):
        if kod[i] == '[':
            brojac += smer
        elif kod[i] == ']':
            brojac -= smer
        
        if brojac == 0:
            return i
        
        i += smer
    
    return -1

def pokreni_kod(brainfuck_kod):
    """
    Ova funkcija pokrece brainfuck kod
    """
    memorija = [0] * 30000
    memorijski_pokazivac = 0
    kod_pokazivac = 0
    
    validni_karakteri = "+-><[].,`"
    ociscen_kod = ''.join(char for char in brainfuck_kod if char in validni_karakteri)
    
    if not ociscen_kod:
        print("Nema validnih komandi u kodu!")
        return False
    
    # provjeri da li su zagrade ok
    balans_zagrada = 0
    for char in ociscen_kod:
        if char == '[':
            balans_zagrada += 1
        elif char == ']':
            balans_zagrada -= 1
        if balans_zagrada < 0:
            print("Neispravan kod - zatvorena zagrada ] bez otvorene [!")
            return False
    
    if balans_zagrada != 0:
        print("Nebalansane zagrade!")
        return False
    
    print("Pokretam program...")
    print("-" * 40)
    
    try:
        # glavna petlja
        while kod_pokazivac < len(ociscen_kod):
            komanda = ociscen_kod[kod_pokazivac]
            
            if komanda == '+':
                memorija[memorijski_pokazivac] = (memorija[memorijski_pokazivac] + 1) % 256
                
            elif komanda == '-':
                memorija[memorijski_pokazivac] = (memorija[memorijski_pokazivac] - 1) % 256
                
            elif komanda == '>':
                memorijski_pokazivac += 1
                if memorijski_pokazivac >= 30000:
                    print("Memorijski pokazivac je van granica!")
                    return False
                    
            elif komanda == '<':
                memorijski_pokazivac -= 1
                if memorijski_pokazivac < 0:
                    print("Memorijski pokazivac je van granica!")
                    return False
                    
            elif komanda == '.':
                print(chr(memorija[memorijski_pokazivac]), end='')
                
            elif komanda == ',':
                try:
                    unos = input()
                    if unos:
                        memorija[memorijski_pokazivac] = ord(unos[0])
                    else:
                        memorija[memorijski_pokazivac] = 10
                except KeyboardInterrupt:
                    print("\nProgram prekinut od strane korisnika.")
                    return False
                    
            elif komanda == '[':
                if memorija[memorijski_pokazivac] == 0:
                    nova_pozicija = pronadji_odgovarajucu_zagradu(ociscen_kod, kod_pokazivac, 1)
                    if nova_pozicija == -1:
                        print("Nije pronadjena zatvarajuca zagrada ]!")
                        return False
                    kod_pokazivac = nova_pozicija
                    
            elif komanda == ']':
                if memorija[memorijski_pokazivac] != 0:
                    nova_pozicija = pronadji_odgovarajucu_zagradu(ociscen_kod, kod_pokazivac, -1)
                    if nova_pozicija == -1:
                        print("Nije pronadjena otvarajuca zagrada [!")
                        return False
                    kod_pokazivac = nova_pozicija
            
            kod_pokazivac += 1
            
    except KeyboardInterrupt:
        print("\nProgram prekinut od strane korisnika.")
        return False
    except Exception as e:
        print(f"Neocekivana greska: {e}")
        return False
    
    print("\nProgram zavrsen!")
    return True

def glavni_meni():
    """glavni meni"""
    print("=" * 50)
    print("    BRAINFUCK INTERPRETER - timyx")
    print("=" * 50)
    print("Komande: + - > < [ ] . ,")
    print("-" * 50)
    
    while True:
        print("\nOpcije:")
        print("1. Unesi brainfuck kod")
        print("2. Izadji")
        
        izbor = input("Izbor (1-2): ").strip()
        
        if izbor == '1':
            print("\nUnesi kod:")
            kod = input("BF> ")
            if kod.strip():
                pokreni_kod(kod)
            else:
                print("Prazan kod.")
                
        elif izbor == '2':
            print("Cao!")
            break
            
        else:
            print("Neispravan izbor!")

# pokretanje
if __name__ == "__main__":
    glavni_meni()
