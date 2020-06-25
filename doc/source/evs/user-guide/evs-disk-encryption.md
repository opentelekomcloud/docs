# EVS Disk Encryption<a name="evs_01_0001"></a>

## What Is EVS Disk Encryption<a name="section14109833104132"></a>

In case your services require encryption for the data stored on EVS disks, EVS provides you with the encryption function. You can encrypt newly created EVS disks. Keys used by encrypted EVS disks are provided by the Key Management Service \(KMS\), which is secure and convenient. Therefore, you do not need to establish and maintain the key management infrastructure.

## Keys Used for EVS Disk Encryption<a name="section17331463223115"></a>

The keys provided by KMS for disk encryption include a Default Master Key and Customer Master Keys \(CMKs\).

-   Default Master Key: A key that is automatically created by EVS through KMS and named  **evs/default**.

    The Default Master Key cannot be disabled and does not support scheduled deletion.

-   CMKs: Keys created by users. You may use existing CMKs or create new CMKs to encrypt disks. For details, see  **Management**  \>  **Creating a CMK**  in the  _Key Management Service User Guide_.

If disks are encrypted using CMKs and a CMK is then disabled or scheduled for deletion, the disks encrypted by this CMK can no longer be read from or written to and data on these disks may never be restored. See  [Table 1](#table15423135384216)  for more information.

**Table  1**  Impact on encrypted disks after a CMK becomes unavailable

<a name="table15423135384216"></a>
<table><thead align="left"><tr id="row64230539421"><th class="cellrowborder" valign="top" width="26.01260126012601%" id="mcps1.2.4.1.1"><p id="p18423125312425"><a name="p18423125312425"></a><a name="p18423125312425"></a>CMK Status</p>
</th>
<th class="cellrowborder" valign="top" width="39.16391639163916%" id="mcps1.2.4.1.2"><p id="p15423453154211"><a name="p15423453154211"></a><a name="p15423453154211"></a>Impact on Encrypted Disks</p>
</th>
<th class="cellrowborder" valign="top" width="34.823482348234826%" id="mcps1.2.4.1.3"><p id="p104231253114218"><a name="p104231253114218"></a><a name="p104231253114218"></a>How to Restore</p>
</th>
</tr>
</thead>
<tbody><tr id="row114238537426"><td class="cellrowborder" valign="top" width="26.01260126012601%" headers="mcps1.2.4.1.1 "><p id="p8423155312427"><a name="p8423155312427"></a><a name="p8423155312427"></a>Disabled</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="39.16391639163916%" headers="mcps1.2.4.1.2 "><a name="ul7272244174918"></a><a name="ul7272244174918"></a><ul id="ul7272244174918"><li>If an encrypted disk is attached to a <span id="text17694103243220"><a name="text17694103243220"></a><a name="text17694103243220"></a>server</span>, the disk cannot be accessed or data on the disk cannot be restored after a period of time or even permanently. If this disk is detached later, it cannot be attached again.</li><li>If an encrypted disk is not attached to any <span id="text157219412556"><a name="text157219412556"></a><a name="text157219412556"></a>server</span>, it cannot be attached any more.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.823482348234826%" headers="mcps1.2.4.1.3 "><p id="p247893525"><a name="p247893525"></a><a name="p247893525"></a>Enable the CMK. For details, see <strong id="b2017879812"><a name="b2017879812"></a><a name="b2017879812"></a>Managing CMKs</strong> &gt; <strong id="b1729287415"><a name="b1729287415"></a><a name="b1729287415"></a>Enabling One or More CMKs</strong> in the <em id="i1764015025"><a name="i1764015025"></a><a name="i1764015025"></a>Key Management Service User Guide</em>.</p>
</td>
</tr>
<tr id="row194235535421"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p24231953104211"><a name="p24231953104211"></a><a name="p24231953104211"></a>Scheduled deletion</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1811015185215"><a name="p1811015185215"></a><a name="p1811015185215"></a>Cancel the scheduled deletion for the CMK. For details, see <strong id="b1103833508"><a name="b1103833508"></a><a name="b1103833508"></a>Managing CMKs</strong> &gt; <strong id="b1257531488"><a name="b1257531488"></a><a name="b1257531488"></a>Canceling the Scheduled Deletion of One or More CMKs</strong> in the <em id="i407155219"><a name="i407155219"></a><a name="i407155219"></a>Key Management Service User Guide</em>.</p>
</td>
</tr>
<tr id="row84234536424"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p134239539426"><a name="p134239539426"></a><a name="p134239539426"></a>Deleted</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p842375394216"><a name="p842375394216"></a><a name="p842375394216"></a>Data on the disks can never be restored.</p>
</td>
</tr>
</tbody>
</table>

## Who Can Use the Disk Encryption Function?<a name="section4401454411508"></a>

-   The security administrator \(having the Security Administrator rights\) can grant the KMS access rights to EVS for using the disk encryption function.
-   When a common user who does not have the Security Administrator rights needs to use the disk encryption function, the condition varies depending on whether the user is the first one ever in the current region or project to use this feature.
    -   If the common user is the first one ever in the current region or project to use the feature, the user must contact a user having the Security Administrator rights to grant the KMS access rights to EVS. Then, the common user can use the disk encryption function.
    -   If the common user is not the first one ever in the current region or project to use the feature, the common user can use the disk encryption function directly.


From the perspective of a tenant, as long as the KMS access rights have been granted to EVS in a region, all the users in the same region can directly use the disk encryption function.

If there are multiple projects in the current region, the KMS access rights need to be granted to each project in this region.

## Application Scenarios of EVS Disk Encryption<a name="en-us_topic_0047272493_section30754477152516"></a>

[Figure 1](#fig682110438439)  shows the user relationships under regions and projects from the perspective of a tenant. The following example uses region B to describe the two application scenarios of the disk encryption function.

**Figure  1**  User relationships<a name="fig682110438439"></a>  
![](figures/user-relationships.png "user-relationships")

-   If the security administrator uses the encryption function for the first time ever, the operation process is as follows:

    1.  Grant the KMS access rights to EVS.

        After the KMS access rights have been granted, the system automatically creates a Default Master Key and names it  **evs/default**. DMK can be used for disk encryption.

        >![](/images/icon-note.gif) **NOTE:**   
        >The EVS disk encryption relies on KMS. When the encryption function is used for the first time ever, the KMS access rights need to be granted to EVS. After the KMS access rights have been granted, all users in this region can use the encryption function, without requiring the KMS access rights to be granted again.  

    2.  Select a key.

        You can select one of the following keys:

        -   DMK:  **evs/default**
        -   CMKs: Existing or newly created CMKs. For details, see  **Creating a CMK**  in the  _Key Management Service User Guide_.

    After the security administrator has used the disk encryption function, all users in Region B can directly use the encryption function.

-   If User E \(common user\) uses the encryption function for the first time ever, the operation process is as follows:

    1.  When user E uses the encryption function, and the system prompts a message indicating that the KMS access rights have not been granted to EVS.
    2.  Contact the security administrator to grant the KMS access rights to EVS.

    After the KMS access rights have been granted to EVS, User E as well as all users in Region B can directly use the disk encryption function and do not need to contact the security administrator to grant the KMS access rights to EVS again.


