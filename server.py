#     THIS -> _app is for getting the controller import the class NOTE
from loging_registration_app.controllers import users

from loging_registration_app import app

#     THIS -> _app is for the app folder   (loginfrom loging_registration_app) getting that code  NOTE

if __name__ == "__main__":
    app.run(debug=True)
