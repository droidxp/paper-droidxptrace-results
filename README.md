## Replication Package

This is the replication package for the paper: The Achilles’ Heel of the Android Mining Sandbox Approach for Malware Identification.

### Abstract

Android is the most popular operating system for the mobile platform, and smartphones’ ubiquitous nature in our daily lives has only made their security an important topic for researchers and practitioners alike. Previous research results have advocated using the Mining Android Sandbox Approach (MAS approach) to identify malicious behavior in repackaged apps, one of the most popular methods to inject malicious behavior into android apps. Nonetheless, these previous studies have drawn their conclusions using a small dataset of 102 pairs of original and repackaged apps, threatening the findings w.r.t. external validity and opening the question of whether or not the MAS approach scales to larger and more diverse datasets. To mitigate these issues, we conduct a new experiment that reproduces the state-of-the-art research that empirically evaluated the MAS approach performance. Our reproduction study uses a dataset that is an order of magnitude larger than the datasets used in previous research (a total of 1203 pairs of apps with a much diverse distribution of malware families, for instance). To our surprise, our experiments revealed that the accuracy rate of the MAS approach for malware identification drops significantly: F1 score drops from 0.89 in the previous dataset to 0.42 in our larger dataset. After an in-depth assessment, we found that the
representative number of malware from the gappusin family explains the higher number of samples for which the MAS approach fails to correctly classify as malware. Our findings open the discussion on the possible blindspots that plague the MAS approach and their accuracy issues when scaled and reveal the need for complementing the MAS approach with other techniques so that it could effectively detect a broader class of malware.

### Malware Dataset

We use a curated dataset of 1203 repackaged apps available in the AndroZoo (https://androzoo.uni.lu/repackaging) repository, and arrange the samples on the following CSV [file](../paper-droidxptrace-results-F55A/appsHash.csv). At this file, the colunms are: app version (original/repackaged), app description and app hash. The original dataset from previous research works is a subset of preview dataset and has 102 repackaged apps, which we separate and available at follow CSV [file](../paper-droidxptrace-results-F55A/originalMalwareSample.csv).

We queried the VirusTotal repository (https://www.virustotal.com/gui/home/upload) to find out which repackaged apps in our dataset have been indeed labeled as a malware, and if positive, find which malware family the sample came from. To collect this information, we use avclass2 tool (https://github.com/malicialab/avclass). The first step for that is create a hash [list](../paper-droidxptrace-results-F55A/listRepackageHash.csv) of all repackage app hash which we would like to check at VirusTotal. With this list we use a python [script](../paper-droidxptrace-results-F55A/urltoFile.py) to download all json files from VirusTotal, which we use at avclass2 tool to get information about repackage family. After this procedure we get the follow [dataset](../paper-droidxptrace-results-F55A/avclass.csv). At this dataset, if the sample was flagged by more than 1 AV engines, the column 'family' contains only the family name, if the sample was flagged by just 1 AV engine, the column contains SINGLETON:APP Hash, otherwise the column contains undetected.

We also characterize our dataset according to the similarity between the original and repackage app version, using SimiDroid tool (https://github.com/lilicoding/SimiDroid). As a first step, we use SimiDroid tool to get Json files containing information about methods identical, similar, new, deleted and similarity Score from our [sample](../paper-droidxptrace-results-F55A/listapps.csv), using a pyhton [script](../paper-droidxptrace-results-F55A/getJsonFilefromSimiDroid.py). As a final result, we have this CSV [file](../paper-droidxptrace-results-F55A/summarySimiDroid.csv) with information about differences between pair apps (original/repackage), and similarity score from our sample.

### Data Collection

We take advantage of the [DroidXP](https://github.com/droidxp/benchmark) infrastructure for data collection. With DroidXP we collect all relevant information, such as calls to sensitive APIs, during the test execution performanced by test generator tool Droidbot. We execute DroidXP using Droidbot for 180 seconds, and repeted all process 3 times for each app pair (original/repackage). The final result from this exploratory step is compiled at this [zip] file.

