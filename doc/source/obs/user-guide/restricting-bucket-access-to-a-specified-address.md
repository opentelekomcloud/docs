# Restricting Bucket Access to a Specified Address <a name="obs_03_0130"></a>

You can configure a bucket policy to authorize a specified address the permission to access the bucket. This example shows how to deny a client access whose source IP address is within the range of 114.115.1.0/24.

## Procedure<a name="section17557163019204"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
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
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p55421614212"><a name="p55421614212"></a><a name="p55421614212"></a><strong id="b38199484516"><a name="b38199484516"></a><a name="b38199484516"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row16532753114417"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p353219537448"><a name="p353219537448"></a><a name="p353219537448"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p26391018182813"><a name="p26391018182813"></a><a name="p26391018182813"></a>Deny</p>
    </td>
    </tr>
    <tr id="row115321753164415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1553215538449"><a name="p1553215538449"></a><a name="p1553215538449"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul034219193595"></a><a name="ul034219193595"></a><ul id="ul034219193595"><li><strong id="b89101659165017"><a name="b89101659165017"></a><a name="b89101659165017"></a>Include</strong> &gt; <strong id="b10821572511"><a name="b10821572511"></a><a name="b10821572511"></a>Other account</strong></li><li>If the account ID is set to <strong id="b371945013539"><a name="b371945013539"></a><a name="b371945013539"></a>*</strong>, the policy setting takes effect on all anonymous users.</li><li>Leave the user ID blank.</li></ul>
    </td>
    </tr>
    <tr id="row653285374414"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p753212538444"><a name="p753212538444"></a><a name="p753212538444"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul12411915123314"></a><a name="ul12411915123314"></a><ul id="ul12411915123314"><li><strong id="b8351230522"><a name="b8351230522"></a><a name="b8351230522"></a>Include</strong></li><li>Leave the field blank, indicating the policy takes effect on the entire bucket.</li></ul>
    </td>
    </tr>
    <tr id="row18790945165418"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12791194519544"><a name="p12791194519544"></a><a name="p12791194519544"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1691025316358"></a><a name="ul1691025316358"></a><ul id="ul1691025316358"><li><strong id="b594281345212"><a name="b594281345212"></a><a name="b594281345212"></a>Include</strong></li><li>Select the asterisk (*), indicating all actions are involved.</li></ul>
    </td>
    </tr>
    <tr id="row3328954204119"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2329115416419"><a name="p2329115416419"></a><a name="p2329115416419"></a>Conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul4774185114612"></a><a name="ul4774185114612"></a><ul id="ul4774185114612"><li>Conditional Operator: <strong id="b10912524131710"><a name="b10912524131710"></a><a name="b10912524131710"></a>IpAddress</strong></li><li>Key: <strong id="b194301328111717"><a name="b194301328111717"></a><a name="b194301328111717"></a>SourceIP</strong></li><li>Value: <strong id="b158527333177"><a name="b158527333177"></a><a name="b158527333177"></a>114.115.1.0/24</strong></li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

## Verification<a name="section159232335471"></a>

Initiate an access request from an IP address within the range of 114.115.1.0/24. The access is denied. Initiate an access request from an IP address outside the range of 114.115.1.0/24. The access is allowed.

