#**Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


//]: # (Image References)

[image1]: ./examples/right_recovery_1.jpg "Training Data"
[image2]: ./examples/right_recovery_2.jpg "Training Data"
[image3]: ./examples/right_recovery_3.jpg "Training Data"
[image4]: ./examples/left_recovery_1.jpg "Training Data"
[image5]: ./examples/left_recovery_2.jpg "Training Data"
[image6]: ./examples/left_recovery_3.jpg "Training Data"
[image7]: ./examples/bridge_recovery_1.jpg "Training Data"
[image8]: ./examples/bridge_recovery_2.jpg "Training Data"
[image9]: ./examples/bridge_recovery_3.jpg "Training Data"
[image10]: ./examples/architecture.png "Model Architecture"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
###Files Submitted & Code Quality

####1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* README.md summarizing the results
* run1.mp4 video showing the output on simulator

####2. Submission includes functional code
Using the Udacity provided simulator and drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

####3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

###Model Architecture and Training Strategy

####1. Model Architecture

The model is based out of the NVIDIA architecture. However, before the data is fed to the NVIDIA model, the following pre processing is done -
Normalizing the data (model.py line 60)
Mean Center the data
Crop the image to make the model learn from relevant data (model.py line 62)

The arrangement of convolution layers and fully connected layers perform well and do a good job of extracting the features and predicting the steering angle.

Please find the architecture summary below created using Keras.

![alt text][image10]


####2. Attempts to reduce overfitting in the model

While reading the data from the file to be fed into the network, the images were flipped (model.py line 42)
and the steering angle was adjusted accordingly to make the data more comprehensive. Also, the images from 
left camera and right camera were used and the steering angle was adjusted with a correction factor. (model.py lines 27-40)

The data was also split into training set and validation set. (model.py line 83)

The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 79).

####4. Appropriate training data

Data was collected using the simulator, however large steering angle was being recorded as the input was not coming form a joystick.
So, that led to the car going off the road while tesing on simulator. Ultimately, the data provided in the project resources was 
used and parameters tuned to keep the vehicle on track.

###Model Architecture and Training Strategy

####1. Solution Design Approach


The overall strategy for deriving a model architecture was to try out different standard architectures such as LeNET, NVIDIA architecture etc

My first step was to preprocess the data by normalizing, mean centering and cropping the data. Also, after initial training, I realized that
the vehicle had a tendency to turn towards left all the time and therefore the images in training data were flipped to ensure that the model was 
learning from a comprehensive data set.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set.

I started off by using a minimum architecture of convolution layer, relu activation, dropout layer etc. The model did not perform well.
Then I tested standard architecture such as LeNET and it performed fairly well, however it would still fail at few curves and at the bridge of track 1.

Then I tested the nvidia architecture and it performed better and kept the vehicle on the track during the entire lap.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

####2. Final Model Architecture

The final model architecture (model.py lines 64-74) is NVIDIA's architecture along with preprocessing of data as mentioned above.

####3. Creation of the Training Set & Training Process

Data was collected using the simulator, however large steering angle was being recorded as the input was not coming form a joystick.
So, that led to the car going off the road while testing on simulato. And I focussed on collecting the data for regions where the model would fail in the simulator.

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to save itself from going off the track. 

The following images depict the recovery from the right side of the track

![alt text][image1]
![alt text][image2]
![alt text][image3]

The following images depict the recovery from the left side of the track

![alt text][image4]
![alt text][image5]
![alt text][image6]

The following images depict the recovery of vehicle while on bridge

![alt text][image7]
![alt text][image8]
![alt text][image9]

I finally randomly shuffled the data set and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 5. I used an adam optimizer so that manually training the learning rate wasn't necessary.
