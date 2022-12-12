import os
import csv
import sys
import time

csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)

OUTPUT_DIR = "output"
SCRIPTS_ALREADY_RUN = "_PYPI" + "_DEPCNT"
THIS_SCRIPT = "(LISTED)"
FILEFORMAT = ".csv"
dep_i =     os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
dep_o =     os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT)

PROJECT_NAME_COL = 2	#1pass

INPUT_FILE_NAME  = dep_i
OUTPUT_FILE_NAME = dep_o
ERRORS_FILE = os.path.join(os.getcwd(), OUTPUT_DIR, "_errors" + THIS_SCRIPT + ".txt")
ERROR_TITLE = dep_o
error_title_already_printed = False

fp_i = open(INPUT_FILE_NAME, newline="", encoding="utf8")
reader = csv.reader(fp_i, delimiter=",", quotechar="|")
fp_o = open(OUTPUT_FILE_NAME, "w", encoding="utf8")

header_line = next(reader)

project_list = []
for line in reader:
    project_list.append(line[PROJECT_NAME_COL])
for p in project_list: 
    fp_o.write(p)
    fp_o.write(",")

fp_i.close()
fp_o.close()

print("Output lines :", str(len(project_list)), "lines")
