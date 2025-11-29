```bash
#!/bin/bash

echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo
echo "Memory Usage:"
free -m

echo
echo "Disk Usage:"
df -h | grep '^/dev/'
```
