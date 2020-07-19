# This file contains stuff related to reading data

import csv

def get_data_csv(file_path):
    """
    Parameters:
        file_path: Path to the csv file from which data is to be read

    Returns:
        header: The csv header
        rows: The rows in csv
    """

    header = []
    rows = []

    with open(file_path) as csvfile:
        csv_rows = csv.reader(csvfile)

        header = next(csv_rows, None)

        for row in csv_rows:
            rows.append(row)

    return header, rows

