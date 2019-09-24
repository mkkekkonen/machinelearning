import json

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
  return filtered_data_frame

def get_data_frames_combined():
  filenames = read_filenames()

  data_frames = []
  for filename in filenames:
    data_frames.append(get_data_frame(filename))

  data_frame = data_frames[0]

  for list_data_frame in data_frames[1:]:
    data_frame = data_frame.append(list_data_frame)

  data_frame = filter_data_frame(data_frame)

  # print(data_frame.head(20))

  return data_frame

get_data_frames_combined()
