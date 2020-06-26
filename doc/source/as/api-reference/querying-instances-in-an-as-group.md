# Querying Instances in an AS Group<a name="EN-US_TOPIC_0043063045"></a>

## Function<a name="section11009764"></a>

This interface is used to query instances in an AS group based on search criteria. The results are displayed by page.

-   Search criteria can be the instance lifecycle status, instance health status, instance protection status, start line number, and number of records in the AS group.
-   If no search criteria are specified, a maximum of 20 instances in an AS group can be queried by default.

## URI<a name="section31979016"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_group\_instance/\{scaling\_group\_id\}/list

>![](/images/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. Instances in an AS group can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="table2199097"></a>
<table><thead align="left"><tr id="row41000636"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.5.1.1"><p id="p32717189"><a name="p32717189"></a><a name="p32717189"></a><strong id="b3103143417515"><a name="b3103143417515"></a><a name="b3103143417515"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p32846614"><a name="p32846614"></a><a name="p32846614"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p43330072"><a name="p43330072"></a><a name="p43330072"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="p20074930"><a name="p20074930"></a><a name="p20074930"></a><strong id="b7757123411513"><a name="b7757123411513"></a><a name="b7757123411513"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row15456653"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p44029393"><a name="p44029393"></a><a name="p44029393"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p9611044"><a name="p9611044"></a><a name="p9611044"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p40297137"><a name="p40297137"></a><a name="p40297137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row50039568"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p26673201"><a name="p26673201"></a><a name="p26673201"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p13045638"><a name="p13045638"></a><a name="p13045638"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p50063735"><a name="p50063735"></a><a name="p50063735"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p28630766"><a name="p28630766"></a><a name="p28630766"></a>Specifies the AS group ID.</p>
</td>
</tr>
<tr id="row56350302"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p971734"><a name="p971734"></a><a name="p971734"></a>life_cycle_state</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p11601606"><a name="p11601606"></a><a name="p11601606"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p206039"><a name="p206039"></a><a name="p206039"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p16689200"><a name="p16689200"></a><a name="p16689200"></a>Specifies the instance lifecycle status in the AS group.</p>
<a name="ul16908952165812"></a><a name="ul16908952165812"></a><ul id="ul16908952165812"><li><strong id="b7576229175212"><a name="b7576229175212"></a><a name="b7576229175212"></a>INSERVICE</strong>: The instance is enabled.</li><li><strong id="b32258777144837"><a name="b32258777144837"></a><a name="b32258777144837"></a>PENDING</strong>: The instance is being added to the AS group.</li><li><strong id="b6394292144837"><a name="b6394292144837"></a><a name="b6394292144837"></a>REMOVING</strong>: The instance is being removed from the AS group.</li></ul>
</td>
</tr>
<tr id="row19723089"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p54066375"><a name="p54066375"></a><a name="p54066375"></a>health_status</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p17300225"><a name="p17300225"></a><a name="p17300225"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p59140967"><a name="p59140967"></a><a name="p59140967"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p25689059"><a name="p25689059"></a><a name="p25689059"></a>Specifies the instance health status.</p>
<a name="ul2121610719490"></a><a name="ul2121610719490"></a><ul id="ul2121610719490"><li><strong id="b28797747144837"><a name="b28797747144837"></a><a name="b28797747144837"></a>INITIALIZING</strong>: The instance is initializing.</li><li><strong id="b53754535164857"><a name="b53754535164857"></a><a name="b53754535164857"></a>NORMAL</strong>: The instance is normal.</li><li><strong id="b66749771144837"><a name="b66749771144837"></a><a name="b66749771144837"></a>ERROR</strong>: The instance is abnormal.</li></ul>
</td>
</tr>
<tr id="row46771154174315"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p3654134174417"><a name="p3654134174417"></a><a name="p3654134174417"></a>protect_from_scaling_down</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p76772547430"><a name="p76772547430"></a><a name="p76772547430"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p367712544434"><a name="p367712544434"></a><a name="p367712544434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p492652064618"><a name="p492652064618"></a><a name="p492652064618"></a>Specifies the instance protection status.</p>
<a name="ul19319440184514"></a><a name="ul19319440184514"></a><ul id="ul19319440184514"><li><strong id="b867617538920"><a name="b867617538920"></a><a name="b867617538920"></a>true</strong>: Instance protection is enabled.</li><li><strong id="b14933121091013"><a name="b14933121091013"></a><a name="b14933121091013"></a>false</strong>: Instance protection is disabled.</li></ul>
</td>
</tr>
<tr id="row439002"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p35559222"><a name="p35559222"></a><a name="p35559222"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p61724767"><a name="p61724767"></a><a name="p61724767"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p33650236"><a name="p33650236"></a><a name="p33650236"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b386112519475"><a name="b386112519475"></a><a name="b386112519475"></a>0</strong>. The minimum parameter value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>.</p>
</td>
</tr>
<tr id="row36287209"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p53582808"><a name="p53582808"></a><a name="p53582808"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p45240216"><a name="p45240216"></a><a name="p45240216"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p40578897"><a name="p40578897"></a><a name="p40578897"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b168447885495335"><a name="b168447885495335"></a><a name="b168447885495335"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section19375690"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query enabled, healthy instances in the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_instance/e5d27f5c-dd76-4a61-b4bc-a67c5686719a/list?life_cycle_state=INSERVICE&health_status=NORMAL
    ```


## Response Message<a name="section40163483"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table61002694"></a>
    <table><thead align="left"><tr id="row47328638"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p8414476"><a name="p8414476"></a><a name="p8414476"></a><strong id="b1496023515516"><a name="b1496023515516"></a><a name="b1496023515516"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8%" id="mcps1.2.4.1.2"><p id="p10483995"><a name="p10483995"></a><a name="p10483995"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="p43897299"><a name="p43897299"></a><a name="p43897299"></a><strong id="b125654017512"><a name="b125654017512"></a><a name="b125654017512"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66020315"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p46045275"><a name="p46045275"></a><a name="p46045275"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.4.1.2 "><p id="p38679804"><a name="p38679804"></a><a name="p38679804"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p46056421"><a name="p46056421"></a><a name="p46056421"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="row11854613"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p20699582"><a name="p20699582"></a><a name="p20699582"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.4.1.2 "><p id="p66053444"><a name="p66053444"></a><a name="p66053444"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p48728718"><a name="p48728718"></a><a name="p48728718"></a>Specifies the start line number.</p>
    </td>
    </tr>
    <tr id="row35905280"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p22646572"><a name="p22646572"></a><a name="p22646572"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.4.1.2 "><p id="p22433040"><a name="p22433040"></a><a name="p22433040"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p5136981"><a name="p5136981"></a><a name="p5136981"></a>Specifies the maximum number of resources to be queried.</p>
    </td>
    </tr>
    <tr id="row46232835"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p53872188"><a name="p53872188"></a><a name="p53872188"></a>scaling_group_instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.4.1.2 "><p id="p1571113"><a name="p1571113"></a><a name="p1571113"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p60151347"><a name="p60151347"></a><a name="p60151347"></a>Specifies details about the instances in the AS group.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_group\_instances**  field description

    <a name="table4301093319610"></a>
    <table><thead align="left"><tr id="r70742bbfa8934fe3957ce895a04570ec"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="a51abf2e749334c12a9e69960b71588a2"><a name="a51abf2e749334c12a9e69960b71588a2"></a><a name="a51abf2e749334c12a9e69960b71588a2"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="9%" id="mcps1.2.4.1.2"><p id="a4e2cd975880e41e5a0537ae1ac9d2283"><a name="a4e2cd975880e41e5a0537ae1ac9d2283"></a><a name="a4e2cd975880e41e5a0537ae1ac9d2283"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="acf4271098e944ce5bc43281cb9c1e6a8"><a name="acf4271098e944ce5bc43281cb9c1e6a8"></a><a name="acf4271098e944ce5bc43281cb9c1e6a8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rfcae682d9e4e45bb8ce4ecb16a18903c"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a07006dc0e72c4cf598e1310e2aa245c2"><a name="a07006dc0e72c4cf598e1310e2aa245c2"></a><a name="a07006dc0e72c4cf598e1310e2aa245c2"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="a535b15d9353a4e1485ab8990acd661a4"><a name="a535b15d9353a4e1485ab8990acd661a4"></a><a name="a535b15d9353a4e1485ab8990acd661a4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="aec2b3792d52346d9a003c86ac718fb20"><a name="aec2b3792d52346d9a003c86ac718fb20"></a><a name="aec2b3792d52346d9a003c86ac718fb20"></a>Specifies the instance ID.</p>
    </td>
    </tr>
    <tr id="r0f2d64e3d3564ce78467b4bcbab0f33e"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="abbab6a7a28354d7abb2aba09b8e901c4"><a name="abbab6a7a28354d7abb2aba09b8e901c4"></a><a name="abbab6a7a28354d7abb2aba09b8e901c4"></a>instance_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="a8288d1f758f340d0ad8eba28e003ac34"><a name="a8288d1f758f340d0ad8eba28e003ac34"></a><a name="a8288d1f758f340d0ad8eba28e003ac34"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a7666cce4ea544c108b300ab0e798cb55"><a name="a7666cce4ea544c108b300ab0e798cb55"></a><a name="a7666cce4ea544c108b300ab0e798cb55"></a>Specifies the instance name.</p>
    </td>
    </tr>
    <tr id="rf5cebf370db44b4da8908094f1e9a3f0"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a70f999e778734195ba3a7e43d4b6f6c0"><a name="a70f999e778734195ba3a7e43d4b6f6c0"></a><a name="a70f999e778734195ba3a7e43d4b6f6c0"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="a62d0ceed255e4dd1901b5142934baa2b"><a name="a62d0ceed255e4dd1901b5142934baa2b"></a><a name="a62d0ceed255e4dd1901b5142934baa2b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="ad53add0be41b4377ab799a88e1a4f907"><a name="ad53add0be41b4377ab799a88e1a4f907"></a><a name="ad53add0be41b4377ab799a88e1a4f907"></a>Specifies the ID of the AS group to which the instance belongs.</p>
    </td>
    </tr>
    <tr id="r5b7c40ac38534849babc98db78b57a06"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a5946a55e48ac49fdb0dcabe1bfe8b0c4"><a name="a5946a55e48ac49fdb0dcabe1bfe8b0c4"></a><a name="a5946a55e48ac49fdb0dcabe1bfe8b0c4"></a>scaling_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="accfabda9fb3a4a718a16c3e6400e2dc6"><a name="accfabda9fb3a4a718a16c3e6400e2dc6"></a><a name="accfabda9fb3a4a718a16c3e6400e2dc6"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a44ecf06e09864853b6029c95aeee72e1"><a name="a44ecf06e09864853b6029c95aeee72e1"></a><a name="a44ecf06e09864853b6029c95aeee72e1"></a>Specifies the name of the AS group to which the instance belongs.</p>
    <p id="p999344172010"><a name="p999344172010"></a><a name="p999344172010"></a>Supports fuzzy search. </p>
    </td>
    </tr>
    <tr id="r373dcb3a77874f1da86f19760410fc3c"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a31b8072135084adab4d8459c50e2be87"><a name="a31b8072135084adab4d8459c50e2be87"></a><a name="a31b8072135084adab4d8459c50e2be87"></a>life_cycle_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="a10fa21308bce4fd081701959df3071dd"><a name="a10fa21308bce4fd081701959df3071dd"></a><a name="a10fa21308bce4fd081701959df3071dd"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a9e042ac9129a4862b60266587156df95"><a name="a9e042ac9129a4862b60266587156df95"></a><a name="a9e042ac9129a4862b60266587156df95"></a>Specifies the instance lifecycle status in the AS group.</p>
    <a name="uac0ce6a3969645c692634f64204824b3"></a><a name="uac0ce6a3969645c692634f64204824b3"></a><ul id="uac0ce6a3969645c692634f64204824b3"><li><strong id="b707262049"><a name="b707262049"></a><a name="b707262049"></a>INSERVICE</strong>: The instance is enabled.</li><li><strong id="b1143242"><a name="b1143242"></a><a name="b1143242"></a>PENDING</strong>: The instance is being added to the AS group.</li><li><strong id="b1773752507"><a name="b1773752507"></a><a name="b1773752507"></a>REMOVING</strong>: The instance is being removed from the AS group.</li></ul>
    </td>
    </tr>
    <tr id="ra6696eb6fe0947e9a6bce923cc8a0b59"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a12384583db9049b1952a1dbaeaccce72"><a name="a12384583db9049b1952a1dbaeaccce72"></a><a name="a12384583db9049b1952a1dbaeaccce72"></a>health_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="a1ee76e9c66ab4fd5ad5b1a16f1acc98e"><a name="a1ee76e9c66ab4fd5ad5b1a16f1acc98e"></a><a name="a1ee76e9c66ab4fd5ad5b1a16f1acc98e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="af8406dc507624ef69b4ff65754839108"><a name="af8406dc507624ef69b4ff65754839108"></a><a name="af8406dc507624ef69b4ff65754839108"></a>Specifies the instance health status.</p>
    <a name="ul4917121148"></a><a name="ul4917121148"></a><ul id="ul4917121148"><li><strong id="b1786810096"><a name="b1786810096"></a><a name="b1786810096"></a>INITIALIZING</strong>: The instance is being initialized.</li><li><strong id="b1794210403"><a name="b1794210403"></a><a name="b1794210403"></a>NORMAL</strong>: The instance is functional.</li><li><strong id="b1188911552548"><a name="b1188911552548"></a><a name="b1188911552548"></a>ERROR</strong>: The instance is faulty.</li></ul>
    </td>
    </tr>
    <tr id="rcd738bb778b14235ad52e8cc6ad70220"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a932b15635ce748f3bb97a72fa5e4061d"><a name="a932b15635ce748f3bb97a72fa5e4061d"></a><a name="a932b15635ce748f3bb97a72fa5e4061d"></a>scaling_configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="adcb19276fe2544ccb68d4015cfdaebfa"><a name="adcb19276fe2544ccb68d4015cfdaebfa"></a><a name="adcb19276fe2544ccb68d4015cfdaebfa"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="abc2d2c7a7535454a9606ca2717281a73"><a name="abc2d2c7a7535454a9606ca2717281a73"></a><a name="abc2d2c7a7535454a9606ca2717281a73"></a>Specifies the AS configuration name.</p>
    </td>
    </tr>
    <tr id="r4c087e502ab2447da75306c3917c009c"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a3818e07041df414b982d5a06ca416a08"><a name="a3818e07041df414b982d5a06ca416a08"></a><a name="a3818e07041df414b982d5a06ca416a08"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="ae907ae4b54244f2198d4fd28f2ddff91"><a name="ae907ae4b54244f2198d4fd28f2ddff91"></a><a name="ae907ae4b54244f2198d4fd28f2ddff91"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p442107134311"><a name="p442107134311"></a><a name="p442107134311"></a>Specifies the AS configuration ID.</p>
    <p id="p1076493254318"><a name="p1076493254318"></a><a name="p1076493254318"></a>If the returned value is not empty, the instance is an ECS automatically created in a scaling action.</p>
    <p id="a6f15c80f7a8e4bc7bb49e16a7b9a6a1e"><a name="a6f15c80f7a8e4bc7bb49e16a7b9a6a1e"></a><a name="a6f15c80f7a8e4bc7bb49e16a7b9a6a1e"></a>If the returned value is empty, the instance is an ECS manually added to the AS group.</p>
    </td>
    </tr>
    <tr id="r2e9d08c03c2d45d49627031bec19adba"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="a2054b48bc54d4c099fca130ada8f2a67"><a name="a2054b48bc54d4c099fca130ada8f2a67"></a><a name="a2054b48bc54d4c099fca130ada8f2a67"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="a9561fe662833467eb155944e92ce45b9"><a name="a9561fe662833467eb155944e92ce45b9"></a><a name="a9561fe662833467eb155944e92ce45b9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="abeff39d08b034646b4f440ebf83247f3"><a name="abeff39d08b034646b4f440ebf83247f3"></a><a name="abeff39d08b034646b4f440ebf83247f3"></a>Specifies the time when the instance is added to the AS group. The time format complies with UTC.</p>
    </td>
    </tr>
    <tr id="row30878528101412"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p18132877101412"><a name="p18132877101412"></a><a name="p18132877101412"></a>protect_from_scaling_down</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.4.1.2 "><p id="p59476922101412"><a name="p59476922101412"></a><a name="p59476922101412"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p52901359101412"><a name="p52901359101412"></a><a name="p52901359101412"></a>Specifies the instance protection status.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "limit": 10,
        "total_number": 1,
        "start_number": 0,
        "scaling_group_instances": [
            {
                "instance_id": "b25c1589-c96c-465b-9fef-d06540d1945c",
                "scaling_group_id": "e5d27f5c-dd76-4a61-b4bc-a67c5686719a",
                "scaling_group_name": "discuz",
                "life_cycle_state": "INSERVICE",
                "health_status": "NORMAL",
                "scaling_configuration_name": "discuz",
                "scaling_configuration_id": "ca3dcd84-d197-4c4f-af2a-cf8ba39696ac",
                "create_time": "2015-07-23T06:47:33Z",
                "instance_name": "discuz_3D210808",
                "protect_from_scaling_down": false
            }
        ]
    }
    ```


## Returned Values<a name="section25927028"></a>

-   Normal

    200

-   Abnormal

    <a name="table44024689"></a>
    <table><thead align="left"><tr id="row17847776"><th class="cellrowborder" valign="top" width="44.18%" id="mcps1.1.3.1.1"><p id="p36383728"><a name="p36383728"></a><a name="p36383728"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.82%" id="mcps1.1.3.1.2"><p id="p61400865"><a name="p61400865"></a><a name="p61400865"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7414170"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p63676932"><a name="p63676932"></a><a name="p63676932"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p57557895"><a name="p57557895"></a><a name="p57557895"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row48259009"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p16665627"><a name="p16665627"></a><a name="p16665627"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p7738529"><a name="p7738529"></a><a name="p7738529"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2537905"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p4243749"><a name="p4243749"></a><a name="p4243749"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p8199418"><a name="p8199418"></a><a name="p8199418"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row6685904"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p4687385"><a name="p4687385"></a><a name="p4687385"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p44133910"><a name="p44133910"></a><a name="p44133910"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row61660876"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p28475059"><a name="p28475059"></a><a name="p28475059"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p24778434"><a name="p24778434"></a><a name="p24778434"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row21679321"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p11194552"><a name="p11194552"></a><a name="p11194552"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p34343508"><a name="p34343508"></a><a name="p34343508"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row40656116"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p4811061"><a name="p4811061"></a><a name="p4811061"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p54151655"><a name="p54151655"></a><a name="p54151655"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row17602849"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p16544703"><a name="p16544703"></a><a name="p16544703"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p65052577"><a name="p65052577"></a><a name="p65052577"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row48602288"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p44471219"><a name="p44471219"></a><a name="p44471219"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p45399024"><a name="p45399024"></a><a name="p45399024"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row5938035"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p11218807"><a name="p11218807"></a><a name="p11218807"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p36308168"><a name="p36308168"></a><a name="p36308168"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row58338056"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p27762102"><a name="p27762102"></a><a name="p27762102"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p34137829"><a name="p34137829"></a><a name="p34137829"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row38805013"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p56198311"><a name="p56198311"></a><a name="p56198311"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p55769358"><a name="p55769358"></a><a name="p55769358"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row32162181"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p54999878"><a name="p54999878"></a><a name="p54999878"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p25805135"><a name="p25805135"></a><a name="p25805135"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row30919631"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p21462168"><a name="p21462168"></a><a name="p21462168"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p60714046"><a name="p60714046"></a><a name="p60714046"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

