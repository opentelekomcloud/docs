# Querying CMK Instances<a name="kms_02_0042"></a>

## Function<a name="en-us_topic_0112992313_section22636485491"></a>

This API allows you to query CMK instances.

You can use the tag filtering function to query the detailed information about a specified CMK.

## URI<a name="en-us_topic_0112992313_section2920193835019"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/resource\_instances/action

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992313_table9289163655118"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992313_row12289153695114"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992313_p2739096916511"><a name="en-us_topic_0112992313_p2739096916511"></a><a name="en-us_topic_0112992313_p2739096916511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992313_p407603016511"><a name="en-us_topic_0112992313_p407603016511"></a><a name="en-us_topic_0112992313_p407603016511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992313_p6172299916511"><a name="en-us_topic_0112992313_p6172299916511"></a><a name="en-us_topic_0112992313_p6172299916511"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992313_p3350702116511"><a name="en-us_topic_0112992313_p3350702116511"></a><a name="en-us_topic_0112992313_p3350702116511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992313_row1329013695117"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p172905364515"><a name="en-us_topic_0112992313_p172905364515"></a><a name="en-us_topic_0112992313_p172905364515"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p172901236145118"><a name="en-us_topic_0112992313_p172901236145118"></a><a name="en-us_topic_0112992313_p172901236145118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p4386100291125"><a name="en-us_topic_0112992313_p4386100291125"></a><a name="en-us_topic_0112992313_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p172907366512"><a name="en-us_topic_0112992313_p172907366512"></a><a name="en-us_topic_0112992313_p172907366512"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992313_section1274672844719"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992313_table976404617134"></a>
<table><thead align="left"><tr id="en-us_topic_0112992313_row376117465134"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992313_p20270144855616"><a name="en-us_topic_0112992313_p20270144855616"></a><a name="en-us_topic_0112992313_p20270144855616"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992313_p4270348125619"><a name="en-us_topic_0112992313_p4270348125619"></a><a name="en-us_topic_0112992313_p4270348125619"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992313_p102705482561"><a name="en-us_topic_0112992313_p102705482561"></a><a name="en-us_topic_0112992313_p102705482561"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992313_p6270174895617"><a name="en-us_topic_0112992313_p6270174895617"></a><a name="en-us_topic_0112992313_p6270174895617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992313_row18761194611312"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p876110465139"><a name="en-us_topic_0112992313_p876110465139"></a><a name="en-us_topic_0112992313_p876110465139"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p1376164651317"><a name="en-us_topic_0112992313_p1376164651317"></a><a name="en-us_topic_0112992313_p1376164651317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p47611446111315"><a name="en-us_topic_0112992313_p47611446111315"></a><a name="en-us_topic_0112992313_p47611446111315"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992313_p4742733103512"><a name="en-us_topic_0112992313_p4742733103512"></a><a name="en-us_topic_0112992313_p4742733103512"></a>list of tags, including tag keys and tag values.<a name="en-us_topic_0112992313_ul17835144253711"></a><a name="en-us_topic_0112992313_ul17835144253711"></a><ul id="en-us_topic_0112992313_ul17835144253711"><li><strong id="en-us_topic_0112992313_b842352706165737"><a name="en-us_topic_0112992313_b842352706165737"></a><a name="en-us_topic_0112992313_b842352706165737"></a>key</strong> indicates the tag key. A CMK can have a maximum of 10 keys, and each of them is unique and cannot be empty. A key cannot have duplicate values. The value of <strong id="en-us_topic_0112992313_b842352706165433"><a name="en-us_topic_0112992313_b842352706165433"></a><a name="en-us_topic_0112992313_b842352706165433"></a>key</strong> contains a maximum of 36 characters.</li><li><strong id="en-us_topic_0112992313_b842352706165447"><a name="en-us_topic_0112992313_b842352706165447"></a><a name="en-us_topic_0112992313_b842352706165447"></a>value</strong> indicates the tag value. Each tag value can contain a maximum of 43 characters. The relationship between values is <strong id="en-us_topic_0112992313_b842352706165526"><a name="en-us_topic_0112992313_b842352706165526"></a><a name="en-us_topic_0112992313_b842352706165526"></a>AND</strong>.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992313_row127611646171314"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p15761124616138"><a name="en-us_topic_0112992313_p15761124616138"></a><a name="en-us_topic_0112992313_p15761124616138"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p13761134621319"><a name="en-us_topic_0112992313_p13761134621319"></a><a name="en-us_topic_0112992313_p13761134621319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p85873323810"><a name="en-us_topic_0112992313_p85873323810"></a><a name="en-us_topic_0112992313_p85873323810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p376164681318"><a name="en-us_topic_0112992313_p376164681318"></a><a name="en-us_topic_0112992313_p376164681318"></a>Number of queried records. If <strong id="en-us_topic_0112992313_b82380259319"><a name="en-us_topic_0112992313_b82380259319"></a><a name="en-us_topic_0112992313_b82380259319"></a>action</strong> is set to <strong id="en-us_topic_0112992313_b11170930113112"><a name="en-us_topic_0112992313_b11170930113112"></a><a name="en-us_topic_0112992313_b11170930113112"></a>count</strong>, this parameter does not need to be set. If <strong id="en-us_topic_0112992313_b685412464311"><a name="en-us_topic_0112992313_b685412464311"></a><a name="en-us_topic_0112992313_b685412464311"></a>action</strong> is set to <strong id="en-us_topic_0112992313_b31861351193114"><a name="en-us_topic_0112992313_b31861351193114"></a><a name="en-us_topic_0112992313_b31861351193114"></a>filter</strong>, the default value is <strong id="en-us_topic_0112992313_b112171459153117"><a name="en-us_topic_0112992313_b112171459153117"></a><a name="en-us_topic_0112992313_b112171459153117"></a>10</strong>.</p>
<p id="en-us_topic_0112992313_p20761124616132"><a name="en-us_topic_0112992313_p20761124616132"></a><a name="en-us_topic_0112992313_p20761124616132"></a>The value ranges from 1 to 1000.</p>
</td>
</tr>
<tr id="en-us_topic_0112992313_row17762646121311"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p12762194621317"><a name="en-us_topic_0112992313_p12762194621317"></a><a name="en-us_topic_0112992313_p12762194621317"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p12762846131315"><a name="en-us_topic_0112992313_p12762846131315"></a><a name="en-us_topic_0112992313_p12762846131315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p15931432486"><a name="en-us_topic_0112992313_p15931432486"></a><a name="en-us_topic_0112992313_p15931432486"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p11632145062412"><a name="en-us_topic_0112992313_p11632145062412"></a><a name="en-us_topic_0112992313_p11632145062412"></a>Index location. The query starts from the next piece of data indexed by this parameter. When data on the first page is queried, the value of this parameter queried on previous page is contained. If <strong id="en-us_topic_0112992313_b1514816455336"><a name="en-us_topic_0112992313_b1514816455336"></a><a name="en-us_topic_0112992313_b1514816455336"></a>action</strong> is <strong id="en-us_topic_0112992313_b85661349143317"><a name="en-us_topic_0112992313_b85661349143317"></a><a name="en-us_topic_0112992313_b85661349143317"></a>count</strong>, this parameter does not need to be set. If <span class="parmname" id="en-us_topic_0112992313_parmname1439498334142844"><a name="en-us_topic_0112992313_parmname1439498334142844"></a><a name="en-us_topic_0112992313_parmname1439498334142844"></a><b>action</b></span> is set to <span class="parmvalue" id="en-us_topic_0112992313_parmvalue475733516142844_3"><a name="en-us_topic_0112992313_parmvalue475733516142844_3"></a><a name="en-us_topic_0112992313_parmvalue475733516142844_3"></a><b>filter</b></span>, the default value is <span class="parmvalue" id="en-us_topic_0112992313_parmvalue863128038142844_3"><a name="en-us_topic_0112992313_parmvalue863128038142844_3"></a><a name="en-us_topic_0112992313_parmvalue863128038142844_3"></a><b>0</b></span>.</p>
<p id="en-us_topic_0112992313_p9762144641316"><a name="en-us_topic_0112992313_p9762144641316"></a><a name="en-us_topic_0112992313_p9762144641316"></a>The value must be a numeral and cannot be a negative number.</p>
</td>
</tr>
<tr id="en-us_topic_0112992313_row6762114621311"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p1876204631319"><a name="en-us_topic_0112992313_p1876204631319"></a><a name="en-us_topic_0112992313_p1876204631319"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p5762184631314"><a name="en-us_topic_0112992313_p5762184631314"></a><a name="en-us_topic_0112992313_p5762184631314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p559923213819"><a name="en-us_topic_0112992313_p559923213819"></a><a name="en-us_topic_0112992313_p559923213819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p157622046191316"><a name="en-us_topic_0112992313_p157622046191316"></a><a name="en-us_topic_0112992313_p157622046191316"></a>Operation ID, which can be set to <strong id="en-us_topic_0112992313_b84235270614519"><a name="en-us_topic_0112992313_b84235270614519"></a><a name="en-us_topic_0112992313_b84235270614519"></a>filter</strong> or <strong id="en-us_topic_0112992313_b842352706145114"><a name="en-us_topic_0112992313_b842352706145114"></a><a name="en-us_topic_0112992313_b842352706145114"></a>count</strong>.</p>
<a name="en-us_topic_0112992313_ul11762134612133"></a><a name="en-us_topic_0112992313_ul11762134612133"></a><ul id="en-us_topic_0112992313_ul11762134612133"><li><strong id="en-us_topic_0112992313_b842352706103947"><a name="en-us_topic_0112992313_b842352706103947"></a><a name="en-us_topic_0112992313_b842352706103947"></a>filter</strong>: indicates filtering.</li><li><strong id="en-us_topic_0112992313_b842352706104030"><a name="en-us_topic_0112992313_b842352706104030"></a><a name="en-us_topic_0112992313_b842352706104030"></a>count</strong>: indicates the number of queried records.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0112992313_row3762154641318"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p1376254621313"><a name="en-us_topic_0112992313_p1376254621313"></a><a name="en-us_topic_0112992313_p1376254621313"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p8762134616139"><a name="en-us_topic_0112992313_p8762134616139"></a><a name="en-us_topic_0112992313_p8762134616139"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p776212466137"><a name="en-us_topic_0112992313_p776212466137"></a><a name="en-us_topic_0112992313_p776212466137"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p8762114611131"><a name="en-us_topic_0112992313_p8762114611131"></a><a name="en-us_topic_0112992313_p8762114611131"></a>Search field.</p>
<a name="en-us_topic_0112992313_ul6762124671319"></a><a name="en-us_topic_0112992313_ul6762124671319"></a><ul id="en-us_topic_0112992313_ul6762124671319"><li><strong id="en-us_topic_0112992313_b842352706122740"><a name="en-us_topic_0112992313_b842352706122740"></a><a name="en-us_topic_0112992313_b842352706122740"></a>key</strong> indicates the field to be matched, for example, <strong id="en-us_topic_0112992313_b842352706122731"><a name="en-us_topic_0112992313_b842352706122731"></a><a name="en-us_topic_0112992313_b842352706122731"></a>resource_name</strong>.</li><li><strong id="en-us_topic_0112992313_b842352706165641"><a name="en-us_topic_0112992313_b842352706165641"></a><a name="en-us_topic_0112992313_b842352706165641"></a>value</strong> indicates the value to be matched, which contains a maximum of 255 characters and cannot be empty.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0112992313_row97646460134"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p1376211466130"><a name="en-us_topic_0112992313_p1376211466130"></a><a name="en-us_topic_0112992313_p1376211466130"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p2764746171314"><a name="en-us_topic_0112992313_p2764746171314"></a><a name="en-us_topic_0112992313_p2764746171314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p19221940781"><a name="en-us_topic_0112992313_p19221940781"></a><a name="en-us_topic_0112992313_p19221940781"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p1176410465135"><a name="en-us_topic_0112992313_p1176410465135"></a><a name="en-us_topic_0112992313_p1176410465135"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992313_p1676444617136"><a name="en-us_topic_0112992313_p1676444617136"></a><a name="en-us_topic_0112992313_p1676444617136"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992313_section15410161125617"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992313_table126197419146"></a>
<table><thead align="left"><tr id="en-us_topic_0112992313_row1161915414146"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992313_p367742135716"><a name="en-us_topic_0112992313_p367742135716"></a><a name="en-us_topic_0112992313_p367742135716"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992313_p667717245711"><a name="en-us_topic_0112992313_p667717245711"></a><a name="en-us_topic_0112992313_p667717245711"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992313_p116771326575"><a name="en-us_topic_0112992313_p116771326575"></a><a name="en-us_topic_0112992313_p116771326575"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992313_p36771211579"><a name="en-us_topic_0112992313_p36771211579"></a><a name="en-us_topic_0112992313_p36771211579"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992313_row56194419141"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p1061934121414"><a name="en-us_topic_0112992313_p1061934121414"></a><a name="en-us_topic_0112992313_p1061934121414"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p1161912410148"><a name="en-us_topic_0112992313_p1161912410148"></a><a name="en-us_topic_0112992313_p1161912410148"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p196197441413"><a name="en-us_topic_0112992313_p196197441413"></a><a name="en-us_topic_0112992313_p196197441413"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p13619846149"><a name="en-us_topic_0112992313_p13619846149"></a><a name="en-us_topic_0112992313_p13619846149"></a>Resource instance list. For details, see <a href="#en-us_topic_0112992313_table824381161412">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992313_row1761916418144"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p186192421420"><a name="en-us_topic_0112992313_p186192421420"></a><a name="en-us_topic_0112992313_p186192421420"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p196191148143"><a name="en-us_topic_0112992313_p196191148143"></a><a name="en-us_topic_0112992313_p196191148143"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p136196401419"><a name="en-us_topic_0112992313_p136196401419"></a><a name="en-us_topic_0112992313_p136196401419"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p1961964201412"><a name="en-us_topic_0112992313_p1961964201412"></a><a name="en-us_topic_0112992313_p1961964201412"></a>Total number of records</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **resource**  field description

<a name="en-us_topic_0112992313_table824381161412"></a>
<table><thead align="left"><tr id="en-us_topic_0112992313_row15243311101418"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992313_p41414565715"><a name="en-us_topic_0112992313_p41414565715"></a><a name="en-us_topic_0112992313_p41414565715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992313_p714114519571"><a name="en-us_topic_0112992313_p714114519571"></a><a name="en-us_topic_0112992313_p714114519571"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992313_p1014111525720"><a name="en-us_topic_0112992313_p1014111525720"></a><a name="en-us_topic_0112992313_p1014111525720"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992313_p814111519579"><a name="en-us_topic_0112992313_p814111519579"></a><a name="en-us_topic_0112992313_p814111519579"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992313_row1243141113142"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p5243181131415"><a name="en-us_topic_0112992313_p5243181131415"></a><a name="en-us_topic_0112992313_p5243181131415"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p1424310113149"><a name="en-us_topic_0112992313_p1424310113149"></a><a name="en-us_topic_0112992313_p1424310113149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p811955119813"><a name="en-us_topic_0112992313_p811955119813"></a><a name="en-us_topic_0112992313_p811955119813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p424391112145"><a name="en-us_topic_0112992313_p424391112145"></a><a name="en-us_topic_0112992313_p424391112145"></a>Resource ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992313_row14243711161415"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p724391181414"><a name="en-us_topic_0112992313_p724391181414"></a><a name="en-us_topic_0112992313_p724391181414"></a>resource_detail</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p1424331191415"><a name="en-us_topic_0112992313_p1424331191415"></a><a name="en-us_topic_0112992313_p1424331191415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p1124145115811"><a name="en-us_topic_0112992313_p1124145115811"></a><a name="en-us_topic_0112992313_p1124145115811"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p62431811191414"><a name="en-us_topic_0112992313_p62431811191414"></a><a name="en-us_topic_0112992313_p62431811191414"></a>Resource details. For details, see <a href="querying-the-information-about-a-cmk.md#en-us_topic_0112992343_t98d238e10953421e84a073707024c329">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992313_row162431117146"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p22431211171410"><a name="en-us_topic_0112992313_p22431211171410"></a><a name="en-us_topic_0112992313_p22431211171410"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p524310116145"><a name="en-us_topic_0112992313_p524310116145"></a><a name="en-us_topic_0112992313_p524310116145"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p230293620205"><a name="en-us_topic_0112992313_p230293620205"></a><a name="en-us_topic_0112992313_p230293620205"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p142433117141"><a name="en-us_topic_0112992313_p142433117141"></a><a name="en-us_topic_0112992313_p142433117141"></a>Lists of tags. If there is no tag, the array is empty by default.</p>
</td>
</tr>
<tr id="en-us_topic_0112992313_row172431311111416"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992313_p5243141171420"><a name="en-us_topic_0112992313_p5243141171420"></a><a name="en-us_topic_0112992313_p5243141171420"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992313_p324361181410"><a name="en-us_topic_0112992313_p324361181410"></a><a name="en-us_topic_0112992313_p324361181410"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992313_p74418531586"><a name="en-us_topic_0112992313_p74418531586"></a><a name="en-us_topic_0112992313_p74418531586"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992313_p142431511141415"><a name="en-us_topic_0112992313_p142431511141415"></a><a name="en-us_topic_0112992313_p142431511141415"></a>Resource name. This parameter is an empty string by default.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992313_section169496492213"></a>

The following example describes how to query key instances.

-   Example request

    ```
       {
              "offset": "100", 
              "limit": "100", 
              "action": "filter", 
              "matches":[
              {
                       "key": "resource_name", 
                       "value": "resource1"
                    }
               ], 
              "tags": [
                   {
                       "key": "key1", 
                       "values": [
                                "value1", 
                                "value2"
                       ]
                   }
              ]
         }
    ```

-   Example response

    ```
    { 
     "resources": [{
           "resource_id": "90c03e67-5534-4ed0-acfa-89780e47a535",
           "resource_detail": {
                  "key_id": "90c03e67-5534-4ed0-acfa-89780e47a535",
                  "domain_id": "4B688Fb77412Aee5570E7ecdbeB5afdc",
                  "key_alias": "tagTest_xmdmi",
                  "key_description": "123",
                  "creation_date": 1521449277000,
                  "scheduled_deletion_date": "",
                  "key_state": 2,
                  "default_key_flag": 0,
                  "key_type": 1
           },
           "resource_name": "tagTest_xmdmi",
           "tags": [{
                  "key": "$",
                  "value": "testValue!"
           }, {
                  "key": "1",
                  "value": "ccwZ"
           }, {
                  "key": "1&",
                  "value": "testValue!"
           }, {
                  "key": "abcd",
                  "value": "1&"
           }, {
                  "key": "efg",
                  "value": "1&"
           }, {
                  "key": "faregbqer",
                  "value": "AAaa00-99"
           }, {
                  "key": "fcwefwq",
                  "value": "$"
           }, {
                  "key": "fwqegqwrg",
                  "value": "1&"
           }, {
                  "key": "haha",
                  "value": "qzzahnzgoqbkabppdehnbrrgbrkvlxkkfoosqyhdylq"
           }, {
                  "key": "quapxpysduboguiluwargcgmvcgxinianbhl",
                  "value": "testValue!"
           }]
     }]
     "total_count": "1"}
    ```

    or

    ```
    {     
           "error": {        
           "error_code": "KMS.XXXX",         
           "error_msg": "XXX"     
            }
     }
    ```


## Status Codes<a name="en-us_topic_0112992313_section655115613254"></a>

[Table 5](#en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  5**  Status codes

<a name="en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992313_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992313_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992313_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992313_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992313_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992313_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992313_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992313_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992313_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992313_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992313_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992313_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992313_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992313_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992313_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992313_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

