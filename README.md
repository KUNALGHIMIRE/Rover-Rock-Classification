**1.Project Title & Description:**

This project classifies rocks (Granite, Basalt, Sandstone,Marble,Quartzite,Limestone,Coal) using images captured by a rover along with detecting the environmental condition like pressure,temperature,uvdetection,rainfall detection,altitude through various sensors.

The model is trained using Roboflow and can be used for real-time prediction.

**2.Dataset Information:**

- The dataset used for this project is a publicly available rock classification dataset from Kaggle:
  [Rock Classification Dataset](https://www.kaggle.com/datasets/salmaneunus/rock-classification)
- **Classes**: Granite, Basalt, Sandstone, Marble, Quartzite, Limestone, Coal
- **Images per class**: 200–500
- Used for **training and testing** the Roboflow model

The process used before training as follows:
- Images were resized to 224x224 pixels
- Data augmentation applied: rotation, flipping, brightness adjustment etc.

**3.Trained Model Info / Roboflow Link:**
- Trained using Roboflow Custom Model
- Version: 3
- Accuracy: 96.2%
View trained model on Roboflow:[Click Here](https://app.roboflow.com/projects-horgn/rock-clasfication-jqetv)

**5.Libaries/Requirements:**
- roboflow
- opencv-python
- numpy
- Pillow




