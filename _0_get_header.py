# Gets the header lines of each CSV file

import csv
import sys

csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)

fn1 = "dependencies-1.6.0-2020-01-12.csv"
fn2 = "projects_with_repository_fields-1.6.0-2020-01-12.csv"
fn3 = "projects-1.6.0-2020-01-12.csv"
fn4 = "repositories-1.6.0-2020-01-12.csv"
fn5 = "repository_dependencies-1.6.0-2020-01-12.csv"
fn6 = "tags-1.6.0-2020-01-12.csv"
fn7 = "versions-1.6.0-2020-01-12.csv"
filenames = []
filenames.extend([fn1, fn2, fn3, fn4, fn5, fn6, fn7])

header_lines = []

for filename in filenames: 
	with open(filename, newline="", encoding="utf8") as fp: 
		reader = csv.reader(fp, delimiter=",", quotechar="|")
		two_lines = []
		hline = next(reader)
		firstline = next(reader)
		for i, h in enumerate(hline): 
			tl = h + "(" + str(i) + ") | " # h should always be string
			try: 
				tl += firstline[i]
			except: 
				tl += "\<SECOND ROW DOES NOT HAVE A VALUE\>"
			two_lines.append(tl)
		header_lines.append(two_lines)

fp = open("_headers.txt", "w", encoding="utf8")
i = 0
for header in header_lines: 
	ws = ""
	fp.write(filenames[i] + "\n")
	i += 1
	for field in header:
		fp.write(ws + field + "\n")
		ws += " "
