class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expr):
        try:
            if '=' in expr:
                var_name, value = expr.split('=')
                # Remove spaces and evaluate the expression
                self.variables[var_name.strip()] = eval(value, {}, self.variables)
            else:
                # This is only reached if there's no assignment, which shouldn't happen in this adjusted interpreter
                eval(expr, {}, self.variables)
        except Exception:
            print("syntax error!!")

    def execute_statement(self, statement):
        statement = statement.strip()
        if statement.startswith("print"):
            var_name = statement.split()[1]
            if var_name in self.variables:
                value = self.variables[var_name]
                print("TRUE" if value else "FALSE")
            else:
                print("syntax error!!")
        elif statement:x =
            self.evaluate_expression(statement)

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
