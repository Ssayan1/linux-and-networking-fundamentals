# Routing Table (ip r)

## Default Route
default via <gateway>

### Observation
- Default route exists via gateway
- Local subnet route present
- Traffic to external networks goes via default gateway

### SRE Insight
If default route is missing, external connectivity will fail.

## Meaning:
- This is how your system reaches the internet
- If this breaks → No internet, DNS timeouts, curl failures
