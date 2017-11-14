#These are all the dependencies needed to successfully install PyAssist on your local machine
#MAKE SURE PYTHON 2.7 AND PYAUDIO ARE INSTALLED!

echo 'PyAssist is built using various modules. You can choose which ones you want to install'

echo 'Installing main PyAssist module'
#speech
sudo apt-get install espeak python-espeak 

#speech recognition
sudo apt-get install pip
sudo pip install SpeechRecognition

#wx python
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-doc wx2.8-examples wx2.8-headers wx2.8-i18n

#webbrowser
sudo apt-get install webbrowser

while true; do
    read -p "Do you want wikipedia modules? [y/n]" yn
    case $yn in
        [Yy]* ) sudo pip install wikipedia; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

while true; do
    read -p "Do you want translation modules? [y/n]" yn
    case $yn in
        [Yy]* ) sudo pip install goslate; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo 'Updating system ...'
#refresh
sudo apt-get upgrade
sudo apt-get update
