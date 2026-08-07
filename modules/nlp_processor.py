import spacy

nlp = spacy.load("en_core_web_sm")


def process_text(text):
    doc = nlp(text)

    for token in doc:
        print(token.text)