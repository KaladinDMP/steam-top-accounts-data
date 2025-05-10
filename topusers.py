import requests
import json
import os

def load_api_key():
    try:
        with open('apikey.txt', 'r') as f:
            api_key = f.read().strip()
            if not api_key:
                print("Error: apikey.txt is empty!")
                return None
            return api_key
    except FileNotFoundError:
        print("Error: apikey.txt not found!")
        print("Please create a file named 'apikey.txt' in the same directory as this script")
        print("and paste your SteamLadder API key inside it.")
        print("\nTo get your API key:")
        print("1. Visit https://steamladder.com/profile/")
        print("2. Click 'API' in the top menu")
        print("3. Copy your API key and paste it into apikey.txt")
        return None
    except Exception as e:
        print(f"Error reading apikey.txt: {e}")
        return None

API_KEY = load_api_key()
if not API_KEY:
    print("\nScript cannot continue without an API key. Exiting...")
    exit(1)

BASE_URL = "https://steamladder.com/api/v1"

headers = {
    "Authorization": f"Token {API_KEY}"
}

def get_top_game_ladders(country_code=None, region=None):
    """
    Get the top accounts with most games
    
    Args:
        country_code: Optional alpha-2 country code (e.g., 'US', 'GB')
        region: Optional region ('europe', 'north_america', 'south_america', 'asia', 'africa', 'oceania', 'antarctica')
    
    Returns:
        List of top game accounts
    """

    if country_code:
        url = f"{BASE_URL}/ladder/games/{country_code}"
    elif region:
        url = f"{BASE_URL}/ladder/games/{region}"
    else:
        url = f"{BASE_URL}/ladder/games/"
    
    try:
        print(f"Requesting URL: {url}")
        response = requests.get(url, headers=headers)
        
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("Parsing JSON response...")
            data = response.json()
            
            print(f"API response keys: {data.keys() if isinstance(data, dict) else 'Not a dict'}")

            if isinstance(data, list):
                profiles = data
            else:
                profiles = data.get('ladder', data.get('profiles', data.get('data', [])))
            
            print(f"Found {len(profiles)} profiles")

            top_20 = profiles[:20]
                        
            results = []
            for i, profile in enumerate(top_20):
                if not isinstance(profile, dict):
                    continue
                                 
                steam_user = profile.get('steam_user', {})
                steam_stats = profile.get('steam_stats', {})
                games_stats = steam_stats.get('games', {})
                
                result = {
                    'rank': profile.get('pos', i) + 1,  
                    'steam_id': steam_user.get('steam_id'),
                    'steam_id_64': steam_user.get('steam_id'), 
                    'persona_name': steam_user.get('steam_name'),
                    'total_games': games_stats.get('total_games', 0),
                    'profile_url': steam_user.get('steamladder_url'),
                    'level': steam_stats.get('level'),
                    'xp': steam_stats.get('xp'),
                    'join_date': steam_user.get('steam_join_date'),
                    'country_code': steam_user.get('steam_country_code')
                }
                results.append(result)
            
            return results
            
        elif response.status_code == 429:
            print("Rate limit exceeded. Please wait before making more requests.")
            print(f"Response: {response.text}")
            return None
        elif response.status_code == 401:
            print("Unauthorized. Check your API key.")
            print(f"Response: {response.text}")
            return None
        elif response.status_code == 404:
            print("Not found. Check the country code or region.")
            print(f"Response: {response.text}")
            return None
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"Error making request: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    print("Fetching top 20 Steam accounts with most games...\n")
    
    top_accounts = get_top_game_ladders()
    
    if top_accounts:
        print("Top 20 Steam accounts by game count:")
        print("-" * 100)
        print(f"{'Rank':<6} {'Steam ID 64':<18} {'Username':<25} {'Games':<8} {'Level':<7} {'Country'}")
        print("-" * 100)
        
        for account in top_accounts:
            print(f"{account['rank']:<6} {account['steam_id_64']:<18} {account['persona_name']:<25} {account['total_games']:<8} {account['level']:<7} {account['country_code'] or 'N/A'}")
        
        with open('top_steam_accounts.json', 'w') as f:
            json.dump(top_accounts, f, indent=2)
        print(f"\nData saved to 'top_steam_accounts.json'")
        
        steam_ids = [account['steam_id_64'] for account in top_accounts if account['steam_id_64']]
        print(f"\nTop 20 Steam ID 64s:")
        for i, steam_id in enumerate(steam_ids, 1):
            print(f"{i}. {steam_id}")
            
        with open('steam_ids_only.txt', 'w') as f:
            for steam_id in steam_ids:
                f.write(f"{steam_id}\n")
        print(f"\nSteam IDs saved to 'steam_ids_only.txt'")
    else:
        print("Failed to fetch data.")

def get_country_ladder(country_code):
    print(f"\nFetching top 20 for {country_code}...")
    results = get_top_game_ladders(country_code=country_code)
    if results:
        for account in results:
            print(f"{account['rank']}. {account['persona_name']} - {account['total_games']} games")

def get_region_ladder(region):
    print(f"\nFetching top 20 for {region}...")
    results = get_top_game_ladders(region=region)
    if results:
        for account in results:
            print(f"{account['rank']}. {account['persona_name']} - {account['total_games']} games")

if __name__ == "__main__":
    # Get global top 20
    main()
    
    # Uncomment these to get country/region specific data
    # get_country_ladder('US')  # Top 20 for United States
    # get_region_ladder('europe')  # Top 20 for Europe