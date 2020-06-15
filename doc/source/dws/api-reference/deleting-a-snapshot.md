# Deleting a Snapshot<a name="dws_02_0027"></a>

## Function<a name="sfcf2baffe2ad46fa81d55b2dd2bf89bc"></a>

This API is used to delete a specified snapshot.

## URI<a name="s38a27afad7024ce3852e9847fd94c040"></a>

-   URI format

    DELETE /v1.0/\{project\_id\}/snapshots/\{snapshot\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="en-us_topic_0067607271_table34550710"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607271_row5432205"><th class="cellrowborder" valign="top" width="21.94%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607271_p37355470"><a name="en-us_topic_0067607271_p37355470"></a><a name="en-us_topic_0067607271_p37355470"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.03%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607271_p5894231"><a name="en-us_topic_0067607271_p5894231"></a><a name="en-us_topic_0067607271_p5894231"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.39%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607271_p7670737"><a name="en-us_topic_0067607271_p7670737"></a><a name="en-us_topic_0067607271_p7670737"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.64%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607271_p17349988"><a name="en-us_topic_0067607271_p17349988"></a><a name="en-us_topic_0067607271_p17349988"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607271_row63171767"><td class="cellrowborder" valign="top" width="21.94%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607271_p16639474"><a name="en-us_topic_0067607271_p16639474"></a><a name="en-us_topic_0067607271_p16639474"></a>project _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.03%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607271_p5620158"><a name="en-us_topic_0067607271_p5620158"></a><a name="en-us_topic_0067607271_p5620158"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.39%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607271_p52579650"><a name="en-us_topic_0067607271_p52579650"></a><a name="en-us_topic_0067607271_p52579650"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.64%" headers="mcps1.2.5.1.4 "><p id="p1590591325620"><a name="p1590591325620"></a><a name="p1590591325620"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607271_row11404133"><td class="cellrowborder" valign="top" width="21.94%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607271_p51319614"><a name="en-us_topic_0067607271_p51319614"></a><a name="en-us_topic_0067607271_p51319614"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.03%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607271_p63248075"><a name="en-us_topic_0067607271_p63248075"></a><a name="en-us_topic_0067607271_p63248075"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.39%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607271_p22820469"><a name="en-us_topic_0067607271_p22820469"></a><a name="en-us_topic_0067607271_p22820469"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.64%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607271_p36518691"><a name="en-us_topic_0067607271_p36518691"></a><a name="en-us_topic_0067607271_p36518691"></a>Snapshot ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s649ab73a82e34ecd9160b0060a337f92"></a>

Sample request

```
DELETE /v1.0/89cd04f168b84af6be287f71730fdb4b/snapshots/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90
```

## Response<a name="sbec897acaf7347c0ac1723e38546a861"></a>

Sample response

```
STATUS CODE 202
```

## Returned Values<a name="s33606771ebd747ddac1c88ee301f2aea"></a>

-   Normal

    202

-   Abnormal 

    **Table  2**  Returned value description

    <a name="en-us_topic_0067607271_table35025494"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607271_row59481773"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="en-us_topic_0067607271_p53294272"><a name="en-us_topic_0067607271_p53294272"></a><a name="en-us_topic_0067607271_p53294272"></a><strong id="b842352706104927"><a name="b842352706104927"></a><a name="b842352706104927"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="en-us_topic_0067607271_p21868813"><a name="en-us_topic_0067607271_p21868813"></a><a name="en-us_topic_0067607271_p21868813"></a><strong id="b1170659825"><a name="b1170659825"></a><a name="b1170659825"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607271_row26543418"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607271_p2533231"><a name="en-us_topic_0067607271_p2533231"></a><a name="en-us_topic_0067607271_p2533231"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607271_p3865173"><a name="en-us_topic_0067607271_p3865173"></a><a name="en-us_topic_0067607271_p3865173"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607271_row34786562"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607271_p66248115"><a name="en-us_topic_0067607271_p66248115"></a><a name="en-us_topic_0067607271_p66248115"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607271_p64497130"><a name="en-us_topic_0067607271_p64497130"></a><a name="en-us_topic_0067607271_p64497130"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607271_row43603258"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607271_p42202994"><a name="en-us_topic_0067607271_p42202994"></a><a name="en-us_topic_0067607271_p42202994"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607271_p62999330"><a name="en-us_topic_0067607271_p62999330"></a><a name="en-us_topic_0067607271_p62999330"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607271_row30123063"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607271_p24049039"><a name="en-us_topic_0067607271_p24049039"></a><a name="en-us_topic_0067607271_p24049039"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607271_p1815156"><a name="en-us_topic_0067607271_p1815156"></a><a name="en-us_topic_0067607271_p1815156"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607271_row16336406"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607271_p48180537"><a name="en-us_topic_0067607271_p48180537"></a><a name="en-us_topic_0067607271_p48180537"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607271_p10309404"><a name="en-us_topic_0067607271_p10309404"></a><a name="en-us_topic_0067607271_p10309404"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607271_row25675773"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607271_p66471715"><a name="en-us_topic_0067607271_p66471715"></a><a name="en-us_topic_0067607271_p66471715"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607271_p15499871"><a name="en-us_topic_0067607271_p15499871"></a><a name="en-us_topic_0067607271_p15499871"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


