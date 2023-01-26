from flask import Flask, render_template, url_for, redirect, request
from sqlalchemy import create_engine, Column, String, DateTime, Integer, Boolean # Para entrar no SQL
from sqlalchemy.orm import sessionmaker # Sessão pro sql
 # Para ORM (FACILITANDO O MANUSEIO DO BANCO)
from datetime import datetime
from db import List

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://root:45093988rgftqj@localhost/todoflask', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    """
    Apenas redirecionando o cliente a home
    """
    return redirect(url_for('home'))

@app.route('/home')
def home():
    """
    Fazendo uma busca por todos os itens na lista
    """
    itens = session.query(List).all()
    return render_template('index.html', itens=itens)

@app.route('/home', methods=['POST'])
def add():
    if request.method == 'POST':
        item = List(item=request.form['item'],when=datetime.utcnow(),done=False) # Criando um item, com ORM.
        session.add(item) # Adicionando
        session.commit() # Atualizando
        return redirect(url_for('home')) # Redirecionando a nova home

@app.route('/home/update/<id>')
def uptade(id):
    item = session.query(List).filter(List.id == id).one() # Buscando apenas um item
    item.done = True # Mudando para feito
    session.add(item)
    session.commit()
    return redirect(url_for('home'))

@app.route('/home/delete/<id>')
def delete(id):
    item = session.query(List).filter(List.id == id).one()
    session.delete(item) # Deletando
    session.commit
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()