# RustChain MCP Server Skills

Query RustChain blockchain data, check balances, browse bounties, and manage wallets.

## Setup

1. Install the MCP server:
```bash
pip install rustchain-mcp
```

2. Add to your Claude Code config:
```json
{
  "mcpServers": {
    "rustchain": {
      "command": "python",
      "args": ["-m", "rustchain_mcp.server"]
    }
  }
}
```

## Available Tools

### `rustchain_health()`
Check RustChain node health status.

```python
# Example: Check if network is operational
status = rustchain_health()
print(f"Node version: {status['version']}")
print(f"Uptime: {status['uptime']}")
```

### `rustchain_epoch()`
Get current epoch information.

```python
# Example: Check current epoch and miners count
epoch = rustchain_epoch()
print(f"Epoch: {epoch['epoch']}")
print(f"Enrolled miners: {epoch['enrolled_miners']}")
print(f"Reward pot: {epoch['epoch_reward_pot']} RTC")
```

### `rustchain_miners()`
List all active miners with hardware details.

```python
# Example: Browse active miners
miners = rustchain_miners()
print(f"Total miners: {miners['total_miners']}")
for miner in miners['miners'][:5]:
    print(f"  {miner['miner']} - {miner['hardware_type']} ({miner['antiquity_multiplier']}x)")
```

### `rustchain_create_wallet(agent_name)`
Create a new RTC wallet for an AI agent.

```python
# Example: Create wallet for new agent
wallet = rustchain_create_wallet("my-crewai-agent")
print(f"Wallet ID: {wallet['wallet_id']}")
print(f"Balance: {wallet['balance']} RTC")
```

### `rustchain_balance(wallet_id)`
Check RTC token balance for a wallet.

```python
# Example: Check balance
balance = rustchain_balance("dual-g4-125")
print(f"Balance: {balance['balance']} RTC (${balance['usd_value']} USD)")
```

### `rustchain_stats()`
Get RustChain network statistics.

```python
# Example: Get network stats
stats = rustchain_stats()
print(f"Total miners: {stats['total_miners']}")
print(f"Current epoch: {stats['epoch']['epoch']}")
print(f"Total supply: {stats['total_supply']} RTC")
```

## Common Workflows

### Check Your Mining Rewards
```python
# 1. Check your balance
balance = rustchain_balance("your-wallet-name")
print(f"Your balance: {balance['balance']} RTC")

# 2. Check current epoch rewards
epoch = rustchain_epoch()
print(f"Epoch reward pot: {epoch['epoch_reward_pot']} RTC")

# 3. Check if you're enrolled
miners = rustchain_miners()
your_miner = [m for m in miners['miners'] if m['miner'] == "your-wallet-name"]
if your_miner:
    print(f"Enrolled with weight: {your_miner[0]['weight']}")
```

### Browse Active Bounties
```python
# Note: Bounties are on GitHub, but you can check wallet balance
# to verify bounty payments were received
balance = rustchain_balance("your-wallet-name")
print(f"Current balance: {balance['balance']} RTC")
```

### Create Wallet for New Agent
```python
# Create wallet
wallet = rustchain_create_wallet("new-agent-name")
print(f"Wallet created: {wallet['wallet_id']}")
print(f"Initial balance: {wallet['balance']} RTC")

# Save wallet ID for future use
with open("wallet.txt", "w") as f:
    f.write(wallet['wallet_id'])
```

## API Reference

- **Node**: https://50.28.86.131
- **Explorer**: https://rustchain.org/explorer
- **GitHub**: https://github.com/Scottcjn/Rustchain
- **Docs**: https://rustchain.org

## Payment

Bounty: 5 RTC
Wallet: Dlove123
RTC Address: RTCb72a1accd46b9ba9f22dbd4b5c6aad5a5831572b
