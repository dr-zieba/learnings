from collections import namedtuple
import datetime

def open_file(file):
    with open(file) as f:
        for line in f:
            yield line.strip('\n')

main_file = open_file('Project+3+-+Description/nyc_parking_tickets_extract.csv')
headers = next(main_file)
headers = headers.replace(" ", "").split(',')
Ticket = namedtuple('Ticket', headers, defaults=(None,) * len(headers))

def parsed_data():
    for row in main_file:
        row = row.split(',')
        summonsNumber = int(row[0])
        plateID = str(row[1])
        registrationState = str(row[2])
        plateType = str(row[3])
        issueDate = datetime.datetime.strptime(row[4], '%m/%d/%Y').date()
        violationCode = int(row[5])
        vehicleBodyType = str(row[6])
        vehicleMake = str(row[7])
        violationDescription = str(row[8])

        data = [summonsNumber, plateID, registrationState, plateType, issueDate, violationCode, vehicleBodyType, vehicleMake, violationDescription]

        ticket = Ticket(*data)

        yield ticket

def makes_count():
    makes_dict = {}
    for data in parsed_data():
        if data.VehicleMake in makes_dict:
            makes_dict[data.VehicleMake] += 1
        else:
            makes_dict[data.VehicleMake] = 1
    yield {make: cnt for make, cnt in sorted(makes_dict.items(), key=lambda x: x[1], reverse=True)}

for k in makes_count():
    print(k)

#sorted(makes_caount.items(), key=lambda i: i[1], reverse=True):

