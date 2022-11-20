import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\dataVisualisation\reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_avg = data.groupby(['Day']).mean()

data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_avg = data.groupby(['Week']).mean()

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg = data.groupby(['Month']).mean()



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
            format: '{value}'
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

def app():
    page = jp.QuasarPage()
    h1 = jp.QDiv(a=page, text="Analisise of reviews.csv", classes="text-h1 text-center")
    p1 = jp.QDiv(a=page, text="Graphs!", classes="text-h4 text-center")

    high_chart = jp.HighCharts(a=page, options=chart)
    high_chart.options.title.text="Average dayli"

    high_chart.options.xAxis.categories=list(day_avg.index)
    high_chart.options.series[0].data=list(day_avg['Rating'])


    high_chart2 = jp.HighCharts(a=page, options=chart)
    high_chart2.options.title.text="Average weekly"

    high_chart2.options.xAxis.categories=list(week_avg.index)
    high_chart2.options.series[0].data=list(week_avg['Rating'])


    high_chart3 = jp.HighCharts(a=page, options=chart)
    high_chart3.options.title.text="Average weekly"

    high_chart3.options.xAxis.categories=list(month_avg.index)
    high_chart3.options.series[0].data=list(month_avg['Rating'])

    return page

jp.justpy(app, port=8002)
