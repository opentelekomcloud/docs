# Why Is Not Connected Displayed as the Status for a Successfully Created VPN?<a name="vpn_07_0008"></a>

After a VPN is created, its status changes to  **Normal**  only after the VMs or physical servers on the two sides of the VPN communicate with each other. 

-   IKE v1:

    If no traffic goes through the VPN for a period of time, the VPN needs to be renegotiated. The negotiation time depends on the value of  **Lifecycle \(s\)**  in the IPsec policy. Generally, the value of  **Lifecycle \(s\)**  is  **3600**  \(1 hour\), indicating that the negotiation will be initiated in the fifty-fourth minute. If the negotiation succeeds, the connection remains to the next round of negotiation. If the negotiation fails, the status is set to be disconnected within one hour. The connection can be restored after the two sides of the VPN communicates with each other. The disconnection can be avoided by using a network monitoring tool, such as IP SLA, to generate packets.

-   IKE v2: If no traffic goes through the VPN for a period of time, the VPN remains in the connected status.

