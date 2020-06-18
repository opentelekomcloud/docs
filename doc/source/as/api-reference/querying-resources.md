# Querying Resources<a name="EN-US_TOPIC_0127174043"></a>

## Function<a name="section8988193392019"></a>

This interface is used to query instances of a specified resource type by project ID.

By default, resources and resource tags are in descending order of their creation time.

## URI<a name="section109942333208"></a>

POST /autoscaling-api/v1/\{project\_id\}/\{resource\_type\}/resource\_instances/action

**Table  1**  Parameter description

<a name="table12999833152012"></a>
<table><thead align="left"><tr id="row4445123412011"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.1"><p id="p104453340205"><a name="p104453340205"></a><a name="p104453340205"></a><strong id="b8711161017462"><a name="b8711161017462"></a><a name="b8711161017462"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p1944523472016"><a name="p1944523472016"></a><a name="p1944523472016"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p104451334132013"><a name="p104451334132013"></a><a name="p104451334132013"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.53465346534653%" id="mcps1.2.5.1.4"><p id="p1744553492017"><a name="p1744553492017"></a><a name="p1744553492017"></a><strong id="b81182013174618"><a name="b81182013174618"></a><a name="b81182013174618"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1445173413208"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p20445193416208"><a name="p20445193416208"></a><a name="p20445193416208"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p1044573432019"><a name="p1044573432019"></a><a name="p1044573432019"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p1044543442012"><a name="p1044543442012"></a><a name="p1044543442012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.53465346534653%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row54459346209"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p94452346209"><a name="p94452346209"></a><a name="p94452346209"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p16445133414202"><a name="p16445133414202"></a><a name="p16445133414202"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p17445143422012"><a name="p17445143422012"></a><a name="p17445143422012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.53465346534653%" headers="mcps1.2.5.1.4 "><p id="p1344523422016"><a name="p1344523422016"></a><a name="p1344523422016"></a>Specifies the resource type. An example value is <strong id="b842352706134936"><a name="b842352706134936"></a><a name="b842352706134936"></a>scaling_group_tag</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section231123103614"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table1471417579369"></a>
    <table><thead align="left"><tr id="row17927115773612"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p592716575364"><a name="p592716575364"></a><a name="p592716575364"></a><strong id="b8215101434614"><a name="b8215101434614"></a><a name="b8215101434614"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p1992745711365"><a name="p1992745711365"></a><a name="p1992745711365"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p692717571364"><a name="p692717571364"></a><a name="p692717571364"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p1292775715360"><a name="p1292775715360"></a><a name="p1292775715360"></a><strong id="b14371171517463"><a name="b14371171517463"></a><a name="b14371171517463"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row492755723618"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p29291657163610"><a name="p29291657163610"></a><a name="p29291657163610"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p49294573369"><a name="p49294573369"></a><a name="p49294573369"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p6339193387"><a name="p6339193387"></a><a name="p6339193387"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p39291357123619"><a name="p39291357123619"></a><a name="p39291357123619"></a>Specifies filter criteria with tags included. A maximum of 10 keys can be contained. The structure body must be complete. For details, see <a href="#table97581357153610">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row69291557183612"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p5929135719369"><a name="p5929135719369"></a><a name="p5929135719369"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p9929185713365"><a name="p9929185713365"></a><a name="p9929185713365"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p67901621165314"><a name="p67901621165314"></a><a name="p67901621165314"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p89311857143618"><a name="p89311857143618"></a><a name="p89311857143618"></a>Specifies filter criteria with any tag included. A maximum of 10 keys can be contained. For details, see <a href="#table97581357153610">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1193195717364"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p11931175773612"><a name="p11931175773612"></a><a name="p11931175773612"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p7931185717366"><a name="p7931185717366"></a><a name="p7931185717366"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p112727234533"><a name="p112727234533"></a><a name="p112727234533"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p1193114572362"><a name="p1193114572362"></a><a name="p1193114572362"></a>Specifies filter criteria without tags included. A maximum of 10 keys can be contained. For details, see <a href="#table97581357153610">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row139311757103615"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p593165793610"><a name="p593165793610"></a><a name="p593165793610"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p793135753619"><a name="p793135753619"></a><a name="p793135753619"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p139314577367"><a name="p139314577367"></a><a name="p139314577367"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p393175733615"><a name="p393175733615"></a><a name="p393175733615"></a>Specifies filter criteria without any tag included. A maximum of 10 keys can be contained. For details, see <a href="#table97581357153610">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row20931175753613"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p893116571366"><a name="p893116571366"></a><a name="p893116571366"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p16931195712367"><a name="p16931195712367"></a><a name="p16931195712367"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1293185733610"><a name="p1293185733610"></a><a name="p1293185733610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p2931145719365"><a name="p2931145719365"></a><a name="p2931145719365"></a>Specifies the maximum number of query records. The maximum value is 1000, and the minimum value is 1.</p>
    <a name="ul1965214204415"></a><a name="ul1965214204415"></a><ul id="ul1965214204415"><li>If the <strong>action</strong> value is <strong>count</strong>, this parameter is invalid.</li><li>If the <strong>action</strong> value is <strong>filter</strong>, the default value is <strong>1000</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row1293195719364"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p17931185720363"><a name="p17931185720363"></a><a name="p17931185720363"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p29311857153619"><a name="p29311857153619"></a><a name="p29311857153619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1593195773618"><a name="p1593195773618"></a><a name="p1593195773618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p176016363494"><a name="p176016363494"></a><a name="p176016363494"></a>Specifies the operation, which can be <strong>filter</strong> or <strong>count</strong>.</p>
    <a name="ul9874843105817"></a><a name="ul9874843105817"></a><ul id="ul9874843105817"><li><strong id="b1519710317171"><a name="b1519710317171"></a><a name="b1519710317171"></a>filter</strong>: indicates that resources are filtered by tag and the resources meeting the search criteria are returned on pages.</li><li><strong>count</strong>: indicates that resources are searched by tag and the number of resources meeting the search criteria is returned.</li></ul>
    </td>
    </tr>
    <tr id="row4931195763619"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p39311257183614"><a name="p39311257183614"></a><a name="p39311257183614"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p18931195718362"><a name="p18931195718362"></a><a name="p18931195718362"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p3931205714368"><a name="p3931205714368"></a><a name="p3931205714368"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p6931125716366"><a name="p6931125716366"></a><a name="p6931125716366"></a>Specifies the index position. The query starts from the next image indexed by this parameter. The value must be a non-negative number.</p>
    <p id="p4931135712361"><a name="p4931135712361"></a><a name="p4931135712361"></a>You do not need to specify this parameter when querying resources on the first page. When you query resources on subsequent pages, set the value of <strong id="b842352706101324"><a name="b842352706101324"></a><a name="b842352706101324"></a>offset</strong> to the location returned in the response body for the previous query.</p>
    <a name="ul129511127259"></a><a name="ul129511127259"></a><ul id="ul129511127259"><li>If the <strong>action</strong> value is <strong>count</strong>, this parameter is invalid.</li><li>If the <strong>action</strong> value is <strong>filter</strong>, the default value is <strong>0</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row2931457143620"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p793117579363"><a name="p793117579363"></a><a name="p793117579363"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p893115714366"><a name="p893115714366"></a><a name="p893115714366"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p92701328105314"><a name="p92701328105314"></a><a name="p92701328105314"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p16931185753618"><a name="p16931185753618"></a><a name="p16931185753618"></a>Specifies fuzzy search. For details, see <a href="#table197711657123614">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row13801745211"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p680112482118"><a name="p680112482118"></a><a name="p680112482118"></a>without_any_tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p195199423237"><a name="p195199423237"></a><a name="p195199423237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p168021748212"><a name="p168021748212"></a><a name="p168021748212"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p1480219422119"><a name="p1480219422119"></a><a name="p1480219422119"></a>If this parameter is set to <strong id="b557910266530"><a name="b557910266530"></a><a name="b557910266530"></a>true</strong>, all resources without tags are queried. In this case, the <strong id="b6580526185310"><a name="b6580526185310"></a><a name="b6580526185310"></a>tags</strong>, <strong id="b258019261538"><a name="b258019261538"></a><a name="b258019261538"></a>tags_any</strong>, <strong id="b105801926185316"><a name="b105801926185316"></a><a name="b105801926185316"></a>not_tags</strong>, and <strong id="b35821126185314"><a name="b35821126185314"></a><a name="b35821126185314"></a>not_tags_any</strong> fields are ignored.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **Tag**  field description

    <a name="table97581357153610"></a>
    <table><thead align="left"><tr id="row69331457153611"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.1"><p id="p693345718361"><a name="p693345718361"></a><a name="p693345718361"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.2"><p id="p5933115763614"><a name="p5933115763614"></a><a name="p5933115763614"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.3"><p id="p6933145703618"><a name="p6933145703618"></a><a name="p6933145703618"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.613861386138616%" id="mcps1.2.5.1.4"><p id="p1793355718363"><a name="p1793355718363"></a><a name="p1793355718363"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12933757103612"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p209331557143618"><a name="p209331557143618"></a><a name="p209331557143618"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.2 "><p id="p4933165713368"><a name="p4933165713368"></a><a name="p4933165713368"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="p7933195763613"><a name="p7933195763613"></a><a name="p7933195763613"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.613861386138616%" headers="mcps1.2.5.1.4 "><p id="p199337572361"><a name="p199337572361"></a><a name="p199337572361"></a>Specifies the resource tag key. It contains a maximum of 127 Unicode characters. It cannot be left blank (This parameter is not verified in the search process.) A maximum of 10 keys are allowed and the key cannot be left blank or an empty string. Each key must be unique.</p>
    </td>
    </tr>
    <tr id="row79331657143613"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p89332574369"><a name="p89332574369"></a><a name="p89332574369"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.2 "><p id="p1093395715360"><a name="p1093395715360"></a><a name="p1093395715360"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="p2933105713361"><a name="p2933105713361"></a><a name="p2933105713361"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.613861386138616%" headers="mcps1.2.5.1.4 "><p id="p199331757103618"><a name="p199331757103618"></a><a name="p199331757103618"></a>Specifies resource tag values. A value contains a maximum of 255 Unicode characters. A key contains a maximum of 10 values. Each value of the same key must be unique.</p>
    <a name="ul12336293017"></a><a name="ul12336293017"></a><ul id="ul12336293017"><li>The asterisk (*) is reserved for the system. If the value starts with *, it indicates that fuzzy match is performed for the digits following *. The value cannot contain only asterisks (*).</li><li>If the values are null (not default), it indicates <strong id="b842352706175623"><a name="b842352706175623"></a><a name="b842352706175623"></a>any_value</strong> (querying any value). The resources contain one or multiple values listed in <strong id="b84235270619578"><a name="b84235270619578"></a><a name="b84235270619578"></a>values</strong> will be found and displayed.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **match**  field description

    <a name="table197711657123614"></a>
    <table><thead align="left"><tr id="row193510576361"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p12935457123615"><a name="p12935457123615"></a><a name="p12935457123615"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p5935155719369"><a name="p5935155719369"></a><a name="p5935155719369"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p179352572364"><a name="p179352572364"></a><a name="p179352572364"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p1693545723613"><a name="p1693545723613"></a><a name="p1693545723613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1793555733614"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p3935557143610"><a name="p3935557143610"></a><a name="p3935557143610"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p6935757183612"><a name="p6935757183612"></a><a name="p6935757183612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p0935135718368"><a name="p0935135718368"></a><a name="p0935135718368"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p23438378275"><a name="p23438378275"></a><a name="p23438378275"></a>Specifies the key parameter to be matched.</p>
    <p id="p1047715257337"><a name="p1047715257337"></a><a name="p1047715257337"></a>The parameter value can only be <strong id="b84235270621544"><a name="b84235270621544"></a><a name="b84235270621544"></a>resource_name</strong>.</p>
    </td>
    </tr>
    <tr id="row19935115723612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p13935857103611"><a name="p13935857103611"></a><a name="p13935857103611"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p1935135783613"><a name="p1935135783613"></a><a name="p1935135783613"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p1893515793616"><a name="p1893515793616"></a><a name="p1893515793616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p993518579366"><a name="p993518579366"></a><a name="p993518579366"></a>Specifies the value. The value is a fixed dictionary value. A value contains a maximum of 255 Unicode characters. If the value is an empty string or <strong id="b84235270616358"><a name="b84235270616358"></a><a name="b84235270616358"></a>resource_id</strong>, exact match is used.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request
    -   Example request when  **action**  is set to  **filter**

        This example shows how to query AS group resources of a tenant using the following search criteria: including tag \(key =  **key1**  and value =  **value**\), excluding tag \(key =  **key2**  and value =  **value2**\), index position 100, and maximum number of records 100.

        ```
        POST https: //{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_tag/resource_instances/action
        
        {
        	"offset": "100",
        	"limit": "100",
        	"action": "filter",
        	"matches": [{
        		"key": "resource_name",
        		"value": "resource1"
        	}],
        	"not_tags": [{
        		"key": "key2",
        		"values": ["value2"]
        	}],
        	"tags": [{
        		"key": "key1",
        		"values": ["value1"]
        	}]
        }
        ```

    -   Example request when  **action**  is set to  **count**

        This example shows how to query the number of AS group resources for a tenant using the following search criteria: including the tag \(key =  **key1**  and value =  **value**\) and excluding the tag \(key =  **key2**  and value =  **value2**\).

        ```
        POST https: //{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_tag/resource_instances/action
        
        {
        	"action": "count",
        	"not_tags": [{
        		"key": "key2",
        		"values": ["value2"]
        	}],
        	"tags": [{
        		"key": "key1",
        		"values": ["value1"]
        	},
        	{
        		"key": "key2",
        		"values": ["value1",
        		"value2"]
        	}],
        	"matches": [{
        		"key": "resource_name",
        		"value": "resource1"
        	}]
        }
        ```



## Response Message<a name="section410163462018"></a>

-   Response parameters

    **Table  5**  Response parameters

    <a name="table711023482015"></a>
    <table><thead align="left"><tr id="row1445073415203"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.1"><p id="p1345013341203"><a name="p1345013341203"></a><a name="p1345013341203"></a><strong id="b245312016465"><a name="b245312016465"></a><a name="b245312016465"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.2"><p id="p345023402015"><a name="p345023402015"></a><a name="p345023402015"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.4059405940594%" id="mcps1.2.4.1.3"><p id="p12450123432019"><a name="p12450123432019"></a><a name="p12450123432019"></a><strong id="b1357719218469"><a name="b1357719218469"></a><a name="b1357719218469"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row345063472018"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.1 "><p id="p1445017347209"><a name="p1445017347209"></a><a name="p1445017347209"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.2 "><p id="p5688103535317"><a name="p5688103535317"></a><a name="p5688103535317"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.4.1.3 "><p id="p1145083414205"><a name="p1145083414205"></a><a name="p1145083414205"></a>Specifies tag resources. For details, see <a href="#table111211234112010">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row0450103412209"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.1 "><p id="p144501234162010"><a name="p144501234162010"></a><a name="p144501234162010"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.2 "><p id="p1450203442017"><a name="p1450203442017"></a><a name="p1450203442017"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.4.1.3 "><p id="p5450203492018"><a name="p5450203492018"></a><a name="p5450203492018"></a>Specifies the total number of records. When <strong id="b84235270621116"><a name="b84235270621116"></a><a name="b84235270621116"></a>action</strong> is set to <strong id="b84235270621123"><a name="b84235270621123"></a><a name="b84235270621123"></a>count</strong>, only this parameter is returned. The values of <strong id="b84235270621137"><a name="b84235270621137"></a><a name="b84235270621137"></a>resources</strong> and <strong id="b84235270621139"><a name="b84235270621139"></a><a name="b84235270621139"></a>marker</strong> are not returned.</p>
    </td>
    </tr>
    <tr id="row54501434142018"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.1 "><p id="p645015343201"><a name="p645015343201"></a><a name="p645015343201"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.2 "><p id="p184501934122015"><a name="p184501934122015"></a><a name="p184501934122015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.4.1.3 "><p id="p4450193411206"><a name="p4450193411206"></a><a name="p4450193411206"></a>Specifies the paging location identifier.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **Resource**  field description

    <a name="table111211234112010"></a>
    <table><thead align="left"><tr id="row9451163414206"><th class="cellrowborder" valign="top" width="20.56794320567943%" id="mcps1.2.4.1.1"><p id="p14511346203"><a name="p14511346203"></a><a name="p14511346203"></a><strong id="b10531522134612"><a name="b10531522134612"></a><a name="b10531522134612"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.848015198480155%" id="mcps1.2.4.1.2"><p id="p94511134162016"><a name="p94511134162016"></a><a name="p94511134162016"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.58404159584042%" id="mcps1.2.4.1.3"><p id="p645120347202"><a name="p645120347202"></a><a name="p645120347202"></a><strong id="b228712364616"><a name="b228712364616"></a><a name="b228712364616"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1645113341207"><td class="cellrowborder" valign="top" width="20.56794320567943%" headers="mcps1.2.4.1.1 "><p id="p045115340207"><a name="p045115340207"></a><a name="p045115340207"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.848015198480155%" headers="mcps1.2.4.1.2 "><p id="p645183462014"><a name="p645183462014"></a><a name="p645183462014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.58404159584042%" headers="mcps1.2.4.1.3 "><p id="p445123452020"><a name="p445123452020"></a><a name="p445123452020"></a>Specifies the resource ID.</p>
    </td>
    </tr>
    <tr id="row245143422017"><td class="cellrowborder" valign="top" width="20.56794320567943%" headers="mcps1.2.4.1.1 "><p id="p1045193419201"><a name="p1045193419201"></a><a name="p1045193419201"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.848015198480155%" headers="mcps1.2.4.1.2 "><p id="p5451934112017"><a name="p5451934112017"></a><a name="p5451934112017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.58404159584042%" headers="mcps1.2.4.1.3 "><p id="p84511434122018"><a name="p84511434122018"></a><a name="p84511434122018"></a>Specifies the resource details.</p>
    </td>
    </tr>
    <tr id="row44511534162010"><td class="cellrowborder" valign="top" width="20.56794320567943%" headers="mcps1.2.4.1.1 "><p id="p1451163419204"><a name="p1451163419204"></a><a name="p1451163419204"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.848015198480155%" headers="mcps1.2.4.1.2 "><p id="p1840743875316"><a name="p1840743875316"></a><a name="p1840743875316"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.58404159584042%" headers="mcps1.2.4.1.3 "><p id="p6451183416202"><a name="p6451183416202"></a><a name="p6451183416202"></a>Specifies tags. If there is no tag, <strong id="b84235270620128"><a name="b84235270620128"></a><a name="b84235270620128"></a>tags</strong> is taken as an empty array by default. For details, see <a href="#table191301634112010">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row24511334152018"><td class="cellrowborder" valign="top" width="20.56794320567943%" headers="mcps1.2.4.1.1 "><p id="p545193472015"><a name="p545193472015"></a><a name="p545193472015"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.848015198480155%" headers="mcps1.2.4.1.2 "><p id="p1451203415202"><a name="p1451203415202"></a><a name="p1451203415202"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.58404159584042%" headers="mcps1.2.4.1.3 "><p id="p545143415205"><a name="p545143415205"></a><a name="p545143415205"></a>Specifies the resource name. If there is no resource, this parameter is an empty string by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **ResourceTag**  field description

    <a name="table191301634112010"></a>
    <table><thead align="left"><tr id="row1345193422010"><th class="cellrowborder" valign="top" width="20.597940205979402%" id="mcps1.2.4.1.1"><p id="p11451183418207"><a name="p11451183418207"></a><a name="p11451183418207"></a><strong id="b1125412417467"><a name="b1125412417467"></a><a name="b1125412417467"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.81801819818018%" id="mcps1.2.4.1.2"><p id="p545163412012"><a name="p545163412012"></a><a name="p545163412012"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.58404159584042%" id="mcps1.2.4.1.3"><p id="p849215412315"><a name="p849215412315"></a><a name="p849215412315"></a><strong id="b332122574610"><a name="b332122574610"></a><a name="b332122574610"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44511934142014"><td class="cellrowborder" valign="top" width="20.597940205979402%" headers="mcps1.2.4.1.1 "><p id="p124515342204"><a name="p124515342204"></a><a name="p124515342204"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81801819818018%" headers="mcps1.2.4.1.2 "><p id="p945153410202"><a name="p945153410202"></a><a name="p945153410202"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.58404159584042%" headers="mcps1.2.4.1.3 "><p id="p84511234172016"><a name="p84511234172016"></a><a name="p84511234172016"></a>Specifies the resource tag key. It contains a maximum of 36 Unicode characters.</p>
    </td>
    </tr>
    <tr id="row14525348204"><td class="cellrowborder" valign="top" width="20.597940205979402%" headers="mcps1.2.4.1.1 "><p id="p14521346205"><a name="p14521346205"></a><a name="p14521346205"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81801819818018%" headers="mcps1.2.4.1.2 "><p id="p84521034192012"><a name="p84521034192012"></a><a name="p84521034192012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.58404159584042%" headers="mcps1.2.4.1.3 "><p id="p7452173452010"><a name="p7452173452010"></a><a name="p7452173452010"></a>Specifies the resource tag value. It contains a maximum of 36 Unicode characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response
    -   Example response when  **action**  is set to  **filter**

        ```
        {
        	"resources": [{
        		"resource_id": "64af4b6f-ec51-4436-8004-7a8f30080c87",
        		"resource_detail": "SCALING_GROUP_TAG",
        		"tags": [{
        			"key": "key1","value": "value1"
        		}],
        		"resource_name": "as_scaling_group_1"
        	},
        	{
        		"resource_id": "7122ef51-604b-40e7-b9b2-1de4cd78dc60",
        		"resource_detail": "SCALING_GROUP_TAG",
        		"tags": [{
        			"key": "key1","value": "value1"
        		}],
        		"resource_name": "as_scaling_group_2"
        	},
        	"marker": "2",
        	"total_count": 2
        }
        ```

    -   Example response when  **action**  is set to  **count**

        ```
        {
               "total_count": 1000
        }
        ```



## Returned Values<a name="section1014063418207"></a>

-   Normal

    200

-   Abnormal

    <a name="table201401734152012"></a>
    <table><thead align="left"><tr id="row1545263412016"><th class="cellrowborder" valign="top" width="43.5%" id="mcps1.1.3.1.1"><p id="p1345217348206"><a name="p1345217348206"></a><a name="p1345217348206"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.49999999999999%" id="mcps1.1.3.1.2"><p id="p3452534172015"><a name="p3452534172015"></a><a name="p3452534172015"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1145213349202"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p10453133482015"><a name="p10453133482015"></a><a name="p10453133482015"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p7453734182018"><a name="p7453734182018"></a><a name="p7453734182018"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row124531734162018"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p745323452014"><a name="p745323452014"></a><a name="p745323452014"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p745311349207"><a name="p745311349207"></a><a name="p745311349207"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row745363415209"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p94538342202"><a name="p94538342202"></a><a name="p94538342202"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p54531634172011"><a name="p54531634172011"></a><a name="p54531634172011"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row845333415205"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p1445311341204"><a name="p1445311341204"></a><a name="p1445311341204"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p1245313492013"><a name="p1245313492013"></a><a name="p1245313492013"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row10453123410203"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p6453634112015"><a name="p6453634112015"></a><a name="p6453634112015"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p5453123416202"><a name="p5453123416202"></a><a name="p5453123416202"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row2453123442011"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p1145383462016"><a name="p1145383462016"></a><a name="p1145383462016"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p445311345204"><a name="p445311345204"></a><a name="p445311345204"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row1345313342201"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p5453034182015"><a name="p5453034182015"></a><a name="p5453034182015"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p845383412016"><a name="p845383412016"></a><a name="p845383412016"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row16453113411205"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p1045310349202"><a name="p1045310349202"></a><a name="p1045310349202"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p174531634172017"><a name="p174531634172017"></a><a name="p174531634172017"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row164533343203"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p345317345207"><a name="p345317345207"></a><a name="p345317345207"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p15453113482017"><a name="p15453113482017"></a><a name="p15453113482017"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row54531934172015"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p17453113419207"><a name="p17453113419207"></a><a name="p17453113419207"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p16453334112013"><a name="p16453334112013"></a><a name="p16453334112013"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row2453153411205"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p134531334142018"><a name="p134531334142018"></a><a name="p134531334142018"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p1945317344206"><a name="p1945317344206"></a><a name="p1945317344206"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1345323452017"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p7453734172016"><a name="p7453734172016"></a><a name="p7453734172016"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p3453153482013"><a name="p3453153482013"></a><a name="p3453153482013"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row144532341208"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p174531334142013"><a name="p174531334142013"></a><a name="p174531334142013"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p64531334112011"><a name="p64531334112011"></a><a name="p64531334112011"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row045314345204"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p145318348201"><a name="p145318348201"></a><a name="p145318348201"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p0454734182019"><a name="p0454734182019"></a><a name="p0454734182019"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

