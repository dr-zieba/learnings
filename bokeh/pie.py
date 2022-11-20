from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral10
from bokeh.transform import factor_cmap

import csv

x = {}
file = csv.reader(open(r"C:\Users\zieba\Desktop\python\bokeh\countries.csv"), delimiter = ',')
for lines in file:
    key = lines[0]
    x[key] = lines[1:]

output_file("strona3.html")
print(x)

