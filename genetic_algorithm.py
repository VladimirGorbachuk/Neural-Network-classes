class genetic_cross_breeding(self,strings=None,evaluations =None,
	                            n_children = 50, n_mutants = 5,
	                            n_elite =5, n_cycles = 50, mutagenity = 0.1
	                            training_x = None, training_y = None, estimation_func = None):
    def __init___:
        self.__children = strings
        self.__evaluation = evaluation
        self.__n_children = n_children
        self.__n_mutants = n_mutants
        self.__n_cycles = n_cycles
        self.__n_elite = elite
        self.__elite = self.gather_elite()
        self.__mutagenity = mutagenity
        self.__estimate = estimation_func
    def gather_elite(self):
        evaluated_children = zip (self.__evaluation, self.__children)
        self.elite = sorted (evaluated_children)[-__n_elite:]
    def __breed (self):
        #self.new_children = []
        for breeds in range(self.__n_children//2):
            [parent_a,parent_b] = random.choices(self.__children, weights = self.evaluation, k = 2)
            child_1 = [random.choice (weights) for weights in zip (parent_a,parent_b)]
            child_2 = [random.choice (weights) for weights in zip (parent_a,parent_b)]
            self.__new_childeren.append (child_1)
            self.__new_children.append (child_2)
       return
    def __mutate (self):
        for mutations in range(self.n_mutants):
            mutant = random.choice (self.new_children):
            mutated = []
            for weight in mutant:
                [weight_2] = random.choices ([weight, random.random ()], weights = [1,self.mutagenity])
                mutated.append (weight_2)
            self.__new_children.append (mutated)
    def __tournament_selection (self):
        for new_child in self.__new_children:
            contestant = random.choice(enumerate(self.__children))
            if self.__estimate (new_child) > self.__estimate(contestant [1])
                self.__children [contestant [0]] = new_child
    def generate (self):
