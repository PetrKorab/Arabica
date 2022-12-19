# Data visualization module


from plotnine import *
from arabica import arabica_freq
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd



def cappuccino(text,
               time,
               plot,
               ngram,
               time_freq,
               max_words,
               stopwords,
               skip,
               numbers,
               punct,
               lower_case):

    result = arabica_freq(text=text,
                          time=time,
                          time_freq=time_freq,
                          max_words=max_words,
                          stopwords=stopwords,
                          skip=skip,
                          numbers=numbers,
                          punct=punct,
                          lower_case=lower_case)


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
                                              margin=7).generate_from_frequencies(unigrams_dict)
                plt.figure(dpi=1200)
                plt.imshow(wordcloud_unigram,interpolation="bilinear")
                fig.set_size_inches(10, 6, forward=True)
                plt.axis('off')
                picture = plt.show()


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
                fig = (ggplot(reshaped_unigram, aes('period', 'unigram', fill='frequency'))
                       + geom_tile(aes(width=.95, height=.95))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 6),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)


                plt.gcf().set_dpi(500)
                picture = plt.show()


            elif plot == 'line':
                fig = (ggplot(reshaped_unigram)
                       + geom_point(aes(x = 'period', y = 'frequency', color = 'unigram'))
                       + geom_text(aes(x = 'period', y = 'frequency', label = 'unigram',size = 2),nudge_y=6)
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'unigram',group='unigram'))
                       + scale_size_continuous(guide = None)
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 6),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(500)
                picture = plt.show()


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
                fig = (ggplot(reshaped_unigram, aes('period', 'unigram', fill='frequency'))
                       + geom_tile(aes(width=.95, height=.95))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust='1'),
                               figure_size=(10, 6),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(500)
                picture = plt.show()


            elif plot == 'line':
                fig = (ggplot(reshaped_unigram)
                       + geom_point(aes(x = 'period', y = 'frequency', color = 'unigram'))
                       + geom_text(aes(x = 'period', y = 'frequency', label = 'unigram',size = 2),nudge_y=6)
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'unigram',group='unigram'))
                       + scale_size_continuous(guide = None)
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 6),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(500)
                picture = plt.show()

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
                                             margin=7
                                             ).generate_from_frequencies(bigrams_dict)
                plt.figure(dpi=1200)
                plt.imshow(wordcloud_bigram,interpolation="bilinear")
                fig.set_size_inches(10, 6, forward=True)
                plt.axis('off')
                picture = plt.show()

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
                fig = (ggplot(reshaped_unigram, aes('period', 'bigram', fill='frequency'))
                       + geom_tile(aes(width=.95, height=.95))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 8),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)


                plt.gcf().set_dpi(500)
                picture = plt.show()


            elif plot == 'line':
                fig = (ggplot(reshaped_unigram)
                       + geom_point(aes(x = 'period', y = 'frequency', color = 'bigram'))
                       + geom_text(aes(x = 'period', y = 'frequency', label = 'bigram',size = 2),nudge_y=6)
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'bigram',group='bigram'))
                       + scale_size_continuous(guide = None)
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 8),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(500)
                picture = plt.show()

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
                fig = (ggplot(reshaped_unigram, aes('period', 'bigram', fill='frequency'))
                       + geom_tile(aes(width=.95, height=.95))
                       + geom_text(aes(label='frequency'), size=10)
                       + theme_minimal()
                       + scale_fill_gradient(name = "frequency",
                                             low = "#f0f4ed",
                                             high = "#496160")
                       + theme(axis_title_x=element_text(colour = "black"),
                               axis_title_y=element_text(colour="black"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 8),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)


                plt.gcf().set_dpi(500)
                picture = plt.show()


            elif plot == 'line':
                fig = (ggplot(reshaped_unigram)
                       + geom_point(aes(x = 'period', y = 'frequency', color = 'bigram'))
                       + geom_text(aes(x = 'period', y = 'frequency', label = 'bigram',size = 2),nudge_y=6)
                       + geom_line(aes(x = 'period', y = 'frequency', color = 'bigram',group='bigram'))
                       + scale_size_continuous(guide = None)
                       + theme_minimal()
                       + theme(axis_title_x=element_text(colour = "black",size = 7),
                               axis_title_y=element_text(colour="black", size = 7),
                               axis_title=element_text(face="bold"),
                               axis_text_x=element_text(colour = "black", rotation=45, hjust=1),
                               figure_size=(10, 8),
                               panel_grid_major = element_blank(),
                               panel_background = element_rect(colour = "white", fill = "white"),
                               plot_background = element_rect(colour = 'white',fill = "white"))
                       ).draw(show=False, return_ggplot=True)

                plt.gcf().set_dpi(500)
                picture = plt.show()


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
                                              margin=7).generate_from_frequencies(trigram_dict)
                plt.figure(dpi=1200)
                plt.imshow(wordcloud_trigram,interpolation="bilinear")
                fig.set_size_inches(10, 6, forward=True)
                plt.axis('off')
                picture = plt.show()


    return picture