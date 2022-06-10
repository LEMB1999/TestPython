from flask import Flask,jsonify,request,session
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine,update,delete,select
from models import *
from datetime import datetime
from flask_bcrypt import Bcrypt

engine = create_engine('postgresql+psycopg2://postgres:IbFNAn1VCuTyBlP@localhost:3306/API_INFO')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = "ZQhLWRGpV2Zfcr8"


@app.route("/login",methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]
    with Session(engine) as conn:
        user = conn.execute(
             select(User).where(User.email == email)
        ).fetchone()
        if bcrypt.check_password_hash(user[0].password , password ):
            session["user"] = {"id_user":user[0].id , "role":user[0].role} 
            return jsonify({
                "message":"welcome {0}".format(user[0].first_name)
            })
        else:
            return jsonify({
                "message":"the credentials are incorrect"
            })
        
@app.route("/logout",methods=["DELETE"])
def logout():
    session.pop('info',default=None)
    return jsonify({
        "message":"See you"
    })


@app.route("/users",methods=["GET"])
def getUsers():
    if "info" in session and session["info"].role == "admin":
        with Session(engine) as conn:
            users = conn.execute(select(User.email, User.first_name,User.last_name)).all()
            users = [ {"email":user[0],"first_name":user[1],"last_name":user[2]} for user in users ]
        return jsonify({
            "users": users
        })
    else:
        return jsonify({
            "message": "Unauthorized request"
        })

@app.route("/user/<int:id_user>",methods=["GET"])
def getUser(id_user):
    if "user" in session and session["user"].role == "admin":
        with Session(engine) as conn:
            user = conn.execute(
                select(User).where(User.id == id_user)
            ).fetchone()
            
        return jsonify({
            "user":user[0].serialize()
        })
    else:
        return jsonify({
            "message": "Unauthorized request"
        })

@app.route("/user",methods=["POST"])
def addUser():
    if "user" in session and session["user"].role == "admin":
        #validate the info
        #save the new user
        with Session(engine) as conn:
            user = User(
                email = request.json["email"],
                password = bcrypt.generate_password_hash(request.json["password"]).decode("utf-8"),
                first_name = request.json["first_name"],
                last_name = request.json["last_name"],
                photo = request.json["photo"],
                role = request.json["role"]
            )

            conn.add(user)
            conn.commit()

            return jsonify({
                "message":"User added",
                "user": user.serialize()
            })
    else:
        return jsonify({
            "message": "Unauthorized request"
        })

@app.route("/user/<int:id_user>",methods=["PUT"])
def editUser(id_user):
    if "user" in session and session["user"].role == "admin":
        #update the user
        with Session(engine) as conn:

            fields = {}
            #validate if the fields are correct
            for field in request.json:
                fields[field] = request.json[field]

            conn.execute(
                update(User).
                where(User.id == id_user).
                values(fields)
            )
            
            conn.commit()

        return jsonify({
            "message":"User was updated"
        })
    else:
        return jsonify({
            "message": "Unauthorized request"
        })

@app.route("/user/<int:id_user>",methods=["DELETE"])
def deleteUser(id_user):
    if "user" in session and session["user"].role == "admin":
        with Session(engine) as conn:
            
            conn.execute(
                delete(User).
                where(User.id == id_user)
            )

            conn.commit()

        return jsonify({
            "message":"User was deleted"
        })
    else:
        return jsonify({
            "message": "Unauthorized request"
        })


@app.route("/publications",methods=["GET"])
def getPublications():
    if "user" in session:
        with Session(engine) as conn:
            publications = conn.execute(
                select(Publication).where(Publication.id_user == session["user"].id)
            ).all()
        
        publications = [ list(publication) for publication in publications]

    return jsonify({
        "publications":publications
    })

@app.route("/publication<int:id_publication>",methods=["GET"])
def getPublication(id_publication):
    if "user" in session:
         with Session(engine) as conn:
            publication = conn.execute(
                select(Publication).where(Publication.id == id_publication)
            ).fetchone()

            if publication[0].id_user == session["user"].id:
                return jsonify({
                    "publication": publication[0].serialize()
                })
            else:
                return jsonify({
                    "message": "Unauthorized request"
                })


@app.route("/publication", methods=["POST"])
def addPublication():
    if "user" in session:
        #save the new publication
        with Session(engine) as conn:
            
            publication = Publication(
                title = request.json['title'],
                description = request.json['description'],
                priority = request.json['priority'],
                status = request.json['status'],
                published = request.json['published'],
                created_at = datetime.now(),
                user_id = session["user"].id
            )

            conn.add(publication)
            conn.commit()

        return jsonify({
            "message":"Publication added",
            "publication": publication.serialize()
        })
    else:
        return jsonify({
            "message":"Please login to continue with the process",
        })

@app.route("/publication/<int:id_publication>",methods=["PUT"])
def editPublication(id_publication):
    if "user" in session:
        #update the user
        with Session(engine) as conn:

            fields = {}
            #validate if the fields are correct
            for field in request.json:
                fields[field] = request.json[field]

            publication = conn.execute(
                select(Publication).where(Publication.id == id_publication)
            ).fetchone()

            if publication[0].id_user == session["user"].id:
                conn.execute(
                    update(Publication).
                    where(Publication.id == id_publication ).
                    values(fields)
                )
            
                conn.commit()
                return jsonify({
                    "message":"Publication was updated"
                })
            else:
                return jsonify({
                    "message":"Unauthorized request"
                })


        

@app.route("/publication<int:id_publication>", methods=["DELETE"])
def deletePublication(id_publication):

    with Session(engine) as conn:
        
        publication = conn.execute(
            select(Publication).where(Publication.id == id_publication)
        ).fetchone()

        if publication[0].id_user == session["user"].id:
            conn.execute(
                delete(Publication).
                where(Publication.id == id_publication)
            )

            conn.commit()

            return jsonify({
                "message":"The publication was deleted"
            })
        else:
            return jsonify({
                "message":"Unauthorized request"
            })

if __name__ == '__main__':
    app.run(debug=True,port=3000)