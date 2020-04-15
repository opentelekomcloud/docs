# ALM-12001 Audit Log Dump Failure<a name="EN-US_TOPIC_0125375886"></a>

## Description<a name="sb6041c18e530485a9d00925996e9ce16"></a>

Cluster audit logs need to be dumped on a third-party server due to the local historical data backup policy. Audit logs can be successfully dumped if the dump server meets the configuration conditions. This alarm is generated when the audit log dump fails due to insufficient disk space on the dump directory on the third-party server or if a user changes the username, password, or dump directory of the dump server.

## Attribute<a name="sfbe5b95c57874ff09af562ff5cb2360e"></a>

<a name="t66c9fedd59c341b4b0f0062935639374"></a>
<table><thead align="left"><tr id="r0a7c7f3415a74c9393dbbb7e7068e1be"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a862bb098dd2c4f5e9d8399aa87794758"><a name="a862bb098dd2c4f5e9d8399aa87794758"></a><a name="a862bb098dd2c4f5e9d8399aa87794758"></a><strong id="a180c45686bcf4158b2f59aa79ba85910"><a name="a180c45686bcf4158b2f59aa79ba85910"></a><a name="a180c45686bcf4158b2f59aa79ba85910"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a79444465010f4a42ba2c4590714957c6"><a name="a79444465010f4a42ba2c4590714957c6"></a><a name="a79444465010f4a42ba2c4590714957c6"></a><strong id="ad170f25d9ca7402eb79dd81ae8951c74"><a name="ad170f25d9ca7402eb79dd81ae8951c74"></a><a name="ad170f25d9ca7402eb79dd81ae8951c74"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a402b3b94b6ba461ebf7e6917315202d7"><a name="a402b3b94b6ba461ebf7e6917315202d7"></a><a name="a402b3b94b6ba461ebf7e6917315202d7"></a><strong id="a4ae7501f1cec4fddbce4dd21de712049"><a name="a4ae7501f1cec4fddbce4dd21de712049"></a><a name="a4ae7501f1cec4fddbce4dd21de712049"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r43df44a87993485ca079594dab7f3c31"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a068c1f9e036547b781012b8f5940e194"><a name="a068c1f9e036547b781012b8f5940e194"></a><a name="a068c1f9e036547b781012b8f5940e194"></a>12001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a31fc52d0adbe4c3ebaca33832a331ebb"><a name="a31fc52d0adbe4c3ebaca33832a331ebb"></a><a name="a31fc52d0adbe4c3ebaca33832a331ebb"></a>Minor</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="abec771b8fd6543d3b67c4caffba25d31"><a name="abec771b8fd6543d3b67c4caffba25d31"></a><a name="abec771b8fd6543d3b67c4caffba25d31"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s832157f06a794737ba1ec5e19d518210"></a>

<a name="t5bbce9a4706b4de0ac52eeaeaf2225be"></a>
<table><thead align="left"><tr id="re33b5b14b1cc4e9d96d85c4b4ce21975"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a1baabc9bddb942b1a01f09524d243144"><a name="a1baabc9bddb942b1a01f09524d243144"></a><a name="a1baabc9bddb942b1a01f09524d243144"></a><strong id="en-us_topic_0035446123_b945591124327"><a name="en-us_topic_0035446123_b945591124327"></a><a name="en-us_topic_0035446123_b945591124327"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a17cd374e46884b6d8f824413fe744f0e"><a name="a17cd374e46884b6d8f824413fe744f0e"></a><a name="a17cd374e46884b6d8f824413fe744f0e"></a><strong id="a16cba98899184fbe943186abfccb3b24"><a name="a16cba98899184fbe943186abfccb3b24"></a><a name="a16cba98899184fbe943186abfccb3b24"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r183b1aa4713e48ab97a35f0887e2cdd2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a668fcec13ebd4e349d132ab064335f9f"><a name="a668fcec13ebd4e349d132ab064335f9f"></a><a name="a668fcec13ebd4e349d132ab064335f9f"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6e2a47b458f54f15b66a3dcd674934b2"><a name="a6e2a47b458f54f15b66a3dcd674934b2"></a><a name="a6e2a47b458f54f15b66a3dcd674934b2"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="re33ee730e08e4e4f87bc30791ab4f534"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a575426a957b04d05b3fa7368bb5f9239"><a name="a575426a957b04d05b3fa7368bb5f9239"></a><a name="a575426a957b04d05b3fa7368bb5f9239"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="abed15af3cdc046b6b91cee3cb34341fe"><a name="abed15af3cdc046b6b91cee3cb34341fe"></a><a name="abed15af3cdc046b6b91cee3cb34341fe"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r1e69401081424a50acdd399cb60a66c8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af1952bbebb814078ae4bee11487bc23c"><a name="af1952bbebb814078ae4bee11487bc23c"></a><a name="af1952bbebb814078ae4bee11487bc23c"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae6afac5806e842a7a62180c96a38c03e"><a name="ae6afac5806e842a7a62180c96a38c03e"></a><a name="ae6afac5806e842a7a62180c96a38c03e"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sf23cdedf2d554a4482e08a4675a48649"></a>

The system can only store a maximum of 50 dump files locally. If the fault persists on the dump server, the local audit log may be lost.

## Possible Causes<a name="s5e08321fb14048d890c8dfef5253ce2b"></a>

-   The network connection is abnormal.
-   The username, password, or dump directory of the dump server does not meet the configuration conditions.
-   The disk space of the dump directory is insufficient.

## Procedure<a name="sa2a57ac1cb394314b45532608d3686a2"></a>

1.  Check whether the username, password, and dump directory are correct.
    1.  Check on the dump configuration page of MRS Manager to see if they are correct.
        -   If yes, go to  [3](#lf4fa80d0bfeb457fbc4cd749a1d0da88).
        -   If no, go to  [1.b](#l2e803299346547719f3622cd7a09a155).

    2.  <a name="l2e803299346547719f3622cd7a09a155"></a>Change the username, password, or dump directory, and click  **OK**.
    3.  Wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lf77d094a28d9462088ed71b0c9b88877).

2.  <a name="lf77d094a28d9462088ed71b0c9b88877"></a>Reset the dump rule.
    1.  On MRS Manager, choose  **System**  \>  **Dump Audit Log**.
    2.  Reset dump rules, set the parameters properly, and click  **OK**.
    3.  Wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#lf4fa80d0bfeb457fbc4cd749a1d0da88).

3.  <a name="lf4fa80d0bfeb457fbc4cd749a1d0da88"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

        Telephone:



## Related Information<a name="s894bbd1937924c81b336155ce64fcf35"></a>

N/A

