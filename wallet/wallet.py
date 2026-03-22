"""
RustChain MCP - Wallet Management (#19)
"""
class WalletManager:
    def __init__(self):
        self.wallets = {}
    
    def create(self, name: str) -> dict:
        wallet = {"name": name, "balance": 0}
        self.wallets[name] = wallet
        return wallet
    
    def get_balance(self, name: str) -> int:
        return self.wallets.get(name, {}).get("balance", 0)

if __name__ == "__main__":
    manager = WalletManager()
    wallet = manager.create("test")
    print(wallet)
