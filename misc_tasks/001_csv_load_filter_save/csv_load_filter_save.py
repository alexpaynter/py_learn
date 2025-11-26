import numpy as np
import pandas as pd

titanic = pd.read_csv("data-raw/titanic_raw_pydata_book.csv")

new_titanic = titanic.query('Sex == "female"')

new_titanic.to_csv(path_or_buf = 'misc_tasks/001_csv_load_filter_save/female_data.csv')
