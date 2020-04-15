# What Can I Do If the NIC Names of the DR Drill Server and Production Site Server Are Different?<a name="sdrs_06_0403"></a>

## Symptom<a name="section22559532136"></a>

The production site server runs the SUSE OS. After users create a DR drill using this server, the NIC names of the DR drill server are different from those of the production site server.

The following is an example:

A production site server running Novell SUSE Linux Enterprise Server 12 SP3 64-bit has five NICs attached. Log in to the production site server and query the NIC names \(eth0 to eth4\).

**Figure  1**  Production site server NIC names<a name="fig19543931816"></a>  
![](figures/production-site-server-nic-names.png "production-site-server-nic-names")

Log in to the DR drill server and query the NIC names \(eth5 to eth9\).

**Figure  2**  DR drill server NIC names<a name="fig1295104810131"></a>  
![](figures/dr-drill-server-nic-names.png "dr-drill-server-nic-names")

The NIC names of the DR drill server are different from those of the production site server.

## Root Cause<a name="section67031648161616"></a>

The NIC names may change when users create a DR drill.

## Handling Method<a name="section12474891189"></a>

After the DR drill, delete the  **/etc/udev/rules.d/70-persistent-net.rules**  file on the DR drill server and then restart it. The procedure is as follows.

1.  Log in to the DR drill server.
    1.  Log in to the management console and click  **Elastic Cloud Server**  under  **Computing**.
    2.  In the server list, select the DR drill server.
    3.  Locate the row containing the server and click  **Remote Login**  in the  **Operation**  column.

        Log in to the server as prompted.

2.  Run the following command to delete the file:

    **rm /etc/udev/rules.d/70-persistent-net.rules**

3.  Run the following command to restart the DR drill server:

    **reboot**


