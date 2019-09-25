# -*- coding: utf-8 -*-

import json
from datetime import datetime

import pandas
import numpy

def get_data_frame(filename):
  data_frame = pandas.read_csv('./data/acc/{}'.format(filename), header=None)
  return data_frame

def read_filenames():
  with open('./data/acc/data.json') as json_file:
    data = json.load(json_file)
    return data

def filter_data_frame(data_frame):
  has_eur_value = data_frame[2].notnull()
  filtered_data_frame = data_frame[has_eur_value]

  difference = filtered_data_frame[1] != 'erotus'
  filtered_data_frame = filtered_data_frame[difference]

  filtered_data_frame[0] = filtered_data_frame[0].fillna(method='ffill')

  return filtered_data_frame

def get_milliseconds(date_str):
  dt = datetime.strptime('{}19'.format(date_str), '%d.%m.%y')

  epoch = datetime.utcfromtimestamp(0)

  return (dt - epoch).total_seconds() * 1000.0

def parse_eur(eur):
  eur = eur.replace('€', '')
  eur_n = float(eur)
  return eur_n

def map_data_frame(data_frame):
  data_frame[0] = data_frame[0].map(get_milliseconds)
  data_frame[2] = data_frame[2].map(parse_eur)

  return data_frame

def get_data_frames_combined():
  filenames = read_filenames()

  data_frames = []
  for filename in filenames:
    data_frames.append(get_data_frame(filename))

  data_frame = data_frames[0]

  for list_data_frame in data_frames[1:]:
    data_frame = data_frame.append(list_data_frame)

  data_frame = filter_data_frame(data_frame)
  data_frame = map_data_frame(data_frame)

  # print(data_frame.head(20))

  return data_frame

get_data_frames_combined()
