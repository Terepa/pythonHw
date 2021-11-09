import sqlite3
con = sqlite3.connect('chinook.db')
cur = con.cursor()

def get_album_by_id(cur, id):
    cur.execute('SELECT * FROM artists WHERE ArtistId = ?', (id,))
    return cur.fetchone()


def get_album_by_name(cur, name):
    cur.execute('SELECT * FROM artists WHERE Title LIKE ?', (name,))
    # return cur.fetchone()
    return cur.fetchall()

def insert_album(cur, album: tuple):
    cur.execute('INSERT INTO artists (Title, ArtistId) VALUES (?, ?)',
                album)



new_albums = get_album_by_name(cur, "Valdis greatest hits%")
print(new_albums)

some_album = get_album_by_id(cur, 1)
print(some_album)
con.commit()  # this should save the database transactions
con.close()
