# Creating an Endpoint Group<a name="en-dc_topic_0055025336"></a>

## Function<a name="en-us_topic_0070658700_section6324186692910"></a>

This API is used to create a Direct Connect endpoint group.

## URI<a name="en-us_topic_0070658700_section853188092910"></a>

POST /v2.0/dcaas/dc-endpoint-groups

## Request<a name="en-us_topic_0070658700_section2281784192910"></a>

[Table 1](#en-us_topic_0070658700_table49278871155710)  lists the request parameter.

**Table  1**  Request parameter

<a name="en-us_topic_0070658700_table49278871155710"></a>
<table><thead align="left"><tr id="en-us_topic_0070658700_row34163686155710"><th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.1"><p id="en-us_topic_0070658700_p15795191155710"><a name="en-us_topic_0070658700_p15795191155710"></a><a name="en-us_topic_0070658700_p15795191155710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0070658700_p4342096155710"><a name="en-us_topic_0070658700_p4342096155710"></a><a name="en-us_topic_0070658700_p4342096155710"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8.25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0070658700_p16165530155710"><a name="en-us_topic_0070658700_p16165530155710"></a><a name="en-us_topic_0070658700_p16165530155710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="69.07%" id="mcps1.2.5.1.4"><p id="en-us_topic_0070658700_p34339581155710"><a name="en-us_topic_0070658700_p34339581155710"></a><a name="en-us_topic_0070658700_p34339581155710"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658700_row30042656155710"><td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0070658700_p17536043155710"><a name="en-us_topic_0070658700_p17536043155710"></a><a name="en-us_topic_0070658700_p17536043155710"></a>dc_endpoint_group</p>
</td>
<td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0070658700_p11133383155710"><a name="en-us_topic_0070658700_p11133383155710"></a><a name="en-us_topic_0070658700_p11133383155710"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0070658700_p29388827155710"><a name="en-us_topic_0070658700_p29388827155710"></a><a name="en-us_topic_0070658700_p29388827155710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="69.07%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0070658700_p31684816155710"><a name="en-us_topic_0070658700_p31684816155710"></a><a name="en-us_topic_0070658700_p31684816155710"></a>Indicates the <strong id="b842352706194419"><a name="b842352706194419"></a><a name="b842352706194419"></a>dc_endpoint_group</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **dc\_endpoint\_group**

<a name="en-us_topic_0070658700_table3523051192910"></a>
<table><thead align="left"><tr id="en-us_topic_0070658700_row1307920992910"><th class="cellrowborder" valign="top" width="21.57%" id="mcps1.1.5.1.1"><p id="en-us_topic_0070658700_p4450739192910"><a name="en-us_topic_0070658700_p4450739192910"></a><a name="en-us_topic_0070658700_p4450739192910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.799999999999999%" id="mcps1.1.5.1.2"><p id="en-us_topic_0070658700_p26394292910"><a name="en-us_topic_0070658700_p26394292910"></a><a name="en-us_topic_0070658700_p26394292910"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.1.5.1.3"><p id="en-us_topic_0070658700_p6472145192910"><a name="en-us_topic_0070658700_p6472145192910"></a><a name="en-us_topic_0070658700_p6472145192910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59.11%" id="mcps1.1.5.1.4"><p id="en-us_topic_0070658700_p6443764692910"><a name="en-us_topic_0070658700_p6443764692910"></a><a name="en-us_topic_0070658700_p6443764692910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658700_row2660185192910"><td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658700_p3605816293239"><a name="en-us_topic_0070658700_p3605816293239"></a><a name="en-us_topic_0070658700_p3605816293239"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.799999999999999%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658700_p6629905993311"><a name="en-us_topic_0070658700_p6629905993311"></a><a name="en-us_topic_0070658700_p6629905993311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658700_p5941630693257"><a name="en-us_topic_0070658700_p5941630693257"></a><a name="en-us_topic_0070658700_p5941630693257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.11%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658700_p1074630693412"><a name="en-us_topic_0070658700_p1074630693412"></a><a name="en-us_topic_0070658700_p1074630693412"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row2405214492910"><td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658700_p1588715393239"><a name="en-us_topic_0070658700_p1588715393239"></a><a name="en-us_topic_0070658700_p1588715393239"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.799999999999999%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658700_p2631109893311"><a name="en-us_topic_0070658700_p2631109893311"></a><a name="en-us_topic_0070658700_p2631109893311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658700_p1210552293257"><a name="en-us_topic_0070658700_p1210552293257"></a><a name="en-us_topic_0070658700_p1210552293257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.11%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658700_p464917193412"><a name="en-us_topic_0070658700_p464917193412"></a><a name="en-us_topic_0070658700_p464917193412"></a>Indicates the name of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row5264583392910"><td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658700_p4444139293239"><a name="en-us_topic_0070658700_p4444139293239"></a><a name="en-us_topic_0070658700_p4444139293239"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.799999999999999%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658700_p45532693311"><a name="en-us_topic_0070658700_p45532693311"></a><a name="en-us_topic_0070658700_p45532693311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658700_p3573563593257"><a name="en-us_topic_0070658700_p3573563593257"></a><a name="en-us_topic_0070658700_p3573563593257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.11%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658700_p6458631593412"><a name="en-us_topic_0070658700_p6458631593412"></a><a name="en-us_topic_0070658700_p6458631593412"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row677461492910"><td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658700_p65056527151044"><a name="en-us_topic_0070658700_p65056527151044"></a><a name="en-us_topic_0070658700_p65056527151044"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="11.799999999999999%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658700_p28152132151058"><a name="en-us_topic_0070658700_p28152132151058"></a><a name="en-us_topic_0070658700_p28152132151058"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658700_p6711601151030"><a name="en-us_topic_0070658700_p6711601151030"></a><a name="en-us_topic_0070658700_p6711601151030"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.11%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658700_p59601471151030"><a name="en-us_topic_0070658700_p59601471151030"></a><a name="en-us_topic_0070658700_p59601471151030"></a>Indicates the list of the Direct Connect endpoints.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row2673906492910"><td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658700_p13276033151044"><a name="en-us_topic_0070658700_p13276033151044"></a><a name="en-us_topic_0070658700_p13276033151044"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="11.799999999999999%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658700_p59598963151058"><a name="en-us_topic_0070658700_p59598963151058"></a><a name="en-us_topic_0070658700_p59598963151058"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658700_p25798842151030"><a name="en-us_topic_0070658700_p25798842151030"></a><a name="en-us_topic_0070658700_p25798842151030"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.11%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658700_p6370425719352"><a name="en-us_topic_0070658700_p6370425719352"></a><a name="en-us_topic_0070658700_p6370425719352"></a>Indicates the type of the Direct Connect endpoint.</p>
<p id="en-us_topic_0070658700_p54361932151030"><a name="en-us_topic_0070658700_p54361932151030"></a><a name="en-us_topic_0070658700_p54361932151030"></a>The value is <strong id="b842352706185352"><a name="b842352706185352"></a><a name="b842352706185352"></a>cidr</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0070658700_section1915447592910"></a>

[Table 2](#en-us_topic_0070658700_table33326591155835)  lists the response parameter.

**Table  2**  Response parameter

<a name="en-us_topic_0070658700_table33326591155835"></a>
<table><thead align="left"><tr id="en-us_topic_0070658700_row62151438155835"><th class="cellrowborder" valign="top" width="25.540000000000003%" id="mcps1.2.4.1.1"><p id="en-us_topic_0070658700_p1101727155835"><a name="en-us_topic_0070658700_p1101727155835"></a><a name="en-us_topic_0070658700_p1101727155835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.99%" id="mcps1.2.4.1.2"><p id="en-us_topic_0070658700_p22131064155835"><a name="en-us_topic_0070658700_p22131064155835"></a><a name="en-us_topic_0070658700_p22131064155835"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.47%" id="mcps1.2.4.1.3"><p id="en-us_topic_0070658700_p45444133155835"><a name="en-us_topic_0070658700_p45444133155835"></a><a name="en-us_topic_0070658700_p45444133155835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658700_row57096136155835"><td class="cellrowborder" valign="top" width="25.540000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0070658700_p61384275155835"><a name="en-us_topic_0070658700_p61384275155835"></a><a name="en-us_topic_0070658700_p61384275155835"></a>dc_endpoint_group</p>
</td>
<td class="cellrowborder" valign="top" width="29.99%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0070658700_p6070383155835"><a name="en-us_topic_0070658700_p6070383155835"></a><a name="en-us_topic_0070658700_p6070383155835"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="44.47%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0070658700_p32229496155835"><a name="en-us_topic_0070658700_p32229496155835"></a><a name="en-us_topic_0070658700_p32229496155835"></a>Indicates the <strong id="b842352706194437"><a name="b842352706194437"></a><a name="b842352706194437"></a>dc_endpoint_group</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **dc\_endpoint\_group**

<a name="en-us_topic_0070658700_table6599744292910"></a>
<table><thead align="left"><tr id="en-us_topic_0070658700_row1344591292910"><th class="cellrowborder" valign="top" width="29.92%" id="mcps1.1.4.1.1"><p id="en-us_topic_0070658700_p4888289392910"><a name="en-us_topic_0070658700_p4888289392910"></a><a name="en-us_topic_0070658700_p4888289392910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27.36%" id="mcps1.1.4.1.2"><p id="en-us_topic_0070658700_p228436892910"><a name="en-us_topic_0070658700_p228436892910"></a><a name="en-us_topic_0070658700_p228436892910"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.72%" id="mcps1.1.4.1.3"><p id="en-us_topic_0070658700_p1567805992910"><a name="en-us_topic_0070658700_p1567805992910"></a><a name="en-us_topic_0070658700_p1567805992910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658700_row557857592910"><td class="cellrowborder" valign="top" width="29.92%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658700_p2232642692910"><a name="en-us_topic_0070658700_p2232642692910"></a><a name="en-us_topic_0070658700_p2232642692910"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658700_p4674730592910"><a name="en-us_topic_0070658700_p4674730592910"></a><a name="en-us_topic_0070658700_p4674730592910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.72%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658700_p5414758192910"><a name="en-us_topic_0070658700_p5414758192910"></a><a name="en-us_topic_0070658700_p5414758192910"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row2072208492910"><td class="cellrowborder" valign="top" width="29.92%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658700_p40455487151221"><a name="en-us_topic_0070658700_p40455487151221"></a><a name="en-us_topic_0070658700_p40455487151221"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658700_p49548139151221"><a name="en-us_topic_0070658700_p49548139151221"></a><a name="en-us_topic_0070658700_p49548139151221"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.72%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658700_p14127953151221"><a name="en-us_topic_0070658700_p14127953151221"></a><a name="en-us_topic_0070658700_p14127953151221"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row2092257692910"><td class="cellrowborder" valign="top" width="29.92%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658700_p60451660151221"><a name="en-us_topic_0070658700_p60451660151221"></a><a name="en-us_topic_0070658700_p60451660151221"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="27.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658700_p8044767151221"><a name="en-us_topic_0070658700_p8044767151221"></a><a name="en-us_topic_0070658700_p8044767151221"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.72%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658700_p2878368151221"><a name="en-us_topic_0070658700_p2878368151221"></a><a name="en-us_topic_0070658700_p2878368151221"></a>Indicates the name of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row404465492910"><td class="cellrowborder" valign="top" width="29.92%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658700_p29866301151221"><a name="en-us_topic_0070658700_p29866301151221"></a><a name="en-us_topic_0070658700_p29866301151221"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="27.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658700_p14174295151221"><a name="en-us_topic_0070658700_p14174295151221"></a><a name="en-us_topic_0070658700_p14174295151221"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.72%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658700_p14446635151221"><a name="en-us_topic_0070658700_p14446635151221"></a><a name="en-us_topic_0070658700_p14446635151221"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row611136292910"><td class="cellrowborder" valign="top" width="29.92%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658700_p42150997151221"><a name="en-us_topic_0070658700_p42150997151221"></a><a name="en-us_topic_0070658700_p42150997151221"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="27.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658700_p60404427151221"><a name="en-us_topic_0070658700_p60404427151221"></a><a name="en-us_topic_0070658700_p60404427151221"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="42.72%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658700_p39362491151221"><a name="en-us_topic_0070658700_p39362491151221"></a><a name="en-us_topic_0070658700_p39362491151221"></a>Indicates the list of the Direct Connect endpoints.</p>
</td>
</tr>
<tr id="en-us_topic_0070658700_row4800353492910"><td class="cellrowborder" valign="top" width="29.92%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658700_p5385967151221"><a name="en-us_topic_0070658700_p5385967151221"></a><a name="en-us_topic_0070658700_p5385967151221"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="27.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658700_p34948125151221"><a name="en-us_topic_0070658700_p34948125151221"></a><a name="en-us_topic_0070658700_p34948125151221"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.72%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658700_p3654187619420"><a name="en-us_topic_0070658700_p3654187619420"></a><a name="en-us_topic_0070658700_p3654187619420"></a>Indicates the type of the Direct Connect endpoint.</p>
<p id="en-us_topic_0070658700_p56273146151221"><a name="en-us_topic_0070658700_p56273146151221"></a><a name="en-us_topic_0070658700_p56273146151221"></a>The value is <strong id="b257945321936"><a name="b257945321936"></a><a name="b257945321936"></a>cidr</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0070658700_section5174176392910"></a>

-   Example request

    ```
    POST /v2.0/dcaas/dc-endpoint-groups
    {  
         "dc_endpoint_group" : {
             "name" : "endpoint group1",
             "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],      
             "type" : "cidr"
         }
    }
    ```


-   Example response

    ```
    {  
         "dc_endpoint_group" : {
             "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
             "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
             "name" : "endpoint group1",
             "description" : "",
             "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],      
             "type" : "cidr"
        }
    }
    ```


## Returned Value<a name="section7887155395216"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

