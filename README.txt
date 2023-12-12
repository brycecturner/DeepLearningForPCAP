# NOTE:

This was written as a markdown file for the github homepage but I am not able to upload .md files to the assignment text. Please see the github link to read the md version. 



# DeepLearningForPCAP
For my final project for my Deep Learning Class CSCI-E89 at the Harvard Extention School

# Report Abstract
I train a CNN classifier on packet-level data to distinguish between malicious DNS traffic from various Botnets and normal DNS traffic from computers running standard software applicaitons. I take advantage of an interesting dataset where researchers at the University of Victoria constructed a virtual cloud and then deployed many differnt botnets on VMs. The researchers then observed all traffic transmitting inside this environment, including the packet-level information. 

This interesting dataset solves two common problems in cybersecurity: We often do not have labeled data and we do not have "baseline" activity for a given system.  I beleive that if the data simulation where expanded, the framework developed here could be used to create a packet-sniffing application that would detect Botnets as soon as they begin executing on a system. 

This report focuses only on the DNS traffic, because often times Botnets will use DNS traffic to transmit Command and Control (C&C) communicatiosn with their central server. However, this report does not look at peer-to-peer botnets, because the data did not have the information to know which servers began infected, I only knew the IP addresses of the Central Server. 

The model I constructed was 1-dimensional Convolutional Neural Net (CNN), where I tuned the depth of the network and the kernel size.  I used a CNN because the the data was bytes in a packet, which is essentially unintelligable to human eyes. Therefore, I thought it would be better to let the CNN conduct the feature engineering.  Given that the data is read as a single 1-D stream, not 2D like an image would be, the CNNs had to be one dimentional.  After each CNN layer, I included a Max Pooling layer. In future work, I could change this Max Pooling to include a Drop Out layer as well. 

The results are very good, although I cannot figure out exactly why.  I have high accuracy (99%) on all test samples. 

# Important Links
- Short Video (5 Min): https://youtu.be/IFmV5LYNvmI
- Long Video (15 Min): https://youtu.be/k-6FbmIZvYg
- Github Project : https://github.com/brycecturner/DeepLearningForPCAP
- Google Colab Notebook: https://colab.research.google.com/drive/1eC2cxiwLtYlFknz2mi2c4aHhNQbPqELg#scrollTo=7ArbUTS22_PU
- Link to Full Data: https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/botnet-and-ransomware-detection-datasets/

# Longer Report
The longer report is written in the notebook "cnns_for_botnet_classification.ipynb"

# Data Source
The data for the project was downloaded from the University of Victoria's Website here
- https://onlineacademiccommunity.uvic.ca/isot/datasets/
Specifically, I downloaded the ISOT HTTP Notenet Dataset from here
- https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/botnet-and-ransomware-detection-datasets/

This dataset looks at all internet traffic, but for my work I focus only on the DNS traffic. 

# Data Description
https://onlineacademiccommunity.uvic.ca/isot/wp-content/uploads/sites/7295/2023/03/ISOT-HTTP-Botnet-Dataset.pdf
