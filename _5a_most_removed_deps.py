import os
import csv
import sys
import time

csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)
start_time = time.time()

OUTPUT_DIR = "output"
SCRIPTS_ALREADY_RUN = "_PYPI" + "_REMOVALS"
FILEFORMAT = ".csv"
dep_i = os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
dep_o = os.path.join(os.getcwd(), OUTPUT_DIR, "mostRemovedDependencies2" + FILEFORMAT)

REMOVED_DEPENDENCIES_COL = 4
ALL_DEPENDENCIES_COL = 6

INPUT_FILE_NAME  = dep_i
OUTPUT_FILE_NAME = dep_o
ERRORS_FILE = os.path.join(os.getcwd(), OUTPUT_DIR, "_errors" + ".txt")
ERROR_TITLE = dep_o
error_title_already_printed = False

fp_i = open(INPUT_FILE_NAME, newline="", encoding="utf8")
reader = csv.reader(fp_i, delimiter=",", quotechar="|")
fp_o = open(OUTPUT_FILE_NAME, "w", encoding="utf8")
fp_e = open(ERRORS_FILE, "a", encoding="utf8")

total_lines = 0
output_lines_count = 0

# Desired output row: Project Name,Removal Count,Removed Dependencies,Current Dependencies,All Dependencies
header_line = next(reader)
fp_o.write("Dependency Name,Removal Count,Total Count\n")

dependency_list = {}

for line in reader:
	total_lines += 1
	proj_removed_deps = line[REMOVED_DEPENDENCIES_COL].split("|")
	proj_all_deps = line[ALL_DEPENDENCIES_COL].split("|")
	temp = []
	for d in proj_removed_deps:
		temp.append(d.lower())
	proj_removed_deps = temp
	temp = []
	for d in proj_all_deps:
		temp.append(d.lower())
	proj_all_deps = temp
	temp = []
	
	for d in proj_removed_deps: 
		if dependency_list.get(d) == None: 
			dependency_list[d] = [1,0]
		else: 
			dependency_list[d] = [dependency_list.get(d)[0] + 1, dependency_list.get(d)[1]]
	for d in proj_all_deps:
		if dependency_list.get(d) == None: 
			dependency_list[d] = [0,1]
		else: 
			dependency_list[d] = [dependency_list.get(d)[0], dependency_list.get(d)[1] + 1]

dependency_list = sorted(dependency_list.items(), key=lambda item: item[1], reverse=True) # Sort by removed dependencies count, descending

for key, value in dependency_list:
	fp_o.write(str(key))
	fp_o.write(",")
	fp_o.write(str(value[0]))
	fp_o.write(",")
	fp_o.write(str(value[1]))
	fp_o.write("\n")


fp_i.close()
fp_o.close()
fp_e.close()

print("Total:", total_lines, "lines")
print("Dict lines :", len(dependency_list), "lines")
end_time = time.time()
print("Time :", end_time - start_time, "seconds")