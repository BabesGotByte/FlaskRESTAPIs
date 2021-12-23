# FlaskRESTAPIs
Building flask REST APIs

[![Generic badge](https://img.shields.io/badge/Framework-Flask-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Language-Python-orange.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Build-RESTAPIs-blue.svg)](https://shields.io/)

## Prerequisites
1. Install any text editor: </br>
  Commands to install sublime text editor: </br>
  `wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -` </br>
  `echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list` </br>
  `sudo apt-get update` </br>
  `sudo apt-get install sublime-text` </br>
2. Install the libraries listed in the requirements.txt file. </br>
  Command: </br>
  `sudo apt install python3-testresources` </br>
  `pip3 install -r requirements.txt` </br>
3. Run code. </br>
   On first terminal: </br>
   `python3 Code.py` </br>
    On second terminal: </br>
   `python3 teset.py` </br>
 
## Deploy on Heroku
`sudo snap install heroku--classic`</br>
`heroku login` </br>
`heroku create flaskapi-heroku --buildpack heroku/python`</br>
Here, flaskapi-heroku is the name of the application created on Heroku.

## Link to test live APIs
https://flaskapi-heroku.herokuapp.com/

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
