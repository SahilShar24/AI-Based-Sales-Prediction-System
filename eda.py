def generate_eda(df):
    report = {}

    # Basic stats
    report['summary'] = df.describe()

    # Top categories (for object columns)
    cat_cols = df.select_dtypes(include='object').columns
    top_values = {}

    for col in cat_cols:
        top_values[col] = df[col].value_counts().head(3)

    report['top_categories'] = top_values

    return report