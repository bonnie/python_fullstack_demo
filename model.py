from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Species(db.Model):
    """Class for pet species options."""

    __tablename__ = 'species'

    species_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    species_name = db.Column(db.Text, nullable=False)

class Pet(db.Model):
    """Class for a pet object."""

    __tablename__ = 'pets'

    pet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pet_name = db.Column(db.Text, nullable=False)
    born_at = db.Column(db.Date)
    species_id = db.Column(db.Integer, db.ForeignKey('species.species_id'))

    species = db.relationship('Species')
    owners = db.relationship('Owner', secondary='petowners', backref='pets')

class Owner(db.Model):
    """Owners of pets."""

    __tablename__ = 'owners'

    owner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    owner_name = db.Column(db.Text, nullable=False)

class PetOwner(db.Model):
    """Association between pets and owners."""

    __tablename__ = 'petowners'

    petowner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.owner_id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'))


def connect_to_db(app, db_uri='postgresql:///python_pets'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == '__main__':

    from server import app

    connect_to_db(app)
    db.drop_all()
    db.create_all()

    print "connected to DB"
