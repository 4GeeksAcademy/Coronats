"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Admins, Products, Allergies, Ingredients, Suppliers, Order
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route("/login", methods=["POST"])
def login():
    response_body = {}
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = db.session.execute(db.select(User).where(User.email == email, User.password == password, User.is_active == True)).scalar()
    print(user)
    print(user.serialize())
    if user is None:
        return jsonify({"msg": "email not registered"}) , 401
    if password != user.password:
        return jsonify({"msg": "Wrong password"}) , 401
    access_token = create_access_token(identity={'user_id': user.id, 'email': user.email})
    response_body['message'] = 'User logged in'
    response_body['access_token'] = access_token
    response_body['data'] = user.serialize()
    return jsonify(access_token=access_token)


@api.route("/signup", methods=['POST'])
def handle_signup():
    response_body = {}
    body = request.get_json()
    email = body["email"].lower()
    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(email=body["email"], password=body["password"], is_active=True)
        db.session.add(user)
        db.session.commit()
        """ name = body.get("name" , " ")
        lastname = body.get("lastname" , " ")
        full_user = User(name=name, lastname=lastname, allergies_id=1)
        db.session.add(full_user)
        db.session.commit() """
        access_token = create_access_token(identity={'user_id': user.id, 'email': user.email})
        response_body['access_token'] = access_token
        response_body['data'] = user.serialize()
        response_body['message'] = 'User created and logged in'
        return response_body , 200
    else:
        return jsonify({"msg": "User already exists"}) , 401


@api.route("/adminlogin", methods=["POST"])
def admin_login():
    response_body = {}
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    admin = db.session.execute(db.select(Admins).where(Admins.email == email, Admins.password == password)).scalar()
    print(admin)
    print(admin.serialize())
    if admin is None:
        return jsonify({"msg": "email not registered"}) , 401
    if password != admin.password:
        return jsonify({"msg": "Wrong password"}) , 401
    access_token = create_access_token(identity={'admin_id': admin.id, 'email': admin.email})
    response_body['message'] = 'Admin logged in'
    response_body['access_token'] = access_token
    response_body['data'] = admin.serialize()
    return jsonify(access_token=access_token)


@api.route("/products", methods=["GET"])
def get_products():
    response_body = {}
    rows = db.session.execute(db.select(Products)).scalars()
    results = [row.serialize() for row in rows]
    response_body['results'] = results
    response_body['message'] = 'Product list'
    return response_body, 200


@api.route("/products/<int:product_id>", methods=["GET"])
def get_product_id(product_id):
    response_body = {}
    product = db.session.execute(db.select(Products).where(Products.id == product_id)).scalar()
    if product:
        response_body['results'] = product.serialize()
        response_body['message'] = 'Product found'
        return response_body, 200
    response_body['message'] = 'Product not found'
    response_body['results'] = {}
    return response_body, 404
   

@api.route("/admin/products", methods=["POST"])
@jwt_required()
def admin_handle_products():
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'POST':
            data = request.json
            product = Products()
            product.name = data['name']
            product.description = data['description']
            product.price = data['price']
            product.category = data['category']
            product.image_url_1 = data['image_url_1']
            product.image_url_2 = data['image_url_2']
            product.ingredient_1_id = data['ingredient_1_id']
            product.ingredient_2_id = data['ingredient_2_id']
            product.ingredient_3_id = data['ingredient_3_id']
            product.ingredient_4_id = data['ingredient_4_id']
            product.ingredient_5_id = data['ingredient_5_id']
            product.ingredient_6_id = data['ingredient_6_id']
            product.ingredient_7_id = data['ingredient_7_id']
            product.ingredient_8_id = data['ingredient_8_id']
            product.ingredient_9_id = data['ingredient_9_id']
            product.ingredient_10_id = data['ingredient_10_id']
            db.session.add(product)
            db.session.commit()
            response_body['results'] = product.serialize()
            response_body['message'] = 'Product posted'
            return response_body, 200


@api.route("/admin/products/<int:product_id>", methods=["PUT" , "GET" , "DELETE"])
@jwt_required()
def admin_handle_products_id(product_id):
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'PUT':
            data = request.json
            product = db.session.execute(db.select(Products).where(Products.id == product_id)).scalar()
            if product:
                product.name = data['name']
                product.description = data['description']
                product.price = data['price']
                product.category = data['category']
                product.image_url_1 = data['image_url_1']
                product.image_url_2 = data['image_url_2']
                product.ingredient_1_id = data['ingredient_1_id']
                product.ingredient_2_id = data['ingredient_2_id']
                product.ingredient_3_id = data['ingredient_3_id']
                product.ingredient_4_id = data['ingredient_4_id']
                product.ingredient_5_id = data['ingredient_5_id']
                product.ingredient_6_id = data['ingredient_6_id']
                product.ingredient_7_id = data['ingredient_7_id']
                product.ingredient_8_id = data['ingredient_8_id']
                product.ingredient_9_id = data['ingredient_9_id']
                product.ingredient_10_id = data['ingredient_10_id']
                db.session.commit()
                response_body['message'] = 'Product updated'
                response_body['results'] = product.serialize()
                return response_body, 200
            response_body['message'] = 'Product not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'GET':
            product = db.session.execute(db.select(Products).where(Products.id == product_id)).scalar()
            if product:
                response_body['results'] = product.serialize()
                response_body['message'] = 'Product found'
                return response_body, 200
            response_body['message'] = 'Product not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'DELETE':
            product = db.session.execute(db.select(Products).where(Products.id == product_id)).scalar()
            if product:
                db.session.commit()
                response_body['message'] = 'Product deleted'
                response_body['results'] = {}
                return response_body, 200
            response_body['message'] = 'Product not found'
            response_body['results'] = {}
            return response_body, 200
    

@api.route("/ingredients", methods=["GET"])
def get_ingredients():
    response_body = {}
    rows = db.session.execute(db.select(Ingredients)).scalars()
    results = [row.serialize() for row in rows]
    response_body['results'] = results
    response_body['message'] = 'Ingredients list'
    return response_body, 200


@api.route("/ingredients/<int:ingredient_id>", methods=["GET"])
def get_ingredient_id(ingredient_id):
    response_body = {}
    ingredient = db.session.execute(db.select(Ingredients).where(Ingredients.id == ingredient_id)).scalar()
    if ingredient:
        response_body['results'] = ingredient.serialize()
        response_body['message'] = 'Ingredient found'
        return response_body, 200
    response_body['message'] = 'Ingredient not found'
    response_body['results'] = {}
    return response_body, 404
   

@api.route("/admin/ingredients", methods=["POST"])
@jwt_required()
def admin_handle_ingredient():
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'POST':
            data = request.json
            ingredient = Ingredients()
            ingredient.name = data['name']
            ingredient.description = data['description']
            ingredient.allergies_id = data['allergies_id']
            ingredient.supplier_id = data['supplier_id']
            ingredient.price = data['price']
            ingredient.in_stock = data['in_stock']
            db.session.add(ingredient)
            db.session.commit()
            response_body['results'] = ingredient.serialize()
            response_body['message'] = 'Ingredient posted'
            return response_body, 200


@api.route("/admin/ingredients/<int:ingredient_id>", methods=["PUT" , "GET" , "DELETE"])
@jwt_required()
def admin_handle_ingredients_id(ingredient_id):
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'PUT':
            data = request.json
            ingredient = db.session.execute(db.select(Ingredients).where(Ingredients.id == ingredient_id)).scalar()
            if ingredient:
                ingredient.name = data['name']
                ingredient.description = data['description']
                ingredient.allergies_id = data['allergies_id']
                ingredient.supplier_id = data['supplier_id']
                ingredient.price = data['price']
                ingredient.in_stock = data['in_stock']
                db.session.commit()
                response_body['message'] = 'Ingredient updated'
                response_body['results'] = ingredient.serialize()
                return response_body, 200
            response_body['message'] = 'Ingredient not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'GET':
            ingredient = db.session.execute(db.select(Ingredients).where(Ingredients.id == ingredient_id)).scalar()
            if ingredient:
                response_body['results'] = ingredient.serialize()
                response_body['message'] = 'Ingredient found'
                return response_body, 200
            response_body['message'] = 'Ingredient not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'DELETE':
            ingredient = db.session.execute(db.select(Ingredients).where(Ingredients.id == ingredient_id)).scalar()
            if ingredient:
                db.session.commit()
                response_body['message'] = 'Ingredient deleted'
                response_body['results'] = {}
                return response_body, 200
            response_body['message'] = 'Ingredient not found'
            response_body['results'] = {}
            return response_body, 200
    response_body['message'] = 'Unathorized user'
    return response_body, 404


@api.route("/allergies", methods=["GET"])
def get_allergies():
    response_body = {}
    rows = db.session.execute(db.select(Allergies)).scalars()
    results = [row.serialize() for row in rows]
    response_body['results'] = results
    response_body['message'] = 'Allergies list'
    return response_body, 200


@api.route("/allergies/<int:allergy_id>", methods=["GET"])
def get_allergy_id(allergy_id):
    response_body = {}
    allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
    if allergy:
        response_body['results'] = allergy.serialize()
        response_body['message'] = 'Allergy found'
        return response_body, 200
    response_body['message'] = 'Allergy not found'
    response_body['results'] = {}
    return response_body, 404
   

@api.route("/admin/allergies", methods=["POST"])
@jwt_required()
def admin_handle_allergies():
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'POST':
            data = request.json
            allergy = Allergies()
            allergy.name = data['name']
            db.session.add(allergy)
            db.session.commit()
            response_body['results'] = allergy.serialize()
            response_body['message'] = 'Allergy posted'
            return response_body, 200
    response_body['message'] = 'Unathorized user'
    return response_body, 404


@api.route("/admin/allergies/<int:allergy_id>", methods=["PUT" , "GET" , "DELETE"])
@jwt_required()
def admin_handle_allergies_id(allergy_id):
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'PUT':
            data = request.json
            allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
            if allergy:
                allergy.name = data['name']
                db.session.commit()
                response_body['message'] = 'Allergy updated'
                response_body['results'] = allergy.serialize()
                return response_body, 200
            response_body['message'] = 'Allergy not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'GET':
            allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
            if allergy:
                response_body['results'] = allergy.serialize()
                response_body['message'] = 'Allergy found'
                return response_body, 200
            response_body['message'] = 'Allergy not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'DELETE':
            allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
            if allergy:
                db.session.commit()
                response_body['message'] = 'Allergy deleted'
                response_body['results'] = {}
                return response_body, 200
            response_body['message'] = 'Allergy not found'
            response_body['results'] = {}
            return response_body, 200
    response_body['message'] = 'Unathorized user'
    return response_body, 404
    

@api.route("/admin/suppliers", methods=["POST", "GET"])
@jwt_required()
def admin_handle_supplier():
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'POST':
            data = request.json
            supplier = Suppliers()
            supplier.name = data['name']
            supplier.number = data['number']
            supplier.email = data['email']
            supplier.last_delivery = data['last_delivery']
            db.session.add(supplier)
            db.session.commit()
            response_body['results'] = supplier.serialize()
            response_body['message'] = 'Supplier posted'
            return response_body, 200
        if request.method == "GET":
            rows = db.session.execute(db.select(Suppliers)).scalars()
            results = [row.serialize() for row in rows]
            response_body['results'] = results
            response_body['message'] = 'Supplier list'
            return response_body, 200
    response_body['message'] = 'Unathorized user'
    return response_body, 404


@api.route("/admin/suppliers/<int:supplier_id>", methods=["PUT" , "GET" , "DELETE"])
@jwt_required()
def admin_handle_suppliers_id(supplier_id):
    admin_info = get_jwt_identity()
    response_body = {}
    if admin_info['admin_id']:
        if request.method == 'PUT':
            data = request.json
            supplier = db.session.execute(db.select(Suppliers).where(Suppliers.id == supplier_id)).scalar()
            if supplier:
                supplier.name = data['name']
                supplier.number = data['number']
                supplier.email = data['email']
                supplier.last_delivery = data['last_delivery']
                db.session.commit()
                response_body['message'] = 'Supplier updated'
                response_body['results'] = supplier.serialize()
                return response_body, 200
            response_body['message'] = 'Supplier not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'GET':
            supplier = db.session.execute(db.select(Suppliers).where(Suppliers.id == supplier_id)).scalar()
            if supplier:
                response_body['results'] = supplier.serialize()
                response_body['message'] = 'Supplier found'
                return response_body, 200
            response_body['message'] = 'Supplier not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'DELETE':
            supplier = db.session.execute(db.select(Suppliers).where(Suppliers.id == supplier_id)).scalar()
            if supplier:
                db.session.commit()
                response_body['message'] = 'Supplier deleted'
                response_body['results'] = {}
                return response_body, 200
            response_body['message'] = 'Supplier not found'
            response_body['results'] = {}
            return response_body, 200
    response_body['message'] = 'Unathorized user'
    return response_body, 404
    

""" @api.route("/order/<int:order_id>", methods=["PUT" , "GET" , "DELETE"])
@jwt_required()
def handle_order(order_id):
    user_info = get_jwt_identity()
    response_body = {}
    user = user_info['user_id']
    if admin_info['admin_id']:
        if request.method == 'PUT':
            data = request.json
            allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
            if allergy:
                allergy.name = data['name']
                db.session.commit()
                response_body['message'] = 'Allergy updated'
                response_body['results'] = allergy.serialize()
                return response_body, 200
            response_body['message'] = 'Allergy not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'GET':
            allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
            if allergy:
                response_body['results'] = allergy.serialize()
                response_body['message'] = 'Allergy found'
                return response_body, 200
            response_body['message'] = 'Allergy not found'
            response_body['results'] = {}
            return response_body, 404
        if request.method == 'DELETE':
            allergy = db.session.execute(db.select(Allergies).where(Allergies.id == allergy_id)).scalar()
            if allergy:
                db.session.commit()
                response_body['message'] = 'Allergy deleted'
                response_body['results'] = {}
                return response_body, 200
            response_body['message'] = 'Allergy not found'
            response_body['results'] = {}
            return response_body, 200
    response_body['message'] = 'Unathorized user'
    return response_body, 404
     """