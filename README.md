# SDN_mininet_Port_status_Monitoring
This project demonstrates SDN concepts using Mininet and POX. It shows how a controller can monitor and control network behavior dynamically. The implementation highlights the flexibility and programmability of SDN in handling network events like port failures.

Commands used:
Step 1: Start Controller 
cd pox 
python3.9 pox.py forwarding.l2_learning misc.port_monitor 

Step 2: Start Mininet 
sudo mn --controller=remote --topo single,3 

Step 3: Verify Connectivity 
pingall 

 Step 4: Trigger Port Down Event 
link h1 s1 down 

 Step 5: Trigger Port Up Event 
link h1 s1 up 

 Step 6: View Flow Table 
sudo ovs-ofctl dump-flows s1 

Observations: 

The controller detects port status changes in real-time 
When a port goes down, communication is interrupted 
Flow rules are dynamically updated based on traffic 
Network recovers immediately after port restoration 

Conclusion: 

This project demonstrates SDN concepts using Mininet and POX. 
It shows us how a controller can monitor and control network behavior dynamically.  
The implementation highlights the flexibility and programmability of SDN in handling network events like port failures. 
