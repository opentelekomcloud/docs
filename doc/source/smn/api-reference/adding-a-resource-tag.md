# Adding a Resource Tag<a name="smn_api_56003"></a>

## Description<a name="section6275354111818"></a>

-   API name

    CreateResourceTag


-   Function

    You can add a maximum of 10 tags to a resource.

    The API is idempotent. If a to-be-created tag has the same key as an existing tag, the tag will be created and overwrite the existing one.


## URI<a name="section12757544187"></a>

-   URI format

    POST /v2/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags

-   Parameter description

    <a name="table1029119541182"></a>
    <table><thead align="left"><tr id="row6634135420184"><th class="cellrowborder" valign="top" width="17.738226177382263%" id="mcps1.1.5.1.1"><p id="p0650125431810"><a name="p0650125431810"></a><a name="p0650125431810"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.357664233576642%" id="mcps1.1.5.1.2"><p id="p1465005418189"><a name="p1465005418189"></a><a name="p1465005418189"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.027397260273972%" id="mcps1.1.5.1.3"><p id="p0650175419188"><a name="p0650175419188"></a><a name="p0650175419188"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.87671232876712%" id="mcps1.1.5.1.4"><p id="p156507545182"><a name="p156507545182"></a><a name="p156507545182"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4650165421816"><td class="cellrowborder" valign="top" width="17.738226177382263%" headers="mcps1.1.5.1.1 "><p id="p3650854151810"><a name="p3650854151810"></a><a name="p3650854151810"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.357664233576642%" headers="mcps1.1.5.1.2 "><p id="p1365025412188"><a name="p1365025412188"></a><a name="p1365025412188"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.027397260273972%" headers="mcps1.1.5.1.3 "><p id="p186502054111811"><a name="p186502054111811"></a><a name="p186502054111811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87671232876712%" headers="mcps1.1.5.1.4 "><p id="p1665018541188"><a name="p1665018541188"></a><a name="p1665018541188"></a>Project ID</p>
    <p id="p118812918506"><a name="p118812918506"></a><a name="p118812918506"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row19650165415182"><td class="cellrowborder" valign="top" width="17.738226177382263%" headers="mcps1.1.5.1.1 "><p id="p99531421797"><a name="p99531421797"></a><a name="p99531421797"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.357664233576642%" headers="mcps1.1.5.1.2 "><p id="p1495310421799"><a name="p1495310421799"></a><a name="p1495310421799"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.027397260273972%" headers="mcps1.1.5.1.3 "><p id="p149531342296"><a name="p149531342296"></a><a name="p149531342296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87671232876712%" headers="mcps1.1.5.1.4 "><p id="p52661238184213"><a name="p52661238184213"></a><a name="p52661238184213"></a>Resource type</p>
    <p id="p278251314214"><a name="p278251314214"></a><a name="p278251314214"></a>The value can be the following:</p>
    <p id="p14550953686"><a name="p14550953686"></a><a name="p14550953686"></a><strong id="b79113111105"><a name="b79113111105"></a><a name="b79113111105"></a>smn_topic</strong>: topic</p>
    <p id="p8682201993"><a name="p8682201993"></a><a name="p8682201993"></a></p>
    <p id="p10462259131014"><a name="p10462259131014"></a><a name="p10462259131014"></a></p>
    </td>
    </tr>
    <tr id="row0650054191817"><td class="cellrowborder" valign="top" width="17.738226177382263%" headers="mcps1.1.5.1.1 "><p id="p1363485413187"><a name="p1363485413187"></a><a name="p1363485413187"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.357664233576642%" headers="mcps1.1.5.1.2 "><p id="p463417547182"><a name="p463417547182"></a><a name="p463417547182"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.027397260273972%" headers="mcps1.1.5.1.3 "><p id="p7634195417180"><a name="p7634195417180"></a><a name="p7634195417180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87671232876712%" headers="mcps1.1.5.1.4 "><p id="p176341254201810"><a name="p176341254201810"></a><a name="p176341254201810"></a>Resource ID</p>
    <p id="p57491711103514"><a name="p57491711103514"></a><a name="p57491711103514"></a>Obtain a resource ID:</p>
    <a name="ul111761720155610"></a><a name="ul111761720155610"></a><ul id="ul111761720155610"><li>Add <strong id="smn_api_56002_b1046628401"><a name="smn_api_56002_b1046628401"></a><a name="smn_api_56002_b1046628401"></a>X-SMN-RESOURCEID-TYPE=name</strong> in the request header and set the resource ID to the topic name.</li><li>Call the <strong id="smn_api_56002_b84235270694340"><a name="smn_api_56002_b84235270694340"></a><a name="smn_api_56002_b84235270694340"></a>GetResourceInstances</strong> API to obtain the resource ID.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section15306154161813"></a>

-   Parameter description

    <a name="table2306754131811"></a>
    <table><thead align="left"><tr id="row10650115416183"><th class="cellrowborder" valign="top" width="16.13838616138386%" id="mcps1.1.5.1.1"><p id="p2650155410184"><a name="p2650155410184"></a><a name="p2650155410184"></a><strong id="b558166876"><a name="b558166876"></a><a name="b558166876"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.837816218378165%" id="mcps1.1.5.1.2"><p id="p3650185481810"><a name="p3650185481810"></a><a name="p3650185481810"></a><strong id="b286245577"><a name="b286245577"></a><a name="b286245577"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.45835416458354%" id="mcps1.1.5.1.3"><p id="p16501254141811"><a name="p16501254141811"></a><a name="p16501254141811"></a><strong id="b117873465"><a name="b117873465"></a><a name="b117873465"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.56544345565444%" id="mcps1.1.5.1.4"><p id="p1765017544189"><a name="p1765017544189"></a><a name="p1765017544189"></a><strong id="b1440922626"><a name="b1440922626"></a><a name="b1440922626"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row465019548182"><td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.1.5.1.1 "><p id="p26501954141814"><a name="p26501954141814"></a><a name="p26501954141814"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.837816218378165%" headers="mcps1.1.5.1.2 "><p id="p13650175411819"><a name="p13650175411819"></a><a name="p13650175411819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.45835416458354%" headers="mcps1.1.5.1.3 "><p id="p12650654151819"><a name="p12650654151819"></a><a name="p12650654151819"></a>Resource tag structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.56544345565444%" headers="mcps1.1.5.1.4 "><p id="p8650554201817"><a name="p8650554201817"></a><a name="p8650554201817"></a>Resource tag to be added. For details, see <a href="#table1127111434346">Table 1</a>.</p>
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
    POST https://{SMN_Endpoint}/v2/{project_id}/{resource_type}/{resource_id}/tags
    ```


-   Example request

    ```
    {
         "tag":
         {
            "key":"DEV",
            "value":"DEV1"
         }
    }
    ```


## Response<a name="section12429402325"></a>

None

## Returned Value<a name="section11338754191819"></a>

See  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

