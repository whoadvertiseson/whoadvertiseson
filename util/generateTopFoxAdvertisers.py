import pandas as pd
from datetime import date, timedelta

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
    productsList = ''
    lastProduct = ''
    lastSeen = ''
    for inner_index, inner_row in observedAdvertisers.iterrows():
        if row['CompanyName'] == inner_row['CompanyName']:
            product = inner_row['ProductName']
            if (product != lastProduct):
                if productsList == '':
                    productsList = product
                else:
                    productsList = productsList + ', ' + product
                if lastSeen == '':
                    lastSeen = inner_row['DateObserved']
                else:
                    if inner_row['DateObserved'] > lastSeen:
                        lastSeen = inner_row['DateObserved']
                lastProduct = product

    topAdvertisers.loc[index, "ProductsAdvertised"] = productsList
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

# TBD: Join to a file that contains general information about companies

# OUTPUT RECENT TOP OBSERVED ADVERTISMENTS FILE
topAdvertisers.to_csv("FoxNewsChannel_RecentTopAdvertisers.csv", index=False)
