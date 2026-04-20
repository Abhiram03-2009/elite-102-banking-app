import db
import os

def run_tests():
    print("Testing db initialization...")
    db.init_db()
    
    print("Creating account...")
    acc_id = db.create_account("Alice", 100.0)
    assert acc_id > 0
    
    print("Checking balance...")
    bal = db.check_balance(acc_id)
    assert bal == 100.0
    
    print("Testing deposit...")
    db.deposit(acc_id, 50.0)
    assert db.check_balance(acc_id) == 150.0
    
    print("Testing withdrawal...")
    db.withdraw(acc_id, 25.0)
    assert db.check_balance(acc_id) == 125.0
    
    print("Testing insufficient funds withdrawal...")
    try:
        db.withdraw(acc_id, 1000.0)
        assert False, "Should have raised exception"
    except ValueError as e:
        assert str(e) == "Insufficient funds."
        
    print("Testing list accounts...")
    accounts = db.list_accounts()
    assert len(accounts) >= 1
    found = False
    for a in accounts:
        if a[0] == acc_id:
            assert a[1] == "Alice"
            assert a[2] == 125.0
            found = True
    assert found
    
    # cleanup db for fresh run if needed, but we'll leave it to show data
    print("ALL TESTS PASSED!")

if __name__ == '__main__':
    run_tests()
