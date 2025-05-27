

# import pandas as pd
# import matplotlib as mpl
# mpl.use('tkagg')
# import matplotlib.pyplot as plt
# import random
# from typing import Optional
#
# def get_colors(n, color_names):
#     if color_names is None:
#         return ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(n)]
#     elif len(color_names) < n:
#         raise ValueError(
#             'More predictors than color_names, please enter more color names in color_names list and try again')
#     return color_names
#
# def plot_scores(
#         plot_df: pd.DataFrame,
#         score_col: str,
#         y_limits: list = [-0.05, 0.2],
#         color_names: Optional[list] = None
#         ) -> None:
#
#     modelnames = plot_df['model'].value_counts().index
#     colors = get_colors(len(modelnames), color_names)
#     for modelname, color in zip(modelnames, colors):
#         single_model_df = plot_df[plot_df['model'] == modelname]
#         plt.plot(single_model_df['threshold'], single_model_df[score_col], color=color)
#
#         plt.ylim(y_limits)
#         plt.legend(modelnames)
#         plt.grid(b=True, which='both', axis='both')
#         plt.xlabel('Threshold Values')
#         plt.ylabel(f'Calculated {score_col.capitalize().replace("_", " ")}')
#     plt.show()
#
# def plot_graphs(plot_df: pd.DataFrame,
#                 graph_type: str = 'net_benefit',
#                 y_limits: list = [-0.05, 1],
#                 color_names: Optional[list] = None
#                 ) -> None:
#     """
#     Plot either net benefit or interventions avoided per threshold.
#
#     Parameters
#     ----------
#     plot_df : pd.DataFrame
#         Data containing threshold values, model columns of net benefit/intervention scores to be plotted
#     graph_type : str
#         Type of plot (either 'net_benefit' or 'net_intervention_avoided')
#     y_limits : list[float]
#         2 floats, lower and upper bounds for y-axis
#     color_names
#         Colors to render each model (if n models supplied, then need n+2 colors, since 'all' and 'none' models will be
#         included by default
#
#     Returns
#     -------
#     None
#     """
#     plot_scores(plot_df, graph_type, y_limits, color_names)