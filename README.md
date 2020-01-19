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
    "records": [
        {
            "weight": 1,
            "priority": 1,
            "host": "139cf6ac648d424fb5c16e0ba7d356a2.test.local",
            "port": 80,
            "resolvedAddresses": [
                "172.31.162.0"
            ]
        },
        {
            "weight": 1,
            "priority": 1,
            "host": "2c78380f190b43b1a45fa2c4be14d4d3.test.local",
            "port": 80,
            "resolvedAddresses": [
                "172.31.163.160"
            ]
        },
        {
            "weight": 1,
            "priority": 1,
            "host": "530966ee05f74230a3e7de67f4f0f2e9.test.local",
            "port": 80,
            "resolvedAddresses": [
                "172.31.163.90"
            ]
        }
     ]
 }
```
