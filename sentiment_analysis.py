# Copyright 2016, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sentiment_tutorial]
"""Demonstrates how to make a simple call to the Natural Language API."""

# [START sentiment_tutorial_import]
import argparse
import csv
import random 
import codecs

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# [END sentiment_tutorial_import]


# [START def_print_result]
def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))
    

        
    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0
# [END def_print_result]


# [START def_analyze]
def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    
    '''
    '''
    sentiment = client.analyze_sentiment(document).document_sentiment
    # 이 py파일과 같은 경로에 위치한 csv파일을 불러온다 
    f = codecs.open('sadSentence.csv','r',encoding='utf-8')
    f2 = codecs.open('goodSentence.csv','r',encoding='utf-8')
    rdr = csv.reader(f)
    rdr2 = csv.reader(f2)
    #count=1
    
    if sentiment.score<0:
        i = random.randrange(0,7)
        j = 0
        for line in rdr:
            if (j==i):
                print(line)
            j = j+1
        
    else:
        i = random.randrange(0,7)
        j = 0 
        for line in rdr2:
            if(j==i):
                print(line)
            j = j+1
    '''
    '''
    # Print the results
    print_result(annotations)
# [END def_analyze]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'movie_review_filename',
        help='The filename of the movie review you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.movie_review_filename)
# [END sentiment_tutorial]
