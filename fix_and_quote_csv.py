import csv

with open("datasets/jd_to_skills.csv", "r", encoding="utf-8") as infile, \
     open("datasets/jd_to_skills_clean.csv", "w", encoding="utf-8", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

    for row in reader:
        if len(row) >= 2:
            # Fix by joining everything after the first column as the second field
            input_text = row[0]
            target_text = ",".join(row[1:]).strip()
            writer.writerow([input_text, target_text])
