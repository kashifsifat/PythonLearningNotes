#NATO Phonetic Alphabet Converter 00
i = str(input("Input: "))

npa = {
    "a":"Alfa",
    "b":"Bravo",
    "c":"Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "q":"Quebec",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "v":"Victor",
    "w":"Whiskey",
    "x":"X-ray",
    "y":"Yankee", 
    "z":"Zulu",
    " ":" ",
    ".":".",
    ",":",",
    }

for letters in i:
    print (npa[letters])
