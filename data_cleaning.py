import pandas as pd

output_file = "output.csv"
def cleaning(csv_file):
    transactions_read = pd.read_csv('data/' + csv_file, delimiter=',')
    pink_morsel_series = transactions_read['product'] == 'pink morsel'
    pink_morsel_df = transactions_read[pink_morsel_series].copy()

    pink_morsel_df['price'] = pink_morsel_df['price'].replace('[\$,]', '', regex=True).astype(float)
    pink_morsel_df['sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
    # print(pink_morsel_df)

    selected_columns = ['sales', 'date', 'region']
    selected_pink_morsel_df = pink_morsel_df[selected_columns]

    print(selected_pink_morsel_df)
    selected_pink_morsel_df.to_csv(output_file, mode='a', header=not pd.io.common.file_exists(output_file), index=False)


    
files_to_process = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

for files in files_to_process:
    cleaning(files)
