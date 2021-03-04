# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

# +
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, SessionStarted, ActionExecuted, EventType




class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    

    async def run(
        self,
        output_channel: "OutputChannel",
        nlg: "NaturalLanguageGenerator",
        tracker: "DialogueStateTracker",
        domain: "Domain",
    ):
        # the session should begin with a `session_started` event
        events = [SessionStarted(metadata=self.metadata)]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(FollowupAction(name='load_profile'))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events


class ActionFollowUpSymptoms(Action):
    def name(self) -> Text:
        return "ask_symptom_develop"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(text="test message for ask_symptom_develop")
        symptoms = tracker.get_slot('old_symptoms')
        #print(symptoms)
        #print(type(symptoms))
        if symptoms:
            dispatcher.utter_message(text='You mentioned in our last conversation that you have symptoms including {}. How do you feel about them now?'.format(', '.join(symptoms)))
        return []

class ActionFollowUpSymptoms(Action):
    def name(self) -> Text:
        return "ask_temperature"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='What is your temperature?')
        return []

class ActionLoadProfile(Action):

    def name(self) -> Text:
        return "load_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        import sqlite3
        import json
        state = tracker.current_state()
        sender_id = state["sender_id"]#"42613706c7444af4ac33a316d0dcc2a8"
        con = sqlite3.connect("patient_profile.db")
        c = con.cursor()
        sessions = list(c.execute(f'SELECT * FROM patient_profile WHERE patient_id="{sender_id}"'))
        #returns = []
        symptoms = None
        drugs = None
        if sessions:
            if sessions[-1][-2]:
                symptoms = json.loads(sessions[-1][-2])
            if sessions[-1][-1]:
                drugs = json.loads(sessions[-1][-1])
        con.close()
        results = [SlotSet("old_symptoms", symptoms), SlotSet("old_drugs", drugs)]
        if symptoms:
            results.append(FollowupAction(name='ask_symptom_develop'))

        return results
    
class ActionRecordSymptom(Action):

    def name(self) -> Text:
        return "record_symptom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Symptom recorded.")

        results = []

        if (tracker.latest_message)['entities']:
            disease_set = set(tracker.get_latest_entity_values('DISEASE'))
            if 'fever' in disease_set:
                results.append(FollowupAction(name='ask_temperature'))

        return results


class ActionRecordDrug(Action):

    def name(self) -> Text:
        return "record_drug"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Drug recorded!")

        return []

class ActionRecordTemperature(Action):

    def name(self) -> Text:
        return "record_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Temperature recorded.")

        return []
