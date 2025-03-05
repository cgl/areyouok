# areyouok

# How to run the app locally?

## Google Sentiment Analysis

Google Sentiment Analysis requires you to have an Google Account and activate
the API (there is $300 initial credit if you use trial version). To do so you need to
follow the steps descripbed in [Google's documentation](https://cloud.google.com/natural-language/docs/quickstart-client-libraries?refresh=1&authuser=1).
Make sure to follow the "Before you begin" section step 1. Save the JSON file and
make sure it's in .gitignore.

Then you need to set your environmental variable pointing to the JSON file you saved:

```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/json/file
```

Example scroes we get back from Sentiment Analyzis API:

```
$ python3 core/analyze_text.py "I'm so scared. omg"
{'score': 0.10000000149011612, 'magnitude': 0.20000000298023224}
$ python3 core/analyze_text.py "I'm so scared."
{'score': 0.10000000149011612, 'magnitude': 0.10000000149011612}
$ python3 core/analyze_text.py "I'm so, so happy"
{'score': 0.8999999761581421, 'magnitude': 0.8999999761581421}
$ python3 core/analyze_text.py "I want to die"
{'score': 0.10000000149011612, 'magnitude': 0.10000000149011612}
$ python3 core/analyze_text.py "I'm sad :("
{'score': -0.4000000059604645, 'magnitude': 0.4000000059604645}
$ python3 core/analyze_text.py "I want to die. I'm rubbish"
{'score': -0.30000001192092896, 'magnitude': 0.800000011920929}
$ python3 core/analyze_text.py "I'm useless"
{'score': -0.699999988079071, 'magnitude': 0.699999988079071}
```

