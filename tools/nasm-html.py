from yattag import Doc

doc, tag, text = Doc().tagtext()

def yeld_header():
    doc.asis('<?xml version="1.0" encoding="utf-8"?>\n')
    doc.asis('<!DOCTYPE html>\n')
    doc.asis('<html lang="en">\n')
    doc.asis('\n')

def yeld_head():
    with tag('head'):
        doc.asis('<meta charset="utf-8">\n')
        doc.asis('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
        doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
        doc.asis('<meta name="description" content="">\n')
        doc.asis('<meta name="author" content="">\n')
        doc.asis('\n')
        doc.asis('<title>NASM</title>\n')
        doc.asis('<link href="css/bootstrap.min.css" rel="stylesheet">\n')
        doc.asis('<link href="css/web-fonts.css" rel="stylesheet">\n')
        doc.asis('<link href="css/nasm.css" rel="stylesheet">\n')

#doc.asis('<head>\n')
#doc.asis('<meta charset="utf-8">\n')
#doc.asis('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
#doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
#doc.asis('<meta name="description" content="">\n')
#doc.asis('<meta name="author" content="">\n')
#doc.asis('\n')
#doc.asis('<title>NASM</title>\n')
#doc.asis('<link href="css/bootstrap.min.css" rel="stylesheet">\n')
#doc.asis('<link href="css/web-fonts.css" rel="stylesheet">\n')
#doc.asis('<link href="css/nasm.css" rel="stylesheet">\n')
#doc.asis('</head>\n')

yeld_header()
yeld_head()

with tag('div class="chapter"'):
    with tag('h1'):
        text('nasm -f <format> <filename> [-o <output>]')

print(doc.getvalue())
