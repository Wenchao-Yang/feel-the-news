__author__ = 'yang'

import re

from nltk.corpus import stopwords


def final_prep(text):

    # Remove non-letters
    letters_only = re.sub("[^a-zA-Z]", " ", text)

    # Convert to lower case, split into individual words
    words = letters_only.lower().split()

    # convert the stop words to a set, because it's much faster
    stops = set(stopwords.words("english"))

    # Remove stop words
    meaningful_words = [w for w in words if not w in stops]

    # Join the words back into one string separated by space,
    # and return the result.
    return(" ".join( meaningful_words ))


import nltk.data
nltk.download()

# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Define a function to split a review into parsed sentences
def review_to_sentences( review, tokenizer):
    # Function to split a review into parsed sentences. Returns a
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(review.strip())
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            sentences.append( final_prep( raw_sentence ))
    #
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences



def simple_analyze(text):
    text = final_prep(text)



if __name__ == '__main__':
    title1 = 'Outrage as children raped in Delhi'
    text1 = '''Two young children are reported to have been raped in the Indian capital of Delhi, drawing strong criticism from the city's chief minister.Arvind Kejriwal accused the government and police of not doing enough to protect minors in the city. The latest attacks come after a four-year-old girl was allegedly raped in Delhi last week. Two years ago, India tightened its laws on sexual violence after the brutal gang-rape and murder of a student.Mr Kejriwal criticised Indian Prime Minister Narendra Modi and Lieutenant-Governor Najeeb Jung for failing to provide adequate safety and security in the city. The responsibility for the Delhi Police comes under the national government's home ministry."Repeated rape of minors is shameful and worrying. Delhi police has completely failed to provide safety. What are PM n his LG doing?," Kejriwal said on Twitter.Kejriwal said the prime minister should either act or transfer the control over the police to the state government.Abducted near home Police say one of the victims in the two separate attacks, a two-and-a-half year old girl, was abducted in west Delhi on Friday night by two men.She was sexually assaulted before being dumped in a park near her home.According to police reports, she was bleeding profusely when she was found. Tests showed she had been raped at least once."We have launched a manhunt for the suspects. So far no-one has been  arrested," west Delhi police chief, Pushpendra Kumar, told AFP.In a separate incident, a five-year-old girl was gang-raped by three men in the east of the city.Police say she was lured to a neighbour's house where she was repeatedly raped.Both girls are undergoing medical treatment but are believed to be out of danger, police said.The incidents come one week after a four-year-old girl was allegedly raped before being abandoned by a railway track in the capital.The girl, who was found near her home in a poor neighbourhood in the north of the city, had been slashed with a sharp object and had severe internal injuries. Police have arrested a 25-year-old man in connection with the attack.The latest attacks have caused outrage in the Indian capital, with many people taking to social media to express their disgust at the crimes.The head of  the Delhi Commission for Women, Swati Maliwal, tweeted "When will Delhi wake-up? Til when will girls continue to be brutalised in Indian capital?".The gang rape and murder of a student in 2012 in Delhi led to protests and new anti-rape laws in the country. However, brutal sexual attacks against women and children continue to be reported across the country. Delhi alone had more than 2,000 rapes reported in 2014. '''

