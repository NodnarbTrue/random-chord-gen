Random Chord Generator
======================


Description
-----------
The project will generate random chord progressions and arpeggios (in .wav files) based on information inputted by the user.


Installation and Running
------------------------
For the project to work, the python libraries must be imported: random, wave, and pydub. In order for pydub to work, ffmpeg must also be installed.

To run the project, run the main.py file and follow the printed instruction (entering the key, scale, and octave the chord should be generated in).

Once the main.py file is run and the input is given, the desire chord and arpeggio .wav files will be put in the "Output" folder.


Using the Project
-----------------
1. Run the main.py file

2. Enter the desired key and scale of the chord (e.g. "C- M" = C Major scale, "D# m" = D# Minor scale)

3. Enter the general octave range of the chord (integers 3 - 6)

4. Open the "Output" file to view results, the file name will be: [Arp/Chord] [Key] [M/m] [Octave] [4 Chord Values] (e.g. "Arp F# m 1625.wav")


Credits
-------
Developed by Brandon Trieu