from randomcolor import RandomColor
import matplotlib.pyplot as plot

from budget_df import get_data_frames_combined

to_unicode = lambda my_str : unicode(my_str)

def plot_budget():
  data_frame = get_data_frames_combined()

  print(data_frame.head(20))

  places = data_frame[1].unique()
  categories = data_frame[3].unique()

  color_generator = RandomColor()

  # print('# PAIKAT')
  # print(places)
  # print('# KATEGORIAT')
  # print(categories)

  plot.subplot(121)

  for category in categories:
    category_filter = data_frame[3] == category
    fdf = data_frame[category_filter]

    plot.scatter(fdf[0], fdf[2],
      color=color_generator.generate()[0], marker='.', label=category)

  plot.xlabel('Ajankohta ms alkaen 1.1.1970 (UNIX timestamp)')
  plot.ylabel('Hinta (EUR)')
  plot.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)
  plot.show()

plot_budget()
