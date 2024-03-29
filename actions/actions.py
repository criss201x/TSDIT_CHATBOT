from rasa_sdk import Tracker, Action
from typing import Any, Text
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


# DO NOT copy paste whole file

class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> list[dict[Text, Any]]:
        # add different functionalities like google search, wiki search, etc to provide more answer

        user_messages = [event for event in tracker.events if event['event'] == 'user']
        if not user_messages or len(user_messages) == 1:
            dispatcher.utter_message(response="utter_saludar")
        else:
            # Handle non-first messages or delegate to another action as needed
            latest_message = tracker.latest_message.get("text")
            dispatcher.utter_message(text="Disculpa, no logró entender lo que dices, podrias reperirlo?")            

        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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
