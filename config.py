class Config:
    def __init__(self):

        self.data = 'k_10.txt'
        self.heuristic = 'regression'

        self.max_interpreter_steps = 1000

        self.min_inital_vars = 1
        self.max_initial_vars = 4

        self.min_const_val = -1000
        self.max_const_val = 1000

        self.min_blocks = 2
        self.max_blocks = 5

        self.max_blocks_depth = 2
        self.max_operations_depth = 2
        self.max_logic_depth = 2

        # between 0 and 1
        # 0 means no complexity
        # 1 means max complexity
        self.complexity_of_operations = 0.3
        self.complexity_of_logic = 0.4

        self.population = 10
        self.generations = 100
        self.tournament_size = 3

        self.not_prob = 30
        self.evolution_prob = {
            'crossover': 50,
            'mutation': 50
        }

        # max 100
        self.mut_prob_per_node = 10
        
        self.block_prob = {
            'equation': 20,
            'while': 0,
            'if': 50,
            'output': 30,
        }

        # Use more vars or consts?
        self.operation_prob = {
            'variable': 50,
            'constant': 0,
            'input': 50,
        }

        self.condition_prob = {
            'operation': 0,
            'true': 33,
            'false': 33,
            'input': 34,
        }

        self.equation_prob = {
            'operation': 0,
            'logic': 50,
            'input': 50,
        }

        self.syntax = {
            'if': 'if',
            'while': 'while',
            'open_scope': '{',
            'close_scope': '}',
            'equation': '=',
            'operations': ['+', '-', '*', '//'],
            'conditions': ['<', '>', '==', '!=', '>=', '<='],
            'logic': ['and', 'or', '^'],
            'not': 'not',
            'variable_prefix': 'var',
            'input': 'input',
            'output': 'output',
            'true': 'true',
            'false': 'false',

            # TODO: add "not", "false", "true"

            # TODO: Fix empty blocks

            
        }

    def assert_probabilities(self):
        assert sum(self.block_prob.values()) == 100, "Block probabilities should sum up to 100"
        assert sum(self.operation_prob.values()) == 100, "Expression probabilities should sum up to 100"
        assert sum(self.evolution_prob.values()) == 100, "Evolution probabilities should sum up to 100"
        assert sum(self.equation_prob.values()) == 100, "Equation probabilities should sum up to 100"
        assert sum(self.condition_prob.values()) == 100, "Condition probabilities should sum up to 100"