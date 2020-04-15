# Modifying a Health Check<a name="EN-US_TOPIC_0096561514"></a>

## Function<a name="en-us_topic_0020100166_section51200735"></a>

This API is used to modify information about a health check.

## URI<a name="en-us_topic_0020100166_section58153438"></a>

PUT /v1.0/\{project\_id\}/elbaas/healthcheck/\{healthcheck\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100166_table2350413"></a>
<table><thead align="left"><tr id="en-us_topic_0020100166_row8575450"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100166_p23522831"><a name="en-us_topic_0020100166_p23522831"></a><a name="en-us_topic_0020100166_p23522831"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100166_p26301173"><a name="en-us_topic_0020100166_p26301173"></a><a name="en-us_topic_0020100166_p26301173"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100166_p3742928817648"><a name="en-us_topic_0020100166_p3742928817648"></a><a name="en-us_topic_0020100166_p3742928817648"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100166_p50020275"><a name="en-us_topic_0020100166_p50020275"></a><a name="en-us_topic_0020100166_p50020275"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100166_row27884521115341"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1592975916416"><a name="p1592975916416"></a><a name="p1592975916416"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p16448891115356"><a name="en-us_topic_0020100166_p16448891115356"></a><a name="en-us_topic_0020100166_p16448891115356"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p6430409411540"><a name="en-us_topic_0020100166_p6430409411540"></a><a name="en-us_topic_0020100166_p6430409411540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100166_p3428698711542"><a name="en-us_topic_0020100166_p3428698711542"></a><a name="en-us_topic_0020100166_p3428698711542"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100166_row25110514"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p20685786"><a name="en-us_topic_0020100166_p20685786"></a><a name="en-us_topic_0020100166_p20685786"></a>healthcheck_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p64935954"><a name="en-us_topic_0020100166_p64935954"></a><a name="en-us_topic_0020100166_p64935954"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p1187346317648"><a name="en-us_topic_0020100166_p1187346317648"></a><a name="en-us_topic_0020100166_p1187346317648"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100166_p25320898"><a name="en-us_topic_0020100166_p25320898"></a><a name="en-us_topic_0020100166_p25320898"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100166_row26561495"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p3997487"><a name="en-us_topic_0020100166_p3997487"></a><a name="en-us_topic_0020100166_p3997487"></a>healthcheck_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p55361044"><a name="en-us_topic_0020100166_p55361044"></a><a name="en-us_topic_0020100166_p55361044"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p2222643517648"><a name="en-us_topic_0020100166_p2222643517648"></a><a name="en-us_topic_0020100166_p2222643517648"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul5527202192327"></a><a name="en-us_topic_0020100166_ul5527202192327"></a><ul id="en-us_topic_0020100166_ul5527202192327"><li>Specifies the health check protocol.</li><li>The value can be <strong>HTTP</strong> or <strong>TCP</strong> (case-insensitive).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100166_row7322556"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p56256135"><a name="en-us_topic_0020100166_p56256135"></a><a name="en-us_topic_0020100166_p56256135"></a>healthcheck_uri</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p60453091"><a name="en-us_topic_0020100166_p60453091"></a><a name="en-us_topic_0020100166_p60453091"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p5551077117648"><a name="en-us_topic_0020100166_p5551077117648"></a><a name="en-us_topic_0020100166_p5551077117648"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul6131662692338"></a><a name="en-us_topic_0020100166_ul6131662692338"></a><ul id="en-us_topic_0020100166_ul6131662692338"><li>Specifies the health check URI. This parameter is valid when <strong>healthcheck_protocol</strong> is <strong>HTTP</strong>.</li><li>The value is a string of 1 to 80 characters that must start with a slash (/) and can contain only letters, digits, and special characters such as -/.%?#&amp;_=</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100166_row19346796"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p23586666"><a name="en-us_topic_0020100166_p23586666"></a><a name="en-us_topic_0020100166_p23586666"></a>healthcheck_connect_port</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p31471768"><a name="en-us_topic_0020100166_p31471768"></a><a name="en-us_topic_0020100166_p31471768"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p7857517648"><a name="en-us_topic_0020100166_p7857517648"></a><a name="en-us_topic_0020100166_p7857517648"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul2614204492350"></a><a name="en-us_topic_0020100166_ul2614204492350"></a><ul id="en-us_topic_0020100166_ul2614204492350"><li>Specifies the health check port.</li><li>The port number ranges from 1 to 65535.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100166_row64880336"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p20815867"><a name="en-us_topic_0020100166_p20815867"></a><a name="en-us_topic_0020100166_p20815867"></a>healthy_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p8363642"><a name="en-us_topic_0020100166_p8363642"></a><a name="en-us_topic_0020100166_p8363642"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p636464017648"><a name="en-us_topic_0020100166_p636464017648"></a><a name="en-us_topic_0020100166_p636464017648"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul3344333792358"></a><a name="en-us_topic_0020100166_ul3344333792358"></a><ul id="en-us_topic_0020100166_ul3344333792358"><li>Specifies the number of consecutive successful health checks when the health check result of a backend ECS changes from <strong id="b40773523181459"><a name="b40773523181459"></a><a name="b40773523181459"></a>fail</strong> to <strong id="b18360893181459"><a name="b18360893181459"></a><a name="b18360893181459"></a>success</strong>.</li><li>The value ranges from <strong id="b142281511161410"><a name="b142281511161410"></a><a name="b142281511161410"></a>1</strong> to <strong id="b530651515147"><a name="b530651515147"></a><a name="b530651515147"></a>10</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100166_row10586695"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p52215961"><a name="en-us_topic_0020100166_p52215961"></a><a name="en-us_topic_0020100166_p52215961"></a>unhealthy_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p1634435"><a name="en-us_topic_0020100166_p1634435"></a><a name="en-us_topic_0020100166_p1634435"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p4577387017648"><a name="en-us_topic_0020100166_p4577387017648"></a><a name="en-us_topic_0020100166_p4577387017648"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul2320456392445"></a><a name="en-us_topic_0020100166_ul2320456392445"></a><ul id="en-us_topic_0020100166_ul2320456392445"><li>Specifies the number of consecutive failed health checks when the health check result of a backend ECS changes from <strong id="b170814536"><a name="b170814536"></a><a name="b170814536"></a>success</strong> to <strong id="b689513465"><a name="b689513465"></a><a name="b689513465"></a>fail</strong>.</li><li>The value ranges from <strong id="b11362164219509"><a name="b11362164219509"></a><a name="b11362164219509"></a>1</strong> to <strong id="b6185134517508"><a name="b6185134517508"></a><a name="b6185134517508"></a>10</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100166_row9249362"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p11000853"><a name="en-us_topic_0020100166_p11000853"></a><a name="en-us_topic_0020100166_p11000853"></a>healthcheck_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p18653909"><a name="en-us_topic_0020100166_p18653909"></a><a name="en-us_topic_0020100166_p18653909"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p1669600017648"><a name="en-us_topic_0020100166_p1669600017648"></a><a name="en-us_topic_0020100166_p1669600017648"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul2556987292455"></a><a name="en-us_topic_0020100166_ul2556987292455"></a><ul id="en-us_topic_0020100166_ul2556987292455"><li>Specifies the maximum time required for waiting for a response from the health check in the unit of second.</li><li>The value ranges from <strong id="b44101611113716"><a name="b44101611113716"></a><a name="b44101611113716"></a>1</strong> to <strong id="b6771314133717"><a name="b6771314133717"></a><a name="b6771314133717"></a>50</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100166_row36902586"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100166_p36319496"><a name="en-us_topic_0020100166_p36319496"></a><a name="en-us_topic_0020100166_p36319496"></a>healthcheck_interval</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100166_p56198103"><a name="en-us_topic_0020100166_p56198103"></a><a name="en-us_topic_0020100166_p56198103"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100166_p1019878317648"><a name="en-us_topic_0020100166_p1019878317648"></a><a name="en-us_topic_0020100166_p1019878317648"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100166_ul520900839255"></a><a name="en-us_topic_0020100166_ul520900839255"></a><ul id="en-us_topic_0020100166_ul520900839255"><li>Specifies the interval between health checks in the unit of second.</li><li>The value ranges from <strong id="b3439120183719"><a name="b3439120183719"></a><a name="b3439120183719"></a>1</strong> to <strong id="b5978112218376"><a name="b5978112218376"></a><a name="b5978112218376"></a>50</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100166_section53618895"></a>

-   Request parameters

    None


-   Example request

    ```
    {
        "healthcheck_connect_port": 88,
        "healthcheck_interval": 5,
        "healthcheck_protocol": "HTTP",
        "healthcheck_timeout": 10,
        "healthcheck_uri": "/",
        "healthy_threshold": 3,
        "unhealthy_threshold": 2
    }
    ```


## Response<a name="en-us_topic_0020100166_section12808013"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100166_table481316231292"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100166_row375500021292"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100166_p216513511292"><a name="en-us_topic_0020100166_p216513511292"></a><a name="en-us_topic_0020100166_p216513511292"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100166_p89290291292"><a name="en-us_topic_0020100166_p89290291292"></a><a name="en-us_topic_0020100166_p89290291292"></a><strong id="b1845862068"><a name="b1845862068"></a><a name="b1845862068"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.66666666666667%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100166_p521627231292"><a name="en-us_topic_0020100166_p521627231292"></a><a name="en-us_topic_0020100166_p521627231292"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100166_row644310011292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p515285921292"><a name="en-us_topic_0020100166_p515285921292"></a><a name="en-us_topic_0020100166_p515285921292"></a>healthcheck_interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p130664151292"><a name="en-us_topic_0020100166_p130664151292"></a><a name="en-us_topic_0020100166_p130664151292"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p517467191292"><a name="en-us_topic_0020100166_p517467191292"></a><a name="en-us_topic_0020100166_p517467191292"></a>Specifies the interval between health checks in the unit of second.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row630672931292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p81770971292"><a name="en-us_topic_0020100166_p81770971292"></a><a name="en-us_topic_0020100166_p81770971292"></a>listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p583650811292"><a name="en-us_topic_0020100166_p583650811292"></a><a name="en-us_topic_0020100166_p583650811292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p299510931292"><a name="en-us_topic_0020100166_p299510931292"></a><a name="en-us_topic_0020100166_p299510931292"></a>Specifies the ID of the listener with which the health check is associated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row11243881292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p239665901292"><a name="en-us_topic_0020100166_p239665901292"></a><a name="en-us_topic_0020100166_p239665901292"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p622456571292"><a name="en-us_topic_0020100166_p622456571292"></a><a name="en-us_topic_0020100166_p622456571292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p87334691292"><a name="en-us_topic_0020100166_p87334691292"></a><a name="en-us_topic_0020100166_p87334691292"></a>Specifies the health check ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row114923571292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p584657201292"><a name="en-us_topic_0020100166_p584657201292"></a><a name="en-us_topic_0020100166_p584657201292"></a>healthcheck_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p381028881292"><a name="en-us_topic_0020100166_p381028881292"></a><a name="en-us_topic_0020100166_p381028881292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p664350681292"><a name="en-us_topic_0020100166_p664350681292"></a><a name="en-us_topic_0020100166_p664350681292"></a>Specifies the health check protocol.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row610447031292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p456739251292"><a name="en-us_topic_0020100166_p456739251292"></a><a name="en-us_topic_0020100166_p456739251292"></a>unhealthy_threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p86004511292"><a name="en-us_topic_0020100166_p86004511292"></a><a name="en-us_topic_0020100166_p86004511292"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p255479701292"><a name="en-us_topic_0020100166_p255479701292"></a><a name="en-us_topic_0020100166_p255479701292"></a>Specifies the number of consecutive failed health checks when the health check result of a backend ECS changes from <strong id="b1518716509"><a name="b1518716509"></a><a name="b1518716509"></a>success</strong> to <strong id="b160913523"><a name="b160913523"></a><a name="b160913523"></a>fail</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row286051461292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p353154521292"><a name="en-us_topic_0020100166_p353154521292"></a><a name="en-us_topic_0020100166_p353154521292"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p419793791292"><a name="en-us_topic_0020100166_p419793791292"></a><a name="en-us_topic_0020100166_p419793791292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p448865671292"><a name="en-us_topic_0020100166_p448865671292"></a><a name="en-us_topic_0020100166_p448865671292"></a>Specifies the time when the certificate was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row13259231292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p402909401292"><a name="en-us_topic_0020100166_p402909401292"></a><a name="en-us_topic_0020100166_p402909401292"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p423407421292"><a name="en-us_topic_0020100166_p423407421292"></a><a name="en-us_topic_0020100166_p423407421292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p70481051292"><a name="en-us_topic_0020100166_p70481051292"></a><a name="en-us_topic_0020100166_p70481051292"></a>Specifies the time when the health check was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row548289991292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p119639641292"><a name="en-us_topic_0020100166_p119639641292"></a><a name="en-us_topic_0020100166_p119639641292"></a>healthcheck_connect_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p295570501292"><a name="en-us_topic_0020100166_p295570501292"></a><a name="en-us_topic_0020100166_p295570501292"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p453108241292"><a name="en-us_topic_0020100166_p453108241292"></a><a name="en-us_topic_0020100166_p453108241292"></a>Specifies the health check port.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row51442321292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p140296661292"><a name="en-us_topic_0020100166_p140296661292"></a><a name="en-us_topic_0020100166_p140296661292"></a>healthcheck_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p626611521292"><a name="en-us_topic_0020100166_p626611521292"></a><a name="en-us_topic_0020100166_p626611521292"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p423885551292"><a name="en-us_topic_0020100166_p423885551292"></a><a name="en-us_topic_0020100166_p423885551292"></a>Specifies the maximum time required for waiting for a response from the health check in the unit of second.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row459526761292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p311792931292"><a name="en-us_topic_0020100166_p311792931292"></a><a name="en-us_topic_0020100166_p311792931292"></a>healthcheck_uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p424947741292"><a name="en-us_topic_0020100166_p424947741292"></a><a name="en-us_topic_0020100166_p424947741292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p195246311292"><a name="en-us_topic_0020100166_p195246311292"></a><a name="en-us_topic_0020100166_p195246311292"></a>Specifies the health check URI. This parameter is valid when <strong>healthcheck_protocol</strong> is <strong>HTTP</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row415039541292"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100166_p63771391292"><a name="en-us_topic_0020100166_p63771391292"></a><a name="en-us_topic_0020100166_p63771391292"></a>healthy_threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100166_p467862891292"><a name="en-us_topic_0020100166_p467862891292"></a><a name="en-us_topic_0020100166_p467862891292"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100166_p315930751292"><a name="en-us_topic_0020100166_p315930751292"></a><a name="en-us_topic_0020100166_p315930751292"></a>Specifies the threshold at which the health check result is <strong>success</strong>, that is, the number of consecutive successful health checks when the health check result of backend ECSs changes from <strong id="b717963276"><a name="b717963276"></a><a name="b717963276"></a>fail</strong> to <strong id="b1069264708"><a name="b1069264708"></a><a name="b1069264708"></a>success</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "healthcheck_interval": 5,
        "listener_id": "3ce8c4429478a5eb6ef4930de2d75b28",
        "id": "134e5ea962327c6a574b83e6e7f31f35",
        "healthcheck_protocol": "HTTP",
        "unhealthy_threshold": 2,
        "update_time": "2015-12-25 03:57:23",
        "create_time": "2015-12-25 03:57:23",
        "healthcheck_connect_port": 88,
        "healthcheck_timeout": 10,
        "healthcheck_uri": "/",
        "healthy_threshold": 3
    }
    ```


## Status Code<a name="en-us_topic_0020100166_section48163256"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100166_table23314621151543"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100166_row33875729151543"><th class="cellrowborder" valign="top" width="12.13%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100166_p59579522151543"><a name="en-us_topic_0020100166_p59579522151543"></a><a name="en-us_topic_0020100166_p59579522151543"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.63%" id="mcps1.1.4.1.2"><p id="p1245432612141"><a name="p1245432612141"></a><a name="p1245432612141"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100166_p61211943151543"><a name="en-us_topic_0020100166_p61211943151543"></a><a name="en-us_topic_0020100166_p61211943151543"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100166_row59220328151543"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100166_p32117295151543"><a name="en-us_topic_0020100166_p32117295151543"></a><a name="en-us_topic_0020100166_p32117295151543"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p157371241131416"><a name="p157371241131416"></a><a name="p157371241131416"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100166_p51364065151543"><a name="en-us_topic_0020100166_p51364065151543"></a><a name="en-us_topic_0020100166_p51364065151543"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row59623407151543"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100166_p64766639151543"><a name="en-us_topic_0020100166_p64766639151543"></a><a name="en-us_topic_0020100166_p64766639151543"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p1873710413145"><a name="p1873710413145"></a><a name="p1873710413145"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100166_p11606416151543"><a name="en-us_topic_0020100166_p11606416151543"></a><a name="en-us_topic_0020100166_p11606416151543"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row37348884151543"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100166_p5360777151543"><a name="en-us_topic_0020100166_p5360777151543"></a><a name="en-us_topic_0020100166_p5360777151543"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p13737144118142"><a name="p13737144118142"></a><a name="p13737144118142"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100166_p31569778151543"><a name="en-us_topic_0020100166_p31569778151543"></a><a name="en-us_topic_0020100166_p31569778151543"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row15692550151543"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100166_p63137017151543"><a name="en-us_topic_0020100166_p63137017151543"></a><a name="en-us_topic_0020100166_p63137017151543"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p12737194191411"><a name="p12737194191411"></a><a name="p12737194191411"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100166_p13824724151543"><a name="en-us_topic_0020100166_p13824724151543"></a><a name="en-us_topic_0020100166_p13824724151543"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row57313656151543"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100166_p11894596151543"><a name="en-us_topic_0020100166_p11894596151543"></a><a name="en-us_topic_0020100166_p11894596151543"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p187382415140"><a name="p187382415140"></a><a name="p187382415140"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100166_p23938187151543"><a name="en-us_topic_0020100166_p23938187151543"></a><a name="en-us_topic_0020100166_p23938187151543"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100166_row14117097151543"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100166_p2634231151543"><a name="en-us_topic_0020100166_p2634231151543"></a><a name="en-us_topic_0020100166_p2634231151543"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p117381141121419"><a name="p117381141121419"></a><a name="p117381141121419"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100166_p12046133151543"><a name="en-us_topic_0020100166_p12046133151543"></a><a name="en-us_topic_0020100166_p12046133151543"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


