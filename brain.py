from warnings import warn


class BrainfuckInterpreter:
    def __init__(self, cell_size=255, memory_size=3000):
        self.program = ""
        self.programPointer = 0
        self.validProgramCharacters = set("<>+-[].,")

        self.memorySize = memory_size
        self.cellSize = cell_size
        self.memoryTape = [0] * self.memorySize
        self.memoryPointer = 0

        self.indentCounter = []

    def check_program_pointer(self):
        # Keep memory Pointer inside memory limits
        if self.memoryPointer > len(self.memoryTape) - 1:
            self.memoryPointer = 0
        elif self.memoryPointer < 0:
            self.memoryPointer = len(self.memoryTape) - 1

    def check_memory_cell(self):
        # Keep current memory cell between 0 and 255
        if self.memoryTape[self.memoryPointer] > self.cellSize:
            self.memoryTape[self.memoryPointer] = 0
        elif self.memoryTape[self.memoryPointer] < 0:
            self.memoryTape[self.memoryPointer] = self.cellSize

    def validate_program(self):
        self.program = ''.join([c if c in self.validProgramCharacters else '' for c in self.program])

        if self.program.count("[") != self.program.count("]"):
            if self.program.count("[") > self.program.count("]"):
                warn("[ Missing matching Closing Bracket",)
            else:
                warn("] Missing matching Opening Bracket")

    def read_program_from_string(self, program_string):
        self.program = program_string
        self.validate_program()

    def read_program_from_file(self, file_path):
        with open(file_path, "r") as file:
            self.program = file.read()
        self.validate_program()

    def jump_to_matching_bracket(self):
        bracket_count = 1
        current_position = self.programPointer + 1
        while bracket_count != 0:
            code = self.program[current_position]
            if code == ']':
                bracket_count -= 1
            elif code == '[':
                bracket_count += 1
            current_position += 1
        self.programPointer = current_position - 1

    def run_program(self):
        while self.programPointer < len(self.program):
            code = self.program[self.programPointer]

            if code == '<':
                self.memoryPointer -= 1
            elif code == '>':
                self.memoryPointer += 1
            elif code == '+':
                self.memoryTape[self.memoryPointer] += 1
            elif code == '-':
                self.memoryTape[self.memoryPointer] -= 1
            elif code == '.':
                print(chr(self.memoryTape[self.memoryPointer]), end="")
            elif code == ',':
                input_chr = ''
                while len(input_chr) < 1:
                    input_chr = input('>')[0]

                self.memoryTape[self.memoryPointer] = ord(input_chr)
            elif code == '[':
                if self.memoryTape[self.memoryPointer] != 0:
                    self.indentCounter.append(self.programPointer)
                else:
                    self.jump_to_matching_bracket()
            elif code == ']':
                if self.memoryTape[self.memoryPointer] != 0:
                    self.programPointer = self.indentCounter[-1]
                else:
                    self.indentCounter.pop(len(self.indentCounter)-1)

            self.check_program_pointer()
            self.check_memory_cell()
            self.programPointer += 1


if __name__ == "__main__":
    brain = BrainfuckInterpreter(cell_size=255)
    brain.read_program_from_file('program.txt')
    #brain.read_program_from_string("--<-<<+[+[<+>--->->->-<<<]>]<<--.<++++++.<<-..<<.<+.>>.>>.<<<.+++.>>.>>-.<<<+.")
    brain.run_program()
