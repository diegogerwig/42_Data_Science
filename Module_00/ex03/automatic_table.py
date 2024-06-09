import os
import sys
sys.path.append(os.path.abspath("ex02"))
from table import load


def extract_table_names(items):
    return [name[:-4] for name in items]


def check_csv(item):
    return item.endswith(".csv") and not item.startswith("._")


def main():
    path = "/System/Volumes/Data/sgoinfre/goinfre/Perso/dgerwig-/Data_Science/subject/customer/"

    files = os.listdir(path)

    tables_to_add = [item for item in files if check_csv(item)]

    table_names = extract_table_names(tables_to_add)

    print("\n🔵 Extracted table names: ", table_names)

    for table_name, csv_file in zip(table_names, tables_to_add):
        csv_path = os.path.join(path, csv_file)
        load(csv_path, table_name)


if __name__ == "__main__":
    main()
