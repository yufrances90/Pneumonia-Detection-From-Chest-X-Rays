# FDA  Submission

**Your Name:**

**Name of your Device:**

## Algorithm Description 

### 1. General Information

**Intended Use Statement:** 

**Indications for Use:**

**Device Limitations:**

**Clinical Impact of Performance:**

### 2. Algorithm Design and Function

<< Insert Algorithm Flowchart >>

**DICOM Checking Steps:**

**Preprocessing Steps:**

**CNN Architecture:**


### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training
* Batch size
* Optimizer learning rate
* Layers of pre-existing architecture that were frozen
* Layers of pre-existing architecture that were fine-tuned
* Layers added to pre-existing architecture


> Model 6 Training Performance
> ![alt text][model_6_training]

> Model 7 Training Performance
> ![alt text][model_7_training]

<< Insert P-R curve >>

**Final Threshold and Explanation:**

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:** 

**Description of Validation Dataset:** 

In the ChestX-ray14 dataset, there are 1431 images labeled with Pneumonia. However, in the sample, there are only 66 images. I used all of 1431 images for training model 6. Therefore, I used other datasets to validate my device.

In order to validate my device, I used two datasets from Kaggle. 

> Dataset is organized into 3 folders(train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).
> Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.
> For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.
> Link: [https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

---
---

> Dataset is organized into 2 folders (train, test) and both train and test contain 3 subfolders (COVID19, PNEUMONIA, NORMAL). DataSet contains total 6432 x-ray images and test data have 20% of total images.
> Link: [https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia](https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia)

### 5. Ground Truth

### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:**

**Ground Truth Acquisition Methodology:**

**Algorithm Performance Standard:**



[model_6_training]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_6_training.png?raw=true "Model 6 Training Performance"
[model_7_training]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_7_training.png?raw=true "Model 6 Training Performance"