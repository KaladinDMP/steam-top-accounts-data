# Top Steam Accounts by Game Count

This repository contains the top 20 Steam accounts ranked by number of games owned.

## Files

- `steam_ids_only.txt` - Just the Steam ID 64s, one per line
- `top_steam_accounts.json` - Full profile data

## Last Updated

Sun Jan  4 03:50:25 UTC 2026

## Note

This data is collected from [SteamLadder](https://steamladder.com) and is updated automatically every Sunday.
The Steam accounts listed are publicly available and ranked by the number of games in their library.

## Using This Data

You can download the `steam_ids_only.txt` file directly:
```
https://raw.githubusercontent.com/KaladinDMP/steam-top-accounts-data/main/steam_ids_only.txt
```

Or use it in your script:
```python
import requests

# Download the file
url = "https://raw.githubusercontent.com/KaladinDMP/steam-top-accounts-data/main/steam_ids_only.txt"
response = requests.get(url)
steam_ids = response.text.strip().split('\n')

# Process the IDs
for steam_id in steam_ids:
    print(f"Processing: {steam_id}")
```
