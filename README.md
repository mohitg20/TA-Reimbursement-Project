# TA-Reimbursement-Project

CS253 Course Project

COURSE PROJECT NAME-: TA Reimbursement-Project

TA-Reimbursement-Project contain source code folder named TA_reimbursementProject,
which comprises of-:
1. home folder -: Which is the app of our project maintaining various files namely -:
    (i) admin.py -: used to register various models of our project.
    (ii) models.py -: which maintain various models(class implementation) of our project.
    (iii) urls.py -: maintains various urls of different pages.
    (iv) views.py -: used to store different attributes/information for storing in database.
    (v) apps.py -: contains file created so as to include configuration for the app.
    (vi) forms.py -: used for user authentication

2. TA_reimbursementProject -: which is our Django project containing-:
    (i) settings.py which maintains various settings and also used for registering apps in Django project.
    (ii) urls.py which contains url to various app of our project.
    (iii) asgi.py and wsgi.py -: contains standard python source files

3. templates -: which is our HTML source files. The major files used are-:
    (i) application -: which contains Application Form
    (ii) base -: which contains common header and footer (basic layout)
    (iii) baseportal -: this contains basic formulation for standard prompt and messages which appear confirming successful, login etc.
    (iv) form -: which contains Claim Bill
    (v) index -: which is our main page
    (vi) login -: This is our login page for looging already registered user along with option for registering new users.
    (vii) register -: which is our register page for registering new users.
    (viii) status -: This is the page for viewing status of user.
    (ix) user_profile -: this is profile of registered user.
    (x) filledform -: displays the filled form

4. db.sqlite3 -: SQLITE3 File which is the standard database of Django framework.

5. manage.py -: Inbulit python file containing basic implementation of framework.

## How to Run 
Clone the repository-
```
git clone https://github.com/mohitg20/TA-Reimbursement-Project.git
cd TA_reimbursementProject
```
```
```
Install all the dependencies-
```
```
Run the server-
```
python manage.py runserver
```
Go on the localhost web address which must have been printed on the terminal
