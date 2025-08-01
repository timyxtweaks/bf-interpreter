# Brainfuck Interpreter

Jednostavan Brainfuck interpreter napisan u Pythonu.

## Autor
**timyx**

## Šta je ovo?

Brainfuck interpreter koji podržava svih 8 komandi:
- `+` - uvećaj vrijednost u trenutnoj ćeliji
- `-` - smanji vrijednost u trenutnoj ćeliji  
- `>` - pomjeri pokazivač udesno
- `<` - pomjeri pokazivač ulijevo
- `[` - ako je trenutna ćelija 0, skoči na komandu nakon odgovarajuće `]`
- `]` - ako trenutna ćelija nije 0, skoči nazad na odgovarajuću `[`
- `.` - ispiši karakter iz trenutne ćelije
- `,` - učitaj karakter u trenutnu ćeliju

## Kako pokrenuti

```bash
python brainfuck_interpreter.py
```

## Primjeri koda

**Hello World:**
```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

**Ispiši 'A':**
```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.
```

**Jednostavan brojač:**
```brainfuck
++++++++++[>++++++++++<-]>+++++.
```

## Karakteristike

- Memorija od 30,000 bajtova
- Provjera grešaka za nebalansane zagrade
- Interaktivni unos koda
- Sve poruke na bosanskom jeziku
- Kompaktan kod (manje od 100 linija)

## Kako na GitHub

1. Napravi folder za projekt
2. Ubaci `brainfuck_interpreter.py` i ovaj `README.md`
3. Pokreni:
```bash
git init
git add .
git commit -m "test"
git remote add origin https://github.com/tvoj-username/brainfuck-interpreter
git push -u origin main
```

## Licenca

Radi šta hoćeš s ovim kodom, samo spomeni autora.

---
*Napravljeno u Bosni 🇧🇦*# bf-interpreter
