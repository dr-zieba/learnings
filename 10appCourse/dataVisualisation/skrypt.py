import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\dataVisualisation\reviews.csv", parse_dates=['Timestamp'])

#print(data['Rating'])
#print(data[(data['Rating'] < 4) & (data['Course Name'] == "The Complete Python Course: Build 10 Professional OOP Apps")])
#print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc)) & (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc))])

avg_rating = data['Rating'].mean()
#print(avg_rating)
'''
course_name = data['Course Name'].unique()
for name in course_name:
    print(name)
    print(data[data['Course Name'] == name]['Rating'].mean())
    #print(df['Rating'].mean())
'''
'''
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg_per_course = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()
month_avg_per_course.plot()
#plt.show()
'''
'''
plt.figure(figsize=(25,3))
plt.plot(month_avg_per_course.index, month_avg_per_course['Rating'])
plt.show()
'''

data['Week Day'] = data['Timestamp'].dt.strftime('%A')
data['Day'] = data['Timestamp'].dt.strftime('%w')

day_avg = data.groupby(['Week Day', 'Day']).mean()
day_avg = day_avg.sort_values('Day')
day_avg = day_avg.reset_index(level=[1,])
#print(data['Day'].to_list())

print(day_avg['Rating'])
#plt.plot(day_avg.index.get_level_values(0), day_avg['Rating'])
#plt.show()
