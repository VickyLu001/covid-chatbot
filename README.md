# Covid Chatbot based on Rasa

## Pre-requisite
1. Install Rasa
```
pip install rasa scispacy==0.3.0
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

## How to generate patient profile
To generate patient profile, you'll need to store all the conversation history. Our `processRasaDB.py` use the `rasa.db` created by RasaX here as an exmaple to illustrate it. To set up other database, please visit [tracker store](https://rasa.com/docs/rasa/tracker-stores/). You might need to modify the python script to work with other tracker store.
