import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(15,5))
    ax = sns.lineplot(x='date', y='value', data=df)
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').mean()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Plot settings
    plt.figure(figsize=(10,9))
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    ax = sns.barplot(x='year', y='value', hue='month', hue_order=months_order, data=df_bar, palette=sns.color_palette())
    ax.set(xlabel='Years', ylabel='Average Page Views', title='')
    ax.legend(loc='upper left', title='Months')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(15,6))
    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[0].set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    ax[1].set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
