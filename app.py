
from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__,template_folder='Template')
filename="model.pkl"
fileobj=open(filename,'rb')
b= pickle.load(fileobj)



@app.route("/")
def seema():
    return render_template('machine.html')

@app.route("/murlidhar",methods=['GET','POST'])
def murlidhar():
    if request.method=='POST':
        gender=request.form['gender']
        married=request.form['married']
        dependents=request.form['dependents']
        education=request.form['education']
        employed=request.form['employed']
        credit=float(request.form['credit'])
        area=request.form['area']
        loan=request.form['loan']
        ApplicantIncome=float(request.form['ApplicantIncome'])
        CoapplicantIncome=float(request.form['CoapplicantIncome'])
        LoanAmount=float(request.form['ApplicantIncome'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])

        #gender
        if(gender=="Male"):
            male=1
        else:
            male=0

        #married
        if(married=="Yes"):
            married_Yes=1
        else:
            married_Yes=0
        
        #dependents
        if(dependents=='1'):
            dependents_1=1
            dependents_2=0
            dependents_3=0
        elif(dependents=='2'):
            dependents_1=0
            dependents_2=1
            dependents_3=0
        elif(dependents=="3+"):
            dependents_1=0
            dependents_2=0
            dependents_3=1
        else:
            dependents_1=0
            dependents_2=0
            dependents_3=0
        
        #education
        if(education=="Not Graduate"):
            not_graduate=1
        else:
            not_graduate=0
        
        #employed
        if(employed=="Yes"):
            employed_Yes=1
        else:
            employed_Yes=0
        
        #property area
        if(area=="Semiurban"):
            semiurban=1
            urban=0
        elif(area=="Urban"):
            semiurban=0
            urban=1
        else:
            semiurban=0
            urban=0

        #Loan status
        if(loan=="Y"):
            loan_y=1
        else:
            loan_y=0
        
        ApplicantIncomelog=np.log(ApplicantIncome)
        totalincomelog=np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountlog=np.log(LoanAmount)
        Loan_Amount_Termlog=np.log(Loan_Amount_Term)

        prediction=b.predict([[credit,ApplicantIncomelog,totalincomelog,LoanAmountlog,Loan_Amount_Termlog,male,married_Yes,dependents_1,dependents_2,dependents_3,not_graduate,employed_Yes,semiurban,urban]])
        
        #Print(prediction)
        if(prediction=="N"):
            prediction="You are not Eligible for Getting Loan"
        else:
            prediction="You are Eligible for Getting Loan"

        return render_template("form.html",prediction_text="loan status is {}".format(prediction))


    else:
        return render_template('form.html')
        

        
if __name__=='__main__':
    app.run(debug=True, port=5)
