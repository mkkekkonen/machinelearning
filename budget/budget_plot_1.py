from budget_df import get_data_frames_combined

to_unicode = lambda my_str : unicode(my_str)

def plot():
  data_frame = get_data_frames_combined()

  # print(data_frame.head(20))

  places = data_frame[1].unique()
  categories = data_frame[3].unique()

  print('# PAIKAT')
  print(places)
  print('# KATEGORIAT')
  print(categories)

plot()
