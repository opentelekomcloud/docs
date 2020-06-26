# Querying Operations on an ECS<a name="EN-US_TOPIC_0065817692"></a>

## Function<a name="en-us_topic_0057973177_section4103816"></a>

This API is used to query all historical operations on an ECS.

## URI<a name="en-us_topic_0057973177_section36934348"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-instance-actions\{?limit,marker\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-instance-actions\{?limit,marker\}

[Table 1](#en-us_topic_0057973177_table32475667)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="en-us_topic_0057973177_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973177_row44937496"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973177_row1664874"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973177_p637140"><a name="en-us_topic_0057973177_p637140"></a><a name="en-us_topic_0057973177_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973177_p51608407"><a name="en-us_topic_0057973177_p51608407"></a><a name="en-us_topic_0057973177_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row41565035"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973177_p11324657"><a name="en-us_topic_0057973177_p11324657"></a><a name="en-us_topic_0057973177_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973177_p44882061"><a name="en-us_topic_0057973177_p44882061"></a><a name="en-us_topic_0057973177_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973177_p11568292"><a name="en-us_topic_0057973177_p11568292"></a><a name="en-us_topic_0057973177_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>Pagination query is supported in microversion 2.58 and later. The query results are displayed by the creation time \(**created\_at**\) of the records in descending order. If the creation time is not provided, the results are displayed by object ID in descending order. The number of records displayed on each page is  **limit**. If the value of  **limit**  exceeds the maximum number configured in Nova, the maximum number configured in Nova is returned.  

**Table  2**  Query parameters

<a name="en-us_topic_0057973177_table25375307161212"></a>
<table><thead align="left"><tr id="en-us_topic_0057973177_row19424792161212"><th class="cellrowborder" valign="top" width="16.72%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973177_p29904339161212"><a name="en-us_topic_0057973177_p29904339161212"></a><a name="en-us_topic_0057973177_p29904339161212"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973177_p6332407161212"><a name="en-us_topic_0057973177_p6332407161212"></a><a name="en-us_topic_0057973177_p6332407161212"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.63%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973177_p43162922161212"><a name="en-us_topic_0057973177_p43162922161212"></a><a name="en-us_topic_0057973177_p43162922161212"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973177_row6535831161212"><td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973177_p41698904161254"><a name="en-us_topic_0057973177_p41698904161254"></a><a name="en-us_topic_0057973177_p41698904161254"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973177_p22168062161254"><a name="en-us_topic_0057973177_p22168062161254"></a><a name="en-us_topic_0057973177_p22168062161254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973177_p50782568161254"><a name="en-us_topic_0057973177_p50782568161254"></a><a name="en-us_topic_0057973177_p50782568161254"></a>Specifies the upper limit on the number of returned results.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row64491372161218"><td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973177_p43508214161254"><a name="en-us_topic_0057973177_p43508214161254"></a><a name="en-us_topic_0057973177_p43508214161254"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973177_p34504442161254"><a name="en-us_topic_0057973177_p34504442161254"></a><a name="en-us_topic_0057973177_p34504442161254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973177_p43396447161254"><a name="en-us_topic_0057973177_p43396447161254"></a><a name="en-us_topic_0057973177_p43396447161254"></a>Specifies that marker that points to the operation. The query starts from the next piece of data indexed by this parameter.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section05103585194"></a>

None

## Response<a name="en-us_topic_0057973177_section63261583"></a>

[Table 3](#en-us_topic_0057973177_table2407422)  describes the response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0057973177_table2407422"></a>
<table><thead align="left"><tr id="en-us_topic_0057973177_row9003795"><th class="cellrowborder" valign="top" width="18.22%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973177_p58218801"><a name="en-us_topic_0057973177_p58218801"></a><a name="en-us_topic_0057973177_p58218801"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.21%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973177_p57014808"><a name="en-us_topic_0057973177_p57014808"></a><a name="en-us_topic_0057973177_p57014808"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973177_p18102480"><a name="en-us_topic_0057973177_p18102480"></a><a name="en-us_topic_0057973177_p18102480"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.57000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973177_p54796720"><a name="en-us_topic_0057973177_p54796720"></a><a name="en-us_topic_0057973177_p54796720"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973177_row9349312"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p19096817"><a name="en-us_topic_0057973177_p19096817"></a><a name="en-us_topic_0057973177_p19096817"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p1970644"><a name="en-us_topic_0057973177_p1970644"></a><a name="en-us_topic_0057973177_p1970644"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p3338346"><a name="en-us_topic_0057973177_p3338346"></a><a name="en-us_topic_0057973177_p3338346"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p25404503"><a name="en-us_topic_0057973177_p25404503"></a><a name="en-us_topic_0057973177_p25404503"></a>Specifies the action.</p>
<p id="en-us_topic_0057973177_p490215356174"><a name="en-us_topic_0057973177_p490215356174"></a><a name="en-us_topic_0057973177_p490215356174"></a>Options:</p>
<p id="en-us_topic_0057973177_p127002371171"><a name="en-us_topic_0057973177_p127002371171"></a><a name="en-us_topic_0057973177_p127002371171"></a><strong id="b842352706173827"><a name="b842352706173827"></a><a name="b842352706173827"></a>create</strong>, <strong id="b842352706173830"><a name="b842352706173830"></a><a name="b842352706173830"></a>delete</strong>, <strong id="b842352706173834"><a name="b842352706173834"></a><a name="b842352706173834"></a>evacuate</strong>, <strong id="b842352706173837"><a name="b842352706173837"></a><a name="b842352706173837"></a>restore</strong>, <strong id="b842352706173842"><a name="b842352706173842"></a><a name="b842352706173842"></a>stop</strong>, <strong id="b842352706173846"><a name="b842352706173846"></a><a name="b842352706173846"></a>start</strong>, <strong id="b842352706173849"><a name="b842352706173849"></a><a name="b842352706173849"></a>reboot</strong>, <strong id="b842352706173854"><a name="b842352706173854"></a><a name="b842352706173854"></a>rebuild</strong>, <strong id="b842352706173857"><a name="b842352706173857"></a><a name="b842352706173857"></a>revertResize</strong>, <strong id="b84235270617392"><a name="b84235270617392"></a><a name="b84235270617392"></a>confirmResize</strong>, <strong id="b84235270617397"><a name="b84235270617397"></a><a name="b84235270617397"></a>detach_volume</strong>, <strong id="b842352706173910"><a name="b842352706173910"></a><a name="b842352706173910"></a>attach_volume</strong>, <strong id="b842352706173914"><a name="b842352706173914"></a><a name="b842352706173914"></a>attach_interface</strong>, <strong id="b842352706173917"><a name="b842352706173917"></a><a name="b842352706173917"></a>detach_interface</strong>, <strong id="b842352706173920"><a name="b842352706173920"></a><a name="b842352706173920"></a>lock</strong>, <strong id="b842352706173924"><a name="b842352706173924"></a><a name="b842352706173924"></a>unlock</strong>, <strong id="b842352706173928"><a name="b842352706173928"></a><a name="b842352706173928"></a>resize</strong>, <strong id="b842352706173932"><a name="b842352706173932"></a><a name="b842352706173932"></a>migrate</strong>, <strong id="b842352706173937"><a name="b842352706173937"></a><a name="b842352706173937"></a>pause</strong>, <strong id="b842352706173941"><a name="b842352706173941"></a><a name="b842352706173941"></a>unpause</strong>, <strong id="b842352706173945"><a name="b842352706173945"></a><a name="b842352706173945"></a>suspend</strong>, <strong id="b842352706173948"><a name="b842352706173948"></a><a name="b842352706173948"></a>resume</strong>, <strong id="b842352706173952"><a name="b842352706173952"></a><a name="b842352706173952"></a>rescue</strong>, <strong id="b842352706173956"><a name="b842352706173956"></a><a name="b842352706173956"></a>unrescue</strong>, <strong id="b84235270617400"><a name="b84235270617400"></a><a name="b84235270617400"></a>changePassword</strong>, <strong id="b84235270617404"><a name="b84235270617404"></a><a name="b84235270617404"></a>shelve</strong>, <strong id="b84235270617407"><a name="b84235270617407"></a><a name="b84235270617407"></a>unshelve</strong>, <strong id="b842352706174010"><a name="b842352706174010"></a><a name="b842352706174010"></a>live-migration</strong>, <strong id="b842352706174015"><a name="b842352706174015"></a><a name="b842352706174015"></a>live_migration_cancel</strong>, <strong id="b842352706174018"><a name="b842352706174018"></a><a name="b842352706174018"></a>live_migration_force_complete</strong>, <strong id="b842352706174023"><a name="b842352706174023"></a><a name="b842352706174023"></a>trigger_crash_dump</strong>, and <strong id="b842352706174025"><a name="b842352706174025"></a><a name="b842352706174025"></a>extend_volume</strong></p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row27313937"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p64945259"><a name="en-us_topic_0057973177_p64945259"></a><a name="en-us_topic_0057973177_p64945259"></a>instance_uuid</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p31668621"><a name="en-us_topic_0057973177_p31668621"></a><a name="en-us_topic_0057973177_p31668621"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p26074609"><a name="en-us_topic_0057973177_p26074609"></a><a name="en-us_topic_0057973177_p26074609"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p15021476"><a name="en-us_topic_0057973177_p15021476"></a><a name="en-us_topic_0057973177_p15021476"></a>Specifies the ECS ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row975562"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p11911720"><a name="en-us_topic_0057973177_p11911720"></a><a name="en-us_topic_0057973177_p11911720"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p38078364"><a name="en-us_topic_0057973177_p38078364"></a><a name="en-us_topic_0057973177_p38078364"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p25325238"><a name="en-us_topic_0057973177_p25325238"></a><a name="en-us_topic_0057973177_p25325238"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p64448643"><a name="en-us_topic_0057973177_p64448643"></a><a name="en-us_topic_0057973177_p64448643"></a>Specifies the result status of the operation.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row43166878"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p6856233"><a name="en-us_topic_0057973177_p6856233"></a><a name="en-us_topic_0057973177_p6856233"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p20807076"><a name="en-us_topic_0057973177_p20807076"></a><a name="en-us_topic_0057973177_p20807076"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p18483976"><a name="en-us_topic_0057973177_p18483976"></a><a name="en-us_topic_0057973177_p18483976"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p7651556"><a name="en-us_topic_0057973177_p7651556"></a><a name="en-us_topic_0057973177_p7651556"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row1755141"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p7948727"><a name="en-us_topic_0057973177_p7948727"></a><a name="en-us_topic_0057973177_p7948727"></a>request_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p8012684"><a name="en-us_topic_0057973177_p8012684"></a><a name="en-us_topic_0057973177_p8012684"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p39867137"><a name="en-us_topic_0057973177_p39867137"></a><a name="en-us_topic_0057973177_p39867137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p45047680"><a name="en-us_topic_0057973177_p45047680"></a><a name="en-us_topic_0057973177_p45047680"></a>Specifies the request ID.</p>
</td>
</tr>
<tr id="row45783415114"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="p11991373115"><a name="p11991373115"></a><a name="p11991373115"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="p15104197815"><a name="p15104197815"></a><a name="p15104197815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1510215718114"><a name="p1510215718114"></a><a name="p1510215718114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="p310597113"><a name="p310597113"></a><a name="p310597113"></a>Specifies the time when the information was updated.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row2775936"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p23524259"><a name="en-us_topic_0057973177_p23524259"></a><a name="en-us_topic_0057973177_p23524259"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p59388871"><a name="en-us_topic_0057973177_p59388871"></a><a name="en-us_topic_0057973177_p59388871"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p26416835"><a name="en-us_topic_0057973177_p26416835"></a><a name="en-us_topic_0057973177_p26416835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p45769240"><a name="en-us_topic_0057973177_p45769240"></a><a name="en-us_topic_0057973177_p45769240"></a>Specifies the time when the action was started.</p>
</td>
</tr>
<tr id="en-us_topic_0057973177_row9269976"><td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973177_p12670598"><a name="en-us_topic_0057973177_p12670598"></a><a name="en-us_topic_0057973177_p12670598"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973177_p51026317"><a name="en-us_topic_0057973177_p51026317"></a><a name="en-us_topic_0057973177_p51026317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973177_p19685557"><a name="en-us_topic_0057973177_p19685557"></a><a name="en-us_topic_0057973177_p19685557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973177_p39490997"><a name="en-us_topic_0057973177_p39490997"></a><a name="en-us_topic_0057973177_p39490997"></a>Specifies the user ID.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973177_section32483342"></a>

```
GET https://{endpoint}/v2/89655fe61c4c4a08b9f3e7f9095441b8/servers/e723eb40-f56e-40f9-8c8c-caa517fe06ba/os-instance-actions
GET https://{endpoint}/v2.1/89655fe61c4c4a08b9f3e7f9095441b8/servers/e723eb40-f56e-40f9-8c8c-caa517fe06ba/os-instance-actions
```

## Example Response<a name="section10181122219535"></a>

```
{
    "instanceActions": [
        {
            "instance_uuid": "e723eb40-f56e-40f9-8c8c-caa517fe06ba",
            "user_id": "752be40780484291a9cc7ae50fff3e6d",
            "start_time": "2014-12-16T10:58:14.000000",
            "request_id": "req-ee56c2b5-d33b-4749-ae83-09281dbbb716",
            "action": "resize",
            "message": "Error",
            "project_id": "89655fe61c4c4a08b9f3e7f9095441b8"
        },
        {
            "instance_uuid": "e723eb40-f56e-40f9-8c8c-caa517fe06ba",
            "user_id": "752be40780484291a9cc7ae50fff3e6d",
            "start_time": "2014-12-16T10:57:56.000000",
            "request_id": "req-23cfd57f-c58a-45cd-86a6-eab3e38f3753",
            "action": "resize",
            "message": "Error",
            "project_id": "89655fe61c4c4a08b9f3e7f9095441b8"
        },
    ]
}
```

## Returned Values<a name="en-us_topic_0057973177_section1642564"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

