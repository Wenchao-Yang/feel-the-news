# coding=utf-8
__author__ = 'yang'


# pseudo code
# 0. loop text, add space after period if there is not
# 1. parse text into separate sentences based on punc
# 2. cal total sentences
# 3. remove pun
# 4. split text into a list of separate word
# 5. cal total words
# 6. cal total digits
# 7. cal total syllables
# 8. cal complex words

class Text(object):
    '''Text to be analyzed'''

    def __init__(self, text):

        self.sent_count = 0  # no of sentences
        self.word_count = 0  # no of words
        self.char_count = 0  # no of chars, no space
        self.syll_count = 0  # no of syllables
        self.comp_count = 0  # no of words which have three or more than three syllables

        # 0. loop text, add space after period if there is not
        text_list = text.split()
        text_list_len = len(text_list)
        for i in range(text_list_len):
            if '.' in text_list[i]:
                text_list[i] = text_list[i].replace('.', '. ')
        text = ' '.join(text_list)

        # 1. parse text into separate sentences based on punc
        from nltk.tokenize import sent_tokenize
        # from 'Models' tab and select 'punkt'
        sentences = sent_tokenize(text.decode('utf8'))
        # 2. cal total sentences
        self.sent_count = len(sentences)
        # 3. remove pun
        import string

        table = string.maketrans("", "")
        punc_removed_text = text.translate(table, string.punctuation)
        # 6. cal total digits
        self.char_count = len(punc_removed_text) - punc_removed_text.count(' ')
        # 4. split text into a list of separate word
        text_list = punc_removed_text.split()
        # 5. cal total words
        self.word_count = len(text_list)
        # 7. cal total syllables
        # 8. cal complex words

        from textstat.textstat import textstat

        for i in text_list:
            each_syll = textstat.syllable_count(i.decode('utf8'))
            if each_syll == 0:
                each_syll = 1
            self.syll_count += each_syll
            if each_syll>=3:
                self.comp_count += 1


    def flesch_read_ease(self):
        '''
        :return:  Flesch reading-ease test, higher scores indicate material that is easier to read
        '''

        score = 206.835 - 1.015*self.word_count/self.sent_count - 84.6*self.syll_count/self.word_count
        return round(score, 1)

    def flesch_grade_level(self):
        '''
        :return: Flesch–Kincaid grade level: the number of years of education generally required to understand this text,
        relevant when the formula results in a number greater than 10.
        '''
        score = 0.39*self.word_count/self.sent_count + 11.8*self.syll_count/self.word_count - 15.59
        return round(score, 1)

    def gunning_fog_index(self):
        '''
        :return: The index estimates the years of formal education needed to understand the text on a first reading.
        '''

        score = 0.4*self.word_count/self.sent_count + 40*self.comp_count/self.word_count
        return round(score, 1)

    def our_index(self):
        '''
        :return: approximates the U.S. grade level thought necessary to comprehend the text.
        '''

        score = 0.0588 * self.char_count/self.word_count*100.0 - 0.296*self.sent_count/(self.word_count/100.0) - 15.8
        return round(score, 1)

    def smog(self): # only perform well when number of sentences >= 30
        '''
        :return:estimates the years of education needed to understand a piece of writing.
        It will only perform well when number of sentences >= 30
        '''
        import math
        score = 1.0430* math.sqrt(self.comp_count * 30.0/self.sent_count) + 3.1291
        return round(score, 1)

    def automated_index(self):

        '''
        :return: produces an approximate representation of the US grade level needed to comprehend the text.
        '''
        score = 4.71* self.char_count/ self.word_count + 0.5*self.word_count/self.sent_count - 21.43
        return round(score, 1)

    def avg_grade(self):

        '''
        :return: Average grade based on Flesch-Kincaid Grade Level, Gunning-Fog Score,
        Coleman-Liau Index, Automated Readability Index
        Smog will be used only when number of sentences >= 30
        '''
        sum4 = self.flesch_grade_level() + self.gunning_fog_index() + self.our_index() + self.automated_index()
        if(self.sent_count<30):
            avg = sum4/4
        else:
            avg = (sum4 + self.smog())/5

        return round(avg, 1)



if __name__ == '__main__':
    test_text1 = '''Two young children a, drawing city's minister.Arvind to prcity. The a four-year-old girl was allegedly raped ministry."Repeated rape of minors is shameful and worrying. Delhi police has completely failed to provide safety. What are PM n his LG doing?," Kejriwal said on Twitter.Kejriwal said the prime minister should either act or transfer the control over the police to the state government.Abducted near home Police say one of the victims in the two separate attacks, a two-and-a-half year old girl, was abducted in west Delhi on Friday night by two men.She was sexually assaulted before being dumped in a park near her home.According to police reports, she was bleeding profusely when she was found. Tests showed she had been raped at least once."We have launched a manhunt for the suspects. So far no-one has been  arrested," west Delhi police chief, Pushpendra Kumar, told AFP.In a separate incident, a five-year-old girl was gang-raped by three men in the east of the city.Police say she was lured to a neighbour's house where she was repeatedly raped.Both girls are undergoing medical treatment but are believed to be out of danger, police said.The incidents come one week after a four-year-old girl was allegedly raped before being abandoned by a railway track in the capital.The girl, who was found near her home in a poor neighbourhood in the north of the city, had been slashed with a sharp object and had severe internal injuries. Police have arrested a 25-year-old man in connection with the attack.The latest attacks have caused outrage in the Indian capital, with many people taking to social media to express their disgust at the crimes.The head of  the Delhi Commission for Women, Swati Maliwal, tweeted "When will Delhi wake-up? Til when will girls continue to be brutalised in Indian capital?".The gang rape and murder of a student in 2012 in Delhi led to protests and new anti-rape laws in the country. However, brutal sexual attacks against women and children continue to be reported across the country. Delhi alone had more than 2,000 rapes reported in 2014. '''
    text1 = Text(test_text1)

    print(text1.sent_count)

    test_text2 = '''Two young children city's minister.Arvind four-year-old girl'''
    text2 = Text(test_text2)
    print(text2.sent_count, text2.word_count, text2.char_count, text2.syll_count, text2.comp_count)
    print(len(test_text2))

    # test: Flesch reading ease
    print('Flesch reading ease: ')
    print(text1.flesch_read_ease())

    # test: Flesch–Kincaid grade level
    print('Flesch–Kincaid grade level: ')
    print(text1.flesch_grade_level())

    # test: Gunning fog index
    print('Gunning fog index: ')
    print(text1.gunning_fog_index())

    # test: Coleman–Liau index
    print('Our index: ')
    print(text1.our_index())

    # test: SMOG
    print('SMOG: ')
    print(text1.smog())

    # test: Automated readability index
    print('Automated readability index: ')
    print(text1.automated_index())

    # test: avg score
    print('AVG: ')
    print(text1.avg_grade())