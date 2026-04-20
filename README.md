#  Sugarcane Leaf Disease Detection using CNN

This project implements an AI-based system for detecting sugarcane leaf diseases using deep learning and image processing techniques. It is inspired by a research approach combining CNNs, data augmentation, and feature extraction.

---

## Features

* CNN-based disease classification
* Data augmentation for better generalization
* Evaluation using Precision, Recall, and F1-score
* Confusion Matrix visualization
* Training & validation accuracy/loss plots
* Modular and scalable code structure

---

## Dataset Structure

Organize your dataset like this:

```
dataset/
  train/
    healthy/
    rust/
    red_rot/
    yellow/
  val/
    healthy/
    rust/
    red_rot/
    yellow/
```

Each folder should contain corresponding images.

---

## Model Architecture

* Convolutional Neural Network (CNN)
* 3 Convolution layers + MaxPooling
* Fully connected Dense layers
* Dropout for overfitting prevention
* Softmax output layer for classification

---

## Results

* Training Accuracy: ~99%
* Validation Accuracy: ~93%
* Balanced Precision, Recall, and F1-score across classes

---

## ▶Run Training

```
python src/train.py
```

---

## Outputs

After training, the model generates:

* Accuracy vs Validation Accuracy graph
* Loss vs Validation Loss graph
* Confusion Matrix
* Classification Report (Precision, Recall, F1-score)
* Saved trained model (`.h5`)

---

## Project Structure

```
sugarcane-disease-detection/
│
├── dataset/
├── notebooks/
│   └── sugarcane_disease_detection.ipynb
├── src/
│   ├── train.py
│   ├── evaluate.py
│   ├── model.py
├── outputs/
│   ├── models/
│   ├── plots/
│   └── reports/
├── requirements.txt
├── README.md
├── .gitignore
├── config.yaml

---

##  Future Improvements

* Use advanced architectures like ResNet or EfficientNet
* Add spectral imaging support
* Deploy using Streamlit or Flask
* Optimize for mobile deployment

---

## Author

Vanshika Garg

----