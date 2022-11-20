import csv
from csv import Sniffer
from itertools import islice
from collections import namedtuple

fnames = 'cars.csv', 'personal_info.csv'

class FileParser:
    def __init__(self, fname):
        self.fname = fname

    def __enter__(self):
        self._f = open(self.fname)
        self.reader = csv.reader(self._f, get_dialect(self.fname))
        headers = map(lambda x: x.lower(), next(self.reader))
        self.nt = namedtuple('Data', headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self.nt(*next(self.reader))


def get_dialect(fname):
    with open(fname) as f:
        return csv.Sniffer().sniff(f.read(1000))

for fname in fnames:
    with FileParser(fname) as f:
        for row in islice(f, 10):
            print(row)