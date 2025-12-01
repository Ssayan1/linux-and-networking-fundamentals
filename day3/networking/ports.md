- LISTEN      – Server socket is open and waiting for incoming connections
- ESTABLISHED – Active TCP connection with data transfer possible
- TIME_WAIT  – Normal state during connection teardown; ensures late packets are handled
- CLOSE_WAIT – Remote side closed connection, but local application has not yet closed the socket (often indicates application bug)

---

### Command
```bash
ss -tulnp
```
### Purpose
List listening TCP/UDP sockets and their owning processes.

## Findings
System is running:
- Local DNS stubs (127.X.X.53, 127.X.X.XX)  
- Web servers (Apache on 80, nginx on 80)  
- Ubuntu snap services  
- DNS proxies (10.XXX.XXX.XXX:53)

### SRE Insight
Used to verify whether a service is listening on the expected port when
debugging connectivity or firewall issues.
