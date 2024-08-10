# Brillouin Zone Navigator


## Description
This project provides an interface simulating probed part of the Brillouin Zone (BZ) depending on the position of the slit and the setup parameters (rotation, tilt). By tuning the ARPES geometry and experimental parameters, you can get a close idea of the 2D BZ part being probed. This kind of info can be useful in real beamtime, which is very valuable. Until now, only a hexagonal lattice system is included.
<br>  
The main goal of this interface is to estimate the good energy value to be used to cover the desirable k range.

## Usage
You have to enter the setup parameter to simulate the analyzer state and the covered k range

<img src="screenshot_app.png"
     alt="gui" width="600" height="450"
      style="float: center"/>


## Installation
You can just run the main.py script available in the source folder within the resources you need. You have to add the required libraries using the following command after cloning (or downloading) the rep:
```console
pip install -r requirements.txt
```
The GUI is tested under a Python 3.8 version. (I recommend to setup a python 3.8 virtual environment).

## Roadmap
 <ul>
  <li>Cover the rest of the crystallographic lattice system</li>
  <li>Avoid the crash of the app in case of empty value</li>
  <li>Transform the project on a desktop application or create a PyPI package</li>
</ul> 

## Support and Contributing
Let me know if you have any suggestions/ideas to enhance those scripts or add further settings. I want you to know that your suggestions are warmly appreciated.
<br>
In case of a problem, it is strongly recommended that an issue be posted. For a more confidential demand, don't hesitate to email me.

## Acknowledgment
I thank Geoffroy Kremer for testing and verifying the formula.  




