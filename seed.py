"""Seed the database with some pets."""

from model import Pet, Species, Owner, connect_to_db, db

def create_data(db):
    tiger = Species(species_name='tiger')
    cat = Species(species_name='cat')
    dog = Species(species_name='dog')
    db.session.add_all([tiger, cat, dog])

    astro = Pet(pet_name='Astro', born_at='1985-10-23')
    crookshanks = Pet(pet_name='Crookshanks', born_at='1985-10-23', species=cat)
    cisco = Pet(pet_name='Cisco', born_at='1999-02-01')
    lexie = Pet(pet_name='Lexie', born_at='1997-02-01')
    hobbes = Pet(pet_name='Hobbes', born_at='1990-10-23')
    db.session.add_all([astro, crookshanks, lexie, hobbes, cisco])

    astro.species = dog
    cisco.species = cat
    lexie.species = cat
    hobbes.species = tiger

    calvin = Owner(owner_name='Calvin')
    hermione = Owner(owner_name='Hermione')
    bonnie = Owner(owner_name='Bonnie')
    george = Owner(owner_name='George Jetson')
    jane = Owner(owner_name='Jane Jetson')
    db.session.add_all([bonnie, calvin, hermione, george, jane])

    bonnie.pets.extend([cisco, lexie])
    hobbes.owners.append(calvin)
    crookshanks.owners.append(hermione)
    astro.owners.extend([george, jane])

    db.session.commit()

if __name__ == '__main__':

    from server import app

    connect_to_db(app)
    create_data(db)
