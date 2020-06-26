# ALM-12357 Failed to Export Audit Logs to the OBS<a name="EN-US_TOPIC_0125375862"></a>

## Description<a name="sdf20bc994e15412d8a2bbf77e2205733"></a>

If the user has configured audit log export to the OBS on MRS Manager, the system regularly exports audit logs to the OBS. This alarm is generated when the system fails to access the OBS.

This alarm is cleared when the system exports audit logs to the OBS successfully.

## Attribute<a name="s25755f9f3e514389a4dff744a631c071"></a>

<a name="tbe560640b8af436cbc3c5699df6265ae"></a>
<table><thead align="left"><tr id="radfc773848b14c68aaa4b233a6c5cdfc"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a6621a968af3345f0946f733bbbb663fe"><a name="a6621a968af3345f0946f733bbbb663fe"></a><a name="a6621a968af3345f0946f733bbbb663fe"></a><strong id="a9cde552f2ede498b98ac47151b7b794a"><a name="a9cde552f2ede498b98ac47151b7b794a"></a><a name="a9cde552f2ede498b98ac47151b7b794a"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a7b371425e9b34a1b9e4d3aaef322f301"><a name="a7b371425e9b34a1b9e4d3aaef322f301"></a><a name="a7b371425e9b34a1b9e4d3aaef322f301"></a><strong id="a799de7e6b10640858c74382c75a9008d"><a name="a799de7e6b10640858c74382c75a9008d"></a><a name="a799de7e6b10640858c74382c75a9008d"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ab553e85abbf64895bcc148027d113272"><a name="ab553e85abbf64895bcc148027d113272"></a><a name="ab553e85abbf64895bcc148027d113272"></a><strong id="a28f4c439895449dbbfc97b484db03f87"><a name="a28f4c439895449dbbfc97b484db03f87"></a><a name="a28f4c439895449dbbfc97b484db03f87"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r79e561d82af547c0b05ad2e612339304"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a3ceade87e1594b808a519097fc5b2f22"><a name="a3ceade87e1594b808a519097fc5b2f22"></a><a name="a3ceade87e1594b808a519097fc5b2f22"></a>12357</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a649b61bbe6d74d38a9ea4d5e52c6654b"><a name="a649b61bbe6d74d38a9ea4d5e52c6654b"></a><a name="a649b61bbe6d74d38a9ea4d5e52c6654b"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a44b32c71670c4ff39dbb41683f3d65db"><a name="a44b32c71670c4ff39dbb41683f3d65db"></a><a name="a44b32c71670c4ff39dbb41683f3d65db"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s498bb3cb99a745879f8e228742289a73"></a>

<a name="t8d8da75da993419ca18f1c08829f32fa"></a>
<table><thead align="left"><tr id="r8271ccbdf14d4141ade915fd54578183"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="af9606e33c09c4ac18b13276114524fdd"><a name="af9606e33c09c4ac18b13276114524fdd"></a><a name="af9606e33c09c4ac18b13276114524fdd"></a><strong id="a65585d018812428ab0fa24def9e42189"><a name="a65585d018812428ab0fa24def9e42189"></a><a name="a65585d018812428ab0fa24def9e42189"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a4a0dc372ee0849bc81b54a85a5eab633"><a name="a4a0dc372ee0849bc81b54a85a5eab633"></a><a name="a4a0dc372ee0849bc81b54a85a5eab633"></a><strong id="a2685618c7e4442bbb75ac3c1835a6327"><a name="a2685618c7e4442bbb75ac3c1835a6327"></a><a name="a2685618c7e4442bbb75ac3c1835a6327"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb3ed06f8b9584797b7379391f290d171"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3a948b83cfde44768f472058ba1d7900"><a name="a3a948b83cfde44768f472058ba1d7900"></a><a name="a3a948b83cfde44768f472058ba1d7900"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a4e747b6a40304d79a16b0ceffcab742b"><a name="a4e747b6a40304d79a16b0ceffcab742b"></a><a name="a4e747b6a40304d79a16b0ceffcab742b"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r97c40ab5df914172a9bff420762b4de6"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="abfa7bdf5984248db9bc4cfeb392054d5"><a name="abfa7bdf5984248db9bc4cfeb392054d5"></a><a name="abfa7bdf5984248db9bc4cfeb392054d5"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a276bcdeb64fc43dab8cf60102fcddc7b"><a name="a276bcdeb64fc43dab8cf60102fcddc7b"></a><a name="a276bcdeb64fc43dab8cf60102fcddc7b"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rff24093b5eb6431a87784fb4936235c7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7254518f402a43189292a9c12ccdf59e"><a name="a7254518f402a43189292a9c12ccdf59e"></a><a name="a7254518f402a43189292a9c12ccdf59e"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aeb035920712045cd8e206d5f82b46ebe"><a name="aeb035920712045cd8e206d5f82b46ebe"></a><a name="aeb035920712045cd8e206d5f82b46ebe"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s78b2c233ea2541f9b50c538df16626ae"></a>

The local system saves a maximum of seven compressed service audit log files. If this alarm persists, local service audit logs may be lost.

The local system saves a maximum of 50 management audit log files \(each file contains 100,000 records\). If this alarm persists, local management audit logs may be lost.

## Possible Causes<a name="s4ef0ab176cb642809a81a7b8ccfd6295"></a>

-   Connection to the OBS server fails.
-   The specified OBS bucket does not exist.
-   The user AK/SK information is invalid.
-   The local OBS configuration cannot be obtained.

## Procedure<a name="sc1eb4c565c994e0bb2a15b551544eee4"></a>

1.  Log in to the OBS server and check whether the OBS server can be properly accessed.
    -   If yes, go to  [3](#l6ad80968d001475fbd0cabb05211d66e).
    -   If no, go to  [2](#ld81c8b7def224e0eb7c5db3fcff39170).

2.  <a name="ld81c8b7def224e0eb7c5db3fcff39170"></a>Contact the maintenance personnel to repair the OBS. Then check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [3](#l6ad80968d001475fbd0cabb05211d66e).

3.  <a name="l6ad80968d001475fbd0cabb05211d66e"></a>On MRS Manager, choose  **System**  \>  **Export Audit Log**. Check whether the AK/SK information, bucket name, and path are correct.
    -   If yes, go to  [5](#l4c18dfaaf6904655ab9ca755022b65fb).
    -   If no, go to  [4](#l7910173b40004fdbb543565fc70a2d72).

4.  <a name="l7910173b40004fdbb543565fc70a2d72"></a>Correct the information. Then check whether the alarm is cleared when the export task is executed again.

    >![](/images/icon-note.gif) **NOTE:**   
    >To check alarm clearance quickly, you can set the start time of audit log collection to 10 or 30 minutes later than the current time. After checking the result, restore the original start time.  

    -   If yes, no further action is required.
    -   If no, go to  [5](#l4c18dfaaf6904655ab9ca755022b65fb).

5.  <a name="l4c18dfaaf6904655ab9ca755022b65fb"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s7c89337058084d8090bc83d74b38fcff"></a>

N/A

