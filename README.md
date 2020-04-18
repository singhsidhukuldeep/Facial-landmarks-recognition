# Facial-landmarks-recognition
Identifying faces in photos or videos is very cool, but this isn’t enough information to create powerful applications, we need more information about the person’s face, like position, whether the mouth is opened or closed, whether the eyes are opened, closed, looking up and etc.

Here we are using  `Dlib`, a library capable of giving you 68 points (land marks) of the face.

## Setup

**Important:** *To install the required libraries you will need [CMake](https://cmake.org/)*

* **`Linux`** Systems:

    ```shell
    sudo pip3 install virtualenv

    virtualenv -p python3 venv --no-site-packages

    source venv/bin/activate

    pip3 install -r requirements.txt
    ```

    ```shell
    deactivate
    ```

* **`Windows`** Systems:

    ```shell
    pip3 install virtualenv

    virtualenv -p python3 venv --no-site-packages

    venv\Scripts\activate

    pip3 install -r requirements.txt
    ```

    ```shell
    venv\Scripts\deactivate
    ```

    If getting issue in installing virtualenv on `windows`, use administrator privileges

## Running

* Using from command line

    ```shell
    python3 faces.py ./face.jpg ./model/shape_predictor_68_face_landmarks.dat
    ```

    >*images will be saved in the same directory as the given image*

* Importing as a module

    ```Python
    # importing
    from faces import detectFaces

    # running the function
    detectFaces (image_loaction = "face.jpg", model_location = "./model/shape_predictor_68_face_landmarks.dat")
    detectFaces (image_loaction = "multiple_faces.png", model_location = "./model/shape_predictor_68_face_landmarks.dat")

    # images will be saved in the same directory as the given image
    ```

    >*images will be saved in the same directory as the given image*

## Results

### Single face

Input            |  Landmarks detected            |  Jawline detected
:-------------------------:|:-------------------------:|:-------------------------:
![](face.jpg)  |  ![](detected_face.jpg)  |  ![](jawline_detected_face.jpg)

### Multiple faces

Input            |  Landmarks detected            |  Jawline detected
:-------------------------:|:-------------------------:|:-------------------------:
![](multiple_faces.png)  |  ![](detected_multiple_faces.png)  |  ![](jawline_detected_multiple_faces.png)
