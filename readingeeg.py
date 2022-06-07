# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:29:00 2022

@author: racer
"""
import mne

if __name__ == "__main__":
  patient1_raw_file = "EEG_Data/Subject_01/20220311213941_Patient01.nedf"
  patient1_raw = mne.io.read_raw_nedf(patient1_raw_file)
  print(patient1_raw)
  print(patient1_raw.info)

