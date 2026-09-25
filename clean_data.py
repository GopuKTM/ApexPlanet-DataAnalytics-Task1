import pandas as pd

def clean_data(input_path: str, output_path: str):
    # 1. Load raw dataset
    df = pd.read_csv(input_path)
    
    # 2. Convert Order_Date to datetime format
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
    # 3. Handle missing values
    df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
    df['City'] = df['City'].fillna('UNKNOWN')
    
    # 4. Save cleaned dataset
    df.to_csv(output_path, index=False)
    print("Data successfully cleaned and saved.")

if __name__ == '__main__':
    clean_data('ApexPlanet_DataAnalytics_Dataset(Sales_Dataset) (1).csv', 'Cleaned_Sales_Dataset.csv')
