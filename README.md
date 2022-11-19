## Replication Package

This is the replication package for the paper: The Achilles’ Heel of the Android Mining Sandbox Approach for Malware Identification.

### Abstract

Android is the most popular operating system for the mobile platform, and smartphones’ ubiquitous nature in our daily lives has only made their security an important topic for researchers and practitioners alike. Previous research results have advocated using the Mining Android Sandbox Approach (MAS approach) to identify malicious behavior in repackaged apps, one of the most popular methods to inject malicious behavior into android apps. Nonetheless, these previous studies have drawn their conclusions using a small dataset of 102 pairs of original and repackaged apps, threatening the findings w.r.t. external validity and opening the question of whether or not the MAS approach scales to larger and more diverse datasets. To mitigate these issues, we conduct a new experiment that reproduces the state-of-the-art research that empirically evaluated the MAS approach performance. Our reproduction study uses a dataset that is an order of magnitude larger than the datasets used in previous research (a total of 1203 pairs of apps with a much diverse distribution of malware families, for instance). To our surprise, our experiments revealed that the accuracy rate of the MAS approach for malware identification drops significantly: F1 score drops from 0.89 in the previous dataset to 0.42 in our larger dataset. After an in-depth assessment, we found that the
representative number of malware from the gappusin family explains the higher number of samples for which the MAS approach fails to correctly classify as malware. Our findings open the discussion on the possible blindspots that plague the MAS approach and their accuracy issues when scaled and reveal the need for complementing the MAS approach with other techniques so that it could effectively detect a broader class of malware.

### Malware Dataset

We use a curated dataset of 1203 repackaged apps available in the AndroZoo (https://androzoo.uni.lu/repackaging) repository, and arrange the samples on the following CSV [file](../paper-droidxptrace-results-F55A/appsHash.csv). At this file, the colunms are: app version (original/repackaged), app description and app hash. The original dataset from previous research works is a subset of preview dataset and has 102 repackaged apps, which we separate and available at follow CSV [file](../paper-droidxptrace-results-F55A/originalMalwareSample.csv).

We queried the VirusTotal repository (https://www.virustotal.com/gui/home/upload) to find out which repackaged apps in our dataset have been indeed labeled as a malware, and if positive, find which malware family the sample came from. To collect this information, we use avclass2 tool (https://github.com/malicialab/avclass). The first step for that is create a hash [list](../paper-droidxptrace-results-F55A/listRepackageHash.csv) of all repackage app hash which we would like to check at VirusTotal. With this list we use a python [script](../paper-droidxptrace-results-F55A/urltoFile.py) to download all Json files from VirusTotal, which we use at avclass2 tool to get information about repackage family. After this procedure we get the follow [dataset](../paper-droidxptrace-results-F55A/avclass.csv). At this dataset, if the sample was flagged by more than 1 AV engines, the column 'family' contains only the family name, if the sample was flagged by just 1 AV engine, the column contains SINGLETON:APP Hash, otherwise the column contains undetected.

We also characterize our dataset according to the similarity between the original and repackage app version, using SimiDroid tool (https://github.com/lilicoding/SimiDroid). As a first step, we use SimiDroid tool to get Json files containing information about methods identical, similar, new, deleted and similarity Score from our [sample](../paper-droidxptrace-results-F55A/listapps.csv), using a pyhton [script](../paper-droidxptrace-results-F55A/getJsonFilefromSimiDroid.py). As a final result, we have this CSV [file](../paper-droidxptrace-results-F55A/summarySimiDroid.csv) with information about differences between app pairs (original/repackage), and similarity score from our sample.

### Data Collection

We take advantage of the [DroidXP](https://github.com/droidxp/benchmark) infrastructure for data collection. With DroidXP we collect all relevant information, such as calls to sensitive APIs, during the test execution performanced by test generator tool Droidbot. We execute DroidXP using Droidbot for 180 seconds, and repet all process 3 times for each app pair (original/repackage). The final result from this exploratory step is compiled at this [zip](../paper-droidxptrace-results-F55A/180_preview_work.zip) file. Because of space issue at repository, this zip file has just the apps explored at original work (102 app samples). 

After the exploratore step, we produces a [dataset](../paper-droidxptrace-results-F55A/methods_explored/output/methodsExplored.zip) with the sensitive methods filter from this [list](../paper-droidxptrace-results-F55A/methods_explored/scripts/sensitive_methods.txt), that both app versions call during their 3 executions. To create this dataset, we take advantage of 2 pyhton scripts present at our repository. Before execute both scripts, we unzip the result folder from emploratory step inside methods_explored folder, present at our repository and execute [run.sh](../paper-droidxptrace-results-F55A/methods_explored/run.sh) command to call both scripts. The [first](../paper-droidxptrace-results-F55A/methods_explored/scripts/generate_union_of_executions.py) python script will generate the union of all sensitive APIs explored from all executions, and the [second](../paper-droidxptrace-results-F55A/methods_explored/scripts/compute_diff_between_benign_and_malign.py) will compute the diff between sensitive APIs called at both versions (original/repackage). This procedure also will generate 2 final CSVs file. The [first](../paper-droidxptrace-results-F55A/methods_explored/output/diffs/summary.csv) is the summary of occurs of differents sensitive methods at both app versions, and the [second](../paper-droidxptrace-results-F55A/methods_explored/output/diffs/methods_in_diff.csv) CSV file presents how many times each sensitive method, was inserted when analyzing the whole sample.

To collect information about trace execution, we extended DroidXP with a new component (DroidXP-Trace), which allows us to investigate dynamic call graphs from the outcomes of a DroidXP execution. Using the logcat files collected from DroidXP execution at both app versions, DroidXP-Trace generate a Json file containing information about traces from entry point to sensitive methods call at both version, and if there are Different traces between them. We collect this information and create 3 Json files [Json_Ex1](../paper-droidxptrace-results-F55A/trace_explored/outputDroidbot_trace_1203_repetition_01_part01.json)[Json_Ex2](../paper-droidxptrace-results-F55A/trace_explored/outputDroidbot_trace_1203_repetition_02_part01.json)[Json_Ex3](../paper-droidxptrace-results-F55A/trace_explored/outputDroidbot_trace_1203_repetition_03_part01.json) referent of each execution. With these Json files we generate the final CSV [file] (../paper-droidxptrace-results-F55A/trace_explored/Summary_trace_1203.csv) with all app pairs and information about different traces from entry point to sensitive method call.

