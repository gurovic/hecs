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
<!--LiveInternet counter--><script type="text/javascript">document.write("<a href='//www.liveinternet.ru/click' target=_blank><img src='//counter.yadro.ru/hit?t44.6;r" + escape(document.referrer) + ((typeof(screen)=="undefined")?"":";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?screen.colorDepth:screen.pixelDepth)) + ";u" + escape(document.URL) + ";" + Math.random() + "' border=0 width=31 height=31 alt='' title='LiveInternet'><\/a>")</script><!--/LiveInternet-->
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
        

        
fout = open("index.html", "w", encoding="utf-8")

LEFT = 9
RIGHT = 25
TOP = 12
BOTTOM = 22



print(HEADER, file=fout)

for j in range(TOP, BOTTOM, 2):
    print('''    <a href="{}"><div class="hecs left {}"><div class="inner">{}</div></div></a>'''.format("pages/" + str(j) + "-" + str(LEFT) + ".html" if text[j][LEFT] else "", color[j][LEFT] or "", text[j][LEFT] or ""), file=fout)
    for i in range(LEFT + 1, RIGHT):
        print('''    <a href="{}"><div class="hecs {}"><div class="inner">{}</div></div></a>'''.format("pages/" + str(j) + "-" + str(i) + ".html"  if text[j][i] else "", color[j][i] or "", text[j][i] or ""), file=fout)
    for i in range(LEFT, RIGHT):
        print('''    <a href="{}"><div class="hecs {}"><div class="inner">{}</div></div></a>'''.format("pages/" + str(j + 1) + "-" + str(i) + ".html"  if text[j + 1][i] else "", color[j + 1][i] or "", text[j + 1][i] or ""), file=fout)
        
print(FOOTER, file=fout)