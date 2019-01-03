import argparse
import datetime
import calendar
import logging
import yattag
import pprint
import json
import time
import sys
import os
import re

#doc, tag, text = yattag.Doc().tagtext()
#
#def yeld_header():
#    doc.asis('<?xml version="1.0" encoding="utf-8"?>\n')
#    doc.asis('<!DOCTYPE html>\n')
#    doc.asis('<html lang="en">\n')
#    doc.asis('\n')
#
#def yeld_head():
#    with tag('head'):
#        doc.asis('<meta charset="utf-8">\n')
#        doc.asis('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
#        doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
#        doc.asis('<meta name="description" content="">\n')
#        doc.asis('<meta name="author" content="">\n')
#        doc.asis('\n')
#        doc.asis('<title>NASM</title>\n')
#        doc.asis('<link href="css/bootstrap.min.css" rel="stylesheet">\n')
#        doc.asis('<link href="css/web-fonts.css" rel="stylesheet">\n')
#        doc.asis('<link href="css/nasm.css" rel="stylesheet">\n')
#
##doc.asis('<head>\n')
##doc.asis('<meta charset="utf-8">\n')
##doc.asis('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
##doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
##doc.asis('<meta name="description" content="">\n')
##doc.asis('<meta name="author" content="">\n')
##doc.asis('\n')
##doc.asis('<title>NASM</title>\n')
##doc.asis('<link href="css/bootstrap.min.css" rel="stylesheet">\n')
##doc.asis('<link href="css/web-fonts.css" rel="stylesheet">\n')
##doc.asis('<link href="css/nasm.css" rel="stylesheet">\n')
##doc.asis('</head>\n')
#
#yeld_header()
#yeld_head()
#
#with tag('div class="chapter"'):
#    with tag('h1'):
#        text('nasm -f <format> <filename> [-o <output>]')
#
#print(doc.getvalue())

logging.basicConfig(format = '%(asctime)s %(filename)s %(funcName)s %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S', level = logging.DEBUG)

parser = argparse.ArgumentParser(prog='nasm-html.py')

sp = parser.add_subparsers(dest = 'cmd')
for cmd in ['build']:
    spp = sp.add_parser(cmd, help = 'Build HTML output.')
    spp.add_argument('--build-dir', dest='build-dir', required=True,
                     help = 'Destination directory to put output at')
    spp.add_argument('--sources', dest='sources', required=True,
                     help = 'Space separated list of TeX sources')

args, unknown_args = parser.parse_known_args()
if args.cmd == None:
    parser.print_help()
    sys.exit(1)

if args.cmd == "build":
    builder = HTMLBuilder(logger)
