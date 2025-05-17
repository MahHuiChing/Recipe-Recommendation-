import sqlite3

def create_and_populate_db():
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS Recipe_Ingredients')
    cursor.execute('DROP TABLE IF EXISTS Recipes')
    cursor.execute('DROP TABLE IF EXISTS Ingredients')
    cursor.execute('DROP TABLE IF EXISTS Allergens')

    cursor.execute('''
        CREATE TABLE Recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cuisine TEXT NOT NULL,
            meal TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE Ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            vegetarian BOOLEAN NOT NULL,
            lacto_vegetarian BOOLEAN NOT NULL,
            lacto_ovo_vegetarian BOOLEAN NOT NULL,
            allergens TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE Recipe_Ingredients (
            recipe_id INTEGER,
            ingredient_id INTEGER,
            FOREIGN KEY (recipe_id) REFERENCES Recipes (id),
            FOREIGN KEY (ingredient_id) REFERENCES Ingredients (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE Allergens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.executemany('''
        INSERT INTO Recipes (name, cuisine, meal) VALUES (?, ?, ?)
    ''', [
        ('Spaghetti Carbonara', 'Western', 'Dinner'),
        ('Veggie Stir Fry', 'Asian', 'Dinner'),
        ('Pancakes', 'Western', 'Breakfast'),
        ('Miso Soup', 'Asian', 'Lunch')
    ])

    cursor.executemany('''
        INSERT INTO Ingredients (name, vegetarian, lacto_vegetarian, lacto_ovo_vegetarian, allergens) VALUES (?, ?, ?, ?, ?)
    ''', [
        ('Spaghetti', True, True, True, None),
        ('Eggs', True, True, True, 'Eggs'),
        ('Parmesan Cheese', True, True, True, 'Dairy'),
        ('Pancetta', False, False, False, None),
        ('Veggie Mix', True, True, True, 'Soy'),
        ('Flour', True, True, True, None),
        ('Miso Paste', True, True, True, 'Soy'),
        ('Tofu', True, True, True, 'Soy'),
        ('Seaweed', True, True, True, None)
    ])

    cursor.executemany('''
        INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id) VALUES (?, ?)
    ''', [
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 5),
        (3, 2), (3, 6),
        (4, 7), (4, 8), (4, 9)
    ])

    cursor.executemany('''
        INSERT INTO Allergens (name) VALUES (?)
    ''', [
        ('Peanuts'), ('Eggs'), ('Soy'), ('Shellfish')
    ])

    connection.commit()
    connection.close()

# Create and populate the database
create_and_populate_db()
