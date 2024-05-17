"""
This module contains the function midi_to_tm, which converts a MIDI file to a Turing machine.
"""

import mido
from turing_machine import TuringMachine, DEFAULT_INPUT_SYMBOLS, DEFAULT_TAPE_SYMBOLS

def initialize_variables():
    """
    Initialize the variables used in the midi_to_tm function.
    """
    states = set(['q1', 'q_accept', 'q_reject'])
    transitions = {'q1': {}, 'q_accept': {}, 'q_reject': {}}
    first_note = None
    last_note = None
    input_string = []
    note_on_time = {}
    tempo = mido.bpm2tempo(60)
    prev_note = None
    chord = []
    prev_time = 0
    current_time = 0
    return states, transitions, first_note, last_note, input_string, note_on_time, tempo, prev_note, chord, prev_time, current_time

def process_note_on(msg, filter, current_time, prev_time, chord, input_string, first_note, last_note, states, transitions, prev_note, note_on_time):
    """
    Process a note_on message from a MIDI file.
    """
    if filter and (msg.note < 50 or msg.note > 81):
        return prev_time, chord, first_note, last_note, states, transitions, prev_note
    note_str = str(msg.note)
    note_on_time[note_str] = current_time
    if prev_time != current_time:
        if chord:
            input_string.append(','.join(chord))
            chord = []
        prev_time = current_time
    chord.append(note_str)
    if first_note is None:
        first_note = note_str
    last_note = note_str
    states.add(note_str)
    if note_str not in transitions:
        transitions[note_str] = {}
    if prev_note is not None:
        transitions[prev_note][note_str] = (note_str, 'X', 'R')
    prev_note = note_str
    return prev_time, chord, first_note, last_note, states, transitions, prev_note

def process_note_off(msg, current_time, note_on_time):
    """
    Process a note_off message from a MIDI file.
    """
    note_str = str(msg.note)
    if note_str in note_on_time:
        duration = (current_time - note_on_time[note_str]) / 1000.0
        del note_on_time[note_str]

def midi_to_tm(midi_file, filter=False):
    """
    Convert a MIDI file to a Turing machine.
    """
    mid = mido.MidiFile(midi_file)
    states, transitions, first_note, last_note, input_string, note_on_time, tempo, prev_note, chord, prev_time, current_time = initialize_variables()
    note_on_time = {}
    for msg in mid:
        if msg.type == 'set_tempo':
            tempo = msg.tempo
        current_time += mido.tick2second(msg.time, mid.ticks_per_beat, tempo)
        if current_time > 60:  # break the loop after 60 seconds
            break
        if msg.type == 'note_on':
            prev_time, chord, first_note, last_note, states, transitions, prev_note = process_note_on(msg, filter, current_time, prev_time, chord, input_string, first_note, last_note, states, transitions, prev_note, note_on_time)
        if msg.type == 'note_off':
            process_note_off(msg, current_time, note_on_time)

    if chord:
        input_string.append(','.join(chord))

    transitions['q1'][first_note] = (first_note, 'X', 'R')
    transitions[last_note]['q_accept'] = ('q_accept', 'X', 'R')
    input_string = ' '.join(input_string)
    try:
        with open('input_string.txt', 'w') as f:
            f.write(input_string)
    except:
        raise Exception("Could not write to input_string.txt")
    return TuringMachine(states, DEFAULT_INPUT_SYMBOLS, DEFAULT_TAPE_SYMBOLS, transitions)