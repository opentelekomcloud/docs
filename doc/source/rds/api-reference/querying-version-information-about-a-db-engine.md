# Querying Version Information About a DB Engine<a name="rds_06_0001"></a>

## Function<a name="section61759636"></a>

This API is used to query the database version information of a specified DB engine.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section18965813"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{_project\_id_\}/datastores/\{_database\_name_\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/619d3e78f61b4be68bc5aa0b59edcf7b/datastores/mysql

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b1712611151775"><a name="b1712611151775"></a><a name="b1712611151775"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1434580163733"><a name="p1434580163733"></a><a name="p1434580163733"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p149071611472"><a name="p149071611472"></a><a name="p149071611472"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row5992637"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>database_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p26952636163519"><a name="p26952636163519"></a><a name="p26952636163519"></a>Specifies the DB engine. Its value can be any of the following and is case-insensitive:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36474591"></a>

None

## Response<a name="section59835867"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b10677139151116"><a name="b10677139151116"></a><a name="b10677139151116"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.62376237623762%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b650871261115"><a name="b650871261115"></a><a name="b650871261115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2456979"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.4.1.1 "><p id="p64797609"><a name="p64797609"></a><a name="p64797609"></a>dataStores</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.62376237623762%" headers="mcps1.2.4.1.2 "><p id="a9a9492e05cb648e885d1e747a339d04d"><a name="a9a9492e05cb648e885d1e747a339d04d"></a><a name="a9a9492e05cb648e885d1e747a339d04d"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.3 "><p id="p22140377"><a name="p22140377"></a><a name="p22140377"></a>Indicates the list of database versions.</p>
    <p id="p1573113732216"><a name="p1573113732216"></a><a name="p1573113732216"></a>For details, see <a href="#table66531170">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  dataStores field data structure description

    <a name="table66531170"></a>
    <table><thead align="left"><tr id="row12984378"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a><strong id="b954223110115"><a name="b954223110115"></a><a name="b954223110115"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38%" id="mcps1.2.4.1.2"><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a><strong id="b547253261112"><a name="b547253261112"></a><a name="b547253261112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a><strong id="b203161339113"><a name="b203161339113"></a><a name="b203161339113"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4719792"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p46758891"><a name="p46758891"></a><a name="p46758891"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.4.1.2 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p30470722"><a name="p30470722"></a><a name="p30470722"></a>Indicates the database version ID. Its value is unique.</p>
    </td>
    </tr>
    <tr id="row5801050"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p123050"><a name="p123050"></a><a name="p123050"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.4.1.2 "><p id="p9967070"><a name="p9967070"></a><a name="p9967070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p2026335"><a name="p2026335"></a><a name="p2026335"></a>Indicates the database version number. Only the major version number (two digits) is returned. For example, if the version number is MySQL 5.6.X, only 5.6 is returned.</p>
    <p id="p153851450162214"><a name="p153851450162214"></a><a name="p153851450162214"></a></p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"dataStores": [{
    		"id": "87620726-6802-46c0-9028-a8785e1f1922",
    		"name": "5.7"
    	}, {
    		"id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a62",
    		"name": "5.6"
    	}]
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

