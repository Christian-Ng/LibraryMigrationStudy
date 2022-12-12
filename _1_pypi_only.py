import os
import csv
import sys
import time


csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)
start_time = time.time()

dep1 =    "dependencies-1.6.0-2020-01-12.csv" ;					  dep2 =    "dependencies_PYPI.csv" ; 					dep_col =	 1 ;	dep_name =		"pypi"
prorep1 = "projects_with_repository_fields-1.6.0-2020-01-12.csv"; prorep2 = "projects_with_repository_fields_PYPI.csv";	prorep_col = 1 ;	prorep_name =	"pypi" # also 16 python
pro1 =    "projects-1.6.0-2020-01-12.csv" ;						  pro2 =    "projects_PYPI.csv"	;						pro_col =	 1 ;	pro_name =		"pypi" # also 16 python
rep1 =    "repositories-1.6.0-2020-01-12.csv" ;					  rep2 =    "repositories_PYPI.csv"	;					rep_col =	11 ;	rep_name =		"python"
repdep1 = "repository_dependencies-1.6.0-2020-01-12.csv" ; 	      repdep2 = "repository_dependencies_PYPI.csv" ;		# None
tag1 =    "tags-1.6.0-2020-01-12.csv" ; 						  tag2 =    "tags_PYPI.csv"	;							# None
ver1 =    "versions-1.6.0-2020-01-12.csv" ; 					  ver2 =    "versions_PYPI.csv"	;						ver_col =	 1 ;	ver_name =		"pypi"

OUTPUT_DIR = "output"
INPUT_FILE_NAME  = rep1 											# Change these 4 lines
OUTPUT_FILE_NAME = os.path.join(os.getcwd(), OUTPUT_DIR, rep2)		# ==
column_number = rep_col												#
column_python = rep_name											#
ERRORS_FILE = os.path.join(os.getcwd(), OUTPUT_DIR, "_errors_pypi.txt")
ERROR_STRING = rep2
error_string_already_printed = False

fp_i = open(INPUT_FILE_NAME, newline="", encoding="utf8")
reader = csv.reader(fp_i, delimiter=",", quotechar="|")

total_lines = 0
pypi_lines = 0

fp_o = open(OUTPUT_FILE_NAME, "w", encoding="utf8")
fp_e = open(ERRORS_FILE, "a", encoding="utf8")

header_line = next(reader)
for cell in header_line: 
	fp_o.write(cell)
	fp_o.write(",")
fp_o.write("\n")

for line in reader:
	total_lines += 1
	try: 
		if line[column_number].lower() == column_python: 
			pypi_lines += 1
			for cell in line: 
				fp_o.write(cell)
				fp_o.write(",")
			fp_o.write("\n")
	except: 
		if error_string_already_printed == False: 
			fp_e.write(ERROR_STRING)
			error_string_already_printed = True
		a_string = ""
		for l in line:
			a_string += l
			fp_e.write(a_string)


fp_i.close()
fp_o.close()
fp_e.close()

print("Total:", total_lines, "lines")
print("PyPI :", pypi_lines, "lines")
end_time = time.time()
print("Time :", end_time - start_time, "seconds")