import pandas as pd
import translators as ts
# Load the CSV file
input_csv = '/home/itamars/Documents/vocabulary_kindel/LOOKUPS.csv'  # replace with your CSV file path
output_csv = 'results'  # output CSV file path

# Load CSV into DataFrame
words_df = pd.read_csv(input_csv, sep=";")

# Initialize the translator
print("check: ", ts.translate_text("word", from_language='en', to_language='he'))

# Specify the column to translate
column_to_translate = 'column_name'  # replace with the name of the column you want to translate

# Translate each cell in the specified column
words_dict = {}
for word_index, word_row in words_df.iterrows():
    # same word - add usage
    if word_row[0] in words_dict:
        words_dict[word_row[0]]["answer"] += f"</hr>{word_row[3]}"
    elif word_row[0]:  # new word
        print(f"word {word_index}: {word_row[0]}")
        words_dict[word_row[0]] = {"answer": f"{ts.translate_text(word_row[0], from_language='en', to_language='he')}<hr>{word_row[3]}"}
    if word_index % 100 == 99 or word_index == len(words_df)-1:
        words_dict_formatted = {"word": [], "answer": []}
        for word in words_dict:
            words_dict_formatted["word"].append(word)
            words_dict_formatted["answer"].append(words_dict[word]["answer"])
        pd.DataFrame(words_dict_formatted).to_csv(f"{output_csv}{word_index//100}.csv", index=False)
        print(f"{output_csv}{word_index//100}.csv was created")
        words_dict = {}


# words_df[column_to_translate] = words_df[column_to_translate].apply(lambda x: translator.translate(x, src='en', dest='he').text if pd.notnull(x) else x)

# Save the translated DataFrame to a new CSV
pd.DataFrame(words_dict_formatted).to_csv(output_csv, index=False)

print(f"Translation complete. The translated CSV is saved as '{output_csv}'")
