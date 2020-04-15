# Querying DeHs by Tag<a name="EN-US_TOPIC_0134153399"></a>

## Function<a name="section54478915181842"></a>

-   This API is used to filter DeHs by tag and return the list of all tags of a DeH.

-   Tag Management Service \(TMS\) uses this API to filter the DeHs.

## URI<a name="en-us_topic_0057972838_section58912114"></a>

POST /v1.0/\{project\_id\}/dedicated-host-tags/resource\_instances/action

[Table 1](#table291625114015)  describes the parameters.

**Table  1**  Parameters description

<a name="table291625114015"></a>
<table><thead align="left"><tr id="row291610574011"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1467218184410"><a name="p1467218184410"></a><a name="p1467218184410"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p0675111204414"><a name="p0675111204414"></a><a name="p0675111204414"></a><strong id="b16105191614456"><a name="b16105191614456"></a><a name="b16105191614456"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p69548610432"><a name="p69548610432"></a><a name="p69548610432"></a><strong id="b234225413538"><a name="b234225413538"></a><a name="b234225413538"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p19679111448"><a name="p19679111448"></a><a name="p19679111448"></a><strong id="b8423527069506"><a name="b8423527069506"></a><a name="b8423527069506"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row69161956409"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p126868117449"><a name="p126868117449"></a><a name="p126868117449"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1688101174411"><a name="p1688101174411"></a><a name="p1688101174411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p59527664313"><a name="p59527664313"></a><a name="p59527664313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1969317113442"><a name="p1969317113442"></a><a name="p1969317113442"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972838_section60446980"></a>

-   Request parameters

    <a name="table13359162912914"></a>
    <table><thead align="left"><tr id="row14654172910298"><th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.1"><p id="p8654729202919"><a name="p8654729202919"></a><a name="p8654729202919"></a><strong id="b1135875625411"><a name="b1135875625411"></a><a name="b1135875625411"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.09%" id="mcps1.1.5.1.2"><p id="p965422982911"><a name="p965422982911"></a><a name="p965422982911"></a><strong id="b10684014558"><a name="b10684014558"></a><a name="b10684014558"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.91%" id="mcps1.1.5.1.3"><p id="p16547295291"><a name="p16547295291"></a><a name="p16547295291"></a><strong id="b201916435511"><a name="b201916435511"></a><a name="b201916435511"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.1.5.1.4"><p id="p1165492982919"><a name="p1165492982919"></a><a name="p1165492982919"></a><strong id="b101721455554"><a name="b101721455554"></a><a name="b101721455554"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row186544299290"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p1165422910297"><a name="p1165422910297"></a><a name="p1165422910297"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p146541129142918"><a name="p146541129142918"></a><a name="p146541129142918"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p1065452992917"><a name="p1065452992917"></a><a name="p1065452992917"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p8654102912911"><a name="p8654102912911"></a><a name="p8654102912911"></a>Displays all DeHs with specified tags. For more information, see <a href="#table1646113155613">Table 2</a>.</p>
    <a name="ul2657192911299"></a><a name="ul2657192911299"></a><ul id="ul2657192911299"><li>A maximum of 10 keys are included. Each key can have a maximum of 10 values.</li><li>The structure body must be included.</li><li>The tag key cannot be left blank or set to an empty string.</li><li>A key must be unique.</li><li>Values of the same key must be unique.</li></ul>
    </td>
    </tr>
    <tr id="row10657102912295"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p565752911290"><a name="p565752911290"></a><a name="p565752911290"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p86571029162919"><a name="p86571029162919"></a><a name="p86571029162919"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p565712922910"><a name="p565712922910"></a><a name="p565712922910"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p1065712962916"><a name="p1065712962916"></a><a name="p1065712962916"></a>Displays the DeHs with none of specified tags.</p>
    <a name="ul1465712914296"></a><a name="ul1465712914296"></a><ul id="ul1465712914296"><li>A maximum of 10 keys are included. Each key can have a maximum of 10 values.</li><li>The structure body must be included.</li><li>The tag key cannot be left blank or set to an empty string.</li><li>Keys must be unique.</li><li>Values of the same key must be unique.</li></ul>
    </td>
    </tr>
    <tr id="row1265717299296"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p1065712298299"><a name="p1065712298299"></a><a name="p1065712298299"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p965742902916"><a name="p965742902916"></a><a name="p965742902916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p13657529162911"><a name="p13657529162911"></a><a name="p13657529162911"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p56571729102918"><a name="p56571729102918"></a><a name="p56571729102918"></a>Limits the maximum number of queried DeHs. The value cannot be a negative number. The maximum value is 1000.</p>
    <a name="ul965716295292"></a><a name="ul965716295292"></a><ul id="ul965716295292"><li>If the <strong id="b54610817215"><a name="b54610817215"></a><a name="b54610817215"></a>action</strong> value is <strong id="b74611882217"><a name="b74611882217"></a><a name="b74611882217"></a>count</strong>, this parameter is invalid.</li><li>If the <strong id="b5610131117213"><a name="b5610131117213"></a><a name="b5610131117213"></a>action</strong> value is <strong id="b1361118118211"><a name="b1361118118211"></a><a name="b1361118118211"></a>filter</strong>, the default value is <strong id="b16612011229"><a name="b16612011229"></a><a name="b16612011229"></a>1000</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row10657132918299"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p5657132914293"><a name="p5657132914293"></a><a name="p5657132914293"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p36571029192913"><a name="p36571029192913"></a><a name="p36571029192913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p146571329132916"><a name="p146571329132916"></a><a name="p146571329132916"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p5657102912292"><a name="p5657102912292"></a><a name="p5657102912292"></a>Specifies the index position. The query starts from the next piece of data indexed by this parameter. The value must be a non-negative number.</p>
    <p id="p1765792922910"><a name="p1765792922910"></a><a name="p1765792922910"></a>You do not need to specify this parameter when querying resources on the first page. When you query resources on subsequent pages, set the value of <strong id="b842352706101324"><a name="b842352706101324"></a><a name="b842352706101324"></a>offset</strong> to the location returned in the response body for the previous query.</p>
    <a name="ul7657129202910"></a><a name="ul7657129202910"></a><ul id="ul7657129202910"><li>If the <strong id="b98590351727"><a name="b98590351727"></a><a name="b98590351727"></a>action</strong> value is <strong id="b1485933512212"><a name="b1485933512212"></a><a name="b1485933512212"></a>count</strong>, this parameter is invalid.</li><li>If the <strong id="b6862103716213"><a name="b6862103716213"></a><a name="b6862103716213"></a>action</strong> value is <strong id="b78631637422"><a name="b78631637422"></a><a name="b78631637422"></a>filter</strong>, the default value is <strong id="b1686417371829"><a name="b1686417371829"></a><a name="b1686417371829"></a>0</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row86574293297"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p5657229102914"><a name="p5657229102914"></a><a name="p5657229102914"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p9657202932918"><a name="p9657202932918"></a><a name="p9657202932918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p14657182982917"><a name="p14657182982917"></a><a name="p14657182982917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p10657102910293"><a name="p10657102910293"></a><a name="p10657102910293"></a>Specifies the operation, which can be <strong id="b126481841128"><a name="b126481841128"></a><a name="b126481841128"></a>filter</strong> or <strong id="b1064918411217"><a name="b1064918411217"></a><a name="b1064918411217"></a>count</strong>.</p>
    <a name="ul86571294299"></a><a name="ul86571294299"></a><ul id="ul86571294299"><li><strong id="b1088116569219"><a name="b1088116569219"></a><a name="b1088116569219"></a>filter</strong>: Filters DeHs by tag and lists DeHs that meet the search criteria. Listed DeHs are queried by page.</li><li><strong id="b24628511466"><a name="b24628511466"></a><a name="b24628511466"></a>count</strong>: Searches for DeHs by tag and returns the number of DeHs that meet the search criteria.</li></ul>
    </td>
    </tr>
    <tr id="row10188191611019"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p118911161005"><a name="p118911161005"></a><a name="p118911161005"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p1518931619014"><a name="p1518931619014"></a><a name="p1518931619014"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p14189161613015"><a name="p14189161613015"></a><a name="p14189161613015"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p155851416541"><a name="p155851416541"></a><a name="p155851416541"></a>Includes any of the specified tags.</p>
    <a name="ul91311449544"></a><a name="ul91311449544"></a><ul id="ul91311449544"><li>This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing.</li><li>Each key must be unique, and cannot contain duplicate values.</li><li>The response returns resources containing the tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship.</li><li>If no tag filtering condition is specified, full data is returned.</li></ul>
    </td>
    </tr>
    <tr id="row594815819020"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p89483819014"><a name="p89483819014"></a><a name="p89483819014"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p4948281504"><a name="p4948281504"></a><a name="p4948281504"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p5948128606"><a name="p5948128606"></a><a name="p5948128606"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p1978512518555"><a name="p1978512518555"></a><a name="p1978512518555"></a>Excludes any of the specified tags.</p>
    <a name="ul16230187125514"></a><a name="ul16230187125514"></a><ul id="ul16230187125514"><li>This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing.</li><li>Each key must be unique, and cannot contain duplicate values.</li><li>The response returns resources containing no tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship.</li><li>If no tag filtering condition is specified, full data is returned.</li></ul>
    </td>
    </tr>
    <tr id="row7657829172918"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p13657529202918"><a name="p13657529202918"></a><a name="p13657529202918"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p1065742918299"><a name="p1065742918299"></a><a name="p1065742918299"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p165711297291"><a name="p165711297291"></a><a name="p165711297291"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p7657132982914"><a name="p7657132982914"></a><a name="p7657132982914"></a>Specifies the search field, which is used to search for DeHs by condition.</p>
    <p id="p065742922915"><a name="p065742922915"></a><a name="p065742922915"></a>Currently, only <strong id="b842352706154915"><a name="b842352706154915"></a><a name="b842352706154915"></a>resource_name</strong> can be used for search. For more information, see <a href="#table159211739175717">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **tag**  field description

    <a name="table1646113155613"></a>
    <table><thead align="left"><tr id="row3646181317563"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p193667812308"><a name="p193667812308"></a><a name="p193667812308"></a><strong id="b83821019171316"><a name="b83821019171316"></a><a name="b83821019171316"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p193660817301"><a name="p193660817301"></a><a name="p193660817301"></a><strong id="b529852415132"><a name="b529852415132"></a><a name="b529852415132"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p1510994524610"><a name="p1510994524610"></a><a name="p1510994524610"></a><strong id="b106061225121312"><a name="b106061225121312"></a><a name="b106061225121312"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p936614813309"><a name="p936614813309"></a><a name="p936614813309"></a><strong id="b1574752721310"><a name="b1574752721310"></a><a name="b1574752721310"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row764691365618"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p193669863019"><a name="p193669863019"></a><a name="p193669863019"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p13686816306"><a name="p13686816306"></a><a name="p13686816306"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p20109164504610"><a name="p20109164504610"></a><a name="p20109164504610"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p33688823011"><a name="p33688823011"></a><a name="p33688823011"></a>Specifies the tag key.</p>
    <a name="ul1336819883017"></a><a name="ul1336819883017"></a><ul id="ul1336819883017"><li>It contains a maximum of 127 Unicode characters.</li><li>This field cannot be left blank.</li></ul>
    </td>
    </tr>
    <tr id="row5646191345618"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p336828123019"><a name="p336828123019"></a><a name="p336828123019"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p2368187304"><a name="p2368187304"></a><a name="p2368187304"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p16841445164614"><a name="p16841445164614"></a><a name="p16841445164614"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p113681981304"><a name="p113681981304"></a><a name="p113681981304"></a>Specifies the tag values.</p>
    <a name="ul1436815817303"></a><a name="ul1436815817303"></a><ul id="ul1436815817303"><li>Each tag contains a maximum of 10 values.</li><li>Values of the same tag must be unique.</li><li>Each value can contain a maximum of 255 Unicode characters.</li><li>If this parameter is not specified, any value can be used.</li><li>The resources containing one or more values listed in <strong id="b166801975155"><a name="b166801975155"></a><a name="b166801975155"></a>values</strong> will be found and displayed.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **match**  field description

    <a name="table159211739175717"></a>
    <table><thead align="left"><tr id="row11922039105715"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p10699148114717"><a name="p10699148114717"></a><a name="p10699148114717"></a><strong id="b17356119181512"><a name="b17356119181512"></a><a name="b17356119181512"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p197027814717"><a name="p197027814717"></a><a name="p197027814717"></a><strong id="b195891420111517"><a name="b195891420111517"></a><a name="b195891420111517"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.3"><p id="p870510824713"><a name="p870510824713"></a><a name="p870510824713"></a><strong id="b6605821181515"><a name="b6605821181515"></a><a name="b6605821181515"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.5.1.4"><p id="p157094824715"><a name="p157094824715"></a><a name="p157094824715"></a><strong id="b8606202213154"><a name="b8606202213154"></a><a name="b8606202213154"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14922123918578"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p3434656203016"><a name="p3434656203016"></a><a name="p3434656203016"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p1434155619301"><a name="p1434155619301"></a><a name="p1434155619301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="p754201411474"><a name="p754201411474"></a><a name="p754201411474"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p1643415618307"><a name="p1643415618307"></a><a name="p1643415618307"></a>Specifies the key parameter to be matched.</p>
    <a name="ul1043435643020"></a><a name="ul1043435643020"></a><ul id="ul1043435643020"><li>The key must be unique, and the value is used for matching.</li><li>The <strong id="b10991315962239"><a name="b10991315962239"></a><a name="b10991315962239"></a>key</strong> field is a fixed dictionary value.</li><li>This field cannot be left blank.</li></ul>
    <div class="note" id="note436011568305"><a name="note436011568305"></a><a name="note436011568305"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p543675653013"><a name="p543675653013"></a><a name="p543675653013"></a>The parameter value can only be <strong id="b842352706172034"><a name="b842352706172034"></a><a name="b842352706172034"></a>resource_name</strong>, which is the DeH name.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row99221939105717"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1143645613018"><a name="p1143645613018"></a><a name="p1143645613018"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p10436956153014"><a name="p10436956153014"></a><a name="p10436956153014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="p1853161464718"><a name="p1853161464718"></a><a name="p1853161464718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p1443615562303"><a name="p1443615562303"></a><a name="p1443615562303"></a>Specifies the tag value.</p>
    <a name="ul1643610561302"></a><a name="ul1643610561302"></a><ul id="ul1643610561302"><li>Each value can contain a maximum of 255 Unicode characters. </li><li>This field cannot be left blank.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-host-tags/resource_instances/action 
    ```

    ```
    { 
        "offset": "0",
        "limit": "100",
        "action": "filter",
        "matches": [
            {
                "key": "resource_name",
                "value": "resource1"
            }
        ],
        "tags": [
            {
                "key": "key1",
                "values": ["value1"]
            }
        ]
    }
    ```


## Response<a name="section40529449"></a>

-   Response parameters

    <a name="table112392047203218"></a>
    <table><thead align="left"><tr id="row1632611475324"><th class="cellrowborder" valign="top" width="25.290000000000003%" id="mcps1.1.4.1.1"><p id="p8326164713219"><a name="p8326164713219"></a><a name="p8326164713219"></a><strong id="b8171155141617"><a name="b8171155141617"></a><a name="b8171155141617"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.64%" id="mcps1.1.4.1.2"><p id="p1732694716321"><a name="p1732694716321"></a><a name="p1732694716321"></a><strong id="b6599356191615"><a name="b6599356191615"></a><a name="b6599356191615"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.07%" id="mcps1.1.4.1.3"><p id="p1732654715328"><a name="p1732654715328"></a><a name="p1732654715328"></a><strong id="b197855572166"><a name="b197855572166"></a><a name="b197855572166"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63267477328"><td class="cellrowborder" valign="top" width="25.290000000000003%" headers="mcps1.1.4.1.1 "><p id="p1326124710326"><a name="p1326124710326"></a><a name="p1326124710326"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.64%" headers="mcps1.1.4.1.2 "><p id="p16326164723215"><a name="p16326164723215"></a><a name="p16326164723215"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.07%" headers="mcps1.1.4.1.3 "><p id="p1932624763211"><a name="p1932624763211"></a><a name="p1932624763211"></a>Specifies the returned DeH list. For details, see <a href="#table924792920312">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row123264478326"><td class="cellrowborder" valign="top" width="25.290000000000003%" headers="mcps1.1.4.1.1 "><p id="p43261647113215"><a name="p43261647113215"></a><a name="p43261647113215"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.64%" headers="mcps1.1.4.1.2 "><p id="p6326947193210"><a name="p6326947193210"></a><a name="p6326947193210"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.07%" headers="mcps1.1.4.1.3 "><p id="p19326184723214"><a name="p19326184723214"></a><a name="p19326184723214"></a>Specifies the total number of resources.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **resource**  field

    <a name="table924792920312"></a>
    <table><thead align="left"><tr id="row724982918315"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p724715654719"><a name="p724715654719"></a><a name="p724715654719"></a><strong id="b1281814112174"><a name="b1281814112174"></a><a name="b1281814112174"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.2"><p id="p1724985617478"><a name="p1724985617478"></a><a name="p1724985617478"></a><strong id="b1746134361713"><a name="b1746134361713"></a><a name="b1746134361713"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p12251105611474"><a name="p12251105611474"></a><a name="p12251105611474"></a><strong id="b849724413179"><a name="b849724413179"></a><a name="b849724413179"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1249182913319"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p14679356153211"><a name="p14679356153211"></a><a name="p14679356153211"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p667935693210"><a name="p667935693210"></a><a name="p667935693210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p16679175693210"><a name="p16679175693210"></a><a name="p16679175693210"></a>Specifies the DeH ID.</p>
    </td>
    </tr>
    <tr id="row192492291539"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11679165693220"><a name="p11679165693220"></a><a name="p11679165693220"></a>resouce_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p167935663210"><a name="p167935663210"></a><a name="p167935663210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p9217447140"><a name="p9217447140"></a><a name="p9217447140"></a>Specifies the DeH details.</p>
    <p id="p156791256163212"><a name="p156791256163212"></a><a name="p156791256163212"></a>This field is used for future extension and is left empty by default.</p>
    </td>
    </tr>
    <tr id="row202492291131"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p16792567326"><a name="p16792567326"></a><a name="p16792567326"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p3679556183215"><a name="p3679556183215"></a><a name="p3679556183215"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p967975614321"><a name="p967975614321"></a><a name="p967975614321"></a>Specifies the tag list.</p>
    </td>
    </tr>
    <tr id="row724992916316"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p206792563325"><a name="p206792563325"></a><a name="p206792563325"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p1167917566327"><a name="p1167917566327"></a><a name="p1167917566327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p767911567325"><a name="p767911567325"></a><a name="p767911567325"></a>Specifies the resource name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **resource\_tag**  field description

    <a name="table145631502043"></a>
    <table><thead align="left"><tr id="row1556511020418"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="p1463712019481"><a name="p1463712019481"></a><a name="p1463712019481"></a><strong id="b19674154816195"><a name="b19674154816195"></a><a name="b19674154816195"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.282828282828287%" id="mcps1.2.4.1.2"><p id="p264150164815"><a name="p264150164815"></a><a name="p264150164815"></a><strong id="b6715125131917"><a name="b6715125131917"></a><a name="b6715125131917"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.4.1.3"><p id="p964314013482"><a name="p964314013482"></a><a name="p964314013482"></a><strong id="b5321553151912"><a name="b5321553151912"></a><a name="b5321553151912"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row956519014410"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p1842104620338"><a name="p1842104620338"></a><a name="p1842104620338"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.2.4.1.2 "><p id="p1842546193319"><a name="p1842546193319"></a><a name="p1842546193319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.4.1.3 "><p id="p12421546203313"><a name="p12421546203313"></a><a name="p12421546203313"></a>Specifies the tag key.</p>
    <a name="ul34244618336"></a><a name="ul34244618336"></a><ul id="ul34244618336"><li>It contains a maximum of 36 Unicode characters.</li><li>This field cannot be left blank.</li><li>It cannot contain the following ASCII characters: =*&lt;&gt;\|/,</li></ul>
    </td>
    </tr>
    <tr id="row125651505416"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p184214613310"><a name="p184214613310"></a><a name="p184214613310"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.2.4.1.2 "><p id="p15421446183319"><a name="p15421446183319"></a><a name="p15421446183319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.4.1.3 "><p id="p18421146123310"><a name="p18421146123310"></a><a name="p18421146123310"></a>Specifies the tag value.</p>
    <a name="ul18425463332"></a><a name="ul18425463332"></a><ul id="ul18425463332"><li>Each value contains a maximum of 43 Unicode characters.</li><li>This field can be left blank.</li><li>It cannot contain the following ASCII characters: =*&lt;&gt;\|/,</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    Response body when  **action**  is set to  **filter**

    ```
    {
        "resources": [
            {
                "resource_detail": null,
                "resource_id": "cdfs_cefs_wesas_12_dsad",
                "resource_name": "resource1",
                "tags": [
                    {
                        "key": "key1",
                        "value": "value1"
                    }
                ]
            }
        ],
        "total_count": 1
    }
    ```

    Response body when  **action**  is set to  **count**

    ```
    {
        "total_count": 100
    }
    ```


## Status Code<a name="section9992350"></a>

See  [Status Codes](status-codes.md).

