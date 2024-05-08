class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expr):
        try:
            # This will use Python's eval to interpret arithmetic expressions
            # and variable resolution in the self.variables dictionary
            return eval(expr, {}, self.variables)
        except:
            print("syntax error!!")
            return None

    def execute_statement(self, statement):
        statement = statement.strip()
        if statement.startswith("print "):
            # Handle print statements
            var_name = statement.split()[1].strip(';')
            if var_name in self.variables:
                print(self.variables[var_name])
            else:
                print("syntax error!!")
        else:
            # Handle assignments
            try:
                var_name, expr = statement.split('=', 1)
                var_name = var_name.strip()
                expr = expr.strip(';').strip()
                self.variables[var_name] = self.evaluate_expression(expr)
            except:
                print("syntax error!!")

    def run(self):
        print("Simple Python Interpreter. Type 'exit' to quit.")
        while True:
            input_line = input(">> ")
            if input_line == "exit":
                break
            statements = input_line.split(';')
            for statement in statements:
                if statement.strip():
                    self.execute_statement(statement)

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.run()
