class TwoPassAssembler:
    def __init__(self):
        self.symbol_table = {}
        self.intermediate_code = []
        self.location_counter = 0
        self.instruction_set = {
            'MOVER': '00', 'MOVEM': '01', 'ADD': '02', 'SUB': '03', 'PRINT': '04', 'STOP': 'FF'
        }

    def pass_1(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith(';'):  # Skip comments or empty lines
                    continue

                parts = line.split()
               
                # Check if the first token is a label (not in instruction set or directives)
                if parts[0] not in self.instruction_set and parts[0] not in {"START", "DS", "DC", "ORIGIN", "EQU", "STOP"}:
                    label = parts[0]
                    self.symbol_table[label] = self.location_counter
                    parts = parts[1:]  # Remove label from parts for further processing
                else:
                    label = None

                opcode = parts[0]
                operand = parts[1] if len(parts) > 1 else None

                # Process each opcode and directive
                if opcode == 'START':
                    self.location_counter = int(operand) if operand is not None else 0
                
                elif opcode in self.instruction_set:
                    # Handle instructions
                    self.intermediate_code.append((self.location_counter, opcode, operand))
                    self.location_counter += 1
                
                elif opcode == 'DS':  # Define storage
                    self.symbol_table[operand] = self.location_counter
                    self.location_counter += int(parts[2])
                
                elif opcode == 'DC':  # Define constant
                    self.symbol_table[operand] = self.location_counter
                    self.intermediate_code.append((self.location_counter, 'DC', parts[2]))
                    self.location_counter += 1
                
                elif opcode == 'ORIGIN':
                    # Set location counter to a specific address or relative position
                    origin_value = operand
                    if '+' in origin_value or '-' in origin_value:
                        label, offset = origin_value.split('+') if '+' in origin_value else origin_value.split('-')
                        offset = int(offset) if '+' in origin_value else -int(offset)
                        self.location_counter = self.symbol_table.get(label, 0) + offset
                    else:
                        self.location_counter = int(origin_value) if origin_value.isdigit() else self.symbol_table.get(origin_value, self.location_counter)
                
                elif opcode == 'EQU':
                    # EQU sets a label to a specific value
                    self.symbol_table[label] = int(operand) if operand.isdigit() else self.symbol_table.get(operand, 0)

    def display_symbol_table(self):
        return self.symbol_table

    def display_intermediate_code(self):
        return self.intermediate_code

# Example usage
assembler = TwoPassAssembler()
assembler.pass_1('input.txt')
print("Symbol Table:", assembler.display_symbol_table())
print("Intermediate Code:", assembler.display_intermediate_code())
