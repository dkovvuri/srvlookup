# SRV Lookup Utility

Helper Utility to Lookup SRV Records

## Installation:

- Install required dependencies:

```
pip install -r requirements.txt
```

## Usage:

```
python3 ./lookup.py -d test.local

optional arguments:
  -h, --help            show this help message and exit

Required Arguments:
  -d DOMAIN, --domain DOMAIN
                        FQDN to fetch the SRV records for
```

## Response Structure:

```json
{
    "weight": 1,
    "priority": 1,
    "host": "6f5d301f9a3f40239fb0388405b0edd5.test.local",
    "port": 80,
    "resolved_addresses": [
        "172.31.174.95"
    ]
}
```
