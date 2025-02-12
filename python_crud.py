# CRUD operations

# Create
# Read
# Update
# Delete
import psycopg2


def create_person(conn, firstname, lastname, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)", (firstname, lastname, age))
    conn.commit()
    cursor.close()

def read_all_persons(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    persons = cursor.fetchall()
    cursor.close()
    return persons

def read_person(conn, person_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person WHERE id = %s", (person_id,))
    person = cursor.fetchone()
    cursor.close()
    return person

def update_person(conn, person_id, person):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE person SET firstname = %s, lastname = %s, age = %s WHERE id = %s",
        (person['firstname'], person['lastname'], person['age'], person_id)
    )
    conn.commit()
    cursor.close()

def delete_person(conn, person_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM person WHERE id = %s", (person_id,))
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="aron",
        password="admin"
    )

    # # create_person(conn, "John", "Doe", 30)
    # persons = read_all_persons(conn)
    # print(persons)

    # print(persons[0][1])

    readperson = read_person(conn, 5)
    print(readperson)

    updateperosn = update_person(conn, 5, {'firstname': 'Aron', 'lastname': 'Alfonso', 'age': 30})
    print(updateperosn)

    deleteperson = delete_person(conn, 5)
    print(deleteperson)