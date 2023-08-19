from flask import Flask, render_template

app = Flask(__name__)

# Sample pet data from pets.json
import json
with open('pets.json') as json_file:
    pets_data = json.load(json_file)

# Index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

# Pets index route
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'

# Show page route for individual pets
@app.route('/pets/<int:pet_id>')
def show_pet(pet_id):
    pet = next((pet for pet in pets_data if pet['pet_id'] == pet_id), None)
    if pet:
        return render_template('show_pet.html', pet=pet)
    else:
        return 'Pet not found'

# Facts create page route
@app.route('/facts/new')
def create_fact():
    return render_template('create_fact.html')

if __name__ == '__main__':
    app.run()
