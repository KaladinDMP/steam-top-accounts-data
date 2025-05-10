# SteamLadder Top (Steam) Accounts Data Script

This script fetches the top 20 Steam accounts with the most games using the SteamLadder API.

## Setup

1. **Get your SteamLadder API key:**
   - Visit [https://steamladder.com/profile/](https://steamladder.com/profile/)
   - Click 'API' in the top menu
   - Copy your API key

2. **Create an API key file:**
   - Create a file named `apikey.txt` in the same folder as the script
   - Paste your API key into this file
   - The file should contain only your API key, nothing else

3. **Install required Python package:**
   ```bash
   pip install requests
   ```

## Usage

Run the script:
```bash
python topusers.py
```

The script will:
- Fetch the top 20 Steam accounts by game count
- Display them in a formatted table
- Save the data to two files:
  - `top_steam_accounts.json` - Full data in JSON format
  - `steam_ids_only.txt` - Just the Steam ID 64s, one per line

## Example Output

```
Top 20 Steam accounts by game count:
----------------------------------------------------------------------------------------------------
Rank   Steam ID 64        Username                  Games    Level   Country
----------------------------------------------------------------------------------------------------
1      76561198017975643  Ian Brandon Anderson      43329    353     US
2      76561198038715009  KaladinDMP                      40512    1084    US
...
```

## Optional: Country/Region Filtering

To get top accounts for a specific country or region, uncomment and modify the last lines in the script:

```python
# For United States
get_country_ladder('US')

# For Europe
get_region_ladder('europe')
```

Available regions: `europe`, `north_america`, `south_america`, `asia`, `africa`, `oceania`, `antarctica`

## Rate Limits

The SteamLadder API has a rate limit of 1000 requests per hour for your API key. If you hit the limit, wait an hour before making more requests.

## Troubleshooting

1. **"apikey.txt not found" error:**
   - Make sure the file is in the same directory as the script
   - Check that it's named exactly `apikey.txt` (not `apikey.txt.txt`)

2. **"Unauthorized" error:**
   - Double-check your API key is correct
   - Make sure there are no extra spaces or characters in the apikey.txt file

3. **"Rate limit exceeded" error:**
   - Wait an hour before trying again
   - Use the script sparingly to avoid hitting the limit

## Files Created

- `top_steam_accounts.json` - Full profile data
- `steam_ids_only.txt` - Just the Steam IDs for easy copying

## Credits

This script uses the [SteamLadder API](https://steamladder.com/). Make sure to add a link to SteamLadder.com if you use this data in your projects.

