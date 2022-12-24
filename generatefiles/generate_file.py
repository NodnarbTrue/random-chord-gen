import generatefiles.constants as const
import wave
from pydub import AudioSegment


def generate_chord_files(prog_list):
    """
    Creates .wav files for each chord in a chord progression
    :param prog_list: List of lists that hold the notes of a chord progression
    """

    for chord in range(len(prog_list)):  # len is 4
        # Initialize the final chord file starting with the bass noe
        note_path = const.NOTES_PATH + prog_list[chord][1] + ".wav"
        final_chord = AudioSegment.from_file(note_path)
        final_chord_path = const.PROCESS_PATH + "chord" + str(chord + 1) + ".wav"

        # Add the 3 other chord notes to the final chord
        for note in range(2, 5):
            note_path = const.NOTES_PATH + prog_list[chord][note] + ".wav"
            temp_note = AudioSegment.from_file(note_path)
            final_chord = final_chord.overlay(temp_note)

        final_chord.export(final_chord_path, format="wav")
        # CHECK TO SEE IF THE WAV FILES IS OKAY


def generate_prog_file(chord_input, prog_list, octave):
    """
    Creates a .wav file of the final chord progression
    :param chord_input: List of the inputs given by the user (key and scale)
    :param prog_list: List of lists that hold the notes of a chord progression
    :param octave: Integer of the general pitch of the notes
    """

    # Create the progression file for output
    final_prog_path = const.CHORDS_PATH + "Prog %(key)s %(scale)s %(octave)s %(a)s%(b)s%(c)s%(d)s.wav" \
                 % {"key": chord_input[0], "scale": chord_input[1], "octave": octave,
                    "a": prog_list[0][0], "b": prog_list[1][0], "c": prog_list[2][0], "d": prog_list[3][0]}
    final_prog = wave.open(final_prog_path, "w")
    final_prog.setnchannels(const.CHANNELS)
    final_prog.setsampwidth(const.SAMPLE_WIDTH)
    final_prog.setframerate(const.SAMPLE_RATE)

    # Loop through the chord files and add them onto the final one
    for i in range(1, 5):
        current_path = const.PROCESS_PATH + "chord" + str(i) + ".wav"
        current_chord = wave.open(current_path, "r")

        final_prog.writeframesraw(current_chord.readframes(const.HALF_NOTE_LEN))
        current_chord.rewind()
        final_prog.writeframesraw(current_chord.readframes(const.QUARTER_NOTE_LEN))
        current_chord.rewind()
        final_prog.writeframesraw(current_chord.readframes(const.QUARTER_NOTE_LEN))
        current_chord.rewind()


def generate_arp_file(chord_input, prog_list, octave, arp_list, bass_arp_list):
    """
    Creates a .wav file of the final arpeggio
    :param chord_input: List of the inputs given by the user (key and scale)
    :param prog_list: List of lists that hold the notes of a chord progression
    :param octave: Integer of the general pitch of the notes
    :param arp_list: List of notes in an arpeggio
    :param bass_arp_list: List of bass notes in an arpeggio
    """

    # Create the arp file
    arp_path = const.PROCESS_PATH + "arp" + ".wav"
    arp_file = wave.open(arp_path, "w")
    arp_file.setnchannels(const.CHANNELS)
    arp_file.setsampwidth(const.SAMPLE_WIDTH)
    arp_file.setframerate(const.SAMPLE_RATE)

    # Create the bass arp file
    bass_arp_path = const.PROCESS_PATH + "bass_arp" + ".wav"
    bass_arp_file = wave.open(bass_arp_path, "w")
    bass_arp_file.setnchannels(const.CHANNELS)
    bass_arp_file.setsampwidth(const.SAMPLE_WIDTH)
    bass_arp_file.setframerate(const.SAMPLE_RATE)

    # Add the notes to the arp file
    i = 0
    while i < len(arp_list):
        current_path = const.NOTES_PATH + arp_list[i] + ".wav"
        current_note = wave.open(current_path, "r")

        if (i + 1) % (len(arp_list) // 4) != 0 and arp_list[i] == arp_list[i + 1]:
            arp_file.writeframesraw(current_note.readframes(const.QUARTER_NOTE_LEN))
            i += 1
        else:
            arp_file.writeframesraw(current_note.readframes(const.EIGHTH_NOTE_LEN))
        current_note.rewind()
        i += 1
    arp_file.close()

    # Add the notes to the bass arp file
    i = 0
    while i < len(bass_arp_list):
        current_path = const.NOTES_PATH + bass_arp_list[i] + ".wav"
        current_note = wave.open(current_path, "r")

        bass_arp_file.writeframesraw(current_note.readframes(const.HALF_NOTE_LEN))
        current_note.rewind()
        bass_arp_file.writeframesraw(current_note.readframes(const.HALF_NOTE_LEN))
        current_note.rewind()
        i += 1
    bass_arp_file.close()

    # Combine the two files to make the final files
    final_arp_path = const.ARPS_PATH + "Arp %(key)s %(scale)s %(octave)s %(a)s%(b)s%(c)s%(d)s.wav" \
                     % {"key": chord_input[0], "scale": chord_input[1], "octave": octave,
                        "a": prog_list[0][0], "b": prog_list[1][0], "c": prog_list[2][0], "d": prog_list[3][0]}
    final_arp_file = AudioSegment.from_file(arp_path)
    final_arp_file = final_arp_file.overlay(AudioSegment.from_file(bass_arp_path))
    final_arp_file.export(final_arp_path, format="wav")
