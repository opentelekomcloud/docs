# Querying Load Balancer or Listener Quotas<a name="EN-US_TOPIC_0096561521"></a>

## Function<a name="en-us_topic_0020100174_section33734921"></a>

This API is used to query the load balancer or listener quotas.

## URI<a name="en-us_topic_0020100174_section35178835"></a>

GET /v1.0/\{project\_id\}/elbaas/quotas

**Table  1**  Parameter description

<a name="en-us_topic_0020100174_table618348671617"></a>
<table><thead align="left"><tr id="en-us_topic_0020100174_row536444891617"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100174_p502363201617"><a name="en-us_topic_0020100174_p502363201617"></a><a name="en-us_topic_0020100174_p502363201617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100174_p426101401617"><a name="en-us_topic_0020100174_p426101401617"></a><a name="en-us_topic_0020100174_p426101401617"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100174_p288693491617"><a name="en-us_topic_0020100174_p288693491617"></a><a name="en-us_topic_0020100174_p288693491617"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100174_p567159381617"><a name="en-us_topic_0020100174_p567159381617"></a><a name="en-us_topic_0020100174_p567159381617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100174_row305882841617"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p87851816121312"><a name="p87851816121312"></a><a name="p87851816121312"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100174_p342304371617"><a name="en-us_topic_0020100174_p342304371617"></a><a name="en-us_topic_0020100174_p342304371617"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100174_p212019881617"><a name="en-us_topic_0020100174_p212019881617"></a><a name="en-us_topic_0020100174_p212019881617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100174_p396394561617"><a name="en-us_topic_0020100174_p396394561617"></a><a name="en-us_topic_0020100174_p396394561617"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100174_section48174063"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100174_section30913391"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100174_table951448410185"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100174_row269956210185"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100174_p1733794910185"><a name="en-us_topic_0020100174_p1733794910185"></a><a name="en-us_topic_0020100174_p1733794910185"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100174_p6219660010185"><a name="en-us_topic_0020100174_p6219660010185"></a><a name="en-us_topic_0020100174_p6219660010185"></a><strong id="b1016279634"><a name="b1016279634"></a><a name="b1016279634"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100174_p475984410185"><a name="en-us_topic_0020100174_p475984410185"></a><a name="en-us_topic_0020100174_p475984410185"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100174_row410792510185"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p6430652610185"><a name="en-us_topic_0020100174_p6430652610185"></a><a name="en-us_topic_0020100174_p6430652610185"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p4144608710185"><a name="en-us_topic_0020100174_p4144608710185"></a><a name="en-us_topic_0020100174_p4144608710185"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p168984810185"><a name="en-us_topic_0020100174_p168984810185"></a><a name="en-us_topic_0020100174_p168984810185"></a>Specifies the resource quotas.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **quotas**  parameter description

    <a name="en-us_topic_0020100174_table40566376102127"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100174_row47343998102127"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100174_p9658647102127"><a name="en-us_topic_0020100174_p9658647102127"></a><a name="en-us_topic_0020100174_p9658647102127"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100174_p44152912102127"><a name="en-us_topic_0020100174_p44152912102127"></a><a name="en-us_topic_0020100174_p44152912102127"></a><strong id="b1945712773"><a name="b1945712773"></a><a name="b1945712773"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100174_p19616081102127"><a name="en-us_topic_0020100174_p19616081102127"></a><a name="en-us_topic_0020100174_p19616081102127"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100174_row45398723102127"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p53417933102127"><a name="en-us_topic_0020100174_p53417933102127"></a><a name="en-us_topic_0020100174_p53417933102127"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p31885336102127"><a name="en-us_topic_0020100174_p31885336102127"></a><a name="en-us_topic_0020100174_p31885336102127"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p24743468102127"><a name="en-us_topic_0020100174_p24743468102127"></a><a name="en-us_topic_0020100174_p24743468102127"></a>Lists the resource quotas.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **resources**  parameter description

    <a name="en-us_topic_0020100174_table5936749910208"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100174_row3030106010208"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100174_p3846681610208"><a name="en-us_topic_0020100174_p3846681610208"></a><a name="en-us_topic_0020100174_p3846681610208"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100174_p2880442510208"><a name="en-us_topic_0020100174_p2880442510208"></a><a name="en-us_topic_0020100174_p2880442510208"></a><strong id="b34131932"><a name="b34131932"></a><a name="b34131932"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100174_p5145709410208"><a name="en-us_topic_0020100174_p5145709410208"></a><a name="en-us_topic_0020100174_p5145709410208"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100174_row727510410208"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p5241254210208"><a name="en-us_topic_0020100174_p5241254210208"></a><a name="en-us_topic_0020100174_p5241254210208"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p1755751310208"><a name="en-us_topic_0020100174_p1755751310208"></a><a name="en-us_topic_0020100174_p1755751310208"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p1287242410208"><a name="en-us_topic_0020100174_p1287242410208"></a><a name="en-us_topic_0020100174_p1287242410208"></a>Specifies the resource type. The value can be <strong id="b842352706173642"><a name="b842352706173642"></a><a name="b842352706173642"></a>elb</strong> or <strong id="b842352706173646"><a name="b842352706173646"></a><a name="b842352706173646"></a>listener</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row4874295510208"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p5586525210208"><a name="en-us_topic_0020100174_p5586525210208"></a><a name="en-us_topic_0020100174_p5586525210208"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p2879152510208"><a name="en-us_topic_0020100174_p2879152510208"></a><a name="en-us_topic_0020100174_p2879152510208"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p5041218310208"><a name="en-us_topic_0020100174_p5041218310208"></a><a name="en-us_topic_0020100174_p5041218310208"></a>Specifies the quantity of used resources.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row5105646510208"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p4193303910208"><a name="en-us_topic_0020100174_p4193303910208"></a><a name="en-us_topic_0020100174_p4193303910208"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p4113300910208"><a name="en-us_topic_0020100174_p4113300910208"></a><a name="en-us_topic_0020100174_p4113300910208"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p4343945610208"><a name="en-us_topic_0020100174_p4343945610208"></a><a name="en-us_topic_0020100174_p4343945610208"></a>Specifies the total resource quotas.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row296714099521"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p545739069521"><a name="en-us_topic_0020100174_p545739069521"></a><a name="en-us_topic_0020100174_p545739069521"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p584102979521"><a name="en-us_topic_0020100174_p584102979521"></a><a name="en-us_topic_0020100174_p584102979521"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p336135799521"><a name="en-us_topic_0020100174_p336135799521"></a><a name="en-us_topic_0020100174_p336135799521"></a>Specifies the maximum number of resources.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row90942879526"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100174_p655486439526"><a name="en-us_topic_0020100174_p655486439526"></a><a name="en-us_topic_0020100174_p655486439526"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100174_p78398969526"><a name="en-us_topic_0020100174_p78398969526"></a><a name="en-us_topic_0020100174_p78398969526"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100174_p310518629526"><a name="en-us_topic_0020100174_p310518629526"></a><a name="en-us_topic_0020100174_p310518629526"></a>Specifies the minimum number of resources.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "quotas": {
            "resources": [
                {
                    "type": "elb",
                    "used": 2,
                    "quota": 5,
                    "max": 100,
                    "min": 1
                },
                {
                    "type": "listener",
                    "quota": 5,
                    "max": 200,
                    "min": 1
                }
            ]
        }
    }
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The  **used**  parameter is unavailable for listeners, for which an empty character string is returned.  


## Status Code<a name="en-us_topic_0020100174_section9785067"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100174_table45362997151624"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100174_row56461172151624"><th class="cellrowborder" valign="top" width="10.299999999999999%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100174_p9952202151624"><a name="en-us_topic_0020100174_p9952202151624"></a><a name="en-us_topic_0020100174_p9952202151624"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.46%" id="mcps1.1.4.1.2"><p id="p18704142212229"><a name="p18704142212229"></a><a name="p18704142212229"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100174_p822070151624"><a name="en-us_topic_0020100174_p822070151624"></a><a name="en-us_topic_0020100174_p822070151624"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100174_row66587677151624"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100174_p24892777151624"><a name="en-us_topic_0020100174_p24892777151624"></a><a name="en-us_topic_0020100174_p24892777151624"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p7639433202219"><a name="p7639433202219"></a><a name="p7639433202219"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100174_p3049090151624"><a name="en-us_topic_0020100174_p3049090151624"></a><a name="en-us_topic_0020100174_p3049090151624"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row27441815151624"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100174_p8194509151624"><a name="en-us_topic_0020100174_p8194509151624"></a><a name="en-us_topic_0020100174_p8194509151624"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p18639103312225"><a name="p18639103312225"></a><a name="p18639103312225"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100174_p59775492151624"><a name="en-us_topic_0020100174_p59775492151624"></a><a name="en-us_topic_0020100174_p59775492151624"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row1108519151624"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100174_p22681218151624"><a name="en-us_topic_0020100174_p22681218151624"></a><a name="en-us_topic_0020100174_p22681218151624"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p26391233102211"><a name="p26391233102211"></a><a name="p26391233102211"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100174_p25239345151624"><a name="en-us_topic_0020100174_p25239345151624"></a><a name="en-us_topic_0020100174_p25239345151624"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row25827516151624"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100174_p11654021151624"><a name="en-us_topic_0020100174_p11654021151624"></a><a name="en-us_topic_0020100174_p11654021151624"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p1163943313228"><a name="p1163943313228"></a><a name="p1163943313228"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100174_p4451606151624"><a name="en-us_topic_0020100174_p4451606151624"></a><a name="en-us_topic_0020100174_p4451606151624"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row40064457151624"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100174_p23995610151624"><a name="en-us_topic_0020100174_p23995610151624"></a><a name="en-us_topic_0020100174_p23995610151624"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p96391733112217"><a name="p96391733112217"></a><a name="p96391733112217"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100174_p64596296151624"><a name="en-us_topic_0020100174_p64596296151624"></a><a name="en-us_topic_0020100174_p64596296151624"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100174_row44495757151624"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100174_p47386577151624"><a name="en-us_topic_0020100174_p47386577151624"></a><a name="en-us_topic_0020100174_p47386577151624"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p1864093382212"><a name="p1864093382212"></a><a name="p1864093382212"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100174_p13107492151624"><a name="en-us_topic_0020100174_p13107492151624"></a><a name="en-us_topic_0020100174_p13107492151624"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


