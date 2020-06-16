# ALM-12007 Process Fault<a name="EN-US_TOPIC_0125376065"></a>

## Description<a name="s40dfdc170b784295a7395ba2bce66d0e"></a>

The process health check module checks the process status every 5 seconds. This alarm is generated when the process health check module detects that the process connection status is  **Bad**  for three times consecutively and is cleared when the process can be connected.

## Attribute<a name="s709222187252440f9acd6434bbbedc39"></a>

<a name="t9160544a922e46c5a12d823e86c20b75"></a>
<table><thead align="left"><tr id="rb323e3caa11d4458a694c605142f9377"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a55fe0bf955a6427f8fceb4e782c99ab5"><a name="a55fe0bf955a6427f8fceb4e782c99ab5"></a><a name="a55fe0bf955a6427f8fceb4e782c99ab5"></a><strong id="acee9ae86b2f348d999d0bd5ecd7b505c"><a name="acee9ae86b2f348d999d0bd5ecd7b505c"></a><a name="acee9ae86b2f348d999d0bd5ecd7b505c"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aae4ee2a131964772a2c227b270e9c861"><a name="aae4ee2a131964772a2c227b270e9c861"></a><a name="aae4ee2a131964772a2c227b270e9c861"></a><strong id="a960799dd990945e2858fad4609a4a333"><a name="a960799dd990945e2858fad4609a4a333"></a><a name="a960799dd990945e2858fad4609a4a333"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a9e6b406b28cd4620aa641b7547200423"><a name="a9e6b406b28cd4620aa641b7547200423"></a><a name="a9e6b406b28cd4620aa641b7547200423"></a><strong id="en-us_topic_0035461477_b545935115740"><a name="en-us_topic_0035461477_b545935115740"></a><a name="en-us_topic_0035461477_b545935115740"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rd90f9953ba8f46f5af962fbd03e9c202"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ab368974c43274596bd59627d07c7e70e"><a name="ab368974c43274596bd59627d07c7e70e"></a><a name="ab368974c43274596bd59627d07c7e70e"></a>12007</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a3ed6cc83eeb440278dd4f58516b91de6"><a name="a3ed6cc83eeb440278dd4f58516b91de6"></a><a name="a3ed6cc83eeb440278dd4f58516b91de6"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aacbe0283d5f347228561b046d60101ef"><a name="aacbe0283d5f347228561b046d60101ef"></a><a name="aacbe0283d5f347228561b046d60101ef"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s0c3c8204d8d1426db130ebea413c40d0"></a>

<a name="t9559c2513d464c16962a821b67706a55"></a>
<table><thead align="left"><tr id="rbd67e77a67064bb4be4506277da15a6b"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae4ae7fb76fa74810aa543d022ca76bd2"><a name="ae4ae7fb76fa74810aa543d022ca76bd2"></a><a name="ae4ae7fb76fa74810aa543d022ca76bd2"></a><strong id="af60d762d8dab412ebfe242d6ceb379f0"><a name="af60d762d8dab412ebfe242d6ceb379f0"></a><a name="af60d762d8dab412ebfe242d6ceb379f0"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a36e9105b4f6849cdad55151eb2095692"><a name="a36e9105b4f6849cdad55151eb2095692"></a><a name="a36e9105b4f6849cdad55151eb2095692"></a><strong id="ada4d9ecc65574233977ee2030cf779ca"><a name="ada4d9ecc65574233977ee2030cf779ca"></a><a name="ada4d9ecc65574233977ee2030cf779ca"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rdc73c3139e08464a9264f947ca5bc068"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6ba2ada8357c4545a9a0607de924ebf1"><a name="a6ba2ada8357c4545a9a0607de924ebf1"></a><a name="a6ba2ada8357c4545a9a0607de924ebf1"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad4ac6d54d1724550a7b4f9879246a28b"><a name="ad4ac6d54d1724550a7b4f9879246a28b"></a><a name="ad4ac6d54d1724550a7b4f9879246a28b"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rcd27c0b4b1a548158dbbc33e77a69c5e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="adc1ff27615b44677b8ce9ec0cefe6c1e"><a name="adc1ff27615b44677b8ce9ec0cefe6c1e"></a><a name="adc1ff27615b44677b8ce9ec0cefe6c1e"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1be014d031b7483bb47d8fcbb4f38d50"><a name="a1be014d031b7483bb47d8fcbb4f38d50"></a><a name="a1be014d031b7483bb47d8fcbb4f38d50"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7402ab480d9a4bd4b787387fd222bd03"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="acdde0fa48cc442e6ae256f6f2074db2a"><a name="acdde0fa48cc442e6ae256f6f2074db2a"></a><a name="acdde0fa48cc442e6ae256f6f2074db2a"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9e2bffea6c0440bc8a8a902d91aa698f"><a name="a9e2bffea6c0440bc8a8a902d91aa698f"></a><a name="a9e2bffea6c0440bc8a8a902d91aa698f"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s6ba23d4012b547c996144eb1ca00f9d2"></a>

The service provided by the process is unavailable.

## Possible Causes<a name="s1979f908b444481c8936c0ff52f3825a"></a>

-   The instance process is abnormal.
-   The disk space is insufficient.

## Procedure<a name="sf0a851a77ae147a8a1b9fc06673763d7"></a>

1.  Check whether the instance process is abnormal.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view its host name and service name in the alarm details.
    2.  On the  **Alarm** page, check whether alarm [ALM-12006 Node Fault](alm-12006-node-fault.md)  is generated.
        -   If yes, go to  [1.c](#ld10391a550a54926aed2d29d870c7c84).
        -   If no, go to  [1.d](#l9ab977d80f3741b7a482ee4224a10f2e).

    3.  <a name="ld10391a550a54926aed2d29d870c7c84"></a>See the procedure in  [ALM-12006 Node Fault](alm-12006-node-fault.md)  to handle the alarm.
    4.  <a name="l9ab977d80f3741b7a482ee4224a10f2e"></a>Check whether the installation directory user, user group, and permission of the alarm role are correct. The user, user group, and the permission must be  **omm:ficommon 750**.
        -   If yes, go to  [1.f](#l36df1d91c38f45e1afe5a4a4749e4960).
        -   If no, go to  [1.e](#l322a58fd54214b0e9433fea936ae5074).

    5.  <a name="l322a58fd54214b0e9433fea936ae5074"></a>Run the following command to set the permission to  **750** and **User:Group** to **omm:ficommon**:

        **chmod 750** _<folder\_name\>_

        **chown omm:ficommon** _<folder\_name\>_

    6.  <a name="l36df1d91c38f45e1afe5a4a4749e4960"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l706e747146d3452c8503745bec85b0d6).

2.  Check whether the disk space is insufficient.
    1.  <a name="l706e747146d3452c8503745bec85b0d6"></a>On MRS Manager, check whether the alarm list contains  **ALM-12017 Insufficient Disk Capacity**.
        -   If yes, go to  [2.b](#lf97fb48d69a24025b44ef07e65e7720f).
        -   If no, go to  [3](#le43018b204b34002beb1addae79582af).

    2.  <a name="lf97fb48d69a24025b44ef07e65e7720f"></a>See the procedure in  [ALM-12017 Insufficient Disk Capacity](alm-12017-insufficient-disk-capacity.md)  to handle the alarm.
    3.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, go to  [2.d](#lfe6e81981e394c92b2b5a227d06d8276).
        -   If no, go to  [3](#le43018b204b34002beb1addae79582af).

    4.  <a name="lfe6e81981e394c92b2b5a227d06d8276"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#le43018b204b34002beb1addae79582af).

3.  <a name="le43018b204b34002beb1addae79582af"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s25b38afe050444c5810ba7702cd4046a"></a>

N/A

