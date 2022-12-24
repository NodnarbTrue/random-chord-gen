import chordprog.constants as const
from chordprog.random_sequence import random_chord_sequence, random_arp_sequence


def create_note_list(key, scale, octave):
    """
    Creates a list of notes in a scale
    :param key: String that contains the key of the scale
    :param scale: String that determines whether the scale is a major or minor scale (M/m)
    :param octave: Integer that determines the general pitch of the notes
    :return: List of notes in a scale with their octaves
    """

    # Create a list with all possible notes, and an empty list to hold the notes in the current scale
    all_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_list = []

    # Shift all_notes until the key is the first element
    while all_notes.index(key) != 0:
        all_notes.append(all_notes.pop(0))

    # Create a list of notes in the current major/minor scale
    if scale == "M":
        for i in const.MAJOR_SCALE:
            note_list.append(all_notes[i])

    elif scale == "m":
        for i in const.MINOR_SCALE:
            note_list.append(all_notes[i])

    # Initialize trackers for octave increases
    octave_change = octave
    octave_increased = False

    # Loop through the current note list and add the octave of the note after each note
    for i in range(len(note_list)):
        if note_list[i][0] == "C" and octave_increased is False and i > 0:
            octave_increased = True
            octave_change += 1
        note_list[i] = note_list[i] + str(octave_change)

    # Get the last note of the scale, reduce its octave by 1, and put at the start of the list
    note_list.insert(0, note_list.pop(-1))
    note_list[0] = note_list[0][:-1] + str(int(note_list[0][-1]) - 1)

    return note_list


def create_chord_list(note_list, chord_root):
    """
    Creates a list of notes in a chord
    :param note_list: List that holds the notes in a scale
    :param chord_root: Integer that determines the root note of a chord in a scale
    :return: List of an octave, bass note, and triad notes of a chord
    """

    # Initialize the chord list that will contain the chord number, bass note, and the 3 notes of the chord
    bass_octave = int(note_list[chord_root][-1]) - 1
    bass_note = note_list[chord_root][:-1] + str(bass_octave)
    chord_list = [chord_root, bass_note]

    # Initialize values for the loop
    insert_index = 2
    looped = False
    current_note = chord_root

    # Find the note and place them into chord_list in the right order (low to high pitch)
    for i in range(const.CHORD_LEN):  # len is 3
        # If at the end of the scale, loop back
        if current_note >= const.SCALE_LEN:  # Scale is normally 7 notes long
            looped = True
            current_note -= const.SCALE_LEN

        # If the notes have already looped, insert in the middle instead of the end
        if looped is True:
            chord_list.insert(insert_index, note_list[current_note])
            insert_index += 1

        else:
            chord_list.append(note_list[current_note])

        current_note += 2

    return chord_list


def create_prog_list(note_list):
    """
    Creates a list containing all the notes in a chord progression
    :param note_list: List that holds the notes in a scale
    :return: List of lists, each containing the octave, bass note, and triad notes of a chord
    """

    # Create a list of lists (each list contains the chord number and the 3 keys for that chord)
    prog_list = []
    chord_sequence = random_chord_sequence()

    for i in chord_sequence:
        chord_list = create_chord_list(note_list, i)
        prog_list.append(chord_list)

    return prog_list


def create_arp_list(prog_list):
    """
    Creates a list containing notes for an arpeggio
    :param prog_list: List of lists that hold the notes of a chord progression
    :return: List of the notes in an arpeggio
    """

    arp_list = []
    note_sequence = random_arp_sequence()

    # Loop to create a list of notes for the arpeggio
    for i in range(const.CHORD_SEQ_LEN):  # len is 4
        current_notes = prog_list[i][2:5]  # get the 3 regular notes of the chord
        higher_notes = current_notes.copy()

        # Add the 3 chord notes with one higher octave to the list
        for elm in higher_notes:
            elm = elm[:-1] + str(int(elm[-1]) + 1)
            current_notes.append(elm)

        # Add the proper notes to the sequence
        for j in note_sequence:
            arp_list.append(current_notes[j])

    return arp_list


def create_bass_arp_list(prog_list):
    """
    Creates a list containing the bass notes for an arpeggio
    :param prog_list: List of lists that hold the notes of a chord progression
    :return: List of the bass notes in an arpeggio
    """

    bass_arp_list = []
    # bass_note_sequence = ???

    # Add the bass note of each chord to the list
    for chord in prog_list:
        bass_arp_list.append(chord[1])

    return bass_arp_list


def print_info(note_list, arp_list, prog_list):
    """
    Prints out the scale, arpeggio notes, and chord progression notes
    :param note_list: List that holds the notes in a scale
    :param arp_list: List of notes in an arpeggio
    :param prog_list: List of lists that hold the notes of a chord progression
    """

    print("==================================================")
    print("Scale:")
    print(note_list)
    print("==================================================")
    print("Arpeggio:")
    print(arp_list[0:8])
    print(arp_list[8:16])
    print(arp_list[16:24])
    print(arp_list[24:32])
    print("==================================================")
    print("Chord:")
    for i in range(len(prog_list[0])):
        for j in range(len(prog_list)):
            print(str(prog_list[j][i]) + "\t\t\t", end="")
        print("")
    print("==================================================")
