# How Can I Log In to an ECS After Its System Disk Is Exchanged with That Attached to Another ECS Running the Same OS? <a name="EN-US_TOPIC_0100005619"></a>

## Symptom<a name="section1794885713568"></a>

Two ECSs run the same OS, for example, both run Windows or Linux. The system disks attached to the two ECSs are exchanged offline. After the exchanging, the login keys of the ECSs may change. In such a case, how can I log in to the ECSs?

>![](/images/icon-note.gif) **NOTE:**   
>Before stopping an ECS for disk detachment, release the IP address assigned to the ECS using DHCP so that ECS can correctly obtain an IP address later. To do so, perform the following operations:  
>1.  Log in to the Windows ECS.  
>2.  Run the following command to release the IP address:  
>    **ipconfig /release**  
>    This operation will interrupt network connections and affect the use of the ECS. After the ECS is restarted, network connections will automatically recover.  

## Windows<a name="section129031037631"></a>

For example, there are two Windows ECSs with parameters configured in  [Table 1](#table1365540183310).

**Table  1**  Parameter configurations

<a name="table1365540183310"></a>
<table><thead align="left"><tr id="row96574014338"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.1"><p id="p634128183316"><a name="p634128183316"></a><a name="p634128183316"></a>ECS</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.2"><p id="p76573013311"><a name="p76573013311"></a><a name="p76573013311"></a>System Disk</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.2.4.1.3"><p id="p16576611543"><a name="p16576611543"></a><a name="p16576611543"></a>Key Pair</p>
</th>
</tr>
</thead>
<tbody><tr id="row1765718083310"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="p1565710013339"><a name="p1565710013339"></a><a name="p1565710013339"></a>ecs_01</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.2 "><p id="p15657202333"><a name="p15657202333"></a><a name="p15657202333"></a>vol_01</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.3 "><p id="p9618440846"><a name="p9618440846"></a><a name="p9618440846"></a>Keypair_01</p>
</td>
</tr>
<tr id="row174892462353"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="p2490194613350"><a name="p2490194613350"></a><a name="p2490194613350"></a>ecs_02</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.2 "><p id="p6490174620351"><a name="p6490174620351"></a><a name="p6490174620351"></a>vol_02</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.3 "><p id="p8575613545"><a name="p8575613545"></a><a name="p8575613545"></a>Keypair_02</p>
</td>
</tr>
</tbody>
</table>

System disk vol\_01 is detached from ecs\_01 offline and then attached to ecs\_02 as the system disk. How can I log in to ecs\_02?

The random password for logging in to ecs\_02 must be resolved again. The procedure is as follows:

1.  Delete the initial password for logging in to ecs\_02.

    Locate the row containing ecs\_02, click  **More**  in the  **Operation**  column, and select  **Delete Password**  from the drop-down list. Then, click  **Delete**.

    >![](/images/icon-note.gif) **NOTE:**   
    >ecs\_02 must be in  **Stopped**  state.  

2.  Start ecs\_02.

    Locate the row containing ecs\_02, click  **More**  in the  **Operation**  column, and select  **Start**  from the drop-down list. Then, in the  **Start ECS**  dialog box, click  **OK**.

3.  <a name="li138721252141517"></a>Obtain the password for logging in to ecs\_02.
    1.  Locate the row containing ecs\_02, click  **More**  in the  **Operation**  column, and select  **Get Password**  from the drop-down list.
    2.  Click  **Select File**  and upload private key file  **Keypair\_02**  of ecs\_02.
    3.  Click  **Get Password**  to obtain a new random password.

4.  Use the random password obtained in step  [3](#li138721252141517)  to log in to ecs\_02 with the system disk replaced.

## Linux<a name="section1756045025614"></a>

For example, there are two Linux ECSs with parameters configured in  [Table 2](#table9561950195614).

**Table  2**  Parameter configurations

<a name="table9561950195614"></a>
<table><thead align="left"><tr id="row1656285019569"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p1562135011562"><a name="p1562135011562"></a><a name="p1562135011562"></a>ECS</p>
</th>
<th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p125626503566"><a name="p125626503566"></a><a name="p125626503566"></a>System Disk</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.3"><p id="p105632050125614"><a name="p105632050125614"></a><a name="p105632050125614"></a>Key Pair</p>
</th>
</tr>
</thead>
<tbody><tr id="row556435013563"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p17564205017567"><a name="p17564205017567"></a><a name="p17564205017567"></a>ecs_01</p>
</td>
<td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p756411505566"><a name="p756411505566"></a><a name="p756411505566"></a>vol_01</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p16564850145611"><a name="p16564850145611"></a><a name="p16564850145611"></a>Keypair_01</p>
</td>
</tr>
<tr id="row6565125085617"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p15565145013568"><a name="p15565145013568"></a><a name="p15565145013568"></a>ecs_02</p>
</td>
<td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p556613502563"><a name="p556613502563"></a><a name="p556613502563"></a>vol_02</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p1566850175616"><a name="p1566850175616"></a><a name="p1566850175616"></a>Keypair_02</p>
</td>
</tr>
</tbody>
</table>

System disk vol\_01 is detached from ecs\_01 offline and then attached to ecs\_02 as the system disk. How can I log in to ecs\_02?

Use either of the following methods to log in to ecs\_02:

-   Use private key file  **Keypair\_01**  of ecs\_01.
-   Use private key file  **Keypair\_02**  of ecs\_02.

