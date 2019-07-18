def get_state(user_id, cursor):
    cursor.execute('SELECT State FROM Users WHERE ID=' +
                   str(user_id))
    a = cursor.fetchone()
    if a is None:
        return -1
    else:
        return a[0]


def set_state(user_id, state, cursor, db):
    cursor.execute('UPDATE Users SET State=' + str(state) +
                   ' WHERE ID=' +str(user_id))
    db.commit()


def add_user(user_id, cursor, db):
    cursor.execute('INSERT INTO Users(ID, State) VALUES (' +
                   str(user_id) + ', 1)')
    db.commit()
