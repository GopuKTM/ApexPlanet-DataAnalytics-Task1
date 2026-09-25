import pandas as pd

def clean_data(input_path: str, output_path: str):
    # 1. Load raw dataset
    df = pd.read_csv(input_path)
    
    # 2. Convert Order_Date to datetime format and format as DD-MM-YYYY
    df['Order_Date'] = pd.to_datetime(df['Order_Date']).dt.strftime('%d-%m-%Y')
    
    # 3. Handle missing values
    # Impute missing Age with median (41)
    df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
    
    # Impute missing City with 'UNKNOWN'
    df['City'] = df['City'].fillna('UNKNOWN')
    
    # 4. Feature engineering: Add Age_Group column
    bins = [0, 24, 40, 60, 100]
    labels = ['Gen Z', 'Young Adult', 'Middle Aged', 'Senior']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    
    # 5. Save cleaned dataset
    df.to_csv(output_path, index=False)
    print("Data successfully cleaned and saved.")

if __name__ == '__main__':
    clean_data('ApexPlanet_DataAnalytics_Dataset(Sales_Dataset) (1).csv', 'Cleaned_Sales_Dataset.csv')
