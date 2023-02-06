# Transportation App
App where passengers can look for their most convenient way of travelling (bus, train or car) and book a trip!
A place where you can find all ways of transport and decide the best way to get to your destination.

## This is what we have so far:
https://user-images.githubusercontent.com/19626464/217091767-3c2fd64a-c728-4a1e-a53f-8f655a1cc4aa.mp4

## Installation
#### 🐍 python_version (3.6 to 3.8 inc)
```bash
git clone https://github.com/DriiGY/transportation-app.git
cd transportation-app
```

### Linux
Install pip:

[pip3](https://www.educative.io/answers/installing-pip3-in-ubuntu)

Install virtualenv via pip: 
```bash
pip install virtualenv
```
Test your installation:
```bash
virtualenv --version
```
Create a virtual environment for project:
```bash
cd transportation-app
virtualenv venv
```
Activate virtual environment variable (To deactivate: deactivate):
```bash
ource venv/bin/activate
```

## Install dependencies
Install kivy: (Kivy and kivymd need to be compatible or might show: error:kivy is too old)
```bash
pip install kivy==2.0.0
```
kivymd (kivymd==0.104.2 should work aswell)
```bash
pip install kivymd==1.0.2 
```
Install xclip and xsel:
```bash
sudo apt-get install xclip
```
Install:
```bash
pip install kivyauth, credentials, plyer, geocoder, geopy, email-validator  
```
Install requirements:
```bash
pip install -r requirements.txt
```
Add `credentials.py` to directory like `./transportation-app/credentials.py`:
```bash
API_KEY = "YOUR_API_KEY"
```
- Get your api key by signing up to https://openrouteservice.org/ and create a key.


!ignore: client_id.txt and client_secret.txt are not used at the moment.

Run program (from `./transportation-app/`):
```bash
python3 main.py --size=412x732
```

## what do we have so far:

 ✅ What you see in the video.
 
 ❌ No settings screen (working on it now).
 
 
 **NO BACKEND**:
 
 ❌ No database.
 
 ❌ Payment method.
 
 ❌ QR code for ticket pdf.
 
 ...
