## Test for sentiment analysis and breakpoint identification method

import unittest
import pandas as pd
import numpy as np
from arabica import coffee_break

class TestCoffeeBreakFunction(unittest.TestCase):
    # test data
    data = pd.DataFrame({
        'text': ['Same folks said daikon paste could treat a cytokine storm #PfizerBioNTech https://t.co/xeHhIMg1kF',
                 '''While the world has been on the wrong side of history this year, hopefully, the biggest vaccination effort we've evâ€¦ https://t.co/dlCHrZjkhm''',
                 "#coronavirus #SputnikV #AstraZeneca #PfizerBioNTech #Moderna #Covid_19 Russian vaccine is created to last 2-4 yearsâ€¦ https://t.co/ieYlCKBr8P",
                 "Facts are immutable, Senator, even when you're not ethically sturdy enough to acknowledge them. (1) You were born iâ€¦ https://t.co/jqgV18kch4",
                 "Explain to me again why we need a vaccine @BorisJohnson @MattHancock #whereareallthesickpeople #PfizerBioNTechâ€¦ https://t.co/KxbSRoBEHq",
                 "Does anyone have any useful advice/guidance for whether the COVID vaccine is safe whilst breastfeeding?â€¦ https://t.co/EifsyQoeKN",
                 "ID19Vaccine Monday, #US says',                               
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

        'time': ['21/09/2020 15:27',
                 '21/09/2020 15:27',
                 '25/08/2020 23:30',
                 '26/08/2020 21:43',
                 '23/07/2020 17:58',
                 '26/07/2020 21:43',
                 '26/06/2020 21:43',
                 '25/06/2020 04:14',
                 '30/05/2020 17:53',
                 '26/05/2020 21:43',
                 '17/05/2020 16:45',
                 '31/04/2020 10:38',
                 '21/04/2020 03:44',
                 '25/03/2020 04:14',
                 '13/03/2020 18:33',
                 '26/02/2020 21:43',
                 '25/02/2020 20:33',             
                 '26/06/2020 21:43']})


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
        self.assertTrue("period" in result.index.names)   # Returns a dataframe with a period column
        self.assertTrue("sentiment" in result.columns)    # Returns a dataframe with a sentiment columns
        self.assertIsNotNone(result)                      # Returns a picture with graphical output, assuming picture is not None


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
