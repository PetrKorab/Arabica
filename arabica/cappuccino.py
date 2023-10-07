# Data visualization module

from plotnine import *
from arabica import arabica_freq
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
import numpy as np
import sys



def cappuccino(text: str,                  # Text
               time: str,                  # Time
               date_format: str,           # Date format: 'eur' - European, 'us' - American
               stopwords: [],              # Languages for stop words
               skip: [ ],                  # Remove additional strings
               plot: str = '',             # Chart type: 'wordcloud'/'heatmap'/'line'
               ngram: int = '',            # N-gram size, 1 = unigram, 2 = bigram, 3 = trigram
               time_freq: str = '',        # Aggregation period: 'Y'/'M', if no aggregation: 'ungroup'
               max_words: int = '',        # Max number for most frequent n-grams displayed for each period
               numbers: bool = False,      # Remove numbers
               lower_case: bool = False):  # Lowercase text before cleaning and frequency analysis

    result = arabica_freq(text = text,
                          time = time,
                          date_format = date_format,
                          time_freq = time_freq,
                          max_words = max_words,
                          stopwords = stopwords,
                          skip = skip,
                          numbers = numbers,
                          lower_case = lower_case)

    if ngram == 1:
        if time_freq == 'ungroup':
            if plot == 'wordcloud':
                unigrams_df = result[['unigram','unigram_freq']]
                unigrams_df = unigrams_df.dropna()
                unigrams_df['unigram_freq'] = unigrams_df['unigram_freq'].astype(int)
                unigrams_dict = dict(unigrams_df.values)
                fig = figure()
                wordcloud_unigram = WordCloud(background_color="white",
                                              colormap='tab20b',
                                              max_font_size=250,
                                              width=2000,
                                              height=1200,
                                              margin=10).generate_from_frequencies(unigrams_dict)
                plt.figure(dpi=1200)
                plt.imshow(wordcloud_unigram,interpolation="bilinear")
                fig.set_size_inches(10, 6, forward=True)
                plt.axis('off')
                picture = plt.show()

            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "wordcloud"')


        elif time_freq == 'M':
            period = result['period']
            subset = result['unigram']
            subset = subset.dropna()
            subset_expand = subset.str.split(pat=",", expand=True)
            subset_expand.columns = ['unigram' + str(i + 1) for i in range(len(subset_expand.columns))]
            subset_expand["id"] = subset_expand.index
            test = subset_expand.merge(period, left_index = True, right_index = True)
            reshaped = pd.wide_to_long(test, ['unigram'], i="id", j="period")
            period_re = reshaped['period']
            period_re.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped['unigram']
            reshaped_unigram.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped_unigram.str.split(pat=": ", expand=True)
            reshaped_unigram = reshaped_unigram.rename(columns={0: 'unigram', 1: 'frequency'})
            reshaped_unigram = reshaped_unigram.dropna()
            reshaped_unigram['frequency'] = reshaped_unigram['frequency'].astype(int)
            reshaped_unigram = reshaped_unigram.merge(period_re, left_index = True, right_index = True)

            if plot == 'heatmap':
                reshaped_unigram = reshaped['unigram']
                reshaped_unigram.reset_index(drop=True, inplace=True)
                reshaped_unigram = reshaped_unigram.str.split(pat=": ", expand=True)
                reshaped_unigram = reshaped_unigram.rename(columns={0: 'unigram', 1: 'frequency'})
                reshaped_unigram = reshaped_unigram.dropna()
                reshaped_unigram['frequency'] = reshaped_unigram['frequency'].astype(int)
                reshaped_unigram = reshaped_unigram.merge(period_re, left_index = True, right_index = True)
                reshaped_unigram_max = reshaped_unigram.groupby(['unigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram = reshaped_unigram.merge(reshaped_unigram_max, on = ['unigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram['label'] = np.where(reshaped_unigram['_merge']=='both', reshaped_unigram['unigram'], '')
                reshaped_unigram = reshaped_unigram[['unigram', 'frequency', 'period','label']]

                fig = (ggplot(reshaped_unigram, aes('period', 'unigram', fill='frequency'))
                       + geom_tile(aes(width=1, height=1))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust= 1),
                               legend_text = element_text(size = 7),
                               legend_title = element_text(color = "black", vjust= -1.3, size = 10),
                               figure_size= (3 + ((len(period) /4)), (3 + (max_words * 1.5))),
                               panel_grid_major = element_line(color='black',size = 0.1),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(800)
                picture = plt.show()


            elif plot == 'line':
                reshaped_unigram_wide = pd.pivot(reshaped_unigram, index = 'unigram', columns = 'period', values = 'frequency')
                reshaped_unigram_wide = reshaped_unigram_wide.fillna(0)
                year_list=list(reshaped_unigram_wide.columns)
                reshaped_unigram_wide = pd.melt(reshaped_unigram_wide, value_vars=year_list,value_name='frequency', ignore_index=False)
                reshaped_unigram_wide = reshaped_unigram_wide.reset_index()
                reshaped_unigram_max = reshaped_unigram_wide.groupby(['unigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram_wide = reshaped_unigram_wide.merge(reshaped_unigram_max, on = ['unigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram_wide['label'] = np.where(reshaped_unigram_wide['_merge']=='both', reshaped_unigram_wide['unigram'], '')
                reshaped_unigram_wide = reshaped_unigram_wide[['unigram', 'frequency', 'period','label']]

                fig = (ggplot(reshaped_unigram_wide)
                       + geom_point(aes(x = 'period', y = 'frequency',color = 'unigram'))
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'unigram',group='unigram'))
                       + geom_label(aes(x = 'period', y = 'frequency', label = 'label',size = 1), nudge_y=2)
                       + scale_size_continuous(guide = None)
                       + guides(color=guide_legend(nrow=40))
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1, size = 7),
                               legend_text = element_text(size=7),
                               legend_title = element_text(size=10),
                               legend_key_height = 0.5,
                               legend_key_width = 0.5,
                               figure_size=(10, 5),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)


                plt.gcf().set_dpi(800)
                picture = plt.show()

            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "heatmap", "line"')


        elif time_freq == 'Y':
            period = result['period']
            subset = result['unigram']
            subset = subset.dropna()
            subset_expand = subset.str.split(pat=",", expand=True)
            subset_expand.columns = ['unigram' + str(i + 1) for i in range(len(subset_expand.columns))]
            subset_expand["id"] = subset_expand.index
            test = subset_expand.merge(period, left_index = True, right_index = True)
            reshaped = pd.wide_to_long(test, ['unigram'], i="id", j="period")
            period_re = reshaped['period']
            period_re.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped['unigram']
            reshaped_unigram.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped_unigram.str.split(pat=": ", expand=True)
            reshaped_unigram = reshaped_unigram.rename(columns={0: 'unigram', 1: 'frequency'})
            reshaped_unigram = reshaped_unigram.dropna()
            reshaped_unigram['frequency'] = reshaped_unigram['frequency'].astype(int)
            reshaped_unigram = reshaped_unigram.merge(period_re, left_index = True, right_index = True)

            if plot == 'heatmap':
                reshaped_unigram = reshaped['unigram']
                reshaped_unigram.reset_index(drop=True, inplace=True)
                reshaped_unigram = reshaped_unigram.str.split(pat=": ", expand=True)
                reshaped_unigram = reshaped_unigram.rename(columns={0: 'unigram', 1: 'frequency'})
                reshaped_unigram = reshaped_unigram.dropna()
                reshaped_unigram['frequency'] = reshaped_unigram['frequency'].astype(int)
                reshaped_unigram = reshaped_unigram.merge(period_re, left_index = True, right_index = True)
                reshaped_unigram_max = reshaped_unigram.groupby(['unigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram = reshaped_unigram.merge(reshaped_unigram_max, on = ['unigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram['label'] = np.where(reshaped_unigram['_merge']=='both', reshaped_unigram['unigram'], '')
                reshaped_unigram = reshaped_unigram[['unigram', 'frequency', 'period','label']]

                fig = (ggplot(reshaped_unigram, aes('period', 'unigram', fill='frequency'))
                       + geom_tile(aes(width=0.95, height=0.95))
                       + geom_text(aes(label='frequency'), size=7)
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust= 1),
                               legend_text = element_text(size = 7),
                               legend_title = element_text(color = "black", size = 10),
                               figure_size= (3 + ((len(period) /4)), (2 + (max_words * 0.5))),
                               panel_grid_major = element_line(color='black',size = 0.1),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(800)
                picture = plt.show()

            elif plot == 'line':
                reshaped_unigram_wide = pd.pivot(reshaped_unigram, index = 'unigram', columns = 'period', values = 'frequency')
                reshaped_unigram_wide = reshaped_unigram_wide.fillna(0)
                year_list=list(reshaped_unigram_wide.columns)
                reshaped_unigram_wide = pd.melt(reshaped_unigram_wide, value_vars=year_list,value_name='frequency', ignore_index=False)
                reshaped_unigram_wide = reshaped_unigram_wide.reset_index()
                reshaped_unigram_max = reshaped_unigram_wide.groupby(['unigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram_wide = reshaped_unigram_wide.merge(reshaped_unigram_max, on = ['unigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram_wide['label'] = np.where(reshaped_unigram_wide['_merge']=='both', reshaped_unigram_wide['unigram'], '')
                reshaped_unigram_wide = reshaped_unigram_wide[['unigram', 'frequency', 'period','label']]

                fig = (ggplot(reshaped_unigram_wide)
                       + geom_point(aes(x = 'period', y = 'frequency',color = 'unigram'))
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'unigram',group='unigram'))
                       + geom_label(aes(x = 'period', y = 'frequency', label = 'label',size = 0.2), nudge_y=0.3)
                       + scale_size_continuous(guide = None)
                       + guides(color=guide_legend(nrow=40))
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1, size = 7),
                               legend_text = element_text(size=7),
                               legend_title = element_text(size=10),
                               legend_key_height = 0.5,
                               legend_key_width = 0.5,
                               figure_size=(5 + max_words, (1 + (max_words * 1.0))),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)


                plt.gcf().set_dpi(800)
                picture = plt.show()

            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "heatmap", "line"')

        else:
            sys.exit('Incorrect value for time_freq parameter. Allowed: "ungroup", "Y", "M"')

    elif ngram == 2:
        if time_freq == 'ungroup':
            if plot == 'wordcloud':
                bigram_df = result[['bigram','bigram_freq']]
                bigram_df = bigram_df.dropna()
                bigram_df['bigram'] = bigram_df['bigram'].str.replace(",", " ")
                bigram_df['bigram_freq'] = bigram_df['bigram_freq'].astype(int)
                bigrams_dict = dict(bigram_df.values)
                fig = figure()
                wordcloud_bigram = WordCloud(background_color="white",
                                             colormap='tab20b',
                                             width=2000,
                                             height=1200,
                                             margin=10
                                             ).generate_from_frequencies(bigrams_dict)
                plt.figure(dpi=1200)
                plt.imshow(wordcloud_bigram,interpolation="bilinear")
                fig.set_size_inches(10, 6, forward=True)
                plt.axis('off')
                picture = plt.show()

            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "wordcloud"')

        elif time_freq == 'M':
            period = result['period']
            subset = result['bigram']
            subset = subset.dropna()
            subset_expand = subset.str.split(pat=",", expand=True)

            cols = (' '.join(w) for w in zip(subset_expand.columns[::2].astype(str), subset_expand.columns[1::2].astype(str)))
            subset_expand_adj = pd.DataFrame(subset_expand.iloc[:, ::2].astype(str).values +
                                             ' ' + subset_expand.iloc[:, 1::2].astype(str).values +
                                             ' ', index=subset_expand.index, columns=cols)

            subset_expand_adj.columns = ['bigram' + str(i + 1) for i in range(len(subset_expand_adj.columns))]
            subset_expand_adj["id"] = subset_expand_adj.index
            test = subset_expand_adj.merge(period, left_index = True, right_index = True)
            reshaped = pd.wide_to_long(test, ['bigram'], i="id", j="period")
            period_re = reshaped['period']
            period_re.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped['bigram']
            reshaped_unigram.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped_unigram.str.split(pat=": ", expand=True)
            reshaped_unigram = reshaped_unigram.rename(columns={0: 'bigram', 1: 'frequency'})
            reshaped_unigram = reshaped_unigram.dropna()
            reshaped_unigram['frequency'] = reshaped_unigram['frequency'].astype(int)
            reshaped_unigram = reshaped_unigram.merge(period_re, left_index = True, right_index = True)

            if plot == 'heatmap':
                reshaped_unigram_max = reshaped_unigram.groupby(['bigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram = reshaped_unigram.merge(reshaped_unigram_max, on = ['bigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram['label'] = np.where(reshaped_unigram['_merge']=='both', reshaped_unigram['bigram'], '')
                reshaped_unigram = reshaped_unigram[['bigram', 'frequency', 'period','label']]

                fig = (ggplot(reshaped_unigram, aes('period', 'bigram', fill='frequency'))
                       + geom_tile(aes(width=.95, height=.95))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust= 1),
                               legend_text = element_text(size = 5,vjust = 0.2),
                               legend_title = element_text(color = "black", vjust = 0.8, size = 10),
                               figure_size= (3 + ((len(period) /4)), (2 + (max_words * 2.2))),
                               panel_grid_major = element_line(color='black',size = 0.1),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)


                plt.gcf().set_dpi(800)
                picture = plt.show()


            elif plot == 'line':
                reshaped_unigram_wide = pd.pivot(reshaped_unigram, index = 'bigram', columns = 'period', values = 'frequency')
                reshaped_unigram_wide = reshaped_unigram_wide.fillna(0)
                year_list=list(reshaped_unigram_wide.columns)
                reshaped_unigram_wide = pd.melt(reshaped_unigram_wide, value_vars=year_list,value_name='frequency', ignore_index=False)
                reshaped_unigram_wide = reshaped_unigram_wide.reset_index()
                reshaped_unigram_max = reshaped_unigram_wide.groupby(['bigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram_wide = reshaped_unigram_wide.merge(reshaped_unigram_max, on = ['bigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram_wide['label'] = np.where(reshaped_unigram_wide['_merge']=='both', reshaped_unigram_wide['bigram'], '')
                reshaped_unigram_wide = reshaped_unigram_wide[['bigram', 'frequency', 'period','label']]


                fig = (ggplot(reshaped_unigram_wide)
                       + geom_point(aes(x = 'period', y = 'frequency',color = 'bigram'))
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'bigram',group='bigram'))
                       + geom_label(aes(x = 'period', y = 'frequency', label = 'label',size = 0.2), nudge_y=0.3)
                       + scale_size_continuous(guide = None)
                       + guides(color=guide_legend(nrow=40))
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1, size = 7),
                               legend_text = element_text(size=7),
                               legend_title = element_text(size=10),
                               legend_key_height = 0.5,
                               legend_key_width = 0.5,
                               figure_size=(10, 5),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(800)
                picture = plt.show()

            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "heatmap", "line"')


        elif time_freq == 'Y':
            period = result['period']
            subset = result['bigram']
            subset = subset.dropna()
            subset_expand = subset.str.split(pat=",", expand=True)

            cols = (' '.join(w) for w in zip(subset_expand.columns[::2].astype(str), subset_expand.columns[1::2].astype(str)))
            subset_expand_adj = pd.DataFrame(subset_expand.iloc[:, ::2].astype(str).values +
                                             ' ' + subset_expand.iloc[:, 1::2].astype(str).values +
                                             ' ', index=subset_expand.index, columns=cols)

            subset_expand_adj.columns = ['bigram' + str(i + 1) for i in range(len(subset_expand_adj.columns))]
            subset_expand_adj["id"] = subset_expand_adj.index
            test = subset_expand_adj.merge(period, left_index = True, right_index = True)
            reshaped = pd.wide_to_long(test, ['bigram'], i="id", j="period")
            period_re = reshaped['period']
            period_re.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped['bigram']
            reshaped_unigram.reset_index(drop=True, inplace=True)
            reshaped_unigram = reshaped_unigram.str.split(pat=": ", expand=True)
            reshaped_unigram = reshaped_unigram.rename(columns={0: 'bigram', 1: 'frequency'})
            reshaped_unigram = reshaped_unigram.dropna()
            reshaped_unigram['frequency'] = reshaped_unigram['frequency'].astype(int)
            reshaped_unigram = reshaped_unigram.merge(period_re, left_index = True, right_index = True)

            if plot == 'heatmap':
                reshaped_unigram_max = reshaped_unigram.groupby(['bigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram = reshaped_unigram.merge(reshaped_unigram_max, on = ['bigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram['label'] = np.where(reshaped_unigram['_merge']=='both', reshaped_unigram['bigram'], '')
                reshaped_unigram = reshaped_unigram[['bigram', 'frequency', 'period','label']]

                fig = (ggplot(reshaped_unigram, aes('period', 'bigram', fill='frequency'))
                       + geom_tile(aes(width=.95, height=.95))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust= 1),
                               legend_text = element_text(size = 5,vjust = 0.2),
                               legend_title = element_text(color = "black", vjust = 0.8, size = 10),
                               figure_size= (3 + ((len(period) /4)), (2 + (max_words * 1.7))),
                               panel_grid_major = element_line(color='black',size = 0.1),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(800)
                picture = plt.show()


            elif plot == 'line':
                reshaped_unigram_wide = pd.pivot(reshaped_unigram, index = 'bigram', columns = 'period', values = 'frequency')
                reshaped_unigram_wide = reshaped_unigram_wide.fillna(0)
                year_list=list(reshaped_unigram_wide.columns)
                reshaped_unigram_wide = pd.melt(reshaped_unigram_wide, value_vars=year_list,value_name='frequency', ignore_index=False)
                reshaped_unigram_wide = reshaped_unigram_wide.reset_index()
                reshaped_unigram_max = reshaped_unigram_wide.groupby(['bigram'], sort=False)['frequency'].max()
                reshaped_unigram_max = reshaped_unigram_max.reset_index()
                reshaped_unigram_wide = reshaped_unigram_wide.merge(reshaped_unigram_max, on = ['bigram','frequency'], how = 'left', indicator=True)
                reshaped_unigram_wide['label'] = np.where(reshaped_unigram_wide['_merge']=='both', reshaped_unigram_wide['bigram'], '')
                reshaped_unigram_wide = reshaped_unigram_wide[['bigram', 'frequency', 'period','label']]


                fig = (ggplot(reshaped_unigram_wide)
                       + geom_point(aes(x = 'period', y = 'frequency',color = 'bigram'))
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'bigram',group='bigram'))
                       + geom_label(aes(x = 'period', y = 'frequency', label = 'label',size = 0.2), nudge_y=0.3)
                       + scale_size_continuous(guide = None)
                       + guides(color=guide_legend(nrow=40))
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1, size = 7),
                               legend_text = element_text(size=7),
                               legend_title = element_text(size=10),
                               legend_key_height = 0.5,
                               legend_key_width = 0.5,
                               figure_size=(5 + max_words, (1 + (max_words * 1.0))),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(800)
                picture = plt.show()


            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "heatmap", "line"')

        else:
            sys.exit('Incorrect value for time_freq parameter. Allowed: "ungroup", "Y", "M"')

    elif ngram == 3:
        if time_freq == 'ungroup':
            if plot == 'wordcloud':
                trigram_df = result[['trigram','trigram_freq']]
                trigram_df = trigram_df.dropna()
                trigram_df['trigram'] = trigram_df['trigram'].str.replace(",", " ")
                trigram_df['trigram_freq'] = trigram_df['trigram_freq'].astype(int)

                fig = figure()
                trigram_dict = dict(trigram_df.values)
                wordcloud_trigram = WordCloud(background_color="white",
                                              colormap='tab20b',
                                              width=2000,
                                              height=1200,
                                              margin=10).generate_from_frequencies(trigram_dict)
                plt.figure(dpi=1200)
                plt.imshow(wordcloud_trigram,interpolation="bilinear")
                fig.set_size_inches(10, 6, forward=True)
                plt.axis('off')
                picture = plt.show()

            else:
                sys.exit('Incorrect value for plot parameter. Allowed: "wordcloud"')

        else:
            sys.exit('Incorrect value for time_freq parameter. Allowed: "ungroup"')

    else:
        sys.exit("Incorrect value for ngram parameter. Allowed: 1,2,3.")

    return picture
#%%
