import csv
from datetime import datetime
from collections import namedtuple
import itertools

employment = 'Project+-+Description/employment.csv'
personal_info = 'Project+-+Description/personal_info.csv'
update_status = 'Project+-+Description/update_status.csv'
vehicles = 'Project+-+Description/vehicles.csv'
files = (employment, personal_info, update_status, vehicles)

def parser_file(file, *, delimiter=',', quotechar='"', header=False):
    with open(file) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        if not header:
            next(reader)
        yield from reader

def parser_date(value, *, date_format='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, date_format)

def extract_field_names(file):
    reader = parser_file(file, header=True)
    return next(reader)

def create_namedtuple(file, class_name):
    fields = extract_field_names(file)
    return namedtuple(class_name, fields)

def create_combo_nemaedtuple_class(files, compressed_fields):
    compressed_fields = itertools.chain.from_iterable(compressed_fields)
    fields_name = itertools.chain.from_iterable(extract_field_names(file) for file in files)
    compressed_field_name = itertools.compress(fields_name, compressed_fields)
    return namedtuple('Data', compressed_field_name)

def iter_file(file, class_name, parser):
    nt_class = create_namedtuple(file, class_name)
    reader = parser_file(file)
    for row in reader:
        p_data = (parser(value) for value, parser in zip(row, parser))
        yield nt_class(*p_data)

def iter_combined_tuple(files, class_names, parsers, compressed_fields):
    compressed_fields = tuple(itertools.chain.from_iterable(compressed_fields))
    zipped_tuples = zip(*(iter_file(file, class_name, parser) for file, class_name, parser in zip(files, class_names, parsers)))
    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compressed_fields)
        yield tuple(compressed_row)

def iter_combined(files, class_names, parsers, compressed_fields):
    combo_nt = create_combo_nemaedtuple_class(files, compressed_fields)
    compressed_fields = tuple(itertools.chain.from_iterable(compressed_fields))
    zipped_tuples = zip(*(iter_file(file, class_name, parser) for file, class_name, parser in zip(files, class_names, parsers)))
    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compressed_fields)
        yield combo_nt(*compressed_row)

def group_key(item):
    return item.vehicle_make

#Parsers
employment_parser = (str, str, str, str)
personal_info_parser = (str, str, str, str, str)
update_status_parser = (str, str, parser_date, parser_date)
vehicles_parser = (str, str, str, int)
parsers = employment_parser, personal_info_parser, update_status_parser, vehicles_parser

#Namedtuple names
employment_class = 'Employment'
personal_info_class = 'Personal'
update_status_class = 'Update'
vehicles_class = 'Vehicle'
class_names = employment_class, personal_info_class, update_status_class, vehicles_class

#Fields include/exclude
employment_fields = [True, True, True, False]
personal_info_fields = [True, True, True, True, True]
update_status_fields = [False, True, True]
vehicles_fields = [False, True, True, True]
compressed_fields = employment_fields, personal_info_fields, update_status_fields, vehicles_fields

#for file, class_name, parser in zip(files, class_names, parsers):
#    file_iter = iter_file(file, class_name, parser)
#    print(file)
#    for _ in range(10):
#        print(next(file_iter))
#    print()

# gen = iter_combined_tuple(files, class_names, parsers, compressed_fields)
# print(list(next(gen)))
# print(list(next(gen)))

# nt = create_combo_nemaedtuple_class(files, compressed_fields)
# print(nt._fields)

data_iter = iter_combined(files, class_names, parsers, compressed_fields)
data1, data2 = itertools.tee(data_iter, 2)
data_m = (row for row in data1 if row.gender == 'Male')
sorted_data_m = sorted(data_m, key=group_key)
groups_m = itertools.groupby(sorted_data_m, key=group_key)
groups_m_counts = ((g[0], len(list(g[1]))) for g in groups_m)
print('Male')
for row in groups_m_counts:
    print(row)

data_f = (row for row in data2 if row.gender == 'Female')
sorted_data_f = sorted(data_f, key=group_key)
groups_f = itertools.groupby(sorted_data_f, key=group_key)
groups_f_counts = ((g[0], len(list(g[1]))) for g in groups_f)
print('Female')
for row in groups_f_counts:
    print(row)