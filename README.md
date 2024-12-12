# JitterBug
A comprehensive suite of scripts and configurations for network performance testing, focusing on metrics like latency, jitter, throughput, and concurrency. This repository provides multiple methods to conduct network tests, including web-based tools, command-line utilities, and containerized solutions.

---

## **Contents**
1. [Prerequisites](#prerequisites)
2. [Methods for Network Testing](#methods-for-network-testing)
   - [Option 1: Cloudflare Speed Test](#option-1-cloudflare-speed-test)
   - [Option 2: iPerf3](#option-2-iperf3)
   - [Option 3: k6 Performance Testing](#option-3-k6-performance-testing)
   - [Option 4: Locust with Docker Compose](#option-4-locust-with-docker-compose)
3. [Jitter Calculation Script](#jitter-calculation-script)
4. [Contributing](#contributing)
5. [License](#license)

---

## **Prerequisites**
Before using the tools in this repository, ensure you have the following installed:
- [Docker](https://www.docker.com/) (for containerized solutions)
- [Node.js](https://nodejs.org/) and npm (for `k6` if running locally)
- Python 3.6+ (for custom scripts like jitter calculation)
- [iPerf3](https://iperf.fr/) (for network performance testing)

---

## **Methods for Network Testing**

### **Option 1: Cloudflare Speed Test**
A simple web-based option for a quick and easy network performance check.

1. Open your browser.
2. Navigate to [https://speed.cloudflare.com/](https://speed.cloudflare.com/).
3. Observe metrics such as download/upload speed, latency, and jitter.

---

### **Option 2: iPerf3**
Use iPerf3 to measure network throughput and latency. Refer to the commands in `commands.txt` for examples.

#### **Installation**
1. Install iPerf3:
   - **Linux**: `sudo apt install iperf3`
   - **macOS**: `brew install iperf3`
   - **Windows**: Download from [iperf.fr](https://iperf.fr/).

#### **Usage**
Run iPerf3 with the provided commands:
```bash
iperf3 -c ping.online.net -p 5209 -P 2 -t 60
```
- -c: Target Server
- -p: Port Number
- -P: Parallel Streams
- -t: Test duration in seconds

---

### **Option 3: k6 Performance Testing**
k6 is a modern load testing tool that provides a scripting API for defining performance tests.

#### **Installation**
1. Install k6:
    - **Linux**: `sudo apt install k6`
    - **macOS**: `brew install k6`
    - **Windows**: Download from [k6.io](https://k6.io/).

#### **Usage**
Run a basic k6 test:
```bash
k6 run test.js
```

---


### **Option 4: Locust with Docker Compose**
Locust is an open-source load testing tool that can be run using Docker Compose for distributed testing.

#### **Installation**
1. Ensure Docker and Docker Compose are installed.
2. Clone the repository:
    ```bash
    git clone https://github.com/example/jitterbug.git
    ```

#### **Usage**
1. Edit locustfile.py to define your test: 
2. Edit docker-compose.yml to include target host (*optional)
   - ```-H https://target.server```
3. Start Locust with Docker Compose:
```bash
docker-compose up -d
```
4. Access Locust's web interface: 
- Open http://localhost:8089

### Testing
1.	Enter the number of users and spawn rate.
2.	Monitor metrics like response time, requests per second, and errors.

---
## **Jitter Calculation Script**
A Python script to calculate jitter from network latency measurements.

#### **Installation**
Ensure Python 3.6+ is installed.

#### **Usage**
1. Ensure your latency data is in a CSV file (e.g., latency.csv).
2. Run the jitter calculation script:
```bash
python jitter_calculation.py latency.csv
```
3. Output:
    - Average jitter (in milliseconds) is printed to terminal.

## **Contributing**
We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.