import pandas

def get_data_frame():
   data_frame = pandas.read_csv('https://archive.ics.uci.edu/ml/'
      'machine-learning-databases/iris/iris.data',
      header=None)

   print(data_frame.tail())

   return data_frame