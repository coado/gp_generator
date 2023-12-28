from config import Config
from utils import Utils

class GpParser(Utils):
    def __init__(self, data, config=Config()):
        super().__init__(config)
        self.data = data
        self.iterator = 0
        self.length = len(data)
        self.result = ''

    def _increment_iterator(self):
        self.iterator += 1

    def _current_token(self):
        return self.data[self.iterator]

    def _next_token(self):
        self._increment_iterator()
        return self._current_token()

    def _add_to_result(self, parsed_string):
        self.result += parsed_string

    def _parse_expression(self):
        expression_token = self._current_token()

        self._increment_iterator()
        left_side = self.traverse()
        self._increment_iterator()
        right_side = self.traverse()

        parsed = f"({left_side} {expression_token} {right_side})"
        return parsed
    
    def _parse_operation(self):
        return self._parse_expression()
    
    def _parse_condition(self):
        return self._parse_expression()

    def _parse_logic(self):
        return self._parse_expression()

    def _parse_equation(self):
        left_side = self._next_token()
        self._increment_iterator()
        right_side = self.traverse()
        
        parsed = f"{left_side} = {right_side};"
        return parsed
        

    def _parse_output(self): 
        output_token = self._current_token()
        variable_token = self._next_token()
        parsed = f"{output_token} {variable_token};"
        return parsed
    
    def _parse_not(self):
        not_token = self._current_token()
        self._increment_iterator()
        expression = self.traverse()

        parsed = f"({not_token} {expression})"
        return parsed
    
    def _parse_conditional_block(self):
        block_token = self._current_token()
        self._increment_iterator()
        condition = self.traverse()

        self._increment_iterator()
        scope = self._traverse_scope()

        parsed = f"{block_token} ({condition}) {scope}"
        return parsed
    
    def _parse_while(self):
        return self._parse_conditional_block()
    
    def _parse_if(self):
        return self._parse_conditional_block()

    
    def _traverse_scope(self):
        open_scope = self._current_token()
        self._increment_iterator()

        content = ''
        while not self.is_close_scope(self._current_token()):
            content += self.traverse()
            self._increment_iterator()

        close_scope = self._current_token()
        parsed = f"{open_scope} {content} {close_scope}"
        return parsed

    def traverse(self):
        token = self._current_token()

        if self.is_equation(token):
            return self._parse_equation()
        elif self.is_output(token):
            return self._parse_output()
        elif self.is_logic(token):
            return self._parse_logic()
        elif self.is_if(token):
            return self._parse_if()
        elif self.is_while(token):
            return self._parse_while()
        elif self.is_not(token):
            return self._parse_not()
        elif self.is_condition(token):
            return self._parse_condition()
        elif self.is_operation(token):
            return self._parse_operation()
        else:
            return token 

    def parse(self):
        while self.iterator < self.length:
            parsed = self.traverse()
            self._add_to_result(parsed)
            self._increment_iterator()

        return self.result


# # read from output.txt
# with open('output.txt', 'r') as f:
#     data = f.read()

# data = [elem.strip().replace("'", "") for elem in data.strip()[1:-1].split(',')]
data = ['=', 'var1', '+', '-', '*', '4', '5', '6', '7', 'if', '<', 'var3', '10', '{', '=', 'var3', 'input', 'while', 'not', 'and', 'false', '<', '4', '5', '{', 'output', '5', '}', '}']
data2 = ['while', '<', '4', '5', '{', 'output', '5', '}']
gpParser = GpParser(data)
res = gpParser.parse()
print("RES: ", res)