
import pandas
from datetime import datetime
from pytz import utc


#data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\dataVisualisation\reviews.csv", parse_dates=['Timestamp'])
#data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
#week_avg = data.groupby(['Week']).mean()

#print(list(zip(week_avg.index, week_avg['Rating'])))
#print(list(week_avg['Rating']))
#print(list(week_avg.index))

#print(list(zip(data.index, day_avg['Rating'])))
data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\dataVisualisation\reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg_per_course = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()

hc_data = [{"name": v1, "data": [v2 for v2 in month_avg_per_course[v1]]} for v1 in month_avg_per_course.columns]
x = 19 % 4 + 15 / 2 * 3
print(x)
