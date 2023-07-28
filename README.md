# PCAP Classification using Image Representation

## Task Description

The goal of this project is to classify PCAP (Packet Capture) files from the [IIoT Priority Dataset](https://www.kaggle.com/datasets/bikashmazumdar/iiot-priority-dataset) into high and low priority. The dataset comprises pcap files generated using sensors in a simulated environment. These sensors include CO2, noise, vibration, and temperature/humidity sensors. The data was captured using the tcpdump utility, and the traffic in the pcap files is categorized into three priorities: high, medium, and low. For our classification task, we only consider the high and low priority categories.

## Repository Structure

The GitHub repository is organized into two main directories: `Data` and `Classification_Model`.

### Data Directory

The `Data` directory contains the script used to convert the pcap files into images. Due to their large size, all the pcap files could not be uploaded to the GitHub repository. However, you can download the required pcap files from the [Kaggle dataset](https://www.kaggle.com/datasets/bikashmazumdar/iiot-priority-dataset) if needed. The repository includes the uploaded pcap image representations generated from the pcap files.

### Classification Model Directory

The `Classification Model` directory contains the Jupyter notebook used to train the classification model. The model training was originally performed on Google Colab to take advantage of its enhanced training capabilities. The notebook outlines the process of fine-tuning the ResNet18 model using the timm library on our dataset. The image data csv's were removed from the Classification_Model directory.

## Model Performance

After training the classification model, we achieved good results, obtaining 1.0 accuracy and F1 score on the validation dataset. These perfect results demonstrate the efficacy of our approach to classify pcap files using their image representations. The image-based approach has proven to be highly accurate and efficient in distinguishing between high and low priority traffic in pcap files generated from sensor data in a simulated environment.

By leveraging image representation techniques and deep learning models, we have showcased a robust solution for PCAP classification. The trained model can be further extended and adapted for real-world applications in network traffic analysis, intrusion detection, and various other domains where prioritizing PCAP files is crucial.

Please note that this repository contains the necessary code and instructions to reproduce our results, and you can easily adapt it to your specific use cases.

For any queries or feedback, feel free to reach out.


