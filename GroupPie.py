# Reference: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
def health_pie(home_xx,target_df,region):
    '''绘制饼图的函数'''
    # 导入包
    import pandas as pd
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import seaborn as sns
    matplotlib.rcParams['font.family'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
    # 為pie圖準備數據
    x = home_xx['Overall Health'].value_counts()
    health_xx = pd.DataFrame(x).reset_index(drop=False)
    health_xx['pecentage'] = health_xx['count']/health_xx['count'].sum() * 100
    health_xx['Overall Health'] = health_xx['Overall Health'].astype('int')
    health_xx = pd.merge(target_df, health_xx, on='Overall Health', how='inner')
    health_xx.replace({np.nan:0}, inplace=True)
    # 統計Overall Health列中小於等於3的數量
    count_1 = (health_xx['Overall Health'] <= 3).sum()
    count_2 = (health_xx['Overall Health'] > 3).sum()
    # 繪製pie圖
    fig, ax = plt.subplots()

    ax.set_aspect('equal')
    wedges, texts, percs = ax.pie(health_xx['pecentage'], labels=health_xx['Overall Health_CN'],
                                autopct="%1.1f%%",colors=health_xx['Color'],
                                startangle=180)

    groups = [list(range(count_1)), list(range(count_1, count_1+count_2))]
    radfraction = 0.05
    for group in groups:
        ang = np.deg2rad((wedges[group[-1]].theta2 + wedges[group[0]].theta1) / 2)
        for j in group:
            center = radfraction * wedges[j].r * np.array([np.cos(ang), np.sin(ang)])
            wedges[j].set_center(center)
            texts[j].set_position(np.array(texts[j].get_position()) + center)
            percs[j].set_position(np.array(percs[j].get_position()) + center)
    ax.autoscale(True)
    ax.set_title(f'{region}居民的健康狀況分佈',pad=20)
    plt.savefig(f'{region}_pie.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()
