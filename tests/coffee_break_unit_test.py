## Test for sentiment analysis and breakpoint identification method

import unittest
import pandas as pd
import numpy as np
from arabica import coffee_break

class TestCoffeeBreakFunction(unittest.TestCase):    
    #test data#
    data = pd.DataFrame({
        'text': ['Same folks said daikon paste could treat a cytokine storm #PfizerBioNTech https://t.co/xeHhIMg1kF',
                '''While the world has been on the wrong side of history this year, hopefully, the biggest vaccination effort we've evâ€¦ https://t.co/dlCHrZjkhm''',
                 "#coronavirus #SputnikV #AstraZeneca #PfizerBioNTech #Moderna #Covid_19 Russian vaccine is created to last 2-4 yearsâ€¦ https://t.co/ieYlCKBr8P",
                "Facts are immutable, Senator, even when you're not ethically sturdy enough to acknowledge them. (1) You were born iâ€¦ https://t.co/jqgV18kch4",
                "Explain to me again why we need a vaccine @BorisJohnson @MattHancock #whereareallthesickpeople #PfizerBioNTechâ€¦ https://t.co/KxbSRoBEHq",
                "Does anyone have any useful advice/guidance for whether the COVID vaccine is safe whilst breastfeeding?â€¦ https://t.co/EifsyQoeKN",
                "it is a bit sad to claim the fame for success of #vaccination on patriotic competition between USA, Canada, UK andâ€¦ https://t.co/IfMrAyGyTP",
                "There have not been many bright days in 2020 but here are some of the best",
                "#BidenHarris winning #Election2020â€¦ https://t.co/77u4f8XXfx",
                'Covid vaccine; You getting it?',            
                '#CovidVaccine #covid19 #PfizerBioNTech #Moderna',
                '#CovidVaccine',            
                'States will start getting #COVID19Vaccine Monday, #US says',
                '#pakustv #NYC #Healthcare #GlobalGoalsâ€¦ https://t.co/MksOvBvs5w',
                "while deaths are closing in on the 300,000 mark... millions of people wait #PfizerBioNTech #Vaccine !",
                'The first Uâ€¦ https://t.co/uQ3A2f7SVP',
                '@cnnbrk #COVID19 #CovidVaccine #vaccine #Corona #PfizerBioNTech #bbcnews #NYTimes #BBCNews Best wishes to the USâ€¦ https://t.co/9xWmfU3LZj',
                'The agency also released new information for health care providers and for patients as the US shipped millions of dâ€¦ https://t.co/sG6BtD7jD9',
                'For all the women and healthcare providers who have been asking about the safety of the #PfizerBioNTechâ€¦ https://t.co/ow0Pglkwte',
                '"Expect 145 sites across all the states to receive vaccine on Monday, another 425 sites on Tuesday," said the officâ€¦ https://t.co/HiUVYJzOBY',
                "Trump announces #vaccine rollout 'in less than 24 hours",
                "The first Americans will be vaccinated againstâ€¦ https://t.co/2FzQSMnhoY",
                "UPDATED: #YellowFever &amp; #COVID19 #ImmunityPassports - Part Two",            
                "#SARSCoV2 #PfizerBioNtech #Britain #Decemberâ€¦ https://t.co/qKT7Rst9aW",
                'Coronavirus: Iran reports 8,201 new cases, 221 deaths in the last 24 hours #Iran #coronavirus #PfizerBioNTechâ€¦ https://t.co/mwDNAdmb7F',
                '.@Pfizer will rake in billions from its expensive #CovidVaccine but @AlbertBourla refuses to cut the price for loweâ€¦ https://t.co/eC94w3TUl0',
                'The trump administration failed to deliver on vaccine promises, *shocker* #COVIDIOTS #coronavirus #CovidVaccineâ€¦ https://t.co/hew6eHTUrD',
                'How much did the #fda get paid to approve this all of a sudden now? money makes the world go around. #vaccineâ€¦ https://t.co/GT9qVVNbKj',
                'Anyone wondering why day after #PfizerBioNTech approval in the UK people were getting vaccinated but all we are tolâ€¦ https://t.co/tPSyL9CUYE',
                "Trump announces #vaccine rollout 'in less than 24 hours",
                "The first Americans will be vaccinated againstâ€¦ https://t.co/P9esXr3zpS",
                "The US Food and Drug Administration (FDA) has granted emergency use authorization to Pfizer-BioNTech's mRNAâ€¦ https://t.co/dPLokxGtBa",
                "#docnosofficial #covid19â€¦ https://t.co/qOd5TPLYvA",
                "#ThankYouNHS @NHSuk @MHRAgovuk and #PfizerBioNTech @pfizer for making the #CovidVaccine dream possâ€¦ https://t.co/3KvJ7UP432",                                                                                                                                                                                                                           'Wear a mask, wash your hands, and remain socially distant when possible. #stayhome #StayAtHome #StayAtHomeSaveLivesâ€¦ https://t.co/Jrlrg6bm0w',
                "â¦@AvgerinosMoscowâ© #PfizerBioNTech #FDA approval Apprentice Style!",
                "â¦@realDonaldTrumpâ©: â€śApprove the #vaccine or youâ€¦ https://t.co/f64cOP5DV6",
                'Interesting and very detailed article showing up how a well tested #supplychain, with #sharedvisibility will help dâ€¦ https://t.co/yt3vn67mVg',
                 "đź’‰ #Vaccine #TrumpVaccine #AstraZeneca #PfizerBioNTech #Pfizervaccine #PfizerCovidVaccine #Pfizer's COVID-19 belongâ€¦ https://t.co/ldxQhN6uix",
                "@ZubyMusic 6 deaths so far."
                """It's only death, nothing to worry about then đź¤"""],
                
        'time': ['21/09/2009 15:27',
                '21/09/2009 15:27',
                '25/06/2020 23:30',
                '26/01/2020 21:43',
                '23/04/2020 17:58',
                '26/01/2020 21:43',
                '26/01/2020 21:43',
                '25/03/2019 04:14',
                '30/10/2009 17:53',
                '26/01/2020 21:43',
                '17/09/2009 16:45',
                '31/08/2020 10:38',
                '21/03/2016 03:44',
                '25/03/2019 04:14',
                '13/01/2019 18:33',
                '26/01/2020 21:43',
                '25/10/2020 20:33',
                '22/05/2015 08:31',
                '24/07/2012 08:18',
                '24/01/2010 04:43',
                '26/01/2020 21:43',
                '23/04/2012 12:18',
                '26/01/2020 21:43',
                '16/03/2014 03:52',
                '26/01/2020 21:43',
                '16/01/2010 23:59',
                '17/09/2009 16:45',
                '17/10/2011 19:03',
                '29/07/2019 20:03',
                '26/01/2020 21:43',
                '26/01/2020 21:43',
                '30/03/2020 13:47',
                '29/01/2016 15:54',
                '16/12/2016 20:29',
                '26/01/2020 21:43',
                '22/06/2017 06:22',
                '13/10/2020 15:21',
                '23/12/2010 11:51',
                '31/01/2014 01:25',
                '26/01/2020 21:43']})


    def test_coffee_break(self):
        date_format = "us"
        model = "vader"
        skip = None
        preprocess = True
        time_freq = "M"
        n_breaks = 3

        # Call the coffee_break function
        result = coffee_break(text=self.data['text'],
                              time=self.data['time'],                              
                              date_format=date_format,
                              model=model, 
                              skip=skip, 
                              preprocess=preprocess, 
                              time_freq=time_freq,
                              n_breaks=n_breaks)

        # Perform assertions based on the expected behavior
        self.assertTrue("period" in result.columns)      # Returns a dataframe with a period column
        self.assertTrue("sentiment" in result.columns)   # Returns a dataframe with a sentiment columns
        self.assertIsNone(result)                        # Returns a picture with graphical output, assuming picture is None when using line plot for monthly frequency


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
