import os
import csv
import sys
import time


csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)
start_time = time.time()

OUTPUT_DIR = "output"
SCRIPTS_ALREADY_RUN = "_PYPI"
DEPCNT = "_DEPCNT"
THIS_SCRIPT = "_REMOVALS"
FILEFORMAT = ".csv"
dep_i =     os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
dep_o =     os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT)

PROJECT_NAME_COL = 2	#1pass
VERSION_ID_COL = 5		#22218
DEPENDENCY_NAME_COL = 6	#simple-pbkdf2

# List of valid projects with more than 2 dependencies
fp = open(os.path.join(os.getcwd(), OUTPUT_DIR, "dependencies" + SCRIPTS_ALREADY_RUN + DEPCNT + FILEFORMAT))
fpr = csv.reader(fp, delimiter=",", quotechar="|")
header_line = next(fpr)
PROJS_WITH_MIN_DEPS = [] 
for line in fpr:
	PROJS_WITH_MIN_DEPS.append(line[PROJECT_NAME_COL])
fp.close()

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

# Desired output row: Project Name,Removal Count,Removed Dependencies,Current Dependencies,All Dependencies
header_line = next(reader)
fp_o.write("Project Name,Removal Count,All Count,Removal Percentage,Removed Dependencies,Current Dependencies,All Dependencies\n")

project_name = "1pass"
version_id = 0
latest_dependencies = []
all_dependencies = []
for line in reader:
	total_lines += 1

	if line[PROJECT_NAME_COL] in PROJS_WITH_MIN_DEPS:
		if line[PROJECT_NAME_COL] == project_name:
			if line[DEPENDENCY_NAME_COL] not in all_dependencies:  # Add dependency to all_dependencies
				all_dependencies.append(line[DEPENDENCY_NAME_COL])
			if int(line[VERSION_ID_COL]) > version_id: # If newer version, clear latest_dependencies and add it
				latest_dependencies = []
				version_id = int(line[VERSION_ID_COL])
			if line[DEPENDENCY_NAME_COL] not in latest_dependencies: 
				latest_dependencies.append(line[DEPENDENCY_NAME_COL])
		else: 		
			output_lines_count += 1
			output_line = previous_line
			#Project Name
			final_output = output_line[PROJECT_NAME_COL] + ","

			removed_dependencies = [x for x in all_dependencies if x not in latest_dependencies]

			#Removal Count,All Count
			final_output = final_output + str(len(removed_dependencies)) + ","
			final_output = final_output + str(len(all_dependencies)) + ","

			#Removal Percentage ====
			if len(removed_dependencies) > 0:
				removal_percentage = len(removed_dependencies) / len(all_dependencies)
				removal_percentage *= 100
				removal_percentage = str(removal_percentage)
			else: 
				removal_percentage = ""
			final_output += removal_percentage + ","

			#Removed Dependencies
			for rd in removed_dependencies: 
				final_output = final_output + rd + "|"
			final_output = final_output.rstrip("|") + ","

			#Current Dependencies
			for ld in latest_dependencies:
				final_output = final_output + ld + "|"
			final_output = final_output.rstrip("|") + ","

			#All Dependencies
			for ad in all_dependencies: 
				final_output = final_output + ad + "|"
			final_output = final_output.rstrip("|")

			fp_o.write(final_output)
			fp_o.write("\n")

			project_name = line[PROJECT_NAME_COL]
			version_id = 0
			latest_dependencies = []
			all_dependencies = []
	previous_line = line

fp_i.close()
fp_o.close()
fp_e.close()

print("Total:", total_lines, "lines")
print("Output lines :", output_lines_count, "lines")
end_time = time.time()
print("Time :", end_time - start_time, "seconds")