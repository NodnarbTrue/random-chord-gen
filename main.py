# Program Function

# User will choose the scale they want their chords to be in
# --- The scale will be in the format (Letter) (Minor, Major)
# --- Example: C# Minor

# User can then choose the general octave range
# --- They can choose between 3 and 6
# --- The chords will be in the range of +1 or -1 octave

# The program will generate a random chord progression (notes and beat)
# --- 4 bars long
# --- Saved to a .wav file
# --- Print out the chord number sequence (and the notes in them)

from chordprog.create_lists import *
from chordprog.input_functions import *
from generatefiles.generate_file import *


if __name__ == '__main__':

    # Ask the user to input the key, scale, and octave
    chordInput = get_chord_input()
    octaveInput = get_octave_input()

    # Convert the key if it has a b into its # equivalent
    chordInput[0] = convert_key(chordInput[0])

    # Find the notes on the given scale
    scaleList = create_note_list(chordInput[0], chordInput[1], octaveInput)

    # Use the scale to generate a random chord progression (4 bars)
    progList = create_prog_list(scaleList)
    arpList = create_arp_list(progList)
    bassarpList = create_bass_arp_list(progList)

    # Print out the info
    print_info(scaleList, arpList, progList)

    # Create sub .wav files and combine them to create the final chord progression
    generate_chord_files(progList)
    generate_prog_file(chordInput, progList, octaveInput)

    # Use the chord progression list to create an arpeggio
    generate_arp_file(chordInput, progList, octaveInput, arpList, bassarpList)
