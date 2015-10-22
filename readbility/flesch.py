__author__ = 'yang'


class Flesch:
    def __init__(self, text, locale='en_GB'):
        from readability_score.common import getTextScores

        self.scores = getTextScores(text, locale)
        self.reading_ease = 206.835 - ( 1.015 * self.scores['sentlen_average'] ) - ( 84.6 * self.scores['wordlen_average'] )