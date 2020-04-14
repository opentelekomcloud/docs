# Querying Details About a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158707"></a>

## Function<a name="section11242227"></a>

This API is used to query details about a BMS based on the BMS ID.

## URI<a name="section34071180"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}

[Table 1](#table17908225144614)  lists the parameters.

**Table  1**  Parameter description

<a name="table17908225144614"></a>
<table><thead align="left"><tr id="row169095255463"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p16058544"><a name="p16058544"></a><a name="p16058544"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p25673664"><a name="p25673664"></a><a name="p25673664"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p66300913"><a name="p66300913"></a><a name="p66300913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19097252465"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p637140"><a name="p637140"></a><a name="p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51608407"><a name="p51608407"></a><a name="p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19531418"><a name="p19531418"></a><a name="p19531418"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row1790915256462"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11324657"><a name="p11324657"></a><a name="p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44882061"><a name="p44882061"></a><a name="p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11568292"><a name="p11568292"></a><a name="p11568292"></a>Specifies the <span id="text188616309102"><a name="text188616309102"></a><a name="text188616309102"></a>BMS</span><span id="text68871630181017"><a name="text68871630181017"></a><a name="text68871630181017"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section38205169"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/9ab74d89-61e7-4259-8546-465fdebe4944
    ```


## Response Message<a name="section8302201"></a>

-   Response parameters

    <a name="table44736746"></a>
    <table><thead align="left"><tr id="row8242429"><th class="cellrowborder" valign="top" width="22.84228422842284%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.872587258725872%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.28512851285129%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18745119"><td class="cellrowborder" valign="top" width="22.84228422842284%" headers="mcps1.1.4.1.1 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>server</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.872587258725872%" headers="mcps1.1.4.1.2 "><p id="p17222571164727"><a name="p17222571164727"></a><a name="p17222571164727"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.28512851285129%" headers="mcps1.1.4.1.3 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Specifies <span id="text22489319112"><a name="text22489319112"></a><a name="text22489319112"></a>BMS</span><span id="text4250438110"><a name="text4250438110"></a><a name="text4250438110"></a></span> information. For details, see <a href="#table6149040">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **server**  field data structure description

    <a name="table6149040"></a>
    <table><thead align="left"><tr id="row9499663"><th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.1"><p id="p937538164712"><a name="p937538164712"></a><a name="p937538164712"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.94%" id="mcps1.2.4.1.2"><p id="p1643193811475"><a name="p1643193811475"></a><a name="p1643193811475"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.07000000000001%" id="mcps1.2.4.1.3"><p id="p15393816472"><a name="p15393816472"></a><a name="p15393816472"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30856945"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p16384644"><a name="p16384644"></a><a name="p16384644"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p58359570"><a name="p58359570"></a><a name="p58359570"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p29504734"><a name="p29504734"></a><a name="p29504734"></a>Specifies the <span id="text11975191216114"><a name="text11975191216114"></a><a name="text11975191216114"></a>BMS</span><span id="text1697711129116"><a name="text1697711129116"></a><a name="text1697711129116"></a></span> name.</p>
    </td>
    </tr>
    <tr id="row64216018"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p34114937"><a name="p34114937"></a><a name="p34114937"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p20045150"><a name="p20045150"></a><a name="p20045150"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p13044459"><a name="p13044459"></a><a name="p13044459"></a>Specifies the unique ID of the <span id="text16163161417111"><a name="text16163161417111"></a><a name="text16163161417111"></a>BMS</span><span id="text6164141461114"><a name="text6164141461114"></a><a name="text6164141461114"></a></span>.</p>
    </td>
    </tr>
    <tr id="row50291273"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p47061312"><a name="p47061312"></a><a name="p47061312"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p1387343"><a name="p1387343"></a><a name="p1387343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p45265976"><a name="p45265976"></a><a name="p45265976"></a>Specifies the <span id="text18356141519118"><a name="text18356141519118"></a><a name="text18356141519118"></a>BMS</span><span id="text43576157111"><a name="text43576157111"></a><a name="text43576157111"></a></span> status.</p>
    <p id="p1210441214413"><a name="p1210441214413"></a><a name="p1210441214413"></a>Value range:</p>
    <a name="ul65801951484"></a><a name="ul65801951484"></a><ul id="ul65801951484"><li><strong id="b1791661112227"><a name="b1791661112227"></a><a name="b1791661112227"></a>ACTIVE</strong>: Running, Stopping, Deleting</li><li><strong id="b598814192210"><a name="b598814192210"></a><a name="b598814192210"></a>BUILD</strong>: Creating</li><li><strong id="b1189210154224"><a name="b1189210154224"></a><a name="b1189210154224"></a>ERROR</strong>: Faulty</li><li><strong id="b164291811226"><a name="b164291811226"></a><a name="b164291811226"></a>HARD_REBOOT</strong>: Forcibly Restarting</li><li><strong id="b1133072018227"><a name="b1133072018227"></a><a name="b1133072018227"></a>REBOOT</strong>: Restarting</li><li><strong id="b15250154172510"><a name="b15250154172510"></a><a name="b15250154172510"></a>SHUTOFF</strong>: Stopped, Starting, Deleting, Rebuilding</li></ul>
    </td>
    </tr>
    <tr id="row4740601"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p48444361"><a name="p48444361"></a><a name="p48444361"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p15873654"><a name="p15873654"></a><a name="p15873654"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p10697636"><a name="p10697636"></a><a name="p10697636"></a>Specifies the time when the <span id="text5512016111111"><a name="text5512016111111"></a><a name="text5512016111111"></a>BMS</span><span id="text3513131620116"><a name="text3513131620116"></a><a name="text3513131620116"></a></span> was created.</p>
    <p id="p68414410213"><a name="p68414410213"></a><a name="p68414410213"></a>The timestamp format is YYYY-MM-DDTHH:MM:SSZ (ISO 8601), for example, 2019-05-22T03:30:52Z.</p>
    </td>
    </tr>
    <tr id="row29169865"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p13948877"><a name="p13948877"></a><a name="p13948877"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p49200685"><a name="p49200685"></a><a name="p49200685"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p25832538"><a name="p25832538"></a><a name="p25832538"></a>Specifies the time when the <span id="text156553172112"><a name="text156553172112"></a><a name="text156553172112"></a>BMS</span><span id="text1165621717118"><a name="text1165621717118"></a><a name="text1165621717118"></a></span> was last updated.</p>
    <p id="p136002456210"><a name="p136002456210"></a><a name="p136002456210"></a>The timestamp format is YYYY-MM-DDTHH:MM:SSZ (ISO 8601), for example, 2019-05-22T04:30:52Z.</p>
    </td>
    </tr>
    <tr id="row31166252"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p41438477"><a name="p41438477"></a><a name="p41438477"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p19839955"><a name="p19839955"></a><a name="p19839955"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p34922074"><a name="p34922074"></a><a name="p34922074"></a>Specifies the <span id="text281721971116"><a name="text281721971116"></a><a name="text281721971116"></a>BMS</span><span id="text1581841941117"><a name="text1581841941117"></a><a name="text1581841941117"></a></span> flavor. For details, see <a href="#table19588408">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row45863212"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p23932707"><a name="p23932707"></a><a name="p23932707"></a>image</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p54863279"><a name="p54863279"></a><a name="p54863279"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p65556790"><a name="p65556790"></a><a name="p65556790"></a>Specifies the <span id="text3649192212112"><a name="text3649192212112"></a><a name="text3649192212112"></a>BMS</span><span id="text116491622111115"><a name="text116491622111115"></a><a name="text116491622111115"></a></span> image. For details, see <a href="#table1258047620856">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row53140205"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p9389347"><a name="p9389347"></a><a name="p9389347"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p64678211"><a name="p64678211"></a><a name="p64678211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p4443775"><a name="p4443775"></a><a name="p4443775"></a>Specifies the ID of the tenant owning the <span id="text2081565516571"><a name="text2081565516571"></a><a name="text2081565516571"></a>BMS</span><span id="text6815185511572"><a name="text6815185511572"></a><a name="text6815185511572"></a></span>. The value is in UUID format.</p>
    <p id="p3869154710124"><a name="p3869154710124"></a><a name="p3869154710124"></a>This parameter specifies the same meaning as <strong id="b77201547172520"><a name="b77201547172520"></a><a name="b77201547172520"></a>project_id</strong>.</p>
    </td>
    </tr>
    <tr id="row15792483165644"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p4122771165644"><a name="p4122771165644"></a><a name="p4122771165644"></a>key_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p65509052165644"><a name="p65509052165644"></a><a name="p65509052165644"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p4632965165644"><a name="p4632965165644"></a><a name="p4632965165644"></a>Specifies the SSH key name.</p>
    </td>
    </tr>
    <tr id="row39993975"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p18286572"><a name="p18286572"></a><a name="p18286572"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p54663960"><a name="p54663960"></a><a name="p54663960"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p65704606"><a name="p65704606"></a><a name="p65704606"></a>Specifies the ID of the user to which the <span id="text209594671212"><a name="text209594671212"></a><a name="text209594671212"></a>BMS</span><span id="text18960262121"><a name="text18960262121"></a><a name="text18960262121"></a></span> belongs.</p>
    </td>
    </tr>
    <tr id="row54470546"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p50038096"><a name="p50038096"></a><a name="p50038096"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p3388666"><a name="p3388666"></a><a name="p3388666"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p54418662"><a name="p54418662"></a><a name="p54418662"></a>Specifies the <span id="text887243121217"><a name="text887243121217"></a><a name="text887243121217"></a>BMS</span><span id="text78731931151214"><a name="text78731931151214"></a><a name="text78731931151214"></a></span> metadata. For details, see <a href="#table2549048917552">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row20005910"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p9865986"><a name="p9865986"></a><a name="p9865986"></a>hostId</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p37794593"><a name="p37794593"></a><a name="p37794593"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p41463203"><a name="p41463203"></a><a name="p41463203"></a>Specifies the host ID of the <span id="text6635143218121"><a name="text6635143218121"></a><a name="text6635143218121"></a>BMS</span><span id="text8636203231219"><a name="text8636203231219"></a><a name="text8636203231219"></a></span>.</p>
    </td>
    </tr>
    <tr id="row37624514"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p27686757"><a name="p27686757"></a><a name="p27686757"></a>addresses</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p56232959"><a name="p56232959"></a><a name="p56232959"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p57420266"><a name="p57420266"></a><a name="p57420266"></a>Specifies <span id="text10701234151220"><a name="text10701234151220"></a><a name="text10701234151220"></a>BMS</span><span id="text97021334101217"><a name="text97021334101217"></a><a name="text97021334101217"></a></span> network addresses. For details, see <a href="#table3730161">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row61793156165818"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p39189735165818"><a name="p39189735165818"></a><a name="p39189735165818"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p20251975165818"><a name="p20251975165818"></a><a name="p20251975165818"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p29797259165818"><a name="p29797259165818"></a><a name="p29797259165818"></a>Specifies the security groups to which the <span id="text3566113731211"><a name="text3566113731211"></a><a name="text3566113731211"></a>BMS</span><span id="text175678373128"><a name="text175678373128"></a><a name="text175678373128"></a></span> belongs. For details, see <a href="#table761507165933">Table 9</a>.</p>
    </td>
    </tr>
    <tr id="row47020346"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p50551688"><a name="p50551688"></a><a name="p50551688"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p17625551"><a name="p17625551"></a><a name="p17625551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p31233872"><a name="p31233872"></a><a name="p31233872"></a>Specifies shortcut links of the <span id="text1182254791217"><a name="text1182254791217"></a><a name="text1182254791217"></a>BMS</span><span id="text108232047101214"><a name="text108232047101214"></a><a name="text108232047101214"></a></span>. For details, see <a href="#table16539321">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row707018122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p38394472122520"><a name="p38394472122520"></a><a name="p38394472122520"></a>OS-DCF:diskConfig</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p22944523122520"><a name="p22944523122520"></a><a name="p22944523122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p46567083122520"><a name="p46567083122520"></a><a name="p46567083122520"></a>Specifies the disk configuration method. This is an extended attribute. The value can be:</p>
    <a name="ul63811370174827"></a><a name="ul63811370174827"></a><ul id="ul63811370174827"><li><strong id="en-us_topic_0113746489_b842352706201852"><a name="en-us_topic_0113746489_b842352706201852"></a><a name="en-us_topic_0113746489_b842352706201852"></a>MANUAL</strong>: The API uses the partitioning scheme in the image and the file system to create a <span id="en-us_topic_0113746489_text5742455133714"><a name="en-us_topic_0113746489_text5742455133714"></a><a name="en-us_topic_0113746489_text5742455133714"></a>BMS</span><span id="en-us_topic_0113746489_text674310553373"><a name="en-us_topic_0113746489_text674310553373"></a><a name="en-us_topic_0113746489_text674310553373"></a></span>. If the target flavor has a large disk, the API does not partition the remaining disk space.</li><li><strong id="en-us_topic_0113746489_b11108728193415"><a name="en-us_topic_0113746489_b11108728193415"></a><a name="en-us_topic_0113746489_b11108728193415"></a>AUTO</strong>: The API uses a single partition with the same size as the disk of the target flavor to create a <span id="en-us_topic_0113746489_text1759675920373"><a name="en-us_topic_0113746489_text1759675920373"></a><a name="en-us_topic_0113746489_text1759675920373"></a>BMS</span><span id="en-us_topic_0113746489_text1159611597371"><a name="en-us_topic_0113746489_text1159611597371"></a><a name="en-us_topic_0113746489_text1159611597371"></a></span>. The API automatically adjusts the file system to adapt to the entire partition.</li></ul>
    </td>
    </tr>
    <tr id="row44817800122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p57427370122520"><a name="p57427370122520"></a><a name="p57427370122520"></a>OS-EXT-AZ:availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p21105408122520"><a name="p21105408122520"></a><a name="p21105408122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p31816494122520"><a name="p31816494122520"></a><a name="p31816494122520"></a>Specifies the AZ where the <span id="text13387111141314"><a name="text13387111141314"></a><a name="text13387111141314"></a>BMS</span><span id="text838819115133"><a name="text838819115133"></a><a name="text838819115133"></a></span> is located.</p>
    </td>
    </tr>
    <tr id="row42807035122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p873534122520"><a name="p873534122520"></a><a name="p873534122520"></a>OS-EXT-SRV-ATTR:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p3647431122520"><a name="p3647431122520"></a><a name="p3647431122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p27006529122520"><a name="p27006529122520"></a><a name="p27006529122520"></a>Specifies the host name of the <span id="text253316205586"><a name="text253316205586"></a><a name="text253316205586"></a>BMS</span><span id="text1653362075817"><a name="text1653362075817"></a><a name="text1653362075817"></a></span>. This is an extended attribute.</p>
    </td>
    </tr>
    <tr id="row27125958122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p24863094122520"><a name="p24863094122520"></a><a name="p24863094122520"></a>OS-EXT-SRV-ATTR:hypervisor_hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p644704122520"><a name="p644704122520"></a><a name="p644704122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p52221046122520"><a name="p52221046122520"></a><a name="p52221046122520"></a>Specifies the name of a host on the hypervisor. This is an extended attribute provided by the Nova virt driver.</p>
    </td>
    </tr>
    <tr id="row62666318122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p18417330122520"><a name="p18417330122520"></a><a name="p18417330122520"></a>OS-EXT-SRV-ATTR:instance_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p15408791122520"><a name="p15408791122520"></a><a name="p15408791122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p40152581122520"><a name="p40152581122520"></a><a name="p40152581122520"></a>Specifies the <span id="text47582222585"><a name="text47582222585"></a><a name="text47582222585"></a>BMS</span><span id="text19758102245818"><a name="text19758102245818"></a><a name="text19758102245818"></a></span> alias. This is an extended attribute.</p>
    </td>
    </tr>
    <tr id="row59158707122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p11766971122520"><a name="p11766971122520"></a><a name="p11766971122520"></a>OS-EXT-STS:power_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p13600613122520"><a name="p13600613122520"></a><a name="p13600613122520"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p27907859122520"><a name="p27907859122520"></a><a name="p27907859122520"></a>Specifies the power status of the <span id="text1544216248585"><a name="text1544216248585"></a><a name="text1544216248585"></a>BMS</span><span id="text4442324125810"><a name="text4442324125810"></a><a name="text4442324125810"></a></span>. This is an extended attribute.</p>
    <p id="p18973135462"><a name="p18973135462"></a><a name="p18973135462"></a>Options: 0, 1, 2, 3, and 4</p>
    <a name="ul934453312193"></a><a name="ul934453312193"></a><ul id="ul934453312193"><li><strong id="b842352706204759"><a name="b842352706204759"></a><a name="b842352706204759"></a>0</strong>: pending</li><li><strong id="b84235270620489"><a name="b84235270620489"></a><a name="b84235270620489"></a>1</strong>: running</li><li><strong id="b842352706204817"><a name="b842352706204817"></a><a name="b842352706204817"></a>2</strong>: paused</li><li><strong id="b842352706204825"><a name="b842352706204825"></a><a name="b842352706204825"></a>3</strong>: shutdown</li><li><strong id="b842352706204833"><a name="b842352706204833"></a><a name="b842352706204833"></a>4</strong>: crashed</li></ul>
    </td>
    </tr>
    <tr id="row28942811122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p10843807122520"><a name="p10843807122520"></a><a name="p10843807122520"></a>OS-EXT-STS:task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p5933192122520"><a name="p5933192122520"></a><a name="p5933192122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p10826513122520"><a name="p10826513122520"></a><a name="p10826513122520"></a>Specifies the task status of the <span id="text1413912393151"><a name="text1413912393151"></a><a name="text1413912393151"></a>BMS</span><span id="text2139539201519"><a name="text2139539201519"></a><a name="text2139539201519"></a></span>. This is an extended attribute.</p>
    <p id="p2461911154718"><a name="p2461911154718"></a><a name="p2461911154718"></a>Value range:</p>
    <a name="ul6637113412578"></a><a name="ul6637113412578"></a><ul id="ul6637113412578"><li><strong id="en-us_topic_0113746489_b10931636133810"><a name="en-us_topic_0113746489_b10931636133810"></a><a name="en-us_topic_0113746489_b10931636133810"></a>rebooting</strong>: The BMS is being restarted.</li><li><strong id="en-us_topic_0113746489_b103981113181314"><a name="en-us_topic_0113746489_b103981113181314"></a><a name="en-us_topic_0113746489_b103981113181314"></a>reboot_started</strong>: The BMS is normally restarted.</li><li><strong id="en-us_topic_0113746489_b842352706142556"><a name="en-us_topic_0113746489_b842352706142556"></a><a name="en-us_topic_0113746489_b842352706142556"></a>reboot_started_hard</strong>: The BMS is forcibly restarted.</li><li><strong id="en-us_topic_0113746489_b1747973441416"><a name="en-us_topic_0113746489_b1747973441416"></a><a name="en-us_topic_0113746489_b1747973441416"></a>powering-off</strong>: The BMS is being powered off.</li><li><strong id="en-us_topic_0113746489_b14239155181411"><a name="en-us_topic_0113746489_b14239155181411"></a><a name="en-us_topic_0113746489_b14239155181411"></a>powering-on</strong>: The BMS is being powered on.</li><li><strong id="en-us_topic_0113746489_b1090037174020"><a name="en-us_topic_0113746489_b1090037174020"></a><a name="en-us_topic_0113746489_b1090037174020"></a>rebuilding</strong>: The BMS is being rebuilt.</li><li><strong id="en-us_topic_0113746489_b1292442794017"><a name="en-us_topic_0113746489_b1292442794017"></a><a name="en-us_topic_0113746489_b1292442794017"></a>scheduling</strong>: The BMS is being scheduled.</li><li><strong id="en-us_topic_0113746489_b1533163584019"><a name="en-us_topic_0113746489_b1533163584019"></a><a name="en-us_topic_0113746489_b1533163584019"></a>deleting</strong>: The BMS is being deleted.</li></ul>
    </td>
    </tr>
    <tr id="row18128948122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p40790901122520"><a name="p40790901122520"></a><a name="p40790901122520"></a>OS-EXT-STS:vm_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p15728710122520"><a name="p15728710122520"></a><a name="p15728710122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p66066036122520"><a name="p66066036122520"></a><a name="p66066036122520"></a>Specifies the stable <span id="text4386124215155"><a name="text4386124215155"></a><a name="text4386124215155"></a>BMS</span><span id="text17387134241519"><a name="text17387134241519"></a><a name="text17387134241519"></a></span> status. This is an extended attribute.</p>
    <p id="p35702402121227"><a name="p35702402121227"></a><a name="p35702402121227"></a>Value range:</p>
    <a name="ul1524416587573"></a><a name="ul1524416587573"></a><ul id="ul1524416587573"><li><strong id="en-us_topic_0113746489_b2288942114020"><a name="en-us_topic_0113746489_b2288942114020"></a><a name="en-us_topic_0113746489_b2288942114020"></a>active</strong>: The BMS is running.</li><li><strong id="en-us_topic_0113746489_b18910145122615"><a name="en-us_topic_0113746489_b18910145122615"></a><a name="en-us_topic_0113746489_b18910145122615"></a>shutoff</strong>: The BMS is stopped.</li><li><strong id="en-us_topic_0113746489_b69874615270"><a name="en-us_topic_0113746489_b69874615270"></a><a name="en-us_topic_0113746489_b69874615270"></a>suspended</strong>: The BMS is suspended.</li><li><strong id="en-us_topic_0113746489_b9129182392714"><a name="en-us_topic_0113746489_b9129182392714"></a><a name="en-us_topic_0113746489_b9129182392714"></a>reboot</strong>: The BMS is restarted.</li></ul>
    </td>
    </tr>
    <tr id="row2014327122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p45085213122520"><a name="p45085213122520"></a><a name="p45085213122520"></a>OS-SRV-USG:launched_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p28023600122520"><a name="p28023600122520"></a><a name="p28023600122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p55319165122520"><a name="p55319165122520"></a><a name="p55319165122520"></a>Specifies the time when the <span id="text411419433150"><a name="text411419433150"></a><a name="text411419433150"></a>BMS</span><span id="text12115643161511"><a name="text12115643161511"></a><a name="text12115643161511"></a></span> was started. This is an extended attribute.</p>
    <p id="p1612313121426"><a name="p1612313121426"></a><a name="p1612313121426"></a>The timestamp format is ISO 8601, for example, <strong id="b1575721782617"><a name="b1575721782617"></a><a name="b1575721782617"></a>2019-05-22T03:23:59.000000</strong>.</p>
    </td>
    </tr>
    <tr id="row7680354122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p62353148122520"><a name="p62353148122520"></a><a name="p62353148122520"></a>OS-SRV-USG:terminated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p17440221122520"><a name="p17440221122520"></a><a name="p17440221122520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p3371762122520"><a name="p3371762122520"></a><a name="p3371762122520"></a>Specifies the time when the <span id="text1087275418157"><a name="text1087275418157"></a><a name="text1087275418157"></a>BMS</span><span id="text087355411155"><a name="text087355411155"></a><a name="text087355411155"></a></span> was deleted. This is an extended attribute.</p>
    <p id="p1528862619210"><a name="p1528862619210"></a><a name="p1528862619210"></a>The timestamp format is ISO 8601, for example, <strong id="b95535332269"><a name="b95535332269"></a><a name="b95535332269"></a>2019-05-22T04:23:59.000000</strong>.</p>
    </td>
    </tr>
    <tr id="row853372122520"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p42095554122520"><a name="p42095554122520"></a><a name="p42095554122520"></a>os-extended-volumes:volumes_attached</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p54296746122520"><a name="p54296746122520"></a><a name="p54296746122520"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p35960290122520"><a name="p35960290122520"></a><a name="p35960290122520"></a>Specifies the EVS disks attached to the <span id="text14400116161"><a name="text14400116161"></a><a name="text14400116161"></a>BMS</span><span id="text144121151614"><a name="text144121151614"></a><a name="text144121151614"></a></span>. For details, see <a href="#table20591095122442">Table 10</a>.</p>
    </td>
    </tr>
    <tr id="row58203854165114"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p16891701165114"><a name="p16891701165114"></a><a name="p16891701165114"></a>accessIPv4</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p26050561165114"><a name="p26050561165114"></a><a name="p26050561165114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p29720730165114"><a name="p29720730165114"></a><a name="p29720730165114"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row32395720165115"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p6807678165115"><a name="p6807678165115"></a><a name="p6807678165115"></a>accessIPv6</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p14551052165115"><a name="p14551052165115"></a><a name="p14551052165115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p37784603165115"><a name="p37784603165115"></a><a name="p37784603165115"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row45481526194558"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p6680555194558"><a name="p6680555194558"></a><a name="p6680555194558"></a>fault</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p4254049194558"><a name="p4254049194558"></a><a name="p4254049194558"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p9033688194558"><a name="p9033688194558"></a><a name="p9033688194558"></a>Specifies the fault cause. If the <span id="text1636954713581"><a name="text1636954713581"></a><a name="text1636954713581"></a>BMS</span><span id="text236974765813"><a name="text236974765813"></a><a name="text236974765813"></a></span> is faulty, this field is returned. For details, see <a href="#table48872702194825">Table 11</a>.</p>
    </td>
    </tr>
    <tr id="row43202810165116"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p9766688165116"><a name="p9766688165116"></a><a name="p9766688165116"></a>config_drive</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p52904263165116"><a name="p52904263165116"></a><a name="p52904263165116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p57386902165116"><a name="p57386902165116"></a><a name="p57386902165116"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row63072391165255"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p8590013165255"><a name="p8590013165255"></a><a name="p8590013165255"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p24702452165255"><a name="p24702452165255"></a><a name="p24702452165255"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p54741587165255"><a name="p54741587165255"></a><a name="p54741587165255"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row62339472192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p4168431192944"><a name="p4168431192944"></a><a name="p4168431192944"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p2098640192944"><a name="p2098640192944"></a><a name="p2098640192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p35772153192944"><a name="p35772153192944"></a><a name="p35772153192944"></a>Provides supplementary information about the pool.</p>
    <p id="p39660978192944"><a name="p39660978192944"></a><a name="p39660978192944"></a>This parameter is added in micro version 2.19.</p>
    </td>
    </tr>
    <tr id="row36752769192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p56041785192944"><a name="p56041785192944"></a><a name="p56041785192944"></a>host_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p43090708192944"><a name="p43090708192944"></a><a name="p43090708192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p55603620192944"><a name="p55603620192944"></a><a name="p55603620192944"></a>Specifies the status of the host that accommodates the <span id="text129271650165813"><a name="text129271650165813"></a><a name="text129271650165813"></a>BMS</span><span id="text10927150135811"><a name="text10927150135811"></a><a name="text10927150135811"></a></span>.</p>
    <a name="ul30670539192944"></a><a name="ul30670539192944"></a><ul id="ul30670539192944"><li><strong id="b842352706183126"><a name="b842352706183126"></a><a name="b842352706183126"></a>UP</strong>: The nova-compute is normal.</li><li><strong id="b1498018510183149"><a name="b1498018510183149"></a><a name="b1498018510183149"></a>UNKNOWN</strong>: The nova-compute status is unknown.</li><li><strong id="b842352706183156"><a name="b842352706183156"></a><a name="b842352706183156"></a>DOWN</strong>: the nova-compute status is abnormal.</li><li><strong id="b842352706183211"><a name="b842352706183211"></a><a name="b842352706183211"></a>MAINTENANCE</strong>: The nova-compute is in the maintenance state.</li><li>Empty string: The <span id="text1940285401612"><a name="text1940285401612"></a><a name="text1940285401612"></a>BMS</span><span id="text240345414164"><a name="text240345414164"></a><a name="text240345414164"></a></span> does not have host information.</li></ul>
    <p id="p47210269192944"><a name="p47210269192944"></a><a name="p47210269192944"></a>Added in micro version 2.16.</p>
    </td>
    </tr>
    <tr id="row18996721192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p56548258192944"><a name="p56548258192944"></a><a name="p56548258192944"></a>OS-EXT-SRV-ATTR:hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p17006177192944"><a name="p17006177192944"></a><a name="p17006177192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p42600570192944"><a name="p42600570192944"></a><a name="p42600570192944"></a>Specifies the hos name of the <span id="text217745951614"><a name="text217745951614"></a><a name="text217745951614"></a>BMS</span><span id="text917825961618"><a name="text917825961618"></a><a name="text917825961618"></a></span>.</p>
    <p id="p47860811192944"><a name="p47860811192944"></a><a name="p47860811192944"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    <tr id="row24480368192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p61030804192944"><a name="p61030804192944"></a><a name="p61030804192944"></a>OS-EXT-SRV-ATTR:reservation_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p44548086192944"><a name="p44548086192944"></a><a name="p44548086192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p20891691192944"><a name="p20891691192944"></a><a name="p20891691192944"></a>Specifies the reserved <span id="text1914315825817"><a name="text1914315825817"></a><a name="text1914315825817"></a>BMS</span><span id="text11441583583"><a name="text11441583583"></a><a name="text11441583583"></a></span> IDs in the batch BMS creation scenario.</p>
    <p id="p53807496192944"><a name="p53807496192944"></a><a name="p53807496192944"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    <tr id="row47459283192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p38361754192944"><a name="p38361754192944"></a><a name="p38361754192944"></a>OS-EXT-SRV-ATTR:launch_index</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p20294378192944"><a name="p20294378192944"></a><a name="p20294378192944"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p7429535192944"><a name="p7429535192944"></a><a name="p7429535192944"></a>Specifies the <span id="text123415015599"><a name="text123415015599"></a><a name="text123415015599"></a>BMS</span><span id="text18341104592"><a name="text18341104592"></a><a name="text18341104592"></a></span> startup sequence in the batch BMS creation scenario.</p>
    <p id="p66865815192944"><a name="p66865815192944"></a><a name="p66865815192944"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    <tr id="row27642875192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p15972052192944"><a name="p15972052192944"></a><a name="p15972052192944"></a>OS-EXT-SRV-ATTR:kernel_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p18667868192944"><a name="p18667868192944"></a><a name="p18667868192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p6207108192944"><a name="p6207108192944"></a><a name="p6207108192944"></a>Specifies the UUID of the kernel image when the AMI image is used. In other scenarios, leave this parameter blank.</p>
    <p id="p55863977192944"><a name="p55863977192944"></a><a name="p55863977192944"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    <tr id="row55267213192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p42050086192944"><a name="p42050086192944"></a><a name="p42050086192944"></a>OS-EXT-SRV-ATTR:ramdisk_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p50613791192944"><a name="p50613791192944"></a><a name="p50613791192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p22426767192944"><a name="p22426767192944"></a><a name="p22426767192944"></a>Specifies the UUID of the Ramdisk image when the AMI image is used. In other scenarios, leave this parameter blank.</p>
    <p id="p514313192944"><a name="p514313192944"></a><a name="p514313192944"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    <tr id="row21053882192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p18967993192944"><a name="p18967993192944"></a><a name="p18967993192944"></a>OS-EXT-SRV-ATTR:root_device_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p60012494192944"><a name="p60012494192944"></a><a name="p60012494192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p14273082192944"><a name="p14273082192944"></a><a name="p14273082192944"></a>Specifies the device name of the <span id="text135871927121818"><a name="text135871927121818"></a><a name="text135871927121818"></a>BMS</span><span id="text1758892716189"><a name="text1758892716189"></a><a name="text1758892716189"></a></span> system disk, for example, <strong id="b16589132710182"><a name="b16589132710182"></a><a name="b16589132710182"></a>/dev/sda</strong>.</p>
    <p id="p61348874192944"><a name="p61348874192944"></a><a name="p61348874192944"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    <tr id="row2339320192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p28826247192944"><a name="p28826247192944"></a><a name="p28826247192944"></a>OS-EXT-SRV-ATTR:user_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p53224662192944"><a name="p53224662192944"></a><a name="p53224662192944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p39593231192944"><a name="p39593231192944"></a><a name="p39593231192944"></a>Specifies the <strong id="b1926595792720"><a name="b1926595792720"></a><a name="b1926595792720"></a>user_data</strong> specified during BMS creation. The value is encoded using Base64 or an empty string.</p>
    </td>
    </tr>
    <tr id="row30086086192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p6653960192944"><a name="p6653960192944"></a><a name="p6653960192944"></a>locked</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p2099860192944"><a name="p2099860192944"></a><a name="p2099860192944"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p19869683192944"><a name="p19869683192944"></a><a name="p19869683192944"></a>Specifies whether the <span id="text55145121813"><a name="text55145121813"></a><a name="text55145121813"></a>BMS</span><span id="text206164511816"><a name="text206164511816"></a><a name="text206164511816"></a></span> is locked.</p>
    <a name="ul44609424192944"></a><a name="ul44609424192944"></a><ul id="ul44609424192944"><li><strong id="b842352706184545"><a name="b842352706184545"></a><a name="b842352706184545"></a>true</strong>: The BMS is locked.</li><li><strong id="b842352706184554"><a name="b842352706184554"></a><a name="b842352706184554"></a>false</strong>: The BMS is not locked.</li></ul>
    <p id="p39580388192944"><a name="p39580388192944"></a><a name="p39580388192944"></a>Added in micro version 2.9.</p>
    </td>
    </tr>
    <tr id="row18255979192944"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p64400516192944"><a name="p64400516192944"></a><a name="p64400516192944"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.94%" headers="mcps1.2.4.1.2 "><p id="p49059297192944"><a name="p49059297192944"></a><a name="p49059297192944"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.07000000000001%" headers="mcps1.2.4.1.3 "><p id="p23937628192944"><a name="p23937628192944"></a><a name="p23937628192944"></a>Specifies tags of the <span id="text1566491395915"><a name="text1566491395915"></a><a name="text1566491395915"></a>BMS</span><span id="text156643131598"><a name="text156643131598"></a><a name="text156643131598"></a></span>.</p>
    <p id="p14112065192944"><a name="p14112065192944"></a><a name="p14112065192944"></a>This parameter is added in microversion 2.26. If the microversion is not used for query, the response does not contain the <strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>tags</strong> field.</p>
    <p id="p65835388184"><a name="p65835388184"></a><a name="p65835388184"></a>The value of this field meets the following requirements:</p>
    <a name="en-us_topic_0020212689_ul871515496611"></a><a name="en-us_topic_0020212689_ul871515496611"></a><ul id="en-us_topic_0020212689_ul871515496611"><li>The key and value of a tag are connected using an equal sign (=), for example, <strong id="b116255414343"><a name="b116255414343"></a><a name="b116255414343"></a>key=value</strong>.</li><li>If the value is empty, only the key is returned.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **flavor**  field data structure description

    <a name="table19588408"></a>
    <table><thead align="left"><tr id="row65668512"><th class="cellrowborder" valign="top" width="23.32233223322332%" id="mcps1.2.4.1.1"><p id="p185203139482"><a name="p185203139482"></a><a name="p185203139482"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.192619261926193%" id="mcps1.2.4.1.2"><p id="p952581311482"><a name="p952581311482"></a><a name="p952581311482"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.48504850485048%" id="mcps1.2.4.1.3"><p id="p55371313144813"><a name="p55371313144813"></a><a name="p55371313144813"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54114449"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p21194271"><a name="p21194271"></a><a name="p21194271"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p6046963"><a name="p6046963"></a><a name="p6046963"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p20041994"><a name="p20041994"></a><a name="p20041994"></a>Specifies the <span id="text256618155911"><a name="text256618155911"></a><a name="text256618155911"></a>BMS</span><span id="text1856161865918"><a name="text1856161865918"></a><a name="text1856161865918"></a></span> type ID.</p>
    <p id="p171237576493"><a name="p171237576493"></a><a name="p171237576493"></a>This field is not supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row46160221"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p47990424"><a name="p47990424"></a><a name="p47990424"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p57492083"><a name="p57492083"></a><a name="p57492083"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p35797372"><a name="p35797372"></a><a name="p35797372"></a>Specifies shortcut links of the <span id="text7269174217192"><a name="text7269174217192"></a><a name="text7269174217192"></a>BMS</span><span id="text1927044214194"><a name="text1927044214194"></a><a name="text1927044214194"></a></span> type.</p>
    <p id="p1457120585564"><a name="p1457120585564"></a><a name="p1457120585564"></a>For details, see <a href="#table16539321">Table 5</a>.</p>
    <p id="p18745351125019"><a name="p18745351125019"></a><a name="p18745351125019"></a>This field is not supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row485182814512"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p18647653114019"><a name="p18647653114019"></a><a name="p18647653114019"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p5647153194013"><a name="p5647153194013"></a><a name="p5647153194013"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p594712133917"><a name="p594712133917"></a><a name="p594712133917"></a>Specifies the number of CPU cores in the BMS flavor.</p>
    <p id="p7411737161018"><a name="p7411737161018"></a><a name="p7411737161018"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row178511428105116"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p460015587400"><a name="p460015587400"></a><a name="p460015587400"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p1760065884017"><a name="p1760065884017"></a><a name="p1760065884017"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p1760065884013"><a name="p1760065884013"></a><a name="p1760065884013"></a>Specifies the memory size (MB) in the BMS flavor.</p>
    <p id="p0979145841010"><a name="p0979145841010"></a><a name="p0979145841010"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row174731835165116"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p338192124118"><a name="p338192124118"></a><a name="p338192124118"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p143817234115"><a name="p143817234115"></a><a name="p143817234115"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p1381422419"><a name="p1381422419"></a><a name="p1381422419"></a>Specifies the system disk size in the BMS flavor. The value <strong id="b193352016288"><a name="b193352016288"></a><a name="b193352016288"></a>0</strong> indicates that the disk size is not limited.</p>
    <p id="p155897161110"><a name="p155897161110"></a><a name="p155897161110"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row14473153555118"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p175990512419"><a name="p175990512419"></a><a name="p175990512419"></a>ephemeral</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p55996517419"><a name="p55996517419"></a><a name="p55996517419"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p1059914514118"><a name="p1059914514118"></a><a name="p1059914514118"></a>This is a reserved attribute.</p>
    <p id="p138227319114"><a name="p138227319114"></a><a name="p138227319114"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row1747333525118"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p66306183429"><a name="p66306183429"></a><a name="p66306183429"></a>swap</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p863019183421"><a name="p863019183421"></a><a name="p863019183421"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p15630121813429"><a name="p15630121813429"></a><a name="p15630121813429"></a>This is a reserved attribute.</p>
    <p id="p568210631113"><a name="p568210631113"></a><a name="p568210631113"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row184731235125117"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p1936516339428"><a name="p1936516339428"></a><a name="p1936516339428"></a>original_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p163651333144219"><a name="p163651333144219"></a><a name="p163651333144219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p2365113374215"><a name="p2365113374215"></a><a name="p2365113374215"></a>This is a reserved attribute.</p>
    <p id="p47911894115"><a name="p47911894115"></a><a name="p47911894115"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    <tr id="row19240134110517"><td class="cellrowborder" valign="top" width="23.32233223322332%" headers="mcps1.2.4.1.1 "><p id="p136311336194210"><a name="p136311336194210"></a><a name="p136311336194210"></a>extra_specs</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.192619261926193%" headers="mcps1.2.4.1.2 "><p id="p563116366423"><a name="p563116366423"></a><a name="p563116366423"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.48504850485048%" headers="mcps1.2.4.1.3 "><p id="p963110362428"><a name="p963110362428"></a><a name="p963110362428"></a>Extended flavor field</p>
    <p id="p68221938111119"><a name="p68221938111119"></a><a name="p68221938111119"></a>This field is supported in microversions later than 2.47.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **image**  field data structure description

    <a name="table1258047620856"></a>
    <table><thead align="left"><tr id="row6041176320856"><th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.1"><p id="p1927472664813"><a name="p1927472664813"></a><a name="p1927472664813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.169999999999998%" id="mcps1.2.4.1.2"><p id="p7278192614818"><a name="p7278192614818"></a><a name="p7278192614818"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.4%" id="mcps1.2.4.1.3"><p id="p122885267488"><a name="p122885267488"></a><a name="p122885267488"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4046402920856"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.1 "><p id="p5636094120856"><a name="p5636094120856"></a><a name="p5636094120856"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p183352620856"><a name="p183352620856"></a><a name="p183352620856"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.3 "><p id="p1429788720856"><a name="p1429788720856"></a><a name="p1429788720856"></a>Specifies the image ID of the <span id="text4676257111913"><a name="text4676257111913"></a><a name="text4676257111913"></a>BMS</span><span id="text667785771919"><a name="text667785771919"></a><a name="text667785771919"></a></span>.</p>
    </td>
    </tr>
    <tr id="row6157211920856"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.1 "><p id="p2128571520856"><a name="p2128571520856"></a><a name="p2128571520856"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p4642138020856"><a name="p4642138020856"></a><a name="p4642138020856"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.3 "><p id="p203547420856"><a name="p203547420856"></a><a name="p203547420856"></a>Specifies shortcut links of the <span id="text082212214201"><a name="text082212214201"></a><a name="text082212214201"></a>BMS</span><span id="text1482472112010"><a name="text1482472112010"></a><a name="text1482472112010"></a></span> image. For details, see <a href="#table16539321">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **links**  field data structure description

    <a name="table16539321"></a>
    <table><thead align="left"><tr id="row4585366"><th class="cellrowborder" valign="top" width="23.86761323867613%" id="mcps1.2.4.1.1"><p id="p5927193513484"><a name="p5927193513484"></a><a name="p5927193513484"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.17738226177382%" id="mcps1.2.4.1.2"><p id="p189301935184812"><a name="p189301935184812"></a><a name="p189301935184812"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.95500449955004%" id="mcps1.2.4.1.3"><p id="p12940123554816"><a name="p12940123554816"></a><a name="p12940123554816"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14455526"><td class="cellrowborder" valign="top" width="23.86761323867613%" headers="mcps1.2.4.1.1 "><p id="p30046962"><a name="p30046962"></a><a name="p30046962"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.17738226177382%" headers="mcps1.2.4.1.2 "><p id="p39387099"><a name="p39387099"></a><a name="p39387099"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.95500449955004%" headers="mcps1.2.4.1.3 "><p id="p36238473"><a name="p36238473"></a><a name="p36238473"></a>Specifies the shortcut link marker name. The value can be:</p>
    <a name="ul207311644172510"></a><a name="ul207311644172510"></a><ul id="ul207311644172510"><li><strong id="en-us_topic_0131326852_b320113110516"><a name="en-us_topic_0131326852_b320113110516"></a><a name="en-us_topic_0131326852_b320113110516"></a>self</strong>: resource link that contains the version number. It is used when immediate tracing is required.</li><li><strong id="en-us_topic_0131326852_b84171947711"><a name="en-us_topic_0131326852_b84171947711"></a><a name="en-us_topic_0131326852_b84171947711"></a>bookmark</strong>: resource link that can be stored for a long time.</li></ul>
    </td>
    </tr>
    <tr id="row57710802"><td class="cellrowborder" valign="top" width="23.86761323867613%" headers="mcps1.2.4.1.1 "><p id="p44063391"><a name="p44063391"></a><a name="p44063391"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.17738226177382%" headers="mcps1.2.4.1.2 "><p id="p62035831"><a name="p62035831"></a><a name="p62035831"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.95500449955004%" headers="mcps1.2.4.1.3 "><p id="p58846418"><a name="p58846418"></a><a name="p58846418"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **metadata**  field data structure description

    <a name="table2549048917552"></a>
    <table><thead align="left"><tr id="row5894027817552"><th class="cellrowborder" valign="top" width="24.467553244675532%" id="mcps1.2.4.1.1"><p id="p91023447486"><a name="p91023447486"></a><a name="p91023447486"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.76742325767423%" id="mcps1.2.4.1.2"><p id="p7108104414810"><a name="p7108104414810"></a><a name="p7108104414810"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.76502349765023%" id="mcps1.2.4.1.3"><p id="p211774424818"><a name="p211774424818"></a><a name="p211774424818"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2346131617552"><td class="cellrowborder" valign="top" width="24.467553244675532%" headers="mcps1.2.4.1.1 "><p id="p2131841817552"><a name="p2131841817552"></a><a name="p2131841817552"></a>User-defined field key and value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.76742325767423%" headers="mcps1.2.4.1.2 "><p id="p4907026417552"><a name="p4907026417552"></a><a name="p4907026417552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.76502349765023%" headers="mcps1.2.4.1.3 "><p id="p5719410617654"><a name="p5719410617654"></a><a name="p5719410617654"></a>Specifies the key and value pair of the metadata.</p>
    <p id="p4498490617654"><a name="p4498490617654"></a><a name="p4498490617654"></a>The maximum size for each metadata key and value pair is 255 bytes.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **addresses**  field data structure description

    <a name="table3730161"></a>
    <table><thead align="left"><tr id="row20014316"><th class="cellrowborder" valign="top" width="21.497850214978502%" id="mcps1.2.4.1.1"><p id="p10546933"><a name="p10546933"></a><a name="p10546933"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.947005299470053%" id="mcps1.2.4.1.2"><p id="p9192332"><a name="p9192332"></a><a name="p9192332"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.555144485551445%" id="mcps1.2.4.1.3"><p id="p6381418"><a name="p6381418"></a><a name="p6381418"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57432766"><td class="cellrowborder" valign="top" width="21.497850214978502%" headers="mcps1.2.4.1.1 "><p id="p25045336115623"><a name="p25045336115623"></a><a name="p25045336115623"></a>VPC ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.947005299470053%" headers="mcps1.2.4.1.2 "><p id="p4439518115623"><a name="p4439518115623"></a><a name="p4439518115623"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.555144485551445%" headers="mcps1.2.4.1.3 "><p id="p2639016112816"><a name="p2639016112816"></a><a name="p2639016112816"></a>Specifies the ID of the VPC used by the <span id="text12203110132013"><a name="text12203110132013"></a><a name="text12203110132013"></a>BMS</span><span id="text1920411010208"><a name="text1920411010208"></a><a name="text1920411010208"></a></span> (the VPC name is a variable). For details, see <a href="#table1656029015527">Table 8</a>.</p>
    <p id="p3618485912816"><a name="p3618485912816"></a><a name="p3618485912816"></a>The value in the data structure is assigned private IP addresses in the VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** _VPC ID_  field data structure description

    <a name="table1656029015527"></a>
    <table><thead align="left"><tr id="row2645284715527"><th class="cellrowborder" valign="top" width="24.702470247024706%" id="mcps1.2.4.1.1"><p id="p1040324134912"><a name="p1040324134912"></a><a name="p1040324134912"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.19271927192719%" id="mcps1.2.4.1.2"><p id="p184063416497"><a name="p184063416497"></a><a name="p184063416497"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.10481048104811%" id="mcps1.2.4.1.3"><p id="p1941717419491"><a name="p1941717419491"></a><a name="p1941717419491"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5009697415527"><td class="cellrowborder" valign="top" width="24.702470247024706%" headers="mcps1.2.4.1.1 "><p id="p3132311415527"><a name="p3132311415527"></a><a name="p3132311415527"></a>addr</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.19271927192719%" headers="mcps1.2.4.1.2 "><p id="p5414433915527"><a name="p5414433915527"></a><a name="p5414433915527"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.10481048104811%" headers="mcps1.2.4.1.3 "><p id="p2361534415527"><a name="p2361534415527"></a><a name="p2361534415527"></a>Specifies the IP address.</p>
    </td>
    </tr>
    <tr id="row1121151015527"><td class="cellrowborder" valign="top" width="24.702470247024706%" headers="mcps1.2.4.1.1 "><p id="p3571711715527"><a name="p3571711715527"></a><a name="p3571711715527"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.19271927192719%" headers="mcps1.2.4.1.2 "><p id="p740535615527"><a name="p740535615527"></a><a name="p740535615527"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.10481048104811%" headers="mcps1.2.4.1.3 "><p id="p6296298815527"><a name="p6296298815527"></a><a name="p6296298815527"></a>Specifies the type of the IP address. The value can be <strong id="b84235270614154"><a name="b84235270614154"></a><a name="b84235270614154"></a>4</strong> or <strong id="b842352706141510"><a name="b842352706141510"></a><a name="b842352706141510"></a>6</strong>.</p>
    <a name="ul2979598615527"></a><a name="ul2979598615527"></a><ul id="ul2979598615527"><li><strong id="b84235270614151"><a name="b84235270614151"></a><a name="b84235270614151"></a>4</strong>: The type of the IP address is IPv4.</li><li><strong id="b842352706141518"><a name="b842352706141518"></a><a name="b842352706141518"></a>6</strong>: The type of the IP address is IPv6.</li></ul>
    </td>
    </tr>
    <tr id="row3913338616494"><td class="cellrowborder" valign="top" width="24.702470247024706%" headers="mcps1.2.4.1.1 "><p id="p37919028165012"><a name="p37919028165012"></a><a name="p37919028165012"></a>OS-EXT-IPS-MAC:mac_addr</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.19271927192719%" headers="mcps1.2.4.1.2 "><p id="p51542402165012"><a name="p51542402165012"></a><a name="p51542402165012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.10481048104811%" headers="mcps1.2.4.1.3 "><p id="p14185000165012"><a name="p14185000165012"></a><a name="p14185000165012"></a>Specifies the MAC address. This is an extended attribute.</p>
    </td>
    </tr>
    <tr id="row5993434716495"><td class="cellrowborder" valign="top" width="24.702470247024706%" headers="mcps1.2.4.1.1 "><p id="p6100298165012"><a name="p6100298165012"></a><a name="p6100298165012"></a>OS-EXT-IPS:type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.19271927192719%" headers="mcps1.2.4.1.2 "><p id="p24362133165012"><a name="p24362133165012"></a><a name="p24362133165012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.10481048104811%" headers="mcps1.2.4.1.3 "><p id="p27175732165012"><a name="p27175732165012"></a><a name="p27175732165012"></a>Specifies the IP address type. This is an extended attribute.</p>
    <a name="ul11563717205"></a><a name="ul11563717205"></a><ul id="ul11563717205"><li><strong id="b143651242163418"><a name="b143651242163418"></a><a name="b143651242163418"></a>fixed</strong>: indicates the private IP address.</li><li><strong id="b75799477344"><a name="b75799477344"></a><a name="b75799477344"></a>floating</strong>: indicates the EIP.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9** **security\_groups**  field data structure description

    <a name="table761507165933"></a>
    <table><thead align="left"><tr id="row29958070165933"><th class="cellrowborder" valign="top" width="24.6975302469753%" id="mcps1.2.4.1.1"><p id="p8701420144919"><a name="p8701420144919"></a><a name="p8701420144919"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.107289271072894%" id="mcps1.2.4.1.2"><p id="p574420174917"><a name="p574420174917"></a><a name="p574420174917"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.1951804819518%" id="mcps1.2.4.1.3"><p id="p108542064912"><a name="p108542064912"></a><a name="p108542064912"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29572324165933"><td class="cellrowborder" valign="top" width="24.6975302469753%" headers="mcps1.2.4.1.1 "><p id="p46548026165933"><a name="p46548026165933"></a><a name="p46548026165933"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.107289271072894%" headers="mcps1.2.4.1.2 "><p id="p12293798165933"><a name="p12293798165933"></a><a name="p12293798165933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.1951804819518%" headers="mcps1.2.4.1.3 "><a name="ul1907127295026"></a><a name="ul1907127295026"></a><ul id="ul1907127295026"><li>If no security group is specified during <span id="text1043291614207"><a name="text1043291614207"></a><a name="text1043291614207"></a>BMS</span><span id="text12433316132011"><a name="text12433316132011"></a><a name="text12433316132011"></a></span> creation, the <strong id="b1435151610203"><a name="b1435151610203"></a><a name="b1435151610203"></a>default</strong> value is used.</li><li>If a security group is specified when you create the <span id="text103411156135920"><a name="text103411156135920"></a><a name="text103411156135920"></a>BMS</span><span id="text43411056205919"><a name="text43411056205919"></a><a name="text43411056205919"></a></span>, the value of this parameter is the security group name.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10** **os-extended-volumes:volumes\_attached**  field data structure description

    <a name="table20591095122442"></a>
    <table><thead align="left"><tr id="row46969160122442"><th class="cellrowborder" valign="top" width="24.532453245324533%" id="mcps1.2.4.1.1"><p id="p10156836154910"><a name="p10156836154910"></a><a name="p10156836154910"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.302730273027304%" id="mcps1.2.4.1.2"><p id="p161669368492"><a name="p161669368492"></a><a name="p161669368492"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.16481648164816%" id="mcps1.2.4.1.3"><p id="p2178236184915"><a name="p2178236184915"></a><a name="p2178236184915"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22997982122442"><td class="cellrowborder" valign="top" width="24.532453245324533%" headers="mcps1.2.4.1.1 "><p id="p50897247122442"><a name="p50897247122442"></a><a name="p50897247122442"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.302730273027304%" headers="mcps1.2.4.1.2 "><p id="p29036308122442"><a name="p29036308122442"></a><a name="p29036308122442"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.16481648164816%" headers="mcps1.2.4.1.3 "><p id="p3130725122442"><a name="p3130725122442"></a><a name="p3130725122442"></a>Specifies the EVS disk ID.</p>
    </td>
    </tr>
    <tr id="row30980296195037"><td class="cellrowborder" valign="top" width="24.532453245324533%" headers="mcps1.2.4.1.1 "><p id="p50956008195037"><a name="p50956008195037"></a><a name="p50956008195037"></a>delete_on_termination</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.302730273027304%" headers="mcps1.2.4.1.2 "><p id="p33796012195037"><a name="p33796012195037"></a><a name="p33796012195037"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.16481648164816%" headers="mcps1.2.4.1.3 "><p id="p7951369195037"><a name="p7951369195037"></a><a name="p7951369195037"></a>Specifies whether to delete the disk when deleting the <span id="text16997124016209"><a name="text16997124016209"></a><a name="text16997124016209"></a>BMS</span><span id="text40541132016"><a name="text40541132016"></a><a name="text40541132016"></a></span>.</p>
    <a name="ul4453459195037"></a><a name="ul4453459195037"></a><ul id="ul4453459195037"><li><strong>true</strong>: Yes</li><li><strong>false</strong>: No</li></ul>
    <p id="p25346744195037"><a name="p25346744195037"></a><a name="p25346744195037"></a>Added in micro version 2.3.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11** **fault**  field data structure description

    <a name="table48872702194825"></a>
    <table><thead align="left"><tr id="row7333744194825"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p4296115020494"><a name="p4296115020494"></a><a name="p4296115020494"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.189999999999998%" id="mcps1.2.4.1.2"><p id="p2030275074910"><a name="p2030275074910"></a><a name="p2030275074910"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.3"><p id="p431725004912"><a name="p431725004912"></a><a name="p431725004912"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22593755194825"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18154898194825"><a name="p18154898194825"></a><a name="p18154898194825"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p61260596194825"><a name="p61260596194825"></a><a name="p61260596194825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.3 "><p id="p15788383194825"><a name="p15788383194825"></a><a name="p15788383194825"></a>Specifies the fault information.</p>
    </td>
    </tr>
    <tr id="row7877723194825"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p34115828194825"><a name="p34115828194825"></a><a name="p34115828194825"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p11918718194825"><a name="p11918718194825"></a><a name="p11918718194825"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.3 "><p id="p16887684194825"><a name="p16887684194825"></a><a name="p16887684194825"></a>Specifies the fault code.</p>
    </td>
    </tr>
    <tr id="row17771429194825"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p30199627194825"><a name="p30199627194825"></a><a name="p30199627194825"></a>details</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p30250759194825"><a name="p30250759194825"></a><a name="p30250759194825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.3 "><p id="p34319578194825"><a name="p34319578194825"></a><a name="p34319578194825"></a>Specifies the fault details.</p>
    </td>
    </tr>
    <tr id="row40440754194825"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p54475616194825"><a name="p54475616194825"></a><a name="p54475616194825"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p50448742194825"><a name="p50448742194825"></a><a name="p50448742194825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.3 "><p id="p13282204194825"><a name="p13282204194825"></a><a name="p13282204194825"></a>Specifies the time when the fault occurred. The time is in ISO 8601 format.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "server": {
            "tenant_id": "c685484a8cc2416b97260938705deb65",
            "addresses": {
                "08a7715f-7de6-4ff9-a343-95ba4209f24a": [
    {
                        "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:0e:c3:77",
                        "OS-EXT-IPS:type": "fixed",
                        "addr": "192.168.0.107",
                        "version": 4
                    }
                ]
            },
            "metadata": {
                "op_svc_userid": "1311c433dd9b408886f57d695c229cbe"
            },
            "OS-EXT-STS:task_state": null,
            "OS-DCF:diskConfig": "MANUAL",
            "OS-EXT-AZ:availability_zone": "az-dc-1",
            "links": [
    {
                    "rel": "self",
                    "href": "https://openstack.example.com/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                },
    {
                    "rel": "bookmark",
                    "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                    }
            ],
            "OS-EXT-STS:power_state": 1,
            "id": "95bf2490-5428-432c-ad9b-5e3406f869dd",
            "os-extended-volumes:volumes_attached": [
    {
                    "id": "dfa375b5-9856-44ad-a937-a4802b6434c3"
                },
    {
                    "id": "bb9f1b27-843b-4561-b62e-ca18eeaec417"
                },
    {
                    "id": "86e801c3-acc6-465d-890c-d43ba493f553"
                },
    {
                    "id": "0994d3ac-3c6a-495c-a439-c597a4f08fa6"
                    }
            ],
            "OS-EXT-SRV-ATTR:host": "bms.az1",
            "image": {
                "links": [
    {
                        "rel": "bookmark",
                        "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/images/1a6635d8-afea-4f2b-abb6-27a202bad319"
                    }
                ],
                "id": "1a6635d8-afea-4f2b-abb6-27a202bad319"
            },
            "OS-SRV-USG:terminated_at": null,
            "accessIPv4": "",
            "accessIPv6": "",
            "created": "2017-05-24T06:14:05Z",
            "hostId": "e9c3ee0fcc58ab6085cf30df70b5544eab958858fb50d925f023e53e",
            "OS-EXT-SRV-ATTR:hypervisor_hostname": "nova004@2",
            "key_name": "KeyPair-JX",
            "flavor": {
                "links": [
    {
                        "rel": "bookmark",
                        "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/flavors/physical.83.medium"
                    }
                ],
                "id": "physical.83.medium"
            },
            "security_groups": [
    {
                    "name": "0011b620-4982-42e4-ad12-47c95ca495c4"
                    }
            ],
            "config_drive": "",
            "OS-EXT-STS:vm_state": "active",
            "OS-EXT-SRV-ATTR:instance_name": "instance-0000ebd3",
            "user_id": "1311c433dd9b408886f57d695c229cbe",
            "name": "bms-83",
            "progress": 0,
            "OS-SRV-USG:launched_at": "2017-05-25T03:40:25.066078",
            "updated": "2017-05-25T03:40:25Z",
            "status": "ACTIVE"
                    }
    }
    ```


## Returned Values<a name="section161481617251"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

