import numpy as np
import pandas as pd
#import statsmodels.api as sm

def simple_heuristic():
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.
    
    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models 
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted
        
    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the 
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data. 

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic disaster.
    
    You prediction should be 78% accurate or higher.
        
    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survied or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the Titantic data that you will be working with
    at the link below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv
    '''

    predictions = {}
    df = pd.read_csv('titanic-data.csv')
    # women = df[df['Sex']=='female']
    # women_S=women[women['Survived'] == 1]
    # women_Ns=women[women['Survived'] == 0]
    # women_odd= women_Ns[women_Ns['PassengerId']%2 !=0 ]
    # len(women_Ns)
    men = df[df['Sex']=='male']
    men_S=men[men['Survived'] == 1]
    men_Ns=men[men['Survived'] == 0]
    men_Sage= men_S[men_S['Age']==9]
    print(len(men_Sage))
    men_NSage= men_Ns[men_Ns['Age']==9]
    print(len(men_NSage))
    
    #df_f=pd.concat([df_S,df_Ns])
    #df_f.to_csv('female-survive_vs_notsurvived.csv')
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
      
        # Your code here:
        # For example, let's assume that if the passenger
        # is a male, then the passenger survived.
        if passenger['Sex'] == 'male':
            predictions[passenger_id] = 0
        elif passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
    print(predictions)    
    return predictions

simple_heuristic()