# Quota Management<a name="sfs_02_0032"></a>

## Function<a name="sae5d66e3796d41b9a2de59a0dc61f223"></a>

This API is used to query quota information.

## URI<a name="s919f447ab875452f9c131736b82de50d"></a>

-   GET /v2/\{project\_id\}/os-quota-sets/\{project\_id\}
-   Parameter description

    <a name="en-us_topic_0076901826_table4500571"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901826_row28406254"><th class="cellrowborder" valign="top" width="16.160000000000004%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.720000000000002%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.980000000000004%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.14000000000001%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901826_row5055772"><td class="cellrowborder" valign="top" width="16.160000000000004%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0076901826_p6864370"><a name="en-us_topic_0076901826_p6864370"></a><a name="en-us_topic_0076901826_p6864370"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.720000000000002%" headers="mcps1.1.5.1.2 "><p id="abe07e8ecc2484f28909f03d317e08907"><a name="abe07e8ecc2484f28909f03d317e08907"></a><a name="abe07e8ecc2484f28909f03d317e08907"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.5.1.3 "><p id="ab5b3a85c0cbd4e9b8fa4058ee0714927"><a name="ab5b3a85c0cbd4e9b8fa4058ee0714927"></a><a name="ab5b3a85c0cbd4e9b8fa4058ee0714927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.14000000000001%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0076901826_p7089989"><a name="en-us_topic_0076901826_p7089989"></a><a name="en-us_topic_0076901826_p7089989"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    <tr id="r0d2a51699d5a49da898264abc9f1b128"><td class="cellrowborder" valign="top" width="16.160000000000004%" headers="mcps1.1.5.1.1 "><p id="a2d281854f2eb4cddbf8e566e0d239477"><a name="a2d281854f2eb4cddbf8e566e0d239477"></a><a name="a2d281854f2eb4cddbf8e566e0d239477"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.720000000000002%" headers="mcps1.1.5.1.2 "><p id="a8a4d149d86514f139178c7a5f130e49d"><a name="a8a4d149d86514f139178c7a5f130e49d"></a><a name="a8a4d149d86514f139178c7a5f130e49d"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.5.1.3 "><p id="a7f05a56b5ab64bb0ba3ce83619e7a1c1"><a name="a7f05a56b5ab64bb0ba3ce83619e7a1c1"></a><a name="a7f05a56b5ab64bb0ba3ce83619e7a1c1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.14000000000001%" headers="mcps1.1.5.1.4 "><p id="a9cbaf09c4cb145d1ba50663237ac0057"><a name="a9cbaf09c4cb145d1ba50663237ac0057"></a><a name="a9cbaf09c4cb145d1ba50663237ac0057"></a>Specifies the UUID of the tenant whose quotas are to be queried, updated, or deleted. This ID differs from the first project ID (the administrative tenant ID) contained in the URI.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s53e70cf9c4294354b04bef2c780a2c40"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="sca6c6277137143418e30f3336643a715"></a>

-   Parameter description

    <a name="en-us_topic_0076901826_table3568621"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901826_row1012336"><th class="cellrowborder" valign="top" width="18.82%" id="mcps1.1.4.1.1"><p id="p1625545571614"><a name="p1625545571614"></a><a name="p1625545571614"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.61%" id="mcps1.1.4.1.2"><p id="p152551855171610"><a name="p152551855171610"></a><a name="p152551855171610"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.57%" id="mcps1.1.4.1.3"><p id="p2025518555164"><a name="p2025518555164"></a><a name="p2025518555164"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901826_row14556344"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0076901826_p38213209"><a name="en-us_topic_0076901826_p38213209"></a><a name="en-us_topic_0076901826_p38213209"></a>quota_set</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.1.4.1.2 "><p id="a5e0ee8dfccfb4fffa9cd255b6b501083"><a name="a5e0ee8dfccfb4fffa9cd255b6b501083"></a><a name="a5e0ee8dfccfb4fffa9cd255b6b501083"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.57%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0076901826_p59737926"><a name="en-us_topic_0076901826_p59737926"></a><a name="en-us_topic_0076901826_p59737926"></a>Specifies the <strong id="a6dd039e874a0499ca1c947697e1eb718"><a name="a6dd039e874a0499ca1c947697e1eb718"></a><a name="a6dd039e874a0499ca1c947697e1eb718"></a>quota_set</strong> object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **quota\_set**

    <a name="en-us_topic_0076901826_table6933822"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901826_row62702560"><th class="cellrowborder" valign="top" width="19.02%" id="mcps1.1.4.1.1"><p id="p668353232318"><a name="p668353232318"></a><a name="p668353232318"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.1%" id="mcps1.1.4.1.2"><p id="p1669993218236"><a name="p1669993218236"></a><a name="p1669993218236"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.879999999999995%" id="mcps1.1.4.1.3"><p id="p1869903222310"><a name="p1869903222310"></a><a name="p1869903222310"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901826_row23970955"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.1.4.1.1 "><p id="a8d8e91948abd415bab9fb23221a90046"><a name="a8d8e91948abd415bab9fb23221a90046"></a><a name="a8d8e91948abd415bab9fb23221a90046"></a>gigabytes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.1%" headers="mcps1.1.4.1.2 "><p id="a517bf08a8d294ea79160b1ac2f5d923a"><a name="a517bf08a8d294ea79160b1ac2f5d923a"></a><a name="a517bf08a8d294ea79160b1ac2f5d923a"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.879999999999995%" headers="mcps1.1.4.1.3 "><p id="a9c2a25e69a44424685d93d13f44b29ba"><a name="a9c2a25e69a44424685d93d13f44b29ba"></a><a name="a9c2a25e69a44424685d93d13f44b29ba"></a>Specifies the capacity in gigabytes allowed for each tenant.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row5408778"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.1.4.1.1 "><p id="a1936c65e0a04435eaa0a3f8582c0c174"><a name="a1936c65e0a04435eaa0a3f8582c0c174"></a><a name="a1936c65e0a04435eaa0a3f8582c0c174"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.1%" headers="mcps1.1.4.1.2 "><p id="a5788cc83a60e4509b31287f82145c82a"><a name="a5788cc83a60e4509b31287f82145c82a"></a><a name="a5788cc83a60e4509b31287f82145c82a"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.879999999999995%" headers="mcps1.1.4.1.3 "><p id="ab98c2c3aac7945489694019fa7f510d4"><a name="ab98c2c3aac7945489694019fa7f510d4"></a><a name="ab98c2c3aac7945489694019fa7f510d4"></a>Specifies the number of snapshots allowed for each tenant.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row41075474"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.1.4.1.1 "><p id="ac5004bccb3024d17b94e14b7927475d1"><a name="ac5004bccb3024d17b94e14b7927475d1"></a><a name="ac5004bccb3024d17b94e14b7927475d1"></a>shares</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.1%" headers="mcps1.1.4.1.2 "><p id="af6c52a75e74e45c3ad7dc9e336832187"><a name="af6c52a75e74e45c3ad7dc9e336832187"></a><a name="af6c52a75e74e45c3ad7dc9e336832187"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.879999999999995%" headers="mcps1.1.4.1.3 "><p id="ac5f7e2ea3aee4bce90a926dc4679625b"><a name="ac5f7e2ea3aee4bce90a926dc4679625b"></a><a name="ac5f7e2ea3aee4bce90a926dc4679625b"></a>Specifies the number of shared file systems allowed for each tenant.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row3980335"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.1.4.1.1 "><p id="a69156d5bfead49deb0957cf3c277a04f"><a name="a69156d5bfead49deb0957cf3c277a04f"></a><a name="a69156d5bfead49deb0957cf3c277a04f"></a>snapshot_gigabytes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.1%" headers="mcps1.1.4.1.2 "><p id="a35386603e0bc49b2bcbc32711536f038"><a name="a35386603e0bc49b2bcbc32711536f038"></a><a name="a35386603e0bc49b2bcbc32711536f038"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.879999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0076901826_p373644417460"><a name="en-us_topic_0076901826_p373644417460"></a><a name="en-us_topic_0076901826_p373644417460"></a>Specifies the snapshot capacity in gigabytes allowed for each tenant.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row53951920"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.1.4.1.1 "><p id="ace8af1d8b3b04deeabc8042616802b4a"><a name="ace8af1d8b3b04deeabc8042616802b4a"></a><a name="ace8af1d8b3b04deeabc8042616802b4a"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.1%" headers="mcps1.1.4.1.2 "><p id="a679c945dff524ecea199bfb5637c5109"><a name="a679c945dff524ecea199bfb5637c5109"></a><a name="a679c945dff524ecea199bfb5637c5109"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.879999999999995%" headers="mcps1.1.4.1.3 "><p id="a0142089f734d4cb0ac737c7b0024ee63"><a name="a0142089f734d4cb0ac737c7b0024ee63"></a><a name="a0142089f734d4cb0ac737c7b0024ee63"></a>Specifies the UUID of the tenant for which you manage quotas.</p>
    </td>
    </tr>
    <tr id="r416c1321d0114a39a2c0a0f69cb2bc7d"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.1.4.1.1 "><p id="aa7ab7e6ff253473d96fcf9b7aa652c8e"><a name="aa7ab7e6ff253473d96fcf9b7aa652c8e"></a><a name="aa7ab7e6ff253473d96fcf9b7aa652c8e"></a>share_networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.1%" headers="mcps1.1.4.1.2 "><p id="ae8441227ac794c4691c7b462ce798d95"><a name="ae8441227ac794c4691c7b462ce798d95"></a><a name="ae8441227ac794c4691c7b462ce798d95"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.879999999999995%" headers="mcps1.1.4.1.3 "><p id="a33b70c5365f749788efee1362395fbcd"><a name="a33b70c5365f749788efee1362395fbcd"></a><a name="a33b70c5365f749788efee1362395fbcd"></a>Specifies the number of share networks for each tenant.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "quota_set": {
        "gigabytes": -1,
        "snapshots": -1,
        "snapshot_gigabytes": -1,
        "shares": -1,
        "id": "da0f615c35eb4d72812d1547a77b5394",
        "share_networks": 10
      }
    }
    ```


## Status Codes<a name="se03a0585821d49e9866d81f1b1c57630"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0076901826_table57106866"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901826_row17172873"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0076901826_p48825474"><a name="en-us_topic_0076901826_p48825474"></a><a name="en-us_topic_0076901826_p48825474"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0076901826_p62549356"><a name="en-us_topic_0076901826_p62549356"></a><a name="en-us_topic_0076901826_p62549356"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901826_row33333103"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p15626802"><a name="en-us_topic_0076901826_p15626802"></a><a name="en-us_topic_0076901826_p15626802"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p57811421"><a name="en-us_topic_0076901826_p57811421"></a><a name="en-us_topic_0076901826_p57811421"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row50540745"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p159717"><a name="en-us_topic_0076901826_p159717"></a><a name="en-us_topic_0076901826_p159717"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p12937084"><a name="en-us_topic_0076901826_p12937084"></a><a name="en-us_topic_0076901826_p12937084"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row49324898"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p35893824"><a name="en-us_topic_0076901826_p35893824"></a><a name="en-us_topic_0076901826_p35893824"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p21718606"><a name="en-us_topic_0076901826_p21718606"></a><a name="en-us_topic_0076901826_p21718606"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row61249726"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p62280792"><a name="en-us_topic_0076901826_p62280792"></a><a name="en-us_topic_0076901826_p62280792"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p11579382"><a name="en-us_topic_0076901826_p11579382"></a><a name="en-us_topic_0076901826_p11579382"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row37105578"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p52761866"><a name="en-us_topic_0076901826_p52761866"></a><a name="en-us_topic_0076901826_p52761866"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p45852771"><a name="en-us_topic_0076901826_p45852771"></a><a name="en-us_topic_0076901826_p45852771"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row10021756"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p6455868"><a name="en-us_topic_0076901826_p6455868"></a><a name="en-us_topic_0076901826_p6455868"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p53163272"><a name="en-us_topic_0076901826_p53163272"></a><a name="en-us_topic_0076901826_p53163272"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row8707407"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p34211353"><a name="en-us_topic_0076901826_p34211353"></a><a name="en-us_topic_0076901826_p34211353"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p19656228"><a name="en-us_topic_0076901826_p19656228"></a><a name="en-us_topic_0076901826_p19656228"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row42688329"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p35202648"><a name="en-us_topic_0076901826_p35202648"></a><a name="en-us_topic_0076901826_p35202648"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p32842235"><a name="en-us_topic_0076901826_p32842235"></a><a name="en-us_topic_0076901826_p32842235"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row27144664"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p51234165"><a name="en-us_topic_0076901826_p51234165"></a><a name="en-us_topic_0076901826_p51234165"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p56326682"><a name="en-us_topic_0076901826_p56326682"></a><a name="en-us_topic_0076901826_p56326682"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row37178096"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p58635765"><a name="en-us_topic_0076901826_p58635765"></a><a name="en-us_topic_0076901826_p58635765"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p51876502"><a name="en-us_topic_0076901826_p51876502"></a><a name="en-us_topic_0076901826_p51876502"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row64235341"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p35680165"><a name="en-us_topic_0076901826_p35680165"></a><a name="en-us_topic_0076901826_p35680165"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p4412237"><a name="en-us_topic_0076901826_p4412237"></a><a name="en-us_topic_0076901826_p4412237"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row39710134"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p62404314"><a name="en-us_topic_0076901826_p62404314"></a><a name="en-us_topic_0076901826_p62404314"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p21584674"><a name="en-us_topic_0076901826_p21584674"></a><a name="en-us_topic_0076901826_p21584674"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row60044343"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p31753649"><a name="en-us_topic_0076901826_p31753649"></a><a name="en-us_topic_0076901826_p31753649"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p21908804"><a name="en-us_topic_0076901826_p21908804"></a><a name="en-us_topic_0076901826_p21908804"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901826_row62961510"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901826_p66717520"><a name="en-us_topic_0076901826_p66717520"></a><a name="en-us_topic_0076901826_p66717520"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901826_p35410022"><a name="en-us_topic_0076901826_p35410022"></a><a name="en-us_topic_0076901826_p35410022"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


