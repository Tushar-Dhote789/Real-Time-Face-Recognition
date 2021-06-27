# Real-Time-Face-Recognition
Face recognition is a method of identifying or varifying the identity of an individual using their face. Face recognition systems can be used to identify people in photos, video, or in real time.

# Uses                                                                                                            
Preventing crime                                                                                 
Unlock device                                                                                   
Blind assistance                                                                                 
Attendance system                                                                               
Payments

# Algorithms

Haar Cascade classifier- Used to detect human face.

![Frontal face algorithm](https://user-images.githubusercontent.com/68141523/123548191-64fd3180-d781-11eb-98d5-87d65898ebad.png)


Fisherface Recogniser Algorithm- Fisherfaces algorithm extracts principle components that separates one individual from another. So, now an individual's feature can't dominate another person's features.
 
 
 LBPHFace Recognizer- Local Binary Pattern Histogram(LBPH) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighbourhood of each pixel and considers the result as a binary number.![LBPHFace Recognizer](https://user-images.githubusercontent.com/68141523/123547686-5ca3f700-d77f-11eb-8a08-93c21d498c57.png)
 
 # Flow
 Load face detection algorithms -> Load classifier for face recognition -> Training classifier for out dataset -> Reading frame from camera & preprocessing -> Face detection by its algorithm-> Predicting face by loading frame into model -> Display recognized class.
