# Querying Resource Tags<a name="dws_02_0049"></a>

## Function<a name="section1760073373414"></a>

This interface is used to query tags of a specified resource.

## URI<a name="section16001333163417"></a>

-   URI format

    GET /v1.0/\{project\_id\}/clusters/\{resource\_id\}/tags

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table12608933133410"></a>
    <table><thead align="left"><tr id="row97131335343"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p17135334341"><a name="p17135334341"></a><a name="p17135334341"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p5713733113415"><a name="p5713733113415"></a><a name="p5713733113415"></a><strong id="b84235270684256"><a name="b84235270684256"></a><a name="b84235270684256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="p1771333323411"><a name="p1771333323411"></a><a name="p1771333323411"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.495049504950494%" id="mcps1.2.5.1.4"><p id="p2713153317341"><a name="p2713153317341"></a><a name="p2713153317341"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1271313333417"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p137131033183420"><a name="p137131033183420"></a><a name="p137131033183420"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p12713033153410"><a name="p12713033153410"></a><a name="p12713033153410"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p1471423363419"><a name="p1471423363419"></a><a name="p1471423363419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="p14202648155510"><a name="p14202648155510"></a><a name="p14202648155510"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row127146339346"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p571416333342"><a name="p571416333342"></a><a name="p571416333342"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p1171413353414"><a name="p1171413353414"></a><a name="p1171413353414"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p16714113312342"><a name="p16714113312342"></a><a name="p16714113312342"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="p97144339347"><a name="p97144339347"></a><a name="p97144339347"></a>Resource ID. Example: <strong id="b84235270614114"><a name="b84235270614114"></a><a name="b84235270614114"></a>7d85f602-a948-4a30-afd4-e84f47471c15</strong></p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4615033123413"></a>

-   Sample request

    ```
    GET /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/7d85f602-a948-4a30-afd4-e84f47471c15/tags
    ```


## **Response**<a name="section10616123373417"></a>

-   Sample response

    ```
    {
        "tags": [
            {
                "key": "Flower",
                "value": "rose"
            },
            {
                "key": "Food",
                "value": "pie"
            }
        ]
    }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="table126191433193417"></a>
    <table><thead align="left"><tr id="row371483310346"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p1971419336342"><a name="p1971419336342"></a><a name="p1971419336342"></a><strong id="b1741278898"><a name="b1741278898"></a><a name="b1741278898"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p1971443313349"><a name="p1971443313349"></a><a name="p1971443313349"></a><strong id="b608206872"><a name="b608206872"></a><a name="b608206872"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p13714633143415"><a name="p13714633143415"></a><a name="p13714633143415"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p1171413383414"><a name="p1171413383414"></a><a name="p1171413383414"></a><strong id="b2056528921"><a name="b2056528921"></a><a name="b2056528921"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1571483393414"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p1171473316347"><a name="p1171473316347"></a><a name="p1171473316347"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p17714153383417"><a name="p17714153383417"></a><a name="p17714153383417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p117143333347"><a name="p117143333347"></a><a name="p117143333347"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p2714033193419"><a name="p2714033193419"></a><a name="p2714033193419"></a>Tag list. For details, see <a href="#table120412164200">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **resource\_tag**  field description

    <a name="table120412164200"></a>
    <table><thead align="left"><tr id="row521271642012"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.1"><p id="p82131816182015"><a name="p82131816182015"></a><a name="p82131816182015"></a><strong id="b1876847109"><a name="b1876847109"></a><a name="b1876847109"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.2"><p id="p1921511619208"><a name="p1921511619208"></a><a name="p1921511619208"></a><strong id="b307078144"><a name="b307078144"></a><a name="b307078144"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.3"><p id="p12161816182020"><a name="p12161816182020"></a><a name="p12161816182020"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.5.1.4"><p id="p19217191662015"><a name="p19217191662015"></a><a name="p19217191662015"></a><strong id="b607756933"><a name="b607756933"></a><a name="b607756933"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row112192016112015"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.1 "><p id="p15220101682019"><a name="p15220101682019"></a><a name="p15220101682019"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p522291615208"><a name="p522291615208"></a><a name="p522291615208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p2022431620202"><a name="p2022431620202"></a><a name="p2022431620202"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="p922511632019"><a name="p922511632019"></a><a name="p922511632019"></a>Key. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces. </p>
    <p id="p119639141303"><a name="p119639141303"></a><a name="p119639141303"></a>It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row13227716142013"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.1 "><p id="p4229191682012"><a name="p4229191682012"></a><a name="p4229191682012"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p1823071662017"><a name="p1823071662017"></a><a name="p1823071662017"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p423241618204"><a name="p423241618204"></a><a name="p423241618204"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="p523361692014"><a name="p523361692014"></a><a name="p523361692014"></a>Key value. A tag value can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces. It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="section263463323410"></a>

-   Normal

    200

-   Abnormal

    **Table  4**  Returned value for failed requests

    <a name="table3639133318349"></a>
    <table><thead align="left"><tr id="row571512332344"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p167151633193412"><a name="p167151633193412"></a><a name="p167151633193412"></a><strong id="b84235270615197"><a name="b84235270615197"></a><a name="b84235270615197"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p14715143353418"><a name="p14715143353418"></a><a name="p14715143353418"></a><strong id="b1637829872"><a name="b1637829872"></a><a name="b1637829872"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2715123333416"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p6715433113411"><a name="p6715433113411"></a><a name="p6715433113411"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p87151233203417"><a name="p87151233203417"></a><a name="p87151233203417"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row1271563353412"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p4715163317341"><a name="p4715163317341"></a><a name="p4715163317341"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p3715173310345"><a name="p3715173310345"></a><a name="p3715173310345"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row16715123333418"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p117151533173418"><a name="p117151533173418"></a><a name="p117151533173418"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p197151733133413"><a name="p197151733133413"></a><a name="p197151733133413"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row5715193311349"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1571523383414"><a name="p1571523383414"></a><a name="p1571523383414"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p671533311340"><a name="p671533311340"></a><a name="p671533311340"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row3715203317345"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1715163373410"><a name="p1715163373410"></a><a name="p1715163373410"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p117154336340"><a name="p117154336340"></a><a name="p117154336340"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


