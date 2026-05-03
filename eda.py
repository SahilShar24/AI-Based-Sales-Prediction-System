def generate_eda(df):
    report = {}

    
    report['summary'] = df.describe()

    
    cat_cols = df.select_dtypes(include='object').columns
    top_values = {}

    for col in cat_cols:
        top_values[col] = df[col].value_counts().head(3)

    report['top_categories'] = top_values

    return report
