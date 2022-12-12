import os
import csv
import sys
import time


csv.field_size_limit(sys.maxsize) # _csv.Error: field larger than field limit (131072)
start_time = time.time()

desired_star_count = 10

OUTPUT_DIR = "output"
SCRIPTS_ALREADY_RUN = "_PYPI" + "_NONFORK"
THIS_SCRIPT = "_" + str(desired_star_count) + "star"
FILEFORMAT = ".csv"
rep1 =     os.path.join(os.getcwd(), OUTPUT_DIR, "repositories" + SCRIPTS_ALREADY_RUN + FILEFORMAT)
rep2 =     os.path.join(os.getcwd(), OUTPUT_DIR, "repositories" + SCRIPTS_ALREADY_RUN + THIS_SCRIPT + FILEFORMAT)
rep_col =  10 
rep_name = desired_star_count

INPUT_FILE_NAME  = rep1 											# Change these 4 lines
OUTPUT_FILE_NAME = rep2												# ==
COLUMN_NUMBER = rep_col												#
COLUMN_VALUE = rep_name											#
ERRORS_FILE = os.path.join(os.getcwd(), OUTPUT_DIR, "_errors" + THIS_SCRIPT + ".txt")
ERROR_STRING = rep2
error_string_already_printed = False

fp_i = open(INPUT_FILE_NAME, newline="", encoding="utf8")
reader = csv.reader(fp_i, delimiter=",", quotechar="|")

total_lines = 0
output_lines = 0

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
		if int(line[COLUMN_NUMBER]) >= COLUMN_VALUE: 
			output_lines += 1
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
print("Output lines :", output_lines, "lines")
end_time = time.time()
print("Time :", end_time - start_time, "seconds")