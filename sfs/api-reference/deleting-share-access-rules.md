# Deleting Share Access Rules<a name="sfs_02_0030"></a>

## Function<a name="s1a5be1c634fa405ba06c19e1af9f3d40"></a>

This API is used to delete a share access rule.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API is an asynchronous API. If the returned status code is  **202**, the API request is successfully delivered and received. Later, you can refer to  [Querying Share Access Rules](querying-share-access-rules.md)  to identify whether the deletion of the share access rule is complete and successful.  

## URI<a name="sd0a208cfe579473ebd8103fe98120524"></a>

-   POST  /v2/\{project\_id\}/shares/\{share\_id\}/action
-   Parameter description

    <a name="en-us_topic_0064390799_table38758958"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390799_row40742509"><th class="cellrowborder" valign="top" width="20.16%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.83%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.279999999999998%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.730000000000004%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390799_row63404869"><td class="cellrowborder" valign="top" width="20.16%" headers="mcps1.1.5.1.1 "><p id="a9ab33272c5414630949ff32c58bf1590"><a name="a9ab33272c5414630949ff32c58bf1590"></a><a name="a9ab33272c5414630949ff32c58bf1590"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.83%" headers="mcps1.1.5.1.2 "><p id="ad364fbce5fdc48189bce7a175ee8e94b"><a name="ad364fbce5fdc48189bce7a175ee8e94b"></a><a name="ad364fbce5fdc48189bce7a175ee8e94b"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.1.5.1.3 "><p id="a8a6d2a4cc8d244f2b4b374571a243128"><a name="a8a6d2a4cc8d244f2b4b374571a243128"></a><a name="a8a6d2a4cc8d244f2b4b374571a243128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.730000000000004%" headers="mcps1.1.5.1.4 "><p id="a4fb7cc60bee246c9a28baa9a19a42260"><a name="a4fb7cc60bee246c9a28baa9a19a42260"></a><a name="a4fb7cc60bee246c9a28baa9a19a42260"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row43163346"><td class="cellrowborder" valign="top" width="20.16%" headers="mcps1.1.5.1.1 "><p id="a59173d5ae3334777871059512bb67a7a"><a name="a59173d5ae3334777871059512bb67a7a"></a><a name="a59173d5ae3334777871059512bb67a7a"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.83%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0064390799_p856561217407"><a name="en-us_topic_0064390799_p856561217407"></a><a name="en-us_topic_0064390799_p856561217407"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.1.5.1.3 "><p id="a23e80aa107554437b2a2cc9d93ced01a"><a name="a23e80aa107554437b2a2cc9d93ced01a"></a><a name="a23e80aa107554437b2a2cc9d93ced01a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.730000000000004%" headers="mcps1.1.5.1.4 "><p id="a7f2f8b0f2c4a484499c65c3e2a6cb2e6"><a name="a7f2f8b0f2c4a484499c65c3e2a6cb2e6"></a><a name="a7f2f8b0f2c4a484499c65c3e2a6cb2e6"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s840db22bfac0425eb0cf3366f68629ef"></a>

-   Parameter description

    <a name="en-us_topic_0064390799_table42069424"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390799_row20618333"><th class="cellrowborder" valign="top" width="19.791979197919794%" id="mcps1.1.5.1.1"><p id="p1783914071518"><a name="p1783914071518"></a><a name="p1783914071518"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.52135213521352%" id="mcps1.1.5.1.2"><p id="p10839134015152"><a name="p10839134015152"></a><a name="p10839134015152"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.801880188018806%" id="mcps1.1.5.1.3"><p id="p11839940121513"><a name="p11839940121513"></a><a name="p11839940121513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.88478847884789%" id="mcps1.1.5.1.4"><p id="p883994019154"><a name="p883994019154"></a><a name="p883994019154"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390799_row35228531"><td class="cellrowborder" valign="top" width="19.791979197919794%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390799_p34938791"><a name="en-us_topic_0064390799_p34938791"></a><a name="en-us_topic_0064390799_p34938791"></a>os-deny_access</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.52135213521352%" headers="mcps1.1.5.1.2 "><p id="abe11d32a4d2143b19ccb091cc19ec0d4"><a name="abe11d32a4d2143b19ccb091cc19ec0d4"></a><a name="abe11d32a4d2143b19ccb091cc19ec0d4"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.801880188018806%" headers="mcps1.1.5.1.3 "><p id="ac6f7260e19d24659ae13f28c9bb97c00"><a name="ac6f7260e19d24659ae13f28c9bb97c00"></a><a name="ac6f7260e19d24659ae13f28c9bb97c00"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.88478847884789%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390799_p18961705"><a name="en-us_topic_0064390799_p18961705"></a><a name="en-us_topic_0064390799_p18961705"></a>Specifies the <strong id="afc657c67057642c8b9ab5fbcb404fd03"><a name="afc657c67057642c8b9ab5fbcb404fd03"></a><a name="afc657c67057642c8b9ab5fbcb404fd03"></a>os-deny_access</strong> object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **os-deny\_access**

    <a name="table555150142610"></a>
    <table><thead align="left"><tr id="row655175018260"><th class="cellrowborder" valign="top" width="19.55%" id="mcps1.1.5.1.1"><p id="p15515017263"><a name="p15515017263"></a><a name="p15515017263"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.26%" id="mcps1.1.5.1.2"><p id="p855125092614"><a name="p855125092614"></a><a name="p855125092614"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.32%" id="mcps1.1.5.1.3"><p id="p655850112611"><a name="p655850112611"></a><a name="p655850112611"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.870000000000005%" id="mcps1.1.5.1.4"><p id="p75525022619"><a name="p75525022619"></a><a name="p75525022619"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7551050132618"><td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.5.1.1 "><p id="p1855165082620"><a name="p1855165082620"></a><a name="p1855165082620"></a>access_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.26%" headers="mcps1.1.5.1.2 "><p id="p15551550192613"><a name="p15551550192613"></a><a name="p15551550192613"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.3 "><p id="p125585032619"><a name="p125585032619"></a><a name="p125585032619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.870000000000005%" headers="mcps1.1.5.1.4 "><p id="p255350192610"><a name="p255350192610"></a><a name="p255350192610"></a>Specifies the UUID of the share access rule of the shared file system. The value contains 1 to 36 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "os-deny_access": {
            "access_id": "418e3cf4-08c3-4ed2-a29a-ceffa346b3b8"
        }
    }
    ```


## Response<a name="s21a46342638f4cacb04ad589d49cf060"></a>

-   Parameter description

None

-   Example response

    None


## Status Codes<a name="sa0baa7bed4bd4ba08b6422614b2d2a8c"></a>

-   Normal

    202

-   Abnormal

    <a name="en-us_topic_0064390799_table60792949"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390799_row42658596"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0064390799_p32794215"><a name="en-us_topic_0064390799_p32794215"></a><a name="en-us_topic_0064390799_p32794215"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0064390799_p39085796"><a name="en-us_topic_0064390799_p39085796"></a><a name="en-us_topic_0064390799_p39085796"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390799_row11832897"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p18940582"><a name="en-us_topic_0064390799_p18940582"></a><a name="en-us_topic_0064390799_p18940582"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p57792188"><a name="en-us_topic_0064390799_p57792188"></a><a name="en-us_topic_0064390799_p57792188"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row50367649"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p53247746"><a name="en-us_topic_0064390799_p53247746"></a><a name="en-us_topic_0064390799_p53247746"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p18100201"><a name="en-us_topic_0064390799_p18100201"></a><a name="en-us_topic_0064390799_p18100201"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row28684081"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p41709209"><a name="en-us_topic_0064390799_p41709209"></a><a name="en-us_topic_0064390799_p41709209"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p23002745"><a name="en-us_topic_0064390799_p23002745"></a><a name="en-us_topic_0064390799_p23002745"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row5698118"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p58894414"><a name="en-us_topic_0064390799_p58894414"></a><a name="en-us_topic_0064390799_p58894414"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p5718243"><a name="en-us_topic_0064390799_p5718243"></a><a name="en-us_topic_0064390799_p5718243"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row51464189"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p7849808"><a name="en-us_topic_0064390799_p7849808"></a><a name="en-us_topic_0064390799_p7849808"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p31854691"><a name="en-us_topic_0064390799_p31854691"></a><a name="en-us_topic_0064390799_p31854691"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row18256764"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p2402898"><a name="en-us_topic_0064390799_p2402898"></a><a name="en-us_topic_0064390799_p2402898"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p60417086"><a name="en-us_topic_0064390799_p60417086"></a><a name="en-us_topic_0064390799_p60417086"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row6882862"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p20640979"><a name="en-us_topic_0064390799_p20640979"></a><a name="en-us_topic_0064390799_p20640979"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p61306625"><a name="en-us_topic_0064390799_p61306625"></a><a name="en-us_topic_0064390799_p61306625"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row14888714"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p65135191"><a name="en-us_topic_0064390799_p65135191"></a><a name="en-us_topic_0064390799_p65135191"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p41459137"><a name="en-us_topic_0064390799_p41459137"></a><a name="en-us_topic_0064390799_p41459137"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row37587916"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p24722347"><a name="en-us_topic_0064390799_p24722347"></a><a name="en-us_topic_0064390799_p24722347"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p56353115"><a name="en-us_topic_0064390799_p56353115"></a><a name="en-us_topic_0064390799_p56353115"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row37415993"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p10796581"><a name="en-us_topic_0064390799_p10796581"></a><a name="en-us_topic_0064390799_p10796581"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p2107829"><a name="en-us_topic_0064390799_p2107829"></a><a name="en-us_topic_0064390799_p2107829"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row18970462"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p60212448"><a name="en-us_topic_0064390799_p60212448"></a><a name="en-us_topic_0064390799_p60212448"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p45370106"><a name="en-us_topic_0064390799_p45370106"></a><a name="en-us_topic_0064390799_p45370106"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row5677776"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p57246722"><a name="en-us_topic_0064390799_p57246722"></a><a name="en-us_topic_0064390799_p57246722"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p6472929"><a name="en-us_topic_0064390799_p6472929"></a><a name="en-us_topic_0064390799_p6472929"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row58256364"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p21145081"><a name="en-us_topic_0064390799_p21145081"></a><a name="en-us_topic_0064390799_p21145081"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p35029990"><a name="en-us_topic_0064390799_p35029990"></a><a name="en-us_topic_0064390799_p35029990"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390799_row46834456"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390799_p35494585"><a name="en-us_topic_0064390799_p35494585"></a><a name="en-us_topic_0064390799_p35494585"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390799_p56489102"><a name="en-us_topic_0064390799_p56489102"></a><a name="en-us_topic_0064390799_p56489102"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


