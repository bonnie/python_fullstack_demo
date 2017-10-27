from flask import Flask, render_template
from model import Pet, Owner, db, connect_to_db

app = Flask(__name__)

@app.route('/')
def show_index():
    """Show index table of pets."""

    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/pet/<int:id>')
def show_pet_data(id):
    """Show details for pet with the specified id."""

    pet = Pet.query.get(id)
    return render_template('pet_detail.html', pet=pet)

if __name__ == '__main__':

    connect_to_db(app)
    app.run(debug=True)
