import re
import sys
import collections
import csv

file_name = sys.argv[1]

if len(sys.argv) != 2:
    print(f"Użycie: python <filename> <file>")
    sys.exit(1)

def login_count():
    try:
        with open(file_name,"r") as file:
            list = re.findall(r'[0-9]{1,3}(?:\.[0-9]{1,3}){3}',file.read())
            counter = collections.Counter(list)
            res = counter.most_common(5)
        with open("raport.csv","w",newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["ip","count"])
            for ip,count in res:
                writer.writerow([ip,count])
    except Exception as e:
        print(f"Exception: {e}")

login_count()