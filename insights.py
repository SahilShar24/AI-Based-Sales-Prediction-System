def generate_insights(df):
    insights = []

    # Top Sales Category
    if 'Category' in df.columns and 'Sales' in df.columns:
        top_category = df.groupby('Category')['Sales'].sum().idxmax()
        insights.append(f"🏆 Top performing category is {top_category}")

    # Top Region
    if 'Region' in df.columns and 'Sales' in df.columns:
        top_region = df.groupby('Region')['Sales'].sum().idxmax()
        insights.append(f"🌍 Highest sales come from {top_region} region")

    # Low Profit Warning
    if 'Profit' in df.columns:
        low_profit = df[df['Profit'] < 0].shape[0]
        if low_profit > 0:
            insights.append(f"⚠️ {low_profit} transactions are in loss")

    # High Sales Trend
    if 'Sales' in df.columns:
        avg_sales = df['Sales'].mean()
        insights.append(f"📈 Average sales value is {round(avg_sales, 2)}")

    return insights