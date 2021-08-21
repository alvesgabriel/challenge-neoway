import functools
import re

import validate_docbr as docbr


def parse_file(lines, file):
    buyer_doc = slice(0, 19)
    private = slice(19, 31)
    incomplete = slice(31, 43)
    created_at = slice(43, 65)
    ticket_average = slice(65, 87)
    ticket = slice(87, 111)
    seller_doc_most_frequency = slice(111, 131)
    seller_doc = slice(131, 152)

    return [
        {
            "file": file,
            "buyer_doc": digits(line[buyer_doc]),
            "private": to_bool(line[private]),
            "incomplete": to_bool(line[incomplete]),
            "created_at": to_date(line[created_at]),
            "ticket_average": to_float(line[ticket_average]),
            "ticket": to_float(line[ticket]),
            "seller_doc_most_frequency": digits(
                line[seller_doc_most_frequency]
            ),
            "seller_doc": digits(line[seller_doc]),
            "invalid_buyer_doc": validate_document(line[buyer_doc]),
            "invalid_seller_doc": validate_document(line[seller_doc]),
            "invalid_seller_doc_most_frequency": validate_document(
                line[seller_doc_most_frequency]
            ),
        }
        for line in lines
        if not line.lower().startswith(b"cpf")
    ]


def to_str(function):
    @functools.wraps(function)
    def wrapper(value):
        value = value.strip().decode("utf-8")
        if value == "NULL":
            return function("")
        return function(value)

    return wrapper


@to_str
def digits(value):
    return re.sub(r"\D", "", value) or None


@to_str
def to_float(value):
    return re.sub(",", ".", value) or None


@to_str
def to_bool(value):
    return bool(int(value))


@to_str
def to_date(value):
    return value or None


@to_str
def validate_document(value):
    docs = (
        (docbr.CPF, value),
        (docbr.CNPJ, value),
    )
    return not any(docbr.validate_docs(docs))
