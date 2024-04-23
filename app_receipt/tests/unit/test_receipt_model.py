# /tests/unit/test_printing_model.py

from datetime import datetime
from uuid import uuid4, UUID


import pytest
from pydantic import ValidationError

from app.models.receipt import Receipt

rec_id: UUID
ord_id: UUID
type: str
customer_info: str
create_date: datetime
rec: str


def test_receipt_creation():
    rec_id = uuid4()
    ord_id = uuid4()
    type = 'test_rec_type_1'
    create_date = datetime.now()
    rec = 'test_rec_rec_1'
    customer_info = 'test_customer_info_0'

    receipt = Receipt(rec_id=rec_id, ord_id=ord_id, type=type, create_date=create_date, rec=rec,
                        customer_info=customer_info)

    assert dict(receipt) == {'rec_id': rec_id, 'ord_id': ord_id, 'type': type,
                              'create_date': create_date, 'rec': rec,
                              'customer_info': customer_info}


def test_receipt_date_required():
    with pytest.raises(ValidationError):
        Receipt(rec_id=uuid4(),
                 ord_id=uuid4(),
                 type='test_rec_type_1',
                 rec='test_rec_rec_1',
                 customer_info='test_customer_info_0')


def test_receipt_ord_id_required():
    with pytest.raises(ValidationError):
        Receipt(rec_id=uuid4(),
                 type='test_rec_type_1',
                 create_date=datetime.now(),
                 rec='test_rec_rec_1',
                 customer_info='test_customer_info_0')
