from flask import Flask  # Permite criar a API
from flask_sqlalchemy import SQLAlchemy  # Permite criar o banco de dados

# Criar uma API flask
app = Flask(__name__)
# Criar uma instância de SQLAlcheny
# SECRET_KEY -> Gera um acesso de autenticação único:
app.config['SECRET_KEY'] = 'HJSFJDGF234H%$#'
# SQLALCHEMY_DATABASE_URL -> Define onde está localizado o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
db: SQLAlchemy

# Definir a estrutura da tabela postagem
# id_postagem, titulo, autor


class Postagem(db.Model):
    __tablename__ = 'postagem'
    # Representa um valor único, que não deve se repetir. OBS.: Ele será incrementado automaticamente de um a um
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
# Definir a estrutura da tabela autor
# id_autor, nome, email, senha, admin, postagens


class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')


# Executar o comando para criar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Criar usuários administradores
        autor = Autor(nome='Guilherme', email='guilherme@gmail.com',
                      senha='12345', admin=True)
        db.session.add(autor)
        db.session.commit()


if __name__ == '__main__':
    inicializar_banco()
