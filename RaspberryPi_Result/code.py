
from picamera import PiCamera
from time import sleep
from lobe import ImageModel

camera = PiCamera()

# Load Lobe TF model
# --> Change model file path as needed
model = ImageModel.load('/home/pi/Desktop/model')

# Take Photo
def take_photo():
    print("Pressed")
    # Start the camera preview
    camera.start_preview(alpha=100)
    # wait 2s or more for light adjustment
    sleep(3) 
    # Optional image rotation for camera
    # --> Change or comment out as needed
    camera.rotation = 270
    #Input image file path here
    # --> Change image path as needed
    camera.capture('/home/pi/Pictures/image.jpg')
    #Stop camera
    camera.stop_preview()
    sleep(1)

# Identify prediction and turn on appropriate LED
def led_select(label):
    print(label)
    if label == "cardboard":
        print('')
       
    if label == "glass":
        print('')
       
    if label == "metal":
        print('')
        
    if label == "paper":
        print('')
      
    if label == "plastic":
        print('')
         
    if label == "trash":
        print('')
        
    else:
        print('')

take_photo()
        # Run photo through Lobe TF model
result = model.predict_from_file('/home/pi/Pictures/image.jpg')
        # --> Change image path
led_select(result.prediction)
