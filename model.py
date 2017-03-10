
# this file assumes that there is a 'data' directory that has a 'driving_log.csv' file
# and 'IMG' directory with images in it



# import libraries
import csv
import cv2
import numpy as np

lines = []

# read the data file 
with open('./data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

images = []
measurements = []
# retrieve images and measurements using the data file
for line in lines[1:]:
    measurement = float(line[3])
    #ignore the data that has steering angle less than 0.01
    if measurement >= 0.01:
        for i in range(3):
            source_path = line[i]
            filename = source_path.split('/')[-1]
            currentpath = './data/IMG/' + filename
            image = cv2.imread(currentpath)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images.append(image)
            #add correction factor for images from left camera
            if i == 1:
                measurement = measurement + 0.2
            #add correction factor for images from right camera
            if i == 2:
                measurement = measurement - 0.2
            measurements.append(measurement)
            #flip the images and adjust the steering angle accordingly
            images.append(cv2.flip(image, 1))
            measurements.append(measurement*-1.0)

# convert to numpy array for use with keras
images = np.array(images)
measurements = np.array(measurements)

# import libraries relevant to keras
from keras.models import Sequential

from keras.layers import Flatten, Dense, core, Cropping2D
from keras.layers.core import Lambda, Activation
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

model = Sequential()

#normalize and mean center the data
model.add(core.Lambda(lambda x: x/255.0 - 0.5, input_shape=(160,320,3)))
#crop the part of the image that is relevant to prediction
model.add(Cropping2D(cropping=((70,25),(0,0))))

#NVIDIA architecture
model.add(Convolution2D(24, 5, 5, subsample=(2,2), activation="relu"))
model.add(Convolution2D(36, 5, 5, subsample=(2,2), activation="relu"))
model.add(Convolution2D(48, 5, 5, subsample=(2,2), activation="relu"))
model.add(Convolution2D(64, 3, 3, activation="relu"))
model.add(Convolution2D(64, 3, 3, activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))


#loss function = mean squared error
#optimizer = adam optimizer
model.compile(loss='mse', optimizer='adam')

#Shuffle the data
#Split 20% data for validation
model.fit(images, measurements, validation_split=0.2, shuffle=True, nb_epoch=5)


#save the model
model.save('model.h5')



