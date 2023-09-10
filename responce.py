import pickle
model = pickle.load(open("heart-disease.pkl", "rb"))
def prediction(parameter):
    ans=model.predict(parameter)
    if ans==[1]:
        return 'Heart Disease'
    else:
        return 'Not Heart Disease'
if __name__ == '__main__':
    test=[[63,1,3,145,233,1,0,150,0,2.3,0,0,1]]
    ans=model.predict(test)
    print(prediction(test))
