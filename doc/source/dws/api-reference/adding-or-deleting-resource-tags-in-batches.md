# Adding or Deleting Resource Tags in Batches<a name="dws_02_0047"></a>

## Function<a name="section961342216326"></a>

This API is used to add or delete tags in batches for a specified resource. A maximum of 10 tags can be added for one resource.

## URI<a name="section3616162211329"></a>

-   URI format

    POST /v1.0/\{project\_id\}/clusters/\{resource\_id\}/tags/action

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table1263414221320"></a>
    <table><thead align="left"><tr id="row38511622143216"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="p1085122233219"><a name="p1085122233219"></a><a name="p1085122233219"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p1785132212326"><a name="p1785132212326"></a><a name="p1785132212326"></a><strong id="b84235270684256"><a name="b84235270684256"></a><a name="b84235270684256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.2.5.1.3"><p id="p68519227328"><a name="p68519227328"></a><a name="p68519227328"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="p285122253218"><a name="p285122253218"></a><a name="p285122253218"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5852142211326"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p285262203215"><a name="p285262203215"></a><a name="p285262203215"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p6852822153217"><a name="p6852822153217"></a><a name="p6852822153217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p188521922133214"><a name="p188521922133214"></a><a name="p188521922133214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p14202648155510"><a name="p14202648155510"></a><a name="p14202648155510"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row4852152214321"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p7852822153215"><a name="p7852822153215"></a><a name="p7852822153215"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p285232210324"><a name="p285232210324"></a><a name="p285232210324"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p985212216324"><a name="p985212216324"></a><a name="p985212216324"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p88521322163214"><a name="p88521322163214"></a><a name="p88521322163214"></a>Resource ID. Example: <strong id="b84235270614114"><a name="b84235270614114"></a><a name="b84235270614114"></a>7d85f602-a948-4a30-afd4-e84f47471c15</strong></p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section96421022183220"></a>

-   Sample request for adding tags in batches

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/7d85f602-a948-4a30-afd4-e84f47471c15/tags/action
    {
        "action": "create",
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

-   Sample request for deleting tags in batches

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/7d85f602-a948-4a30-afd4-e84f47471c15/tags/action
    {
        "action": "delete",
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

    **Table  2**  Request parameter description

    <a name="table12646422113215"></a>
    <table><thead align="left"><tr id="row20852122213217"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p5852112218325"><a name="p5852112218325"></a><a name="p5852112218325"></a><strong id="b509628314"><a name="b509628314"></a><a name="b509628314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p285272214324"><a name="p285272214324"></a><a name="p285272214324"></a><strong id="b962126441"><a name="b962126441"></a><a name="b962126441"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p2852202214326"><a name="p2852202214326"></a><a name="p2852202214326"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="p20852152253220"><a name="p20852152253220"></a><a name="p20852152253220"></a><strong id="b2063706827"><a name="b2063706827"></a><a name="b2063706827"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8852172213322"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p7852322193218"><a name="p7852322193218"></a><a name="p7852322193218"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1685272213212"><a name="p1685272213212"></a><a name="p1685272213212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p20853422113216"><a name="p20853422113216"></a><a name="p20853422113216"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p1853102211322"><a name="p1853102211322"></a><a name="p1853102211322"></a>Tag list. For details, see <a href="#table594583311194">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row178536228326"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p3853162263213"><a name="p3853162263213"></a><a name="p3853162263213"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p14853172283211"><a name="p14853172283211"></a><a name="p14853172283211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p285332216322"><a name="p285332216322"></a><a name="p285332216322"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p3455728124210"><a name="p3455728124210"></a><a name="p3455728124210"></a>Identifies the operation. The value can be <strong id="b842352706112823"><a name="b842352706112823"></a><a name="b842352706112823"></a>create</strong> or <strong id="b842352706112836"><a name="b842352706112836"></a><a name="b842352706112836"></a>delete</strong>.</p>
    <a name="ul1611136174215"></a><a name="ul1611136174215"></a><ul id="ul1611136174215"><li><strong id="b84235270611286"><a name="b84235270611286"></a><a name="b84235270611286"></a>create</strong>: indicates to add tags in batches.</li><li><strong id="b84235270611295"><a name="b84235270611295"></a><a name="b84235270611295"></a>delete</strong>: indicates to delete tags in batches.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **resource\_tag**  field description

    <a name="table594583311194"></a>
    <table><thead align="left"><tr id="row1955183371910"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p17959153314198"><a name="p17959153314198"></a><a name="p17959153314198"></a><strong id="b202867273"><a name="b202867273"></a><a name="b202867273"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p11963153351911"><a name="p11963153351911"></a><a name="p11963153351911"></a><strong id="b1126141287"><a name="b1126141287"></a><a name="b1126141287"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p3965183313192"><a name="p3965183313192"></a><a name="p3965183313192"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="p19692338199"><a name="p19692338199"></a><a name="p19692338199"></a><strong id="b2046507491"><a name="b2046507491"></a><a name="b2046507491"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15976163371911"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p59811333121919"><a name="p59811333121919"></a><a name="p59811333121919"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p189831133141917"><a name="p189831133141917"></a><a name="p189831133141917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p598719331190"><a name="p598719331190"></a><a name="p598719331190"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p16990933201912"><a name="p16990933201912"></a><a name="p16990933201912"></a>Tag key. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces.</p>
    <p id="p1740919129378"><a name="p1740919129378"></a><a name="p1740919129378"></a>It can contain only uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row499283311914"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p189946338192"><a name="p189946338192"></a><a name="p189946338192"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p15996143318198"><a name="p15996143318198"></a><a name="p15996143318198"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p086349191"><a name="p086349191"></a><a name="p086349191"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p1211143481914"><a name="p1211143481914"></a><a name="p1211143481914"></a>Key value. A tag value can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces.</p>
    <p id="p4764545454"><a name="p4764545454"></a><a name="p4764545454"></a>It can contain only uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Response**<a name="section1267862233212"></a>

Sample response

```
STATUS CODE 204
```

## Returned Value<a name="section367910228327"></a>

-   Normal

    204

-   Abnormal

    **Table  4**  Returned value for failed requests

    <a name="table5682122263215"></a>
    <table><thead align="left"><tr id="row13855122218322"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p188551522163210"><a name="p188551522163210"></a><a name="p188551522163210"></a><strong id="b84235270611397"><a name="b84235270611397"></a><a name="b84235270611397"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p8855102283212"><a name="p8855102283212"></a><a name="p8855102283212"></a><strong id="b1146115892"><a name="b1146115892"></a><a name="b1146115892"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17855722163216"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p785572213216"><a name="p785572213216"></a><a name="p785572213216"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p88559223327"><a name="p88559223327"></a><a name="p88559223327"></a>Invalid tag.</p>
    </td>
    </tr>
    <tr id="row1085562212325"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p15855102243213"><a name="p15855102243213"></a><a name="p15855102243213"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p885518226328"><a name="p885518226328"></a><a name="p885518226328"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row12855622183220"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p385532293210"><a name="p385532293210"></a><a name="p385532293210"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p38551822153220"><a name="p38551822153220"></a><a name="p38551822153220"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row198552222326"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p13855022103219"><a name="p13855022103219"></a><a name="p13855022103219"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p19855222183220"><a name="p19855222183220"></a><a name="p19855222183220"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1885502219326"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p78551522163211"><a name="p78551522163211"></a><a name="p78551522163211"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p12855182213325"><a name="p12855182213325"></a><a name="p12855182213325"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


