# Configuring SNMP Northbound Interface<a name="EN-US_TOPIC_0125375924"></a>

## Scenario<a name="section732795117183"></a>

You can integrate the alarm and monitoring data of MRS Manager to the network management system \(NMS\) using the Simple Network Management Protocol \(SNMP\).

## Prerequisites<a name="section2874236017183"></a>

-   The corresponding ECS of the interconnected server and the Master node of the MRS cluster are deployed on the same VPC.
-   The Master node can access the IP address and specific ports of the interconnected server.

## Procedure<a name="section1521501017183"></a>

1.  On MRS Manager, click  **System**.
2.  In  **Configuration**, click **Configure SNMP** under **Monitoring and Alarm**.

    The switch of the  **SNMP Service**  is disabled by default. Click the switch to enable the SNMP service

3.  On the displayed page, set SNMP parameters listed in  [Table 1](#table2220034417183):

    **Table  1**  Description of SNMP parameters

    <a name="table2220034417183"></a>
    <table><thead align="left"><tr id="row3246263417183"><th class="cellrowborder" valign="top" width="25.16%" id="mcps1.2.3.1.1"><p id="p1222773517183"><a name="p1222773517183"></a><a name="p1222773517183"></a><strong id="b43099469172052"><a name="b43099469172052"></a><a name="b43099469172052"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="74.83999999999999%" id="mcps1.2.3.1.2"><p id="p5564903017183"><a name="p5564903017183"></a><a name="p5564903017183"></a><strong id="b1396110172052"><a name="b1396110172052"></a><a name="b1396110172052"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3438931117183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p32402859172112"><a name="p32402859172112"></a><a name="p32402859172112"></a><span class="parmname" id="parmname2632302184427"><a name="parmname2632302184427"></a><a name="parmname2632302184427"></a><b>Version</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p7385918172112"><a name="p7385918172112"></a><a name="p7385918172112"></a>Specifies the version of the SNMP protocol. Possible values are:</p>
    <a name="ul66473267172112"></a><a name="ul66473267172112"></a><ul id="ul66473267172112"><li><strong id="b46992337172115"><a name="b46992337172115"></a><a name="b46992337172115"></a>v2c</strong>: an earlier version of SNMP with low security</li><li><strong id="b57708885172112"><a name="b57708885172112"></a><a name="b57708885172112"></a>v3</strong>: the latest version of SNMP with higher security than SNMPv2c</li></ul>
    <p id="p49617923172112"><a name="p49617923172112"></a><a name="p49617923172112"></a>SNMPv3 is recommended.</p>
    </td>
    </tr>
    <tr id="row6506540517183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p4821087117212"><a name="p4821087117212"></a><a name="p4821087117212"></a><span class="parmname" id="parmname11358648184431"><a name="parmname11358648184431"></a><a name="parmname11358648184431"></a><b>Local Port</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p1276650417212"><a name="p1276650417212"></a><a name="p1276650417212"></a>Specifies the local port number. The default value is <strong id="b4778968017212"><a name="b4778968017212"></a><a name="b4778968017212"></a>20000</strong>. The value ranges from&nbsp;<strong id="b2745394217212"><a name="b2745394217212"></a><a name="b2745394217212"></a>1025</strong>&nbsp;to&nbsp;<strong id="b4575889117212"><a name="b4575889117212"></a><a name="b4575889117212"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="row6468578217183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p512659917212"><a name="p512659917212"></a><a name="p512659917212"></a><span class="parmname" id="parmname54255067184442"><a name="parmname54255067184442"></a><a name="parmname54255067184442"></a><b>Read-Only Community</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p1260137017212"><a name="p1260137017212"></a><a name="p1260137017212"></a>Specifies the read-only community name. This parameter is valid when <strong id="b4630347117212"><a name="b4630347117212"></a><a name="b4630347117212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b1407805817212"><a name="b1407805817212"></a><a name="b1407805817212"></a>v2c</strong>.</p>
    </td>
    </tr>
    <tr id="row6269244517183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p6235713717212"><a name="p6235713717212"></a><a name="p6235713717212"></a><span class="parmname" id="parmname9766708184445"><a name="parmname9766708184445"></a><a name="parmname9766708184445"></a><b>Read-Write Community</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p1776335117212"><a name="p1776335117212"></a><a name="p1776335117212"></a>Specifies the write community name. This parameter is valid when <strong id="b2565243617212"><a name="b2565243617212"></a><a name="b2565243617212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b2954533317212"><a name="b2954533317212"></a><a name="b2954533317212"></a>v2c</strong>.</p>
    </td>
    </tr>
    <tr id="row6703633317183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p6371199617212"><a name="p6371199617212"></a><a name="p6371199617212"></a><span class="parmname" id="parmname28748743184455"><a name="parmname28748743184455"></a><a name="parmname28748743184455"></a><b>Security Username</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p6039801417212"><a name="p6039801417212"></a><a name="p6039801417212"></a>Specifies the SNMP security username. This parameter is valid when <strong id="b671122017212"><a name="b671122017212"></a><a name="b671122017212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b6040098117212"><a name="b6040098117212"></a><a name="b6040098117212"></a>v3</strong>.</p>
    </td>
    </tr>
    <tr id="row1211114817183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p890098117212"><a name="p890098117212"></a><a name="p890098117212"></a><span class="parmname" id="parmname45039224184459"><a name="parmname45039224184459"></a><a name="parmname45039224184459"></a><b>Authentication Protocol</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p4989086217212"><a name="p4989086217212"></a><a name="p4989086217212"></a>Specifies the authentication protocol. You are advised to set this parameter to <strong id="b4636458217212"><a name="b4636458217212"></a><a name="b4636458217212"></a>SHA</strong>. This parameter is valid when&nbsp;<strong id="b1462805617212"><a name="b1462805617212"></a><a name="b1462805617212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b6454364717212"><a name="b6454364717212"></a><a name="b6454364717212"></a>v3</strong>.</p>
    </td>
    </tr>
    <tr id="row3917709617183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p900534217212"><a name="p900534217212"></a><a name="p900534217212"></a><span class="parmname" id="parmname5693353318453"><a name="parmname5693353318453"></a><a name="parmname5693353318453"></a><b>Authentication Password</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p5834407317212"><a name="p5834407317212"></a><a name="p5834407317212"></a>Specifies the authentication key. This parameter is valid when <strong id="b5533461317212"><a name="b5533461317212"></a><a name="b5533461317212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b2824947717212"><a name="b2824947717212"></a><a name="b2824947717212"></a>v3</strong>.</p>
    </td>
    </tr>
    <tr id="row5871947717183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p5855668017212"><a name="p5855668017212"></a><a name="p5855668017212"></a><span class="parmname" id="parmname4932767618458"><a name="parmname4932767618458"></a><a name="parmname4932767618458"></a><b>Confirm Password</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p4547066017212"><a name="p4547066017212"></a><a name="p4547066017212"></a>Used to confirm the authentication key. This parameter is valid when <strong id="b658276417212"><a name="b658276417212"></a><a name="b658276417212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b5924487717212"><a name="b5924487717212"></a><a name="b5924487717212"></a>v3</strong>.</p>
    </td>
    </tr>
    <tr id="row1273227217183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p3851619217212"><a name="p3851619217212"></a><a name="p3851619217212"></a><span class="parmname" id="parmname11018081184513"><a name="parmname11018081184513"></a><a name="parmname11018081184513"></a><b>Encryption Protocol</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p3280384717212"><a name="p3280384717212"></a><a name="p3280384717212"></a>Specifies the encryption protocol. You are advised to set this parameter to <strong id="b2679917017212"><a name="b2679917017212"></a><a name="b2679917017212"></a>AES256</strong>. This parameter is valid when&nbsp;<strong id="b3986594217212"><a name="b3986594217212"></a><a name="b3986594217212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b2324916517212"><a name="b2324916517212"></a><a name="b2324916517212"></a>v3</strong>.</p>
    </td>
    </tr>
    <tr id="row732697317183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p3720769517212"><a name="p3720769517212"></a><a name="p3720769517212"></a><span class="parmname" id="parmname26574381184518"><a name="parmname26574381184518"></a><a name="parmname26574381184518"></a><b>Encryption Password</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p6103328817212"><a name="p6103328817212"></a><a name="p6103328817212"></a>Specifies the encryption key. This parameter is valid when <strong id="b1242868017212"><a name="b1242868017212"></a><a name="b1242868017212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b4474925717212"><a name="b4474925717212"></a><a name="b4474925717212"></a>v3</strong>.</p>
    </td>
    </tr>
    <tr id="row6674865217183"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.2.3.1.1 "><p id="p730075717212"><a name="p730075717212"></a><a name="p730075717212"></a><span class="parmname" id="parmname57962784184533"><a name="parmname57962784184533"></a><a name="parmname57962784184533"></a><b>Confirm Password</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74.83999999999999%" headers="mcps1.2.3.1.2 "><p id="p5449048317212"><a name="p5449048317212"></a><a name="p5449048317212"></a>Used to confirm the encryption key. This parameter is valid when <strong id="b2065230417212"><a name="b2065230417212"></a><a name="b2065230417212"></a>Version</strong>&nbsp;is set to&nbsp;<strong id="b5165301317212"><a name="b5165301317212"></a><a name="b5165301317212"></a>v3</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >-   The values of  **Authentication Password** and **Encryption Password**  must contain 8 to 16 characters. At least three of the following types of character must be used: uppercase letters, lowercase letters, digits, and special characters. The passwords must be different and cannot be the same as the security username or the security username written backwards.  
    >-   For security purposes, periodically change the values of  **Authentication Password** and **Encryption Password**  if the SNMP protocol is used.  
    >-   If SNMPv3 is used, a security user will be locked if authentication fails five consecutive times in a 5-minute window. They will be unlocked 5 minutes later.  

4.  Click  **Create Trap Target** under **Trap Target**, and set the following parameters in the **Create Trap Target**  dialog box:

    -   **Target Symbol**

        Specifies the ID of the Trap target. This is generally the ID of the network management or host that receives Trap. The value consists of 1 to 255 characters, including letters and digits.

    -   **Target IP Address**

        Specifies the target IP address. The value of this parameter can be set to an IP address of A, B, or C class and can communicate with the IP address of the management plane on the management node.

    -   **Target Port**

        Specifies the port that receives Trap. The value of this parameter must be that same as that on the peer end and ranges from 0 to 65535.

    -   **Trap Community**

        Specifies the trap community name. This parameter is valid when  **Version**  is set to **v2c**.

    Click  **OK**  to finish the settings and exit the **Create Trap Target**  dialog box.

5.  Click  **OK**.

