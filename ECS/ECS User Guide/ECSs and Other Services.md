### ECSs and Other Services

-   Auto Scaling (AS)

    Automatically adjusts ECS service resources based on the configured AS policies.This improves resource usage and reduces resource costs.

-   Elastic Load Balance (ELB)

    Automatically distributes traffic to multiple ECSs. This enhances system service and fault tolerance capabilities.

-   Elastic Volume Service (EVS)

    Enables you to attach EVS disks to an ECS and expand their capacity.

-   Virtual Private Cloud (VPC)

    Enables you to configure internal networks and change network configurations by customizing security groups, VPNs, IP address segments, and bandwidth. This simplifies network management. You can also customize the ECS access rules within a security group and between security groups to strengthen ECS security protection.

-   Image Management Service (IMS)

    Enables you to create ECSs using images. This improves the efficiency of ECS
    creation.

-   Cloud Eye (CES)

    Allows you to check the status of monitored service objects after you have obtained an ECS. This can be done without requiring additional plug-ins be installed. Table 1-16 lists the ECS metrics supported by CES.

   **Table 1-1** ECS monitoring metrics 
<table>
      <tr>
         <th>Metric</th>
         <th>Description</th>
         <th>Formula</th>
         <th>Remarks</th>
      </tr>
      <tr>
         <td>CPU Usage</td>
         <td>Indicates the CPU usage (%) of an ECS.</td>
         <td>CPU usage of an ECS/Number of CPU cores in the ECS</td>
         <td>N/A</td>
      </tr>
      <tr>
         <td>Memory Usage</td>
         <td>Indicates the memory usage (%) of an ECS.</td>
         <td>Used memory of an ECS/Total memory of the ECS</td>
         <td>This metric is unavailable if the image has no OTC Tools installed.</td>
      </tr>
      <tr>
         <td>Disk Usage</td>
         <td>Indicates the disk usage (%) of an ECS.</td>
         <td>Used capacity of an ECS disk/Total capacity of the ECS disk</td>
         <td>This metric is unavailable if the image has no OTC Tools installed.</td>
      </tr>
      <tr>
         <td>Disks Read Rate</td>
         <td>Indicates the number of bytes read from an ECS per second.</td>
         <td>Total number of bytes read from an ECS disk/Monitoring period</td>
         <td>byte_out = (rd_bytes - last_rd_bytes) /Time difference</td>
      </tr>
      <tr>
         <td>Disks Write Rate</td>
         <td>Indicates the number of bytes written to an ECS per second.</td>
         <td>Total number of bytes written to an ECS disk/Monitoring period</td>
         <td>N/A</td>
      </tr>
      <tr>
         <td>Disks Read Requests</td>
         <td>Indicates the number of read requests sent to an ECS per second.</td>
         <td>Total number of read requests sent to an ECS disk/Monitoring period</td>
         <td>req_out = (rd_req - last_rd_req)/Time difference</td>
      </tr>
      <tr>
         <td>Disks Write Requests</td>
         <td>Indicates the number of write requests sent to an ECS per second.</td>
         <td>Total number of write requests sent to an ECS disk/Monitoring period</td>
         <td>req_in = (wr_req - last_wr_req)/Time difference</td>
      </tr>
      <tr>
         <td>Inband Incoming Rate</td>
         <td>Indicates the number of incoming bytes on an ECS per second.</td>
         <td>Total number of inband incoming bytes on an ECS/Monitoring period</td>
         <td>N/A</td>
      </tr>
      <tr>
         <td>Inband Outgoing Rate</td>
         <td>Indicates the number of outgoing bytes on an ECS per second.</td>
         <td>Total number of inband outgoing bytes on an ECS/Monitoring period</td>
         <td>N/A</td>
      </tr>
      <tr>
         <td>Outband Incoming Rate</td>
         <td>Indicates the number of incoming bytes on an ECS per second at the virtualization layer.</td>
         <td>Total number of outband incoming bytes on an ECS/Monitoring period</td>
         <td>This metric is unavailable if SR-IOV is enabled.</td>
      </tr>
      <tr>
         <td>Outband Outgoing Rate</td>
         <td>Indicates the number of outgoing bytes on an ECS per second at the virtualization layer.</td>
         <td>Total number of outband outgoing bytes on an ECS/Monitoring period</td>
         <td>This metric is unavailable if SR-IOV is enabled.</td>
      </tr>
      <tr>
         <td>Failed to check the system status</td>
         <td>This metric is used to monitor the cloud platform on which ECSs run.</td>
         <td>The system periodically checks the system status and returns check results using value 0 or 1.
         <ul>
            <li>0: The system is running properly. All check items are normal.</li>
            <li>1: The system is not running properly. One or multiple check items are abnormal.</li></td>
         <td>When the power source of the physical host fails or the hardware/software becomes faulty, the check result is 1.</td>
      </tr>
      <tr>
         <td>InfiniBand NIC status</td>
         <td>This metric is used to monitor the status of an InfiniBand NIC on a high-performance h2 ECS to ensure proper InfiniBand NIC running.
         <b>NOTE:</b>
         <dd>Only Mellanox EDL 100 GB single-port InfiniBand NICs are supported.</dd></td>
         <td>The system periodically checks the system status and returns check results using value 0 or 1.
         <ul>
            <li>0: The system is running properly. That is, the InfiniBand NIC is functional.</li>
            <li>1: The system is not running properly. That is, the InfiniBand NIC malfunctions.</li></ul></td>
         <td>When the physical NIC corresponding to a virtual NIC becomes faulty, for example, the network cable is not securely connected to the NIC, the switch or adapter is incompatible with the InifiniBand NIC, or the NIC is disabled, the returned value is 1.</td>
      </tr>
</table>

-   Key Management Service (KMS)

    The encryption feature relies on KMS. You can use an encrypted image or EVS disks when creating an ECS. In such a case, you are required to use the key provided by KMS to improve data security.
