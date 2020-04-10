# Adding or Deleting Resource Tags in Batches<a name="smn_api_56002"></a>

## Description<a name="section11166154101819"></a>

-   API name

    BatchCreateOrDeleteResourceTags

-   Function

    Add or delete tags for a specified resource in batches.

    You can add a maximum of 10 tags to a resource.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The API is idempotent. When you are to create tags, if there are duplicate keys in the request body, an error is reported.  
    >If a to-be-created tag has the same key as an existing tag, the tag will be created and overwrite the existing one.  
    >When tags are being deleted and some tags do not exist, the operation is considered successful by default. The character set of the tags will not be checked.  


## URI<a name="section171812054161811"></a>

-   URI format

    POST /v2/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags/action

-   Parameter description

    <a name="table4181105410187"></a>
    <table><thead align="left"><tr id="row9634205461818"><th class="cellrowborder" valign="top" width="22.972297229722972%" id="mcps1.1.5.1.1"><p id="p13634105451820"><a name="p13634105451820"></a><a name="p13634105451820"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.972297229722972%" id="mcps1.1.5.1.2"><p id="p9634155461818"><a name="p9634155461818"></a><a name="p9634155461818"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.27202720272027%" id="mcps1.1.5.1.3"><p id="p176342054151820"><a name="p176342054151820"></a><a name="p176342054151820"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.78337833783379%" id="mcps1.1.5.1.4"><p id="p8634185410184"><a name="p8634185410184"></a><a name="p8634185410184"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row863485461812"><td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.5.1.1 "><p id="p15634154191818"><a name="p15634154191818"></a><a name="p15634154191818"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.5.1.2 "><p id="p36341354151815"><a name="p36341354151815"></a><a name="p36341354151815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.27202720272027%" headers="mcps1.1.5.1.3 "><p id="p196341954171820"><a name="p196341954171820"></a><a name="p196341954171820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.78337833783379%" headers="mcps1.1.5.1.4 "><p id="p11634105415185"><a name="p11634105415185"></a><a name="p11634105415185"></a>Project ID</p>
    <p id="p118812918506"><a name="p118812918506"></a><a name="p118812918506"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row1563419545185"><td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.5.1.1 "><p id="p99531421797"><a name="p99531421797"></a><a name="p99531421797"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.5.1.2 "><p id="p1495310421799"><a name="p1495310421799"></a><a name="p1495310421799"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.27202720272027%" headers="mcps1.1.5.1.3 "><p id="p149531342296"><a name="p149531342296"></a><a name="p149531342296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.78337833783379%" headers="mcps1.1.5.1.4 "><p id="p52661238184213"><a name="p52661238184213"></a><a name="p52661238184213"></a>Resource type</p>
    <p id="p278251314214"><a name="p278251314214"></a><a name="p278251314214"></a>The value can be the following:</p>
    <p id="p14550953686"><a name="p14550953686"></a><a name="p14550953686"></a><strong id="b55671313121318"><a name="b55671313121318"></a><a name="b55671313121318"></a>smn_topic</strong>: topic</p>
    <p id="p8682201993"><a name="p8682201993"></a><a name="p8682201993"></a></p>
    <p id="p11902194391011"><a name="p11902194391011"></a><a name="p11902194391011"></a></p>
    </td>
    </tr>
    <tr id="row6634254101816"><td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.5.1.1 "><p id="p1363485413187"><a name="p1363485413187"></a><a name="p1363485413187"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.5.1.2 "><p id="p463417547182"><a name="p463417547182"></a><a name="p463417547182"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.27202720272027%" headers="mcps1.1.5.1.3 "><p id="p7634195417180"><a name="p7634195417180"></a><a name="p7634195417180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.78337833783379%" headers="mcps1.1.5.1.4 "><p id="p176341254201810"><a name="p176341254201810"></a><a name="p176341254201810"></a>Resource ID</p>
    <p id="p57491711103514"><a name="p57491711103514"></a><a name="p57491711103514"></a>Obtain a resource ID:</p>
    <a name="ul969372310137"></a><a name="ul969372310137"></a><ul id="ul969372310137"><li>Add <strong id="b1046628401"><a name="b1046628401"></a><a name="b1046628401"></a>X-SMN-RESOURCEID-TYPE=name</strong> in the request header and set the resource ID to the topic name.</li><li>Call the <strong id="b84235270694340"><a name="b84235270694340"></a><a name="b84235270694340"></a>GetResourceInstances</strong> API to obtain the resource ID.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section2197105410186"></a>

-   Parameter description

    <a name="table4213165415189"></a>
    <table><thead align="left"><tr id="row16634145491814"><th class="cellrowborder" valign="top" width="16.88%" id="mcps1.1.5.1.1"><p id="p463435412187"><a name="p463435412187"></a><a name="p463435412187"></a><strong id="b492621386"><a name="b492621386"></a><a name="b492621386"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.68%" id="mcps1.1.5.1.2"><p id="p16634054131814"><a name="p16634054131814"></a><a name="p16634054131814"></a><strong id="b1873939549"><a name="b1873939549"></a><a name="b1873939549"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.78%" id="mcps1.1.5.1.3"><p id="p9634155414185"><a name="p9634155414185"></a><a name="p9634155414185"></a><strong id="b207078290"><a name="b207078290"></a><a name="b207078290"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.66%" id="mcps1.1.5.1.4"><p id="p2063413547181"><a name="p2063413547181"></a><a name="p2063413547181"></a><strong id="b674219474"><a name="b674219474"></a><a name="b674219474"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18634195431818"><td class="cellrowborder" valign="top" width="16.88%" headers="mcps1.1.5.1.1 "><p id="p156341354131810"><a name="p156341354131810"></a><a name="p156341354131810"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.1.5.1.2 "><p id="p763418543186"><a name="p763418543186"></a><a name="p763418543186"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.1.5.1.3 "><p id="p563413548183"><a name="p563413548183"></a><a name="p563413548183"></a>Resource_tag structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p7634654141810"><a name="p7634654141810"></a><a name="p7634654141810"></a>Tag list. For details, see <a href="#table1127111434346">Table 1</a>.</p>
    <p id="p14459433554"><a name="p14459433554"></a><a name="p14459433554"></a>When you delete tags, the tag structure cannot be missing, and the key cannot be left blank or be an empty string. The system does not check the character set when deleting a tag.</p>
    </td>
    </tr>
    <tr id="row1263445419182"><td class="cellrowborder" valign="top" width="16.88%" headers="mcps1.1.5.1.1 "><p id="p16341754191812"><a name="p16341754191812"></a><a name="p16341754191812"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.1.5.1.2 "><p id="p363415545188"><a name="p363415545188"></a><a name="p363415545188"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.1.5.1.3 "><p id="p176349545181"><a name="p176349545181"></a><a name="p176349545181"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p186342054101815"><a name="p186342054101815"></a><a name="p186342054101815"></a>Operation to be performed, which can be <strong id="b842352706101829"><a name="b842352706101829"></a><a name="b842352706101829"></a>create</strong> or <strong id="b842352706101833"><a name="b842352706101833"></a><a name="b842352706101833"></a>delete</strong></p>
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


-   Request example

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/{resource_type}/{resource_id}/tags/action
    ```


-   Request body

    Request body when  **action**  is set to  **create**

    ```
    {
        "action": "create",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key",
                "value": "value3"
            }
        ]
    }
    ```

    Request body when  **action**  is set to  **delete**

    ```
    {
        "action": "delete",
        "tags": [
            {
                 "key": "key1"
             },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## Response<a name="section112591544183"></a>

None

## Returned Value<a name="section10259185419185"></a>

See  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

