"""
This file contains utility functions that are used in the main program.
The function load_transitions_from_csv is used to read a CSV file containing
transitions and load them into a dictionary that can be used by the Turing
Machine class.
"""

import csv


def load_transitions_from_csv(filename):
    transitions = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].split('#')[0].split('//')[0].strip()
            # Strip out inline comments (after a '#' or '//' in any part of the row)
            if len(row) > 5:
                # remove the extra comments
                row = row[:5]
            print(row)
            # Skip empty rows or rows that have become empty after removing comments
            if not row:
                continue
            try:
                current_state, input_symbol, new_state, new_symbol, move = row
            except ValueError:
                print(f"Error: Invalid row: {row}")
                continue
            # Ensure no trailing spaces interfere
            current_state, input_symbol, new_state, new_symbol, move = row

            if current_state not in transitions:
                transitions[current_state] = {}

            transitions[current_state][input_symbol] = (
                new_state, new_symbol, move)

    return transitions
