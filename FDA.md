# FDA  Submission

**Your Name:** Beijia(Frances) Yu

**Name of your Device:** Pneumonia Detector

## Algorithm Description 

### 1. General Information

**Intended Use Statement:** For assisting the radiologists in the detection of pneumonia in chest radiography

**Indications for Use:** Screening chest radiography for people aging from 5-65 years old

**Device Limitations:**
* Results from the device does not take into account patients' medical history
* It is not for patients over 90 years old
* It is not intented for patients with Atelectasis or Infiltration

**Clinical Impact of Performance:**
![alt text][cx_testing] 
* It does not achieve fast performace in the absence of GPU
* Most of the time, the device can detect if a patient has Pneumonia. However, it can classify healthy people as patients with Pneumonia

### 2. Algorithm Design and Function

![alt text][algorithm_flowchart] 

**DICOM Checking Steps:**
1. Checks if it is a .dcm file
2. Checks if all required fields are included in the header
3. Checks if the image type is DX
4. Checks if the image position is either AP or PA
5. Checks if body part examined is CHEST

**Preprocessing Steps:**
1. Converts color space from BGR to RGB
2. Normalizes image numpy array
3. Uses intensity threshold to separate the background of the image
3. Converts to tensor from numpy array 
4. Changes the size of the image to 224 * 224

**CNN Architecture:**

---
![alt text][cnn_model]
---

1. Uses existing VGG19 architecture with weights trained on ImageNet dataset but without any fully connected layers to extract features
2. Adds 4 dense layers for classifying images
3. Adds 4 dropout layers to avoid overfitting


### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training:
  * Rotation
  * Horizontal shift
  * Vertical shift
  * Shearing
  * Zoom
  * Horizontal flip
  * Normalization
  * Resize the images to 224 * 224
* Batch size: 64
* Optimizer learning rate: 0.001 (default learning rate of Adam)
* Layers of pre-existing architecture that were frozen: All but not fully connected layers
* Layers of pre-existing architecture that were fine-tuned: None
* Layers added to pre-existing architecture: 4 dense layers + 4 dropout

> Training Performance
> ![alt text][model_training]

> Classification Report for Testing Dataset
> ![alt text][classification_report_testing]

**Final Threshold and Explanation:**

When the threshold equals 0.2, recall gets over 80%, but F1-score reaches its highest when threshold equals 0.5.
The device can detect pneumonia most of the time, but it is less certain in confirming if a suspicious patient truly gets pneumonia.

### 4. Databases
 ![alt text][pneumonia_distribution]
 ![alt text][age_distribution]
 ![alt text][gender_distribution]

**Description of Training Dataset:** 
The entire training dataset is selected from random sample (5606 images) of NIH dataset. There are only 66 pneumonia-positive images, and the rest of the data is pneumonia-negative. To balance the dataset, the number of pneumonia-positive images must be the same as the pneumonia-negative ones. Up-sampling was done for the PNEUMONIA class by sampling with replacement. At the mean time, down-sampling was done for the NON PNEUMONIA class by sampling without replacement. The number of male patients is greater than the number of female patients. Patient ages forms a bell curve distribution. 
**Description of Validation Dataset:** 
The entire testing dataset is selected from all images that are not in the sample NIH dataset. The ratio between pneumonia-positive cases and pneumonia-negative cases is 1:4. Patient ages forms a bell curve distribution, and the number of male patients is greater than the number of female patients.

### 5. Ground Truth

Natural Language Processing is used to extract disease labels from the associated radiological reports. Because the number of these reports is huge, it is faster and less expensive using NLP. However, some disease labels may not be extracted correctly since the accuracy of using NLP labelling is estimated to be over 90%. Due to potential risks of wrong labelling, and as the device depends on these disease labels, the predictions made by the device may not be correct.


### 6. FDA Validation Plan

![alt text][thresh_vs_f1_score]

**Patient Population Description for FDA Validation Dataset:**
* Age ranges: 5 - 65
* Sex: 40% of Female & 60% of Male
* Type of imaging modality: Frontal radiographs
* Body part imaged: Chest
* Prevalence of disease of interest: 25%
* Any other diseases that should be excluded as comorbidities in the population: Atelectasis, Infiltration

**Ground Truth Acquisition Methodology:**
The diagnoses for the images should be graded by two expert physicians. In order to account for any grading errors, the dataset should be checked by a third expert who has more years of experience

**Algorithm Performance Standard:**
* F1 Score: 43.5% (95% CI 0.387, 0.481)
* AUROC: 0.7680

### References:
* [CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning](https://arxiv.org/pdf/1711.05225.pdf)

[algorithm_flowchart]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/versions/v1/assets/algorithm_flowchart.png?raw=true  "Algorithm Flowchart"

[cnn_model]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/versions/v1/assets/cnn1.png?raw=true "CNN Model"

[model_training]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/__results___8_0.png?raw=true "Model Training Performance"

[thresh_vs_f1_score]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/thresh_vs_f1score.png?raw=true "Threshold Vs. F1-score"

[cx_testing]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/confusion_matrix_testing.png?raw=true "Confusion Matrix for Testing Dataset"

[classification_report_testing]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/classification_report_testing.png?raw=true "Classification Report for Testing Dataset"

[pneumonia_distribution]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/pneumonia_distribution.png?raw=true "Distribution of Pneumonia-positive and Pneumonia-negative"
[age_distribution]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/age_distribution.png?raw=true "Distribution of Patient Age"
[gender_distribution]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/gender_distribution.png?raw=true "Distribution of Patient Gender"