# Analyzer Simulator


## Description
This project provides an interface simulating probed part of the BZ depending on the position of the slit and the setup parameters (rotation, tilt). It can be useful in the real beamtime which is very valuable. 
<br>  
The main goal of this interface is to estimate the good energy value to be used to cover the desirable k range.

## Usage
You just have to enter the setup paramter to simulate the analyzer state and the coverd k range

<img src="screenshot_app.png"
     alt="gui" width="600" height="450"
      style="float: center"/>


## Installation
You can run the main.py script which is available in the source folder within the necessary resources. You have to add the required libraries using the following command after cloning (or downloading) the rep:
```console
pip install -r requirements.txt
```
The gui is tested under a python 3.8 version. (I recommend to setup a python 3.8 virtual environment).

## Roadmap
 <ul>
  <li>Avoid the crash of the app in case of empty value</li>
  <li>Transform the project on a desktop application or create a PyPI package</li>
</ul> 

## Support and Contributing
Let me know if you have any suggestions/ideas to enhance those scripts or add further settings. Your suggestions are warmly welcomed.
<br>
In case of a problem, It is strongly recommended to post an issue. For a more confidential demand, don't hesitate to email me.

## Acknowledgment
I thank Geoffroy Kremer for testing and verifying the formula.  




