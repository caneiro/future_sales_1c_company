import numpy as np
import pandas as pd
from pathlib import Path
import data_functions

project_dir = Path(__file__).resolve().parents[2]

raw_dir = Path(project_dir, "./data/raw")
processed = Path(project_dir, "./data/processed")

def main():
    sales = pd.read_csv(Path(raw_dir,"sales_train.csv"))

    sales["date"] = pd.to_datetime(sales["date"], format="%d.%m.%Y")
    sales["pk"] = sales.shop_id.map(str) + "#" + \
                sales.item_id.map(str) + "#" + \
                sales.date_block_num.map(str)

    sales.reset_index(drop=False, inplace=True)
    
    sales = data_functions.reduce_mem_usage(sales)

    print(sales.shape)



if __name__ == '__main__':
    main()