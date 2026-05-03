import pandas as pd

def clean_data(df):
    report = {}

    # Remove duplicates
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    report['duplicates_removed'] = before - after

    # Handle missing values
    missing_before = df.isnull().sum().sum()

    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

    missing_after = df.isnull().sum().sum()
    report['missing_values_fixed'] = missing_before - missing_after

    #Convert date columns automatically
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
                report[f"{col}_converted"] = True
            except:
                report[f"{col}_converted"] = False

    return df, report