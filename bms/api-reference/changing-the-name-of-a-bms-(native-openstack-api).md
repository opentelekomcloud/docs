# Changing the Name of a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158710"></a>

## Function<a name="section15039321"></a>

This interface is used to modify BMS information. Currently, only the name of the BMS can be changed.

## URI<a name="section1136168"></a>

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}

[Table 1](#table31881691585)  lists the parameters.

**Table  1**  Parameter description

<a name="table31881691585"></a>
<table><thead align="left"><tr id="row71901797582"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p44796718"><a name="p44796718"></a><a name="p44796718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p4655547"><a name="p4655547"></a><a name="p4655547"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p41555045"><a name="p41555045"></a><a name="p41555045"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row119012955817"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46447150"><a name="p46447150"></a><a name="p46447150"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4122781"><a name="p4122781"></a><a name="p4122781"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p65509833"><a name="p65509833"></a><a name="p65509833"></a>Specifies the project ID.</p>
<p id="p13397185821014"><a name="p13397185821014"></a><a name="p13397185821014"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row20190179175820"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p31999978165316"><a name="p31999978165316"></a><a name="p31999978165316"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41861457165316"><a name="p41861457165316"></a><a name="p41861457165316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35334819165316"><a name="p35334819165316"></a><a name="p35334819165316"></a>Specifies the BMS ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section10225512"></a>

-   Request parameters

    <a name="table13100926"></a>
    <table><thead align="left"><tr id="row35303864"><th class="cellrowborder" valign="top" width="19.45%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.22%" id="mcps1.1.5.1.2"><p id="p143595272555"><a name="p143595272555"></a><a name="p143595272555"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.27%" id="mcps1.1.5.1.3"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.06%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34270115"><td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.1 "><p id="p24415962"><a name="p24415962"></a><a name="p24415962"></a>server</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.22%" headers="mcps1.1.5.1.2 "><p id="p73591627155515"><a name="p73591627155515"></a><a name="p73591627155515"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.5.1.3 "><p id="p4268531"><a name="p4268531"></a><a name="p4268531"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.06%" headers="mcps1.1.5.1.4 "><p id="p24751971"><a name="p24751971"></a><a name="p24751971"></a>Specifies the BMS data structure. For details, see <a href="#table26827213163326">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **server**  field data structure description

    <a name="table26827213163326"></a>
    <table><thead align="left"><tr id="row36672866163326"><th class="cellrowborder" valign="top" width="19.451945194519453%" id="mcps1.2.5.1.1"><p id="p123868247529"><a name="p123868247529"></a><a name="p123868247529"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.592359235923592%" id="mcps1.2.5.1.2"><p id="p145845348553"><a name="p145845348553"></a><a name="p145845348553"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.891889188918892%" id="mcps1.2.5.1.3"><p id="p10389142410522"><a name="p10389142410522"></a><a name="p10389142410522"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.06380638063806%" id="mcps1.2.5.1.4"><p id="p143961224105219"><a name="p143961224105219"></a><a name="p143961224105219"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31760590163326"><td class="cellrowborder" valign="top" width="19.451945194519453%" headers="mcps1.2.5.1.1 "><p id="p22470979163326"><a name="p22470979163326"></a><a name="p22470979163326"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.592359235923592%" headers="mcps1.2.5.1.2 "><p id="p1758413425513"><a name="p1758413425513"></a><a name="p1758413425513"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.2.5.1.3 "><p id="p61032295163326"><a name="p61032295163326"></a><a name="p61032295163326"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.06380638063806%" headers="mcps1.2.5.1.4 "><p id="p66475806163326"><a name="p66475806163326"></a><a name="p66475806163326"></a>Specifies the new BMS name.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    PUT https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd
    ```

    ```
    {
        "server": {
            "name": "new-server-test"
        }
    }
    ```


## Response Message<a name="section24920747"></a>

-   Response parameters

    <a name="table2736041"></a>
    <table><thead align="left"><tr id="row37718351"><th class="cellrowborder" valign="top" width="23.64%" id="mcps1.1.4.1.1"><p id="p167261534135214"><a name="p167261534135214"></a><a name="p167261534135214"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.13%" id="mcps1.1.4.1.2"><p id="p147298341527"><a name="p147298341527"></a><a name="p147298341527"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.23%" id="mcps1.1.4.1.3"><p id="p147341234175215"><a name="p147341234175215"></a><a name="p147341234175215"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36874222"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p34022005"><a name="p34022005"></a><a name="p34022005"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p14295716"><a name="p14295716"></a><a name="p14295716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p17102365"><a name="p17102365"></a><a name="p17102365"></a>Specifies the BMS name.</p>
    </td>
    </tr>
    <tr id="row19703558"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p52484326"><a name="p52484326"></a><a name="p52484326"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p14082739"><a name="p14082739"></a><a name="p14082739"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p66960113"><a name="p66960113"></a><a name="p66960113"></a>Specifies the unique ID of the BMS.</p>
    </td>
    </tr>
    <tr id="row65770110"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p25778706"><a name="p25778706"></a><a name="p25778706"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p19753106"><a name="p19753106"></a><a name="p19753106"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p56497743"><a name="p56497743"></a><a name="p56497743"></a>Specifies the current status of the BMS.</p>
    <a name="ul13331145023611"></a><a name="ul13331145023611"></a><ul id="ul13331145023611"><li><strong id="en-us_topic_0113746489_b23014110118"><a name="en-us_topic_0113746489_b23014110118"></a><a name="en-us_topic_0113746489_b23014110118"></a>ACTIVE</strong>: Running, Stopping, Deleting</li><li><strong id="en-us_topic_0113746489_b56772617123"><a name="en-us_topic_0113746489_b56772617123"></a><a name="en-us_topic_0113746489_b56772617123"></a>BUILD</strong>: Creating</li><li><strong id="en-us_topic_0113746489_b2334141210"><a name="en-us_topic_0113746489_b2334141210"></a><a name="en-us_topic_0113746489_b2334141210"></a>ERROR</strong>: Faulty</li><li><strong id="en-us_topic_0113746489_b1059115316129"><a name="en-us_topic_0113746489_b1059115316129"></a><a name="en-us_topic_0113746489_b1059115316129"></a>HARD_REBOOT</strong>: Forcibly Restarting</li><li><strong id="en-us_topic_0113746489_b391019910131"><a name="en-us_topic_0113746489_b391019910131"></a><a name="en-us_topic_0113746489_b391019910131"></a>REBOOT</strong>: Restarting</li></ul>
    </td>
    </tr>
    <tr id="row38717641"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p49121210"><a name="p49121210"></a><a name="p49121210"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p27494304"><a name="p27494304"></a><a name="p27494304"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p12446183"><a name="p12446183"></a><a name="p12446183"></a>Specifies the time when the BMS was created.</p>
    <p id="p56671946154011"><a name="p56671946154011"></a><a name="p56671946154011"></a>The timestamp format is YYYY-MM-DDTHH:MM:SSZ (ISO 8601), for example, 2019-05-22T03:30:52Z.</p>
    </td>
    </tr>
    <tr id="row44906783"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p13570791"><a name="p13570791"></a><a name="p13570791"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p51607432"><a name="p51607432"></a><a name="p51607432"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p19452465"><a name="p19452465"></a><a name="p19452465"></a>Specifies the time when the BMS was last updated.</p>
    <p id="p1129858164012"><a name="p1129858164012"></a><a name="p1129858164012"></a>The timestamp format is YYYY-MM-DDTHH:MM:SSZ (ISO 8601), for example, 2019-05-22T04:30:52Z.</p>
    </td>
    </tr>
    <tr id="row40854465"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p20877354"><a name="p20877354"></a><a name="p20877354"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p1624603194154"><a name="p1624603194154"></a><a name="p1624603194154"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p31304760"><a name="p31304760"></a><a name="p31304760"></a>Specifies the BMS flavor information. For details, see <a href="#table16383173">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row13307388"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p4156611"><a name="p4156611"></a><a name="p4156611"></a>image</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p25330920"><a name="p25330920"></a><a name="p25330920"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p11303491"><a name="p11303491"></a><a name="p11303491"></a>Specifies the BMS image. For details, see <a href="#table1258047620856">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row34622559"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p52963885"><a name="p52963885"></a><a name="p52963885"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p6355191"><a name="p6355191"></a><a name="p6355191"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p45008451"><a name="p45008451"></a><a name="p45008451"></a>Specifies the ID of the tenant owning the BMS. The ID is in UUID format.</p>
    <p id="p3931710171316"><a name="p3931710171316"></a><a name="p3931710171316"></a>This parameter specifies the same meaning as <strong id="b11685184074618"><a name="b11685184074618"></a><a name="b11685184074618"></a>project_id</strong>.</p>
    </td>
    </tr>
    <tr id="row2422875"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p62035148"><a name="p62035148"></a><a name="p62035148"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p64457512"><a name="p64457512"></a><a name="p64457512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p53676003"><a name="p53676003"></a><a name="p53676003"></a>Specifies the ID of the user to which the BMS belongs.</p>
    </td>
    </tr>
    <tr id="row13321984"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p5338943"><a name="p5338943"></a><a name="p5338943"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p65089762"><a name="p65089762"></a><a name="p65089762"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p4469833"><a name="p4469833"></a><a name="p4469833"></a>Specifies the BMS metadata. For details, see <a href="#table2549048917552">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row40228503"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p37283276"><a name="p37283276"></a><a name="p37283276"></a>hostId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p3766004"><a name="p3766004"></a><a name="p3766004"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p36610870"><a name="p36610870"></a><a name="p36610870"></a>Specifies the host ID of the BMS.</p>
    </td>
    </tr>
    <tr id="row61062380"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p47105724"><a name="p47105724"></a><a name="p47105724"></a>addresses</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p1211038219426"><a name="p1211038219426"></a><a name="p1211038219426"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p27451543"><a name="p27451543"></a><a name="p27451543"></a>Specifies the BMS network address. For details, see <a href="#table12204733">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row45737299"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p13733718"><a name="p13733718"></a><a name="p13733718"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p11865367194214"><a name="p11865367194214"></a><a name="p11865367194214"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p47217024"><a name="p47217024"></a><a name="p47217024"></a>Specifies the shortcut links of the BMS. For details, see <a href="#table66226203">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row31237596165611"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p29731982165611"><a name="p29731982165611"></a><a name="p29731982165611"></a>accessIPv4</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p59480357165611"><a name="p59480357165611"></a><a name="p59480357165611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p53179641165611"><a name="p53179641165611"></a><a name="p53179641165611"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row33297005165611"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p46144126165611"><a name="p46144126165611"></a><a name="p46144126165611"></a>accessIPv6</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p46686760165611"><a name="p46686760165611"></a><a name="p46686760165611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p23531243165611"><a name="p23531243165611"></a><a name="p23531243165611"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row57669497165636"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p16765718165636"><a name="p16765718165636"></a><a name="p16765718165636"></a>OS-DCF:diskConfig</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p15845898165636"><a name="p15845898165636"></a><a name="p15845898165636"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p8449355165636"><a name="p8449355165636"></a><a name="p8449355165636"></a>Specifies the disk configuration method. This is an extended attribute. The value can be:</p>
    <a name="ul1147816353420"></a><a name="ul1147816353420"></a><ul id="ul1147816353420"><li><strong id="en-us_topic_0113746489_b842352706201852"><a name="en-us_topic_0113746489_b842352706201852"></a><a name="en-us_topic_0113746489_b842352706201852"></a>MANUAL</strong>: The API uses the partitioning scheme in the image and the file system to create a <span id="en-us_topic_0113746489_text5742455133714"><a name="en-us_topic_0113746489_text5742455133714"></a><a name="en-us_topic_0113746489_text5742455133714"></a>BMS</span><span id="en-us_topic_0113746489_text674310553373"><a name="en-us_topic_0113746489_text674310553373"></a><a name="en-us_topic_0113746489_text674310553373"></a></span>. If the target flavor has a large disk, the API does not partition the remaining disk space.</li><li><strong id="en-us_topic_0113746489_b11108728193415"><a name="en-us_topic_0113746489_b11108728193415"></a><a name="en-us_topic_0113746489_b11108728193415"></a>AUTO</strong>: The API uses a single partition with the same size as the disk of the target flavor to create a <span id="en-us_topic_0113746489_text1759675920373"><a name="en-us_topic_0113746489_text1759675920373"></a><a name="en-us_topic_0113746489_text1759675920373"></a>BMS</span><span id="en-us_topic_0113746489_text1159611597371"><a name="en-us_topic_0113746489_text1159611597371"></a><a name="en-us_topic_0113746489_text1159611597371"></a></span>. The API automatically adjusts the file system to adapt to the entire partition.</li></ul>
    </td>
    </tr>
    <tr id="row1117451016576"><td class="cellrowborder" valign="top" width="23.64%" headers="mcps1.1.4.1.1 "><p id="p3974163816576"><a name="p3974163816576"></a><a name="p3974163816576"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.1.4.1.2 "><p id="p6495609616576"><a name="p6495609616576"></a><a name="p6495609616576"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.4.1.3 "><p id="p2695244316576"><a name="p2695244316576"></a><a name="p2695244316576"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **flavor**  field data structure description

    <a name="table16383173"></a>
    <table><thead align="left"><tr id="row9359886"><th class="cellrowborder" valign="top" width="23.617638236176383%" id="mcps1.2.4.1.1"><p id="p4590244539"><a name="p4590244539"></a><a name="p4590244539"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.857114288571147%" id="mcps1.2.4.1.2"><p id="p1359319455312"><a name="p1359319455312"></a><a name="p1359319455312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.52524747525248%" id="mcps1.2.4.1.3"><p id="p26002415311"><a name="p26002415311"></a><a name="p26002415311"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23603084"><td class="cellrowborder" valign="top" width="23.617638236176383%" headers="mcps1.2.4.1.1 "><p id="p32801677"><a name="p32801677"></a><a name="p32801677"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.857114288571147%" headers="mcps1.2.4.1.2 "><p id="p60791181"><a name="p60791181"></a><a name="p60791181"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.52524747525248%" headers="mcps1.2.4.1.3 "><p id="p25138652"><a name="p25138652"></a><a name="p25138652"></a>Specifies the flavor ID.</p>
    </td>
    </tr>
    <tr id="row24921279"><td class="cellrowborder" valign="top" width="23.617638236176383%" headers="mcps1.2.4.1.1 "><p id="p5357756"><a name="p5357756"></a><a name="p5357756"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.857114288571147%" headers="mcps1.2.4.1.2 "><p id="p39382544194229"><a name="p39382544194229"></a><a name="p39382544194229"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.52524747525248%" headers="mcps1.2.4.1.3 "><p id="p60214201"><a name="p60214201"></a><a name="p60214201"></a>Specifies the shortcut link of the BMS flavor. For details, see <a href="#table66226203">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **image**  field data structure description

    <a name="table1258047620856"></a>
    <table><thead align="left"><tr id="row6041176320856"><th class="cellrowborder" valign="top" width="23.59%" id="mcps1.2.4.1.1"><p id="p138511149537"><a name="p138511149537"></a><a name="p138511149537"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.96%" id="mcps1.2.4.1.2"><p id="p1439013147533"><a name="p1439013147533"></a><a name="p1439013147533"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.449999999999996%" id="mcps1.2.4.1.3"><p id="p16396101410533"><a name="p16396101410533"></a><a name="p16396101410533"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4046402920856"><td class="cellrowborder" valign="top" width="23.59%" headers="mcps1.2.4.1.1 "><p id="p5636094120856"><a name="p5636094120856"></a><a name="p5636094120856"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.96%" headers="mcps1.2.4.1.2 "><p id="p183352620856"><a name="p183352620856"></a><a name="p183352620856"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p1429788720856"><a name="p1429788720856"></a><a name="p1429788720856"></a>Specifies the ID of the BMS image.</p>
    </td>
    </tr>
    <tr id="row6157211920856"><td class="cellrowborder" valign="top" width="23.59%" headers="mcps1.2.4.1.1 "><p id="p2128571520856"><a name="p2128571520856"></a><a name="p2128571520856"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.96%" headers="mcps1.2.4.1.2 "><p id="p4642138020856"><a name="p4642138020856"></a><a name="p4642138020856"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p203547420856"><a name="p203547420856"></a><a name="p203547420856"></a>Specifies the shortcut links of the BMS image. For details, see <a href="#table66226203">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **metadata**  field data structure description

    <a name="table2549048917552"></a>
    <table><thead align="left"><tr id="row5894027817552"><th class="cellrowborder" valign="top" width="24.782478247824784%" id="mcps1.2.4.1.1"><p id="p5705192625312"><a name="p5705192625312"></a><a name="p5705192625312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.012801280128013%" id="mcps1.2.4.1.2"><p id="p13707126155313"><a name="p13707126155313"></a><a name="p13707126155313"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.2047204720472%" id="mcps1.2.4.1.3"><p id="p1771411266532"><a name="p1771411266532"></a><a name="p1771411266532"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2346131617552"><td class="cellrowborder" valign="top" width="24.782478247824784%" headers="mcps1.2.4.1.1 "><p id="p2131841817552"><a name="p2131841817552"></a><a name="p2131841817552"></a>User-defined field key and value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.2.4.1.2 "><p id="p4907026417552"><a name="p4907026417552"></a><a name="p4907026417552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.2047204720472%" headers="mcps1.2.4.1.3 "><p id="p5719410617654"><a name="p5719410617654"></a><a name="p5719410617654"></a>Specifies the key and value pair of the metadata.</p>
    <p id="p4498490617654"><a name="p4498490617654"></a><a name="p4498490617654"></a>The maximum size for each metadata key and value pair is 255 bytes.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **links**  field data structure description

    <a name="table66226203"></a>
    <table><thead align="left"><tr id="row15444572"><th class="cellrowborder" valign="top" width="24.942494249424943%" id="mcps1.2.4.1.1"><p id="p15239143810536"><a name="p15239143810536"></a><a name="p15239143810536"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.162816281628167%" id="mcps1.2.4.1.2"><p id="p1924133845312"><a name="p1924133845312"></a><a name="p1924133845312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.89468946894689%" id="mcps1.2.4.1.3"><p id="p02471838115319"><a name="p02471838115319"></a><a name="p02471838115319"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26881137"><td class="cellrowborder" valign="top" width="24.942494249424943%" headers="mcps1.2.4.1.1 "><p id="p29888458"><a name="p29888458"></a><a name="p29888458"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.162816281628167%" headers="mcps1.2.4.1.2 "><p id="p6072445"><a name="p6072445"></a><a name="p6072445"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.89468946894689%" headers="mcps1.2.4.1.3 "><p id="p22106023"><a name="p22106023"></a><a name="p22106023"></a>Specifies the shortcut link marker name. The value can be:</p>
    <a name="ul207311644172510"></a><a name="ul207311644172510"></a><ul id="ul207311644172510"><li><strong id="en-us_topic_0131326852_b320113110516"><a name="en-us_topic_0131326852_b320113110516"></a><a name="en-us_topic_0131326852_b320113110516"></a>self</strong>: resource link that contains the version number. It is used when immediate tracing is required.</li><li><strong id="en-us_topic_0131326852_b84171947711"><a name="en-us_topic_0131326852_b84171947711"></a><a name="en-us_topic_0131326852_b84171947711"></a>bookmark</strong>: resource link that can be stored for a long time.</li></ul>
    </td>
    </tr>
    <tr id="row64736485"><td class="cellrowborder" valign="top" width="24.942494249424943%" headers="mcps1.2.4.1.1 "><p id="p9163943"><a name="p9163943"></a><a name="p9163943"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.162816281628167%" headers="mcps1.2.4.1.2 "><p id="p62201881"><a name="p62201881"></a><a name="p62201881"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.89468946894689%" headers="mcps1.2.4.1.3 "><p id="p5187609"><a name="p5187609"></a><a name="p5187609"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **addresses**  field data structure description

    <a name="table12204733"></a>
    <table><thead align="left"><tr id="row12924626"><th class="cellrowborder" valign="top" width="25.05749425057494%" id="mcps1.2.4.1.1"><p id="p166389551533"><a name="p166389551533"></a><a name="p166389551533"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.637136286371362%" id="mcps1.2.4.1.2"><p id="p1064205516532"><a name="p1064205516532"></a><a name="p1064205516532"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.305369463053694%" id="mcps1.2.4.1.3"><p id="p176491455165312"><a name="p176491455165312"></a><a name="p176491455165312"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2649692"><td class="cellrowborder" valign="top" width="25.05749425057494%" headers="mcps1.2.4.1.1 "><p id="p41262825165352"><a name="p41262825165352"></a><a name="p41262825165352"></a>VPC ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.637136286371362%" headers="mcps1.2.4.1.2 "><p id="p62308393194236"><a name="p62308393194236"></a><a name="p62308393194236"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.305369463053694%" headers="mcps1.2.4.1.3 "><p id="p63354276165352"><a name="p63354276165352"></a><a name="p63354276165352"></a>Specifies the ID of the VPC used by the BMS (the VPC name is a variable). For details, see <a href="#table12341194102918">Table 8</a>.</p>
    <p id="p33317573165352"><a name="p33317573165352"></a><a name="p33317573165352"></a>The value in the data structure is assigned private IP addresses in the VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** _VPC ID_  field data structure description

    <a name="table12341194102918"></a>
    <table><thead align="left"><tr id="row235171102918"><th class="cellrowborder" valign="top" width="25.532553255325535%" id="mcps1.2.4.1.1"><p id="p13293191195412"><a name="p13293191195412"></a><a name="p13293191195412"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.9028902890289%" id="mcps1.2.4.1.2"><p id="p132963112541"><a name="p132963112541"></a><a name="p132963112541"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.564556455645565%" id="mcps1.2.4.1.3"><p id="p630351114541"><a name="p630351114541"></a><a name="p630351114541"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10748082102918"><td class="cellrowborder" valign="top" width="25.532553255325535%" headers="mcps1.2.4.1.1 "><p id="p984890102947"><a name="p984890102947"></a><a name="p984890102947"></a>addr</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.2 "><p id="p12667285102947"><a name="p12667285102947"></a><a name="p12667285102947"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.564556455645565%" headers="mcps1.2.4.1.3 "><p id="p19417177102947"><a name="p19417177102947"></a><a name="p19417177102947"></a>Specifies the IP address.</p>
    </td>
    </tr>
    <tr id="row7305181102918"><td class="cellrowborder" valign="top" width="25.532553255325535%" headers="mcps1.2.4.1.1 "><p id="p62260628102947"><a name="p62260628102947"></a><a name="p62260628102947"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.2 "><p id="p9946116102947"><a name="p9946116102947"></a><a name="p9946116102947"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.564556455645565%" headers="mcps1.2.4.1.3 "><p id="p329048102947"><a name="p329048102947"></a><a name="p329048102947"></a>Specifies the version of the IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "server": {
            "tenant_id": "c685484a8cc2416b97260938705deb65",
            "image": {
                "links": [
                    {
                        "rel": "bookmark",
                        "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/images/1a6635d8-afea-4f2b-abb6-27a202bad319"
                    }
                ],
                "id": "1a6635d8-afea-4f2b-abb6-27a202bad319"
            },
            "accessIPv4": "",
            "addresses": {
                "08a7715f-7de6-4ff9-a343-95ba4209f24a": [
                    {
                        "addr": "192.168.0.107",
                        "version": 4
                    }
                ]
            },
            "metadata": {
                "op_svc_userid": "1311c433dd9b408886f57d695c229cbe"
            },
            "accessIPv6": "",
            "created": "2017-05-24T06:14:05Z",
            "hostId": "e9c3ee0fcc58ab6085cf30df70b5544eab958858fb50d925f023e53e",
            "flavor": {
                "links": [
                    {
                        "rel": "bookmark",
                        "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/flavors/physical.83.medium"
                    }
                ],
                "id": "physical.83.medium"
            },
            "OS-DCF:diskConfig": "MANUAL",
            "user_id": "1311c433dd9b408886f57d695c229cbe",
            "name": "new-server-test",
            "progress": 0,
            "links": [
                {
                    "rel": "self",
                    "href": "https://openstack.example.com/v2/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                },
                {
                    "rel": "bookmark",
                    "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                }
            ],
            "id": "95bf2490-5428-432c-ad9b-5e3406f869dd",
            "updated": "2017-05-25T03:40:25Z",
            "status": "ACTIVE"
        }
    }
    ```


## Returned Values<a name="section7610951"></a>

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

