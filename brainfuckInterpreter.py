import sys
import getch
import fileinput


class brainfuckInterpreter:
    # Data Array
    dA = []
    # Instruction Array
    iA = []

    sizeCells = 0

    def __init__(self, sizeDataArray: int = 30000, sizeCells: int = 8) -> None:
        self.dA = [0 for i in range(sizeDataArray)]
        self.sizeCells = sizeCells

    def setInstructions(self, instructions: str) -> None:
        '''Sets the instructions in the form of a string.'''

        self.iA = list(instructions)

    def run(self) -> None:
        '''Executes the preset instructions.'''

        # Instruction Pointer
        iP = 0
        # Data Pointer
        dP = 0

        while iP < len(self.iA):
            instruction = self.iA[iP]

            if instruction == ">":
                dP += 1

            elif instruction == "<":
                dP -= 1

            elif instruction == "+":
                self.dA[dP] += 1

                if self.dA[dP] == 2 ** self.sizeCells:
                    self.dA[dP] = 0

            elif instruction == "-":
                self.dA[dP] -= 1

                if self.dA[dP] == -1:
                    self.dA[dP] = 2 ** self.sizeCells - 1

            elif instruction == ".":
                sys.stdout.write(chr(self.dA[dP]))

            elif instruction == ",":
                #char = input("input: ")[0]
                char = getch.getch()

                self.dA[dP] = ord(char)

            elif instruction == "[":
                if self.dA[dP] == 0:
                    bracketBalance = 1

                    while bracketBalance != 0:
                        iP += 1
                        
                        if self.iA[iP] == "[":
                            bracketBalance += 1
                        if self.iA[iP] == "]":
                            bracketBalance -= 1

            elif instruction == "]":
                if self.dA[dP] != 0:
                    bracketBalance = -1

                    while bracketBalance != 0:
                        iP -= 1

                        if self.iA[iP] == "[":
                            bracketBalance += 1
                        if self.iA[iP] == "]":
                            bracketBalance -= 1

            iP += 1


def main():
    if len(sys.argv) != 2:
        print("brainfuckInterpreter takes exactly one argument. The file to read the instructions from.")
        sys.exit()

    bfI = brainfuckInterpreter(sizeDataArray=30000, sizeCells=8)

    path = sys.argv[1]
    with open(path) as file:
        instructions = file.read()

    bfI.setInstructions(instructions)

    bfI.run()


if __name__ == "__main__":
    main()
