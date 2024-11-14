from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/getdata', methods = ['GET'])
def getdata():
    try:
        con = sqlite3.connect('sql.db')
        cursor_obj = con.cursor()
        data = cursor_obj.execute('''SELECT Email, First_Name, Last_Name FROM EMPLOYEES''').fetchall()
        con.close()
        return jsonify(data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An internal error occurred'}), 500
    # return data


@app.route('/post_end', methods=['POST'])
def create_employee():
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
            cursor_obj.execute('''INSERT INTO EMPLOYEES VALUES ('akash@gmail.com', 'Akash', 'Batra')''')
            con.commit()
            con.close()
            return jsonify({'message': 'Employees created successfully!'}), 201
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)