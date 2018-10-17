import sys

import six

from google.api_core.exceptions import InvalidArgument
from google.cloud import language_v1
from google.cloud.language_v1 import enums


def format_request(text):
    type_ = enums.Document.Type.PLAIN_TEXT
    return {"type": type_, "content": text}


def analyze_sentiment(text):
    client = language_v1.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    document = format_request(text)

    try:
        response = client.analyze_sentiment(document)
        sentiment = response.document_sentiment
        return {"score": sentiment.score, "magnitude": sentiment.magnitude}
    except InvalidArgument as e:
        return {"error": e}


def main():
    response = analyze_sentiment(*sys.argv[1:])
    print(response)


if __name__ == "__main__":
    main()
