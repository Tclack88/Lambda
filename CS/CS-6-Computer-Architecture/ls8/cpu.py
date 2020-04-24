"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0 # process counter
        self.ram = [0]*256 # Initialize 8 byte ram (array of 0's)
        self.reg = [0] * 8 # Initialize register values (array of 0's)
        self.sp = 7 # stack pointer, set it to last (arbitrary) spot in register
        self.fl = 0 # flag (indicating if a jump of some sort is happening)
        self.reg[self.sp] = 0xf4
        # map the bytes to a class method
        self.instruction_map = {
            0b10000010: self.handle_LDI,  # LDI (load instruction)
            0b00000001: self.handle_HLT,  # HLT (Hault)
            0b01000111: self.handle_PRN,  # PRN (print)
            0b10100000: self.handle_ADD,  # ADD (add)
            0b10100010: self.handle_MUL,  # MUL (multiply)
            0b01000101: self.handle_PUSH, # PUSH (push)
            0b01000110: self.handle_POP,  # POP (pop)
            0b01010000: self.handle_CALL, # CALL (call)
            0b00010001: self.handle_RET   # RET (return)
            }


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:
        program_file = sys.argv[1]
        with open(program_file) as f:
            for instruction in f:
                # each line is a string if a comment (#) is inline of an
                # instruction, remove it and return the 0th item (the instr.)
                # otherwise a line that is a comment or blank, ignore it
                instruction  = instruction.split('#')[0].strip()
                if instruction == '':
                    continue
                # append to ram
                self.ram_write(address, int(instruction, 2))
                address += 1
    
    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

    def handle_LDI(self, adr, val):
        """Set register address to value (given at self.pc + 1 and +2  respectively"""
        self.reg[adr] = val # set specified register variable to value

    def handle_PRN(self, register, _):
        """print value stored in register (given in self.pc + 1"""
        val = self.reg[register]
        print(val)

    def handle_HLT(self, *args):
        """Exit the program"""
        print('program exiting')
        exit()

    def handle_ADD(self, val1, val2):
        """ pass on val1 and val2 (at self.pc +1 and + 2 respectively) 
        to alu for operation"""
        self.alu('ADD', val1, val2)

    def handle_MUL(self, val1, val2):
        """ take val 1 and val 2 (at self.pc +1 and + 2 respectively)
        pass to alu for operation """
        self.alu('MUL',val1, val2)

    def handle_PUSH(self, register, _):
        """Increment stack pointer, place registry value onto stack"""
        self.reg[self.sp] += 1 # increment stack pointer
        value = self.reg[register] # get register to be moved 
        address = self.reg[self.sp] # Get address of newly incremented stack
                                    # pointer where we will write
        self.ram_write(address, value)

    def handle_POP(self, register, _):
        """pop item from stack into register, decrement stack pointer
        this function accepts the register were we will store from the top of the stack"""
        address = self.reg[self.sp] # Get address on top of stack
        value = self.ram_read(address) # Get value stored at that address
        self.reg[register] = value # move value into specified register
        self.reg[self.sp] -= 1 # decrement stack pointer
    
    def handle_CALL(self, register, _):
        self.reg[self.sp] -= 1 # decrement stack pointer (prepare to push)
        self.ram_write(self.reg[self.sp], self.pc + 2) # push return addr
        self.pc = self.reg[register] # change pc to value specified in register

    def handle_RET(self, *args):
        """to last instruction on the stack"""
        # set return address to pc from top of stack
        self.pc = self.ram_read(self.reg[self.sp])
        self.reg[self.sp] += 1 # increment stack pointer (i.e. pop off top)

    def run(self):
        """Run the CPU."""
        while True:
            ir = self.ram_read(self.pc)
            # map ir to function and execute
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            function = self.instruction_map[ir]
            if function == None: # handle errors without silence
                print(f'Instructiona: {int(ir, 2)}, not understood')
                self.instruction_map[0] # call exit instruction
            function(operand_a,operand_b)

            # instruction length stored as top most significant bits
            # performing a logical "and" to get those and shifting over
            # returns the amount we shift to get to next instruction
            instr_len = ((ir & 0b11000000) >> 6) + 1
            self.fl = ((ir & 0b00010000) >> 4)
            if self.fl:
                self.fl = 0 # reset
            else: # ignore flag and increment pc
                self.pc += instr_len

