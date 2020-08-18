# Configuring the Start Time and End Time of Access to Objects in a Bucket<a name="obs_03_0131"></a>

You can configure the bucket policy to limit the time when objects in a bucket are accessible. In the following example, the access time window is from 2019-03-26T12:00:00Z to 2019-03-26T15:00:00Z.

## Procedure<a name="section17557163019204"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
3.  Choose  **Bucket Policies**  \>  **Custom Bucket Policies**.
4.  Click  **Create Bucket Policy**. The  **Create Bucket Policy**  dialog box is displayed.
5.  Configure the parameters according to the following table:

    **Table  1**  Parameters for authorizing the permission to access a specified bucket

    <a name="table7531653104420"></a>
    <table><thead align="left"><tr id="row2532105311447"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p16532195364414"><a name="p16532195364414"></a><a name="p16532195364414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p15532145310443"><a name="p15532145310443"></a><a name="p15532145310443"></a>Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row953216536449"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1653265344417"><a name="p1653265344417"></a><a name="p1653265344417"></a>Policy Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p55421614212"><a name="p55421614212"></a><a name="p55421614212"></a><strong id="b172342029135518"><a name="b172342029135518"></a><a name="b172342029135518"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row16532753114417"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p353219537448"><a name="p353219537448"></a><a name="p353219537448"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p26391018182813"><a name="p26391018182813"></a><a name="p26391018182813"></a><strong id="b143218342553"><a name="b143218342553"></a><a name="b143218342553"></a>Allow</strong></p>
    </td>
    </tr>
    <tr id="row115321753164415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1553215538449"><a name="p1553215538449"></a><a name="p1553215538449"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1133312113418"></a><a name="ul1133312113418"></a><ul id="ul1133312113418"><li><strong id="b1994283616555"><a name="b1994283616555"></a><a name="b1994283616555"></a>Include</strong></li><li>Select <strong id="b1161253710553"><a name="b1161253710553"></a><a name="b1161253710553"></a>Other account</strong>, and enter an asterisk (*) as the account ID, indicating all anonymous users.</li></ul>
    </td>
    </tr>
    <tr id="row653285374414"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p753212538444"><a name="p753212538444"></a><a name="p753212538444"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul12411915123314"></a><a name="ul12411915123314"></a><ul id="ul12411915123314"><li><strong id="b12264540175515"><a name="b12264540175515"></a><a name="b12264540175515"></a>Include</strong></li><li>Leave the field blank, indicating the policy takes effect on the entire bucket.</li></ul>
    </td>
    </tr>
    <tr id="row18790945165418"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12791194519544"><a name="p12791194519544"></a><a name="p12791194519544"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1691025316358"></a><a name="ul1691025316358"></a><ul id="ul1691025316358"><li><strong id="b1431713433559"><a name="b1431713433559"></a><a name="b1431713433559"></a>Include</strong></li><li>Select the asterisk (*), indicating all actions are involved.</li></ul>
    </td>
    </tr>
    <tr id="row3328954204119"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2329115416419"><a name="p2329115416419"></a><a name="p2329115416419"></a>Conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul4774185114612"></a><a name="ul4774185114612"></a><ul id="ul4774185114612"><li>Condition Operator: DateGreaterThan</li><li>Key: CurrentTime</li><li>Value: 2019-03-26T12:00:00Z</li></ul>
    </td>
    </tr>
    <tr id="row7578193710492"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4237154224913"><a name="p4237154224913"></a><a name="p4237154224913"></a>Conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul162371942124912"></a><a name="ul162371942124912"></a><ul id="ul162371942124912"><li>Condition Operator: DateLessThan</li><li>Key: CurrentTime</li><li>Value: 2019-03-26T15:00:00Z</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

## Verification<a name="section159232335471"></a>

During the specified time period, any user can access the specified resources in the bucket. Outside the specified time period, only the bucket owner can access the bucket.

