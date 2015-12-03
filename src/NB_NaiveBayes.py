# coding=utf-8
__author__ = 'yang'

import json
from collections import defaultdict
import numpy as np

# TODO: check whether remove stopwords will improve prediction accuracy

class NBtrain(object):
    # For each case, it will have:
    # dictClass, storing each class and prior probabilities
    # For each class, it will have list of dictionaries to store P(w_k|c_j)
    # 1.
    # 2.
    # 3.
    # 4.


    def __init__(self, project):
        # firstTrain has generated some dictionaries, which includes:
        # 1. 'text_' + project + '.json': a defauldict, keys are classes, values are lists of original articles
        # 2. 'prior_'+project+'.json': a defaultdict, keys are classes, values are number of articles in each classes
        # Can be used to calculate prior probabilities
        # 3. 'num_'+project+'.json': a defaultdict, keys are classes, values are total number of words in that article
        # 4. 'wordfreq_' + project +'.json': a defaultdict, keys are classes, values are defaultdict (keys are words, values
        #     are the number of occurence of the words)
        # 5. 'vocab_' + project +'.json': a list of all vocabularies in the train data


        # classes: a list containing the project for each class
        # project: project of this classifier: sentiment, spam, category

        with open('prior_' + project + '.json') as f:
            self.prior_dict = json.load(f)

        with open('num_' + project + '.json') as f:
            self.num_dict = json.load(f)

        with open('wordfreq_' + project + '.json') as f:
            self.wordfreq_dict = json.load(f)

        with open('vocab_' + project + '.json') as f:
            self.vocabulary = json.load(f)  # vocabulary is a list

        self.classes = self.prior_dict.keys()  # self.classes is a list
        self.num_classes = len(self.classes)

        self.total_doc = sum(self.prior_dict.values())
        self.total_vocab = len(self.vocabulary)


class NBtest(object):
    '''
    @:param train It is a NBtrain object
    '''

    def __init__(self, text, train):

        classes = train.classes

        # un-normalized prob
        unnorm_prob = defaultdict(float)  # keys are classes, values are probabilities
        prob_word = defaultdict(float)  # keys are words in the test data, values are probabilities

        # process text first
        text = NBtext(text).text
        words = text.split()
        # total_words = len(words)

        # calculate the un-normalized prob
        for class1 in classes:
            for word in words:

                # add 1 smoothing
                if word in train.vocabulary:
                    if word in train.wordfreq_dict[class1].keys():
                        prob_word[word] += np.log(
                            (train.wordfreq_dict[class1][word] + 1.0) / (train.prior_dict[class1] + train.total_vocab))
                    else:
                        prob_word[word] += np.log(1.0 / (train.prior_dict[class1] + train.total_vocab))
                else:
                    prob_word[word] += np.log(1.0 / (train.prior_dict[class1] + train.total_vocab + 1.0))

            unnorm_prob[class1] = np.sum(prob_word.values()) #+ np.log(train.prior_dict[class1] * 1.0 / train.total_doc)
            prob_word = defaultdict(float)

        self.prob = unnorm_prob.copy()
        # self.prob.update( (x, np.e**y  ) for x, y in self.prob.items())
        # total_prob = sum(self.prob.values())
        # self.prob.update( (x, y/total_prob) for x, y in self.prob.items())


import basicProcess as bp


class NBtext(object ):
    '''
    Create a text that is ready to be analyzed
    Each text must be analyzed before putting into NB analyzer
    Criteria:
    0. add space after period if there is not. This is to fix one bug in crawler
    1. text is converted to lower case
    2. punctuation is removed
    3. stop word may be removed (leave one option to remove it or not)
    4. word is stemmed

    '''

    def __init__(self, text, removeStop=True, sentiment=False):
        # 0. add space after period if there is not
        text = bp.addSpace(text)

        # 1. text is converted to lower case
        text = text.lower()

        # 2. punctuation is removed
        text = bp.removePunc(text)

        # 3. stop word may be removed (leave one option to remove it or not)
        if removeStop:
            text = bp.removeStop(text)

        # 4. word is stemmed
        text = bp.stem(text)

        self.text = text


if __name__ == '__main__':
    # text = '''\nThe White House has '''

    # print('Test NBtext:')
    # NBtext1 = NBtext(text)
    # print(NBtext1.text)



    train = NBtrain('category')

    text = '\nThe White House has strongly condemned a visit to Moscow by Syrian President Bashar al-Assad.A spokesman criticised Russia for putting on a "red carpet welcome".The Syrian leader\'s trip on Tuesday came three weeks after Russia began air strikes in Syria against Islamic State militants and other forces.It was Mr Assad\'s first overseas trip since civil war broke out in Syria in 2011. The conflict has claimed more than a quarter of a million lives.On Thursday, a team of Russian MPs is due to meet President Assad and the head of the Syrian parliament in Damascus.\n\n\n\n\nWhile in Moscow, Mr Assad made a point of expressing his gratitude for Russia\'s military intervention in the conflict.He said Russia\'s involvement had stopped "terrorism" becoming "more widespread and harmful" in Syria.For his part, Mr Putin said Moscow\'s hope was that a "long-term resolution can be achieved on the basis of a political process with the participation of all political forces, ethnic and religious groups".  The BBC\'s Steve Rosenberg in Moscow says that by hosting the Syrian leader, President Putin was sending a clear message to the West - that Moscow is a key player in the Middle East, and that there can be no solution to the Syrian conflict without Russia\'s involvement.\'Emboldening\'"We view the red carpet welcome for Assad, who has used chemical weapons against his own people, at odds with the stated goal by the Russians for a political transition in Syria," White House spokesman Eric Schultz told reporters.A state department official said it was not surprised by the visit, but the main US concern was Russia\'s continued military support, which he said had emboldened the Assad government - something that would only serve to lengthen the civil war.In the wake of Mr Assad\'s surprise visit, President Putin spoke to a number of  Middle Eastern leaders to brief them. They included the leaders of Saudi Arabia and Turkey, which give support to Syrian rebels. Mr Putin also spoke to the Egyptian and Jordanian leaders, Russian news agencies said.Turkish Prime Minister Ahmet Davutoglu said that after the visit "the Syrian government has no legitimacy left".Analysis: Diplomatic correspondent Jonathan MarcusPresident Assad\'s surprise visit to Moscow represents a sign of growing confidence for the embattled Syrian president. Firstly he feels it safe to leave Damascus for the first time since the civil war in Syria erupted. It is also a  visible symbol of Russia\'s confidence in the current Syrian regime. The visit leaves little doubt that for now at least President Putin is intent on shoring up Mr Assad\'s position. But the trip may also mark a new stage in Russia\'s efforts to roll out a diplomatic plan alongside its military intervention in Syria. Mr Putin has been speaking to other regional players: the Turks, the Saudis, the Jordanians and the Egyptians. There\'s a simple message here. The road to any diplomatic settlement now runs through Moscow and,  for now at least,  Mr Assad has to be part of any interim solution.Russia launched air strikes in Syria on 30 September, saying they were hitting IS positions - which are also being targeted by US-led strikes.Western countries and Syrian activists say Russian planes have been focused on hitting non-IS targets in order to shore up the position of the Syrian army, a claim Moscow denies.Why is there a war in Syria?Anti-government protests developed into a civil war that, four years on, has ground to a stalemate, with the Assad government, Islamic State, an array of Syrian rebels and Kurdish fighters all holding territory.Who is fighting whom?Government forces concentrated in Damascus and the centre and west of Syria are fighting the jihadists of Islamic State and Jabhat al-Nusra, as well as less numerous so-called "moderate" rebel groups, who are strongest in the north and east. These groups are also battling each other. What\'s the human cost?More than 250,000 Syrians have been killed and a million injured. Some 11 million others have been forced from their homes, of whom four million have fled abroad - including growing numbers who are making the dangerous journey to Europe.How has the world reacted?Iran, Russia and Lebanon\'s Hezbollah movement are propping up the Alawite-led Assad government, while Turkey, Saudi Arabia and Qatar back the more moderate Sunni-dominated opposition, along with the US, UK and France. Hezbollah and Iran are believed to have troops and officers on the ground, while a Western-led coalition and Russia are carrying out air strikes.'

    text = '''A shooting at a family planning clinic in Colorado Springs has left two civilians and a police officer dead, with the suspected gunman under arrest.
Nine other people were injured during the standoff at the Planned Parenthood clinic, which lasted five hours before the suspect surrendered
A number of people were trapped inside the building as shots were exchanged.
The motive remains unclear. The Planned Parenthood group has drawn anti-abortion protests in the past.
"I want to convey to the loved ones of the victims, this is a terrible, terrible tragedy that occurred here in Colorado Springs today," Mayor John Suthers told a news conference.
"Obviously, we lost two civilian victims. We mourn the loss of a very brave police officer."
The dead officer was named as Garrett Swasey, 44.'''

    text = '''Minister digs in over doping row

The Belgian sports minister at the centre of the Svetlana Kuznetsova doping row says he will not apologise for making allegations against her.

Claude Eerdekens claims the US Open champion tested positive for ephedrine at an exhibition event last month. Criticised for making the announcement, he said: "I will never apologise. This product is banned and it's up to her to explain why it's there." Kuznetsova says the stimulant may have been in a cold remedy she took. The Russian said she did nothing wrong by taking the medicine during the event. The Women's Tennis Association cleared Kuznetsova of any offence because the drug is not banned when taken out of competition.

Eerdekens said he made the statement in order to protect the other three players that took part in the tournament, Belgian Justine Henin-Hardenne, Nathalie Dechy of France and Russia's Elena Dementieva. But Dechy is fuming that she has been implicated in the row. "How can you be happy when you see your face on the cover page and talking about doping?" Dechy said. "I'm really upset about it and I think the Belgian government did a really bad job about this. "I think we deserve an apology from the guy. You cannot say anything like this - you cannot say some stuff like this, saying it's one of these girls. This is terrible." Dementieva is also angry and says that Dechy and herself are the real victims of the scandal. "You have no idea what I have been through all these days. It's been too hard on me," she said. "The WTA are trying to handle this problem by saying there are three victims, but I see only two victims in this story - me and Nathalie Dechy, who really have nothing to do with this. "To be honest with you, I don't feel like I want to talk to Sveta at all. I'm just very upset with the way everything has happened."
'''

    text = 'dvd entertainment entertainment movie star oscar'

    text = '''A new method of delivering data, which uses the visible spectrum rather than radio waves, has been tested in a working office.
Li-fi can deliver internet access 100 times faster than traditional wi-fi, offering speeds of up to 1Gbps (gigabit per second).
It requires a light source, such as a standard LED bulb, an internet connection and a photo detector.
It was tested this week by Estonian start-up Velmenni, in Tallinn.'''

    text = '''Helpful or harmful? A drug that you can take before and after sex can help people cut their risk of HIV infection.

Men and women in the US can already take the drug as a daily pill. The new “on demand” regime could make the drug more convenient, and cheaper to use regularly, yet not everyone is convinced. Some doctors fear the approach will discourage condom use, while others, such as Michael Weinstein of AIDS Healthcare Foundation, see it as a free pass to promiscuity.

We should abandon such moralising for the sake of public health. “This will be a powerful tool for almost eliminating HIV transmission,” says Cécile Tremblay at the University of Montreal, Canada. “If we combine it with other measures we could reach that goal in developed countries within ten years.”



The medicine in question is called Truvada. It contains two antiviral drugs, also given to people infected with HIV, which stop the virus multiplying. Tremblay and her colleagues followed 400 gay men over nine months and showed that the drug reduced risk of infection by 86 per cent when taken just before sex and for two days after, and so was just as effective as the daily pill.

On the face of it, having any kind of unprotected sex seems risky. Yet Truvada users are making highly nuanced decisions about their risks, argues Sheena McCormack of University College London, who helped run a trial of daily Truvada.

In the West, such pre-exposure prophylaxis, or PrEP, has mainly been studied in gay men. Most trial participants used condoms some of the time, only forgoing them when it seemed safe, after asking their partners when they were last tested and when they’d had unsafe sex (see “Why I don’t always use condoms”, below).

PrEP may paradoxically reduce risk-taking in some. “If anything, I probably use condoms more now than I did before,” says Colby Briggs, a project manager at McGill University in Montreal. “Taking Truvada reminds you that '''

    text = '''Chicago's police chief has been fired following the outcry over the fatal shooting of a black teenager by a police officer.
The city's mayor, Rahm Emanuel, told reporters he had dismissed Superintendent Garry McCarthy because of an erosion in public trust.
A black 17-year-old, Laquan McDonald, was shot 16 times by a white police officer in October 2014.
Officer Jason Van Dyke has been charged with first-degree murder.
"This is not the end of the problem but it's the beginning to the solution of the problem," said Mr Emanuel.
"It's time for fresh eyes and new leadership to confront the challenges."
Mr Emanuel appointed the city's chief of detectives, John Escalante, to oversee the police department until they find a permanent replacement.
There had been calls for Mr McCarthy's resignation leading up to the mayor's announcement.
Members of the city council's black caucus, urging for his resignation, cited Chicago's high crime rate and lack of transparency from the police department.'''

    result = NBtest(text, train)
    print(result.prob)



    

    #result = NBtest(text, train)
    #print(result.prob)