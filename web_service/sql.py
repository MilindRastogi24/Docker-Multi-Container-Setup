insert_data = """
Insert Into users (name , email) Values ('Milind' , 'milind@gmail.com');"""

create_table = """ CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""