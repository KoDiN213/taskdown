import sqlite3


def init_db():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    cur.execute("""
                CREATE TABLE task
                    (id INT AUTO INCREMENT,
                     description TEXT,
                     tag TEXT,
                     priority TEXT,
                     status Boolean,
                     start_date TIMESTAMP,
                     end_date TIMESTAMP,
                     time_spent TIME,
                     PRIMARY KEY(id)
                );
                """)
    cur.execute(""" CREATE TABLE time
                (id INT AUTO INCREMENT,
                 task_id INT, 
                 date TIMESTAMP,
                 duration TIME,
                 PRIMARY KEY(id),
                 FOREIGN KEY(task_id) REFERENCES task(id)
                ); """)
    con.commit()
