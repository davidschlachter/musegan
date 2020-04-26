# MuseGAN

We investigated using [MuseGAN](https://salu133445.github.io/musegan/) to create polyphonic piano music, trained with a dataset of MIDI files from [Classical Archives](https://fr.wikipedia.org/wiki/Classical_Music_Archives). About piano 900 pieces, represented as MIDI files with two tracks (piano right hand, piano left hand) were used for training. (For conditional generation, some tracks were removed to be used as the test dataset.)

We created tools for [preparing datasets for MuseGAN](https://github.com/davidschlachter/musegan-pianoroll-midi-utils/), for [merging datasets to the single-file NPZ format](https://github.com/davidschlachter/musegan/blob/master/scripts/manymidi2npz.py) used by MuseGAN v3, as well as for [post-processing generated samples](https://github.com/davidschlachter/musegan-pianoroll-midi-utils/blob/master/fix-glissando.py).

We used a [simplified MuseGAN network](https://colab.research.google.com/drive/1cKYe99-XPCxMupgrJRWTESfGhApME-L9) based on presentation material from [Hao-Wen Dong and Yi-Hsuan Yang](https://salu133445.github.io/ismir2019tutorial/) to create _de novo_ songs. Here are some generated samples:

[De novo piano tracks](https://github.com/davidschlachter/musegan/blob/master/exp/denovopiano.m4a?raw=true)

For conditional track generation, we used MuseGAN v3 to create accompaniment tracks for either piano left or right hand. The experiment files used are available in this repository. Here are some generated samples:

[Generated piano left-hand](https://github.com/davidschlachter/musegan/blob/master/exp/0_fake_x_hard_thresholding_12900.m4a?raw=true)

[Generated piano right-hand](https://github.com/davidschlachter/musegan/blob/master/exp/1_fake_x_hard_thresholding_32400.m4a?raw=true)

An example pianoroll for conditional track generation (top: piano right hand, given; bottom, generated accompaniment)

![Example pianoroll](https://raw.githubusercontent.com/davidschlachter/musegan/master/exp/0_fake_x_hard_thresholding_12900.npz.mid.png)