# Querying a Protected Instance Tag<a name="sdrs_05_0805"></a>

## Function<a name="section4824646124711"></a>

This interface is used to query tags of a specified protected instance.

## URI<a name="section182518469474"></a>

-   URI format

    GET /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}/tags

-   Parameter description

    <a name="table982754614711"></a>
    <table><thead align="left"><tr id="row796014469473"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.1"><p id="p696084618471"><a name="p696084618471"></a><a name="p696084618471"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.530000000000005%" id="mcps1.1.5.1.2"><p id="p119603469470"><a name="p119603469470"></a><a name="p119603469470"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.1.5.1.3"><p id="p49602046114713"><a name="p49602046114713"></a><a name="p49602046114713"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.84%" id="mcps1.1.5.1.4"><p id="p129601446124715"><a name="p129601446124715"></a><a name="p129601446124715"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row696014694719"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.1 "><p id="p0960746124715"><a name="p0960746124715"></a><a name="p0960746124715"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.2 "><p id="p99601446154714"><a name="p99601446154714"></a><a name="p99601446154714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p2960146124716"><a name="p2960146124716"></a><a name="p2960146124716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.84%" headers="mcps1.1.5.1.4 "><p id="p4960184612473"><a name="p4960184612473"></a><a name="p4960184612473"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row17960204684712"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.1 "><p id="p596064624711"><a name="p596064624711"></a><a name="p596064624711"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.2 "><p id="p3960184617471"><a name="p3960184617471"></a><a name="p3960184617471"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p596064664713"><a name="p596064664713"></a><a name="p596064664713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.84%" headers="mcps1.1.5.1.4 "><p id="p119613464471"><a name="p119613464471"></a><a name="p119613464471"></a>Specifies the ID of a protected instance.</p>
    <p id="p13101121716915"><a name="p13101121716915"></a><a name="p13101121716915"></a>For details, see <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section883411463475"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/50f5091e-9e9e-473c-a932-2a2cbcbeb1ff/tags


## Response<a name="section178349461475"></a>

-   Parameter description

    <a name="table17838184694718"></a>
    <table><thead align="left"><tr id="row10961046134712"><th class="cellrowborder" valign="top" width="10.2%" id="mcps1.1.5.1.1"><p id="p119611446134711"><a name="p119611446134711"></a><a name="p119611446134711"></a><strong id="b842352706162023_1"><a name="b842352706162023_1"></a><a name="b842352706162023_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.47%" id="mcps1.1.5.1.2"><p id="p1996104617477"><a name="p1996104617477"></a><a name="p1996104617477"></a><strong id="b84235270615447_1"><a name="b84235270615447_1"></a><a name="b84235270615447_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.55%" id="mcps1.1.5.1.3"><p id="p1696124612470"><a name="p1696124612470"></a><a name="p1696124612470"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.78%" id="mcps1.1.5.1.4"><p id="p8961104644718"><a name="p8961104644718"></a><a name="p8961104644718"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19961746114718"><td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.1.5.1.1 "><p id="p396154604718"><a name="p396154604718"></a><a name="p396154604718"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.1.5.1.2 "><p id="p6961446124718"><a name="p6961446124718"></a><a name="p6961446124718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.1.5.1.3 "><p id="p1196144618478"><a name="p1196144618478"></a><a name="p1196144618478"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.1.5.1.4 "><p id="p119611246124717"><a name="p119611246124717"></a><a name="p119611246124717"></a>Specifies the tag list.</p>
    <p id="p1582425517144"><a name="p1582425517144"></a><a name="p1582425517144"></a>For details, see <a href="#table684444618473">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Data structure of the  **resource\_tag**  field

    <a name="table684444618473"></a>
    <table><thead align="left"><tr id="row6961114614475"><th class="cellrowborder" valign="top" width="10.2%" id="mcps1.2.5.1.1"><p id="p179627461479"><a name="p179627461479"></a><a name="p179627461479"></a><strong id="b842352706162023_2"><a name="b842352706162023_2"></a><a name="b842352706162023_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.5.1.2"><p id="p139621546154716"><a name="p139621546154716"></a><a name="p139621546154716"></a><strong id="b84235270615447_2"><a name="b84235270615447_2"></a><a name="b84235270615447_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.270000000000001%" id="mcps1.2.5.1.3"><p id="p11962174619471"><a name="p11962174619471"></a><a name="p11962174619471"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.04%" id="mcps1.2.5.1.4"><p id="p5962104694712"><a name="p5962104694712"></a><a name="p5962104694712"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1596254615471"><td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.1 "><p id="p996217464474"><a name="p996217464474"></a><a name="p996217464474"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.2 "><p id="p0962194644715"><a name="p0962194644715"></a><a name="p0962194644715"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.2.5.1.3 "><p id="p4962144644720"><a name="p4962144644720"></a><a name="p4962144644720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.04%" headers="mcps1.2.5.1.4 "><p id="p13546111671114"><a name="p13546111671114"></a><a name="p13546111671114"></a>Specifies the tag key. The tag key of a resource must be unique.</p>
    </td>
    </tr>
    <tr id="row496204664713"><td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.1 "><p id="p10962346174712"><a name="p10962346174712"></a><a name="p10962346174712"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.2 "><p id="p1096224619477"><a name="p1096224619477"></a><a name="p1096224619477"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.2.5.1.3 "><p id="p396284611472"><a name="p396284611472"></a><a name="p396284611472"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.04%" headers="mcps1.2.5.1.4 "><p id="p613413217119"><a name="p613413217119"></a><a name="p613413217119"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## **Returned Value**<a name="section486354618476"></a>

-   Normal

    <a name="table19866104694716"></a>
    <table><thead align="left"><tr id="row7963134614470"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1696315467474"><a name="p1696315467474"></a><a name="p1696315467474"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p1596315467473"><a name="p1596315467473"></a><a name="p1596315467473"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row396317469476"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p17963154694714"><a name="p17963154694714"></a><a name="p17963154694714"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p11963184613472"><a name="p11963184613472"></a><a name="p11963184613472"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table1486854619478"></a>
    <table><thead align="left"><tr id="row496334618471"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1696344615478"><a name="p1696344615478"></a><a name="p1696344615478"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p6963184614475"><a name="p6963184614475"></a><a name="p6963184614475"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14963046204717"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p09631146194710"><a name="p09631146194710"></a><a name="p09631146194710"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p396354619470"><a name="p396354619470"></a><a name="p396354619470"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row7963104613472"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p496313465475"><a name="p496313465475"></a><a name="p496313465475"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p0963184664715"><a name="p0963184664715"></a><a name="p0963184664715"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row11963846174710"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p9963174612474"><a name="p9963174612474"></a><a name="p9963174612474"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p12963154664712"><a name="p12963154664712"></a><a name="p12963154664712"></a>Insufficient permission.</p>
    </td>
    </tr>
    <tr id="row59631464478"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p199644460479"><a name="p199644460479"></a><a name="p199644460479"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p169641346134712"><a name="p169641346134712"></a><a name="p169641346134712"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row296464624720"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11964174611471"><a name="p11964174611471"></a><a name="p11964174611471"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p199641546124713"><a name="p199641546124713"></a><a name="p199641546124713"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


