import csv
import sys

HEADER = '''<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <link rel="stylesheet" href="hecs.css" type="text/css">
</head>
<body>

<div class="container">
'''

FOOTER = '''</div>
</body>
</html>'''

csvfile = open("hecs.csv", newline="", encoding="utf-8")
csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
data = dict()

color = [[None] * 40 for i in range(40)]
text = [[None] * 40 for i in range(40)]

for row in csvreader:
    if row[14]:
        color[int(row[14])][int(row[15])] = row[17]
        text[int(row[14])][int(row[15])] = row[1]
        

        
fout = open("index_gen.html", "w", encoding="utf-8")


print(HEADER, file=fout)

for j in range(10, 24, 2):
    print('''    <div class="hecs left">
        <div class="text {}"><a href="{}">{}</a></div>
    </div>
'''.format(color[j][8] or "", "pages/" + str(j) + "-8.html",text[j][8] or ""), file=fout)
    for i in range(9, 9 + 17):
        print('''    <div class="hecs">
        <div class="text {}"><a href="{}">{}</a></div>
    </div>
'''.format(color[j][i] or "", "pages/" + str(j) + "-" + str(i) + ".html",text[j][i] or ""), file=fout)
    for i in range(9, 9 + 17):
        print('''    <div class="hecs">
        <div class="text {}"><a href="{}">{}</a></div>
    </div>
'''.format(color[j + 1][i] or "", "pages/" + str(j + 1) + "-" + str(i) + ".html",text[j + 1][i] or ""), file=fout)
        
print(FOOTER, file=fout)