from models import session, User, Account, Transaction

def get_user_by_phone(phone):
    return session.query(User).filter_by(phone=phone).first()

def get_account_by_no(acct_no):
    return session.query(Account).filter_by(account_no=acct_no).first()

def get_balance(acct_no):
    acct = get_account_by_no(acct_no)
    return acct.balance if acct else None

def transfer(from_acct, to_acct, amount):
    f = get_account_by_no(from_acct)
    t = get_account_by_no(to_acct)
    if not f or not t:
        return False, "Account not found"
    if f.balance < amount:
        return False, "Insufficient funds"

    f.balance -= amount
    t.balance += amount

    session.add(Transaction(account_id=f.id, amount=amount, type="debit", description=f"To {to_acct}"))
    session.add(Transaction(account_id=t.id, amount=amount, type="credit", description=f"From {from_acct}"))
    session.commit()
    return True, "Transfer Successful"

def get_transactions(acct_no):
    acct = get_account_by_no(acct_no)
    if not acct:
        return []
    txns = session.query(Transaction).filter_by(account_id=acct.id).all()
    return [{"amount": t.amount, "type": t.type, "desc": t.description} for t in txns]
