from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

engine = create_engine(
    "sqlite:///mock_bank.db", echo=False, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True)
    name = Column(String)
    accounts = relationship("Account", back_populates="owner")


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    account_no = Column(String, unique=True)
    balance = Column(Float, default=0.0)
    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Float)
    type = Column(String)  # "debit" or "credit"
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    account = relationship("Account", back_populates="transactions")


def init_db():
    Base.metadata.create_all(bind=engine)
    # Create a default user and accounts only if DB is empty
    if not session.query(User).first():
        # User Alice
        u = User(phone="9999999999", name="Alice")
        # Accounts for Alice
        a1 = Account(account_no="ACCT1001", balance=5000, owner=u)
        a2 = Account(account_no="ACCT2001", balance=1500, owner=u)
        # Add some transactions
        t1 = Transaction(account=a1, amount=2000, type="credit", description="Initial deposit")
        t2 = Transaction(account=a1, amount=500, type="debit", description="Grocery shopping")
        t3 = Transaction(account=a2, amount=1500, type="credit", description="Initial deposit")
        session.add_all([u, a1, a2, t1, t2, t3])
        session.commit()
