# import csv
# import random

# def read_csv_file(file_path, num_records):
#     data = []
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip the header row
#         for i, row in enumerate(csv_reader):
#             if i >= num_records:
#                 break
#             data.append(row)
#     return data

# def extract_notes_and_codes(notes_data, codes_data):
#     notes = []
#     codes = []
#     for note_row, code_row in zip(notes_data, codes_data):
#         clinical_note = note_row[-1].replace('\n', ' ')  # Replace newline characters with spaces
#         icd9_codes = code_row[4:]  # Extract multiple ICD-9 codes
#         notes.append(clinical_note)
#         codes.append(icd9_codes)
#     return notes, codes

# def write_to_text_file(data, output_file, is_notes=False):
#     with open(output_file, 'w') as file:
#         if is_notes:
#             file.write('\n'.join(data))
#         else:
#             file.write('\n'.join(data))

# def split_data(notes, codes, train_ratio):
#     data = list(zip(notes, codes))
#     random.shuffle(data)
#     train_size = int(len(data) * train_ratio)
#     train_data = data[:train_size]
#     test_data = data[train_size:]
#     train_notes, train_labels = zip(*train_data)
#     test_notes, test_labels = zip(*test_data)
#     return train_notes, train_labels, test_notes, test_labels

# def get_label_indices(labels, label_names):
#     label_indices = []
#     for label_set in labels:
#         indices = [label_names.index(label) for label in label_set if label in label_names]
#         label_indices.append(indices)
#     return label_indices

# # Specify the file paths
# notes_file = 'mimic/NOTEEVENTS.csv'
# codes_file = 'mimic/DIAGNOSES_ICD.csv'

# label_names_file = 'data/mimic/label_names.txt'
# test_labels_file = 'data/mimic/test_labels.txt'
# test_notes_file = 'data/mimic/test.txt'
# train_labels_file = 'data/mimic/train_labels.txt'
# train_notes_file = 'data/mimic/train.txt'

# # Specify the number of records to process
# num_records = 500

# # Specify the train/test split ratio
# train_ratio = 0.8

# # Read the clinical notes CSV file
# notes_data = read_csv_file(notes_file, num_records)

# # Read the ICD-9 codes CSV file
# codes_data = read_csv_file(codes_file, num_records)

# # Extract clinical notes and ICD-9 codes
# notes, codes = extract_notes_and_codes(notes_data, codes_data)

# # Split the data into training and testing sets
# train_notes, train_labels, test_notes, test_labels = split_data(notes, codes, train_ratio)

# # Get unique label names
# label_names = sorted(set(code for code_set in codes for code in code_set))

# # Get label indices for training and testing labels
# train_label_indices = get_label_indices(train_labels, label_names)
# test_label_indices = get_label_indices(test_labels, label_names)

# # Convert label indices to strings
# train_label_indices_str = [' '.join(map(str, indices)) for indices in train_label_indices]
# test_label_indices_str = [' '.join(map(str, indices)) for indices in test_label_indices]

# # Write the label names to a text file
# write_to_text_file(label_names, label_names_file)

# # Write the test labels (indices) to a text file
# write_to_text_file(test_label_indices_str, test_labels_file)

# # Write the test notes to a text file
# write_to_text_file(test_notes, test_notes_file, is_notes=True)

# # Write the train labels (indices) to a text file
# write_to_text_file(train_label_indices_str, train_labels_file)

# # Write the train notes to a text file
# write_to_text_file(train_notes, train_notes_file, is_notes=True)

# print(f"{num_records} records processed.")
# print(f"Label names saved to {label_names_file}.")
# print(f"Test labels (indices) saved to {test_labels_file}.")
# print(f"Test notes saved to {test_notes_file}.")
# print(f"Train labels (indices) saved to {train_labels_file}.")
# print(f"Train notes saved to {train_notes_file}.")

import csv

# # Input CSV file path
# input_file = "mimic/icd9NotesDataTable_valid.csv"

# # Output text file paths
# text_output_file = "data/mimic/test.txt"
# # labels_output_file = "data/mimic/train_labels.txt"

# # Open the input CSV file and output text files
# with open(input_file, "r") as csv_file, open(text_output_file, "w") as text_file:
#     # Create a CSV reader object
#     csv_reader = csv.DictReader(csv_file)

#     # Iterate over each row in the CSV file
#     for row in csv_reader:
#         # Extract the "TEXT" and "TopLevelICD" values
#         text = row["TEXT"]
#         # top_level_icd = row["TopLevelICD"]

#         # Write the "TEXT" value to the text output file
#         text_file.write(text + "\n")

#         # Write the "TopLevelICD" value to the labels output file
#         # labels_file.write(top_level_icd + "\n")

# print("Extraction completed.")

import random

def get_sample_from_text(file_path, ratio, output_file):
    with open(file_path, 'r') as file:
        data = file.readlines()
        sample_size = int(len(data) * ratio)
        sample = random.sample(data, sample_size)
        with open(output_file, 'w') as output:
            output.writelines(sample)
    print(f"Sampled {sample_size} records from {file_path} and saved to {output_file}.")
    
print("traing.txt")
file_path = 'data/dbpedia/temp/train_labels.txt'
ratio = 0.3
output_file = 'data/dbpedia/train_labels.txt'
get_sample_from_text(file_path, ratio, output_file)

print("train_labels.txt")
file_path = 'data/dbpedia/temp/train.txt'
ratio = 0.3
output_file = 'data/dbpedia/train.txt'
get_sample_from_text(file_path, ratio, output_file)

print("test.txt")
test_file_path = 'data/dbpedia/temp/test_labels.txt'
ratio = 0.2
output_file = 'data/dbpedia/test_labels.txt'
get_sample_from_text(test_file_path, ratio, output_file)

print("test_labels.txt")
test_file_path = 'data/dbpedia/temp/test.txt'
ratio = 0.2
output_file = 'data/dbpedia/test.txt'
get_sample_from_text(test_file_path, ratio, output_file)

