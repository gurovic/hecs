import csv

HEADER = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <link rel="stylesheet" href="../hecs.css" type="text/css">
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="../hecs.js" type="text/javascript"></script>
</head>
<body>
'''

FOOTER = '''
<br><br><br>
<hr>
<!--LiveInternet counter--><script type="text/javascript">document.write("<a href='//www.liveinternet.ru/click' target=_blank><img src='//counter.yadro.ru/hit?t44.6;r" + escape(document.referrer) + ((typeof(screen)=="undefined")?"":";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?screen.colorDepth:screen.pixelDepth)) + ";u" + escape(document.URL) + ";" + Math.random() + "' border=0 width=31 height=31 alt='' title='LiveInternet'><\/a>")</script><!--/LiveInternet-->
</body>
</html>
'''

csvfile = open("hecs.csv", newline="", encoding="utf-8")
csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
data = dict()

for row in csvreader:
    if row[0] and row[0] != '-':
        if row[0] not in data:
            data[row[0]] = {'title': row[1], 'task': [], 'video': [], 'vis':[], 'theory':[], 'pres':[]}
        if row[2]:
            data[row[0]]['task'] += [('informatics', row[2], row[3] or row[1])]
        if row[4]:
            data[row[0]]['theory'] += [('e-maxx', row[4], row[5] or row[1])]
        if row[7]:
            data[row[0]]['theory'] += [('foxford', row[7], row[8] or row[1])]
        if row[9]:
            data[row[0]]['video'] += [('foxford', row[9], row[10] or row[1])]
        if row[12]:
            data[row[0]]['video'] += [('sis-video', row[12], row[13] or row[1])]
        if row[18]:
            data[row[0]]['theory'] += [('habr', row[18], row[19] or row[1])]

        if row[14]:
            data[row[0]]['id'] = row[14] + '-' + row[15]

for key, value in data.items():
    if 'id' not in data[key]:
        continue
    f = open("pages/" + data[key]['id'] + ".html", "w", encoding="utf-8")
    print(HEADER, file=f)
    print('<h1>' + data[key]['title'] + '</h1>\n<ul class="resources">', file=f)
    for section in ['theory', 'video', 'task', 'vis', 'pres']:
        if data[key][section]:
            print('    <li class="{}">\n        <ul>'.format(section), file=f)
            for line in data[key][section]:
                print('            <li class="{}"><a href="{}">{}</a></li>'.format(line[0], line[1], line[2]), file=f)
            print('        </ul>', file=f)
    print('</ul>\n', FOOTER, file=f)
    f.close()
print(data)
                        