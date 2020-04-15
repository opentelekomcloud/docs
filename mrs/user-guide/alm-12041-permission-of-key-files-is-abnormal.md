# ALM-12041 Permission of Key Files Is Abnormal<a name="EN-US_TOPIC_0125375437"></a>

## Description<a name="s079c15d370344286900d0b13f593afbe"></a>

The system checks the permission, users, and user groups of key directories or files every hour. This alarm is generated when any of these is abnormal.

This alarm is cleared when the problem that causes abnormal permission, users, or user groups is solved.

## Attribute<a name="s0af0e33039034b4996cff6c93ddca98e"></a>

<a name="t26a5c1041cc641858a2c313feeed8559"></a>
<table><thead align="left"><tr id="rb3dcf6e6f7bf4c76926522ccb079ac83"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0057219549_p381563195959"><a name="en-us_topic_0057219549_p381563195959"></a><a name="en-us_topic_0057219549_p381563195959"></a><strong id="af66ad2b01a8e4b499477a28eeb296778"><a name="af66ad2b01a8e4b499477a28eeb296778"></a><a name="af66ad2b01a8e4b499477a28eeb296778"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a2adc2b4f99974cc49cb2b0e6f8db6e37"><a name="a2adc2b4f99974cc49cb2b0e6f8db6e37"></a><a name="a2adc2b4f99974cc49cb2b0e6f8db6e37"></a><strong id="en-us_topic_0057219549_b275129495959"><a name="en-us_topic_0057219549_b275129495959"></a><a name="en-us_topic_0057219549_b275129495959"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a53182aa0cfc74d1184edbb4de51dd1b8"><a name="a53182aa0cfc74d1184edbb4de51dd1b8"></a><a name="a53182aa0cfc74d1184edbb4de51dd1b8"></a><strong id="a4e216aa4735d4bb49d528de911a6316c"><a name="a4e216aa4735d4bb49d528de911a6316c"></a><a name="a4e216aa4735d4bb49d528de911a6316c"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r325d867c973342179267636d65361d14"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a9cd11cefc5f84fc68e232375f53cbbb1"><a name="a9cd11cefc5f84fc68e232375f53cbbb1"></a><a name="a9cd11cefc5f84fc68e232375f53cbbb1"></a>12041</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057219549_p215465395959"><a name="en-us_topic_0057219549_p215465395959"></a><a name="en-us_topic_0057219549_p215465395959"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a22d2fbca8cf447999b8a24c1515879b5"><a name="a22d2fbca8cf447999b8a24c1515879b5"></a><a name="a22d2fbca8cf447999b8a24c1515879b5"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s4b784c050e154fbba324c41bcb1b782c"></a>

<a name="tc86b25dd9bab4a23a60299f45a2819f1"></a>
<table><thead align="left"><tr id="rbca6042cbed64918b3293fa643f32cfc"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a649b27b3bdff42cba782de940771842b"><a name="a649b27b3bdff42cba782de940771842b"></a><a name="a649b27b3bdff42cba782de940771842b"></a><strong id="afc7e46bbedac40258132b3ab3347094c"><a name="afc7e46bbedac40258132b3ab3347094c"></a><a name="afc7e46bbedac40258132b3ab3347094c"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="af28770dd9a13416782e405dacb5aca0b"><a name="af28770dd9a13416782e405dacb5aca0b"></a><a name="af28770dd9a13416782e405dacb5aca0b"></a><strong id="af6be0f121e204c99be584f79c866464e"><a name="af6be0f121e204c99be584f79c866464e"></a><a name="af6be0f121e204c99be584f79c866464e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r5be2a0daa358463ba08c884539deceed"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac7bd685f1d0e4b4682600bc458c547ba"><a name="ac7bd685f1d0e4b4682600bc458c547ba"></a><a name="ac7bd685f1d0e4b4682600bc458c547ba"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0057219549_p882488010027"><a name="en-us_topic_0057219549_p882488010027"></a><a name="en-us_topic_0057219549_p882488010027"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra4f8ce039f2b4d65befb09a2fa87bce0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="afbee214128b94e0a9e85b4aa177bdd62"><a name="afbee214128b94e0a9e85b4aa177bdd62"></a><a name="afbee214128b94e0a9e85b4aa177bdd62"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0057219549_p2780510027"><a name="en-us_topic_0057219549_p2780510027"></a><a name="en-us_topic_0057219549_p2780510027"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rac2071c7009144cc818db3399ea1fe92"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae6ac5a3b66ec4afdabca37baae64c75b"><a name="ae6ac5a3b66ec4afdabca37baae64c75b"></a><a name="ae6ac5a3b66ec4afdabca37baae64c75b"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a67949d7128f84faa844b8cff308d8232"><a name="a67949d7128f84faa844b8cff308d8232"></a><a name="a67949d7128f84faa844b8cff308d8232"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r145f21926fcf42deb28e91c083150a40"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ace1a9008a226438ba55c6bfa4a03b046"><a name="ace1a9008a226438ba55c6bfa4a03b046"></a><a name="ace1a9008a226438ba55c6bfa4a03b046"></a>PathName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a632c63564870412d9b68e141a14fe346"><a name="a632c63564870412d9b68e141a14fe346"></a><a name="a632c63564870412d9b68e141a14fe346"></a>Specifies the file path or file name.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sba191e6a34934b908d2c1f7d3dd5c750"></a>

System functions are unavailable.

## Possible Causes<a name="s4f8f179c1c43438ba0dcdde9d6cef8f1"></a>

The user has manually modified the file permission, user information, or user groups, or the system has experienced an unexpected power-off.

## Procedure<a name="s2587f37cdf0d413c8b5552a67e4ce8e0"></a>

1.  Check the file permission.
    1.  On MRS Manager, click  **Alarm**.
    2.  In the details of the alarm, query the  **HostName** \(name of the alarmed host\) and **PathName**  \(path or name of the involved file\).
    3.  Log in to the alarm node.
    4.  Run the  **ll** _PathName_  command to query the current user, permission, and user group of the file or path.
    5.  <a name="l7e4f0e9011824aef908256cbfa50212e"></a>Go to the  **$\{BIGDATA\_HOME\}/nodeagent/etc/agent/autocheck** directory and run the **vi keyfile**  command. Search for the name of the involved file and query the correct permission of the file.
    6.  Compare the actual permission of the file with the permission obtained in  [1.e](#l7e4f0e9011824aef908256cbfa50212e). If they are different, change the actual permission, user information, and user group to the correct values.
    7.  Wait until the next system check is complete and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l38006af57f344e799eb4fd427e227149).

2.  <a name="l38006af57f344e799eb4fd427e227149"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

        Telephone:

        Germany: 0800 330 44 44

        International: +800 44556600



## Related Information<a name="s617aff6984d94af38d6ebfcb5e5668f2"></a>

N/A

