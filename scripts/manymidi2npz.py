#!/usr/bin/python
# modified from https://github.com/salu133445/musegan/issues/51


from pypianoroll import Multitrack
import numpy as np
import os

# Parameters
SRC_DIR="/home/azure/musegan/data/classical-2_0-0"
FILENAMES = [] # The input MIDI filenames
RESULT_FILENAME= './classical-2_0-0.npz' # The resulting filename
N_TRACKS = 2
BEAT_RESOLUTION = 12 # The beat resolution

# Initialize an empty list to collect the results
results = []

# Find all the midi files
for root, dirs, files in os.walk(SRC_DIR):
    for file in files:
        if file.endswith(".mid"):
            FILENAMES.append(os.path.join(root, file))


# Iterate through all the MIDI files
for filename in FILENAMES:
    
    # Parse the MIDI file into multitrack pianoroll
    try:
        multitrack  = Multitrack(filename, beat_resolution=BEAT_RESOLUTION)
    except:
        continue

    # Pad to multtple
    multitrack.pad_to_multiple(4 * BEAT_RESOLUTION)

    # Binarize the pianoroll
    multitrack.binarize()

    # Sort the tracks according to program number
    multitrack.tracks.sort(key=lambda x: x.program)

    # Bring the drum track to the first track
    multitrack.tracks.sort(key=lambda x: ~x.is_drum)

    # Get the stacked pianoroll
    pianoroll = multitrack.get_stacked_pianorolls()

    # Check length
    if pianoroll.shape[0] < 4 * 4 * BEAT_RESOLUTION:
        continue

    # Keep only the mid-range pitches
    pianoroll = pianoroll[:, 24:108]

    # Reshape and get the phrase pianorolls
    # https://docs.scipy.org/doc/numpy-1.14.2/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape
    # "One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions."
    try:
        pianoroll = pianoroll.reshape(-1, 4 * BEAT_RESOLUTION, 84, N_TRACKS)
        pianoroll = pianoroll.reshape(-1, 4, 4 * BEAT_RESOLUTION, 84, N_TRACKS)
        results.append(pianoroll)
    except ValueError:
        pass

result = np.concatenate(results, 0)
# NOTE: You might want to shuffle the training data here
np.savez_compressed(
    RESULT_FILENAME, nonzero=np.array(result.nonzero()),
    shape=result.shape)
