import csv
from contextlib import contextmanager
from csv import Sniffer
from collections import namedtuple
from itertools import islice

@contextmanager
def parsed_data(fname):
    f = open(fname, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda x: x.lower(), next(reader))
        nt = namedtuple('Data', headers)
        yield (nt(*row) for row in reader)
    finally:
        f.close()

with parsed_data('cars.csv') as f:
    for row in islice(f, 5):
        print(row)
