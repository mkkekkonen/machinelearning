from budget22_df import get_dfs_combined
import matplotlib.pyplot as plot
from randomcolor import RandomColor


def plot_budget_by_column(col: int):
    df = get_dfs_combined()

    categories = df[col].unique()
    color_generator = RandomColor()

    df2 = df.groupby(df[col], sort=False).agg(sum)
    df2 = df2.sort_values(by=[2], ascending=False)
    df2[2] = df2[2].apply(lambda x: 0 if x < 0 else x)
    print(df2)

    periods = df[0]

    fig, ax = plot.subplots()

    colors = [color_generator.generate()[0] for cat in categories]

    # ax.bar(df2.index, df2[2], color=colors, label=df2.index)
    ax.pie(df2[2], colors=colors, labels=df2.index)
    fig.legend(loc='right', bbox_to_anchor=(1, 0.5))

    plot.xticks(rotation=90)

    plot.show()


plot_budget_by_column(3)
