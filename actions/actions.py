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




# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionSearchWord(Action):
#     def name(self) -> Text:
#         return "action_searchword"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         word = tracker.get_slot("word")

#         if word and word.lower() == "bank":
#             response = "Here are three different meanings of the word bank:\n"\
#                        "a) a long pile or heap\n"\
#                        "b) a business institution for receiving, lending, and keeping money safe.\n"\
#                        "c) the slope of land that borders a stream, river, or lake"
#         elif word:
#             response = f"Sorry, I don't have information on the word {word}"
#         else:
#             response = "Sorry, I didn't catch the word you're asking about."

#         dispatcher.utter_message(response)
#         return []

# class ActionSearchPhrase(Action):
#     def name(self) -> Text:
#         return "action_searchphrase"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response = "The meaning of the phrase 'It's raining cats and dogs' means: to rain heavily."
#         dispatcher.utter_message(response)
#         return []

# class ActionSearchSynonymsWord(Action):
#     def name(self) -> Text:
#         return "action_searchsynonyms_word"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response = "Some synonyms of bank as a long pile are row, series, array, group, sequence, line.\n"\
#                    "For the word bank as a business institution some synonyms are: savings bank, commercial bank, "\
#                    "credit union, investment firm, banking house, depository.\n"\
#                    "For the meaning as a slope of land that borders a river some synonyms are: edge, shore, shoreline, "\
#                    "coast, lakeside, riverside, seaside, waterfront, seafront."
#         dispatcher.utter_message(response)
#         return []

# class ActionSearchSynonymsPhrase(Action):
#     def name(self) -> Text:
#         return "action_searchsynonyms_phrase"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response = "It's raining cats and dogs it's like saying there is a rainstorm, or storm, thunderstorm, "\
#                    "thundershower, tempest, downpour"
#         dispatcher.utter_message(response)
#         return []

# class ActionLanguage(Action):
#     def name(self) -> Text:
#         return "action_language"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response = "In what language please?\nSay 'Spanish' or 'Italian' to understand the language target."
#         dispatcher.utter_message(response)
#         return []

# class ActionTranslateWord(Action):
#     def name(self) -> Text:
#         return "action_translateword"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         language = tracker.get_slot("language")
#         response = f"Translation in {language}:\n"\
#                    "a) for a long pile or heap the word is banco\n"\
#                    "b) for a business institution for money the word is banco\n"\
#                    "c) for a slope of land that borders a river or lake the word is orilla"
#         dispatcher.utter_message(response)
#         return []

# class ActionTranslatePhrase(Action):
#     def name(self) -> Text:
#         return "action_translatephrase"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         language = tracker.get_slot("language")
#         response = f"Translation in {language}:\n"\
#                    "a) llover a cántaros\n"\
#                    "b) llover a mares\n"\
#                    "c) caer soretes de punta"
#         dispatcher.utter_message(response)
#         return []

