import chordprog.constants as const
import random


def random_chord_sequence():
    """
    Creates a random note sequence for a chord
    :return: List of random integers for a chord sequence
    """

    # Create a list that will contain the chord numbers
    chord_sequence = [random.randint(1, 6)]

    # Each loop, find the next value for the sequence
    for i in range(const.CHORD_SEQ_LEN - 1):  # Chord sequence is 4
        curr_val = 1
        last1_val = chord_sequence[-1]
        last2_val = 0
        last3_val = 0

        # If the sequence is long enough, initialize the previous values
        if len(chord_sequence) > 1:
            last2_val = chord_sequence[-2]

        if len(chord_sequence) > 2:
            last3_val = chord_sequence[-3]

        # Based on previous values in the sequence, change the current value
        if last1_val == 1:
            curr_val = random.randint(2, 6)

        elif last1_val == 2:
            if last2_val == 6 or last2_val == 4:
                curr_val = 5
            else:
                curr_val = random.choice([3, 5])

        elif last1_val == 3:
            curr_val = random.choice([4, 6])

        elif last1_val == 4:
            curr_val = random.choice([2, 5])

        elif last1_val == 5:
            if last3_val == 0:
                curr_val = random.choice([3, 6])
            else:
                curr_val = 1

        elif last1_val == 6:
            curr_val = random.choice([2, 4])

        chord_sequence.append(curr_val)

    return chord_sequence


def random_arp_sequence():
    """
    Creates a random note sequence for an arpeggio
    :return: List of random integers for an arpeggio sequence
    """

    # Create a list that will hold the note number order
    arp_sequence = [random.randint(0, 5)]

    while len(arp_sequence) != const.ARP_SEQ_LEN:  # Arpeggio sequence is 8
        curr_val = 0
        last_val = arp_sequence[-1]
        percentage = random.randint(1, 100)

        # If the current value is not at the start of a quarter beat
        # if len(arp_sequence) % 2 == 1:
        probability = [(15, 2), (30, 1), (10, 0), (30, -1), (15, -2)]
        # elif len(arp_sequence) % 2 == 0:
        #    probability = [(15, 2), (35, 1), (35, -1), (15, -2)]

        # Check the probability of each outcome from the list
        for pair in probability:
            percentage -= pair[0]
            if percentage <= 0:
                curr_val = last_val + pair[1]
                break

        if curr_val < 0 or 5 < curr_val:
            continue

        arp_sequence.append(curr_val)

    return arp_sequence
