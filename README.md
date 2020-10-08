# AI-rock-paper-scissors
The program is written in python and uses OpenCV, tensorflow, Keras for implementation
Creating a virtual environment is always advised as some of the keras applications working may change in the future.

Direction to use the repository:

1. The folder computer_moves contains the images of rock, paper, scissors that are used to display as computer moves.
2. Creation of python virtual environment is advised and all the basic module that are required to be installed are given is the "requirements.txt" file
3. The programs are to be executed in the following order:
          images_for_model.py -> train_the_model.py -> test_the_model.py
          
   a) images_for_model will use openCV and will obtain 200 images of rock, paper, scissors and none by         default but it can be changed. It automatically creates and stores in their prescribed folder name
   b) Train_the_model is used to both built and train the model on the images given.
   c) Test_the_model is used to test our model on any other test data.

4. After the execution of above programs, there are 3 variety of programs - finalgame vs CPU, finalgame for 2 players and finalgame with interface. These programs work accordingly to their names.



