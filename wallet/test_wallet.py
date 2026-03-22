import pytest
from wallet import WalletManager

class TestWalletManager:
    def test_create(self):
        manager = WalletManager()
        wallet = manager.create("test")
        assert wallet["name"] == "test"
        assert wallet["balance"] == 0
    
    def test_get_balance(self):
        manager = WalletManager()
        manager.create("test")
        assert manager.get_balance("test") == 0

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
