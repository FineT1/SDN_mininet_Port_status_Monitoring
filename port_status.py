# Run on POX controller to monitor port status changes
# Run on specific python 3.9 version to avoid compatibility issues with POX
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PortStatus(event):
    port = event.ofp.desc.port_no
    reason = event.ofp.reason
    state = event.ofp.desc.state

    if state == 1:
        log.info(f"Port {port} is DOWN")
    else:
        log.info(f"Port {port} is UP")

def launch():
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)