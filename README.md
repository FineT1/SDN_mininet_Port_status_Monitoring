# SDN_mininet_Port_status_Monitoring
This project demonstrates SDN concepts using Mininet and POX. It shows how a controller can monitor and control network behavior dynamically. The implementation highlights the flexibility and programmability of SDN in handling network events like port failures.

Commands used:
Step 1: Start Controller 
cd pox 
python3.9 pox.py forwarding.l2_learning misc.port_monitor 
<img width="807" height="181" alt="forward_monitor_pox_check" src="https://github.com/user-attachments/assets/e032825f-d3eb-4248-91ae-4a22ff95e25d" />


Step 2: Start Mininet 
sudo mn --controller=remote --topo single,3 
<img width="736" height="505" alt="miniet_topology_creation" src="https://github.com/user-attachments/assets/5469ed74-a60a-4b35-b965-9f716f2d7f33" />


Step 3: Verify Connectivity 
pingall 


 Step 4: Trigger Port Down Event 
link h1 s1 down 
<img width="413" height="207" alt="after_h1_down" src="https://github.com/user-attachments/assets/447ca3bd-2f30-4c87-bdf2-6de97aec42a0" />


 Step 5: Trigger Port Up Event 
link h1 s1 up 
<img width="905" height="215" alt="port_up_down_check" src="https://github.com/user-attachments/assets/038e7188-971b-4eb3-82b5-9a73f052421e" />


 Step 6: View Flow Table 
sudo ovs-ofctl dump-flows s1 
<img width="1074" height="592" alt="flow_table_screenshot" src="https://github.com/user-attachments/assets/67523070-ff63-44a4-b5d5-ee933f0514d0" />


Observations: 

The controller detects port status changes in real-time 
When a port goes down, communication is interrupted 
Flow rules are dynamically updated based on traffic 
Network recovers immediately after port restoration 

Conclusion: 

This project demonstrates SDN concepts using Mininet and POX. 
It shows us how a controller can monitor and control network behavior dynamically.  
The implementation highlights the flexibility and programmability of SDN in handling network events like port failures. 
