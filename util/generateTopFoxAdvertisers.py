import pandas as pd
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# LOAD THE RAW OBSERVER ADVERTISEMENTS DATA
observedAdvertisers = pd.read_csv(
    "FoxNewsChannel_ObservedAdvertisements.csv", parse_dates=['DateObserved'])
print("advertisers file loaded")
print(observedAdvertisers.head())

# HANDLE DATES AND LIMIT CALCULATION TO MOST RECENT THREE MONTHS
observedAdvertisers['DateObserved'] = pd.to_datetime(
    observedAdvertisers['DateObserved'], errors='coerce')
observedAdvertisers['year'] = observedAdvertisers['DateObserved'].dt.year
observedAdvertisers['month'] = observedAdvertisers['DateObserved'].dt.month
observedAdvertisers['day'] = observedAdvertisers['DateObserved'].dt.day
threemonthsago = pd.datetime.today() - timedelta(94)
observedAdvertisers = observedAdvertisers[(observedAdvertisers['DateObserved'].dt.year == 1970) | (
    observedAdvertisers['DateObserved'] >= threemonthsago)]

# CALCULATE FREQUENCIES
topAdvertisers = pd.value_counts(
    observedAdvertisers.CompanyName).to_frame().reset_index()
topAdvertisers.columns = ['CompanyName', 'AdsSampled']
# Require multiple ads to be listed as 'top'
topAdvertisers = topAdvertisers[topAdvertisers['AdsSampled'] > 1]
print(topAdvertisers.head())

# BUILD PRODUCT LIST (probably a more efficient way to do this)
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
                    print("in")
                    lastSeen = inner_row['DateObserved']

    topAdvertisers.loc[index, "ProductsAdvertised"] = ", ".join(productsList)
    topAdvertisers.loc[index, "LastObserved"] = lastSeen

# ADD INDICATION OF TIMESPAN (probably a more efficient way to do this)
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
total = topAdvertisers['AdsSampled'].sum()
threshhold = 3  # manually decide where to draw the line of what is a top advertiser
topAdvertisers["EstFreqProminence"] = topAdvertisers['AdsSampled']/total
topAdvertisers_subset = topAdvertisers.loc[(
    topAdvertisers['AdsSampled'] >= threshhold)]
names = topAdvertisers_subset['CompanyName']
plt.rcdefaults()
fig, ax = plt.subplots(constrained_layout=True)
prominence = topAdvertisers_subset['EstFreqProminence']
ax.barh(names, prominence)
y_pos = np.arange(len(names))
ax.set_yticks(y_pos)
ax.set_yticklabels(names)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Proportion of Total Sampled Ads')
title = ax.set_title("\n".join(wrap("Estimates of Most Frequent Fox News Channel Advertisers (2021 to date)", 40)),
                     fontsize=11, fontweight="bold", loc="center")
fig.subplots_adjust(bottom=0.12, left=0.4)  # or whatever
plt.figtext(0.07, 0.01, 'Estimates based on daily sampling excluding overnight hours, advertisements by nonprofit organizations, and local advertisements ',
            horizontalalignment='left', fontsize=6)
plt.savefig('FoxNewsChannel_RecentTopAdvertisers.png', dpi=200)
# plt.show()


# TBD: Join to a file that contains general information about companies

# OUTPUT RECENT TOP OBSERVED ADVERTISMENTS FILE
topAdvertisers.to_csv("FoxNewsChannel_RecentTopAdvertisers.csv", index=False)
