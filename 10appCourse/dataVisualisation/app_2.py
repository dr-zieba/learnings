import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\dataVisualisation\reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg_per_course = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()


chart = '''
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
'''

def app():
    page = jp.QuasarPage()
    h1 = jp.QDiv(a=page, text="Areaspline chart", classes="text-h3 text-center")

    high_chart = jp.HighCharts(a=page, options=chart)
    high_chart.options.xAxis.categories = list(month_avg_per_course.index)
    high_chart.options.series = [{"name": v1, "data": [v2 for v2 in month_avg_per_course[v1]]} for v1 in month_avg_per_course.columns]

    return page

jp.justpy(app, port=8002)
