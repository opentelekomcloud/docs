# Shrinking a Shared File System<a name="sfs_02_0035"></a>

## Function<a name="s33bdca688810484fbd276da8f2b74e1f"></a>

This API is used to shrink the capacity of a shared file system.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API is an asynchronous API. If the returned status code is  **202**, the API request is successfully delivered and received. Later, you can refer to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether the shared file system is shrunk successfully.  

## URI<a name="s296c37d90ca2445280a080298971565a"></a>

-   POST /v2/\{project\_id\}/shares/\{share\_id\}/action
-   Parameter description

    <a name="en-us_topic_0076901183_table45911036"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901183_row36188385"><th class="cellrowborder" valign="top" width="14.799999999999999%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.73%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.88%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.59%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901183_row33273344"><td class="cellrowborder" valign="top" width="14.799999999999999%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0076901183_p642732921719"><a name="en-us_topic_0076901183_p642732921719"></a><a name="en-us_topic_0076901183_p642732921719"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.1.5.1.2 "><p id="a9ec20f066b3544f58d94c3e9748815a6"><a name="a9ec20f066b3544f58d94c3e9748815a6"></a><a name="a9ec20f066b3544f58d94c3e9748815a6"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.1.5.1.3 "><p id="a5f88253ef9744bfcbf324e9e4c9ffa30"><a name="a5f88253ef9744bfcbf324e9e4c9ffa30"></a><a name="a5f88253ef9744bfcbf324e9e4c9ffa30"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.1.5.1.4 "><p id="a1311aca9574a46989c203ecbc3aadd10"><a name="a1311aca9574a46989c203ecbc3aadd10"></a><a name="a1311aca9574a46989c203ecbc3aadd10"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row60643168"><td class="cellrowborder" valign="top" width="14.799999999999999%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0076901183_p502797541719"><a name="en-us_topic_0076901183_p502797541719"></a><a name="en-us_topic_0076901183_p502797541719"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.1.5.1.2 "><p id="aab705787a2274508a09104ba59cb5901"><a name="aab705787a2274508a09104ba59cb5901"></a><a name="aab705787a2274508a09104ba59cb5901"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.1.5.1.3 "><p id="ac30571b6991542e5934d578a18801382"><a name="ac30571b6991542e5934d578a18801382"></a><a name="ac30571b6991542e5934d578a18801382"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.1.5.1.4 "><p id="a06f18709bc764f818dedfef3939d8c11"><a name="a06f18709bc764f818dedfef3939d8c11"></a><a name="a06f18709bc764f818dedfef3939d8c11"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sda74a7c5f3a04e60afb288b1d8944df3"></a>

-   Parameter description

    <a name="en-us_topic_0076901183_table64295127"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901183_row64026895"><th class="cellrowborder" valign="top" width="14.71%" id="mcps1.1.5.1.1"><p id="p1939171172517"><a name="p1939171172517"></a><a name="p1939171172517"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13%" id="mcps1.1.5.1.2"><p id="p10391181122515"><a name="p10391181122515"></a><a name="p10391181122515"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.73%" id="mcps1.1.5.1.3"><p id="p739151172513"><a name="p739151172513"></a><a name="p739151172513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.43%" id="mcps1.1.5.1.4"><p id="p9391121117255"><a name="p9391121117255"></a><a name="p9391121117255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901183_row39641102"><td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0076901183_p56812682"><a name="en-us_topic_0076901183_p56812682"></a><a name="en-us_topic_0076901183_p56812682"></a>os-shrink</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.1.5.1.2 "><p id="a306f65b61c814e3cad969c311ae42bc1"><a name="a306f65b61c814e3cad969c311ae42bc1"></a><a name="a306f65b61c814e3cad969c311ae42bc1"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.1.5.1.3 "><p id="a15e2f47dfa30434ab4553c8c6916b4b7"><a name="a15e2f47dfa30434ab4553c8c6916b4b7"></a><a name="a15e2f47dfa30434ab4553c8c6916b4b7"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.43%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0076901183_p44136375"><a name="en-us_topic_0076901183_p44136375"></a><a name="en-us_topic_0076901183_p44136375"></a>Specifies the <strong id="a0dc9ad946c254e56beae3a1006a25749"><a name="a0dc9ad946c254e56beae3a1006a25749"></a><a name="a0dc9ad946c254e56beae3a1006a25749"></a>os-shrink</strong> object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **os-shrink**

    <a name="en-us_topic_0076901183_table18276642"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901183_row4957353"><th class="cellrowborder" valign="top" width="14.23%" id="mcps1.1.5.1.1"><p id="p1996851472518"><a name="p1996851472518"></a><a name="p1996851472518"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.669999999999998%" id="mcps1.1.5.1.2"><p id="p496871418257"><a name="p496871418257"></a><a name="p496871418257"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.1.5.1.3"><p id="p12968714102512"><a name="p12968714102512"></a><a name="p12968714102512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.55%" id="mcps1.1.5.1.4"><p id="p1296819149257"><a name="p1296819149257"></a><a name="p1296819149257"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901183_row8849323"><td class="cellrowborder" valign="top" width="14.23%" headers="mcps1.1.5.1.1 "><p id="a004f5fed487d42468a2d8a0168fb29cb"><a name="a004f5fed487d42468a2d8a0168fb29cb"></a><a name="a004f5fed487d42468a2d8a0168fb29cb"></a>new_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.669999999999998%" headers="mcps1.1.5.1.2 "><p id="a56d7fffc1ee64c20a0da617bcc9b01e7"><a name="a56d7fffc1ee64c20a0da617bcc9b01e7"></a><a name="a56d7fffc1ee64c20a0da617bcc9b01e7"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.5.1.3 "><p id="a775819df804f4f70b6e19a2168d6bb29"><a name="a775819df804f4f70b6e19a2168d6bb29"></a><a name="a775819df804f4f70b6e19a2168d6bb29"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.1.5.1.4 "><p id="a7446186d1e584e739f3756fe4839ce93"><a name="a7446186d1e584e739f3756fe4839ce93"></a><a name="a7446186d1e584e739f3756fe4839ce93"></a>Specifies the post-shrinking capacity (GB) of the shared file system.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "os-shrink": {
            "new_size": 1
        }
    }
    ```


## Response<a name="sc7abb610536242c4b1c4b3c9bc3a698b"></a>

-   Parameter description

    None


-   Example response

    None


## Status Codes<a name="sf0c6d6a79e744278acab17a058623890"></a>

-   Normal

    202

-   Abnormal

    <a name="en-us_topic_0076901183_table59073500"></a>
    <table><thead align="left"><tr id="en-us_topic_0076901183_row46587076"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0076901183_p15456783"><a name="en-us_topic_0076901183_p15456783"></a><a name="en-us_topic_0076901183_p15456783"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0076901183_p44039915"><a name="en-us_topic_0076901183_p44039915"></a><a name="en-us_topic_0076901183_p44039915"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0076901183_row10463359"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p42225780"><a name="en-us_topic_0076901183_p42225780"></a><a name="en-us_topic_0076901183_p42225780"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p64845042"><a name="en-us_topic_0076901183_p64845042"></a><a name="en-us_topic_0076901183_p64845042"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row46734467"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p27395488"><a name="en-us_topic_0076901183_p27395488"></a><a name="en-us_topic_0076901183_p27395488"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p4442074"><a name="en-us_topic_0076901183_p4442074"></a><a name="en-us_topic_0076901183_p4442074"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row39978669"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p17046748"><a name="en-us_topic_0076901183_p17046748"></a><a name="en-us_topic_0076901183_p17046748"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p38609372"><a name="en-us_topic_0076901183_p38609372"></a><a name="en-us_topic_0076901183_p38609372"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row11940034"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p27618686"><a name="en-us_topic_0076901183_p27618686"></a><a name="en-us_topic_0076901183_p27618686"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p22521054"><a name="en-us_topic_0076901183_p22521054"></a><a name="en-us_topic_0076901183_p22521054"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row1362895"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p43285665"><a name="en-us_topic_0076901183_p43285665"></a><a name="en-us_topic_0076901183_p43285665"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p16477963"><a name="en-us_topic_0076901183_p16477963"></a><a name="en-us_topic_0076901183_p16477963"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row14083945"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p67057771"><a name="en-us_topic_0076901183_p67057771"></a><a name="en-us_topic_0076901183_p67057771"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p62970394"><a name="en-us_topic_0076901183_p62970394"></a><a name="en-us_topic_0076901183_p62970394"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row29862637"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p2954570"><a name="en-us_topic_0076901183_p2954570"></a><a name="en-us_topic_0076901183_p2954570"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p37993607"><a name="en-us_topic_0076901183_p37993607"></a><a name="en-us_topic_0076901183_p37993607"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row6398145"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p48487730"><a name="en-us_topic_0076901183_p48487730"></a><a name="en-us_topic_0076901183_p48487730"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p35192023"><a name="en-us_topic_0076901183_p35192023"></a><a name="en-us_topic_0076901183_p35192023"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row48292752"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p19398879"><a name="en-us_topic_0076901183_p19398879"></a><a name="en-us_topic_0076901183_p19398879"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p27805399"><a name="en-us_topic_0076901183_p27805399"></a><a name="en-us_topic_0076901183_p27805399"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row48922001"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p3259160"><a name="en-us_topic_0076901183_p3259160"></a><a name="en-us_topic_0076901183_p3259160"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p62665436"><a name="en-us_topic_0076901183_p62665436"></a><a name="en-us_topic_0076901183_p62665436"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row27118016"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p49075689"><a name="en-us_topic_0076901183_p49075689"></a><a name="en-us_topic_0076901183_p49075689"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p15707907"><a name="en-us_topic_0076901183_p15707907"></a><a name="en-us_topic_0076901183_p15707907"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row7153442"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p42557928"><a name="en-us_topic_0076901183_p42557928"></a><a name="en-us_topic_0076901183_p42557928"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p24640114"><a name="en-us_topic_0076901183_p24640114"></a><a name="en-us_topic_0076901183_p24640114"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row20434436"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p44576624"><a name="en-us_topic_0076901183_p44576624"></a><a name="en-us_topic_0076901183_p44576624"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p53936788"><a name="en-us_topic_0076901183_p53936788"></a><a name="en-us_topic_0076901183_p53936788"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0076901183_row15669051"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0076901183_p61233639"><a name="en-us_topic_0076901183_p61233639"></a><a name="en-us_topic_0076901183_p61233639"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0076901183_p60977760"><a name="en-us_topic_0076901183_p60977760"></a><a name="en-us_topic_0076901183_p60977760"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


