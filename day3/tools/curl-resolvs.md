# DNS Override Testing — `curl --resolve`

## Command
```
curl -v https://google.com --resolve google.com:443:172.217.26.14
```

## Purpose
Force curl to use a specific IP, bypassing DNS.

## Uses

- Test load balancer nodes  
- Debug DNS outages  
- Validate certificates even when DNS is broken  
- Test new deployments before DNS switch  
- Do canary testing without routing traffic through DNS  

## Output Summary
- Successfully connected  
- TLS validated correctly  
- Same 301 redirect as expected  
