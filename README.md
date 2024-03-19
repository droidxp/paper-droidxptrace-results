## Replication Package


This is the replication package for the paper: The Achilles' Heel of the Android Mining Sandbox Approach.

### Abstract


The widespread use of smartphones in our daily lives has elevated concerns regarding their security among researchers and practitioners. Particularly, security issues are highly prevalent in Android, the most popular mobile operating system. Previous research has explored various techniques to address these concerns, including the Mining Android Sandbox approach (MAS approach), which aims to identify malicious behavior in repackaged Android applications (apps). However, earlier studies have been limited by small datasets, typically consisting of only 102 pairs of original and repackaged apps. This limitation raises questions about the external validity of their findings and whether the MAS approach is scalable to larger datasets. To address these concerns, this paper presents the results of an experiment that replicates state-of-the-art research on evaluating the accuracy of the MAS approach. Unlike previous studies, our research employs a dataset that is an order of magnitude larger, comprising 4,076 pairs of apps covering a more diverse range of Android malware families. Surprisingly, our findings indicate a significant drop in the accuracy of the MAS approach for identifying malware, with the F1-score decreasing from 0.89 in previous studies to 0.59 in our larger dataset. Upon closer examination, we discovered that the higher representation of malware from the gappusin family partially accounts for the increased number of instances where the MAS approach fails to correctly classify a repackaged app as malware. Additionally, we investigated the impact of two extensions—–Trace Analysis and Parameter Analysis—implemented from the literature to enhance the MAS approach. However, these extensions only marginally improved the approach’s performance, with both extensions combined increasing accuracy by 6% (from 59% to 65%)—–still falling short of the accuracy reported in previous studies. Our findings highlight the limitations of the MAS approach, particularly when scaled, and underscore the importance of complementing it with other techniques to effectively detect a broader range of malware. This opens avenues for further discussion on addressing the blind spots that affect the accuracy of the MAS approach.

### Malware Dataset

We use a curated dataset of 4,076 repackaged apps based on two repositories, RePack (https://github.com/serval-snt-uni-lu/RepackageRepo.git) and AndroMalPack (https://github.com/hasnainrafique/AndroMalPack-Dataset). Both were curated using automatic procedures that extract repackaged apps from the [Androzoo repository] (https://androzoo.uni.lu/gp-metadata), and arrange the samples on the following CSV [file](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/appsHash.csv). In this file, the columns are: First - original app hash, Second - repackage app repackaged. The original dataset from previous research works has 102 repackaged apps, which we also separate and available in the following CSV [file](https://github.com/droidxp/paper-droidxptrace-results/blob/main/originalMalwareSample.csv). To download both dataset we used this python [script](https://github.com/droidxp/paper-droidxptrace-results/blob/main/getApps.py)

We queried the VirusTotal repository (https://www.virustotal.com/gui/home/upload) to find out which repackaged apps in our dataset have been indeed labeled as malware, and if positive, find which malware family the sample came from. To collect this information, we use avclass2 tool (https://github.com/malicialab/avclass). The first step for that is to create a hash [list](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/listRepackagedHash.csv) of all repackage app hash which we would like to check at VirusTotal. With this list, we use a python [script](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/urltoFile.py) to download all Json files from VirusTotal, which we use at avclass2 tool to get information about repackage family. After this procedure, we get the following [dataset](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/avClassResultRepackaged.csv). In this dataset, if the sample was flagged by more than 1 AV engine, the column 'family' contains only the family name, if the sample was flagged by just 1 or 0 AV engine, the column contains 'None'.

We also characterize our dataset according to the similarity between the original and repackage app versions, using SimiDroid tool (https://github.com/lilicoding/SimiDroid). As a first step, we use SimiDroid tool to get Json files containing information about methods identical, similar, new, deleted, and similarity Score from our sample. As a final result, we have this CSV [file](https://github.com/droidxp/paper-droidxptrace-results/blob/main/summarySimiDroid.csv) with information about differences between app pairs (original/repackage), and similarity score from our samples.

### Data Collection


We take advantage of the [DroidXP](https://github.com/droidxp/benchmark) infrastructure for data collection. With DroidXP we collect all relevant information, such as calls to sensitive APIs, during the test execution performed by the test generator tool Droidbot. We execute DroidXP using Droidbot for 180 seconds, and repeat all processes 3 times for each app pair (original/repackage). The final result from this exploratory step is compiled in this [zip](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/180_preview_work.zip) file. Because of space issues at the repository, this zip file has just the apps explored in the original work (102 app samples).

After the exploratory step, we produce a [dataset](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/output/methods_explored.zip) with the sensitive methods filter from this [list](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/scripts/sensitive_methods.txt), that both app versions call during their 3 executions. To create this dataset, we take advantage of 2 pyhton scripts present in our repository. Before executing both scripts, we unzip the result folder from the exploratory step inside methods_explored folder, present at our repository, and execute [run.sh](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/run.sh) command to call both scripts. The [first](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/scripts/generate_union_of_executions.py) python script will generate the union of all sensitive APIs explored from all executions, and the [second](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/scripts/compute_diff_between_benign_and_malign.py) will compute the diff between sensitive APIs called at both versions (original/repackage). This procedure also will generate 2 final CSVs file. The [first](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/output/diffs/summary.csv) is the summary of occurs of different sensitive methods at both app versions, and the [second](https://github.com/droidxp/paper-droidxptrace-results/blob/main/methods_explored/output/diffs/methods_in_diff.csv) CSV file presents how many times each sensitive method, was inserted when analyzing the whole sample.

To merge all results into just one dataset and facilitate analysis, we generate a [partial](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/sample_final_ds_before_VT_check.csv) dataset (4,806 samples) taking advantage of a R [script](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/merge-datasets.Rmd) file. We get the final dataset (4,076 samples) when apply a filter at [partial](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/sample_final_ds_before_VT_check.csv) dataset, recovering just the benign original app (benign=True). The original dataset from previous research which we replicated is available at the CSV [file](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/samples_previewStudy_dataSet.csv). We have also available a CSV [file](https://github.com/droidxp/paper-droidxptrace-results/blob/main/TSE/final_dataset_TSE.csv) that present the impact of all 116 malware families on the performance of Mining Android Sandbox approach (MAS) approach.
