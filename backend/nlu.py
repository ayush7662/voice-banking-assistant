import re

INTENTS = {
    "check_balance": [r"balance", r"account balance"],
    "transfer": [r"transfer", r"send money", r"pay"],
    "transactions": [r"recent transactions", r"history"],
}

def parse(text):
    t = text.lower()
    for intent, patterns in INTENTS.items():
        for pat in patterns:
            if re.search(pat, t):
                amount = re.search(r"\b(\d+)\b", t)
                account = re.search(r"(acct|account)\s*(\d+)", t)
                return {
                    "intent": intent,
                    "amount": float(amount.group(1)) if amount else None,
                    "account": account.group(2) if account else None
                }
    return {"intent": "unknown"}
