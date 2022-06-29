# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:29:00 2022

@author: jenna
"""
import glob
import mne
import os.path

#see https://mne.tools/dev/auto_tutorials/raw/10_raw_overview.html#the-raw-info-attribute
def print_patient_info(raw):
  # raw.info
  n_time_stamps = raw.n_times
  time_secs = raw.times
  ch_names = raw.ch_names
  n_chan = len(ch_names)      #note: there is no raw.n_channels attribute
  print('the sample data object has {} time samples and {} channels.'''.format(n_time_stamps, n_chan))
  print('the last time sample is at {} seconds.'.format(time_secs[-1]))
  print('the first few channel names are {}'.format(', '.join(ch_names[:3])))
  print()

  print('bad channels: ', raw.info['bads'])  # channels marked "bad" during acquisition
  print(raw.info['sfreq'], 'Hz')  # sampling frequency
  print(raw.info['description'], '\n')  # misc acquisition info

  print(raw.info)

def annotate_patient_info(file, raw):
    patient_annotations = mne.Annotations(onset=
                                          [0, 60, 61, 121, 122, 127, 128, 133, 134, 139, 140, 145, 146, 151, 152, 157,
                                           158, 163, 164, 169, 170, 175, 176, 181, 182, 187, 188, 193, 194, 199, 200,
                                           205,
                                           206, 211, 212, 217, 218, 223, 224, 229, 230, 235, 236, 241, 242, 247, 248,
                                           253,
                                           254, 259, 260, 265, 266, 271, 272, 277, 278, 283, 284, 289, 290, 295, 296,
                                           301,
                                           302, 307, 308, 313, 314, 319, 320, 325, 326, 331, 332, 337, 338, 343, 344,
                                           349,
                                           350, 355, 356, 361, 362, 367, 368, 373, 374, 379, 380, 385, 386, 391, 392,
                                           397,
                                           398, 403, 404, 409, 410, 415, 416, 421, 422, 427, 428, 433, 434, 439, 440,
                                           445,
                                           446, 451, 452, 457, 458, 463, 464, 469, 470, 475, 476, 481, 482, 487, 488,
                                           493,
                                           494, 499, 500, 505, 506, 511, 512, 517, 518, 523, 524, 529, 530, 535, 536,
                                           541,
                                           542, 547, 548, 553, 554, 559, 560, 565, 566, 571, 572, 577, 578, 583, 584],
                                          # , 589],
                                          duration=
                                          [60, 1, 60, 1, 5,  # eye open, eye close, A
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter A, B
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter B, C
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter C, D
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter D, E
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter E, F
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter F, G
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter G, H
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter H, I
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter I, J
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter J, K
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter K, L
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter L, M
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter M, N
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter N, O
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter O, P
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter P, Q
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter Q, R
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter R, S
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter S, T
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter T, U
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter U, V
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter V, W
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter W, X
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter X, Y
                                           1, 5, 1, 5, 1, 5,  # black screen, imagined letter Y, Z
                                           1, 5, 1, 5  # black screen, imagined letter Z
                                           ],
                                          description=
                                          ['Eye Open', 'transition', 'Eye Closed', 'transition', 'A',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter A', 'transition',
                                           'B',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter B', 'transition',
                                           'C',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter C', 'transition',
                                           'D',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter D', 'transition',
                                           'E',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter E', 'transition',
                                           'F',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter F', 'transition',
                                           'G',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter G', 'transition',
                                           'H',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter H', 'transition',
                                           'I',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter I', 'transition',
                                           'J',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter J', 'transition',
                                           'K',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter K', 'transition',
                                           'L',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter L', 'transition',
                                           'M',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter M', 'transition',
                                           'N',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter N', 'transition',
                                           'O',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter O', 'transition',
                                           'P',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter P', 'transition',
                                           'Q',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter Q', 'transition',
                                           'R',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter R', 'transition',
                                           'S',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter S', 'transition',
                                           'T',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter T', 'transition',
                                           'U',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter U', 'transition',
                                           'V',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter V', 'transition',
                                           'W',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter W', 'transition',
                                           'X',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter X', 'transition',
                                           'Y',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter Y', 'transition',
                                           'Z',
                                           'transition', 'Black Screen', 'transition', 'Imagined Letter Z'
                                           ])
    raw.set_annotations(patient_annotations)
    print(raw.annotations)

    #print annotation information
    for annotation in raw.annotations:
        description = annotation['description']
        start = annotation['onset']
        end = annotation['onset'] + annotation['duration']
        print("'{}' goes from {} to {}".format(description, start, end))

    #plot annotated data
    fig = raw.plot()
    #allow modifications to annotations from plot window
    fig.fake_keypress('a')

    raw.annotations.save('results/EEG_Data/{}/{}.csv'.format(os.path.dirname(file).split("\\")[1], os.path.basename(file)), overwrite=True)

    return raw


if __name__ == "__main__":
  for nedf_file in glob.glob('EEG_Data/*/*.nedf'):
      patient_raw = mne.io.read_raw_nedf(str(nedf_file))
      print_patient_info(patient_raw)
      raw_annotated = annotate_patient_info(nedf_file, patient_raw)
      all_events, all_event_id = mne.events_from_annotations(raw_annotated)
      print()