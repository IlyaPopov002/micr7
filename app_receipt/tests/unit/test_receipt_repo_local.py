# /tests/unit/test_printing_repo.py

from datetime import datetime
from uuid import uuid4, UUID

import pytest

from app.models.receipt import Receipt
from app.repositories.local_receipt_repo import ReceiptRepo

receipt_test_repo = ReceiptRepo()


def test_empty_list() -> None:
    assert receipt_test_repo.get_receipt() == []


def test_add_first_receipt() -> None:
    receipt = Receipt(rec_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                        ord_id=uuid4(),
                        type='test_rec_type_1',
                        create_date=datetime.now(),
                        rec='test_rec_rec_1',
                        customer_info='test_customer_info_0')
    assert receipt_test_repo.create_receipt(receipt) == receipt


def test_add_first_receipt_repeat() -> None:
    receipt = Receipt(rec_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                        ord_id=uuid4(),
                        type='test_rec_type_1',
                        create_date=datetime.now(),
                        rec='test_rec_rec_1',
                        customer_info='test_customer_info_0')
    # receipt_test_repo.create_receipt(receipt)
    with pytest.raises(KeyError):
        receipt_test_repo.create_receipt(receipt)


def test_get_receipt_by_id() -> None:
    receipt = Receipt(rec_id=uuid4(),
                        ord_id=uuid4(),
                        type='test_rec_type_1',
                        create_date=datetime.now(),
                        rec='test_rec_rec_1',
                        customer_info='test_customer_info_0')
    receipt_test_repo.create_receipt(receipt)
    assert receipt_test_repo.get_receipt_by_id(receipt.rec_id) == receipt


def test_get_receipt_by_id_error() -> None:
    with pytest.raises(KeyError):
        receipt_test_repo.get_receipt_by_id(uuid4())
