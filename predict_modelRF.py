import random
import numpy as np      
import pandas as pd  


filename = 'Disney_data.csv'
df = pd.read_csv(filename, header=0)   
print(f"{filename} : file read into a pandas dataframe.")

Characters=['Aladdin','Alice','Anna','Ariel','Aurora','Beast','Belle',
            'Cinderella','Elsa','Eric','Flynn Rider','Hercules','Jasmine',
            'Kristoff','Li Shang','Merida','Moana','Mulan','Perter Pan',
            'Prince Charming','Pocahontas','Rapunzel','Raya','Snow White','Tiana' ]
Characters_INDEX={'Aladdin':0,'Alice':1,'Anna':2,'Ariel':3,'Aurora':4,'Beast':5,'Belle':6,
            'Cinderella':7,'Elsa':8,'Eric':9,'Flynn Rider':10,'Hercules':11,'Jasmine':12,
            'Kristoff':13,'Li Shang':14,'Merida':15,'Moana':16,'Mulan':17,'Perter Pan':18,
            'Prince Charming':19,'Pocahontas':20,'Rapunzel':21,'Raya':22,'Snow White':23,'Tiana':24}


def convert_characters(characters):
    """ return the species index (a unique integer/category) """
    return Characters_INDEX[characters]


df['Name']=df['Name'].apply(convert_characters).copy()

SEX=['Male','Female']
SEX_INDEX={'Male':1,'Female':0}

def convert_sex(sex):
    """ return the species index (a unique integer/category) """
    return SEX_INDEX[sex]

df['Sex']=df['Sex'].apply(convert_sex).copy()

Zodiac_Signs=['Aries','Taurus','Gemini','Cancer','Leo','Virgo',
              'Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']
Zodiac_Signs_INDEX={'Aries':3,'Taurus':4,'Gemini':5,'Cancer':6,'Leo':7,'Virgo':8,
              'Libra':9,'Scorpio':10,'Sagittarius':11,'Capricorn':12,'Aquarius':1,'Pisces':2}

def convert_ZS(zs):
    """ return the species index (a unique integer/category) """
    return Zodiac_Signs_INDEX[zs]

df['Zodiac Signs']=df['Zodiac Signs'].apply(convert_ZS).copy()

df_final=df.copy()
df_final['Character'] = df['Name']
df_final=df_final.drop('Name', axis=1)

A = df_final.values 
NUM_ROWS, NUM_COLS = A.shape
COLUMNS = df_final.columns 
COL_INDEX = {}
for i, name in enumerate(COLUMNS):
    COL_INDEX[name] = i

X_all = A[:,0:13].copy() 
y_all = A[:,13].copy() 
indices = np.random.permutation(len(y_all))
X_labeled = X_all[indices]              
y_labeled = y_all[indices]              


NUM_ROWS = X_labeled.shape[0]    
TEST_PERCENT = 0.20
TEST_SIZE = int(TEST_PERCENT*NUM_ROWS)   

X_test = X_labeled[:TEST_SIZE]   
y_test = y_labeled[:TEST_SIZE]

X_train = X_labeled[TEST_SIZE:]  
y_train = y_labeled[TEST_SIZE:]


# Create a RF model and train it! 
#
from sklearn import tree     
from sklearn import ensemble  



from sklearn.model_selection import cross_val_score

best_depth = 0   
best_num_trees = 0
best_acc= 0


for ntrees in range(50,200,50):
    
    for d in range(1,6):
        rforest_model = ensemble.RandomForestClassifier(max_depth=d, 
                                                        n_estimators=ntrees)
        cv_scores = cross_val_score( rforest_model, X_train, y_train, cv=5 ) # 5 means 80/20 split
        # print(cv_scores)  # if we want to see the five individual scores 
        average_cv_accuracy = cv_scores.mean()  # more likely, only their average
        if average_cv_accuracy>best_acc:
            best_acc=average_cv_accuracy
            best_depth= d
            best_num_trees= ntrees

rforest_model_tuned = ensemble.RandomForestClassifier(max_depth=best_depth, 
                                                      n_estimators=best_num_trees)
rforest_model_tuned.fit(X_train, y_train)

rforest_model_final = ensemble.RandomForestClassifier(max_depth=best_depth, 
                                                      n_estimators=best_num_trees)
rforest_model_final.fit(X_all, y_all)  


def predictive_modelRF( Features ):
    """ input: a list of four features 
        output: the predicted species of iris, from
    """
    our_features = np.asarray([Features])                 # extra brackets needed
    predicted_characters_RF = rforest_model_final.predict(our_features)
    
    predicted_characters_RF = int(round(predicted_characters_RF[0]))  # unpack one element
    name = Characters[predicted_characters_RF]
    return f"{name} ({predicted_characters_RF})"

def predictive_modelRF_image( Features ):
    """ input: a list of four features 
        output: the predicted species of iris, from
    """
    our_features = np.asarray([Features])                 # extra brackets needed
    predicted_characters_RF = rforest_model_final.predict(our_features)
    
    predicted_characters_RF = int(round(predicted_characters_RF[0]))  # unpack one element
    return predicted_characters_RF

Features =[0,170, 29, 2, 65,105,220, 22,180,115,40,255,150]
result = predictive_modelRF( Features )
print(result)
