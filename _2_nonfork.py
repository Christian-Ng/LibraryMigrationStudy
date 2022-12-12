import os
import csv
import sys
import time

csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)
start_time = time.time()

OUTPUT_DIR = "output"
SCRIPTS_ALREADY_RUN = "_PYPI"
THIS_SCRIPT = "_NONFORK"
FILEFORMAT = ".csv"
#dep1 = "dependencies" + SCRIPTS_ALREADY_RUN + FILEFORMAT
#dep2 = "dependencies" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT
#pro1 = "projects" + SCRIPTS_ALREADY_RUN + FILEFORMAT
#pro2 = "projects" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT
#prorep1 = os.path.join(os.getcwd(), OUTPUT_DIR, "projects_with_repository_fields" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
#prorep2 = os.path.join(os.getcwd(), OUTPUT_DIR, "projects_with_repository_fields" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT)
#prorep_col = 24
#prorep_name = "Repository Fork?" ; prorep_bool = "false"
rep1 = os.path.join(os.getcwd(), OUTPUT_DIR, "repositories" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
rep2 = os.path.join(os.getcwd(), OUTPUT_DIR, "repositories" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT)
rep_col = 4
rep_bool = "false"

INPUT_FILE_NAME  = rep1
OUTPUT_FILE_NAME = rep2
FORK_COLUMN_NUMBER = rep_col
FORK_BOOL = rep_bool
ERRORS_FILE = os.path.join(os.getcwd(), OUTPUT_DIR, "_errors_fork.txt")

fp_i = open(INPUT_FILE_NAME, newline="", encoding="utf8")
reader = csv.reader(fp_i, delimiter=",", quotechar="|")

total_lines = 0
nonfork_lines = 0

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
		if line[FORK_COLUMN_NUMBER].lower() == FORK_BOOL: 
			nonfork_lines += 1
			for cell in line: 
				fp_o.write(cell)
				fp_o.write(",")
			fp_o.write("\n")
	except Exception as e:
		fp_e.write("Problem on line %s: " % line, e)

fp_i.close()
fp_o.close()
fp_e.close()

print("Total:", total_lines)
print("PyPI nonforks :", nonfork_lines)
end_time = time.time()
print("Time :", end_time - start_time)