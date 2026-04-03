import pandas as pd

class DataLoader:
    _instance = None
    _data = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance

    def __init__(self, file_path=None):
        if self._data is None and file_path is not None:
            print(f"Loading data from {file_path}...")
            self._data = pd.read_csv(file_path)
        elif self._data is None and file_path is None:
            raise ValueError("File path must be provided for the first initialization.")

    @property
    def data(self):
        return self._data

    def get_drg_info(self, input_text):
        return {"code": input_text, "nk025": "", "nk026": ""}


    def get_nk025_info(self, input_params):
        return f"{input_params}"

    def get_nk026_info(self, input_params):
        return f"{input_params}"


def auto_type_detection(input_text):
    return "drg"

def text_preprocessor(input_text):
    return input_text.upper().replace(" ", "")

def drg_processor(input_text):
    sort_table_info = DataLoader().get_drg_info(input_text)
    full_nk025_info = DataLoader().get_nk025_info(sort_table_info["nk025"])
    full_nk026_info = DataLoader().get_nk026_info(sort_table_info["nk026"])
    full_table_info = {"info": sort_table_info, "full_nk025": full_nk025_info, "full_nk026": full_nk026_info}
    return full_table_info

def main(input_text):
    processed_text = text_preprocessor(input_text)
    code_text_type = auto_type_detection(processed_text)
    DataLoader("data/table.csv")

    match code_text_type:
        case "drg":
            return drg_processor(processed_text)
        case "diagnose":
            return "drg"
        case "intervention":
            return "intervention"
        case _:
            return "Вхідний текст не розпізнано"


if __name__ == "__main__":
    print(main("b01"))