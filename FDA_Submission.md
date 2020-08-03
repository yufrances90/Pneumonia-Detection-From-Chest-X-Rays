# FDA  Submission

**Your Name:** Beijia(Frances Yu)

**Name of your Device:** Pneumonia Detection System

## Algorithm Description 

### 1. General Information

**Intended Use Statement:** For assisting the radiologists in the detection of pneumonia in chest radiography

**Indications for Use:** Screening chest radiography for people aging from 5-65 years old

**Device Limitations:**
* Results from the device does not take into account patients' medical history
* It is not for patients over 90 years old

**Clinical Impact of Performance:**
* It does not achieve fast performace in the absence of GPU

### 2. Algorithm Design and Function

<< Insert Algorithm Flowchart >>

**DICOM Checking Steps:**

**Preprocessing Steps:**

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

> Model 1 Training Performance
> ![alt text][model_1_training]

(Only selected P-R curves are shown. More on evaluation reports for both models)

> Model 2 P-R curve for [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
> ![alt text][model_2_pr]

**Final Threshold and Explanation:**

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:** 


**Description of Validation Dataset:** 

Three datasets are used to validate model 1, and among the datasets for validating model 1, two of them are used to validate model 2.

> For validating model 1
> * A subset of  ChestX-ray14 dataset is used. It contains a total of 1121 images(uniform distribution of pneumonia-positive and pneumonia-negative cases)
>
> For validating both model 1 and model 2
> * Dataset is organized into 3 folders(train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal). Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care. For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.
> Link: [https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
> ---
> * Dataset is organized into 2 folders (train, test) and both train and test contain 3 subfolders (COVID19, PNEUMONIA, NORMAL). DataSet contains total 6432 x-ray images and test data have 20% of total images.
> Link: [https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia](https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia)


### 5. Ground Truth

### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:**

**Ground Truth Acquisition Methodology:**

**Algorithm Performance Standard:**

[cnn_model]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/cnn1.png?raw=true "CNN Model"

[model_1_training]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_1_training.png?raw=true "Model 1 Training Performance"
[model_2_pr]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_2_pr.png?raw=true "Model 6 Training Performance"
