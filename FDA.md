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
* It does not achieve fast performace in the absence of GPU

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

<< Insert P-R curve >>

**Final Threshold and Explanation:**

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:** 


**Description of Validation Dataset:** 


### 5. Ground Truth



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