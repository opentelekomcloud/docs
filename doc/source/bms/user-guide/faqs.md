# FAQs<a name="EN-US_TOPIC_0159392326"></a>

## How Do I Enable Layer-3 Communication Between a VMware VM and an ECS Through NSX-Edge?<a name="section486517501272"></a>

To enable this, perform the following operations:

1.  On the VMware platform, provision logical routes and NSX Edge devices using NSX, configure OSPF, and connect an internal interface of the logical router to the logical switch of the VM.
2.  Configure an SNAT rule on NSX Edge, and map the IP address and port of the VMware VM to the IP address and port of Edge uplink.
    -   **Applicable To**:  **uplink**
    -   **Source IP Address/Range**:  **11.11.200.2**
    -   **Protocol**:  **Any**
    -   **Source Port**:  **Any**
    -   **Converted Source IP Address/Range**:  **11.11.11.30**
    -   **Converted Port/Range**:  **Any**


## What Configurations Are Required for Enabling a VMware VM Connected to NSX Edge to Provide Services Through an EIP?<a name="section12317816172816"></a>

To enable a VMware VM to provide services through an EIP, perform the following configurations:

1.  Bind an EIP to the port reserved for the Edge uplink by adding a DNAT rule.

    Assume that the IP address of the port reserved for Edge uplink is 11.11.11.30, and the EIP bound to the port is 188.xxx.xxx.xxx.

2.  Configure a DNAT rule on Edge, and map the IP address and port of the VMware VM to the IP address and port of the Edge uplink.
    -   **Applicable To**:  **uplink**
    -   **Protocol**:  **tcp**
    -   **Original Target IP Address/Range**:  **11.11.11.30**
    -   **Source Port/Range**:  **2201**
    -   **Converted Source IP Address/Range**:  **11.11.200.2**
    -   **Converted Port/Range**:  **22**

        In the preceding example, the configured DNAT rule will convert the packets of 11.11.11.30:2201 into those of 11.11.200.2:22.

        After the configuration is complete, you can access port 2201 of EIP 188.xxx.xxx.xxx, which is converted into port 22 of a VMware VM whose IP address is 11.11.200.2 through DNAT.



