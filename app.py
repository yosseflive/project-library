import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from myModals import Customer, Book, Loan, db, app

CORS(app)



#views
# @app.route('/')
# def show_all():
#     res = []
#     for customer in Customer.query.all():
#         res.append({"id":customer.id, "name":customer.name, "city":customer.city, "age":customer.age,})
#     return (json.dumps(res))

@app.route('/newCustomer', methods = ['GET', 'POST'])
def new():
    request_data = request.get_json()
    name = request_data["name"]
    city = request_data["city"]
    age = request_data["age"]
    mail = request_data["mail"]
 
    newCustomer= Customer(name=name, city=city, age=age, mail=mail)
    db.session.add (newCustomer)
    db.session.commit()
    return "a new rcord was create"


# @app.route('/del/<id>', methods = ['DELETE'])
# @app.route('/del/', methods = ['DELETE'])
# def delete_customer(id=-1):
#     del_row = Customer.query.filter_by(id=id).first()
#     if del_row:
#         db.session.delete(del_row)
#         db.session.commit()
#         return "a row was delete"
#     return "no such customer..."


# @app.route('/upd/<id>', methods = ['PUT'])
# @app.route('/upd/', methods = ['PUT'])
# def update_customer(id=-1):
#     request_data = request.get_json()
#     upd_row = Customer.query.filter_by(id=id).first()
#     if upd_row:
#         upd_row.Name =request_data['Name']
#         upd_row.City =request_data["City"]
#         upd_row.Age =request_data["Age"]
#         db.session.commit()
#         return "a row was update"
#     return "no such customer...."


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug = True)