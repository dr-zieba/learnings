import json
import csv

def to_json(export_file, users):
    json.dump(users, export_file, indent=4)
    export_file.close()

def to_csv(export_file, users):
    export_file.write('name, id, home, shell\n')
    writer = csv.writer(export_file)
    rows = [[user['name'], user['id'], user['home'], user['shell']] for user in users]
    writer.writerows(rows)
    export_file.close()
