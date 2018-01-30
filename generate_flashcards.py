import pandas as pd
import csv

PARTS_CSV = 'principal_parts.csv'
PARTS_START = 1
TRANSLATION = 'translation'
FIRST = 'first'
MESSAGE_A = ' principal part for '
MESSAGE_B = ', '
NEW_COLUMNS = ['Part', 'Identification']

parts = pd.read_csv(PARTS_CSV)
headers = list(parts)

flashcards = []
for index, row in parts.iterrows():
	for i in range(PARTS_START, len(row)):
		english = row[TRANSLATION]
		number = headers[i]
		part = row[number]
		if not pd.isnull(part):
			identification = number + MESSAGE_A + row[FIRST] + MESSAGE_B + english
			flashcards.append([part, identification])

flashcards_df = pd.DataFrame(flashcards, columns=NEW_COLUMNS)
print flashcards_df['Identification']
flashcards_df.to_csv('flashcards.csv', sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\\', index=False)
