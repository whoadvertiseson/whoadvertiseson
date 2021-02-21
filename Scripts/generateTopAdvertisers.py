import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# ------------------------------------------
# CONFIG OPTIONS (these need to be customized for the channel)
# Where does the CSV file live currently?
observedAdvertisersFilePath = 'FoxNews/FoxNewsChannel_ObservedAdvertisements.csv'

# Where should the top advertisers data file be saved?
topAdvertisersFilePath = 'FoxNews/FoxNewsChannel_RecentTopAdvertisers.csv'

# Where should the top advertisers image be saved?
topAdvertisersImagePath = 'FoxNews/FoxNewsChannel_RecentTopAdvertisers.png'

# For how long prior to today, if available, should records be compiled
numberDaysPast = 93  # default to about three months

# What should be the title of the bar chart?
topAdvertisersImageTitle = "Estimates of Most Frequent Fox News Channel Advertisers"

# What should be the footnote of the bar chart?
topAdvertisersImageFootnote = 'Estimates based on daily sampling excluding overnight hours, advertisements by nonprofit organizations, and local advertisements'

# Above what proportion level should we include in the chart?
# .01 = 1 in every 100 ads, .02 = 2 in every 100 ads etc.
# This should be adjusted so that you have between 20 and 40 advertisers listed
topAdvertisersThreshhold = .01


# ------------------------------------------
# LOAD THE RAW OBSERVER ADVERTISEMENTS DATA
print("Loading advertisers file")
observedAdvertisers = pd.read_csv(
    observedAdvertisersFilePath, parse_dates=['DateObserved'])
# print(observedAdvertisers.head())

if len(observedAdvertisers.index) < 50:
    print("ERROR: Not enough observations to determine top advertisers. The minimum amount is 50.")
else:
    # HANDLE DATES AND LIMIT CALCULATION TO MOST RECENT THREE MONTHS
    print("Determining dates")
    observedAdvertisers['DateObserved'] = pd.to_datetime(
        observedAdvertisers['DateObserved'], errors='coerce')
    observedAdvertisers['year'] = observedAdvertisers['DateObserved'].dt.year
    observedAdvertisers['month'] = observedAdvertisers['DateObserved'].dt.month
    observedAdvertisers['day'] = observedAdvertisers['DateObserved'].dt.day
    howLongAgo = dt.datetime.today() - dt.timedelta(days=numberDaysPast)
    observedAdvertisers = observedAdvertisers[(observedAdvertisers['DateObserved'].dt.year == 1970) | (
        observedAdvertisers['DateObserved'] >= howLongAgo)]

    # CHECK FOR BIAS IN TIME OF DAY
    print("Checking for time of day bias")
    checkseries = observedAdvertisers.groupby(['TimeOfDay']).size()
    checkseries.sort_values(ascending=True, inplace=True)
    maxvariation = checkseries[len(checkseries.index)-1] - checkseries[0]
    totalsum = checkseries.sum()
    biascheck = maxvariation/totalsum
    labels = checkseries.index.tolist()
    if (biascheck > 0.1):
        print("  WARNING: TimeOfDay is biased in the data which may effect the accuracy of estimates.")
        print("  CONT.:", labels[0], "is underrepresented.")
        print("  CONT.:", labels[len(checkseries.index)-1],
              "is overrepresented.")
        print("  CONT.: Adjust your sampling accordingly.")

    # CALCULATE FREQUENCIES
    print("Calculating top advertisers")
    topAdvertisers = pd.value_counts(
        observedAdvertisers.CompanyName).to_frame().reset_index()
    topAdvertisers.columns = ['CompanyName', 'AdsSampled']
    # Require multiple ads to be listed as 'top'
    topAdvertisers = topAdvertisers[topAdvertisers['AdsSampled'] > 1]
    if len(topAdvertisers.index) < 5:
        print("ERROR: Not enough distinct advertisers. The minimum amount is 5.")
    else:
        print("Preview")
        print(topAdvertisers.head())

        # BUILD PRODUCT LIST (probably a more efficient way to do this)
        print("Building product lists")
        for index, row in topAdvertisers.iterrows():
            productsList = []
            lastProduct = ''
            lastSeen = ''
            for inner_index, inner_row in observedAdvertisers.iterrows():
                if row['CompanyName'] == inner_row['CompanyName']:
                    product = inner_row['ProductName']
                    if (product not in productsList):
                        productsList.append(product)
                    if lastSeen == '':
                        lastSeen = inner_row['DateObserved']
                    else:
                        if inner_row['DateObserved'] > lastSeen:
                            lastSeen = inner_row['DateObserved']

            topAdvertisers.loc[index, "ProductsAdvertised"] = ", ".join(
                productsList)
            topAdvertisers.loc[index, "LastObserved"] = lastSeen

        # ADD INDICATION OF TIMESPAN
        print("Determining timeframe")
        timeSpan = ''
        if (observedAdvertisers['year'].min() != observedAdvertisers['year'].max()):
            timeSpan = ''
            # We have until December 2021 to add code here
        else:
            if (observedAdvertisers['month'].min() == observedAdvertisers['month'].max()):
                timeSpan = 'Month of ' + \
                    str(int(observedAdvertisers['month'].min())) + \
                    '/' + str(int(observedAdvertisers['year'].min()))
            else:
                timeSpan = '' + str(int(observedAdvertisers['month'].min())) + '/' + str(int(observedAdvertisers['year'].min(
                ))) + ' to ' + str(int(observedAdvertisers['month'].max())) + '/' + str(int(observedAdvertisers['year'].max()))

        topAdvertisers['TimeSpan'] = timeSpan

        # MAKE A CHART OF TOP ADVERTISERS AND SAVE TO FILE
        print("Building barchart")
        total = topAdvertisers['AdsSampled'].sum()
        topAdvertisers["EstFreqProminence"] = topAdvertisers['AdsSampled']/total
        topAdvertisers_subset = topAdvertisers.loc[(
            topAdvertisers['EstFreqProminence'] >= topAdvertisersThreshhold)]
        names = topAdvertisers_subset['CompanyName']
        plt.rcdefaults()
        fig, ax = plt.subplots()
        prominence = topAdvertisers_subset['EstFreqProminence']
        ax.barh(names, prominence)
        y_pos = np.arange(len(names))
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Proportion of Total Sampled Ads')
        datestr = dt.datetime.today().strftime("%b-%d-%y")
        title = ax.set_title("\n".join(wrap(topAdvertisersImageTitle+' (as of '+datestr+')', 40)),
                             fontsize=11, fontweight="bold", loc="center")
        fig.subplots_adjust(bottom=0.12, left=0.4)
        plt.figtext(0.07, 0.01, topAdvertisersImageFootnote,
                    horizontalalignment='left', fontsize=6)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=9)
        # plt.show()  # use this to show the image before saving it

        # OUTPUT RECENT TOP OBSERVED ADVERTISMENTS FILES
        print("Outputting files")
        plt.savefig(topAdvertisersImagePath, dpi=200)
        topAdvertisers.to_csv(topAdvertisersFilePath, index=False)

        print("Success")
