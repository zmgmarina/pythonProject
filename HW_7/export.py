import csv

sp = []
with open("file.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter = ",")
    for row in reader_object:
        sp.append(row)

with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    for row in sp:
        file_writer.writerow(row)



