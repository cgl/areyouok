MOOD_SAD = 'SAD'
MOOD_NEUTRAL = 'NEUTRAL'
MOOD_OK = 'OK'
MOOD_HAPPY = 'HAPPY'

MOOD_MAPPING = [
    {
        'from': -1,
        'to': -0.3,
        'mood': MOOD_SAD,
    },
    {
        'from': -0.3,
        'to': 0.2,
        'mood': MOOD_NEUTRAL,
    },
    {
        'from': 0.2,
        'to': 0.6,
        'mood': MOOD_OK,
    },
    {
        'from': 0.6,
        'to': 1,
        'mood': MOOD_HAPPY,
    },
]


def format_sentiment_analyzis_result(results):
    score = results.get('score')
    for mood_mapping in MOOD_MAPPING:
        if mood_mapping['from'] <= score < mood_mapping['to']:
            mood = mood_mapping['mood']
            break

    return {
        'mood': mood
    }

