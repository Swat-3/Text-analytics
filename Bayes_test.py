#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:54:59 2018

@author: swat
"""
import nltk
from nltk.corpus import names
import random
split_word=[]
male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)

def name_features(word):
    split_word=list(word)
    a=[]
    import collections
    d = collections.defaultdict(int)
    for c in split_word:
        d[c] += 1
    for v in d.values():
        a.append(v)
    a.sort(reverse = True)
    if((a[0]>1.0) and split_word[-2:] == 'ie' or 'ey' ):
        return {'last_letters': ''.join(split_word[-2:])},'nickname' 
    else:
        return {'last_letters': ''.join(split_word[-2:])},'normal name'
        #print('real')

def name_features_actual(word):
    split_word=list(word)
    a=[]
    import collections
    d = collections.defaultdict(int)
    for c in split_word:
        d[c] += 1
    for v in d.values():
        a.append(v)
    a.sort(reverse = True)
    if((a[0]>1.0)and split_word[-2:] == 'ie' or 'ey' ):
        return {'last_letters': ''.join(split_word[-2:])}
    else:
        return {'last_letters': ''.join(split_word[-2:])}
featuresets2 = [(name_features(n)) for (n,gender) in labeled_names]

train_set, test_set = featuresets2[500:], featuresets2[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(classifier.classify(name_features('Debbie'))
c=0
f=0
ans1=[]
ans1.append(classifier.classify(name_features_actual('Debbie')))
ans1.append(classifier.classify(name_features_actual('Connie')))
ans1.append(classifier.classify(name_features_actual('Mikey')))
ans1.append(classifier.classify(name_features_actual('Cicily')))
ans1.append(classifier.classify(name_features_actual('Eddie')))

for x in ans1:
    if x=='nickname':
        c=c+1
print('Nick Name Accuracy:', (c/5)*100.0)
ans2=[]
ans2.append(classifier.classify(name_features_actual('Leo')))
ans2.append(classifier.classify(name_features_actual('David')))
ans2.append(classifier.classify(name_features_actual('William')))
ans2.append(classifier.classify(name_features_actual('Sherman')))
ans2.append(classifier.classify(name_features_actual('Katie')))

for x in ans2:
    if x=='normal name':
        f=f+1
print('Normal Name Accuracy:',(f/5)*100.0)



