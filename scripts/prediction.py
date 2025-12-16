import os
from roboflow import Roboflow


# Initialize RoboFlow
rf = Roboflow(api_key="MwEVNza1ltsKzRCUCm4W")
workspace = rf.workspace("projects-horgn")
project = workspace.project("rock-clasfication-jqetv")
model = project.version(2).model


# Path to your test image folder
test_folder = r"C:\Users\kunal\Downloads\archive (3)\Dataset\All_Rocks"


# Loop through and predict
for file in os.listdir(test_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(test_folder, file)
        print(f"\nPredicting: {file}")
       
        # Get prediction
        prediction = model.predict(image_path).json()
       
        # Extract the top prediction only
        predictions_dict = prediction['predictions'][0]['predictions']
       
        # Find the class with highest confidence
        top_class = max(predictions_dict.items(), key=lambda x: x[1]['confidence'])
        class_name, class_data = top_class
        confidence = class_data['confidence']
       
        # Display only the top prediction
        print(f"Top Prediction: {class_name} ({confidence:.2%})")
        print(". " * 20)
        