# Reference: https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
def health_bar(home_xx,target_df_2,region):
    '''绘制柱状图的函数'''
    # 導入包
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 设定颜色为set1
    sns.set_palette("Set3")
    # 為bar圖準備數據
    home_xx_selected = home_xx.iloc[:,0:6]
    y1 = home_xx_selected.groupby('Walking').mean()['Overall Health']
    walking_xx = pd.DataFrame(y1).reset_index(drop=False)
    y2 = home_xx_selected.groupby('Moderate Activity').mean()['Overall Health']
    moderate_xx = pd.DataFrame(y2).reset_index(drop=False)
    y3 = home_xx_selected.groupby('Vigorous Activity').mean()['Overall Health']
    vigorous_xx = pd.DataFrame(y3).reset_index(drop=False)
    data = pd.merge(target_df_2, walking_xx, left_on='Frequency', right_on='Walking', how='left')
    data = pd.merge(data, moderate_xx, left_on='Frequency', right_on='Moderate Activity', how='left')
    data = pd.merge(data, vigorous_xx, left_on='Frequency', right_on='Vigorous Activity', how='left')
    data = data.round(1) # 保留一位小数
    # 将Frequency列重分类
    data['frequency_2groups'] = data['Frequency'].apply(lambda x: 'Low' if x<=3 else 'High')
    y4 = data.groupby('frequency_2groups').mean()
    data_2 = pd.DataFrame(y4).reset_index(drop=False)
    data_2 = data_2[['frequency_2groups','Overall Health_x','Overall Health_y','Overall Health']]
    # 转置data_2
    data_2 = data_2.T
    data_2.columns = data_2.iloc[0,:]
    data_2.drop(index='frequency_2groups', inplace=True)
    data_2.reset_index(drop=False, inplace=True)
    data_2['index'] = data_2['index'].replace({'Overall Health_x':'步行',
                                            'Overall Health_y':'適度活動',
                                            'Overall Health':'劇烈活動'})

    # 繪製bar圖
    frequency = tuple(data_2['index'])
    physical_activity = {
        '高頻組（>= 4天/周）': tuple(data_2['High'].apply(lambda x: round(x,2))),
        '低頻組（<= 3天/周）': tuple(data_2['Low'].apply(lambda x: round(x,2)))
    }
    x = np.arange(len(frequency))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    bar_colors = ['#d6604d','#878787']

    for i, (attribute, measurement) in enumerate(physical_activity.items()):
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute, color=bar_colors[i])
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('居民健康水平（好-->差）')
    # ax.set_xlabel('頻率（天/周）')
    ax.set_title(f'{region}按活動水平分類的居民健康水平')
    ax.set_xticks(x + width, frequency)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(1, 5)
    plt.savefig(f'{region}_bar_2.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()
