## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_ask_symptom

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
* tell_symptom{"DISEASE":"headache"}
    - record_symptom

## interactive_story_1
* greet
    - utter_greet
* tell_symptom{"DISEASE": "headache"}
    - record_symptom

## interactive_story_1
* greet
    - utter_greet
* tell_drug{"CHEMICAL": "aspirin"}
    - record_drug

## interactive_story_1
* greet
    - utter_greet
* tell_symptom{"DISEASE": "vomited"}
    - record_symptom
* tell_drug{"CHEMICAL": "advil"}
    - record_drug
* goodbye
    - utter_goodbye


## Story from conversation with 9459eb04f1534f68ae26a287b746cf21 on October 18th 2020

* greet
    - utter_greet
* greet
    - utter_greet
* mood_unhappy
    - utter_ask_symptom
* tell_symptom
    - record_symptom

## Story from conversation with 33cf450af7e04d7f81f953a637666b52 on October 18th 2020

* greet
    - utter_greet
* greet
    - utter_greet
* mood_unhappy
    - utter_ask_symptom
* tell_symptom
    - record_symptom

## interactive_story_1
* greet
    - utter_greet
* mood_unhappy
    - utter_cheer_up
    - utter_ask_symptom
* tell_symptom{"DISEASE": "chest pain"}
    - record_symptom

## New Story

* greet
    - utter_greet
* mood_unhappy
    - utter_ask_symptom
* tell_symptom
    - record_symptom

## New Story

* greet
    - utter_greet
* tell_drug{"CHEMICAL":"hydroxychloroquine"}
    - record_drug

## Story from conversation with d015f1c7f87242759ca601080f01b56a on October 20th 2020

* greet
    - utter_greet
* mood_unhappy
    - utter_cheer_up
    - utter_ask_symptom
* tell_symptom{"DISEASE":"headache"}
    - record_symptom

## New Story

* tell_symptom
    - record_symptom

## New Story

* greet
    - utter_greet
    - load_profile
    - slot{"symptoms":["nose","coughing","headache"]}
    - slot{"drugs":null}
    - ask_symptom_develop

## New Story

* greet
    - utter_greet
    - load_profile
    - slot{"old_symptoms":["nose","coughing","headache"]}
    - slot{"old_drugs":null}
    - ask_symptom_develop

## New Story

* greet
    - utter_greet
    - load_profile
    - slot{"old_symptoms":null}
    - slot{"old_drugs":null}
    - ask_symptom_develop
* tell_symptom{"DISEASE":"fever"}
    - record_symptom
* tell_temperature{"TEMPERATURE":"105"}
    - record_symptom

## New Story

* greet
    - utter_greet
    - load_profile
    - slot{"old_symptoms":null}
    - slot{"old_drugs":null}
    - ask_symptom_develop
* tell_symptom{"DISEASE":"fever"}
    - record_symptom
    - ask_temperature
* tell_temperature{"TEMPERATURE":"38"}
    - record_symptom

## New Story

* greet
    - utter_greet
    - load_profile
    - slot{"old_symptoms":null}
    - slot{"old_drugs":null}
    - ask_symptom_develop
* tell_symptom{"DISEASE":"fever"}
    - record_symptom
    - ask_temperature
* tell_temperature{"TEMPERATURE":"100"}
    - record_symptom
