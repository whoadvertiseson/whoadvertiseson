# WhoAdvertisesOn
## Toolkit for tracking advertisers on partisan news channels with sampling, data science, and open data. Now tracking Fox News.

### Project Purpose
For-profit television news is funded in part through advertising. To boost viewership, commercial news channels set aside journalistic standards in favor of sensational and emotional styles of programming. Furthermore, partisan channels, such as conservative media, selectively report or distort information for political gain. These deviations from journalistic standards have real world consequences that effect lives and families of even non-viewers. Therefore everyone has a right to know whose dollars are funding these channels.

### Sampling Strategy
The most comprehensive way to know who is advertising on a particular channel would entail watching every hour every day, yet this is not feasible for volunteers. Therefore the notion of "sampling" is used to gather data with less effort. Our strategy is that nearly every day a volunteer watches a channel for a fifteen minute interval at an arbitrary time (excluding overnight), and collects data about observed advertisements. Over time this should generate a comprehensive picture of advertising on a particular channel.

### Data Collection
The following data is collected for each observed advertisement: 

*CompanyName, ProductName, DateObserved, TimeOfDay, Channel, ShowName*

### Data Files
Currently data is only being collected about Fox News Channel, and the following files are available in the repository: 

- *[DATA: FoxNewsChannel_ObservedAdvertisements.csv](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/FoxNews/FoxNewsChannel_ObservedAdvertisements.csv)*
- *[DATA: FoxNewsChannel_RecentTopAdvertisers.csv](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/FoxNews/FoxNewsChannel_RecentTopAdvertisers.csv)*
- *[IMAGE: FoxNewsChannel_RecentTopAdvertisers.png](https://raw.githubusercontent.com/whoadvertiseson/whoadvertiseson/main/FoxNews/FoxNewsChannel_RecentTopAdvertisers.png)*

### Toolkit 
WhoAdvertisesOn is not just a project tracking and summarizing advertising on a single partisan news outlet. It is also an open source data science toolkit that can allow any person or organization to do the same for their own purposes and in their own contexts. Doing so does not require advanced coding skills. Read the [Toolkit Guide here](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/Toolkits/AdvertiserTrackingToolkit.md). 


### Contact
If you have questions or comments please find us on Twitter at [https://twitter.com/WhoAdvertisesOn](https://twitter.com/WhoAdvertisesOn), or write to us at whoadvertiseson@protonmail.com

### Licenses

- Data files (ie. .csv) are governed by an Open Data Commons Open Database License (ODbL) v1.0 as detailed in the file LICENSE_data
- Code files (ie. .py) are governed by a GNU GENERAL PUBLIC LICENSE Version 3 as detailed in the file LICENSE_code
