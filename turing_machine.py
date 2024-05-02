"""
Turing Machine class implementation for the Turing Machine Simulator
"""

class TuringMachine:
    def __init__(self, states=None, input_symbols=None, tape_symbols=None, transitions=None):
        self.states = states
        self.input_symbols = input_symbols
        self.tape_symbols = tape_symbols
        self.transitions = transitions
        self.current_state = 'q1'
        self.head = 0
        self.tape = ['_'] * 20

    def set_input(self, input_string):
        self.tape = list(input_string) + ['_'] * (20 - len(input_string))

    def get_transition(self, tape_symbol):
        return self.transitions[self.current_state].get(tape_symbol, None)

    def get_configuration(self, tape, head):
        return f"{''.join(tape[:head])}{self.current_state}{''.join(tape[head:])}"

    def get_state(self):
        return self.current_state

    def pretty_print(self, tape, head):
        """print head above the tape"""
        print(' '.join(tape), end=' ')
        print(f'| state: {self.current_state}')
        print('  ' * head + '^')

    def apply_transition(self, state=None, tape_symbol=None):
        if state is None:
            state = self.current_state
        if tape_symbol is None:
            tape_symbol = self.tape[self.head]
        self.pretty_print(self.tape, self.head)
        transition = self.get_transition(tape_symbol)
        new_state, new_tape_symbol, move = transition
        if new_state == None:
            new_state = state
        if new_tape_symbol == None:
            new_tape_symbol = tape_symbol
        if move == None:
            move = 'R'
        return new_state, new_tape_symbol, move

    def step(self):
        new_state, new_tape_symbol, move = self.apply_transition()
        self.tape[self.head] = new_tape_symbol
        if move == 'R':
            self.head += 1
        elif move == 'L':
            if self.head > 0:
                self.head -= 1

        self.current_state = new_state
        return self.current_state in {'q_accept', 'q_reject'}, self.current_state
