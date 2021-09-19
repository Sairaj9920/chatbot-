# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
##from rasa_core.events import Restarted
import pred


class ActionPredict(Action):

    def name(self) -> Text:
        return "action_predict"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mes = "thank you for your precious time....."+pred.pred()
        dispatcher.utter_message(text=mes)

        return []

##class ActionRestarted(Action):
##    """ This is for restarting the chat"""
##
##    def name(self):
##        return "action_chat_restart"
##
##    def run(self, dispatcher, tracker, domain):
##        return [Restarted()]
