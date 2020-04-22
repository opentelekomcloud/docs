# Querying the Defense Status of a Specified EIP<a name="antiddos_02_0024"></a>

## Function<a name="section35493489"></a>

This API allows you to query the defense status of a specified EIP.

## URI<a name="section51005947"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/\{floating\_ip\_id\}/status

-   Parameter description

    <a name="table43467946"></a>
    <table><thead align="left"><tr id="row29878402"><th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.1"><p id="p4231468"><a name="p4231468"></a><a name="p4231468"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52824717528247%" id="mcps1.1.5.1.2"><p id="p7204610"><a name="p7204610"></a><a name="p7204610"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.617938206179375%" id="mcps1.1.5.1.3"><p id="p46702574"><a name="p46702574"></a><a name="p46702574"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.4"><p id="p24812117"><a name="p24812117"></a><a name="p24812117"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63624481"><td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.1 "><p id="p53309370"><a name="p53309370"></a><a name="p53309370"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52824717528247%" headers="mcps1.1.5.1.2 "><p id="p23091719"><a name="p23091719"></a><a name="p23091719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p58489969"><a name="p58489969"></a><a name="p58489969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p40067039"><a name="p40067039"></a><a name="p40067039"></a>A user's ID</p>
    </td>
    </tr>
    <tr id="row25059035"><td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.1 "><p id="p16515979"><a name="p16515979"></a><a name="p16515979"></a>floating_ip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52824717528247%" headers="mcps1.1.5.1.2 "><p id="p62725940"><a name="p62725940"></a><a name="p62725940"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p47636349"><a name="p47636349"></a><a name="p47636349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p33339022"><a name="p33339022"></a><a name="p33339022"></a>ID corresponding to the EIP of a user</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section56400342"></a>

-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/1df977c2-fdc6-4483-bc1c-ba46829f57b8/status
    ```


## Response<a name="section37841036"></a>

-   Element description

    <a name="table50461073"></a>
    <table><thead align="left"><tr id="row8925963"><th class="cellrowborder" valign="top" width="19.830000000000002%" id="mcps1.1.5.1.1"><p id="p51914417"><a name="p51914417"></a><a name="p51914417"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.369999999999997%" id="mcps1.1.5.1.2"><p id="p44318255"><a name="p44318255"></a><a name="p44318255"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.899999999999999%" id="mcps1.1.5.1.3"><p id="p33008942"><a name="p33008942"></a><a name="p33008942"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.5.1.4"><p id="p56478678"><a name="p56478678"></a><a name="p56478678"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11370190"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p48570174"><a name="p48570174"></a><a name="p48570174"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.369999999999997%" headers="mcps1.1.5.1.2 "><p id="p41870031"><a name="p41870031"></a><a name="p41870031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.899999999999999%" headers="mcps1.1.5.1.3 "><p id="p36029352"><a name="p36029352"></a><a name="p36029352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><div class="p" id="p32696434"><a name="p32696434"></a><a name="p32696434"></a>Defense status, the possible value of which is one of the following:<a name="ul25832457"></a><a name="ul25832457"></a><ul id="ul25832457"><li><span class="parmvalue" id="parmvalue555125744114325"><a name="parmvalue555125744114325"></a><a name="parmvalue555125744114325"></a><b>normal</b></span>: indicates that the defense status is normal.</li><li><span class="parmvalue" id="parmvalue404664094114337"><a name="parmvalue404664094114337"></a><a name="parmvalue404664094114337"></a><b>configging</b></span>: indicates that defense is being configured.</li><li><span class="parmvalue" id="parmvalue600552156114412"><a name="parmvalue600552156114412"></a><a name="parmvalue600552156114412"></a><b>notConfig</b></span>: indicates that defense is not configured.</li><li><span class="parmvalue" id="parmvalue1506354986114925"><a name="parmvalue1506354986114925"></a><a name="parmvalue1506354986114925"></a><b>packetcleaning</b></span>: indicates that traffic cleaning is underway.</li><li><span class="parmvalue" id="parmvalue1400332350143613"><a name="parmvalue1400332350143613"></a><a name="parmvalue1400332350143613"></a><b>packetdropping</b></span>: indicates that traffic is discarded.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {"status": "normal"}
    ```


## Returned Value<a name="section5025004"></a>

See  [Status Code](status-code.md).

