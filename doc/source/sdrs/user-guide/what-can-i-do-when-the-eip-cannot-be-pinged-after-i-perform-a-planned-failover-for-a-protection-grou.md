# What Can I Do When the EIP Cannot Be Pinged After I Perform a Planned Failover for a Protection Group Containing a SUSE Server?<a name="sdrs_06_0402"></a>

## Symptom<a name="section22559532136"></a>

The production site server in a protection group runs the SUSE OS. After users enable protection and perform a planned failover for the protection group, the EIP of the server cannot be pinged.

## Root Cause<a name="section67031648161616"></a>

After the planned failover, the server NIC name may already change. If the NIC has an EIP bound, the EIP cannot be pinged.

## Handling Method<a name="section12474891189"></a>

After the planned failover, delete the  **/etc/udev/rules.d/70-persistent-net.rules**  file on the DR site server and then restart it. The procedure is as follows.

1.  Log in to the DR site server.
    1.  Log in to the management console and click  **Elastic Cloud Server**  under  **Computing**.
    2.  In the server list, select the DR site server.
    3.  Locate the row containing the server and click  **Remote Login**  in the  **Operation**  column.

        Log in to the server as prompted.

2.  Run the following command to delete the file:

    **rm /etc/udev/rules.d/70-persistent-net.rules**

3.  Run the following command to restart the DR site server:

    **reboot**


