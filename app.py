import psutil 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu.percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Usage Detected, Please Scale Up."
    return f"CPU Utilization: {cpu_percent} and Memory Utilization: {mem_percent}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')