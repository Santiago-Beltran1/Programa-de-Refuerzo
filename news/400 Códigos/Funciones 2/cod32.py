class SantiagoMorse:
    SantiagoCod = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': '/'
    }

    @staticmethod
    def SantiagoTaMorse(SantiagoTexto):
        return ' '.join(SantiagoMorse.SantiagoCod.get(c.upper(), '') for c in SantiagoTexto)

SantiagoF = "David Santiago Beltran Pedraza"
print(F"Texto en morse: {SantiagoMorse.SantiagoTaMorse(SantiagoF)}")
