import os


class CsvHandler:
    @staticmethod
    def deleteCsv(filename):
        filepath = f"../../../temp/csv/{filename}.csv"
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
            except OSError as e:
                print(f"Error: {filepath} - {e}")
