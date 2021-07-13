import pytest

from main import phone_regex, make_phone_format

phones = [
    ">+8(924)1112233.",
    " +8-924-111-2233<",
    ".+89241112233 ",
    " +892411122-33.",
    ")+8924 111 22-33<",
    "=+8(924)111 22-33.",
    ">88004442233-",
]
not_phones = [
    "+8(924)1112233",
    "+8(924)111223",
    "+8((924)1112233",
    "43+8(924)1112233",
    "a+8(924)1112233",
    "a+8(924)1112233b",
    "+8(924)1112233b",
    "d+8-924-111-2233",
    "f+89241112233",
    "3+892411122-33",
    "588004442233",
    "88004442233a",
]


@pytest.mark.parametrize("phone", phones)
def test_is_phone(phone: str):
    assert phone_regex.search(phone) is not None


@pytest.mark.parametrize("phone", not_phones)
def test_is_not_phone(phone: str):
    assert phone_regex.search(phone) is None


def test_return_format():
    phones = [
        ("8", "495", "111", "22", "33"),
    ]
    res = make_phone_format(phones)
    assert res[0] == "84951112233"
