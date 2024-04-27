from turing_machine import TuringMachine
from turing_machine_app import TuringMachineApp
from utils import load_transitions_from_csv

DEFAULT_INPUT_SYMBOLS = {'0', '1'}
DEFAULT_TAPE_SYMBOLS = {'0', '1', '_', 'x', 'y'}


if __name__ == "__main__":
    input_symbols = {'0', '1'}
    tape_symbols = {'0', '1', '_', 'x', 'y'}
    transitions = load_transitions_from_csv('a3.csv')
    states = set(transitions.keys())
    tm = TuringMachine(states, DEFAULT_INPUT_SYMBOLS,
                       DEFAULT_TAPE_SYMBOLS, transitions)
    app = TuringMachineApp(tm)
    app.run()
