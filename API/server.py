#import Environment Variables
from env import *

from flask import Flask,jsonify,request,session
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine,update,delete,select
from models import *
from datetime import datetime

#we use flask_bcrypt to encrypt the password 
import bcrypt

engine = create_engine(CONNECTION_URL_DATABASE)

app = Flask(__name__)

#configure startup app
app.config['SECRET_KEY'] = KEY_COOKIES

#---------- utilities --------------#

#this method validate the request 
def checkRequest(body,allow_fields,required_params):
        
        #validate the required fields
        for param in required_params:
            if body.get(param) == None:
                return { "passValidation":False, "info":{
                    "status":400,
                    "message":"The param {0} is required".format(param)
                }}
        #validate the fields 
        for field in body:
            if not field in allow_fields:
                return { "passValidation":False, "info":{
                    "status":400,
                    "message": "The field {0} is not known".format(field)
                }}
            #validate the type of the fields
            if not isinstance(body[field],str):
                return {"passValidation":False, "info":{
                    "status":400,
                    "message":"The param {0} its must be string".format(field)
                }}

        return {"passValidation":True}



#----------- utilities ------------ #


#------------ Auth ------------------#

@app.route("/login",methods=["POST"])
def login():
    
    #validate the body
    if request.json.get("email") == None or request.json.get("password") == None:
        return jsonify({
                "status":400,
                "message":"The email and password are required"
        })
    
    #receive the params
    email = request.json["email"]
    password = request.json["password"]

    with Session(engine) as conn:
        
        #try to get the user
        user = conn.execute(
             select(User).where(User.email == email)
        ).fetchone()

        #verify the credentials 
        if user != None and bcrypt.checkpw( password.encode("utf8") , user[0].password.encode("utf8") ):
            #we add the session to keep authentication
            session["user"] = {"id_user":user[0].id , "role":user[0].role} 
            return jsonify({
                "status":200,
                "message":"welcome {0}".format(user[0].first_name)
            })
        else:
            return jsonify({
                "status":401,
                "message":"the credentials are incorrect"
            })
        
@app.route("/logout",methods=["DELETE"])
def logout():
    #we delete the session
    session.pop('user',default=None)
    return jsonify({
        "status":200,
        "message":"See you"
    })


#----------------------- Auth ------------------#


#----------------------- User ------------------#

@app.route("/users",methods=["GET"])
def getUsers():
    #verify if the user has session and the rol is admin
    if session.get("user") != None and session["user"]["role"] == "admin":
        with Session(engine) as conn:
            #get the users of database
            users = conn.execute(select(User.email, User.first_name,User.last_name)).all()
            users = [ {"email":user[0],"first_name":user[1],"last_name":user[2]} for user in users ]
        return jsonify({
            "status":200,
            "users": users
        })
    else:
        return jsonify({
            "status": 401,
            "message": "Unauthorized request"
        })

@app.route("/user/<int:id_user>",methods=["GET"])
def getUser(id_user):
    #verify if the user has session and the rol is admin
    if session.get("user") != None and session["user"]["role"] == "admin":
        #get the user
        with Session(engine) as conn:
            #get user of database
            user = conn.execute(
                select(User).where(User.id == id_user)
            ).fetchone()
        #verify if the user exist
        if not user:
            return jsonify({
                "status":400,
                "message": "User not Found"
            })

        return jsonify({
            "status":200,
            "user":user[0].serialize()
        })

    else:
        return jsonify({
            "status":401,
            "message": "Unauthorized request"
        })


@app.route("/user",methods=["POST"])
def addUser():
    #verify if the user has session and the rol is admin
    if session.get("user") != None and session["user"]["role"] == "admin":
        #validate request
        allow_fields = ["email","password","first_name","role","photo","last_name"]
        required_params = ["email","password","first_name","role"]
        result = checkRequest(request.json,allow_fields,required_params)
        if( result["passValidation"] != True):
            return jsonify(result["info"])

        #validate the length of the info 
        for field in request.json:
            if(len(request.json[field]))>255:
                return jsonify({
                    "status": 400,
                    "message":"The {0} field only allows 255 characters".format(field)
                })
            
        #save the new user
        with Session(engine) as conn:
            user = User(
                email = request.json["email"],
                #encrypt and save the password in database
                password = bcrypt.hashpw(request.json["password"].encode("utf8"),bcrypt.gensalt()).decode("utf8"),
                first_name = request.json["first_name"],
                last_name =  request.json["last_name"] if request.json.get("last_name") != None else None,
                photo =      request.json["photo"] if request.json.get("photo") != None else None,
                role = request.json["role"]
            )

            #save user in database
            conn.add(user)
            conn.commit()

            return jsonify({
                "status":200,
                "message":"User added",
                "user": user.serialize()
            })
    else:
        return jsonify({
            "status": 401,
            "message": "Unauthorized request"
        })

@app.route("/user/<int:id_user>",methods=["PUT"])
def editUser(id_user):
    #verify if the user has session and the rol is admin
    if "user" in session and session["user"]["role"] == "admin":
        #update the user
        with Session(engine) as conn:

            #validate request
            allow_fields = ["email","password","first_name","role","photo","last_name"]
            required_params = ["email","password","first_name","role"]
            result = checkRequest(request.json,allow_fields,required_params)
            if(result["passValidation"] != True):
                return jsonify(result["info"])

            fields = {}
            #generat the objet to pass database
            for field in request.json:
                fields[field] = request.json[field]

            conn.execute(
                update(User).
                where(User.id == id_user).
                values(fields)
            )
            
            conn.commit()

        return jsonify({
            "status": 200,
            "user" : fields,
            "message":"User was updated"
        })
        
    else:
        return jsonify({
            "status": 401,
            "message": "Unauthorized request"
        })

@app.route("/user/<int:id_user>",methods=["DELETE"])
def deleteUser(id_user):

    #verify if the user has session and the rol is admin
    if "user" in session and session["user"]["role"] == "admin":
        with Session(engine) as conn:
            
            #delete user for database
            conn.execute(
                delete(User).
                where(User.id == id_user)
            )

            conn.commit()

        return jsonify({
            "status": 200,
            "message":"User was deleted"
        })
    else:
        return jsonify({
            "status": 401,
            "message": "Unauthorized request"
        })

#----------------------- User ------------------#


#---------------------- Publication ------------------#

@app.route("/publications",methods=["GET"])
def getPublications():
    if "user" in session:
        with Session(engine) as conn:
            #get the publication of the user 
            publications = conn.execute(
                select(Publication).where(Publication.id_user == session["user"]["id_user"])
            ).all()

            if len(publications) > 0:
                publications = [ publication[0].serialize() for publication in publications]
        

            return jsonify({
                "status": 200,
                "publications":publications
            })
    else:
        return jsonify({
            "status": 401,
            "message": "Please login to continue with the process"
        })


@app.route("/publication/<int:id_publication>",methods=["GET"])
def getPublication(id_publication):
    if "user" in session:
        if not isinstance(id_publication,int):
            return jsonify({
                "status":400,
                "message":"The id publication must be a integer"
        })

        with Session(engine) as conn:
            #get a specific publication
            publication = conn.execute(
                select(Publication).where(Publication.id == id_publication)
            ).fetchone()

            if publication == None:
                return jsonify({
                    "status": 400,
                    "message": "Publication not Found"
            })
                

            #validate that user has a permissions to see the publication
            if publication[0].id_user == session["user"]["id_user"]:
                return jsonify({
                    "status": 200,
                    "publication": publication[0].serialize()
                })
            else:
                 return jsonify({
                    "status": 400,
                    "publication": "Unauthorized request"
                })

    else:
        return jsonify({
            "status": 401,
            "message": "Please login to continue with the process"
        })

@app.route("/publication", methods=["POST"])
def addPublication():


    #validate the user is authenticated
    if "user" in session:

        #validate request
        allow_fields = ["title","description","priority","status","published"]
        required_params = ["title","description","priority","status"]
        result = checkRequest(request.json,allow_fields,required_params)
        if( result["passValidation"] != True):
            return jsonify(result["info"])

        status = [ "published", "pending", "deleted" ]
        priority = [ "High", "Medium", "Low" ]

        #validate priorities
        if not request.json["priority"] in priority:
            return jsonify({
                "status":400,
                "message":"The values allowed for priority are {0}".format(priority)
            })

        #validate status
        if not request.json["status"] in status:
            return jsonify({
                "status":400,
                "message":"The values allowed for status are {0}".format(status)
            })

        with Session(engine) as conn:
            publication = Publication(
                title = request.json['title'],
                description = request.json['description'],
                priority = request.json['priority'] if request.json.get("priority") != None else None,
                status = request.json['status'] ,
                published = request.json['published'] if request.json.get("published") != None else None,
                created_at = datetime.now(),
                id_user = session["user"]["id_user"]
            )

            #we save publication in database
            conn.add(publication)
            conn.commit()

            print()

            return jsonify({
                "status":200,
                "message":"Publication added",
                "publication":publication.serialize()
            })
    else:
        return jsonify({
            "status": 401,
            "message":"Please login to continue with the process",
        })

@app.route("/publication/<int:id_publication>",methods=["PUT"])
def editPublication(id_publication):

    
    #validate the user is authenticated
    if "user" in session:

        if not isinstance(id_publication,int):
            return jsonify({
                "status":400,
                "message":"The id publication must be a integer"
        })

        #validate request
        allow_fields = ["title","description","priority","status","published"]
        required_params = ["title","description","status"]
        result = checkRequest(request.json,allow_fields,required_params)
        if( result["passValidation"] != True):
            return jsonify(result["info"])

        with Session(engine) as conn:

            fields = {}
            #generate the object to save in db
            for field in request.json:
                fields[field] = request.json[field]
            
            #save when updated the publication
            fields["updated_at"] = datetime.now()

            #save changes in database
            publication = conn.execute(
                select(Publication).where(Publication.id == id_publication)
            ).fetchone()

            #validate if user its owner of publication
            if publication[0].id_user == session["user"]["id_user"]:
                #update publication
                conn.execute(
                    update(Publication).
                    where(Publication.id == id_publication ).
                    values(fields)
                )
            
                conn.commit()
                return jsonify({
                    "status": 200,
                    "publication":publication[0].serialize(),
                    "message":"Publication was updated"
                })

            else:
                return jsonify({
                    "status": 400,
                    "message":"Unauthorized request"
                })
                
    else:
        return jsonify({
            "status":401,
            "message":"Please login to continue with the process"
        })

@app.route("/publication/<int:id_publication>", methods=["DELETE"])
def deletePublication(id_publication):
    
     
    #validate the user is authenticated
    if "user" in session:
        if not isinstance(id_publication,int):
            return jsonify({
                "status":400,
                "message":"The id publication must be a integer"
            })
        with Session(engine) as conn:
            
            #get the publication in the database 
            publication = conn.execute(
                select(Publication).where(Publication.id == id_publication)
            ).fetchone()

            print(publication)
            #check if exist the publication
            if publication == None:
                return jsonify({
                    "status": 400,
                    "message":"Publication not found"
                })

            #check if the user is the owner of the publication
            if publication[0].id_user == session["user"]["id_user"]:
                conn.execute(
                    delete(Publication).
                    where(Publication.id == id_publication)
                )

                conn.commit()

                return jsonify({
                    "status": 200,
                    "message":"Publication was deleted"
                })

            else:
                return jsonify({
                    "status": 400,
                    "message":"Unauthorized request"
                })

    else:
        return jsonify({
            "status":401,
            "message":"Please login to continue with the process"
        })

#----------------------- Publication ------------------#

#check if is a principal module
if __name__ == '__main__':
    #Start the server
    app.run(debug=True,port=3000)