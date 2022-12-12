import os
import csv
import sys
import time


csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)
start_time = time.time()

desired_dependency_count = 2

# 1) from dependencies, count the number of unique "Dependency Name"

OUTPUT_DIR = "output"
SCRIPTS_ALREADY_RUN = "_PYPI"
THIS_SCRIPT = "_DEPCNT"
FILEFORMAT = ".csv"
dep_i =     os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
dep_o =     os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT)

PROJECT_NAME_COL = 2	#1pass
#VERSION_ID_COL = 5		#22218
DEPENDENCY_NAME_COL = 6	#simple-pbkdf2

INPUT_FILE_NAME  = dep_i
OUTPUT_FILE_NAME = dep_o
ERRORS_FILE = os.path.join(os.getcwd(), OUTPUT_DIR, "_errors" + THIS_SCRIPT + ".txt")
ERROR_TITLE = dep_o
error_title_already_printed = False

fp_i = open(INPUT_FILE_NAME, newline="", encoding="utf8")
reader = csv.reader(fp_i, delimiter=",", quotechar="|")
fp_o = open(OUTPUT_FILE_NAME, "w", encoding="utf8")
fp_e = open(ERRORS_FILE, "a", encoding="utf8")

total_lines = 0
output_lines_count = 0

header_line = next(reader)
for cell in header_line: 
	fp_o.write(cell)
	fp_o.write(",")
fp_o.write("All dependencies,Dependency count") #NEW COLUMNS
fp_o.write("\n")

project_name = "1pass" # Manual lol
#latest_version_id = False
#version_id = 0
dependency_names = []
for line in reader:
	total_lines += 1
 
	if line[PROJECT_NAME_COL] == project_name:
		previous_line = line
	else: 
		if len(dependency_names) >= desired_dependency_count: 
			output_lines_count += 1
			output_line = previous_line
			all_deps = ""
			for dep in dependency_names:
				all_deps += dep + " | "
			output_line.append(all_deps)
			output_line.append(str(len(dependency_names)))
			for cell in output_line: 
				fp_o.write(cell)
				fp_o.write(",")
			fp_o.write("\n")

		previous_line = line
		project_name = line[PROJECT_NAME_COL]
		dependency_names = []
	if line[DEPENDENCY_NAME_COL].lower() not in dependency_names:
		dependency_names.append(line[DEPENDENCY_NAME_COL].lower())
		

	#except: 
	#	if error_string_already_printed == False: 
	#		fp_e.write(ERROR_STRING)
	#		error_string_already_printed = True
	#	a_string = ""
	#	for l in line:
	#		a_string += l
	#		fp_e.write(a_string)
	

fp_i.close()
fp_o.close()
fp_e.close()

print("Total:", total_lines, "lines")
print("Output lines :", output_lines_count, "lines")
end_time = time.time()
print("Time :", end_time - start_time, "seconds")