# /tests/integration/app_repositories/test_db_delivery_repo.py

from datetime import datetime
from uuid import UUID, uuid4

import pytest

from app.models.receipt import Receipt
from app.repositories.db_receipt_repo import ReceiptRepo


@pytest.fixture()
def receipt_repo() -> ReceiptRepo:
    repo = ReceiptRepo()
    return repo


@pytest.fixture(scope='session')
def receipt_id() -> UUID:
    return uuid4()


@pytest.fixture(scope='session')
def first_receipt() -> Receipt:
    return Receipt(rec_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    ord_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    type='test_rec_type_1', create_date=datetime.now(),
                    rec='test_rec_rec_1', customer_info='test_customer_info_0')


@pytest.fixture(scope='session')
def second_receipt() -> Receipt:
    return Receipt(rec_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                    ord_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                    type='test_rec_type_2', create_date=datetime.now(),
                    rec='test_rec_rec_2', customer_info='test_customer_info_1')


# def test_empty_list(receipt_repo: ReceiptRepo) -> None:
#     receipt_repo.delete_all_receipt()
#     assert receipt_repo.get_receipt() == []


def test_add_first_receipt(first_receipt: Receipt, receipt_repo: ReceiptRepo) -> None:
    assert receipt_repo.create_receipt(first_receipt) == first_receipt


def test_add_first_receipt_repeat(first_receipt: Receipt, receipt_repo: ReceiptRepo) -> None:
    with pytest.raises(KeyError):
        receipt_repo.create_receipt(first_receipt)


def test_get_receipt_by_id(first_receipt: Receipt, receipt_repo: ReceiptRepo) -> None:
    assert receipt_repo.get_receipt_by_id(first_receipt.rec_id) == first_receipt


def test_get_receipt_by_id_error(receipt_repo: ReceiptRepo) -> None:
    with pytest.raises(KeyError):
        receipt_repo.get_receipt_by_id(uuid4())


def test_add_second_receipt(first_receipt: Receipt, second_receipt: Receipt, receipt_repo: ReceiptRepo) -> None:
    assert receipt_repo.create_receipt(second_receipt) == second_receipt
    receipts = [receipt_repo.get_receipt_by_id(first_receipt.rec_id),
                 receipt_repo.get_receipt_by_id(second_receipt.rec_id)]
    assert len(receipts) == 2
    assert receipts[0] == first_receipt
    assert receipts[1] == second_receipt


def test_delete_created_order(first_receipt: Receipt, second_receipt: Receipt, receipt_repo: Receipt) -> None:
    assert receipt_repo.delete_receipt_by_id(first_receipt.rec_id) == first_receipt
    assert receipt_repo.delete_receipt_by_id(second_receipt.rec_id) == second_receipt
