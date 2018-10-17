# areyouok

# How to run the app locally?

## Google Sentiment Analyzis

Google Sentiment Analyzis requires you to have an Google Account and activate
the API (there is $300 initial credit if you use trial version). To do so you need to
follow the steps descripbed in [Google's documentation](https://cloud.google.com/natural-language/docs/quickstart-client-libraries?refresh=1&authuser=1).
Make sure to follow the "Before you begin" section step 1. Save the JSON file and
make sure it's in .gitignore.

Then you need to set your environmental variable pointing to the JSON file you saved:

```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/json/file
```
