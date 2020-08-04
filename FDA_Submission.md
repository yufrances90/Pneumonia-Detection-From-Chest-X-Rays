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

* Does not adjust threshold because resampling is done instead.
* From the evaluation report for model 2, precision achieves 82% and recall achieves 89% for both datasets for validation. It means the device can detect 89% of real pneumonia cases, and about 82% of the positive predictions by the model is correct

### 4. Databases


**Description of Training Dataset:** 

The NIH Chest X-ray dataset contains over 100,000 X-ray images with disease labels from 30,805 unique patients. The disease labels were created using NLP to mime the associated radiological reports. The labels include Atelectasis, Consolidation, Infiltration, Pneumothorax, Edema, Emphysema, Fibrosis, Effusion, Pneumonia, Pleural thickening, Cardiomegaly, Nodule, Mass, Hernia.

![alt text][model_1_distribution]

At the beginning, the device is trained using random sample (5%, 5606 images) of the full NIH dataset. Because there are only 66 pneumonia-positive images in the sample dataset, resampling was done to solve the data imbalance problem - randomly duplicating images from the Pneumonia class and randomly removing images from the Normal class. Finally, up-sampled pneumonia-positive images and down-sampled pneumonia-negative images are combined to train my device - model 1.

![alt text][model_2_distribution]

The predictions made by model 1 does not seem that bad, but the training set contains too many duplications of the pneumonia-positive images as a result of resampling. Due to the concern of too many duplications, I am thinking about constructing a new dataset to feed into the same network. All pneumonia-positive images (1431 images) from the full NIH Chest X-ray are used. For Normal class, all images (1431 images) are randomly selected from the sample NIH dataset - no duplicated images is used to train model 2.


**Description of Validation Dataset:** 

Three datasets are used to validate model 1, and among the datasets for validating model 1, two of them are used to validate model 2.

> For validating model 1
> * A subset of  NIH Chest X-ray dataset is used. It contains a total of 1121 images(uniform distribution of pneumonia-positive and pneumonia-negative cases)
>
> For validating both model 1 and model 2
> * Dataset is organized into 3 folders(train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal). Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care. For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.
> Link: [https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
> ---
> * Dataset is organized into 2 folders (train, test) and both train and test contain 3 subfolders (COVID19, PNEUMONIA, NORMAL). DataSet contains total 6432 x-ray images and test data have 20% of total images.
> Link: [https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia](https://www.kaggle.com/prashant268/chest-xray-covid19-pneumonia)


### 5. Ground Truth

Natural Language Processing is used to extract disease labels from the associated radiological reports. Because the number of these reports is huge, it is faster and less expensive using NLP. However, some disease labels may not be extracted correctly since the accuracy of using NLP labelling is estimated to be over 90%. 

### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:**

* Age ranges: 5 - 65
* Sex: 40% of Female & 60% of Male
* Type of imaging modality: Frontal radiographs
* Body part imaged: Chest
* Prevalence of disease of interest: 50%
* Any other diseases that should be included or excluded as comorbidities in the population: Pneumonia without any comorbidities

**Ground Truth Acquisition Methodology:**
The diagnoses for the images should be graded by two expert physicians. In order to account for any grading errors, the dataset should be checked by a third expert who has more years of experience

**Algorithm Performance Standard:**
* F1 Score: 43.5% (95% CI 0.387, 0.481)
* AUROC: 0.7680

### References:
* [CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning](https://arxiv.org/pdf/1711.05225.pdf)


[cnn_model]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/cnn1.png?raw=true "CNN Model"

[model_1_training]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_1_training.png?raw=true "Model 1 Training Performance"
[model_2_pr]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_2_pr.png?raw=true "Model 6 Training Performance"
[model_1_distribution]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_1_distribution.png?raw=true "Model 1 Pneumonia Distribution"
[model_2_distribution]: https://github.com/yufrances90/Pneumonia-Detection-From-Chest-X-Rays/blob/master/assets/model_2_distribution.png?raw=true "Model 2 Pneumonia Distribution"