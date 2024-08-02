from flask import Flask, jsonify
import sqlite3


# Expose a REST API endpoint using the Flask framework
# to serve a JSON-serialized list of books queried from
# a file-based SQLite database.
app = Flask(__name__)
DATABASE = "books.db"


# Define a route to handle GET requests to the /books endpoint
@app.route("/books", methods=["GET"])
def get_books():
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Query all books from the database
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Serialize the books as JSON and return the response
    return jsonify(books)


if __name__ == "__main__":
    app.run(debug=True)
