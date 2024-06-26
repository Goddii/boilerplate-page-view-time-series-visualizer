import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14,5))
    ax.plot(df.index,df['value'],color='skyblue',linewidth=2)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')







    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df_bar = df.groupby(['year','month'], sort=False) ['value'].mean().unstack()

    # month order
    month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']

    #reindex the dataframe
    df_bar = df_bar.reindex(columns=month_order)

    # Draw bar plot
    ax = df_bar.plot(kind='bar', figsize=(20,6), legend=True, title='Average Daily Page Views')
    ax.legend(title='Months',loc='upper left')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.xticks(rotation=45)
    
    #create the fig object
    fig = ax.get_figure()






    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    df_box['year'] = df_box['year'].astype('category')
    df_box['month'] = df_box['month'].astype('category')
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2, figsize=(28,6))
    plt.subplots_adjust(wspace=0.4)

    sns.boxplot(data=df_box,x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot(Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Value')

    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1],order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    axes[1].set_title('Month-wise Box Plot(Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Value')

    plt.show()





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


draw_line_plot()
draw_bar_plot()
draw_box_plot()