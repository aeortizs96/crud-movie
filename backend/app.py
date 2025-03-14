from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL 
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'products' 

mysql = MySQL(app)
api = Api(app)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class Movie(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM movies")
        data = dictfetchall(cur)
        cur.close()
        print(type(data))
        return jsonify({'movies':data,'Method':'GET'})


    def post(self):
        data = request.get_json()
        print(data)
        name = data['name']
        description = data['description']
        price = data['price']
        image = data['image']
        category = data['category']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO movies(name,description,price,image,category) VALUES(%s, %s, %s, %s, %s)", (name,description,price,image,category))

        return jsonify({'Method':'POST', 'message': 'New movie created succesfully'})


    def put(self):
        data = request.get_json()
        print(data)
        id = data['id']
        name = data['name']
        description = data['description']
        price = data['price']
        image = data['image']
        category = data['category']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE movies SET name=%s, description=%s, price=%s, image=%s, category=%s
        WHERE id=%s 
        """, (name,description,price,image,category,id))
        return jsonify({'Method':'PUT', 'message':'Movie updated successfully'})


    def patch(self):
        data = request.get_json()
        print(data)
        id = data['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM movies WHERE id=%s", (id,))
        mysql.connection.commit()


        return jsonify({'Method':'PATCH', 'message':'Movie deleted successfully'})

api.add_resource(Movie,'/api/movies/')



if __name__ == '__main__':
    app.run(debug=True)