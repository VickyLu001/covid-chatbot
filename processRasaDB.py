import pandas as pd
import sqlite3
import json 

RASA_DB_FILE = "rasa.db"
RASA_ANA_FILE = "cleanRasa.db"
# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect(RASA_DB_FILE)
conversation_data = pd.read_sql_query("SELECT data FROM conversation_event", con)

# Divide the conversation into sessions
# inactivity period in the units of seconds
inactivity_period_allowed = 1*60
old_sender_id = None
old_timestamp = 0

# extract conversation text and entities information from the database
conversation_text = pd.DataFrame(columns=('sender_id', 'session_id', 'event', 'timestamp', 'text', 'entities'))
for conversation in conversation_data['data']:
    if 'text' in conversation:
        res = json.loads(conversation)
        sender_id = res['sender_id']
        event = res['event']
        timestamp = res['timestamp']
        text = res['text']
        entities = defaultdict(list)
        if 'parse_data' in res:
            for i in res['parse_data']['entities']:
                entities[i['entity']].append(i['value'])
        if old_sender_id != sender_id:
            conversation_id = 1
        elif timestamp - old_timestamp > inactivity_period_allowed or text=='/restart':
            conversation_id += 1
            
        values_to_add = {'sender_id': sender_id,'session_id': conversation_id, 'event':event,\
                         'timestamp':timestamp, 'text':text, 'entities':json.dumps(entities) if entities else ""}
        row_to_add = pd.Series(values_to_add,)
        conversation_text = conversation_text.append(row_to_add, ignore_index=True)
        
        old_sender_id = sender_id
        old_timestamp = timestamp  
con.close()

# save the conversation text into database as table "conversation_text"
sqlite_connection = sqlite3.connect(RASA_ANA_FILE)
conversation_text.to_sql('conversation_text', sqlite_connection, if_exists='replace')
sqlite_connection.close()

# Build patient profiles based on NER results
con = sqlite3.connect("conversation.db")
conversation_data = pd.read_sql_query("SELECT * FROM conversation_text", con)
patient_profile = pd.DataFrame(columns=('patient_id', 'session_id', 'symptoms', 'drugs'))
old_conversation_id = None
old_sender_id = None
symptoms = set()
drugs = set()
for index, message in conversation_data.iterrows():
    if old_conversation_id !=  message['session_id'] or old_sender_id != message['sender_id']:
        if drugs or symptoms:
            values_to_add = {'patient_id': message['sender_id'], 'session_id': message['session_id'],\
                             'symptoms':json.dumps(list(symptoms)) if symptoms else "", 'drugs': json.dumps(list(drugs))if drugs else ""}
            row_to_add = pd.Series(values_to_add,)
            patient_profile = patient_profile.append(row_to_add, ignore_index=True)
            symptoms = set()
            drugs = set()
    if message['event'] == 'user':
        if message['entities']:
            entities = json.loads(message['entities'])
            if 'DISEASE' in entities:
                for entity in entities['DISEASE']:
                    symptoms.add(entity.lower())
            if 'CHEMICAL' in entities:
                for entity in entities['CHEMICAL']:
                    drugs.add(entity.lower())
    old_conversation_id = message['session_id']
    old_sender_id = message['sender_id']
con.close()

#Save it to database as "patient_profile" table
sqlite_connection = sqlite3.connect(RASA_ANA_FILE)
patient_profile.to_sql('patient_profile', sqlite_connection, if_exists='replace')
sqlite_connection.close()