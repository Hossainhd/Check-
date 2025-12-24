import json
import time
import os

class UptimeTracker:
    def __init__(self, filename="uptime_data.json"):
        self.filename = filename
        self.data = self.load_data()
        
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return self.get_default_data()
        return self.get_default_data()
    
    def get_default_data(self):
        return {
            "start_time": time.time(),
            "total_uptime": 0,
            "restarts": 0,
            "last_start": time.time()
        }
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_uptime_string(self):
        seconds = int(time.time() - self.data["last_start"])
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        return f"{days} দিন {hours} ঘন্টা {minutes} মিনিট {secs} সেকেন্ড"
