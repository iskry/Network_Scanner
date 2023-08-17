# Network Scanner

This script allows users to quickly scan a given IP range to identify devices on their network and retrieve their MAC addresses.

## Prerequisites

- Python 2.x
- `scapy`
- `optparse`

## Installation

1. Clone the repository:

` git clone https://github.com/iskry/Network_Scanner.git `

2. Navigate to the directory:

` cd path-to-directory `

3. Install required Python packages:

` pip install scapy optparse `

## Usage

To use the script, run:

` python network_scanner.py -t <target-ip-range> `

For example, to scan the IP range `192.168.1.0/24`:

` python network_scanner.py -t 192.168.1.0/24 `

## Output

Upon running the script, you will receive an output of IP addresses and their corresponding MAC addresses.

## License

This project is licensed under the MIT License. For more details, see the LICENSE file in this repository.



