import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

#chart from https://www.highcharts.com/docs/chart-and-series-types/spline-chart
chart = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''
#Pandas read file
#parse_dates parse column Timestamp to date format for further modifications
data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\dataVisualisation\reviews.csv", parse_dates=['Timestamp'])

#creates to column Week Day = %A -> Full weekday name.
data['Week Day'] = data['Timestamp'].dt.strftime('%A')
#creates to column Week Day = %w -> Weekday as a decimal number. Made possible to sort weekdays based on int not full name. Sort on full day name is mady alphabetacilly
data['Day'] = data['Timestamp'].dt.strftime('%w')

#average rating per days. Pandas automatically recognize column for mean
day_avg = data.groupby(['Week Day', 'Day']).mean()
#sort of days from Sunday to Saturday
day_avg = day_avg.sort_values('Day')
#multi index in day_avg changed to single with full day format column index
day_avg = day_avg.reset_index(level=[1,])

def app():
    #creates quasar obj
    page = jp.QuasarPage()
    #adds text to page
    h1 = jp.QDiv(a=page, text="Happiness chart", classes="text-h3 text-center")

    #adds chart to page
    high_chart = jp.HighCharts(a=page, options=chart)
    #adds index column = days to xAsix categorie list
    high_chart.options.xAxis.categories=list(day_avg.index)
    #adds rating to yAxis
    high_chart.options.series[0].data=list(day_avg['Rating'])

    return page

jp.justpy(app)
