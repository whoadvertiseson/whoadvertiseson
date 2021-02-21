# WhoAdvertisesOn Data Science ToolKit Guide
## *For Reproducing This Project to Track Advertisers on Different Partisan News Channels*
***

## Overview
WhoAdvertisesOn is not just a project tracking and summarizing advertising on a single partisan news channel. It is also an open source data science toolkit that can allow any person or organization to do the same for their own purposes and in their own contexts. Doing so does not require advanced coding skills, but it does require a comfort with editing spreadsheets, and knowledge of some basic tools of data science, including the ability to run Python code locally to process your data. This guide will help you with gaining that basic knowledge.

## Outline of Steps
This guide will provide details on the following steps:
1. Make your own copy of the WhoAdvertisesOn repository from GitHub
1. Create your plan for the manual sampling of advertisements
1. Start collecting samples and adding them to your spreadsheet
1. Install a Python Anaconda environment and use a Jupyter Notebook to run scripts
1. Options for sharing your data

## 1. Make your own copy of the WhoAdvertisesOn repository from GitHub
GitHub is a hosted version control service that is commonly used to share and collaborate on open source software projects. It can also be used an open repository for data. WhoAdvertisesOn hosts all of its code and data in a GitHub repository available here: https://github.com/whoadvertiseson/whoadvertiseson

The first step is copy all of our code and data. At the top right of the main page columns you will see a green button button that reads "Code". This will allow you to download (aka "clone") the repository. If you are an experience GitHub user you may do this many ways -- have fun! 

If you are not an experienced GitHub user you can simply choose the "Download ZIP" option to download the files to your local computer. Unzip these files into some working directory of your choice. Just keep in mind that WhoAdvertisesOn is a living repository, and its code will be updated to fix problems and new features added, which means that what you just downloaded is a snapshot in time. To access the newest features at a later date you will need to go back and read up on what has changed and update your files manually. As this is a farily simple repository, it should be not too complicated to do so.

To get this directory ready to begin collecting data simple create a folder at the top level named after the channel you will be tracking. This can live next to the existing "FoxNews" example folder. Make a copy of "ToolkitGuide/Templates/ChannelName_ObservedAdvertisements.csv" and put it in this new folder, renamed with your channel name.

## 2. Create your plan for the manual sampling of advertisements

There is no getting around the need for someone to watch a channel and manually record its advertisements into a spreadsheet. But by using a sampling approach, you can make this as painless, efficient and accurate as possible.

### Sampling 101
Sampling here means that instead of watching and recording every advertisement, you will just record some of them and use that to make assumptions about the rest. This has two important implications:

- All knowledge derived from sampling must be regarded as estimates, with some possibility of error
- The extent and form of that error is shaped by when and how often you take samples.

For example if you only take samples in the morning, you may completely miss advertisers who run ads at night. And if you only take samples once per week, then it is going to be a very long time before you can reliably estimate who the top advertisers are on a channel.

Therefore you need to be systematic and consistent in your sampling. To start we recommend daily 15 minutes samples spread evenly between morning, afternoon, and evening. After a couple months you could decrease this to every other day. Eventually you will come to know what minutes ads are generally shown in a given hour to make you time use even more efficient.

### Decide on spreadsheet software: Online or local?
There are many options for what software can be used to collect data and how. Only two approaches will be described here, one illustrating a use case where a single individual is conducting all sampling. And a second illustrating a use case where multiple individuals are collaborating on sampling. 

#### **Local Excel for Individual-Only Data Collection** 
In this approach, you simply the edit the  data file in place in your working directory. Just add advertisers as you observe them. Use the sort feature to keep them in date order. And be sure to always save the file as a csv file (Comma Seperate Values).

#### **Online Google Sheets for Collaborative Data Collection**
In this approach, you can collaborate with others using an online file, such as a Google Sheet. Each collaborator can add advertisers as they are observed. Then a single point person can keep this file sorted, and can download into a local working directory as needed to run scripts (more on that later). In this collaborative approach care must be take to ensure that collaborators are being consistent with their company and product names. For example there is a danger of ending up with "Kraft Hienz", "Kraft Hienz Co.", "Kraft Hienz Company" etc., which should all have the same name. The point person must be vigilent about this. A larger number of less trained collaborators increases the risk that the data will lose integrity.

## 3. Start collecting samples and adding them to your spreadsheet
The template csv file has a header row that defines column names. This row must be preserved exactly, because the scripts rely on recognizing these column names. Therefore your data should begin in row 2. The columns names are CompanyName,ProductName, DateObserved, TimeOfDay, Channel, ShowName. The best way to understand the columns and their use is to look at the example FoxNews_ObservedAdvertisements.csv file. As noted above, consistency in naming is important, not just for companies, but also for products, times of day, shows etc. So consider it one of your main responsibilities as data curator to maintain this consistency.

Note that the content on partisan channels can be very toxic and triggering. It is thus a lot to ask of someone to watch it everyday. Additionally there may already be organizations that track and catalog the content of these channels (such as Media Matters in the United States). As such it is not neccessary to even watch with the sound on when you are just tracking advertisements. Please take care, and if you need a day off you can certainly take it without overly undermining the accuracy of the sampling.

## 4. Install a Python Anaconda environment and use a Jupyter Notebook to run scripts
Currently there is only one script for processing data, but it is a core script that calculates the recent top advertisers on the channel and creates a bar chart image. Note that this script requires at least 50 rows of data, so it cannot be used until you have done at least some sampling of advertisements.

To setup a Python environment on your computer, download and install Anaconda from the following URL. Remember to choose the installer for Python 3.x.  https://www.anaconda.com/products/individual#download-section

The script can run from a Jupyter Notebook, and this is then best option for non-coders. After installing Anaconda, on a Mac, Jupyter Notebook can be launched by opening the Terminal application and typing "jupyter notebook at the prompt. On Windows you can click on the Jupyter Notebook icon installed by Anaconda in the start menu. In both cases the notebook with open in a webbrowser tab. Navigate to find the Scripts folder in the working directory and open the file entitled generateTopAdvertisers.ipynb. Follow the guidance contained in this notebook to run the script. Note that the configuration the first time you do this may be time consuming. But once it is done the script can be run daily in a matters of seconds as part of your workflow.

## 5. Options for sharing your data
Once have successfuly completed the above, you should have a functioning system for collecting sample data on advertisements, and drawing conclusions and making visualizations based on that data. There are of course many options for sharing that data and may possible uses of the data. The spirit of this project is based on the notion of not just open source but even more essentially, the notion of open data. As such you might consider releasing your data as open data through a platform like GitHub or some of the many open data platforms available. 

Finally, if you do find use for this toolkit, please acknowledge the original project. And also if you build any useful addons please consider releasing those as open source, or contributing them to the original repository.

Any questions, please contact whoadvertiseson@protonmail.com