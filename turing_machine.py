"""
Turing Machine class implementation for the Turing Machine Simulator
"""
from AudioVisualSynth.music import generate_and_play_note
DEFAULT_INPUT_SYMBOLS = {'0', '1'}
DEFAULT_TAPE_SYMBOLS = {'0', '1', '_', 'x', 'y'}

class TuringMachine:
    """
    Turing Machine class for the Turing Machine Simulator.
    """
    def __init__(self, states=None, input_symbols=None, tape_symbols=None, transitions=None):
        self.states = states
        self.input_symbols = input_symbols
        self.tape_symbols = tape_symbols
        self.transitions = transitions
        self.current_state = 'q1'
        self.head = 0
        self.tape = ['_'] * 20
        self.tempo_file = "note_durations.txt"

    def set_input(self, input_string):
        """
        Set the input string for the Turing Machine.
        """
        if ' ' in input_string:
            input_string = input_string.split(' ')
        self.tape = list(input_string) + ['_'] * (20 - len(input_string))

    def get_transition(self, tape_symbol):
        """
        Get the transition for the current state and tape symbol.
        """
        if self.current_state not in self.transitions:
            return None
        return self.transitions[self.current_state].get(tape_symbol, None)

    def get_configuration(self, tape, head):
        """
        Get the configuration of the Turing Machine.
        """
        return f"{''.join(tape[:head])}{self.current_state}{''.join(tape[head:])}"

    def get_state(self):
        """
        Get the current state of the Turing Machine.
        """
        return self.current_state

    def pretty_print(self, tape, head):
        """print head above the tape"""
        print(' '.join(tape), end=' ')
        print(f'| state: {self.current_state}')
        print('  ' * head + '^')

    def apply_transition(self, state=None, tape_symbol=None):
        """
        Apply the transition for the current state and tape symbol.
        """
        state = state or self.current_state
        tape_symbol = tape_symbol or self.tape[self.head]

        if "," in tape_symbol:
            self.process_chord(tape_symbol)
        else:
            self.process_note(tape_symbol)

        return self.get_transition_result(tape_symbol, state)

    def process_chord(self, tape_symbol):
        """
        Process a chord from the input string.
        """
        with open(self.tempo_file, "r") as f:
            lines = f.readlines()
            chord = [int(i) for i in tape_symbol.split(",")]
            self.last_chord = [str(i) for i in chord]
            tempo = float(lines[self.head].split(": ")[1])
            print(f"Chord = {chord}, Tempo = {tempo}")
            generate_and_play_note(chord, tempo)

    def process_note(self, tape_symbol):
        """
        Process a note from the input string.
        """
        with open('note_durations.txt', 'r') as f:
            lines = f.readlines()
            if self.head < len(lines):
                line = lines[self.head]
                tempo = float(line.split(': ')[1])  # Extract the tempo from the line
                print(f'Note = {tape_symbol}, Tempo = {tempo}')
                self.last_chord = [tape_symbol]
                generate_and_play_note(int(tape_symbol), tempo)  # Pass the tempo to the function

    def get_transition_result(self, tape_symbol, state):
        """
        Get the result of applying the transition for the current state and tape symbol.
        """
        transition = self.get_transition(tape_symbol)
        if transition is None:
            return state, tape_symbol, 'R'

        new_state, new_tape_symbol, move = transition
        new_state = new_state or state
        new_tape_symbol = new_tape_symbol or tape_symbol
        move = move or 'R'
        return new_state, new_tape_symbol, move

    def step(self):
        """
        Perform a single step of the Turing Machine.
        """
        new_state, new_tape_symbol, move = self.apply_transition()
        self.tape[self.head] = new_tape_symbol
        self.move_head(new_state, move)
        self.current_state = new_state
        return self.current_state in {'q_accept', 'q_reject'}, self.current_state

    def move_head(self, new_state, move):
        """
        Move the head of the Turing Machine.
        """
        if new_state not in ['q_accept', 'q_reject']:
            if move == 'R':
                self.head += 1
            elif move == 'L' and self.head > 0:
                self.head -= 1