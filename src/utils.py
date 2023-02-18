"""
this file could contain all functions that we want to use  in the project.
e.g.
def function_name(parameter_name):
    local_variable=0
    return
"""
# Please Note that the function name should be in snake case and the parameters , local variables in the same convention
import seaborn as sns



def count_plot_percentage(data, feature):
    ax = sns.countplot(x=data[feature])

    # Add count on each plot
    total = data.shape[0]
    for p in ax.patches:
        percentage = f'{(100 * p.get_height()/total):.1f}%'
        x = p.get_x() + p.get_width() / 2 - 0.1
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y))
