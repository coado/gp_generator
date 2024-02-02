import random
from utils import Utils
from gpParser import GpParser
from traverseAdapter import TraverseAdapter

class Evolution(Utils):
    def __init__(self, state, fitness, config):
        self.state = state
        self.fitness = fitness
        self.config = config

    def _mutation(self, parent_index):
        parent_stack_copy = self.state.stack[parent_index][:]
        parent_stack_length = len(parent_stack_copy)
        
        for i in range(parent_stack_length):
            random_number = random.randint(0, 100)

            if random_number > self.config.mut_prob_per_node:
                continue

            token = parent_stack_copy[i]

            # If random token is a scope, input/output or equation, continue
            if (self.is_open_scope(token) or 
                self.is_close_scope(token) or
                self.is_input(token) or
                self.is_output(token) or
                self.is_equation(token)
            ):    
                continue

            elif self.is_operation(token):
                # Replace operation
                random_operation = self.choose_random_operation(token)
                parent_stack_copy[i] = random_operation
                # print(f"Mutated operation to from {token} to {random_operation} at index {i}")

            elif self.is_condition(token):
                # Replace condition
                random_condition = self.choose_random_condition(token)
                parent_stack_copy[i] = random_condition
                # print(f"Mutated condition to from {token} to {random_condition} at index {i}")
                
            
            elif self.is_if(token):
                # Replace if statement to while loop
                parent_stack_copy[i] = self.config.syntax['while']
                # print(f"Mutated if statement to while loop at index {i}")
                
            
            elif self.is_while(token):
                # Replace while loop to if statement
                parent_stack_copy[i] = self.config.syntax['if']
                # print(f"Mutated while loop to if statement at index {i}")
                
            elif self.is_logic(token):
                # Replace logic
                random_logic = self.choose_random_logic(token)
                parent_stack_copy[i] = random_logic
                # print(f"Mutated logic from {token} to {random_logic} at index {i}")

            elif self.is_constant(token):
                # Replace constant
                random_const = self.choose_random_const()
                parent_stack_copy[i] = random_const
                # print(f"Mutated constant from {token} to {random_const} at index {i}")

            elif self.is_variable(token):
                # Replace variable
                random_var_index = random.randint(0, len(self.state.variables[parent_index]) - 1)
                random_variable = self.state.variables[parent_index][random_var_index]
                parent_stack_copy[i] = random_variable
                # print(f"Mutated variable from {token} to {random_variable} at index {i}")


        return parent_stack_copy

    def _get_token_type(self, token):
        if self.is_block(token):
            return 'block'
        elif self.is_operation(token):
            return 'operation'
        elif self.is_condition(token):
            return 'condition'
        elif self.is_logic(token):
            return 'logic'
        elif self.is_not(token):
            return 'not'
        elif self.is_input(token):
            return 'input'
        elif self.is_output(token):
            return 'output'
        elif self.is_true(token):
            return 'true'
        elif self.is_false(token):
            return 'false'
        elif self.is_constant(token):
            return 'constant'
        elif self.is_variable(token):
            return 'variable'
        else:
            return 'unknown'

    def _analyze_stack(self, stack):
        stats = {
            "block": [],
            "operation": [],
            "condition": [],
            "logic": [],
            "not": [],
            "input": [],
            "output": [],
            "true": [],
            "false": [],
            "constant": [],
            "variable": [],
        }

        for i in range(len(stack)):
            token = stack[i]
            type = self._get_token_type(token)
            if type == 'unknown':
                continue
            stats[type].append(i)
                
        return stats
        
            
    def _crossover(self, parent1_index, parent2_index):
        parent_copy = self.state.stack[parent1_index][:]
        parent2_stack = self.state.stack[parent2_index]

        parent_copy_length = len(parent_copy)
        parent2_stack_length = len(parent2_stack)
        parent2_stats = self._analyze_stack(parent2_stack)

        # Get random index from parent1
        start_index = random.randint(0, parent_copy_length - 1)
        random_index = start_index
        qualified = []
        
        while len(qualified) == 0:
            # Try the neighbour
            random_index = (random_index + 1) % parent_copy_length
            if random_index == start_index:
                # No qualified tokens
                return parent_copy
            token = parent_copy[random_index]
            type = self._get_token_type(token)
            if type == 'unknown':
                continue
            qualified = parent2_stats[type]

        # Get random index from parent2
        random_index2 = random.choice(qualified)
           
        traverseAdapterParent1 = TraverseAdapter(parent_copy, random_index)
        traverseAdapterParent2 = TraverseAdapter(parent2_stack, random_index2)

        s1, e1 = traverseAdapterParent1.shallow_traverse()
        s2, e2 = traverseAdapterParent2.shallow_traverse()

        parent_copy = parent_copy[:s1] + parent2_stack[s2:e2] + parent_copy[e1:]

        return parent_copy
        

    def _tournament(self):
        best = float('-inf')
        best_indiv_index = 0

        for _ in range(self.config.tournament_size):
            random_indiv_index = random.randint(0, self.config.population - 1)
            fitness = self.state.get_fitness(random_indiv_index)
            if fitness > best:
                best = fitness
                best_indiv_index = random_indiv_index
        
        return best_indiv_index
    
    def negative_tournament(self):
        worst = float('inf')
        worst_indiv_index = 0

        for _ in range(self.config.tournament_size):
            random_indiv_index = random.randint(0, self.config.population - 1)
            fitness = self.state.get_fitness(random_indiv_index)
            if fitness < worst:
                worst = fitness
                worst_indiv_index = random_indiv_index
        
        return worst_indiv_index
    
    def stats(self, g):
        fitness_avg = -sum(self.state.fitness) / len(self.state.fitness)
        best_fitness = max(self.state.fitness)
        best_indiv_index = self.state.fitness.index(best_fitness)
        best_indiv = self.state.stack[best_indiv_index]
        gpParser = GpParser(best_indiv)
        indiv = gpParser.parse()
        print(f"Generation: {g} \nAvg_fitness: {fitness_avg} \nBest_fitness: {-best_fitness} \nBest_individual: {indiv}\n")

    def problem_solved(self):
        best_indiv_index = self.state.fitness.index(0)
        best_indiv = self.state.stack[best_indiv_index]
        gpParser = GpParser(best_indiv)
        indiv = gpParser.parse()
        print(f"\n\n\nFound solution: {indiv}\n\n")
        return 1 
    
    def evolve(self):
        for g in range(self.config.generations):
            self.stats(g)

            best_fitness = max(self.state.fitness)
            if best_fitness == 0:
                    return self.problem_solved()
    

            # print(f"Generation {g}")   

            for _ in range(self.config.population):
                evolution_type = self.get_random_evolution_type()

                if evolution_type == 'crossover':
                    # print(f"Individual {i} will be crossed over")
                    # TODO: What if parents are the same?
                    parent1_index = self._tournament()
                    parent2_index = self._tournament()
                    new_indiv = self._crossover(parent1_index, parent2_index)

                elif evolution_type == 'mutation':
                    indiv_index = self._tournament()
                    new_indiv = self._mutation(indiv_index)

                
                new_fitness = self.fitness.fitness_function(new_indiv, best_fitness)

                # Get worst individual and replace it with new individual
                offspring_index = self.negative_tournament()
                self.state.replace_indiv(offspring_index, new_indiv, new_fitness)
            
            # 2.2 SEED CORRECT VALUES
            if g == 10:
                print("SEED CORRECT VALUES")
                indiv_index = self.negative_tournament()
                self.state.stack[indiv_index] = ['=', 'var0', '1','=', 'var1', 'input', 'if', '<', 'var1', '1000', '{', '=', 'var0', '0', '}', 'if', '>=', 'var1', '2000', '{', '=', 'var0', '2', '}','output','var0']
                self.state.variables[indiv_index] = ['var0', 'var1']
                new_indiv_fitness = self.fitness.fitness_function(self.state.stack[indiv_index], 0)
                self.state.fitness[indiv_index] = new_indiv_fitness
                print("FINTESS: ", new_indiv_fitness)
                
            

                

                

                
            