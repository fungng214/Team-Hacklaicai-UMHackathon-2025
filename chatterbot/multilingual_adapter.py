from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from langdetect import detect
from translate import Translator

class MultilingualAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.supported_languages = ['en', 'id', 'ms', 'th', 'vi', 'tl', 'my', 'km', 'lo']

    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters=None):
        user_input = input_statement.text

        try:
            detected_lang = detect(user_input)
        except Exception:
            return Statement(text="Sorry, I couldn't detect the language. Responding in English."), 1.0

        if detected_lang not in self.supported_languages:
            return Statement(text="Sorry, your language is not supported. Responding in English."), 1.0

        # Step 1: Translate input to English (fallback to original input if failed)
        if detected_lang != 'en':
            try:
                translator_to_en = Translator(from_lang=detected_lang, to_lang="en")
                translated_input = translator_to_en.translate(user_input)
            except Exception:
                translated_input = user_input
        else:
            translated_input = user_input

        # Step 2: Get response in English
        response = self.chatbot.get_response(translated_input)
        response_text = str(response)

        # Step 3: Translate back to user's language (fallback to English if failed)
        if detected_lang != 'en':
            try:
                translator_to_user = Translator(from_lang="en", to_lang=detected_lang)
                translated_response = translator_to_user.translate(response_text)
            except Exception:
                translated_response = response_text  # fallback to English
        else:
            translated_response = response_text

        return Statement(text=translated_response), 1.0
