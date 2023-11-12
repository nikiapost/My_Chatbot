# My Chatbot
Conversational Chatbot for Accessibility
# Introduction
The Conversational Chatbot for Accessibility is a project aimed at providing a user-friendly interface for visually impaired people in order to have access into dictionary functionalities and translation services. This chatbot serves as an assistant for blind users to explore word meanings, find synonyms and translate text into various languages. In short, it enables the accessibility of linguistic resources.
Conversational Chatbot for Accessibility is built on the Rasa conversational AI platform. In its current basic form, the chatbot provides fundamental dictionary and translation capabilities, paving the way for future integrations with external resources to be used as databases, in order to enrich the user experience and expand the range of the available services.
# Features
•	Word meaning lookup
•	Synonym retrieval
•	Text translation into various languages
# Getting Started
To run the chatbot locally, follow these steps:
1.	Clone the repository.
2.	Install the required dependencies using pip install -r requirements.txt    
3.	Run the chatbot using rasa run actions and rasa shell commands.
# Main Scenarios
First scenario, called search_word, is about finding the meaning of a word.
Second scenario, called search_synonyms, is about finding synonyms of a word.
Finally the third scenario, called translate_words, is about translating words in other languages.
All three scenarios try to keep in mind the formal and informal way of speaking.
# Usage
Once the chatbot is up and running, you can interact with it using, among others, the following commands:
•	"Find the meaning of [word]."
•	"Are there any synonyms of the [word]"
•	"Translate [text] to [language]."
# Next Steps
The next phase of development includes integrating external APIs such as https://www.wordreference.com/ and https://www.deepl.com/translator to improve the chatbot's functionality, in order for the chatbot to be able to provide users with a wide scope experience in accessing linguistic resources, when finished.
# Acknowledgements
We express our gratitude to the Rasa team for their conversational AI platform, which has enabled us to create this chatbot for accessibility.
# References
1.	Diamantino Freitas, Georgios Kouroupetroglou (2008). “Speech technologies for blind and low vision Persons”, Technology and Disability, Volume 20, 135–156.
2.	S. Dobrisek, J. Gros, F. Mihelic and N. Pavesic, "HOMER: a voice-driven text-to-speech system for the blind," ISIE '99. Proceedings of the IEEE International Symposium on Industrial Electronics (Cat. No.99TH8465), Bled, Slovenia, 1999, pp. 205-208 vol.1, doi: 10.1109/ISIE.1999.801785.
3.	BATŮŠEK, Robert and Ivan KOPEČEK. User Interfaces for Visually Impaired People. In Proceedings of 5th ERCIM Workshop on User Interfaces for All. Dagstuhl, SRN: GMD, 1999. p. 167-174. GMD Report 74. ISBN 3-88457-969-X.
