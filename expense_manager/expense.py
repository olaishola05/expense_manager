from datetime import datetime
from typing import Dict
import uuid
from utils import date_formatter as df

class Expense():
    def __init__(self, title: str, amount: float, created_at: datetime) -> None:
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.title = title
        self.created_at = created_at
        self.updated_at = None
    
    def update_expense(self, expense: Dict, amount: float, title: str):
        expense['amount'] = amount
        expense['title'] = title
        expense['updated_at'] = df.create_date()
        return expense

    def to_dict(self):
        return self.__dict__