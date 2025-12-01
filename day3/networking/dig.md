# DNS Lookup with `dig`

## Command
```
dig google.com
```

## Output (WSL)
```
google.com.  35  IN  A  172.217.26.14
SERVER: 8.8.8.8#53
```

## Analysis
- DNS resolver is configured correctly.
- Response comes from Google Public DNS (8.8.8.8).
- Single IPv4 A record resolved.
- Low query time → good network connectivity.

---

