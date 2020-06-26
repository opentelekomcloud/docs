# Adding a Protected Instance Tag<a name="sdrs_05_0803"></a>

## Function<a name="section156711130476"></a>

You can add a maximum of 20 tags to a protected instance.

This API is idempotent.

If a to-be-created tag has the same key as an existing tag, the tag will be created and overwrite the existing one.

## URI<a name="section196717394711"></a>

-   URI format

    POST /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}/tags

-   Parameter description

    <a name="table9673183114717"></a>
    <table><thead align="left"><tr id="row684110384719"><th class="cellrowborder" valign="top" width="20.41%" id="mcps1.1.5.1.1"><p id="p198411438476"><a name="p198411438476"></a><a name="p198411438476"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.1.5.1.2"><p id="p684113154719"><a name="p684113154719"></a><a name="p684113154719"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.1.5.1.3"><p id="p2841183164713"><a name="p2841183164713"></a><a name="p2841183164713"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86%" id="mcps1.1.5.1.4"><p id="p2084114334716"><a name="p2084114334716"></a><a name="p2084114334716"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15841133194710"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.1.5.1.1 "><p id="p584118334716"><a name="p584118334716"></a><a name="p584118334716"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.1.5.1.2 "><p id="p58410374720"><a name="p58410374720"></a><a name="p58410374720"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p168417310472"><a name="p168417310472"></a><a name="p168417310472"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.1.5.1.4 "><p id="p5841143134717"><a name="p5841143134717"></a><a name="p5841143134717"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row784114310474"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.1.5.1.1 "><p id="p684219394716"><a name="p684219394716"></a><a name="p684219394716"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.1.5.1.2 "><p id="p13842153184713"><a name="p13842153184713"></a><a name="p13842153184713"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p18421933474"><a name="p18421933474"></a><a name="p18421933474"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.1.5.1.4 "><p id="p68426318470"><a name="p68426318470"></a><a name="p68426318470"></a>Specifies the ID of a protected instance.</p>
    <p id="p1288981015716"><a name="p1288981015716"></a><a name="p1288981015716"></a>For details, see <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11681936470"></a>

-   Parameter description

    <a name="table1868414316477"></a>
    <table><thead align="left"><tr id="row084203134717"><th class="cellrowborder" valign="top" width="10.31%" id="mcps1.1.5.1.1"><p id="p684215334712"><a name="p684215334712"></a><a name="p684215334712"></a><strong id="b2013674311"><a name="b2013674311"></a><a name="b2013674311"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.65%" id="mcps1.1.5.1.2"><p id="p3842239473"><a name="p3842239473"></a><a name="p3842239473"></a><strong id="b59255491"><a name="b59255491"></a><a name="b59255491"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.4%" id="mcps1.1.5.1.3"><p id="p138426324720"><a name="p138426324720"></a><a name="p138426324720"></a><strong id="b489656963"><a name="b489656963"></a><a name="b489656963"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.64%" id="mcps1.1.5.1.4"><p id="p1884212320477"><a name="p1884212320477"></a><a name="p1884212320477"></a><strong id="b22008581"><a name="b22008581"></a><a name="b22008581"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7842113194717"><td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.1.5.1.1 "><p id="p16842193134720"><a name="p16842193134720"></a><a name="p16842193134720"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.1.5.1.2 "><p id="p188421364714"><a name="p188421364714"></a><a name="p188421364714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.1.5.1.3 "><p id="p48421439473"><a name="p48421439473"></a><a name="p48421439473"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.64%" headers="mcps1.1.5.1.4 "><p id="p98428394716"><a name="p98428394716"></a><a name="p98428394716"></a>Specifies the tag to be added.</p>
    <p id="p105811647181312"><a name="p105811647181312"></a><a name="p105811647181312"></a>For details, see <a href="#table1569003154718">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Data structure of field  **tag**

    <a name="table1569003154718"></a>
    <table><thead align="left"><tr id="row13842636476"><th class="cellrowborder" valign="top" width="10.2%" id="mcps1.2.5.1.1"><p id="p1584214311477"><a name="p1584214311477"></a><a name="p1584214311477"></a><strong id="b994682339"><a name="b994682339"></a><a name="b994682339"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.5.1.2"><p id="p684214314714"><a name="p684214314714"></a><a name="p684214314714"></a><strong id="b502054040"><a name="b502054040"></a><a name="b502054040"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.270000000000001%" id="mcps1.2.5.1.3"><p id="p10842123134718"><a name="p10842123134718"></a><a name="p10842123134718"></a><strong id="b1001301507"><a name="b1001301507"></a><a name="b1001301507"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.08%" id="mcps1.2.5.1.4"><p id="p38427317473"><a name="p38427317473"></a><a name="p38427317473"></a><strong id="b1205942685"><a name="b1205942685"></a><a name="b1205942685"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1584218314471"><td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.1 "><p id="p6842732471"><a name="p6842732471"></a><a name="p6842732471"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.2 "><p id="p384363164719"><a name="p384363164719"></a><a name="p384363164719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.2.5.1.3 "><p id="p68431334478"><a name="p68431334478"></a><a name="p68431334478"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.08%" headers="mcps1.2.5.1.4 "><p id="p1333413193"><a name="p1333413193"></a><a name="p1333413193"></a>Specifies the tag key. The tag key of a resource must be unique.</p>
    </td>
    </tr>
    <tr id="row5843338477"><td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.1 "><p id="p884315311475"><a name="p884315311475"></a><a name="p884315311475"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.2 "><p id="p5843932476"><a name="p5843932476"></a><a name="p5843932476"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.2.5.1.3 "><p id="p1784312334715"><a name="p1784312334715"></a><a name="p1784312334715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.08%" headers="mcps1.2.5.1.4 "><p id="p2703810913"><a name="p2703810913"></a><a name="p2703810913"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/67a2cc7e-fb87-41a8-ba28-9c032abcaee1/tags

    ```
    {
        "tag": {
            "key": "DEV",
            "value": "DEV1"
        }
    }
    ```


## Response<a name="section8560173116203"></a>

-   Example response

    None


## **Returned Value**<a name="section12705237478"></a>

-   Normal

    <a name="table14707131479"></a>
    <table><thead align="left"><tr id="row2084313164712"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p184453104711"><a name="p184453104711"></a><a name="p184453104711"></a><strong id="b2105107720"><a name="b2105107720"></a><a name="b2105107720"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p98441039474"><a name="p98441039474"></a><a name="p98441039474"></a><strong id="b1917470285"><a name="b1917470285"></a><a name="b1917470285"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1884418312473"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p20844638476"><a name="p20844638476"></a><a name="p20844638476"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p13844334479"><a name="p13844334479"></a><a name="p13844334479"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table127107354710"></a>
    <table><thead align="left"><tr id="row168447364714"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p108447316477"><a name="p108447316477"></a><a name="p108447316477"></a><strong id="b644007098"><a name="b644007098"></a><a name="b644007098"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p1884419394717"><a name="p1884419394717"></a><a name="p1884419394717"></a><strong id="b197890121"><a name="b197890121"></a><a name="b197890121"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2084415320479"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p58444364717"><a name="p58444364717"></a><a name="p58444364717"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p148441533470"><a name="p148441533470"></a><a name="p148441533470"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row5844183114718"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p384418314475"><a name="p384418314475"></a><a name="p384418314475"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1684413310472"><a name="p1684413310472"></a><a name="p1684413310472"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row38443316475"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12844431478"><a name="p12844431478"></a><a name="p12844431478"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p188442313474"><a name="p188442313474"></a><a name="p188442313474"></a>Insufficient permission.</p>
    </td>
    </tr>
    <tr id="row184423204712"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p2084410316474"><a name="p2084410316474"></a><a name="p2084410316474"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p108447384710"><a name="p108447384710"></a><a name="p108447384710"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row48447318472"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3845639471"><a name="p3845639471"></a><a name="p3845639471"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1584518354710"><a name="p1584518354710"></a><a name="p1584518354710"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


