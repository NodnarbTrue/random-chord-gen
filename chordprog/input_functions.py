import chordprog.constants as const


def get_chord_input():
    """
    Asks the user for input on the chord they want to generate
    :return: List of strings holding the key and scale type
    """

    keys = const.KEY_LIST
    semis = ["-", "#", "b"]
    scale = ["M", "m"]

    print("Enter the scale of the chord progression:\nFormat: [A, B, C, D, E, F, G][-, #, b] [M (Major), m (Minor)]")
    invalid = True

    while invalid is True:
        chord_input = str(input("Enter with correct format (e.g. 'C- M' for a C Major scale): "))

        if len(chord_input) != 4:
            continue
        invalid1 = keys.count(chord_input[0]) == 0
        invalid2 = semis.count(chord_input[1]) == 0
        invalid3 = scale.count(chord_input[3]) == 0
        invalid4 = chord_input[2] != " "
        invalid = invalid1 or invalid2 or invalid3 or invalid4

    return chord_input.split()


def get_octave_input():
    """
    Asks the user for input on the octave they want to have
    :return: Integer of the general octave scale of the chord
    """

    print("Enter the general octave range (3 - 6)")
    invalid = True

    while invalid is True:
        octave_input = str(input("Enter with correct format (e.g. '5'): "))

        if not octave_input.isdigit() or len(octave_input) != 1:
            continue
        invalid1 = int(octave_input) < 3
        invalid2 = 6 < int(octave_input)
        invalid = invalid1 or invalid2

    return int(octave_input)


def convert_key(key):
    """
    Converts a into its sharp equivalent
    :param key: String that contains the key of the scale
    :return: String that holds sharp equivalent of the key
    """

    key_list = const.KEY_LIST
    new_key = key

    # If a key is given with "b", convert it to its "#" equivalent
    if key[1] == "-":
        new_key = key[0]

    elif key[1] == "#":
        if key == "B#" or key == "E#":
            new_index = key_list.index(key[0]) + 1
            new_key = key_list[new_index]

    elif key[1] == "b":
        new_index = key_list.index(key[0]) - 1
        if new_index == -1:
            new_index = len(key_list) - 1
        new_key = key_list[new_index]
        if new_key != "B" and new_key != "E":
            new_key += "#"

    return new_key
