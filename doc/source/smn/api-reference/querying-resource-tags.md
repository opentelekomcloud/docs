# Querying Resource Tags<a name="smn_api_56005"></a>

## Description<a name="section199791258152011"></a>

-   API name

    ListResourceTags


-   Function

    Query tags of a specified resource.


## URI<a name="section49791258162015"></a>

-   URI format

    GET /v2/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags

-   Parameter description

    <a name="table29791058162012"></a>
    <table><thead align="left"><tr id="row17151155952013"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p1915195972018"><a name="p1915195972018"></a><a name="p1915195972018"></a><strong id="b112541522174019"><a name="b112541522174019"></a><a name="b112541522174019"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p3151105916206"><a name="p3151105916206"></a><a name="p3151105916206"></a><strong id="b6302182419405"><a name="b6302182419405"></a><a name="b6302182419405"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.61%" id="mcps1.1.5.1.3"><p id="p191517591201"><a name="p191517591201"></a><a name="p191517591201"></a><strong id="b030115252401"><a name="b030115252401"></a><a name="b030115252401"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.39%" id="mcps1.1.5.1.4"><p id="p1715185918204"><a name="p1715185918204"></a><a name="p1715185918204"></a><strong id="b16220192634014"><a name="b16220192634014"></a><a name="b16220192634014"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51511159172015"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p201511599202"><a name="p201511599202"></a><a name="p201511599202"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p21513598202"><a name="p21513598202"></a><a name="p21513598202"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.61%" headers="mcps1.1.5.1.3 "><p id="p215118592200"><a name="p215118592200"></a><a name="p215118592200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.39%" headers="mcps1.1.5.1.4 "><p id="p5151115912205"><a name="p5151115912205"></a><a name="p5151115912205"></a>Project ID</p>
    <p id="p118812918506"><a name="p118812918506"></a><a name="p118812918506"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row151511559172017"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p99531421797"><a name="p99531421797"></a><a name="p99531421797"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p1495310421799"><a name="p1495310421799"></a><a name="p1495310421799"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.61%" headers="mcps1.1.5.1.3 "><p id="p149531342296"><a name="p149531342296"></a><a name="p149531342296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.39%" headers="mcps1.1.5.1.4 "><p id="p52661238184213"><a name="p52661238184213"></a><a name="p52661238184213"></a>Resource type</p>
    <p id="p1533013513535"><a name="p1533013513535"></a><a name="p1533013513535"></a>The value can be the following:</p>
    <p id="p14550953686"><a name="p14550953686"></a><a name="p14550953686"></a><strong id="b76637571712"><a name="b76637571712"></a><a name="b76637571712"></a>smn_topic</strong>: topic</p>
    <p id="p8682201993"><a name="p8682201993"></a><a name="p8682201993"></a></p>
    <p id="p278251314214"><a name="p278251314214"></a><a name="p278251314214"></a></p>
    </td>
    </tr>
    <tr id="row20151259132010"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1363485413187"><a name="p1363485413187"></a><a name="p1363485413187"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p463417547182"><a name="p463417547182"></a><a name="p463417547182"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.61%" headers="mcps1.1.5.1.3 "><p id="p7634195417180"><a name="p7634195417180"></a><a name="p7634195417180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.39%" headers="mcps1.1.5.1.4 "><p id="p176341254201810"><a name="p176341254201810"></a><a name="p176341254201810"></a>Resource ID</p>
    <p id="p57491711103514"><a name="p57491711103514"></a><a name="p57491711103514"></a>Obtain a resource ID:</p>
    <a name="ul111761720155610"></a><a name="ul111761720155610"></a><ul id="ul111761720155610"><li>Add <strong id="smn_api_56002_b1046628401"><a name="smn_api_56002_b1046628401"></a><a name="smn_api_56002_b1046628401"></a>X-SMN-RESOURCEID-TYPE=name</strong> in the request header and set the resource ID to the topic name.</li><li>Call the <strong id="smn_api_56002_b84235270694340"><a name="smn_api_56002_b84235270694340"></a><a name="smn_api_56002_b84235270694340"></a>GetResourceInstances</strong> API to obtain the resource ID.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1799514588205"></a>

-   Parameter description

    None


-   Request example

    ```
    GET https://{SMN_Endpoint}/v2/{project_id}/{resource_type}/{resource_id}/tags
    ```


## Response<a name="section799516585208"></a>

-   Parameter description

    <a name="table2010959142017"></a>
    <table><thead align="left"><tr id="row141511359192017"><th class="cellrowborder" valign="top" width="20.51%" id="mcps1.1.4.1.1"><p id="p10151105918204"><a name="p10151105918204"></a><a name="p10151105918204"></a><strong id="b442811136417"><a name="b442811136417"></a><a name="b442811136417"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.2"><p id="p515195922016"><a name="p515195922016"></a><a name="p515195922016"></a><strong id="b1161316157419"><a name="b1161316157419"></a><a name="b1161316157419"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.160000000000004%" id="mcps1.1.4.1.3"><p id="p201517594209"><a name="p201517594209"></a><a name="p201517594209"></a><strong id="b1899111674120"><a name="b1899111674120"></a><a name="b1899111674120"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17151559122015"><td class="cellrowborder" valign="top" width="20.51%" headers="mcps1.1.4.1.1 "><p id="p715119594207"><a name="p715119594207"></a><a name="p715119594207"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.2 "><p id="p271610325517"><a name="p271610325517"></a><a name="p271610325517"></a>Resource_tag structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.160000000000004%" headers="mcps1.1.4.1.3 "><p id="p1815155919201"><a name="p1815155919201"></a><a name="p1815155919201"></a>Tag list. For details, see <a href="#table1127111434346">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Resource\_tag structure

    <a name="table1127111434346"></a>
    <table><thead align="left"><tr id="smn_api_56001_row139311651171713"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.6.1.1"><p id="smn_api_56001_p993135161718"><a name="smn_api_56001_p993135161718"></a><a name="smn_api_56001_p993135161718"></a><strong id="smn_api_56001_b6377153915111"><a name="smn_api_56001_b6377153915111"></a><a name="smn_api_56001_b6377153915111"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.6.1.2"><p id="smn_api_56001_p19311451131719"><a name="smn_api_56001_p19311451131719"></a><a name="smn_api_56001_p19311451131719"></a><strong id="smn_api_56001_b553769561"><a name="smn_api_56001_b553769561"></a><a name="smn_api_56001_b553769561"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.6.1.3"><p id="smn_api_56001_p13931451141710"><a name="smn_api_56001_p13931451141710"></a><a name="smn_api_56001_p13931451141710"></a><strong id="smn_api_56001_b1343797695"><a name="smn_api_56001_b1343797695"></a><a name="smn_api_56001_b1343797695"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.6.1.4"><p id="smn_api_56001_p393125141712"><a name="smn_api_56001_p393125141712"></a><a name="smn_api_56001_p393125141712"></a><strong id="smn_api_56001_b36311841175120"><a name="smn_api_56001_b36311841175120"></a><a name="smn_api_56001_b36311841175120"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.633663366336634%" id="mcps1.2.6.1.5"><p id="smn_api_56001_p1715443212610"><a name="smn_api_56001_p1715443212610"></a><a name="smn_api_56001_p1715443212610"></a><strong id="smn_api_56001_b134437429517"><a name="smn_api_56001_b134437429517"></a><a name="smn_api_56001_b134437429517"></a>Constraint</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="smn_api_56001_row3931105113173"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.1 "><p id="smn_api_56001_p17931145131711"><a name="smn_api_56001_p17931145131711"></a><a name="smn_api_56001_p17931145131711"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.2 "><p id="smn_api_56001_p9931145120179"><a name="smn_api_56001_p9931145120179"></a><a name="smn_api_56001_p9931145120179"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.3 "><p id="smn_api_56001_p16931751111714"><a name="smn_api_56001_p16931751111714"></a><a name="smn_api_56001_p16931751111714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.6.1.4 "><p id="smn_api_56001_p393175116171"><a name="smn_api_56001_p393175116171"></a><a name="smn_api_56001_p393175116171"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.2.6.1.5 "><p id="smn_api_56001_p171314419267"><a name="smn_api_56001_p171314419267"></a><a name="smn_api_56001_p171314419267"></a>The key contains 36 Unicode characters at most and cannot be blank or an empty string. It can contain only digits, letters, hyphens (-), and underscores (_) and must not start or end with a space.</p>
    </td>
    </tr>
    <tr id="smn_api_56001_row39312515173"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.1 "><p id="smn_api_56001_p09311651171711"><a name="smn_api_56001_p09311651171711"></a><a name="smn_api_56001_p09311651171711"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.2 "><p id="smn_api_56001_p1693155113179"><a name="smn_api_56001_p1693155113179"></a><a name="smn_api_56001_p1693155113179"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.3 "><p id="smn_api_56001_p14931751141720"><a name="smn_api_56001_p14931751141720"></a><a name="smn_api_56001_p14931751141720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.6.1.4 "><p id="smn_api_56001_p159313515179"><a name="smn_api_56001_p159313515179"></a><a name="smn_api_56001_p159313515179"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.2.6.1.5 "><p id="smn_api_56001_p344164632615"><a name="smn_api_56001_p344164632615"></a><a name="smn_api_56001_p344164632615"></a>Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_) and must not start or end with a space.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

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


## Returned Value<a name="section242171292113"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

