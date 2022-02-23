class bfTranspiler:
    # Cell Pointers for named cells
    cellPts = {}
    # Lengths of strings
    strLns = {}
    # Current Data Pointer
    currentDP = int

    # Name prefix for cells belonging to a string
    # Char 0 of string test would be stored in cell _s_test_0
    strPrefix = "_s_"

    def __init__(self):
        pass

    def transpile(self):
        bf = ""
        self.currentDP = 0

        # self.nameCell("c")

        # bf += self.setCell("c", ord("H"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("e"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("l"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("l"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("o"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord(" "))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("W"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("o"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("r"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("l"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("d"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("!"))
        # bf += self.outCell("c")
        # bf += self.setCell("c", ord("\n"))
        # bf += self.outCell("c")

        self.nameString("s1")
        self.nameString("s2")

        bf += self.setString("s1", "Hello World! Nice to meet you :)\n")
        bf += self.outString("s1")

        bf += self.setString("s2", "Pretty Cool\n")
        bf += self.outString("s2")

        bf += self.setString("s1", "Bye World!\n")
        bf += self.outString("s1")

        return bf

    def nameString(self, strName: str) -> None:
        self.strLns[strName] = 0

    def setString(self, strName: str, string: str) -> str:
        bf = ""

        self.strLns[strName] = len(string)

        for strChr in range(0, len(string)):
            cellName = self.strPrefix + strName + "_" + str(strChr)

            bf += self.setCell(cellName, ord(string[strChr]))

        return bf

    def outString(self, strName: str) -> str:
        bf = ""

        for strChr in range(0, self.strLns[strName]):
            cellName = self.strPrefix + strName + "_" + str(strChr)

            bf += self.outCell(cellName)

        return bf

    def outCell(self, cell: str) -> str:
        bf = ""

        p = self.cellPts[cell]
        bf += self.moveDP(p)

        bf += "."

        return bf

    def setCell(self, cell: str, value: int) -> str:
        bf = ""

        self.nameCell(cell)
        bf += self.incrementCell(cell, value)

        return bf

    def incrementCell(self, cell: str, value: int) -> str:
        bf = ""

        p = self.cellPts[cell]
        bf += self.moveDP(p)

        bf += "+" * value

        return bf

    def decrementCell(self, cell: str, value: int) -> str:
        bf = ""

        p = self.cellPts[cell]
        bf += self.moveDP(p)

        bf += "-" * value

        return bf

    def moveDP(self, p: int) -> str:
        bf = ""

        if self.currentDP < p:
            distance = p - self.currentDP
            bf += ">" * distance
        elif p < self.currentDP:
            distance = self.currentDP - p
            bf += "<" * distance

        self.currentDP = p

        return bf

    def nameCell(self, cell: str) -> None:
        '''Stores a pointer to a Cell in cellP.'''

        if len(self.cellPts) == 0:
            self.cellPts[cell] = 0
            return

        maxCellP = max(self.cellPts.values())
        self.cellPts[cell] = maxCellP+1


def main():
    bfT = bfTranspiler()

    print(bfT.transpile())


if __name__ == "__main__":
    main()
