from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
def getdata():
    try:
        con = sqlite3.connect('sql.db')
        cursor_obj = con.cursor()
        table = """CREATE TABLE IF NOT EXISTS EMPLOYEES (
                    Email VARCHAR(255) NOT NULL,
                    First_Name CHAR(25) NOT NULL,
                    Last_Name CHAR(25)
                );"""
        cursor_obj.execute(table)

        cursor_obj.execute("DELETE FROM EMPLOYEES")
        cursor_obj.execute('''INSERT INTO EMPLOYEES VALUES ('ayush@gmail.com', 'Ayush', 'Srivastava')''')
        cursor_obj.execute('''INSERT INTO EMPLOYEES VALUES ('ajay@gmail.com', 'Ajay', 'Kumar')''')
        cursor_obj.execute('''INSERT INTO EMPLOYEES VALUES ('ashish@gmail.com', 'Ashish', 'Singh')''')
        con.commit()
        data = cursor_obj.execute('''SELECT First_Name FROM EMPLOYEES''').fetchall()
        con.close()
        return data

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

@app.route('/api/data')
def data():
    try:
        rows = getdata()
        return jsonify(rows)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
