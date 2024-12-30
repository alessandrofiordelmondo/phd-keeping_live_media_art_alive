import csv

csv_file01 = "INCCA-links-arts.csv"
csv_file02 = "incca-postreview.csv"

csv01 = []
check = []
csv02 = []
check2 = 0

with open(csv_file01) as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        csv01.append(row[1])

with open(csv_file02) as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        csv02.append(row[1])

for i in range(len(csv02)):
    try:
        idx = csv01.index(csv02[i])
        check.append(str(idx))
        check2 += 1
    except:
        check.append("")

with open('INCCA-links-arts-check.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["n", "link", "check"]

    for i in range(len(csv01)):
        writer.writerow([str(i), csv02[i], check[i]])

print(check2)