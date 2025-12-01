# Routing Table (ip r)

## Default Route
default via <gateway>

### Observation
- Default route exists via gateway
- Local subnet route present
- Traffic to external networks goes via default gateway
- WSL virtual gateway: `172.xx.xxx.x`
- All outbound traffic flows through this device.
- Routing is simple: 1 default route → NAT → Windows → Wi-Fi → ISP.

### SRE Insight
If default route is missing, external connectivity will fail.

## Meaning:
- This is how system reaches the internet
- If this breaks → No internet, DNS timeouts, curl failures
