
def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import control
    import io
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    gesture = {'Hand':False,'Finger':False,'Thumb':False}
    
    for label in labels:
        hand = 'Hand' in label.description
        finger = 'Finger' in label.description
        thumb = 'Thumb' in label.description
        
        if hand and label.score > .60:
            gesture['Hand'] = hand
        if finger and label.score > .60:
            gesture['Finger'] = finger
        if thumb and label.score > .60:
            gesture['Thumb'] = thumb
        
    print(gesture)
        
    if(gesture['Hand'] and gesture['Finger'] and gesture['Thumb']):
        control.openTab()
    if((gesture['Finger'] or gesture['Hand']) and not gesture['Thumb']):
        control.closeTab()

def recordVideo():
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    
    frames = 1
    while(True):
        frames += 1
        frame_path = 'Frames/frame' + str(frames) + '.png'
        
        ret,frame = cap.read() #return a single frame in variable `frame`
        cv2.imshow('C O M H A N D',frame) #display the captured image
        
        if frames%5 == 0:   
            cv2.imwrite(frame_path,frame) #write frame to file
            detect_labels(frame_path)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #quit pressing 'q' 
            cv2.destroyAllWindows()
            break

    cap.release()

  