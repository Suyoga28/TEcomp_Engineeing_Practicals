class TwoPassAssembler:
    def __init__(self):
        # Initialize the symbol table and intermediate code list
        self.symbol_table = {}
        self.intermediate_code = []
        self.location_counter = 0  # Used for addressing
        self.instruction_set = {'LOAD': '00', 'ADD': '01', 'SUB': '02', 'MUL': '03', 'DIV': '04', 'END': 'FF'}  # Example opcodes

    def pass_1(self, source_code):
        # Process each line of the source code
        for line in source_code:
            line = line.strip()  # Remove leading and trailing whitespace
            if not line or line.startswith(';'):  # Skip empty lines and comments
                continue
            
            # Split the line into parts
            parts = line.split()            
            if not parts:
                continue  # Skip to the next line if parts is empty
            
            if parts[0].endswith(':'):  # Label definition
                label = parts[0][:-1]  # Remove the ':' from the label
                self.symbol_table[label] = self.location_counter  # Add label to symbol table
                parts = parts[1:]  # Remove label from parts for further processing
            
            # Process instruction or directive
            if parts and parts[0] in self.instruction_set:  # It's an instruction
                self.intermediate_code.append((parts[0], parts[1] if len(parts) > 1 else None))
                self.location_counter += 1                             # Increment the location counter for each instruction
            elif parts and parts[0] == 'WORD':                         # Example directive
                self.intermediate_code.append(('WORD', parts[1]))
                self.location_counter += 1  # Increment for directives too

    def pass_2(self):
        machine_code = []
        # Translate intermediate code to machine code
        for instr in self.intermediate_code:
            opcode = self.instruction_set.get(instr[0])  # Get opcode for instruction
            if opcode:
                operand = instr[1]
                if operand and operand in self.symbol_table:  # If there's an operand
                    address = self.symbol_table[operand]
                    machine_code.append(f"{opcode} {address:02}")  # Format address
                elif operand and operand.isdigit():  # Handle immediate values
                    machine_code.append(f"{opcode} {int(operand):02}")  # Immediate value as operand
                else:
                    machine_code.append(f"{opcode} 00")  # No valid operand, default to 00
            elif instr[0] == 'WORD':
                machine_code.append(f"00 {instr[1]}")  # Assuming WORD just carries the value
        
        return machine_code

# Example usage
if __name__ == "__main__":
    # Sample source code for the assembler
    '''source_code = [
        "START:",
        "LOAD A",  # Adjusted to use LOAD
        "ADD B",
        "SUB C",
        "WORD 100",  # This is a directive
        "END"
    ]'''
    source_code = [
    "START:",
    "A    DS    3",
    "L1    MOVER    AREG    B",
    "ADD    AREG    C",
    "MOVEM    AREG    D",
    "D EQU    A+1",
    "L2    PRINT    D",
    "ORIGIN    A-1",
    "C    DC    5",
    "ORIGIN    L2+1",
    "STOP",
    "B    DC    19",
    "END    L1"
    ]
    assembler = TwoPassAssembler()
    
    # Pass I: Build symbol table and intermediate code
    assembler.pass_1(source_code)
    print("Symbol Table:", assembler.symbol_table)
    print("Intermediate Code:", assembler.intermediate_code)
    
    # Pass II: Generate machine code
    machine_code = assembler.pass_2()
    print("Machine Code:", machine_code)

