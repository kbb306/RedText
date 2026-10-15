import sys

class HexText():
    set1 = {
    1: " ", 2: "E", 3: "T", 4: "A",
    5: "O", 6: "I", 7: "N", 8: "S",
    9: "R", 10: "H", 11: "L", 12: "D",
    13: "C", 14: "U"}

    set2 = {
        1: "M", 2: "F", 3: "P", 4: "G",
        5: "W", 6: "Y", 7: "B", 8: "V",
        9: "K", 10: "X", 11: "J", 12: "Q",
        13: "Z", 14: "?"
        }
    master = {False : set1, True: set2}

    @staticmethod
    def decode(input):
        output = ""
        shift = False
        for c in input:
            n = int(c)
            if n == 15:
                shift = not shift
                continue
            output += HexText.master[shift][n]
        return output

    @staticmethod
    def revlookup(inDict,val):
        return next((key for key, value in inDict.items() if value == val),None)

    @staticmethod
    def encode(input):
        outlist = []
        shift = False

        for c in input.upper():
            if c not in HexText.master[shift].values():
                if c not in HexText.master[not shift].values():
                    raise ValueError(f"Unsupported character: {c!r}")

                outlist.append(15)
                shift = not shift

            n = HexText.revlookup(HexText.master[shift], c)
            outlist.append(n)

        return outlist  

if len(sys.argv) < 3:
    print("""Usage: hexText.py -[e | d] input """)
    sys.exit()
else:
    match sys.argv[1]:
        case "-e": 
            print(HexText.encode(sys.argv[2]))
        case "-d":
            print(HexText.decode(sys.argv[2]))
        case _: 
            print("""Usage: hexText.py -[e | d] input """)
            sys.exit()



