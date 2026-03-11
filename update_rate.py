import json
import datetime
import requests
import re

def get_roblox_rate():
    # We check the main help page
    url = "https://en.help.roblox.com/hc/en-us/articles/13061189551124"
    # NEVER set this to 0. Use the current known rate as the fallback.
    fallback_rate = 0.00 
    
    try:
        response = requests.get(url, timeout=15)
        # Search for the specific rate pattern in the text
        # This looks for "0.00" followed by any digits
        match = re.search(r"0\.00\d+", response.text)
        
        if match:
            found_rate = float(match.group())
            print(f"Success! Found rate on Roblox site: {found_rate}")
            return found_rate
        else:
            print("Could not find rate pattern on page. Using fallback.")
    except Exception as e:
        print(f"Connection Error: {e}")
        
    return fallback_rate

# Create the data
new_devex = get_roblox_rate()
data = {
    "devex": new_devex,
    "retail": 0.00, # Retail doesn't change often, keep as constant
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open('rate.json', 'w') as f:
    json.dump(data, f, indent=4)
    print("rate.json has been updated.")
