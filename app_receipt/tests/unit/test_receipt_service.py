from uuid import uuid4, UUID

import pytest

from app.repositories.local_receipt_repo import ReceiptRepo
from app.services.receipt_service import ReceiptService


@pytest.fixture(scope='session')
def receipt_service() -> ReceiptService:
    return ReceiptService(ReceiptRepo(clear=True))


@pytest.fixture(scope='session')
def first_receipt_data() -> tuple[UUID, str, str, str]:
    return (uuid4(), 'test_receipt_type_1', 'test_receipt_rec_1', 'test_receipt_customer_info_1')


@pytest.fixture(scope='session')
def second_receipt_data() -> tuple[UUID, str, str, str]:
    return (uuid4(), 'test_receipt_type_2', 'test_receipt_rec_2', 'test_receipt_customer_info_2')


def test_empty_receipt(receipt_service: ReceiptService) -> None:
    assert receipt_service.get_receipt() == []


def test_create_first_receipt(
        first_receipt_data: tuple[UUID, str, str, str],
        receipt_service: ReceiptService
) -> None:
    ord_id, type, rec, customer_info = first_receipt_data
    receipt = receipt_service.create_receipt(ord_id, type, rec, customer_info)
    assert receipt.ord_id == ord_id
    assert receipt.type == type
    assert receipt.customer_info == customer_info
    assert receipt.rec == rec


def test_create_second_receipt(
        second_receipt_data: tuple[UUID, str, str, str],
        receipt_service: ReceiptService
) -> None:
    ord_id, type, rec, customer_info = second_receipt_data
    receipt = receipt_service.create_receipt(ord_id, type, rec, customer_info)
    assert receipt.ord_id == ord_id
    assert receipt.type == type
    assert receipt.customer_info == customer_info
    assert receipt.rec == rec


def test_get_receipt_full(
        first_receipt_data: tuple[UUID, str, str, str],
        second_receipt_data: tuple[UUID, str, str, str],
        receipt_service: ReceiptService
) -> None:
    receipt = receipt_service.get_receipt()
    assert len(receipts) == 2
    assert receipts[0].ord_id == first_receipt_data[0]
    assert receipts[0].type == first_receipt_data[1]
    assert receipts[0].rec == first_receipt_data[2]
    assert receipts[0].customer_info == first_receipt_data[3]

    assert receipts[1].ord_id == second_receipt_data[0]
    assert receipts[1].type == second_receipt_data[1]
    assert receipts[1].rec == second_receipt_data[2]
    assert receipts[1].customer_info == second_receipt_data[3]
