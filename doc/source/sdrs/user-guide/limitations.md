# Limitations<a name="EN-US_TOPIC_0110981899"></a>

Before using this service, you should be aware of the limitations listed in  [Table 1](#table14007370).

**Table  1**  Limitations

<a name="table14007370"></a>
<table><thead align="left"><tr id="row9030085"><th class="cellrowborder" valign="top" width="19.259999999999998%" id="mcps1.2.3.1.1"><p id="p60348264"><a name="p60348264"></a><a name="p60348264"></a><strong id="b10890753010"><a name="b10890753010"></a><a name="b10890753010"></a>Limitation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="80.74%" id="mcps1.2.3.1.2"><p id="p37578639"><a name="p37578639"></a><a name="p37578639"></a><strong id="b14114187173016"><a name="b14114187173016"></a><a name="b14114187173016"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1646139131316"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p44719395133"><a name="p44719395133"></a><a name="p44719395133"></a>Computing</p>
</td>
<td class="cellrowborder" valign="top" width="80.74%" headers="mcps1.2.3.1.2 "><p id="p348139101311"><a name="p348139101311"></a><a name="p348139101311"></a>SDRS does not support ECSs of the GPU-accelerated and FPGA-accelerated types.</p>
</td>
</tr>
<tr id="row14412003"><td class="cellrowborder" rowspan="2" valign="top" width="19.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p26521624"><a name="p26521624"></a><a name="p26521624"></a>Replication</p>
</td>
<td class="cellrowborder" valign="top" width="80.74%" headers="mcps1.2.3.1.2 "><div class="p" id="p12111630984"><a name="p12111630984"></a><a name="p12111630984"></a>Server limitations<a name="ul17410181318112"></a><a name="ul17410181318112"></a><ul id="ul17410181318112"><li>The <span id="text164511550123112"><a name="text164511550123112"></a><a name="text164511550123112"></a>server</span><span id="text1240115317318"><a name="text1240115317318"></a><a name="text1240115317318"></a></span>s must be from different AZs of the same region.</li><li class="msonormal">Bare Metal Server (BMS) is not supported.</li><li>Servers of following types cannot be used to create protected instances:<a name="ul102821376910"></a><a name="ul102821376910"></a><ul id="ul102821376910"><li>Large Memory (Xen): This type of servers is bound to InfiniBand NICs.</li></ul>
<a name="ul147981058919"></a><a name="ul147981058919"></a><ul id="ul147981058919"><li>Disk Intensive I (Xen): This type of servers has local disks.</li><li>Disk Intensive II (KVM): This type of ECSs has local disks.</li><li>Servers attached with shared disks</li></ul>
<div class="note" id="note472420152612"><a name="note472420152612"></a><a name="note472420152612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1381019588914"><a name="p1381019588914"></a><a name="p1381019588914"></a>You can create a replication pair using shared disks in the <strong id="b71612129162"><a name="b71612129162"></a><a name="b71612129162"></a>Available</strong> state and attach the replication pair to a protected instance.</p>
<p id="p172414156613"><a name="p172414156613"></a><a name="p172414156613"></a>A replication pair consisting of shared disks can be attached to multiple protected instances.</p>
</div></div>
</li></ul>
</div>
</td>
</tr>
<tr id="row1133243715715"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1521442613815"><a name="p1521442613815"></a><a name="p1521442613815"></a>Disk limitations</p>
<a name="ul868528192610"></a><a name="ul868528192610"></a><ul id="ul868528192610"><li>Disks which have been used to create replication pairs do not support deletion or data rollback using snapshots.</li><li>High I/O (performance-optimized I) and ultra-high I/O (latency-optimized) disks can be attached to SAP HANA ECSs, HPC ECSs, and HL1 ECSs. However, these types of disks cannot be used to create replication pairs due to InfiniBand network limitations.</li></ul>
</td>
</tr>
<tr id="row11877063"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p22518022"><a name="p22518022"></a><a name="p22518022"></a>Storage</p>
</td>
<td class="cellrowborder" valign="top" width="80.74%" headers="mcps1.2.3.1.2 "><p id="p117111453153318"><a name="p117111453153318"></a><a name="p117111453153318"></a>Only servers using EVS can use this service.</p>
</td>
</tr>
<tr id="row41075474"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p38779059"><a name="p38779059"></a><a name="p38779059"></a>Application</p>
</td>
<td class="cellrowborder" valign="top" width="80.74%" headers="mcps1.2.3.1.2 "><p id="p474492411387"><a name="p474492411387"></a><a name="p474492411387"></a>Storage-based synchronous replication ensures disk data consistency but cannot ensure application consistency. If your applications support crash consistency, the applications can run and be replicated on devices supporting replication. </p>
</td>
</tr>
<tr id="row19705455"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p52638042"><a name="p52638042"></a><a name="p52638042"></a>Deployment model</p>
</td>
<td class="cellrowborder" valign="top" width="80.74%" headers="mcps1.2.3.1.2 "><p id="p146641210171919"><a name="p146641210171919"></a><a name="p146641210171919"></a><strong id="b107412895217"><a name="b107412895217"></a><a name="b107412895217"></a>VPC migration</strong>: The <span id="text15343104716308"><a name="text15343104716308"></a><a name="text15343104716308"></a>server</span><span id="text203431747183014"><a name="text203431747183014"></a><a name="text203431747183014"></a></span>s at the production and DR sites are in the same VPC. NIC migration and multiple NICs are supported for each <span id="text13674853205220"><a name="text13674853205220"></a><a name="text13674853205220"></a>server</span><span id="text667718535526"><a name="text667718535526"></a><a name="text667718535526"></a></span>. </p>
</td>
</tr>
<tr id="row895715810316"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p8958287314"><a name="p8958287314"></a><a name="p8958287314"></a>Backup and restoration</p>
</td>
<td class="cellrowborder" valign="top" width="80.74%" headers="mcps1.2.3.1.2 "><p id="p1958138138"><a name="p1958138138"></a><a name="p1958138138"></a>Only servers at the production site can be backed up and restored. Servers at the DR site can only be backed up.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>If the AZ of the production site becomes faulty, you can use the DR drill function to restore the server services in the AZ.  

## Restrictions on Logging In to a Server After You Perform a Planned Failover, Failover, or DR Drill for the First Time<a name="section330514140125"></a>

-   For servers with Cloud-Init/Cloudbase-Init installed, after you perform a planned failover, failover, or DR drill for the first time, Cloud-Init/Cloudbase-Init will start when the servers start for the first time to inject the initial data. The password or key pair for logging in to the production site server, DR site server, or DR drill server will change.
-   For servers without Cloud-Init/Cloudbase-Init installed, the password or key pair for logging in to the production site, DR site server, or DR drill server will not change after you perform a planned failover or failover for the first time.

The following describes an example of server login restrictions after you perform a planned failover or failover for the first time. For details about the login restrictions for the DR drill server, see the login restrictions for the DR site server in this scenario.

Server A and server B are deployed. After the first time planned failover or failover, the production site server and DR site server are listed as follows.

**Table  2**  Production site and DR site servers after a planned failover or failover

<a name="table92017496206"></a>
<table><thead align="left"><tr id="row92016497207"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p22014982019"><a name="p22014982019"></a><a name="p22014982019"></a>-</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12201349182012"><a name="p12201349182012"></a><a name="p12201349182012"></a>Production Site Server</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p721184962020"><a name="p721184962020"></a><a name="p721184962020"></a>DR Site Server</p>
</th>
</tr>
</thead>
<tbody><tr id="row19211749182018"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p142194942018"><a name="p142194942018"></a><a name="p142194942018"></a>Before</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5219498200"><a name="p5219498200"></a><a name="p5219498200"></a>A</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16219493202"><a name="p16219493202"></a><a name="p16219493202"></a>B</p>
</td>
</tr>
<tr id="row1221114972012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p102184942014"><a name="p102184942014"></a><a name="p102184942014"></a>After</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p421849152011"><a name="p421849152011"></a><a name="p421849152011"></a>B</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p82104942011"><a name="p82104942011"></a><a name="p82104942011"></a>A</p>
</td>
</tr>
</tbody>
</table>

In this case, the detailed login restrictions are as follows:

Scenario 1: Server A runs Windows and does not have Cloudbase-Init installed. After the first time planned failover or failover:

-   If you choose to use a password for the server login, use the password of server A to log in to the production site server B or DR site server A.
-   If you choose to use a key pair for the server login, use the password obtained from server A to log in to the production site server B or DR site server A.

>![](/images/icon-note.gif) **NOTE:**   
>From the second time planned failover or failover, the login password or key pair of the server without Cloudbase-Init installed will remain the same. Take servers listed in  [Table 2](#table92017496206)  as an example.  
>You can use the password of server A to log in to the production site server or DR site server.  

Scenario 2: Server A runs Windows and already has Cloudbase-Init installed. After the first time planned failover or failover:

-   If you choose to use a password for the server login, check whether Cloudbase-Init is started.

    If Cloudbase-Init is not started \(normally within three to five minutes after the production site server starts\), you can use the password of server B for the login.

    After the Cloudbase-Init is started, the login password of server B set before the planned failover or failover becomes invalid. You need to reset the login password of server B and then use the new password to log in to server B.

-   If you choose to use a key pair for the server login, check whether Cloudbase-Init is started.

    If Cloudbase-Init is not started \(normally within three to five minutes after the production site server starts\), you can use the password of server B for the login.

    After the Cloudbase-Init is started, the login password of server B obtained before the planned failover or failover becomes invalid. You need to obtain the login password of server B again.


>![](/images/icon-note.gif) **NOTE:**   
>From the second time planned failover or failover, the login password or key pair of the server with Cloudbase-Init installed will remain the same. Take servers listed in  [Table 2](#table92017496206)  as an example.  
>-   Login using a password: Reset the password of server B and use the new password to log in to server B after the first time planned failover or failover.  
>-   Login using a key pair: Obtain the password of server B and use the obtained password to log in to server B after the first time planned failover or failover.  

Scenario 3: Server A runs Linux. After the first time planned failover or failover:

-   If you choose to use a password for the server login, use the password of server A to log in to the production site server B or DR site server A. 

    If the login password of server A is not changed before the planned failover or failover, use the login password configured when server A is created after the planned failover or failover. 

    If the login password of server A is changed before the planned failover or failover, use the new login password after the planned failover or failover.

    >![](/images/icon-note.gif) **NOTE:**   
    >For ECSs running OSs other than CoreOS, the login password does not change after the first-time planned failover or failover.  
    >For ECSs running CoreOS, the login password of server A will restore to the initial one after the first-time planned failover or failover. Therefore, you need to use the login password configured when server A is created to log in to production site server A or DR site server B.  

-   If you choose to use a key pair for the server login, use the key pair of server A to log in to the production site server B or DR site server A in SSH mode. 

