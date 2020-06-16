# ALM-20002 Hue Service Unavailable<a name="EN-US_TOPIC_0125376117"></a>

## Description<a name="s8532b34c48f44d8c8c2222ac741d1946"></a>

The system checks the Hue service status every 60 seconds. This alarm is generated when the Hue service is unavailable and is cleared when the Hue service recovers.

## Attribute<a name="s111d268235864fa2ab4995a038ec69b9"></a>

<a name="te76ade421865448abc1a7daa6735480a"></a>
<table><thead align="left"><tr id="r4f530dc45fa342b6aa8888c12fa75cd1"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a477e6b712fe44a8ebd707691382a831b"><a name="a477e6b712fe44a8ebd707691382a831b"></a><a name="a477e6b712fe44a8ebd707691382a831b"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ae8a69a0c4f7f4511829017f7bf5078e5"><a name="ae8a69a0c4f7f4511829017f7bf5078e5"></a><a name="ae8a69a0c4f7f4511829017f7bf5078e5"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a884043e7c0b74a21af43069cbd8e59fe"><a name="a884043e7c0b74a21af43069cbd8e59fe"></a><a name="a884043e7c0b74a21af43069cbd8e59fe"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r480b9045210f41ab82ca146040a14f73"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ad1f8e895bf83467fbf45c6696be1d5fb"><a name="ad1f8e895bf83467fbf45c6696be1d5fb"></a><a name="ad1f8e895bf83467fbf45c6696be1d5fb"></a>20002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ab7c9c061cf9945d4a5d6f62b0702e26d"><a name="ab7c9c061cf9945d4a5d6f62b0702e26d"></a><a name="ab7c9c061cf9945d4a5d6f62b0702e26d"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="abf73f4acba044494a30609ac075e29eb"><a name="abf73f4acba044494a30609ac075e29eb"></a><a name="abf73f4acba044494a30609ac075e29eb"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sd4076027b44143278b7cb2b9a54b59af"></a>

<a name="ta479351bc74747608b577232eb3ead45"></a>
<table><thead align="left"><tr id="r8dd0f9da1a7c4c7fa36a060119290409"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a1abafcfb605a41f6b7f118bc20f3636e"><a name="a1abafcfb605a41f6b7f118bc20f3636e"></a><a name="a1abafcfb605a41f6b7f118bc20f3636e"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="af5e9962509dc470188b7dfaa670704a5"><a name="af5e9962509dc470188b7dfaa670704a5"></a><a name="af5e9962509dc470188b7dfaa670704a5"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="re6a080eb05b14e41bb3b0bd5b8c643e6"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="afd4d0c6fe8a54e50b11d05c75ae17dc3"><a name="afd4d0c6fe8a54e50b11d05c75ae17dc3"></a><a name="afd4d0c6fe8a54e50b11d05c75ae17dc3"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6a7028fbd447438d96f1873fc7a089f4"><a name="a6a7028fbd447438d96f1873fc7a089f4"></a><a name="a6a7028fbd447438d96f1873fc7a089f4"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r5e2a1073989440f98df87d9d44aa3475"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a4260c6dc23b1414281c640d5fe744236"><a name="a4260c6dc23b1414281c640d5fe744236"></a><a name="a4260c6dc23b1414281c640d5fe744236"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8d67dabe65004a969c12e40fdd8750da"><a name="a8d67dabe65004a969c12e40fdd8750da"></a><a name="a8d67dabe65004a969c12e40fdd8750da"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r034fda736fa24dbb84625d28751e16f6"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa6aaaab13bb748beb5a12e7af23fdedb"><a name="aa6aaaab13bb748beb5a12e7af23fdedb"></a><a name="aa6aaaab13bb748beb5a12e7af23fdedb"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="abf3b97ac9e9a4eb697e7295f478f36e7"><a name="abf3b97ac9e9a4eb697e7295f478f36e7"></a><a name="abf3b97ac9e9a4eb697e7295f478f36e7"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8366e9a4ac1240a88f1d9143d03bfe66"></a>

The system cannot provide data loading, query, and extraction services.

## Possible Causes<a name="s14d211ed1cb642358de340d724240fb4"></a>

-   The internal KrbServer service on which the Hue service depends is abnormal.
-   The internal DBService service on which the Hue service depends is abnormal.
-   The network connection to the DBService is abnormal.

## Procedure<a name="s7224757486974dda942204380a72ab5a"></a>

**Check whether the KrbServer is abnormal.**

1.  On the MRS Manager home page, click  **Service**. In the service list, check whether the **KrbServer** health status is **Good**.
    -   If yes, go to  [4](#l3d9d0c62e49f45bfa98f6ecdb3986401).
    -   If no, go to  [2](#l74a4e457ce2e48b3af82d57f43725f69).

2.  <a name="l74a4e457ce2e48b3af82d57f43725f69"></a>Click  **Restart** in the **Operation**  column of the KrbServer to restart the KrbServer.
3.  Wait several minutes, and check whether  **ALM-20002 Hue Service Unavailable**  is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [4](#l3d9d0c62e49f45bfa98f6ecdb3986401).


**Check whether the DBService is abnormal.**

1.  <a name="l3d9d0c62e49f45bfa98f6ecdb3986401"></a>On the MRS Manager home page, click  **Service**.
2.  In the service list, check whether the  **DBService** health status is **Good**.
    -   If yes, go to  [8](#l0d96f89170974af9a390d2d91562b400).
    -   If no, go to  [6](#l122f87021bcf407f827413c337789db7).

3.  <a name="l122f87021bcf407f827413c337789db7"></a>Click  **Restart** in the **Operation**  column of the DBService to restart the DBService.

    >![](/images/icon-note.gif) **NOTE:**   
    >To restart the service, enter the MRS Manager administrator password and select  **Start or restart related services.**.  

4.  Wait several minutes, and check whether  **ALM-20002 Hue Service Unavailable**  is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [8](#l0d96f89170974af9a390d2d91562b400).


**Check whether the network connection to the DBService is normal.**

1.  <a name="l0d96f89170974af9a390d2d91562b400"></a>Choose  **Service** \> **Hue** \> **Instance**, record the IP address of the active Hue.
2.  Use PuTTY to log in to the active Hue.
3.  Run the  **ping**  command to check whether communication between the host that runs the active Hue and the hosts that run the DBService is normal. \(Obtain the IP addresses of the hosts that run the DBService in the same way as that for obtaining the IP address of the active Hue.\)
    -   If yes, go to  [13](#l8533eba5c6d44bc88f00b63994de5b8e).
    -   If no, go to  [11](#l89904ab8b6c04e1783a2b2465bdd0614).

4.  <a name="l89904ab8b6c04e1783a2b2465bdd0614"></a>Contact the administrator to restore the network.
5.  Wait several minutes, and check whether  **ALM-20002 Hue Service Unavailable**  is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [13](#l8533eba5c6d44bc88f00b63994de5b8e).


**Collect fault information.**

1.  <a name="l8533eba5c6d44bc88f00b63994de5b8e"></a>On MRS Manager, choose  **System** \> **Export Log**.
2.  Select the following nodes from the  **Service** drop-down list and click **OK**:
    -   Hue
    -   Controller

3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.

**The Hue is restarted.**

1.  On MRS Manager, choose  **Service** \> **Hue**.
2.  Choose  **More Actions** \> **Restart service**, and click **OK**.
3.  Check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [19](#led6244cdb00845f6bd3ba23126585b38).

4.  <a name="led6244cdb00845f6bd3ba23126585b38"></a>Contact Technical Support.
5.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s2b5b04c98bc7468b862865c964451136"></a>

N/A

