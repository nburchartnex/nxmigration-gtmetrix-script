#!/usr/bin/python3
#import time
import json
import python_gtmetrix2

domain_list = open("gtmdomains.txt").read().splitlines()
load_time = []
result_url = []
api_key = "c141cc7cb41499a33d712284f52f7e9d"
account = python_gtmetrix2.Account(api_key)

for domain in domain_list:
	url = f"http://{domain}"
	test = account.start_test(url)
	test.fetch(wait_for_completion=True)
	report = test.getreport()
	if report is None:
		print(f"The test for {domain} has failed!\n")
		result_url.append("Failure")
		load_time.append("Failure")
		continue
	else:
		# Store the report URLs and load times into a list
		result_url.append(report['links']['report_url'])
		#load_time.append(round((report['attributes']['fully_loaded_time'] / 1000), 1))
		load_time.append(f"{round((report['attributes']['fully_loaded_time'] / 1000), 1)}s")
		# Print the domain tested as well as the link to the GTMetrix report
		print(f"{report['attributes']['url']}:")
		print(report['links']['report_url'])
		# Convert and print fully loaded time in seconds, rounded to the nearest tenth
		fully_loaded = round(report['attributes']['fully_loaded_time'] / 1000, 1)
		print(f"{fully_loaded}s\n")
	
format_check = input("Would you like the results formatted for a migration spreadsheet? Y/n:\n")
if format_check == "Y":
    print("\n========Test Result URLs========")
    [print(i) for i in result_url]
    print("\n========Load Times========")
    [print(k) for k in load_time]
else:
    exit()