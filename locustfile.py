import csv
import time
from datetime import datetime
from locust import HttpUser, task, between, events

# Generate a unique filename based on the current datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"/mnt/locust/network_test_results_{timestamp}.csv"

# Initialize CSV file and write the header
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Latency (ms)", "Response Code", "Current Users", "Requests Per Second"])

# Custom listener to track request success/failure rates
class NetworkPerformanceTest(HttpUser):
    wait_time = between(1, 2)  # Random wait time between requests

    @task
    def simulate_network_request(self):
        start_time = time.time()
        try:
            response = self.client.get("/")  # Replace with the target endpoint
            latency = (time.time() - start_time) * 1000  # Convert to milliseconds

            # Get Locust's runtime stats
            stats = self.environment.stats.total
            current_rps = stats.current_rps
            current_users = self.environment.runner.user_count if self.environment.runner else 0

            # Write data to CSV
            with open(csv_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    time.strftime("%Y-%m-%d %H:%M:%S"),
                    latency,
                    response.status_code,
                    current_users,
                    current_rps,
                ])
        except Exception as e:
            # Handle exceptions if the request fails
            with open(csv_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    time.strftime("%Y-%m-%d %H:%M:%S"),
                    "N/A",
                    f"ERROR: {e}",
                    0,
                    0,
                ])