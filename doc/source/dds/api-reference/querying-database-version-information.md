# Querying Database Version Information<a name="dds_database_version"></a>

## Function<a name="section61759636"></a>

This API is used to obtain database version information about a specified type of a DB instance.

## URI<a name="section18965813"></a>

-   URI format

    GET /v3/\{project\_id\}/datastores/\{datastore\_name\}/versions

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.689999999999998%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b18901131134212"><a name="b18901131134212"></a><a name="b18901131134212"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.689999999999998%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p1434580163733"><a name="p1434580163733"></a><a name="p1434580163733"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row5992637"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.689999999999998%" headers="mcps1.2.4.1.2 "><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p5562520192718"><a name="p5562520192718"></a><a name="p5562520192718"></a>Specifies the database type. DDS Community Edition is supported. The value is <strong id="b42993511538"><a name="b42993511538"></a><a name="b42993511538"></a>DDS-Community</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="section36474591"></a>

-   Request header

    ```
    GET https://DDS endpoint/v3/{project_id}/datastores/{datastore_name}/versions
    ```

-   Request body

    N/A


## Responses<a name="section59835867"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table66531170"></a>
    <table><thead align="left"><tr id="row12984378"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a><strong id="b37981314144218"><a name="b37981314144218"></a><a name="b37981314144218"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5801050"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p123050"><a name="p123050"></a><a name="p123050"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1299616431919"><a name="p1299616431919"></a><a name="p1299616431919"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39568472259"><a name="p39568472259"></a><a name="p39568472259"></a>Specifies the database version. Currently, versions 3.2 and 3.4 are supported.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "versions": [
            "3.2",
            "3.4"
        ]
    }
    ```


## **Status Code**<a name="section5382712154838"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

