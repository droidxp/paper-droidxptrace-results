### Replication Package

This is the replication package for the paper The Achilles’ Heel of the Android Mining Sandbox Approach for Malware Identification.

### Abstract

Android is the most popular operating system for the mobile platform, and smartphones’ ubiquitous nature in our daily lives has only made their security an important topic for researchers and practitioners alike. Repackaging Android apps is one of the most popular methods to inject malicious behavior into android apps, and previous research results have advocated using the Mining Android Sandbox Approach (MAS approach) to identify malicious behavior in repackaged apps. Nonetheless, these previous studies draw their conclusions using a small dataset of 102 pairs of original and repackaged apps, threatening the validity of the findings concerning external validity and opening the question of whether or not the MAS approach scales. To investigate these issues, we conduct a new experiment that replicates the methodology used in the state-of-the-art research that empirically evaluated the MAS approach performance on a dataset with an order of magnitude larger than the datasets used in previous research (our large dataset comprise 1203 pairs of apps with a much diverse distribution of malware families, for instance). To our surprise, our experiments revealed that the accuracy rate of the MAS approach for malware identification drops significantly: F-Score drops from 0.89 in the previous dataset to 0.42 in our large dataset. After an in-depth assessment, we find that the more significant number of malware from the gappusin family explains the higher number of samples for which the MAS approach fails to classify as malware correctly (false negative). Our findings open the discussion on the possible blindspots that plague the MAS approach and their accuracy issues when scaled.
