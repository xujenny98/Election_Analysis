import csv
import os
file_to_load = os.path.join("Resource","election_results.csv")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
file_to_save = os.path.join("analysis", "election_analysis.txt")

