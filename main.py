from collections import deque

# Define the state class
class State:
    def __init__(self, farmer, fox, chicken, grain):
        self.farmer = farmer
        self.fox = fox
        self.chicken = chicken
        self.grain = grain

    # Method to check if the current state is valid
    def is_valid(self):
        # Check if the fox will eat the chicken
        if self.fox == self.chicken and self.farmer != self.fox:
            return False
        # Check if the chicken will eat the grain
        if self.chicken == self.grain and self.farmer != self.chicken:
            return False
        return True

    # Method to generate the next possible states
    def next_states(self):
        next_states = []
        # Check if the farmer is on the left side
        if self.farmer == 0:
            # Farmer crosses alone
            state = State(1, self.fox, self.chicken, self.grain)
            if state.is_valid():
                next_states.append(state)
            # Farmer with fox
            if self.fox == 0:
                state = State(1, self.fox ^ 1, self.chicken, self.grain)
                if state.is_valid():
                    next_states.append(state)
            # Farmer with chicken
            if self.chicken == 0:
                state = State(1, self.fox, self.chicken ^ 1, self.grain)
                if state.is_valid():
                    next_states.append(state)
            # Farmer with grain
            if self.grain == 0:
                state = State(1, self.fox, self.chicken, self.grain ^ 1)
                if state.is_valid():
                    next_states.append(state)
        else:
            # Farmer crosses alone
            state = State(0, self.fox, self.chicken, self.grain)
            if state.is_valid():
                next_states.append(state)
            # Farmer with fox
            if self.fox == 1:
                state = State(0, self.fox ^ 1, self.chicken, self.grain)
                if state.is_valid():
                    next_states.append(state)
            # Farmer with chicken
            if self.chicken == 1:
                state = State(0, self.fox, self.chicken ^ 1, self.grain)
                if state.is_valid():
                    next_states.append(state)
            # Farmer with grain
            if self.grain == 1:
                state = State(0, self.fox, self.chicken, self.grain ^ 1)
                if state.is_valid():
                    next_states.append(state)
        return next_states

    # Method to check if the current state is the goal state
    def is_goal(self):
        return self.farmer == 1 and self.fox == 1 and self.chicken == 1 and self.grain == 1

# Breadth-First Search algorithm
def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state.is_goal():
            return path + [state]
        if state not in visited:
            visited.add(state)
            for next_state in state.next_states():
                queue.append((next_state, path + [state]))

    return None

# Initial state: Farmer, Fox, Chicken, Grain (0 represents they are on the starting side)
initial_state = State(0, 0, 0, 0)
solution = bfs(initial_state)

# Print the solution
if solution:
    num_possible_states = sum([4 ** i for i in range(len(solution))])
    num_valid_states = len(solution)
    print("Number of possible states:", num_possible_states)
    print("Number of valid states:", num_valid_states)
    print("Solution:", [state.farmer * 1000 + state.fox * 100 + state.chicken * 10 + state.grain for state in solution])
    for i, state in enumerate(solution):
        print(f"+---+---+---+STEP [{i}]+---+---+---+")
        print("  +---+---+---+---+---+---+---+")
        for row in range(3):
            print("  |", end="")
            for col in range(7):
                if row == 0:  # Starting side
                    if col == 0 and not state.farmer:
                        print(" F ", end="|")
                    elif col == 2 and not state.fox:
                        print(" X ", end="|")
                    elif col == 4 and not state.chicken:
                        print(" C ", end="|")
                    elif col == 6 and not state.grain:
                        print(" G ", end="|")
                    else:
                        print("   ", end="|")
                elif row == 1:  # River
                    print("   ", end="|")
                else:  # Ending side
                    if col == 0 and state.farmer:
                        print(" F ", end="|")
                    elif col == 2 and state.fox:
                        print(" X ", end="|")
                    elif col == 4 and state.chicken:
                        print(" C ", end="|")
                    elif col == 6 and state.grain:
                        print(" G ", end="|")
                    else:
                        print("   ", end="|")
            print("\n  +---+---+---+---+---+---+---+")
        if i < len(solution) - 1:
            print()
else:
    print("No solution found.")
    