import plotly.express as px

def generate_charts(df):
    charts = []

    
    if 'Category' in df.columns and 'Sales' in df.columns:
        fig1 = px.bar(df, x='Category', y='Sales', title='Sales by Category')
        charts.append(fig1)

    
    if 'Region' in df.columns and 'Sales' in df.columns:
        fig2 = px.pie(df, names='Region', values='Sales', title='Sales by Region')
        charts.append(fig2)

    return charts
