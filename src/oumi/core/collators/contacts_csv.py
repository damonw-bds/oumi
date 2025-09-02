import os
import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# --- Config ---
CSV_PATH = os.environ.get('CONTACTS_CSV_PATH', 'contacts.csv')
COMMON_NAMES = {'John', 'Mary', 'James', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda'}
DATABASE_URL = os.environ.get('DATABASE_URL')  # Set this in your environment

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set.")

# --- DB Setup ---
Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# --- CSV Load & Filter ---
def load_and_store_contacts():
    df = pd.read_csv(CSV_PATH)
    filtered = df[~df['name'].str.split().str[0].isin(COMMON_NAMES)]
    session = Session()
    for _, row in filtered.iterrows():
        contact = Contact(name=row['name'], email=row['email'])
        session.add(contact)
    session.commit()
    session.close()

# --- REST API ---
app = Flask(__name__)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    session = Session()
    contacts = session.query(Contact).all()
    result = {c.id: {'name': c.name, 'email': c.email} for c in contacts}
    session.close()
    return jsonify(result)

if __name__ == '__main__':
    load_and_store_contacts()
    # Do NOT enable debug mode in production
    app.run()