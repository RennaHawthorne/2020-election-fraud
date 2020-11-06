import csv
import sys
import json

with open(sys.argv[1], mode='r') as infile:
    reader = csv.reader(infile)
    data = []
    with open(sys.argv[2], mode='w') as outfile:
        for row in reader:
            try:
                if int(row[4]) < 1910:
                    data.append({
                        'first':  row[1],
                        'middle': row[2],
                        'last': row[0],
                        'suffix': row[3],
                        'zip': int(row[17]), # 5 digit 
                        'street':  row[8] + ' ' + row[10] + ' ' + row[11] + ' ' + row[12],
                        'city': row[15],
                        'state': 'MI',
                        'yob': int(row[4]),
                        'yod': None,
                        'dob': None,
                        'dod': None,
                        'voter_id_num': int(row[23])
                    })
            except:
                pass
        json.dump(data, outfile)
