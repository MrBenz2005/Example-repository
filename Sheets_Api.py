import gspread

def create_table_without_duplicate(sheet_name: str, row_number: int, col_number: int):
    sh = gc.create('A new spreadsheet')