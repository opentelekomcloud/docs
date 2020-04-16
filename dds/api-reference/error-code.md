# Error Code<a name="dds_error_code"></a>

If an error occurs in an API, no result is returned. You can locate the error cause based on the error codes of each API. When the invocation fails, an HTTP status code is returned. The returned message body contains the specific error code and information.

## Error Response Body Format<a name="section15564659114717"></a>

-   Parameter description

    **Table  1**  Parameter description

    <a name="t1600a24cde73446fadb04fa4fd4176c9"></a>
    <table><thead align="left"><tr id="rd8bc4cbf15874672964a2f6155ff619b"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="ae933c42bba744097bb871e1e47a3d811"><a name="ae933c42bba744097bb871e1e47a3d811"></a><a name="ae933c42bba744097bb871e1e47a3d811"></a><strong id="b986813198327"><a name="b986813198327"></a><a name="b986813198327"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="a70dcf20d1f394d3886396b45ae4ed9e9"><a name="a70dcf20d1f394d3886396b45ae4ed9e9"></a><a name="a70dcf20d1f394d3886396b45ae4ed9e9"></a><strong id="b11336122111322"><a name="b11336122111322"></a><a name="b11336122111322"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="aab87d22c016b458fbf47a74f2c84238b"><a name="aab87d22c016b458fbf47a74f2c84238b"></a><a name="aab87d22c016b458fbf47a74f2c84238b"></a><strong id="b1193810973518"><a name="b1193810973518"></a><a name="b1193810973518"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r3a83848174a44b2499a0b79476a18366"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p6826111184918"><a name="p6826111184918"></a><a name="p6826111184918"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="a70943c58d7524abcb12b87181c64e2a5"><a name="a70943c58d7524abcb12b87181c64e2a5"></a><a name="a70943c58d7524abcb12b87181c64e2a5"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="ac399032b44cd41cd82fc0a0c3e083886"><a name="ac399032b44cd41cd82fc0a0c3e083886"></a><a name="ac399032b44cd41cd82fc0a0c3e083886"></a>Specifies the error returned when a task submission exception occurs.</p>
    </td>
    </tr>
    <tr id="r406296b9b2bf4aafb5e79cf9da8fb201"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="aa97ccde9ddfc4aa0823d82c4a22f6962"><a name="aa97ccde9ddfc4aa0823d82c4a22f6962"></a><a name="aa97ccde9ddfc4aa0823d82c4a22f6962"></a>error_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="a1ef067712a0141029c3dd10e0df28ab9"><a name="a1ef067712a0141029c3dd10e0df28ab9"></a><a name="a1ef067712a0141029c3dd10e0df28ab9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="a0994d9a70c8241ba8a2b1fc9b0757e6e"><a name="a0994d9a70c8241ba8a2b1fc9b0757e6e"></a><a name="a0994d9a70c8241ba8a2b1fc9b0757e6e"></a>Specifies the description of the error returned when a task submission exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    { 
        "error_code": "DBS.200001",
        "error_msg": "Parameter error"
    }
    ```


## Error Code Description<a name="section87781628164717"></a>

**Table  2**  Error code description

<a name="table181314564313"></a>
<table><thead align="left"><tr id="row557425615319"><th class="cellrowborder" valign="top" width="19.73%" id="mcps1.2.5.1.1"><p id="p189962289386"><a name="p189962289386"></a><a name="p189962289386"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="22.61%" id="mcps1.2.5.1.2"><p id="p2057415616310"><a name="p2057415616310"></a><a name="p2057415616310"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="29.37%" id="mcps1.2.5.1.3"><p id="p10574135612311"><a name="p10574135612311"></a><a name="p10574135612311"></a>Error Information</p>
</th>
<th class="cellrowborder" valign="top" width="28.29%" id="mcps1.2.5.1.4"><p id="p11512350163815"><a name="p11512350163815"></a><a name="p11512350163815"></a>Handling Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="row3235122919140"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p15996172803813"><a name="p15996172803813"></a><a name="p15996172803813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p201968417517"><a name="p201968417517"></a><a name="p201968417517"></a>DBS.200001</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p16642171683711"><a name="p16642171683711"></a><a name="p16642171683711"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p105121750183815"><a name="p105121750183815"></a><a name="p105121750183815"></a>Check whether the transferred parameters or URLs are correct.</p>
</td>
</tr>
<tr id="row13686151782218"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p999642816385"><a name="p999642816385"></a><a name="p999642816385"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p29612214220"><a name="p29612214220"></a><a name="p29612214220"></a>DBS.200002</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p79612218228"><a name="p79612218228"></a><a name="p79612218228"></a>The DB instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p55121750153811"><a name="p55121750153811"></a><a name="p55121750153811"></a>Check whether the DB instance and its ID are correct and whether the DB instance exists.</p>
</td>
</tr>
<tr id="row174701046172210"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p8996112893820"><a name="p8996112893820"></a><a name="p8996112893820"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p34705465225"><a name="p34705465225"></a><a name="p34705465225"></a>DBS.200010</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p4266759113219"><a name="p4266759113219"></a><a name="p4266759113219"></a>Authentication failed</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p45121950103816"><a name="p45121950103816"></a><a name="p45121950103816"></a>Check whether the tenant and instance match.</p>
</td>
</tr>
<tr id="row41311137316"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p159961128173815"><a name="p159961128173815"></a><a name="p159961128173815"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p4131032310"><a name="p4131032310"></a><a name="p4131032310"></a>DBS.200011</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p3131836315"><a name="p3131836315"></a><a name="p3131836315"></a>Operation cannot be executed in current state of the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p155121850153816"><a name="p155121850153816"></a><a name="p155121850153816"></a>Check whether the instance status or the ongoing operation on the instance conflicts with the request.</p>
</td>
</tr>
<tr id="row89642041152814"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p399602863820"><a name="p399602863820"></a><a name="p399602863820"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p710312456289"><a name="p710312456289"></a><a name="p710312456289"></a>DBS.200013</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p210324582818"><a name="p210324582818"></a><a name="p210324582818"></a>The node does not exist</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1351255083816"><a name="p1351255083816"></a><a name="p1351255083816"></a>Check whether the node ID or group ID is correct.</p>
</td>
</tr>
<tr id="row35381165184"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p2099615286387"><a name="p2099615286387"></a><a name="p2099615286387"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p18625131623710"><a name="p18625131623710"></a><a name="p18625131623710"></a>DBS.200018</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p13623181610374"><a name="p13623181610374"></a><a name="p13623181610374"></a>This DB instance is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1575173012710"><a name="p1575173012710"></a><a name="p1575173012710"></a>Check whether the instance status conflicts with the ongoing operation on the instance.</p>
</td>
</tr>
<tr id="row125751156133115"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p999612819388"><a name="p999612819388"></a><a name="p999612819388"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p19622161683713"><a name="p19622161683713"></a><a name="p19622161683713"></a>DBS.200019</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p15621151633715"><a name="p15621151633715"></a><a name="p15621151633715"></a>Operation cannot be executed in current state of the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p396132712711"><a name="p396132712711"></a><a name="p396132712711"></a>Check whether the instance status conflicts with the ongoing operation on the instance.</p>
</td>
</tr>
<tr id="row1717611596269"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p179968286385"><a name="p179968286385"></a><a name="p179968286385"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p83638317271"><a name="p83638317271"></a><a name="p83638317271"></a>DBS.200024</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p63632037276"><a name="p63632037276"></a><a name="p63632037276"></a>The region is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p651325013814"><a name="p651325013814"></a><a name="p651325013814"></a>Check whether the region name is correct and whether the region is available.</p>
</td>
</tr>
<tr id="row9769233133618"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p9769183353619"><a name="p9769183353619"></a><a name="p9769183353619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p11769123313618"><a name="p11769123313618"></a><a name="p11769123313618"></a>DBS.200022</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p3769183317369"><a name="p3769183317369"></a><a name="p3769183317369"></a>The DB instance name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1316224863914"><a name="p1316224863914"></a><a name="p1316224863914"></a>Check whether the DB instance name exists.</p>
</td>
</tr>
<tr id="row651118610271"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1199642813820"><a name="p1199642813820"></a><a name="p1199642813820"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p6546131052716"><a name="p6546131052716"></a><a name="p6546131052716"></a>DBS.200025</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p135111465277"><a name="p135111465277"></a><a name="p135111465277"></a>Invalid AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p4983845102715"><a name="p4983845102715"></a><a name="p4983845102715"></a>Check whether the AZ name is correct and whether the AZ is available.</p>
</td>
</tr>
<tr id="row5984112672310"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p149963281388"><a name="p149963281388"></a><a name="p149963281388"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p9712143013233"><a name="p9712143013233"></a><a name="p9712143013233"></a>DBS.200028</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p9712030142317"><a name="p9712030142317"></a><a name="p9712030142317"></a>The maximum storage space has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p2513125013384"><a name="p2513125013384"></a><a name="p2513125013384"></a>Check whether the storage space exceeds the upper limit.</p>
</td>
</tr>
<tr id="row151072618123"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p71016263120"><a name="p71016263120"></a><a name="p71016263120"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p14104260129"><a name="p14104260129"></a><a name="p14104260129"></a>DBS.200042</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p410182691218"><a name="p410182691218"></a><a name="p410182691218"></a>Invalid DB engine.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1710826191215"><a name="p1710826191215"></a><a name="p1710826191215"></a>Check whether the DB engine is supported by DDS.</p>
</td>
</tr>
<tr id="row45591155163516"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1199610284385"><a name="p1199610284385"></a><a name="p1199610284385"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1748175912356"><a name="p1748175912356"></a><a name="p1748175912356"></a>DBS.200029</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p11482059113513"><a name="p11482059113513"></a><a name="p11482059113513"></a>Invalid username and password.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p12513350203811"><a name="p12513350203811"></a><a name="p12513350203811"></a>Check whether the username and password match and whether the password meets the password strength requirements.</p>
</td>
</tr>
<tr id="row55777564319"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p199968289388"><a name="p199968289388"></a><a name="p199968289388"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p144644183511"><a name="p144644183511"></a><a name="p144644183511"></a>DBS.200047</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p206621412753"><a name="p206621412753"></a><a name="p206621412753"></a>Operation cannot be executed in current state of the DB instance or node.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p17513125013382"><a name="p17513125013382"></a><a name="p17513125013382"></a>Check whether the instance status conflicts with the ongoing operation on the instance.</p>
</td>
</tr>
<tr id="row357855673117"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p159961228143811"><a name="p159961228143811"></a><a name="p159961228143811"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p17579192418371"><a name="p17579192418371"></a><a name="p17579192418371"></a>DBS.200048</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p19576324183719"><a name="p19576324183719"></a><a name="p19576324183719"></a>Invalid VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p135133501383"><a name="p135133501383"></a><a name="p135133501383"></a>Check whether the VPC ID and name are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row165780560312"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1199662816383"><a name="p1199662816383"></a><a name="p1199662816383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p12574172414372"><a name="p12574172414372"></a><a name="p12574172414372"></a>DBS.200049</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1757282443716"><a name="p1757282443716"></a><a name="p1757282443716"></a>Invalid subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p11513135017382"><a name="p11513135017382"></a><a name="p11513135017382"></a>Check whether the subnet ID and name are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row105781356183114"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1699616283388"><a name="p1699616283388"></a><a name="p1699616283388"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p18571202417372"><a name="p18571202417372"></a><a name="p18571202417372"></a>DBS.200050</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p7201511500"><a name="p7201511500"></a><a name="p7201511500"></a>Invalid security group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1851319509383"><a name="p1851319509383"></a><a name="p1851319509383"></a>Check whether the security group ID and name are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row1466393118278"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p5996228123812"><a name="p5996228123812"></a><a name="p5996228123812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p16905173411276"><a name="p16905173411276"></a><a name="p16905173411276"></a>DBS.200052</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p13905153462714"><a name="p13905153462714"></a><a name="p13905153462714"></a>Invalid password.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1887915166294"><a name="p1887915166294"></a><a name="p1887915166294"></a>Check whether the username and password match and whether the password meets the password strength requirements.</p>
</td>
</tr>
<tr id="row19850203963010"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p3996162819386"><a name="p3996162819386"></a><a name="p3996162819386"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p53757435301"><a name="p53757435301"></a><a name="p53757435301"></a>DBS.200053</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p437524393014"><a name="p437524393014"></a><a name="p437524393014"></a>The DB instance specifications do not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p115131550133815"><a name="p115131550133815"></a><a name="p115131550133815"></a>Check whether the specifications are correct and supported in the current AZ.</p>
</td>
</tr>
<tr id="row1363802621716"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p899642803819"><a name="p899642803819"></a><a name="p899642803819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1955611243375"><a name="p1955611243375"></a><a name="p1955611243375"></a>DBS.200054</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p410210101706"><a name="p410210101706"></a><a name="p410210101706"></a>Invalid DB instance specifications.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p0176258552"><a name="p0176258552"></a><a name="p0176258552"></a>Check whether the specifications are correct and supported in the current AZ.</p>
</td>
</tr>
<tr id="row128661335194015"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1599618284383"><a name="p1599618284383"></a><a name="p1599618284383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p4452143874016"><a name="p4452143874016"></a><a name="p4452143874016"></a>DBS.200057</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1453123884011"><a name="p1453123884011"></a><a name="p1453123884011"></a>Invalid parameter group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p2513115013818"><a name="p2513115013818"></a><a name="p2513115013818"></a>Check whether the parameter group is correct, whether the parameter group exists, and whether the parameter group matches the instance type.</p>
</td>
</tr>
<tr id="row6366337163413"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p0996192833814"><a name="p0996192833814"></a><a name="p0996192833814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p151254063418"><a name="p151254063418"></a><a name="p151254063418"></a>DBS.200075</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p151219404342"><a name="p151219404342"></a><a name="p151219404342"></a>Invalid node role.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1051320504388"><a name="p1051320504388"></a><a name="p1051320504388"></a>Check whether the role of the node meets the requirements and whether the instance is normal.</p>
</td>
</tr>
<tr id="row15980124484815"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p2098144484816"><a name="p2098144484816"></a><a name="p2098144484816"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p998174410483"><a name="p998174410483"></a><a name="p998174410483"></a>DBS.200076</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1098111444482"><a name="p1098111444482"></a><a name="p1098111444482"></a>Operation cannot be executed in current state of the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1998194418485"><a name="p1998194418485"></a><a name="p1998194418485"></a>Check whether the instance status conflicts with the ongoing operation on the instance.</p>
</td>
</tr>
<tr id="row7967161542919"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p096731510292"><a name="p096731510292"></a><a name="p096731510292"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p69671715142918"><a name="p69671715142918"></a><a name="p69671715142918"></a>DBS.200095</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p996712153291"><a name="p996712153291"></a><a name="p996712153291"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p996710156291"><a name="p996710156291"></a><a name="p996710156291"></a>Check whether the parameters in the request and URLs are correct.</p>
</td>
</tr>
<tr id="row0381909716"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p7996182883813"><a name="p7996182883813"></a><a name="p7996182883813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p17388016716"><a name="p17388016716"></a><a name="p17388016716"></a>DBS.200302</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1138150279"><a name="p1138150279"></a><a name="p1138150279"></a>The storage space must be a multiple of 10.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p6513125020382"><a name="p6513125020382"></a><a name="p6513125020382"></a>Check whether the storage space is a multiple of 10.</p>
</td>
</tr>
<tr id="row116791934152415"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p16797346242"><a name="p16797346242"></a><a name="p16797346242"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1767914349241"><a name="p1767914349241"></a><a name="p1767914349241"></a>DBS.200303</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1667912343241"><a name="p1667912343241"></a><a name="p1667912343241"></a>The maximum number of times that the storage space can be scaled up has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p5679143410246"><a name="p5679143410246"></a><a name="p5679143410246"></a>The maximum number of times that the storage space can be scaled up has been reached. To continue to scale up the storage space, contact technical support.</p>
</td>
</tr>
<tr id="row14310342119"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1999662815383"><a name="p1999662815383"></a><a name="p1999662815383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p202118712213"><a name="p202118712213"></a><a name="p202118712213"></a>DBS.200304</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1021113716217"><a name="p1021113716217"></a><a name="p1021113716217"></a>The storage space can be scaled up a maximum of four times.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p751365063819"><a name="p751365063819"></a><a name="p751365063819"></a>Check whether the instance has been scaled up for multiple times.</p>
</td>
</tr>
<tr id="row8894959193415"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p119961328203819"><a name="p119961328203819"></a><a name="p119961328203819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p187671626353"><a name="p187671626353"></a><a name="p187671626353"></a>DBS.200306</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1876719233517"><a name="p1876719233517"></a><a name="p1876719233517"></a>Invalid storage space.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p251315017384"><a name="p251315017384"></a><a name="p251315017384"></a>Check whether the storage space is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row1558018566315"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p16996172811387"><a name="p16996172811387"></a><a name="p16996172811387"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p14834315376"><a name="p14834315376"></a><a name="p14834315376"></a>DBS.200311</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p693164418611"><a name="p693164418611"></a><a name="p693164418611"></a>Scaling up the storage space is not allowed in current state of the node.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p15131350203813"><a name="p15131350203813"></a><a name="p15131350203813"></a>Check whether the node type, instance type, and node ID are correct.</p>
</td>
</tr>
<tr id="row1463220318269"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p5633143102612"><a name="p5633143102612"></a><a name="p5633143102612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p763333152619"><a name="p763333152619"></a><a name="p763333152619"></a>DBS.200434</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p7633103111265"><a name="p7633103111265"></a><a name="p7633103111265"></a>Failed to restart the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p2633931172613"><a name="p2633931172613"></a><a name="p2633931172613"></a>Check whether the DB instance status is normal and whether other operations are being performed on the DB instance.</p>
</td>
</tr>
<tr id="row1558115623117"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p3996142814384"><a name="p3996142814384"></a><a name="p3996142814384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1895103714377"><a name="p1895103714377"></a><a name="p1895103714377"></a>DBS.200470</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1992937103710"><a name="p1992937103710"></a><a name="p1992937103710"></a>Invalid AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1251345043810"><a name="p1251345043810"></a><a name="p1251345043810"></a>Check whether the AZ is correct.</p>
</td>
</tr>
<tr id="row6668111218380"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1299602863815"><a name="p1299602863815"></a><a name="p1299602863815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p204164197386"><a name="p204164197386"></a><a name="p204164197386"></a>DBS.200501</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p766831211384"><a name="p766831211384"></a><a name="p766831211384"></a>The subnet does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p151345023818"><a name="p151345023818"></a><a name="p151345023818"></a>Check whether the subnet ID and name exist and match the VPC.</p>
</td>
</tr>
<tr id="row198691582383"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p19996192823810"><a name="p19996192823810"></a><a name="p19996192823810"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1421212159388"><a name="p1421212159388"></a><a name="p1421212159388"></a>DBS.200502</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p11212121513381"><a name="p11212121513381"></a><a name="p11212121513381"></a>The security group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1351312507381"><a name="p1351312507381"></a><a name="p1351312507381"></a>Check whether the security group ID and name exist and match the VPC.</p>
</td>
</tr>
<tr id="row7647466384"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p18996528113813"><a name="p18996528113813"></a><a name="p18996528113813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p10487182303814"><a name="p10487182303814"></a><a name="p10487182303814"></a>DBS.200503</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1664719613384"><a name="p1664719613384"></a><a name="p1664719613384"></a>The VPC does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1151365016381"><a name="p1151365016381"></a><a name="p1151365016381"></a>Check whether the tenant has the VPC.</p>
</td>
</tr>
<tr id="row195853252812"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p19585182102817"><a name="p19585182102817"></a><a name="p19585182102817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p185851242814"><a name="p185851242814"></a><a name="p185851242814"></a>DBS.200506</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p171529132813"><a name="p171529132813"></a><a name="p171529132813"></a>The encryption key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p45855262818"><a name="p45855262818"></a><a name="p45855262818"></a>Check whether the disk encryption key ID exists.</p>
</td>
</tr>
<tr id="row8517202032920"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p951711203298"><a name="p951711203298"></a><a name="p951711203298"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p451772042918"><a name="p451772042918"></a><a name="p451772042918"></a>DBS.200507</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p125171320162913"><a name="p125171320162913"></a><a name="p125171320162913"></a>The encryption key is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p175171420122915"><a name="p175171420122915"></a><a name="p175171420122915"></a>Check whether the disk encryption key is available.</p>
</td>
</tr>
<tr id="row167001342173618"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p7996102820385"><a name="p7996102820385"></a><a name="p7996102820385"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p437212452367"><a name="p437212452367"></a><a name="p437212452367"></a>DBS.201000</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1737264563612"><a name="p1737264563612"></a><a name="p1737264563612"></a>Operation cannot be executed in current state of the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p7514135015386"><a name="p7514135015386"></a><a name="p7514135015386"></a>Check whether the instance status or the ongoing operation on the instance conflicts with the request.</p>
</td>
</tr>
<tr id="row16281721113618"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p129971228153811"><a name="p129971228153811"></a><a name="p129971228153811"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p161627246362"><a name="p161627246362"></a><a name="p161627246362"></a>DBS.201006</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1916212416363"><a name="p1916212416363"></a><a name="p1916212416363"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p195141050193812"><a name="p195141050193812"></a><a name="p195141050193812"></a>Check whether the transferred parameters or URLs are correct.</p>
</td>
</tr>
<tr id="row4474174321813"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p4997162843818"><a name="p4997162843818"></a><a name="p4997162843818"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p4878346151819"><a name="p4878346151819"></a><a name="p4878346151819"></a>DBS.201014</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p17882114621811"><a name="p17882114621811"></a><a name="p17882114621811"></a>Operation cannot be executed in current state of the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p9514205003815"><a name="p9514205003815"></a><a name="p9514205003815"></a>Check whether the instance status or the ongoing operation on the instance conflicts with the request.</p>
</td>
</tr>
<tr id="row75831556173114"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p20997628163814"><a name="p20997628163814"></a><a name="p20997628163814"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1553550161916"><a name="p1553550161916"></a><a name="p1553550161916"></a>DBS.201015</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p10540808197"><a name="p10540808197"></a><a name="p10540808197"></a>This operation cannot be performed because another operation is being performed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p2051418502383"><a name="p2051418502383"></a><a name="p2051418502383"></a>Check whether the instance status or the ongoing operation on the instance conflicts with the request.</p>
</td>
</tr>
<tr id="row1723684155515"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1223794105510"><a name="p1223794105510"></a><a name="p1223794105510"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p123717485520"><a name="p123717485520"></a><a name="p123717485520"></a>DBS.201020</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p10237745554"><a name="p10237745554"></a><a name="p10237745554"></a>Invalid DB engine.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p197831717134317"><a name="p197831717134317"></a><a name="p197831717134317"></a>Check whether the DB engine is supported by DDS.</p>
</td>
</tr>
<tr id="row4744716133313"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p12997428123815"><a name="p12997428123815"></a><a name="p12997428123815"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p145484207331"><a name="p145484207331"></a><a name="p145484207331"></a>DBS.201028</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p35481120113310"><a name="p35481120113310"></a><a name="p35481120113310"></a>The DB instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p65140503388"><a name="p65140503388"></a><a name="p65140503388"></a>Check whether the DB instance belongs to the tenant and whether the DB instance exists.</p>
</td>
</tr>
<tr id="row3761214162813"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1199722893818"><a name="p1199722893818"></a><a name="p1199722893818"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p877331815284"><a name="p877331815284"></a><a name="p877331815284"></a>DBS.201201</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p13773121813289"><a name="p13773121813289"></a><a name="p13773121813289"></a>The backup already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p13514650113819"><a name="p13514650113819"></a><a name="p13514650113819"></a>Check whether the backup name or ID already exists.</p>
</td>
</tr>
<tr id="row1212015117343"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p109971928143815"><a name="p109971928143815"></a><a name="p109971928143815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1927414143414"><a name="p1927414143414"></a><a name="p1927414143414"></a>DBS.201202</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p112731483410"><a name="p112731483410"></a><a name="p112731483410"></a>Operation cannot be executed in current state of the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1351419502382"><a name="p1351419502382"></a><a name="p1351419502382"></a>Check whether the instance status or the ongoing operation on the instance conflicts with the request.</p>
</td>
</tr>
<tr id="row1232455811169"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p13997112816387"><a name="p13997112816387"></a><a name="p13997112816387"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p132416582167"><a name="p132416582167"></a><a name="p132416582167"></a>DBS.201204</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p93259584166"><a name="p93259584166"></a><a name="p93259584166"></a>The backup file does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1351425073813"><a name="p1351425073813"></a><a name="p1351425073813"></a>Check whether the backup file exists and matches the instance.</p>
</td>
</tr>
<tr id="row12840150134111"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p59971228113811"><a name="p59971228113811"></a><a name="p59971228113811"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p8859736412"><a name="p8859736412"></a><a name="p8859736412"></a>DBS.201214</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p08593324115"><a name="p08593324115"></a><a name="p08593324115"></a>The backup file does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p25146506388"><a name="p25146506388"></a><a name="p25146506388"></a>Check whether the backup exists and matches the instance.</p>
</td>
</tr>
<tr id="row14220162815245"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1299714285384"><a name="p1299714285384"></a><a name="p1299714285384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p10112103113246"><a name="p10112103113246"></a><a name="p10112103113246"></a>DBS.201319</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p11121231162411"><a name="p11121231162411"></a><a name="p11121231162411"></a>Deleting backup file is not allowed because a restoration task is currently in progress. Please wait.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p16514450133814"><a name="p16514450133814"></a><a name="p16514450133814"></a>Check whether the backup is being used to restore instances.</p>
</td>
</tr>
<tr id="row6155032133917"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1399782820384"><a name="p1399782820384"></a><a name="p1399782820384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p12951193510396"><a name="p12951193510396"></a><a name="p12951193510396"></a>DBS.201501</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p095113543917"><a name="p095113543917"></a><a name="p095113543917"></a>The DB instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p2514550143817"><a name="p2514550143817"></a><a name="p2514550143817"></a>Check whether the tenant has the DB instance, whether the DB instance name or ID is correct, and whether the DB instance exists.</p>
</td>
</tr>
<tr id="row124471653017"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p9441116103016"><a name="p9441116103016"></a><a name="p9441116103016"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p8441916133020"><a name="p8441916133020"></a><a name="p8441916133020"></a>DBS.201502</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p94411620300"><a name="p94411620300"></a><a name="p94411620300"></a>The DB instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1144191617307"><a name="p1144191617307"></a><a name="p1144191617307"></a>Check whether the tenant has the DB instance, whether the DB instance name or ID is correct, and whether the DB instance exists.</p>
</td>
</tr>
<tr id="row2058335693120"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1499710289384"><a name="p1499710289384"></a><a name="p1499710289384"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p0298124116376"><a name="p0298124116376"></a><a name="p0298124116376"></a>DBS.212001</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1429514163716"><a name="p1429514163716"></a><a name="p1429514163716"></a>The security group does not exist or has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p165141150113813"><a name="p165141150113813"></a><a name="p165141150113813"></a>Check whether the parameter group exists.</p>
</td>
</tr>
<tr id="row758375611315"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p15997152893814"><a name="p15997152893814"></a><a name="p15997152893814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1028604110370"><a name="p1028604110370"></a><a name="p1028604110370"></a>DBS.212003</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p928215415379"><a name="p928215415379"></a><a name="p928215415379"></a>This operation is not permitted.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1251495083817"><a name="p1251495083817"></a><a name="p1251495083817"></a>Check whether the instance status or the ongoing operation on the instance conflicts with the request.</p>
</td>
</tr>
<tr id="row45842562315"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p8997182873819"><a name="p8997182873819"></a><a name="p8997182873819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1327824163715"><a name="p1327824163715"></a><a name="p1327824163715"></a>DBS.212006</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p12274134123718"><a name="p12274134123718"></a><a name="p12274134123718"></a>The node associated with this parameter group is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p25144504389"><a name="p25144504389"></a><a name="p25144504389"></a>Check whether the node that is associated with the parameter group is normal.</p>
</td>
</tr>
<tr id="row1258485623111"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p499772863814"><a name="p499772863814"></a><a name="p499772863814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1226704153719"><a name="p1226704153719"></a><a name="p1226704153719"></a>DBS.212008</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p102657417378"><a name="p102657417378"></a><a name="p102657417378"></a>The database type is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1851495023810"><a name="p1851495023810"></a><a name="p1851495023810"></a>Check whether the database type is supported</p>
</td>
</tr>
<tr id="row165931933151"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p19971628193819"><a name="p19971628193819"></a><a name="p19971628193819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p122577418377"><a name="p122577418377"></a><a name="p122577418377"></a>DBS.212013</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p102532414372"><a name="p102532414372"></a><a name="p102532414372"></a>This parameter group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1651411503389"><a name="p1651411503389"></a><a name="p1651411503389"></a>Check whether the parameter exists.</p>
</td>
</tr>
<tr id="row13584125683119"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p09971428123814"><a name="p09971428123814"></a><a name="p09971428123814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p3252141153713"><a name="p3252141153713"></a><a name="p3252141153713"></a>DBS.212017</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p142498411373"><a name="p142498411373"></a><a name="p142498411373"></a>Invalid parameter.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p111629109317"><a name="p111629109317"></a><a name="p111629109317"></a>Check whether the transferred parameters or URLs are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row9584185603116"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1099772812384"><a name="p1099772812384"></a><a name="p1099772812384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p32121517421"><a name="p32121517421"></a><a name="p32121517421"></a>DBS.212019</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1420917510428"><a name="p1420917510428"></a><a name="p1420917510428"></a>Invalid parameter.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p457715820313"><a name="p457715820313"></a><a name="p457715820313"></a>Check whether the transferred parameters or URLs are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row6585195653117"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1699711280384"><a name="p1699711280384"></a><a name="p1699711280384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p161851158426"><a name="p161851158426"></a><a name="p161851158426"></a>DBS.212028</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p218420519422"><a name="p218420519422"></a><a name="p218420519422"></a>Invalid parameter group description.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p851425014382"><a name="p851425014382"></a><a name="p851425014382"></a>Check whether the parameter group description is valid.</p>
</td>
</tr>
<tr id="row3585105612312"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p119971828113811"><a name="p119971828113811"></a><a name="p119971828113811"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1818013513423"><a name="p1818013513423"></a><a name="p1818013513423"></a>DBS.212030</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p617725204213"><a name="p617725204213"></a><a name="p617725204213"></a>The parameter group name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p4514175013817"><a name="p4514175013817"></a><a name="p4514175013817"></a>Check whether the parameter group name is correct and whether the tenant has created the parameter group.</p>
</td>
</tr>
<tr id="row89021026144310"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p169971028193815"><a name="p169971028193815"></a><a name="p169971028193815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1922433254312"><a name="p1922433254312"></a><a name="p1922433254312"></a>DBS.212031</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p4229123294319"><a name="p4229123294319"></a><a name="p4229123294319"></a>Invalid parameter group name.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1651475043819"><a name="p1651475043819"></a><a name="p1651475043819"></a>Check whether the parameter group name meets the requirements:</p>
</td>
</tr>
<tr id="row122954172917"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1999742813387"><a name="p1999742813387"></a><a name="p1999742813387"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p19327742142916"><a name="p19327742142916"></a><a name="p19327742142916"></a>DBS.212032</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1532734262911"><a name="p1532734262911"></a><a name="p1532734262911"></a>The operation cannot be performed because this parameter group is applied to one or more DB instance nodes.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p85141650123811"><a name="p85141650123811"></a><a name="p85141650123811"></a>Check whether the parameter group has been applied to the instance.</p>
</td>
</tr>
<tr id="row8475111812514"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1997528173811"><a name="p1997528173811"></a><a name="p1997528173811"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1053816218519"><a name="p1053816218519"></a><a name="p1053816218519"></a>DBS.280001</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p175362211514"><a name="p175362211514"></a><a name="p175362211514"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p75141750123811"><a name="p75141750123811"></a><a name="p75141750123811"></a>Check whether the transferred parameters or URLs are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row194759184519"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p12997202816389"><a name="p12997202816389"></a><a name="p12997202816389"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p45314211516"><a name="p45314211516"></a><a name="p45314211516"></a>DBS.280005</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p45301521359"><a name="p45301521359"></a><a name="p45301521359"></a>Server error. Try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p19514750193814"><a name="p19514750193814"></a><a name="p19514750193814"></a>Contact technical support engineers.</p>
</td>
</tr>
<tr id="row1847431815514"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1299712286381"><a name="p1299712286381"></a><a name="p1299712286381"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p35249211459"><a name="p35249211459"></a><a name="p35249211459"></a>DBS.280015</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p45217212059"><a name="p45217212059"></a><a name="p45217212059"></a>Permission denied.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p13514450133816"><a name="p13514450133816"></a><a name="p13514450133816"></a>Check whether the token expires and whether the instance matches the tenant.</p>
</td>
</tr>
<tr id="row191618261555"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p199971928173810"><a name="p199971928173810"></a><a name="p199971928173810"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p010112616518"><a name="p010112616518"></a><a name="p010112616518"></a>DBS.280016</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p71051826051"><a name="p71051826051"></a><a name="p71051826051"></a>Resource not found.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p125141550193818"><a name="p125141550193818"></a><a name="p125141550193818"></a>Check whether the transferred parameters are correct and whether the instance exists.</p>
</td>
</tr>
<tr id="row16980191794811"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1199752863815"><a name="p1199752863815"></a><a name="p1199752863815"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p798010172481"><a name="p798010172481"></a><a name="p798010172481"></a>DBS.280019</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p2098091794810"><a name="p2098091794810"></a><a name="p2098091794810"></a>Account suspended.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p155141150123811"><a name="p155141150123811"></a><a name="p155141150123811"></a>Check the account balance. </p>
</td>
</tr>
<tr id="row136599442418"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p126593472419"><a name="p126593472419"></a><a name="p126593472419"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p46606414243"><a name="p46606414243"></a><a name="p46606414243"></a>DBS.280032</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p2660144142410"><a name="p2660144142410"></a><a name="p2660144142410"></a>Permission denied.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1266014442415"><a name="p1266014442415"></a><a name="p1266014442415"></a>Check whether the rights of the user group to which the current user belongs allow the corresponding operation.</p>
</td>
</tr>
<tr id="row1566420275512"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p11997132817389"><a name="p11997132817389"></a><a name="p11997132817389"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p16273273516"><a name="p16273273516"></a><a name="p16273273516"></a>DBS.280042</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p4632122713510"><a name="p4632122713510"></a><a name="p4632122713510"></a>Invalid request.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p11514155013814"><a name="p11514155013814"></a><a name="p11514155013814"></a>Check whether the request is allowed by the current instance status and the operations being performed on the instance and whether the request is valid.</p>
</td>
</tr>
<tr id="row3465143117512"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p4997112813381"><a name="p4997112813381"></a><a name="p4997112813381"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1638614319512"><a name="p1638614319512"></a><a name="p1638614319512"></a>DBS.280056</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p339119317519"><a name="p339119317519"></a><a name="p339119317519"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1651435010382"><a name="p1651435010382"></a><a name="p1651435010382"></a>Check whether the instance belongs to the tenant and whether the token has been obtained again.</p>
</td>
</tr>
<tr id="row10717194915518"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p199792873815"><a name="p199792873815"></a><a name="p199792873815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p3114105219519"><a name="p3114105219519"></a><a name="p3114105219519"></a>DBS.200072</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1511485218515"><a name="p1511485218515"></a><a name="p1511485218515"></a>Invalid storage space.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1514135011382"><a name="p1514135011382"></a><a name="p1514135011382"></a>Check whether the storage space exceeds the upper limit.</p>
</td>
</tr>
<tr id="row17939349318"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p157931534193113"><a name="p157931534193113"></a><a name="p157931534193113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p6793103483112"><a name="p6793103483112"></a><a name="p6793103483112"></a>DBS.280110</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p679393423112"><a name="p679393423112"></a><a name="p679393423112"></a>The DB instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1979315343316"><a name="p1979315343316"></a><a name="p1979315343316"></a>Check whether the tenant has the DB instance, whether the DB instance name or ID is correct, and whether the DB instance exists.</p>
</td>
</tr>
<tr id="row964891204917"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p12997028163819"><a name="p12997028163819"></a><a name="p12997028163819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p66482164914"><a name="p66482164914"></a><a name="p66482164914"></a>DBS.280122</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p964991154915"><a name="p964991154915"></a><a name="p964991154915"></a>Invalid DB engine.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p951455013388"><a name="p951455013388"></a><a name="p951455013388"></a>Check whether the storage engine matches the instance engine.</p>
</td>
</tr>
<tr id="row1846116310512"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p7997192814386"><a name="p7997192814386"></a><a name="p7997192814386"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p640512311512"><a name="p640512311512"></a><a name="p640512311512"></a>DBS.280123</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p14094314515"><a name="p14094314515"></a><a name="p14094314515"></a>Invalid node number.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p051455012380"><a name="p051455012380"></a><a name="p051455012380"></a>Check whether the number of nodes to be added to the instance meets the requirements.</p>
</td>
</tr>
<tr id="row176814142117"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p576884102111"><a name="p576884102111"></a><a name="p576884102111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p3768348212"><a name="p3768348212"></a><a name="p3768348212"></a>DBS.280124</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p17689414211"><a name="p17689414211"></a><a name="p17689414211"></a>Invalid backup.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p167684416216"><a name="p167684416216"></a><a name="p167684416216"></a>Check whether the backup ID is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row152723418518"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p16997192863814"><a name="p16997192863814"></a><a name="p16997192863814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p79497331955"><a name="p79497331955"></a><a name="p79497331955"></a>DBS.280127</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p99531833250"><a name="p99531833250"></a><a name="p99531833250"></a>Invalid backup description.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p165150508387"><a name="p165150508387"></a><a name="p165150508387"></a>Check whether the backup description is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row1526113412516"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1999752817385"><a name="p1999752817385"></a><a name="p1999752817385"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p5960113315510"><a name="p5960113315510"></a><a name="p5960113315510"></a>DBS.280200</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p179648331556"><a name="p179648331556"></a><a name="p179648331556"></a>The password contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p11515250133814"><a name="p11515250133814"></a><a name="p11515250133814"></a>Check whether the password is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row1324133412515"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p5997928133811"><a name="p5997928133811"></a><a name="p5997928133811"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p20969173316517"><a name="p20969173316517"></a><a name="p20969173316517"></a>DBS.280214</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p09722033554"><a name="p09722033554"></a><a name="p09722033554"></a>Invalid retention period.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p4515165093814"><a name="p4515165093814"></a><a name="p4515165093814"></a>Check whether the backup retention period is correct.</p>
</td>
</tr>
<tr id="row142210349512"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p139971528183819"><a name="p139971528183819"></a><a name="p139971528183819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p39801331159"><a name="p39801331159"></a><a name="p39801331159"></a>DBS.280215</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1152914478154"><a name="p1152914478154"></a><a name="p1152914478154"></a>Invalid backup period.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p205151650173815"><a name="p205151650173815"></a><a name="p205151650173815"></a>Check whether the backup start time, end time, and backup cycle are correct and meet the requirements.</p>
</td>
</tr>
<tr id="row142173411516"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p10997728133815"><a name="p10997728133815"></a><a name="p10997728133815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p998918331858"><a name="p998918331858"></a><a name="p998918331858"></a>DBS.280216</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p14993133311516"><a name="p14993133311516"></a><a name="p14993133311516"></a>Invalid backup start time.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p14515150143819"><a name="p14515150143819"></a><a name="p14515150143819"></a>Check whether the backup start time meets the requirements and whether the relationship between the backup start time and end time is correct.</p>
</td>
</tr>
<tr id="row91912346516"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p19971228153817"><a name="p19971228153817"></a><a name="p19971228153817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p299717331512"><a name="p299717331512"></a><a name="p299717331512"></a>DBS.280234</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p2028347513"><a name="p2028347513"></a><a name="p2028347513"></a>Invalid DB instance name.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p651545073811"><a name="p651545073811"></a><a name="p651545073811"></a>Check whether the instance name is correct and whether the instance exists.</p>
</td>
</tr>
<tr id="row1645835353"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p149974289383"><a name="p149974289383"></a><a name="p149974289383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p056817357514"><a name="p056817357514"></a><a name="p056817357514"></a>DBS.280235</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p960957111514"><a name="p960957111514"></a><a name="p960957111514"></a>Invalid DB engine.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p18515135016384"><a name="p18515135016384"></a><a name="p18515135016384"></a>Check whether the DB engine information is correct.</p>
</td>
</tr>
<tr id="row5643935753"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p189992281383"><a name="p189992281383"></a><a name="p189992281383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p95764351251"><a name="p95764351251"></a><a name="p95764351251"></a>DBS.280236</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p7581835357"><a name="p7581835357"></a><a name="p7581835357"></a>Invalid database version.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p2515135012384"><a name="p2515135012384"></a><a name="p2515135012384"></a>Check whether the database version is supported.</p>
</td>
</tr>
<tr id="row464118355518"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p16999102893816"><a name="p16999102893816"></a><a name="p16999102893816"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p115871035857"><a name="p115871035857"></a><a name="p115871035857"></a>DBS.280239</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p359110353512"><a name="p359110353512"></a><a name="p359110353512"></a>Invalid specifications.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p145151350113814"><a name="p145151350113814"></a><a name="p145151350113814"></a>Check whether the specification code is correct, whether the specification exists in the current AZ, and whether the specification is supported.</p>
</td>
</tr>
<tr id="row1263793513515"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p199982815386"><a name="p199982815386"></a><a name="p199982815386"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p160523511514"><a name="p160523511514"></a><a name="p160523511514"></a>DBS.280241</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p176421119181619"><a name="p176421119181619"></a><a name="p176421119181619"></a>Invalid storage type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p20707212223"><a name="p20707212223"></a><a name="p20707212223"></a>Check whether the storage type is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row4636535858"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p0999122815385"><a name="p0999122815385"></a><a name="p0999122815385"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p8615103514510"><a name="p8615103514510"></a><a name="p8615103514510"></a>DBS.280242</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p562020359513"><a name="p562020359513"></a><a name="p562020359513"></a>The storage space is out of range.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1999445411211"><a name="p1999445411211"></a><a name="p1999445411211"></a>Check whether the disk size is correct.</p>
</td>
</tr>
<tr id="row19837236355"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p199918288388"><a name="p199918288388"></a><a name="p199918288388"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1176243613516"><a name="p1176243613516"></a><a name="p1176243613516"></a>DBS.280244</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1476743616519"><a name="p1476743616519"></a><a name="p1476743616519"></a>Invalid AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p8515165016386"><a name="p8515165016386"></a><a name="p8515165016386"></a>Check whether the parameters of the AZ are correct, whether the AZ exists, and whether the AZ matches the specifications.</p>
</td>
</tr>
<tr id="row1783493611511"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p3999152818388"><a name="p3999152818388"></a><a name="p3999152818388"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p8783936153"><a name="p8783936153"></a><a name="p8783936153"></a>DBS.280247</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p4788636752"><a name="p4788636752"></a><a name="p4788636752"></a>Invalid VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1451535063811"><a name="p1451535063811"></a><a name="p1451535063811"></a>Check whether the VPC ID is correct and whether the VPC exists.</p>
</td>
</tr>
<tr id="row108331361651"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1899962820384"><a name="p1899962820384"></a><a name="p1899962820384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p19793836155"><a name="p19793836155"></a><a name="p19793836155"></a>DBS.280248</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p12585183618161"><a name="p12585183618161"></a><a name="p12585183618161"></a>Invalid subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p12515195063813"><a name="p12515195063813"></a><a name="p12515195063813"></a>Check whether the subnet ID is correct and whether the subnet exists.</p>
</td>
</tr>
<tr id="row18311836253"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p169991928103819"><a name="p169991928103819"></a><a name="p169991928103819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p3809133617515"><a name="p3809133617515"></a><a name="p3809133617515"></a>DBS.280249</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p161143821619"><a name="p161143821619"></a><a name="p161143821619"></a>Invalid security group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p5515850123810"><a name="p5515850123810"></a><a name="p5515850123810"></a>Check whether the security group ID is correct and whether the security group exists.</p>
</td>
</tr>
<tr id="row128119112102"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1199920283382"><a name="p1199920283382"></a><a name="p1199920283382"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p162635114107"><a name="p162635114107"></a><a name="p162635114107"></a>DBS.280266</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p22665111100"><a name="p22665111100"></a><a name="p22665111100"></a>Invalid storage space.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p10531181181910"><a name="p10531181181910"></a><a name="p10531181181910"></a>Check whether the storage space is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row1528115115100"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p15999112873813"><a name="p15999112873813"></a><a name="p15999112873813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p62731411105"><a name="p62731411105"></a><a name="p62731411105"></a>DBS.280267</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p8396132412178"><a name="p8396132412178"></a><a name="p8396132412178"></a>Specifications not match.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p751565011387"><a name="p751565011387"></a><a name="p751565011387"></a>Check whether the specification information is correct and whether the specification matches the instance.</p>
</td>
</tr>
<tr id="row125612214105"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p12999328133813"><a name="p12999328133813"></a><a name="p12999328133813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p053952191014"><a name="p053952191014"></a><a name="p053952191014"></a>DBS.280277</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p6203162825313"><a name="p6203162825313"></a><a name="p6203162825313"></a>Invalid backup name.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p175151503389"><a name="p175151503389"></a><a name="p175151503389"></a>Check whether the backup name is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row4561112121010"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1099952853817"><a name="p1099952853817"></a><a name="p1099952853817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p135511929106"><a name="p135511929106"></a><a name="p135511929106"></a>DBS.280280</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1818217287538"><a name="p1818217287538"></a><a name="p1818217287538"></a>Invalid DB instance number.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p751535020385"><a name="p751535020385"></a><a name="p751535020385"></a>Check whether the number of DB instances is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row119051846184612"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p129991628143813"><a name="p129991628143813"></a><a name="p129991628143813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p59051246194618"><a name="p59051246194618"></a><a name="p59051246194618"></a>DBS.280284</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p3905174619466"><a name="p3905174619466"></a><a name="p3905174619466"></a>Invalid IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p45151350193816"><a name="p45151350193816"></a><a name="p45151350193816"></a>Check whether the IP address is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row12653176161013"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p9999152819384"><a name="p9999152819384"></a><a name="p9999152819384"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p196281611109"><a name="p196281611109"></a><a name="p196281611109"></a>DBS.280292</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p11354164451716"><a name="p11354164451716"></a><a name="p11354164451716"></a>Invalid username.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p05154503381"><a name="p05154503381"></a><a name="p05154503381"></a>Check whether the username is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row1927110135103"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p169991228123812"><a name="p169991228123812"></a><a name="p169991228123812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p141711113101014"><a name="p141711113101014"></a><a name="p141711113101014"></a>DBS.280311</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p17175121310105"><a name="p17175121310105"></a><a name="p17175121310105"></a>Invalid storage space.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p185151250173817"><a name="p185151250173817"></a><a name="p185151250173817"></a>Check whether the storage space is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row5709135464416"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p199952893818"><a name="p199952893818"></a><a name="p199952893818"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p18709654114410"><a name="p18709654114410"></a><a name="p18709654114410"></a>DBS.280314</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p167094549444"><a name="p167094549444"></a><a name="p167094549444"></a>Invalid storage type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1751535073817"><a name="p1751535073817"></a><a name="p1751535073817"></a>Check whether the storage type is correct and whether the instance supports the disk type.</p>
</td>
</tr>
<tr id="row126371823195016"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p139991428103817"><a name="p139991428103817"></a><a name="p139991428103817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1163742318502"><a name="p1163742318502"></a><a name="p1163742318502"></a>DBS.280327</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p2637102318506"><a name="p2637102318506"></a><a name="p2637102318506"></a>Invalid node type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p951585013386"><a name="p951585013386"></a><a name="p951585013386"></a>Check whether the node type is correct, whether the node type matches the instance, and whether the node type matches the group ID and node ID.</p>
</td>
</tr>
<tr id="row71151219165417"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p3999112853813"><a name="p3999112853813"></a><a name="p3999112853813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p18115141975412"><a name="p18115141975412"></a><a name="p18115141975412"></a>DBS.280342</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p161151719195418"><a name="p161151719195418"></a><a name="p161151719195418"></a>Invalid DB instance mode.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p651512506384"><a name="p651512506384"></a><a name="p651512506384"></a>Check whether the instance mode is correct and whether the instance mode matches the instance ID.</p>
</td>
</tr>
<tr id="row145231327134419"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p15999132815386"><a name="p15999132815386"></a><a name="p15999132815386"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p2523142720441"><a name="p2523142720441"></a><a name="p2523142720441"></a>DBS.280365</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p18523172710444"><a name="p18523172710444"></a><a name="p18523172710444"></a>Invalid payment mode.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p151545015383"><a name="p151545015383"></a><a name="p151545015383"></a>Check whether the payment mode is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row22881619105"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p13999162810385"><a name="p13999162810385"></a><a name="p13999162810385"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p15876171519104"><a name="p15876171519104"></a><a name="p15876171519104"></a>DBS.280404</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p58814150103"><a name="p58814150103"></a><a name="p58814150103"></a>Invalid DB instance ID.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1515185014381"><a name="p1515185014381"></a><a name="p1515185014381"></a>Check whether the instance ID is correct and meets the requirements.</p>
</td>
</tr>
<tr id="row65873983215"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p25833912325"><a name="p25833912325"></a><a name="p25833912325"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p18581139113213"><a name="p18581139113213"></a><a name="p18581139113213"></a>DBS.280406</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p458193911322"><a name="p458193911322"></a><a name="p458193911322"></a>The DB instance cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p9613534191"><a name="p9613534191"></a><a name="p9613534191"></a>Check whether the DB engine and billing mode support direct deletion of instances.</p>
</td>
</tr>
<tr id="row72451617102"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p18999228193818"><a name="p18999228193818"></a><a name="p18999228193818"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1893911561013"><a name="p1893911561013"></a><a name="p1893911561013"></a>DBS.280414</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p3946161581013"><a name="p3946161581013"></a><a name="p3946161581013"></a>Invalid group type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p95151509384"><a name="p95151509384"></a><a name="p95151509384"></a>Check whether the group type is correct, whether the group type matches the instance, and whether the node type matches the group ID.</p>
</td>
</tr>
<tr id="row3143292346"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p414152963413"><a name="p414152963413"></a><a name="p414152963413"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p18141529203410"><a name="p18141529203410"></a><a name="p18141529203410"></a>DBS.280434</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p6151029113419"><a name="p6151029113419"></a><a name="p6151029113419"></a>Invalid resource specifications code.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1915152993410"><a name="p1915152993410"></a><a name="p1915152993410"></a>Check whether the resource specifications code exists and meets the requirements.</p>
</td>
</tr>
<tr id="row8332314153510"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p2033231453520"><a name="p2033231453520"></a><a name="p2033231453520"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1133231483515"><a name="p1133231483515"></a><a name="p1133231483515"></a>DBS.280446</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1133251411354"><a name="p1133251411354"></a><a name="p1133251411354"></a>The database information does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p933281416353"><a name="p933281416353"></a><a name="p933281416353"></a>Check whether the <strong id="b13824414517"><a name="b13824414517"></a><a name="b13824414517"></a>datastore</strong> field exists.</p>
</td>
</tr>
<tr id="row1636342143512"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p263615427352"><a name="p263615427352"></a><a name="p263615427352"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1363634217357"><a name="p1363634217357"></a><a name="p1363634217357"></a>DBS.280438</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p196361442163515"><a name="p196361442163515"></a><a name="p196361442163515"></a>Invalid encryption key ID.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p20636194243511"><a name="p20636194243511"></a><a name="p20636194243511"></a>Check whether the disk encryption key ID in the request is created and available, and whether the current DB engine supports disk encryption.</p>
</td>
</tr>
<tr id="row248234703516"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p148214719359"><a name="p148214719359"></a><a name="p148214719359"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p204829477352"><a name="p204829477352"></a><a name="p204829477352"></a>DBS.280439</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p154821647143516"><a name="p154821647143516"></a><a name="p154821647143516"></a>Invalid query limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p3482194717357"><a name="p3482194717357"></a><a name="p3482194717357"></a>Check whether the value of the <strong id="b1552023619450"><a name="b1552023619450"></a><a name="b1552023619450"></a>limit</strong> parameter is valid.</p>
</td>
</tr>
<tr id="row1150417043613"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p450412063612"><a name="p450412063612"></a><a name="p450412063612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p195054011365"><a name="p195054011365"></a><a name="p195054011365"></a>DBS.280440</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p850590173617"><a name="p850590173617"></a><a name="p850590173617"></a>Invalid offset.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p35058016369"><a name="p35058016369"></a><a name="p35058016369"></a>Check whether the value of the <strong id="b5477449194511"><a name="b5477449194511"></a><a name="b5477449194511"></a>offset</strong> parameter is valid.</p>
</td>
</tr>
<tr id="row7514188193612"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1351411815362"><a name="p1351411815362"></a><a name="p1351411815362"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p195141285367"><a name="p195141285367"></a><a name="p195141285367"></a>DBS.280441</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p15141582368"><a name="p15141582368"></a><a name="p15141582368"></a>Invalid key.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p1851413816369"><a name="p1851413816369"></a><a name="p1851413816369"></a>Check whether the tag key is valid.</p>
</td>
</tr>
<tr id="row1391665193112"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p12917195133117"><a name="p12917195133117"></a><a name="p12917195133117"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1591725153113"><a name="p1591725153113"></a><a name="p1591725153113"></a>DBS.280443</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1391745115312"><a name="p1391745115312"></a><a name="p1391745115312"></a>The maximum number of connections has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p791775183117"><a name="p791775183117"></a><a name="p791775183117"></a>APIs are frequently called by the same tenant. Reduce the frequency of API calls.</p>
</td>
</tr>
<tr id="row83521241112113"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p15352144112215"><a name="p15352144112215"></a><a name="p15352144112215"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p113527417217"><a name="p113527417217"></a><a name="p113527417217"></a>DBS.280445</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p103521841112120"><a name="p103521841112120"></a><a name="p103521841112120"></a>The DB instance class is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p535254162117"><a name="p535254162117"></a><a name="p535254162117"></a>The current DB instance class is unavailable. Select another one.</p>
</td>
</tr>
<tr id="row265995817586"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1299952815381"><a name="p1299952815381"></a><a name="p1299952815381"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.2 "><p id="p1641417169394"><a name="p1641417169394"></a><a name="p1641417169394"></a>DBS.290000</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.5.1.3 "><p id="p1541815164394"><a name="p1541815164394"></a><a name="p1541815164394"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.5.1.4 "><p id="p165471911286"><a name="p165471911286"></a><a name="p165471911286"></a>Check whether the transferred parameters or URLs are correct and meet the requirements.</p>
</td>
</tr>
</tbody>
</table>

