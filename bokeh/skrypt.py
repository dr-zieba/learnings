from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral10
from bokeh.transform import factor_cmap

import pandas as pd

file_top10 = pd.read_excel(r"C:\Users\zieba\Desktop\python\bokeh\top10.xlsx")
output_file("strona2.html")

lang = file_top10["Language"]
rating = file_top10["Ratings"]

src = ColumnDataSource(data = dict(language = lang, rating = rating))
p = figure(x_range = lang, plot_height = 800, toolbar_location = None, title = "Top10")

p.vbar(x = 'language',
       top = 'rating',
       width = 0.7,
       source = src,
       line_color = 'white',
       fill_color = factor_cmap('language', palette = Spectral10, factors = lang))


show(p)
