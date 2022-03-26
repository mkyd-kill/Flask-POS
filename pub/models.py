from .database import db_session
from datetime import datetime
from sqlalchemy import Column, Float, Integer, String, DateTime, event, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    tax = Column(Float, nullable=True)
    status = Column(String(20), nullable=False)


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_on = Column(DateTime(timezone=True), nullable=False)

    def __init__(self):
        self.create_on = datetime.now()


class TransactionProducts(Base):
    __tablename__ = 'transaction_products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product_qty = Column(Integer, nullable=False)
    transaction = relationship("Transactions", backref="transaction_products")
    product = relationship("Products", backref="transaction_products")


@event.listens_for(db_session, 'before_flush')
def reduce_stock_product(*args):
    sess = args[0]
    for obj in sess.new:
        if not isinstance(obj, TransactionProducts):
            continue
        product = Products.query.filter_by(id=obj.product_id).first() 

        product.stock = product.stock - obj.product_qty
        db_session.add(product)


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), unique=True, nullable=False)
    date_login = Column(DateTime(timezone=True), onupdate=datetime.utcnow)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f'<Admin: {self.name!r}'


class Super_Admin(Base):
    __tablename__ = 'super-admin'
    id = Column(Integer, primary_key=True)
    admin_name = Column(String(50), nullable=False)
    admin_pass = Column(String(50), nullable=False)

    def __init__(self, name, password):
        self.admin_name = name
        self.admin_pass = password

    def serialize(self):
        return {
            'id': self.id,
            'username': self.admin_name,
            'password': self.admin_pass
        }
        
    def __repr__(self):
        return f'<Super_User: {self.admin_name!r}'