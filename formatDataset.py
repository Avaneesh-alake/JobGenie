import csv
######### ----------------------- ##################
######### This code is depricated ###################
######### Use fix_and_quote_csv.py instead ###############
######### ----------------------- ##################
with open("datasets/jd_to_skills.csv", "r", encoding="utf-8") as infile, \
     open("datasets/jd_to_skills_clean.csv", "w", encoding="utf-8", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
######### ----------------------- ##################
######### This code is depricated ###################
######### Use fix_and_quote_csv.py instead ###############
######### ----------------------- ##################
    for row in reader:
        if len(row) >= 2:
            # Only keep first 2 columns to avoid extra commas being interpreted as new columns
            writer.writerow([row[0], row[1]])
######### ----------------------- ##################
######### This code is depricated ###################
######### Use fix_and_quote_csv.py instead ###############
######### ----------------------- ##################