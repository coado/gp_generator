import random
from config import Config
from state import State

class TinyGPGenerator:
    def __init__(self, config=Config()):
        self.config = config
        self.state = State(self.config.syntax)

    def _generate_expression(self, depth=0):
        if depth > self.config.max_expressions_depth or random.random() < (1 - self.config.complexity_of_expressions):
            return self.state.get_random_variable()
        else:
            # Choose an arithmetic expression
            operation = self.state.get_random_operation()

            left = self._generate_expression(depth + 1)
            right = self._generate_expression(depth + 1)
            return f'({left} {operation} {right})'

    def _generate_condition(self):
        # Generate and save a condition
        condition = self.state.get_random_condition()

        left = self._generate_expression()
        right = self._generate_expression()
        return f'{left} {condition} {right}'
    
    # Create random number of variables with random values from the range
    def _generate_initial_variables(self):
        for _ in range(random.randint(self.config.min_inital_vars, self.config.max_initial_vars)):
            self.state.create_variable_with_initial_value(self.config.min_var_initial_value, self.config.max_var_initial_value)

    def _print_config_probabilities(self):
        prev = 0
        for key, value in self.config.prob.items():
            prob = value - prev
            prev = value
            print(f'{key}: {prob}')


    def _generate_statement(self, depth=0):
        content = ''
        
        if depth > self.config.max_statements_depth:
            return content
        
        number_of_statements = random.randint(self.config.min_number_of_statements, self.config.max_number_of_statements)
        print('number_of_statements: ', number_of_statements)

        for _ in range(number_of_statements):
            random_number = random.randint(1, 100)

            # Generate variable declaration
            if random_number < self.config.prob['variable']:
                variable, init_value = self.state.create_variable_with_initial_value(self.config.min_var_initial_value, self.config.max_var_initial_value)
                content += f'int {variable} = {init_value};\n'
            
            # Generate while loop
            elif random_number < self.config.prob['while_loop']:
                while_loop_syntax = self.state.get_while_loop()
                condition = self._generate_condition()
                open_scope_syntax = self.state.get_open_scope()
                content += f'{while_loop_syntax} ({condition}) {open_scope_syntax}\n'
                content += self._generate_statement(depth + 1)
                close_scope_syntax = self.state.get_close_scope()
                content += f'{close_scope_syntax}\n'

            # Generate operation
            elif random_number < self.config.prob['operation']:
                variable = self.state.get_random_variable()
                expression = self._generate_expression()
                content += f'{variable} = {expression};\n'
            
            # Generate if statement
            elif random_number < self.config.prob['if_statement']:
                if_statement_syntax = self.state.get_if_statement()
                condition = self._generate_condition()
                open_scope_syntax = self.state.get_open_scope()
                content += f'{if_statement_syntax} ({condition}) {open_scope_syntax}\n'
                content += self._generate_statement(depth + 1)
                close_scope_syntax = self.state.get_close_scope()
                content += f'{close_scope_syntax}\n'
        
        return content

    def _generate_program(self):
        self._generate_initial_variables()
        program = ''
        
        for var in self.state.variables:
            program += f'int {var} = {self.state.values[var]};\n'
        
        
        content = self._generate_statement()
        program += content

        return program
    
    def run(self):
        self._print_config_probabilities()
        program = self._generate_program()
        print("stack: ", self.state.stack)
        return program
        

if __name__ == "__main__":
    generator = TinyGPGenerator()
    generated_program = generator.run()
    print("\n")
    print("GENERATED PROGRAM: \n")
    print(generated_program)