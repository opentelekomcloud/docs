# Configuring the Default Protection Policy for Newly Purchased Public IP Addresses<a name="antiddos_02_0038"></a>

## Functions<a name="section621837"></a>

This API enables you to configure the default protection policy. After a protection policy is configured, it applies to the newly purchased public IP addresses.

## URI<a name="section5596537"></a>

-   URI format

    POST /v1/\{project\_id\}/antiddos/default/config

-   Parameter description

    <a name="table1988636"></a>
    <table><thead align="left"><tr id="row48062879"><th class="cellrowborder" valign="top" width="22.467753224677534%" id="mcps1.1.5.1.1"><p id="p779118"><a name="p779118"></a><a name="p779118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.537946205379463%" id="mcps1.1.5.1.2"><p id="p63108622"><a name="p63108622"></a><a name="p63108622"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.038596140385962%" id="mcps1.1.5.1.3"><p id="p11524775"><a name="p11524775"></a><a name="p11524775"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.955704429557045%" id="mcps1.1.5.1.4"><p id="p61091552"><a name="p61091552"></a><a name="p61091552"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49468641"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.5.1.1 "><p id="p47536979"><a name="p47536979"></a><a name="p47536979"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.537946205379463%" headers="mcps1.1.5.1.2 "><p id="p25290077"><a name="p25290077"></a><a name="p25290077"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.038596140385962%" headers="mcps1.1.5.1.3 "><p id="p35230376"><a name="p35230376"></a><a name="p35230376"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.955704429557045%" headers="mcps1.1.5.1.4 "><p id="p35088220"><a name="p35088220"></a><a name="p35088220"></a>User ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50368838"></a>

-   Parameter description

    <a name="table1660410"></a>
    <table><thead align="left"><tr id="row30785969"><th class="cellrowborder" valign="top" width="30.3%" id="mcps1.1.5.1.1"><p id="p10635570"><a name="p10635570"></a><a name="p10635570"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.98%" id="mcps1.1.5.1.2"><p id="p56174843"><a name="p56174843"></a><a name="p56174843"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.94%" id="mcps1.1.5.1.3"><p id="p53868469"><a name="p53868469"></a><a name="p53868469"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.78%" id="mcps1.1.5.1.4"><p id="p1269896"><a name="p1269896"></a><a name="p1269896"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35752731"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p10290070"><a name="p10290070"></a><a name="p10290070"></a>enable_L7</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p28189346"><a name="p28189346"></a><a name="p28189346"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p1635686"><a name="p1635686"></a><a name="p1635686"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p65381771"><a name="p65381771"></a><a name="p65381771"></a>Whether to enable layer-7 protection.</p>
    </td>
    </tr>
    <tr id="row51565033"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p16018178"><a name="p16018178"></a><a name="p16018178"></a>traffic_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p22404047"><a name="p22404047"></a><a name="p22404047"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p367798481566"><a name="p367798481566"></a><a name="p367798481566"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p24544935"><a name="p24544935"></a><a name="p24544935"></a>Position ID of traffic. The value ranges from 1 to 9 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row19577827"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p42300179"><a name="p42300179"></a><a name="p42300179"></a>http_request_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p3762492"><a name="p3762492"></a><a name="p3762492"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p2257395515612"><a name="p2257395515612"></a><a name="p2257395515612"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p56757654"><a name="p56757654"></a><a name="p56757654"></a>Position ID of number of HTTP requests. The value ranges from 1 to 15 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row41056841"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p37269850"><a name="p37269850"></a><a name="p37269850"></a>cleaning_access_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p66067912"><a name="p66067912"></a><a name="p66067912"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p1659686615617"><a name="p1659686615617"></a><a name="p1659686615617"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p15422169"><a name="p15422169"></a><a name="p15422169"></a>Position ID of access limit during cleaning. The value ranges from 1 to 8 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row4581796"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p35581233"><a name="p35581233"></a><a name="p35581233"></a>app_type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p63507614"><a name="p63507614"></a><a name="p63507614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p4066881915621"><a name="p4066881915621"></a><a name="p4066881915621"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><div class="p" id="p2630238915650"><a name="p2630238915650"></a><a name="p2630238915650"></a>Application type ID. Possible values:<a name="ul2584619815657"></a><a name="ul2584619815657"></a><ul id="ul2584619815657"><li>0</li><li>1</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:** 
    >If values of  **traffic\_pos\_id**,  **http\_request\_pos\_id**,  **cleaning\_access\_pos\_id**  are set between  **33 to 36**, their values must be the same.


-   Request example

    ```
    POST /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/default/config 
    ```

    ```
    {
        "enable_L7":true,
        "traffic_pos_id":1,
        "http_request_pos_id":1,
        "cleaning_access_pos_id":1,
        "app_type_id":1
    }
    ```


## Response<a name="section50666366"></a>

-   Parameter description

    <a name="table10229816"></a>
    <table><thead align="left"><tr id="row54739329"><th class="cellrowborder" valign="top" width="25.490000000000002%" id="mcps1.1.4.1.1"><p id="p4700647"><a name="p4700647"></a><a name="p4700647"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.89%" id="mcps1.1.4.1.2"><p id="p45208163"><a name="p45208163"></a><a name="p45208163"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.62%" id="mcps1.1.4.1.3"><p id="p37982554"><a name="p37982554"></a><a name="p37982554"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56688054"><td class="cellrowborder" valign="top" width="25.490000000000002%" headers="mcps1.1.4.1.1 "><p id="p28329695"><a name="p28329695"></a><a name="p28329695"></a>statusCode</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.89%" headers="mcps1.1.4.1.2 "><p id="p13003964"><a name="p13003964"></a><a name="p13003964"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.62%" headers="mcps1.1.4.1.3 "><p id="p46688182"><a name="p46688182"></a><a name="p46688182"></a>Internal error code</p>
    </td>
    </tr>
    <tr id="row17540457"><td class="cellrowborder" valign="top" width="25.490000000000002%" headers="mcps1.1.4.1.1 "><p id="p11490904"><a name="p11490904"></a><a name="p11490904"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.89%" headers="mcps1.1.4.1.2 "><p id="p58348056"><a name="p58348056"></a><a name="p58348056"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.62%" headers="mcps1.1.4.1.3 "><p id="p28572113"><a name="p28572113"></a><a name="p28572113"></a>Internal error description</p>
    </td>
    </tr>
    <tr id="row55822426"><td class="cellrowborder" valign="top" width="25.490000000000002%" headers="mcps1.1.4.1.1 "><p id="p25322618"><a name="p25322618"></a><a name="p25322618"></a>header</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.89%" headers="mcps1.1.4.1.2 "><p id="p37866150"><a name="p37866150"></a><a name="p37866150"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.62%" headers="mcps1.1.4.1.3 ">&nbsp;&nbsp;</td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "statusCode": 0,
        "body": null,
        "header": null
    }
    ```


## Status Code<a name="section53344112"></a>

For details, see  [Status Code](status-code.md).

