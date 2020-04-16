# Database Version Queries<a name="en-us_topic_0032347782"></a>

## Function<a name="section61759636"></a>

This API is used to obtain version information about a specified type of a database.

## URI<a name="section18965813"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/datastores/\{datastore\_name\}/versions

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328"><a name="b842352706102328"></a><a name="b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.689999999999998%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p43671367163229"><a name="p43671367163229"></a><a name="p43671367163229"></a>Specifies the DB engine. Valid value:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36474591"></a>

None

## Normal Response<a name="section59835867"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b1193848353"><a name="b1193848353"></a><a name="b1193848353"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.339999999999996%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b1543410584"><a name="b1543410584"></a><a name="b1543410584"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2456979"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p64797609"><a name="p64797609"></a><a name="p64797609"></a>dataStores</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.2 "><p id="p14114947"><a name="p14114947"></a><a name="p14114947"></a>List data structure. For details, see <a href="#table66531170">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p22140377"><a name="p22140377"></a><a name="p22140377"></a>Indicates the list of database versions.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  dataStores field data structure description

    <a name="table66531170"></a>
    <table><thead align="left"><tr id="row12984378"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a><strong id="b1497928198"><a name="b1497928198"></a><a name="b1497928198"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a><strong id="b1619437561"><a name="b1619437561"></a><a name="b1619437561"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a><strong id="b595212698"><a name="b595212698"></a><a name="b595212698"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4719792"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46758891"><a name="p46758891"></a><a name="p46758891"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30470722"><a name="p30470722"></a><a name="p30470722"></a>Indicates the database version ID. Its value is unique.</p>
    </td>
    </tr>
    <tr id="row5801050"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p123050"><a name="p123050"></a><a name="p123050"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9967070"><a name="p9967070"></a><a name="p9967070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2026335"><a name="p2026335"></a><a name="p2026335"></a>Indicates the database version.</p>
    </td>
    </tr>
    <tr id="row18237015"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p803253"><a name="p803253"></a><a name="p803253"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65063572"><a name="p65063572"></a><a name="p65063572"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35658012"><a name="p35658012"></a><a name="p35658012"></a>Indicates the database ID.</p>
    </td>
    </tr>
    <tr id="row52486654"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23560597"><a name="p23560597"></a><a name="p23560597"></a>image</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29360233"><a name="p29360233"></a><a name="p29360233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p29368673"><a name="p29368673"></a><a name="p29368673"></a>Indicates the database image ID.</p>
    </td>
    </tr>
    <tr id="row62991470"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2035480"><a name="p2035480"></a><a name="p2035480"></a>packages</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30656219"><a name="p30656219"></a><a name="p30656219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p125790"><a name="p125790"></a><a name="p125790"></a>Indicates the database package version information.</p>
    </td>
    </tr>
    <tr id="row1132111"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24592149"><a name="p24592149"></a><a name="p24592149"></a>active</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45807089"><a name="p45807089"></a><a name="p45807089"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p195391288540"><a name="p195391288540"></a><a name="p195391288540"></a>Indicates the database version activation status. The API returns information only about activated database versions.</p>
    <a name="ul1589151015546"></a><a name="ul1589151015546"></a><ul id="ul1589151015546"><li><strong id="b599005943910"><a name="b599005943910"></a><a name="b599005943910"></a>0</strong>: The database version is not activated.</li><li><strong id="b1440819784015"><a name="b1440819784015"></a><a name="b1440819784015"></a>1</strong>: The database version is activated.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "dataStores": [
        {
          "id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a62",
          "name": "5.6.33",
          "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
          "image": "36bdc308-0389-4830-8813-4a98d62b97de",
          "packages": "MySQL-server-5.6.33",
          "active": 1
        },
        {
          "id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61",
          "name": "5.6.30",
          "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
          "image": "36bdc308-0389-4830-8813-4a98d62b97de",
          "packages": "MySQL-server-5.6.30",
          "active": 1
        },
        {
          "id": "96cccede-bc51-11e6-bd4d-286ed488dd62",
          "name": "5.6.34",
          "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
          "image": "36bdc308-0389-4830-8813-4a98d62b97de",
          "packages": "MySQL-server-5.6.34",
          "active": 1
        },
        {
          "id": "35a3d5ba-6f74-4b29-824d-6de20f1ac090",
          "name": "5.6.35",
          "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
          "image": "36bdc308-0389-4830-8813-4a98d62b97de",
          "packages": "MySQL-server-5.6.35",
          "active": 1
        },
        {
          "id": "129a90a5-d4ef-4828-b3e3-4d3a1e91700d",
          "name": "5.6.36",
          "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
          "image": "36bdc308-0389-4830-8813-4a98d62b97de",
          "packages": "MySQL-server-5.6.36",
          "active": 1
        },
        {
          "id": "87620726-6802-46c0-9028-a8785e1f1922",
          "name": "5.7.17",
          "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
          "image": "36bdc308-0389-4830-8813-4a98d62b97de",
          "packages": "MySQL-server-5.7.17",
          "active": 1
        }
      ]
    }
    ```


## Abnormal Response<a name="section1651899"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

