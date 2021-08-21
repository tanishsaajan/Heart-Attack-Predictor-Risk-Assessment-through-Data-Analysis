from flask import Flask, render_template, request
import pickle
import numpy as np

lgc= pickle.load(open('heartfinal.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('new.html')


@app.route('/predict', methods=['POST'])
def predict():
        age = int(request.form['age'])
        sex = str(request.form['sex'])
        cp = str(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = str(request.form['chol'])
        fbs = str(request.form['fbs'])
        thalach = int(request.form['thalach'])
        exang = str(request.form['exang'])
        ca = str(request.form['ca'])
        thal = str(request.form['thal']) 
        
        if(sex == '0'):
            sex_0=0
            sex_1 = 0
        else:
            sex_0 = 1
            sex_1 = 0

        
        cp_0 = 0
        cp_1 = 0
        cp_2 = 0
        cp_3 = 0
        if(cp == '0'):
            cp_0 = 1
        elif(cp == '1'):
            cp_1 = 1
        elif(cp == '2'):
            cp_2 = 1
        else:
            cp_3 = 1


        if(fbs == '0'):
            fbs_0 = 1
            fbs_1 = 0
        else:
            fbs_0 = 0
            fbs_1 = 1


        if(exang == '0'):
            exang_0 = 1
            exang_1 = 0
        else:
            exang_0 = 0
            exang_1 = 1

        
        ca_0 = 0
        ca_1 = 0
        ca_2 = 0
        ca_3 = 0
        ca_4 = 0

        if(ca == '0'):
            ca_0 = 1
        elif(ca == '1'):
            ca_1 = 1
        elif(ca == '2'):
            ca_2 = 1
        elif(ca == '3'):
            ca_3 = 1
        else:
            ca_4 = 1


        thal_0 = 0
        thal_1 = 0
        thal_2 = 0
        thal_3 = 0
        if(thal == '0'):
            thal_0 = 1
        elif(thal == '1'):
            thal_1 = 1
        elif(thal == '2'):
            thal_2 = 1
        else:
            thal_3 = 1  
        result = np.array([[int(age), int(trestbps), int(chol), int(thalach), int(sex_0), int(sex_1), int(cp_0), int(cp_1), int(cp_2), int(cp_3), int(fbs_0), int(fbs_1), int(exang_0), int(exang_1), int(ca_0), int(ca_1), int(ca_2), int(ca_3), int(ca_4), int(thal_0), int(thal_1), int(thal_2), int(thal_3)]])
        #result = np.array([[57, 140, 240, 162, 1.6, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]])
        print(result.dtype)

        pred = lgc.predict_proba(result)
        predd=lgc.predict(result)
        output='{0:.{1}f}'.format(pred[0][1], 2)
        f=float(output)
        p=f*100
        if output>str(0.5):
            return render_template('after.html',prediction=predd,prediction_text='\n Probability of Getting a Heart Attack is {}%'.format(p))
        else:
            return render_template('after.html',prediction=predd,prediction_text='\n Probability Not Getting a Heart Attack is {}%'.format(p))
    

if __name__ == '__main__':
    app.run(debug = True)























    #int_features= [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #pred = clf.predict(final_features)
    ###output='{0:.{1}f}'.format(pred[0][1], 2)
    ###if output>str(0.5):
    #return render_template('after.html',prediction = pred)
    ###else:
        ###return render_template('after.html',prediction_text='\n Probability of fire  not occuring is {}'.format(output))
    ###return render_template('after.html',data=pred)
    ###if pred==1:
        ###return render_template('after.html',data=pred)
    ###else:
       ## return render_template('after.html',prediction_text='No Heart Attack'.format(pred))


#if __name__ == "__main__":
 #   app.run(debug=True)