import csv
import sys

def calculate_jitter(csv_file):
    latencies = []

    # Read the CSV and extract latencies
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    latencies.append(float(row["Latency (ms)"]))
                except ValueError:
                    pass  # Skip rows with invalid latency values
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None

    # Calculate jitter (average absolute difference between consecutive latencies)
    if len(latencies) < 2:
        print("Not enough data to calculate jitter.")
        return None

    jitter_sum = sum(abs(latencies[i] - latencies[i - 1]) for i in range(1, len(latencies)))
    jitter = jitter_sum / (len(latencies) - 1)

    return jitter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculate_jitter.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    jitter = calculate_jitter(csv_file)

    if jitter is not None:
        print(f"Calculated Jitter: {jitter:.2f} ms")