### Command
ip neigh

### Observation
- Neighbor table contains gateway entry
- MAC address learned via ARP
- State was REACHABLE

### SRE Insight
If ARP resolution fails, IP connectivity will break even if routes exist.
