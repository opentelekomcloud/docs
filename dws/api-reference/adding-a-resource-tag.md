# Adding a Resource Tag<a name="dws_02_0046"></a>

## Function<a name="section1575619425339"></a>

This API is used to add a resource tag for a resource. A maximum of 10 tags can be added for one resource.

## URI<a name="section875774253320"></a>

-   URI format

    POST /v1.0/\{project\_id\}/clusters/\{resource\_id\}/tags

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table157630425330"></a>
    <table><thead align="left"><tr id="row19894154214335"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p12894154253318"><a name="p12894154253318"></a><a name="p12894154253318"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p158941442123317"><a name="p158941442123317"></a><a name="p158941442123317"></a><strong id="b84235270684256"><a name="b84235270684256"></a><a name="b84235270684256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p1389411427332"><a name="p1389411427332"></a><a name="p1389411427332"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p1089414220333"><a name="p1089414220333"></a><a name="p1089414220333"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15894184214336"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1889410428338"><a name="p1889410428338"></a><a name="p1889410428338"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1689474219337"><a name="p1689474219337"></a><a name="p1689474219337"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p11894154210333"><a name="p11894154210333"></a><a name="p11894154210333"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p14202648155510"><a name="p14202648155510"></a><a name="p14202648155510"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row13895154219336"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p13895154223310"><a name="p13895154223310"></a><a name="p13895154223310"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p08955423332"><a name="p08955423332"></a><a name="p08955423332"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p188955425332"><a name="p188955425332"></a><a name="p188955425332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p158951842193319"><a name="p158951842193319"></a><a name="p158951842193319"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section177454283320"></a>

-   Sample request

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/7d85f602-a948-4a30-afd4-e84f47471c15/tags
    {
         "tag":
         {
            "key":"Flower",
            "value":"rose"
         }
    }
    ```

-   Parameter description

    **Table  2**  Request parameter description

    <a name="table8775154243312"></a>
    <table><thead align="left"><tr id="row689694212335"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p1289694223319"><a name="p1289694223319"></a><a name="p1289694223319"></a><strong id="b191920613"><a name="b191920613"></a><a name="b191920613"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p589644283312"><a name="p589644283312"></a><a name="p589644283312"></a><strong id="b1012064496"><a name="b1012064496"></a><a name="b1012064496"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p489684217332"><a name="p489684217332"></a><a name="p489684217332"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p889664283319"><a name="p889664283319"></a><a name="p889664283319"></a><strong id="b1137131069"><a name="b1137131069"></a><a name="b1137131069"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row589624293319"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1389616422333"><a name="p1389616422333"></a><a name="p1389616422333"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1089614263318"><a name="p1089614263318"></a><a name="p1089614263318"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p789844219336"><a name="p789844219336"></a><a name="p789844219336"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p8898124293318"><a name="p8898124293318"></a><a name="p8898124293318"></a>Tags. For details, see <a href="#table354113151341">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tag**  field description

    <a name="table354113151341"></a>
    <table><thead align="left"><tr id="row75500152343"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p1055331553419"><a name="p1055331553419"></a><a name="p1055331553419"></a><strong id="b1411414057"><a name="b1411414057"></a><a name="b1411414057"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p1955513152341"><a name="p1955513152341"></a><a name="p1955513152341"></a><strong id="b948459285"><a name="b948459285"></a><a name="b948459285"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p14556111515343"><a name="p14556111515343"></a><a name="p14556111515343"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p25591515193418"><a name="p25591515193418"></a><a name="p25591515193418"></a><strong id="b2088756909"><a name="b2088756909"></a><a name="b2088756909"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row456181593412"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p7564151563419"><a name="p7564151563419"></a><a name="p7564151563419"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p0567115143415"><a name="p0567115143415"></a><a name="p0567115143415"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p2569191518343"><a name="p2569191518343"></a><a name="p2569191518343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p75721115103417"><a name="p75721115103417"></a><a name="p75721115103417"></a>Tag key. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces. </p>
    <p id="p922511632019"><a name="p922511632019"></a><a name="p922511632019"></a>It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row457371583412"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p4575515143418"><a name="p4575515143418"></a><a name="p4575515143418"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p17578015193411"><a name="p17578015193411"></a><a name="p17578015193411"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p18579815123412"><a name="p18579815123412"></a><a name="p18579815123412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p9582161516342"><a name="p9582161516342"></a><a name="p9582161516342"></a>Key value. A tag value can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces. It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section1267862233212"></a>

Sample response

```
STATUS CODE 204
```

## Returned Value<a name="section12791174212331"></a>

-   Normal

    **Table  4**  Returned value for successful requests

    <a name="table14791154243313"></a>
    <table><thead align="left"><tr id="row189919424333"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p19899154215335"><a name="p19899154215335"></a><a name="p19899154215335"></a><strong id="b842352706111354"><a name="b842352706111354"></a><a name="b842352706111354"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p13899134214337"><a name="p13899134214337"></a><a name="p13899134214337"></a><strong id="b1524526187"><a name="b1524526187"></a><a name="b1524526187"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row0899134215334"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1889934213310"><a name="p1889934213310"></a><a name="p1889934213310"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p159001442163319"><a name="p159001442163319"></a><a name="p159001442163319"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  5**  Returned value for failed requests

    <a name="table079410423337"></a>
    <table><thead align="left"><tr id="row1890018421333"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p590014263316"><a name="p590014263316"></a><a name="p590014263316"></a><strong id="b1096493955"><a name="b1096493955"></a><a name="b1096493955"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p1790014263315"><a name="p1790014263315"></a><a name="p1790014263315"></a><strong id="b244844631"><a name="b244844631"></a><a name="b244844631"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15900134293311"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p390016425330"><a name="p390016425330"></a><a name="p390016425330"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p16900194213316"><a name="p16900194213316"></a><a name="p16900194213316"></a>Invalid tag.</p>
    </td>
    </tr>
    <tr id="row1890044213335"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p59001542133319"><a name="p59001542133319"></a><a name="p59001542133319"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p69001642163314"><a name="p69001642163314"></a><a name="p69001642163314"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row1890014253315"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p109004427335"><a name="p109004427335"></a><a name="p109004427335"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p6900154293315"><a name="p6900154293315"></a><a name="p6900154293315"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row149007426339"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p209006420331"><a name="p209006420331"></a><a name="p209006420331"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p18900642183316"><a name="p18900642183316"></a><a name="p18900642183316"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row129001842173315"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p11900342133310"><a name="p11900342133310"></a><a name="p11900342133310"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p169001642103316"><a name="p169001642103316"></a><a name="p169001642103316"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


