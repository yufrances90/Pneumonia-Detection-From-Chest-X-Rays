# %% [code]
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import seaborn as sns

from keras_preprocessing.image import ImageDataGenerator
from sklearn.metrics import \
    classification_report, \
    confusion_matrix, \
    roc_auc_score, \
    average_precision_score, \
    precision_recall_curve, \
    roc_curve,\
    auc

def generate_file_path(dir_path, filename):
    return os.path.join(dir_path, filename)

def load_model(model_dir, model_file_path):
    
    model_file = generate_file_path(model_dir, model_file_path)
    
    model = tf.keras.models.load_model(
        model_file,
        custom_objects={
            'KerasLayer': hub.KerasLayer
        }
    )
    
    return model


def plot_roc_curve(t_y, p_y):
    
    fig, c_ax = plt.subplots(1,1, figsize = (9, 9))
    
    fpr, tpr, thresholds = roc_curve(t_y, p_y)
    
    c_ax.plot(fpr, tpr, label = '%s (AUC:%0.2f)'  % ('Pneumonia', auc(fpr, tpr)))
    
    c_ax.legend()
    
    c_ax.set_xlabel('False Positive Rate')
    c_ax.set_ylabel('True Positive Rate')
    
    
def plot_precision_recall_curve(t_y, p_y):
    
    fig, c_ax = plt.subplots(1,1, figsize = (9, 9))
    
    precision, recall, thresholds = precision_recall_curve(t_y, p_y)
    
    c_ax.plot(recall, precision, label = '%s (AP Score:%0.2f)'  % ('Pneumonia', average_precision_score(t_y,p_y)))
    
    c_ax.legend()
    
    c_ax.set_xlabel('Recall')
    c_ax.set_ylabel('Precision')
    
def create_test_data_generator_from_directory(
    image_dir, 
    classes,
    image_size=(224, 224), 
    color_mode='rgb', 
    batch_size=32, 
    class_mode='binary',
    shuffle=False,
    seed=None,
    datagen=None):
    
    datagen = ImageDataGenerator(rescale=1./255.)
    
    return datagen.flow_from_directory(
        directory=image_dir,
        target_size=image_size,
        color_mode=color_mode,
        batch_size=batch_size,
        class_mode=class_mode,
        shuffle=shuffle,
        seed=seed,
        classes=classes
    )
    

def generate_datasets(
    data_dir, 
    train_dir_name, 
    test_dir_name, 
    classes,
    valid_dir_name=None
):
    
    test_dir = generate_file_path(data_dir, test_dir_name)
    train_dir = generate_file_path(data_dir, train_dir_name)
    
    test_generator = create_test_data_generator_from_directory(
        image_dir=test_dir,
        classes=classes,
        seed=42
    )
    
    train_generator = create_test_data_generator_from_directory(
        image_dir=train_dir,
        classes=classes,
        seed=42
    )
    
    valid_generator = None
    
    if valid_dir_name:
        
        valid_dir = os.path.join(data_dir, valid_dir_name)
        
        valid_generator = create_test_data_generator_from_directory(
            image_dir=valid_dir,
            classes=classes,
            seed=42
        )
        
    return (train_generator, valid_generator, test_generator)


def evaludate_model_n_print_loss_n_acc(model, data_generator):
    
    loss, accuracy = model.evaluate(data_generator)

    print('\nLoss: {:,.3f}'.format(loss))
    print('Accuracy: {:.3%}'.format(accuracy))
    

def get_predictions(model, data_generator):
    
    Y_pred = model.predict(data_generator, verbose=1)
    
    return Y_pred


def draw_confusion_matrix_by_data_generator_n_predictions(
    data_generator,
    predictions,
    classes,
    cmap='Blues'
):
    
    cf_matrix = confusion_matrix(data_generator.classes, predictions)

    group_names = ['TN', 'FP', 'FN', 'TP']

    group_counts = ['{0:0.0f}'.format(value) for value in
                    cf_matrix.flatten()]
    
    labels = [f'{v1}\n{v2}' for v1, v2 in
              zip(group_names, group_counts)]

    labels = np.asarray(labels).reshape(2,2)

    sns.heatmap(
        cf_matrix, 
        annot=labels,
        xticklabels=classes,
        yticklabels=classes,
        fmt='',
        cmap=cmap
    )
    
    plt.show()
    
def generate_classification_report(
    data_generator,
    predictions,
    classes, 
    title='Classification Report'
):

    print(title)
    
    print(classification_report(data_generator.classes, predictions, target_names=classes))