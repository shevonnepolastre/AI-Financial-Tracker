import pytest
from project.project import Categories, Transactions

def test_is_income_category_existing(monkeypatch):
    cat = Categories()
    # This category already exists, so no input() will be called
    assert cat.is_income_category("salary") is True

def test_is_income_category_new_accept(monkeypatch):
    cat = Categories()
    # Mock user saying "y" to adding a new income category
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert cat.is_income_category("freelance") is True
    assert "freelance" in cat.income_cat

def test_is_income_category_new_decline(monkeypatch):
    cat = Categories()
    # Mock user saying "n" to adding a new category
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert cat.is_income_category("freelance") is False

def test_is_expense_category_existing(monkeypatch):
    cat = Categories()
    # Existing expense category, no subcategory given
    assert cat.is_expense_category("house") is True

def test_is_expense_category_new_with_sub_accept(monkeypatch):
    cat = Categories()
    inputs = iter(["y", "y"])  # Add new category, then add new subcategory
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert cat.is_expense_category("travel", "flights") is True
    assert "travel" in cat.expense_cat
    assert "flights" in cat.expense_cat["travel"]

def test_add_income_valid(monkeypatch):
    trans = Transactions()
    # Mock user entering a valid amount
    monkeypatch.setattr("builtins.input", lambda _: "500")
    result = trans.add_income("salary")
    assert result == ("salary", 500.0)
    assert trans.income["salary"] == 500.0

def test_add_income_invalid(monkeypatch):
    trans = Transactions()
    # Mock user entering invalid number
    monkeypatch.setattr("builtins.input", lambda _: "not_a_number")
    result = trans.add_income("salary")
    assert result is False
