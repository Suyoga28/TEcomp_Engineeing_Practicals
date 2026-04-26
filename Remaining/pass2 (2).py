class TwoPassMacroProcessor:
    def __init__(self):
        # Macro Name Table (MNT) and Macro Definition Table (MDT)
        self.mnt = []  # Macro Name Table
        self.mdt = []  # Macro Definition Table
        self.intermediate_code = []  # Intermediate code
        self.macro_defining = False  # Flag for macro definition
        self.current_macro = None  # Current macro name being processed

    def pass_1(self, source_code):
        # Process each line of the source code
        for line in source_code:
            line = line.strip()  # Remove whitespace
            if not line or line.startswith(';'):  # Skip empty lines and comments
                continue
            
            # Detect macro definition
            if line.startswith('MACRO'):
                self.macro_defining = True
                self.current_macro = line.split()[1]  # Get macro name
                self.mnt.append((self.current_macro, len(self.mdt)))  # Add to MNT
                continue
            
            if self.macro_defining:
                # Add lines to MDT while defining the macro
                if line == 'END':
                    self.macro_defining = False
                    self.current_macro = None
                else:
                    self.mdt.append(line)  # Add macro body to MDT
                continue
            
            # If not in macro definition, add to intermediate code
            self.intermediate_code.append(line)

    def pass_2(self):
        expanded_code = []
        # Replace macro calls with their definitions
        for line in self.intermediate_code:
            # Check if the line is a macro call
            for macro_name, index in self.mnt:
                if line == macro_name:  # It's a macro call
                    # Add the corresponding macro definition from MDT to the expanded code
                    expanded_code.extend(self.mdt[index:index + self.mdt.count(macro_name)])  # Add corresponding MDT lines
                    break
            else:
                expanded_code.append(line)  # If not a macro call, add line as is
        return expanded_code

# Example usage
if __name__ == "__main__":
    # Sample source code for the macro processor
    source_code = [
        "MACRO ADD",
        "   LOAD A, 1",
        "   ADD A, B",
        "END",
        "MACRO SUB",
        "   LOAD A, 2",
        "   SUB A, B",
        "END",
        "START:",
        "ADD",  # Macro call
        "SUB",  # Another macro call
        "END"
    ]
    
    macro_processor = TwoPassMacroProcessor()
    
    # Pass I: Build MNT, MDT and intermediate code
    macro_processor.pass_1(source_code)
    print("Macro Name Table (MNT):", macro_processor.mnt)
    print("Macro Definition Table (MDT):", macro_processor.mdt)
    print("Intermediate Code:", macro_processor.intermediate_code)
    
    # Pass II: Generate expanded code
    expanded_code = macro_processor.pass_2()
    print("Expanded Code:", expanded_code)

