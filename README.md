# Covid Chatbot based on Rasa

## Pre-requisite
1. Install Rasa
```
pip install rasa
```
For more information regarding rasa, please visit [rasa docs](https://rasa.com/docs/)

2. Install Scispacy model en_ner_bc5cdr_md
```
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.3.0/en_ner_bc5cdr_md-0.3.0.tar.gz
```
For more inforamtion regarding scispacy, please visit [scispacy](https://allenai.github.io/scispacy/)

## How to use our chatbot
To install our project
```
git clone https://github.com/VickyLu001/covid-chatbot.git
cd covid-chatbot
```
Now you can talk with our chatbot in terminal
```
rasa shell
```
To talk with our chatbot in other channels, refer to [Connecting to Messaging and Voice Channels](https://rasa.com/docs/rasa/messaging-and-voice-channels/)
