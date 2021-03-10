import csv

cwb_filename = '108061131.csv'
target_station = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]
target_station.sort
target_len = len(target_station)

with open(cwb_filename) as csvfile:
	mycsv = csv.DictReader(csvfile)
	total = [0] * target_len
	counter = [0] * target_len
	output = []
	
	for row in mycsv:
		for i in range(target_len):
			if row["station_id"] == target_station[i] and float(row["PRES"]) >= 0:
				counter[i] += 1
				total[i] += float(row["PRES"])
	
	for i in range(target_len):
		if (counter[i] == 0):
			total[i] = "None"
		else:
			total[i] = total[i] / counter[i]
		output.append([target_station[i], total[i]])
	print(output)
