from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String, unique=False, nullable=True)
    lastname = db.Column(db.String, unique=False, nullable=True)
   

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname}


class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(), nullable=True)
    department = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'<Admin {self.name, self.department}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "title": self.title,
            "department": self.department}


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url_1 = db.Column(db.String(), nullable=False)
    image_url_2 = db.Column(db.String(), nullable=False)
    ingredient_1_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_1_id = db.relationship('Ingredients', foreign_keys=[ingredient_1_id])
    ingredient_2_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_2_id = db.relationship('Ingredients', foreign_keys=[ingredient_2_id])
    ingredient_3_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_3_id = db.relationship('Ingredients', foreign_keys=[ingredient_3_id])
    ingredient_4_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_4_id = db.relationship('Ingredients', foreign_keys=[ingredient_4_id])
    ingredient_5_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_5_id = db.relationship('Ingredients', foreign_keys=[ingredient_5_id])
    ingredient_6_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_6_id = db.relationship('Ingredients', foreign_keys=[ingredient_6_id])
    ingredient_7_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_7_id = db.relationship('Ingredients', foreign_keys=[ingredient_7_id])
    ingredient_8_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_8_id = db.relationship('Ingredients', foreign_keys=[ingredient_8_id])
    ingredient_9_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_9_id = db.relationship('Ingredients', foreign_keys=[ingredient_9_id])
    ingredient_10_id = db.Column(db.Integer(), db.ForeignKey('ingredients.id'))
    to_ingredient_10_id = db.relationship('Ingredients', foreign_keys=[ingredient_10_id])


    def __repr__(self):
        return f'<Product {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "image_url_1": self.image_url_1,
            "image_url_2": self.image_url_2,
            "ingredient_1_id": self.ingredient_1_id,
            "ingredient_2_id": self.ingredient_2_id,
            "ingredient_3_id": self.ingredient_3_id,
            "ingredient_4_id": self.ingredient_4_id,
            "ingredient_5_id": self.ingredient_5_id,
            "ingredient_6_id": self.ingredient_6_id,
            "ingredient_7_id": self.ingredient_7_id,
            "ingredient_8_id": self.ingredient_8_id,
            "ingredient_9_id": self.ingredient_9_id,
            "ingredient_10_id": self.ingredient_10_id}


class Allergies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Allergies {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name }


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(), nullable=False)
    allergies_id = db.Column(db.Integer(), db.ForeignKey('allergies.id'))
    to_allergies_id = db.relationship('Allergies', foreign_keys=[allergies_id])
    supplier_id = db.Column(db.Integer(), db.ForeignKey('suppliers.id'))
    to_supplier_id = db.relationship('Suppliers', foreign_keys=[supplier_id])
    price = db.Column(db.Integer(), nullable=True)
    in_stock = db.Column(db.Boolean(), unique=False, nullable=True)

    def __repr__(self):
        return f'<{self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "allergies_id": self.allergies_id,
            "supplier_id": self.supplier_id,
            "price": self.price,
            "in_stock": self.in_stock}
    
    def public_serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "allergies_id": self.allergies_id}
    

class Suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=True)
    last_delivery = db.Column(db.String(), unique=False, nullable=True)

    def __repr__(self):
        return f'<Supplier {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "email": self.email,
            "last_delivery": self.last_delivery }
    
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_address = db.Column(db.String(200), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Order {self.customer_name, self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "customer_email": self.customer_email,
            "customer_address": self.customer_address,
            "total_price": self.total_price,
            "status": self.status
        }