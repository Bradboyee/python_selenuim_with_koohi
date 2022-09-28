import csv
import kanjikoohi.constants as const


class csv_writer:
    def __init__(self, csv_path=const.csv_path):
        self.path = csv_path

    def read(self):
        with open(self.path, 'r', encoding="utf8") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                print(line)
        file.close()

    def write(self, text=list):
        with open(self.path, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(text)

    def append(self, text: list):
        with open(self.path, 'a', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(text)
