You can use this carpet Rectangle/Circle classifier just by **2 commands**.

1. git clone https://gitlab.com/aali361/carpet-shape-classifier-rmi .
2. docker-compose up
and boom :)


**Usage:**
send your image by post request to this endpoint
http://YOUR_IP_ADDRESS:9020/v1/carpet_classifier/image/


**Main Code:**
This classifier is powered by OpenCV package in python. The main code is in
"image/views.py" file. Take look at it and improve it for your usage.