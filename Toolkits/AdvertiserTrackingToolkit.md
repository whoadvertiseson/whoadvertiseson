# WhoAdvertisesOn ToolKit for Tracking Advertisers
## How to Reproduce This Project to Track Advertisers on Different Partisan News Outlets
***

## Overview
[WhoAdvertisesOn](http://whoadvertiseson.org/) is not just a project tracking and summarizing advertising on the partisan news outlet Fox News. It is also an open source data science toolkit that can allow any person or organization to do the same for their own purposes and in their own contexts. Doing so does not require advanced coding skills, but it does require a comfort with editing spreadsheets, and knowledge of some basic tools of data science, including the ability to run Python code locally to process your data. This guide will help you gain that basic knowledge and to get started with tracking advertisers. This guide is written for use with TV channels, but it could be adapted to radio, print, or online media.

## Outline of Steps
This guide will walk you through the following steps:
1. Create your plan for the manual sampling of advertisements
1. Make your own copy of the WhoAdvertisesOn repository from GitHub
1. Start collecting samples and adding them to your spreadsheet
1. Install a Python Anaconda environment and use a Jupyter Notebook to run scripts
1. Start sharing your data

## 1. Create your plan for the manual sampling of advertisements

There is no getting around the need for someone to watch a channel and manually record its advertisements into a spreadsheet. But by using a sampling approach, you can make this as brief, efficient, and accurate as possible.

### Sampling 101
Sampling here means that instead of watching and listing every advertisement, you will just list some of them and use that to make assumptions about the rest. This has two important implications:

- All knowledge derived from sampling should be regarded as estimates, with some existence of error
- The extent and form of that error is shaped by when and how often you take samples.

For example if you only take samples in the morning, you may completely miss advertisers who run ads at night. And if you only take samples once per week, then it is going to be a very long time before you can reliably estimate who the top advertisers are on the channel.

Therefore you need to be systematic and consistent in your sampling. To start, we recommend daily 15 minutes samples spread evenly between morning, afternoon, and evening. After a couple months you could decrease this to every other day. Eventually you will come to know what minutes ads are generally shown in a given hour to make your time use even more efficient.

### Decide on spreadsheet software: Local or online?
There are many options for what software can be used to collect data and how. Only two approaches will be described here, one illustrating a use case where a single individual is conducting all sampling for a channel. And a second illustrating a use case where multiple individuals are collaborating on collecting samples. 

#### **Local Excel for Individual-Only Data Collection** 
In this approach, you simply the edit the data file in place in your working directory. Just add advertisers as you observe them. Use the sort feature to keep them in date order. And be sure to always save the file as a csv file (Comma Seperated Values).

#### **Online Google Sheets for Collaborative Data Collection**
In this approach, you can collaborate with others using an online file, such as a Google Sheet. Each collaborator can add advertisers as they are observed. Then a single point person can keep this file sorted, and can download into a local working directory as needed to run scripts (more on that later). In this collaborative approach care must be taken to ensure that collaborators are being consistent with their company and product names. For example there is a danger of ending up with "Kraft Heinz", "Kraft Hienz", "Kraft Heinz Co.", "Kraft Heinz Company" etc., which should ideally all have the same name. The point person must be vigilent about this. Because of this, a larger number of less trained collaborators increases the risk that the data will lose integrity.

## 2. Make your own copy of the WhoAdvertisesOn repository from GitHub
GitHub is a hosted version control service that is commonly used to share and collaborate on open source software projects. It can also be used an open repository for data. WhoAdvertisesOn hosts all of its code and data in a GitHub repository available here: [https://github.com/whoadvertiseson/whoadvertiseson](https://github.com/whoadvertiseson/whoadvertiseson)

The first step is copy all of our code and data. At the top right of the main page column you will see a green button button that reads "Code". This will allow you to download (aka "clone") the repository. If you are an experienced GitHub user you may do this many ways.

If you are not an experienced GitHub user you have two options. Firstly you can simply choose the "Download ZIP" option to download the files to your local computer. Unzip these files into some working directory of your choice. Just keep in mind that WhoAdvertisesOn is a living repository, and its code will be updated to fix problems and new features added, which means that what you just downloaded is a snapshot in time. To access newest features at a later date you will need to go back and read up on what has changed and update your files manually. As this is a fairly simple repository, it should be not too complicated to do so. But the alternative is to install and use the [GitHub Desktop](https://desktop.github.com/) application, which will allow you to download the files but will also keep you apprised of changes. We will strive to make all new changes backwards compatible.

To get your downloaded directory ready to begin collecting data simply create a folder at the top level named after the channel you will be tracking. This will live next to the existing "FoxNews" example folder. Then, make a copy of "ToolkitGuide/Templates/ChannelName_ObservedAdvertisements.csv" and put it in this new folder, replacing "ChannelName" with the name of the channel you are tracking.

## 3. Start collecting samples and adding them to your spreadsheet
The template csv file [ChannelName_ObservedAdvertisements.csv](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/ToolkitGuide/Templates/ChannelName_ObservedAdvertisements.csv), which you copied and renamed earlier, has a header row that defines column names. This row must be preserved exactly, because the scripts rely on recognizing these column names. Therefore your data should begin in row 2. The columns names are CompanyName,ProductName, DateObserved, TimeOfDay, Channel, ShowName. Additional columns may be supported by future scripts. The best way to understand each column and their use is to look at the example [FoxNews/FoxNews_ObservedAdvertisements.csv](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/FoxNews/FoxNewsChannel_ObservedAdvertisements.csv) file. As noted above, consistency in naming is important, not just for companies, but also for products, times of day, shows etc. So consider it one of your main responsibilities as data curator to maintain this consistency across all of the rows of your data. The scripts that will help to process your data depend on it.

Note that the content on partisan channels can be very toxic and triggering. It is thus a lot to ask of someone to watch it everyday. Additionally there may already be organizations that track and catalog the content of these channels (such as Media Matters in the United States). As such it may not be necessary to even watch with the sound on when you are just tracking advertisements. Please take care, and if you need a day off you can certainly take it without overly undermining the accuracy of the sampling.

## 4. Install a Python Anaconda environment and use a Jupyter Notebook to run scripts
Currently there is only one script for processing data, but it is a core script that calculates the recent top advertisers on the channel and creates a bar chart image. Note that this script requires at least 50 rows of data, so it cannot be used until you have done at least some sampling of advertisements.

To setup a Python environment on your computer, download and install Anaconda from the following URL. Remember to choose the installer for Python 3.x. [https://www.anaconda.com/products/individual#download-section](https://www.anaconda.com/products/individual#download-section)

The core script that should be run regularly is generateTopAdvertisers, and these are two version is the Scripts folder. One version, [generateTopAdvertisers.ipynb](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/Scripts/generateTopAdvertisers.ipynb), can be run from from a Jupyter Notebook, and is the best option for non-coders. After installing Anaconda, on a Mac, Jupyter Notebook can be launched by opening the Terminal application and typing "jupyter notebook" at the prompt. On Windows you can click on the Jupyter Notebook icon installed by Anaconda in the start menu. In both cases the notebook will open in a web browser tab. In that tab, navigate to find the Scripts folder in the WhoAdvertisesOn directory and open the file [generateTopAdvertisers.ipynb](https://github.com/whoadvertiseson/whoadvertiseson/blob/main/Scripts/generateTopAdvertisers.ipynb). Follow the guidance contained in that notebook to run the script. Note that the first time you do this the configuration may be hard and time consuming. But once it is done the script can be run daily in a matter of seconds as part of your regular workflow. You can customize the script as needed, and if you have ideas or innovations please share them with the original project.

## 5. Start sharing your data
Once you have successfuly completed the above four steps, you should have a functioning system for collecting sample data on advertisements, and drawing conclusions and making visualizations based on that data. There are of course many options for sharing that data and many possible uses of the data. The spirit of this project is based on the notion of not just open source but even more essentially, the notion of open data. As such we recommend you consider releasing your data as open data through a platform like GitHub or some of the many open data platforms available. 

Finally, if you do find use for this toolkit, please acknowledge the original project. And also if you build any useful addons please consider releasing those as open source, or contributing them to the original repository.

If you have any questions, comments or want assistance, please contact whoadvertiseson@protonmail.com
