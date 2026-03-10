import json
import datetime
import requests
import re

def get_roblox_rate():
    # Official DevEx Help Page
    url = "https://en.help.roblox.com/hc/en-us/articles/115005718246"
    # Fallback rate if scraping fails
    default_rate = 0.0038
    
    try:
        response = requests.get(url, timeout=10)
        # Search for the rate pattern (e.g., $0.0035 or $0.0038)
        match = re.search(r"\$0\.00\d+", response.text)
        if match:
            return float(match.group().replace('$', ''))
    except Exception as e:
        print(f"Error fetching: {e}")
        
    return default_rate

# Data structure for your website
data = {
    "devex": get_roblox_rate(),
    "retail": 0.0125, 
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d")
}

# This creates/updates the rate.json file in your repo
with open('rate.json', 'w') as f:
    json.dump(data, f, indent=4)
    print("rate.json updated successfully!")
