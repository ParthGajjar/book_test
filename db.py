import sqlite3




def get_db():
    conn = sqlite3.connect('example.db')
    cr = conn.cursor()
    return cr, conn

def get_recipes():
    cr, conn = get_db()
    rows = []
    for row in cr.execute('SELECT * FROM recipes'):
        rows.append(row[0])
    conn.close()
    return rows


def add_recipe(name):
    cr, conn = get_db()
    cr.execute('INSERT INTO recipes VALUES (?)', (name,))
    conn.commit()
    conn.close()

def delete_recipe(name):
    cr, conn = get_db()
    cr.execute('DELETE FROM recipes WHERE s = (?)', (name,))
    conn.commit()
    conn.close()
