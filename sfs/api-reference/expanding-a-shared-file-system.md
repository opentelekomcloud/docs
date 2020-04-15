# Expanding a Shared File System<a name="sfs_02_0034"></a>

## Function<a name="s4f6c8c4d908b42c684eb84e837062288"></a>

This API is used to expand the capacity of a shared file system.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API is an asynchronous API. If the returned status code is  **202**, the API request is successfully delivered and received. Later, you can refer to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether the shared file system is expanded successfully.  

## URI<a name="sd7de213608b64be19fc069d3ed492035"></a>

-   POST /v2/\{project\_id\}/shares/\{share\_id\}/action
-   Parameter description

    <a name="en-us_topic_0076901182_table45001781"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901182_row42052973"><th class="cellrowborder" valign="top" width="18.96%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.489999999999998%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.93%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.62%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901182_row33631540"><td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.1 "><p id="aedfbfdb579c44e8999a6b19f0c120f21"><a name="aedfbfdb579c44e8999a6b19f0c120f21"></a><a name="aedfbfdb579c44e8999a6b19f0c120f21"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.5.1.2 "><p id="a3121e3e565c84c5c9a278230940473b8"><a name="a3121e3e565c84c5c9a278230940473b8"></a><a name="a3121e3e565c84c5c9a278230940473b8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.93%" headers="mcps1.1.5.1.3 "><p id="ab2a72bed03004193a29602dddc423715"><a name="ab2a72bed03004193a29602dddc423715"></a><a name="ab2a72bed03004193a29602dddc423715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.62%" headers="mcps1.1.5.1.4 "><p id="a4dc199fc384e446b91b4c696aba10de2"><a name="a4dc199fc384e446b91b4c696aba10de2"></a><a name="a4dc199fc384e446b91b4c696aba10de2"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row52334961"><td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.1 "><p id="a13d92d0f99b64184bf787c5aaaf08e68"><a name="a13d92d0f99b64184bf787c5aaaf08e68"></a><a name="a13d92d0f99b64184bf787c5aaaf08e68"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.5.1.2 "><p id="addb93471cf8f4e28868bab4ff0e872c1"><a name="addb93471cf8f4e28868bab4ff0e872c1"></a><a name="addb93471cf8f4e28868bab4ff0e872c1"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.93%" headers="mcps1.1.5.1.3 "><p id="a582ca5c66a514507a75aca16841d8b47"><a name="a582ca5c66a514507a75aca16841d8b47"></a><a name="a582ca5c66a514507a75aca16841d8b47"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.62%" headers="mcps1.1.5.1.4 "><p id="abfe5b79c46fc49e8a0a9562a7a4ee510"><a name="abfe5b79c46fc49e8a0a9562a7a4ee510"></a><a name="abfe5b79c46fc49e8a0a9562a7a4ee510"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s3a7db8387fb7411d8cd846a82e921b21"></a>

-   Parameter description

    <a name="td1edbbef558c45dc93c04a19b4d19c95"></a>
    <table><thead align="left"><tr id="r6316f3ede17f448b8d59d8f206e4cb2d"><th class="cellrowborder" valign="top" width="19.041904190419043%" id="mcps1.1.5.1.1"><p id="p131881436162417"><a name="p131881436162417"></a><a name="p131881436162417"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.491349134913492%" id="mcps1.1.5.1.2"><p id="p191881736142411"><a name="p191881736142411"></a><a name="p191881736142411"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.992199219921993%" id="mcps1.1.5.1.3"><p id="p720210367248"><a name="p720210367248"></a><a name="p720210367248"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.474547454745476%" id="mcps1.1.5.1.4"><p id="p520212367242"><a name="p520212367242"></a><a name="p520212367242"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r66d0739dd8074f8fb9f374eb544d4975"><td class="cellrowborder" valign="top" width="19.041904190419043%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0076901182_p558669416566"><a name="en-us_topic_0076901182_p558669416566"></a><a name="en-us_topic_0076901182_p558669416566"></a>os-extend</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.491349134913492%" headers="mcps1.1.5.1.2 "><p id="aa732e4db77d047edb2a11e0c9849eef9"><a name="aa732e4db77d047edb2a11e0c9849eef9"></a><a name="aa732e4db77d047edb2a11e0c9849eef9"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.992199219921993%" headers="mcps1.1.5.1.3 "><p id="a98e384c67a554123a24dda987cef6c10"><a name="a98e384c67a554123a24dda987cef6c10"></a><a name="a98e384c67a554123a24dda987cef6c10"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.474547454745476%" headers="mcps1.1.5.1.4 "><p id="a58584a8208054f19b1d8b19d5d1d998a"><a name="a58584a8208054f19b1d8b19d5d1d998a"></a><a name="a58584a8208054f19b1d8b19d5d1d998a"></a>Specifies the <strong id="a830cecef16ad4e0aaccf32b92495055d"><a name="a830cecef16ad4e0aaccf32b92495055d"></a><a name="a830cecef16ad4e0aaccf32b92495055d"></a>os-extend</strong> object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **os-extend**

    <a name="t5f52f8ee95e042c999e4c980a32639ca"></a>
    <table><thead align="left"><tr id="r927230140bfd4f158c1e71fdd1175ac8"><th class="cellrowborder" valign="top" width="19.09190919091909%" id="mcps1.1.5.1.1"><p id="p471810438242"><a name="p471810438242"></a><a name="p471810438242"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.611361136113612%" id="mcps1.1.5.1.2"><p id="p1971864317241"><a name="p1971864317241"></a><a name="p1971864317241"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.802180218021803%" id="mcps1.1.5.1.3"><p id="p13718114314248"><a name="p13718114314248"></a><a name="p13718114314248"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.4945494549455%" id="mcps1.1.5.1.4"><p id="p1971810432247"><a name="p1971810432247"></a><a name="p1971810432247"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rc028b30fffb54c19a3beb3b6076a1c22"><td class="cellrowborder" valign="top" width="19.09190919091909%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0076901182_p175453116566"><a name="en-us_topic_0076901182_p175453116566"></a><a name="en-us_topic_0076901182_p175453116566"></a>new_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.611361136113612%" headers="mcps1.1.5.1.2 "><p id="a21f0e930a19543bbbf58337ee63c2b51"><a name="a21f0e930a19543bbbf58337ee63c2b51"></a><a name="a21f0e930a19543bbbf58337ee63c2b51"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.1.5.1.3 "><p id="ac05b15b7a921463a8b6bb53b8a087420"><a name="ac05b15b7a921463a8b6bb53b8a087420"></a><a name="ac05b15b7a921463a8b6bb53b8a087420"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.4945494549455%" headers="mcps1.1.5.1.4 "><p id="a08a732f87cea4d28b8931eb0b3621bc9"><a name="a08a732f87cea4d28b8931eb0b3621bc9"></a><a name="a08a732f87cea4d28b8931eb0b3621bc9"></a>Specifies the post-expansion capacity (GB) of the shared file system.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "os-extend": {
            "new_size": 2
        }
    }
    ```


## Response<a name="s8703d904c5b7413188ce12352326a73e"></a>

-   Parameter description

    None


-   Example response

    None


## Status Codes<a name="s7194f469973442a09f40e4760eb0a747"></a>

-   Normal

    202

-   Abnormal

    <a name="en-us_topic_0076901182_table24991814"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901182_row17706563"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0076901182_p24945537"><a name="en-us_topic_0076901182_p24945537"></a><a name="en-us_topic_0076901182_p24945537"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0076901182_p7322627"><a name="en-us_topic_0076901182_p7322627"></a><a name="en-us_topic_0076901182_p7322627"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901182_row56261938"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p60923125"><a name="en-us_topic_0076901182_p60923125"></a><a name="en-us_topic_0076901182_p60923125"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p35826101"><a name="en-us_topic_0076901182_p35826101"></a><a name="en-us_topic_0076901182_p35826101"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="r6a88088baf7c4c158aa8a4c6bccf7c34"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p534990621322"><a name="en-us_topic_0076901182_p534990621322"></a><a name="en-us_topic_0076901182_p534990621322"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a831eaa0025e24bd6884fed2bb2a5df4f"><a name="a831eaa0025e24bd6884fed2bb2a5df4f"></a><a name="a831eaa0025e24bd6884fed2bb2a5df4f"></a>Invalid input: The post-deduction capacity must be larger than 0 and smaller than the current capacity. (Current capacity: <em id="i1442372620142837"><a name="i1442372620142837"></a><a name="i1442372620142837"></a>XX</em>; post-deduction capacity: <em id="i1852505181142837"><a name="i1852505181142837"></a><a name="i1852505181142837"></a>XX</em>)</p>
    </td>
    </tr>
    <tr id="r4bc3f27fc2384de9ade4c5976682e08d"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a59b5a7ea71554a679c1147c64cbbf34a"><a name="a59b5a7ea71554a679c1147c64cbbf34a"></a><a name="a59b5a7ea71554a679c1147c64cbbf34a"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ae6d27ab5da85456aa12088fd4e2afe71"><a name="ae6d27ab5da85456aa12088fd4e2afe71"></a><a name="ae6d27ab5da85456aa12088fd4e2afe71"></a>Invalid input: The post-expansion capacity must be larger than the current capacity. (Current capacity: <em id="i167922714514297"><a name="i167922714514297"></a><a name="i167922714514297"></a>XX</em>; post-expansion capacity: <em id="i66903648114297"><a name="i66903648114297"></a><a name="i66903648114297"></a>XX</em>)</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row53999455"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p11879716"><a name="en-us_topic_0076901182_p11879716"></a><a name="en-us_topic_0076901182_p11879716"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p22732954"><a name="en-us_topic_0076901182_p22732954"></a><a name="en-us_topic_0076901182_p22732954"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row3269999"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p63543344"><a name="en-us_topic_0076901182_p63543344"></a><a name="en-us_topic_0076901182_p63543344"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p46737271"><a name="en-us_topic_0076901182_p46737271"></a><a name="en-us_topic_0076901182_p46737271"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row17982255"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p47276535"><a name="en-us_topic_0076901182_p47276535"></a><a name="en-us_topic_0076901182_p47276535"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p4194103"><a name="en-us_topic_0076901182_p4194103"></a><a name="en-us_topic_0076901182_p4194103"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row37746932"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p37602652"><a name="en-us_topic_0076901182_p37602652"></a><a name="en-us_topic_0076901182_p37602652"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p25915985"><a name="en-us_topic_0076901182_p25915985"></a><a name="en-us_topic_0076901182_p25915985"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row31917275"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p35162510"><a name="en-us_topic_0076901182_p35162510"></a><a name="en-us_topic_0076901182_p35162510"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p29591041"><a name="en-us_topic_0076901182_p29591041"></a><a name="en-us_topic_0076901182_p29591041"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row64992778"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p29923648"><a name="en-us_topic_0076901182_p29923648"></a><a name="en-us_topic_0076901182_p29923648"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p7896460"><a name="en-us_topic_0076901182_p7896460"></a><a name="en-us_topic_0076901182_p7896460"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row3959276"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p52265969"><a name="en-us_topic_0076901182_p52265969"></a><a name="en-us_topic_0076901182_p52265969"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p5685119"><a name="en-us_topic_0076901182_p5685119"></a><a name="en-us_topic_0076901182_p5685119"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row51166072"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p50811173"><a name="en-us_topic_0076901182_p50811173"></a><a name="en-us_topic_0076901182_p50811173"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p22064367"><a name="en-us_topic_0076901182_p22064367"></a><a name="en-us_topic_0076901182_p22064367"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row64361578"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p45905321"><a name="en-us_topic_0076901182_p45905321"></a><a name="en-us_topic_0076901182_p45905321"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p27343545"><a name="en-us_topic_0076901182_p27343545"></a><a name="en-us_topic_0076901182_p27343545"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row44765319"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p2112211"><a name="en-us_topic_0076901182_p2112211"></a><a name="en-us_topic_0076901182_p2112211"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p36871363"><a name="en-us_topic_0076901182_p36871363"></a><a name="en-us_topic_0076901182_p36871363"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row63406812"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p35678142"><a name="en-us_topic_0076901182_p35678142"></a><a name="en-us_topic_0076901182_p35678142"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p4248376"><a name="en-us_topic_0076901182_p4248376"></a><a name="en-us_topic_0076901182_p4248376"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row38235390"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p10058896"><a name="en-us_topic_0076901182_p10058896"></a><a name="en-us_topic_0076901182_p10058896"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p9464271"><a name="en-us_topic_0076901182_p9464271"></a><a name="en-us_topic_0076901182_p9464271"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901182_row18069578"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901182_p54349751"><a name="en-us_topic_0076901182_p54349751"></a><a name="en-us_topic_0076901182_p54349751"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901182_p40253700"><a name="en-us_topic_0076901182_p40253700"></a><a name="en-us_topic_0076901182_p40253700"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


