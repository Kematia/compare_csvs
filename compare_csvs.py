import csv
import sys
import argparse

def read_csv(file_path):
    with open(file_path, 'rb') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = [row for row in reader]
    return headers, data

def compare_csvs(file1, file2):
    headers1, data1 = read_csv(file1)
    headers2, data2 = read_csv(file2)

    if headers1 != headers2:
        sys.exit("Error: The two CSV files have different headers. Please make sure they have the same structure and column order.")

    differences = []
    data1_set = set(tuple(row) for row in data1)
    data2_set = set(tuple(row) for row in data2)

    for row1 in data1:
        if tuple(row1) not in data2_set:
            differences.append(row1)

    for row2 in data2:
        if tuple(row2) not in data1_set:
            differences.append(row2)

    return headers1, differences

def write_csv(headers, data, output_file):
    with open(output_file, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Compare two CSV files and generate a new CSV file with the differences.")
    parser.add_argument("file1", help="Path to the first CSV file")
    parser.add_argument("file2", help="Path to the second CSV file")
    parser.add_argument("-o", "--output", default="differences.csv", help="Path to the output CSV file (default: differences.csv)")

    return parser.parse_args()

def main():
    args = parse_arguments()
    file1 = args.file1
    file2 = args.file2
    output_file = args.output

    headers, differences = compare_csvs(file1, file2)
    write_csv(headers, differences, output_file)
    print("Differences saved to {}".format(output_file))

if __name__ == "__main__":
    main()