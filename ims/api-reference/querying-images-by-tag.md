# Querying Images by Tag<a name="EN-US_TOPIC_0102682861"></a>

## Function<a name="section36076688173551"></a>

This API is used to filter or count images using tags or other conditions.

## Constraints<a name="section60340116173551"></a>

To be compatible with remaining tags, the system will not verify the character set of the tag keys and values in the query condition when parameters  **tags** **not\_tags**,  **tags\_any**, and  **not\_tags\_any**  are used.

## URI<a name="section16316966173551"></a>

POST /v2/\{project\_id\}/images/resource\_instances/action

[Table 1](#table27444833173551)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table27444833173551"></a>
<table><thead align="left"><tr id="row31891586173551"><th class="cellrowborder" valign="top" width="19.87198719871987%" id="mcps1.2.5.1.1"><p id="p33081663173551"><a name="p33081663173551"></a><a name="p33081663173551"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.152015201520154%" id="mcps1.2.5.1.2"><p id="p62369028173551"><a name="p62369028173551"></a><a name="p62369028173551"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.51155115511551%" id="mcps1.2.5.1.3"><p id="p18726522173551"><a name="p18726522173551"></a><a name="p18726522173551"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.46444644464446%" id="mcps1.2.5.1.4"><p id="p40453320173551"><a name="p40453320173551"></a><a name="p40453320173551"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55493527173551"><td class="cellrowborder" valign="top" width="19.87198719871987%" headers="mcps1.2.5.1.1 "><p id="p65790735173551"><a name="p65790735173551"></a><a name="p65790735173551"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.152015201520154%" headers="mcps1.2.5.1.2 "><p id="p27449303173551"><a name="p27449303173551"></a><a name="p27449303173551"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.51155115511551%" headers="mcps1.2.5.1.3 "><p id="p8801047173551"><a name="p8801047173551"></a><a name="p8801047173551"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.46444644464446%" headers="mcps1.2.5.1.4 "><p id="p41796216173551"><a name="p41796216173551"></a><a name="p41796216173551"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section40621628173551"></a>

-   Request parameters

    <a name="table29206682173551"></a>
    <table><thead align="left"><tr id="row40241448173551"><th class="cellrowborder" valign="top" width="19.220000000000002%" id="mcps1.1.5.1.1"><p id="p38331852173551"><a name="p38331852173551"></a><a name="p38331852173551"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.92%" id="mcps1.1.5.1.2"><p id="p17872337173551"><a name="p17872337173551"></a><a name="p17872337173551"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.980000000000002%" id="mcps1.1.5.1.3"><p id="p38373215173551"><a name="p38373215173551"></a><a name="p38373215173551"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.88%" id="mcps1.1.5.1.4"><p id="p21222685173551"><a name="p21222685173551"></a><a name="p21222685173551"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41315891173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p58252874173551"><a name="p58252874173551"></a><a name="p58252874173551"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p20862345173551"><a name="p20862345173551"></a><a name="p20862345173551"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p12128409173551"><a name="p12128409173551"></a><a name="p12128409173551"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p4087185510714"><a name="p4087185510714"></a><a name="p4087185510714"></a>Identifies the operation. This parameter is case sensitive and its value can be <strong id="b5500079110714"><a name="b5500079110714"></a><a name="b5500079110714"></a>filter</strong> or <strong id="b2524507610714"><a name="b2524507610714"></a><a name="b2524507610714"></a>count</strong>.</p>
    <a name="ul4576144810721"></a><a name="ul4576144810721"></a><ul id="ul4576144810721"><li>The value <strong id="b6006908310724"><a name="b6006908310724"></a><a name="b6006908310724"></a>filter</strong> indicates pagination query.</li><li>The value <strong id="b84235270611312"><a name="b84235270611312"></a><a name="b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</li></ul>
    </td>
    </tr>
    <tr id="row50349491173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p51776931173551"><a name="p51776931173551"></a><a name="p51776931173551"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p33181855173551"><a name="p33181855173551"></a><a name="p33181855173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p3375760173551"><a name="p3375760173551"></a><a name="p3375760173551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p5001182173551"><a name="p5001182173551"></a><a name="p5001182173551"></a>Includes all specified tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can contain a maximum of 10 tag values. Both tag keys and values must be unique. The tag keys cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row45010643173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p21983479173551"><a name="p21983479173551"></a><a name="p21983479173551"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p35831338173551"><a name="p35831338173551"></a><a name="p35831338173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p16657303173551"><a name="p16657303173551"></a><a name="p16657303173551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p7064292173551"><a name="p7064292173551"></a><a name="p7064292173551"></a>Includes any of specified tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can contain a maximum of 10 tag values. Both tag keys and values must be unique. The tag keys cannot be left blank and set to an empty string.</p>
    </td>
    </tr>
    <tr id="row63578630173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p49595399173551"><a name="p49595399173551"></a><a name="p49595399173551"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p57804348173551"><a name="p57804348173551"></a><a name="p57804348173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p51640589173551"><a name="p51640589173551"></a><a name="p51640589173551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p22138212173551"><a name="p22138212173551"></a><a name="p22138212173551"></a>Excludes all specified tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can contain a maximum of 10 tag values. Both tag keys and values must be unique. The tag keys cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row65026180173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p32629212173551"><a name="p32629212173551"></a><a name="p32629212173551"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p25720492173551"><a name="p25720492173551"></a><a name="p25720492173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p2985117173551"><a name="p2985117173551"></a><a name="p2985117173551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p40467926173551"><a name="p40467926173551"></a><a name="p40467926173551"></a>Excludes any of specified tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can contain a maximum of 10 tag values. Both tag keys and values must be unique. The tag keys cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row756221564115"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p856351584114"><a name="p856351584114"></a><a name="p856351584114"></a>without_any_tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p056316159417"><a name="p056316159417"></a><a name="p056316159417"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p65631615174111"><a name="p65631615174111"></a><a name="p65631615174111"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p10563215184117"><a name="p10563215184117"></a><a name="p10563215184117"></a>If this parameter is set to <strong id="b133471142173611"><a name="b133471142173611"></a><a name="b133471142173611"></a>true</strong>, all resources without tags are queried. In this case, the <strong id="b1495014375374"><a name="b1495014375374"></a><a name="b1495014375374"></a>tag</strong>, <strong id="b6513164123718"><a name="b6513164123718"></a><a name="b6513164123718"></a>not_tags</strong>, <strong id="b0116445133710"><a name="b0116445133710"></a><a name="b0116445133710"></a>tags_any</strong>, and <strong id="b729145011374"><a name="b729145011374"></a><a name="b729145011374"></a>not_tags_any</strong> fields are ignored.</p>
    </td>
    </tr>
    <tr id="row28667022173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p40327431173551"><a name="p40327431173551"></a><a name="p40327431173551"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p45296477173551"><a name="p45296477173551"></a><a name="p45296477173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p45135991173551"><a name="p45135991173551"></a><a name="p45135991173551"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p32136637173551"><a name="p32136637173551"></a><a name="p32136637173551"></a>Specifies the maximum number of query records. This parameter is invalid when <strong id="b84010315911"><a name="b84010315911"></a><a name="b84010315911"></a>action</strong> is set to <strong id="b11335153414915"><a name="b11335153414915"></a><a name="b11335153414915"></a>count</strong>. If <strong id="b84235270692122"><a name="b84235270692122"></a><a name="b84235270692122"></a>action</strong> is set to <strong id="b84235270692134"><a name="b84235270692134"></a><a name="b84235270692134"></a>filter</strong>, the parameter <strong id="b8618148172614"><a name="b8618148172614"></a><a name="b8618148172614"></a>limit</strong> takes effect and its default value is <strong id="b0343185310109"><a name="b0343185310109"></a><a name="b0343185310109"></a>10</strong>. The value of <strong id="b3754120171219"><a name="b3754120171219"></a><a name="b3754120171219"></a>limit</strong> ranges from 1 to 1000.</p>
    </td>
    </tr>
    <tr id="row20794285173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p6615521173551"><a name="p6615521173551"></a><a name="p6615521173551"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p66095222173551"><a name="p66095222173551"></a><a name="p66095222173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p52112788173551"><a name="p52112788173551"></a><a name="p52112788173551"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p60386274173551"><a name="p60386274173551"></a><a name="p60386274173551"></a>Specifies the index position. The query starts from the next image indexed by this parameter. This parameter is not required when data on the first page is queried, and it is invalid when <strong id="b144908401093720"><a name="b144908401093720"></a><a name="b144908401093720"></a>action</strong> is set to <strong id="b212072672793720"><a name="b212072672793720"></a><a name="b212072672793720"></a>count</strong>. If <strong id="b128328859593720"><a name="b128328859593720"></a><a name="b128328859593720"></a>action</strong> is set to <strong id="b99502117793720"><a name="b99502117793720"></a><a name="b99502117793720"></a>filter</strong>, the default value of <strong id="b1841944014292"><a name="b1841944014292"></a><a name="b1841944014292"></a>offset</strong> is <strong id="b41874131793720"><a name="b41874131793720"></a><a name="b41874131793720"></a>0</strong>. The value of <strong id="b172018160303"><a name="b172018160303"></a><a name="b172018160303"></a>offset</strong> cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row6605554173551"><td class="cellrowborder" valign="top" width="19.220000000000002%" headers="mcps1.1.5.1.1 "><p id="p65287884173551"><a name="p65287884173551"></a><a name="p65287884173551"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.1.5.1.2 "><p id="p53827242173551"><a name="p53827242173551"></a><a name="p53827242173551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.980000000000002%" headers="mcps1.1.5.1.3 "><p id="p65039349173551"><a name="p65039349173551"></a><a name="p65039349173551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.88%" headers="mcps1.1.5.1.4 "><p id="p33695892173551"><a name="p33695892173551"></a><a name="p33695892173551"></a>Specifies the search criteria. The tag key is the field to match, for example, <strong id="b84235270615351"><a name="b84235270615351"></a><a name="b84235270615351"></a>resource_name</strong> or <strong id="b1731781636144949"><a name="b1731781636144949"></a><a name="b1731781636144949"></a>resource_id</strong>. <strong id="b84235270621735"><a name="b84235270621735"></a><a name="b84235270621735"></a>value</strong> indicates the matched value. Keys in this list must be unique. The parameter cannot be left blank and may not be transferred.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Data structure description of the tag field

    <a name="table45012720173551"></a>
    <table><thead align="left"><tr id="row14748653173551"><th class="cellrowborder" valign="top" width="18.848115188481152%" id="mcps1.2.5.1.1"><p id="p53790264173551"><a name="p53790264173551"></a><a name="p53790264173551"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.48795120487951%" id="mcps1.2.5.1.2"><p id="p62044140173551"><a name="p62044140173551"></a><a name="p62044140173551"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.238176182381764%" id="mcps1.2.5.1.3"><p id="p59519407173551"><a name="p59519407173551"></a><a name="p59519407173551"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.425757424257576%" id="mcps1.2.5.1.4"><p id="p56342700173551"><a name="p56342700173551"></a><a name="p56342700173551"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row355977173551"><td class="cellrowborder" valign="top" width="18.848115188481152%" headers="mcps1.2.5.1.1 "><p id="p28834158173551"><a name="p28834158173551"></a><a name="p28834158173551"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.2.5.1.2 "><p id="p53865476173551"><a name="p53865476173551"></a><a name="p53865476173551"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.238176182381764%" headers="mcps1.2.5.1.3 "><p id="p1027442173551"><a name="p1027442173551"></a><a name="p1027442173551"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.425757424257576%" headers="mcps1.2.5.1.4 "><p id="p16114017173551"><a name="p16114017173551"></a><a name="p16114017173551"></a>Specifies the tag key. The tag key contains a maximum of 127 Unicode characters and cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row10808433173551"><td class="cellrowborder" valign="top" width="18.848115188481152%" headers="mcps1.2.5.1.1 "><p id="p3067843173551"><a name="p3067843173551"></a><a name="p3067843173551"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.2.5.1.2 "><p id="p47168746173551"><a name="p47168746173551"></a><a name="p47168746173551"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.238176182381764%" headers="mcps1.2.5.1.3 "><p id="p62572110173551"><a name="p62572110173551"></a><a name="p62572110173551"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.425757424257576%" headers="mcps1.2.5.1.4 "><p id="p35176150173551"><a name="p35176150173551"></a><a name="p35176150173551"></a>Lists the tag values. Each value can contain a maximum of 255 Unicode characters. If this parameter is left blank, any value is matched. When multiple values are specified and the key requirements are met, images that have any of the specified values are queried.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Data structure description of the  **matches**  field

    <a name="table194603471868"></a>
    <table><thead align="left"><tr id="row34598479615"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.1"><p id="p1045912474620"><a name="p1045912474620"></a><a name="p1045912474620"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="p145912475616"><a name="p145912475616"></a><a name="p145912475616"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p3459347567"><a name="p3459347567"></a><a name="p3459347567"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="p6459124720613"><a name="p6459124720613"></a><a name="p6459124720613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8459847762"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p1345913474610"><a name="p1345913474610"></a><a name="p1345913474610"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p16459114720614"><a name="p16459114720614"></a><a name="p16459114720614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p945917475618"><a name="p945917475618"></a><a name="p945917475618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p745914472616"><a name="p745914472616"></a><a name="p745914472616"></a>Specifies the tag key, that is to say, the field name for the query operation. Valid values include <strong id="b842352706211410"><a name="b842352706211410"></a><a name="b842352706211410"></a>resource_name</strong> and <strong id="b842352706211416"><a name="b842352706211416"></a><a name="b842352706211416"></a>resource_id</strong>.</p>
    <p id="p1459124716612"><a name="p1459124716612"></a><a name="p1459124716612"></a>If the field name is <strong id="b842352706211428"><a name="b842352706211428"></a><a name="b842352706211428"></a>resource_name</strong> and the value is an empty string, exact query is performed. Otherwise, fuzzy query is performed based on the image name. If the field name is <strong id="b842352706211525"><a name="b842352706211525"></a><a name="b842352706211525"></a>resource_id</strong>, exact query is performed based on the image ID.</p>
    </td>
    </tr>
    <tr id="row154607471165"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p6460747369"><a name="p6460747369"></a><a name="p6460747369"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p184601471168"><a name="p184601471168"></a><a name="p184601471168"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p546034719613"><a name="p546034719613"></a><a name="p546034719613"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p134606477616"><a name="p134606477616"></a><a name="p134606477616"></a>Specifies the tag value. It cannot be left blank. Each value can contain a maximum of 255 Unicode characters. </p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example requests

    ```
    POST https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/resource_instances/action
    ```

    -   Request body when  **action**  is set to  **count**

        ```
        {
           "action": "count",
           "matches": [{
              "key": "resource_name",
              "value": "test100"
           }],
           "tags": [
           {
              "key": "key3",
              "values": ["valueXX"]
           }],
           "tags_any": [
           {
              "key": "key0",
              "values": ["valueXX"]
           }],
              "not_tags": [
           {
              "key": "key9",
              "values": ["value9"]
           }],
           "not_tags_any": [{
              "key": "key7",
              "values": ["value7"]
           }]
        }
        ```

    -   Request body when  **action**  is set to  **filter**

        ```
        {
           "action": "filter",
           "limit": "1",
           "offset": "0",
           "matches": [{
              "key": "resource_name",
              "value": "test100"
           }],
           "tags": [
           {
              "key": "key3",
              "values": ["valueXX"]
           }],
           "tags_any": [
           {
              "key": "key0",
              "values": ["valueXX"]
           }],
           "not_tags": [
           {
              "key": "key9",
              "values": ["value9"]
           }],
           "not_tags_any": [{
              "key": "key7",
              "values": ["value7"]
           }]
        }
        ```



## Response<a name="section44009837173551"></a>

-   Response parameters

    <a name="table46209794173551"></a>
    <table><thead align="left"><tr id="row58695561173551"><th class="cellrowborder" valign="top" width="33.78337833783378%" id="mcps1.1.4.1.1"><p id="p56719981173551"><a name="p56719981173551"></a><a name="p56719981173551"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.78337833783378%" id="mcps1.1.4.1.2"><p id="p21147139173551"><a name="p21147139173551"></a><a name="p21147139173551"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.43324332433243%" id="mcps1.1.4.1.3"><p id="p35196676173551"><a name="p35196676173551"></a><a name="p35196676173551"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32358539173551"><td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.1 "><p id="p3795965173551"><a name="p3795965173551"></a><a name="p3795965173551"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.2 "><p id="p7942344173551"><a name="p7942344173551"></a><a name="p7942344173551"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.43324332433243%" headers="mcps1.1.4.1.3 "><p id="p39350128173551"><a name="p39350128173551"></a><a name="p39350128173551"></a>Lists the images.</p>
    </td>
    </tr>
    <tr id="row18606837173551"><td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.1 "><p id="p30758863173551"><a name="p30758863173551"></a><a name="p30758863173551"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.2 "><p id="p12551541173551"><a name="p12551541173551"></a><a name="p12551541173551"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.43324332433243%" headers="mcps1.1.4.1.3 "><p id="p10041872173551"><a name="p10041872173551"></a><a name="p10041872173551"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Data structure description of the resource field

    <a name="table3856915489"></a>
    <table><thead align="left"><tr id="row1855115287"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p18855615086"><a name="p18855615086"></a><a name="p18855615086"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12855151510816"><a name="p12855151510816"></a><a name="p12855151510816"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1185517151082"><a name="p1185517151082"></a><a name="p1185517151082"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row158558151887"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p985541519812"><a name="p985541519812"></a><a name="p985541519812"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1785518155810"><a name="p1785518155810"></a><a name="p1785518155810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p485516151781"><a name="p485516151781"></a><a name="p485516151781"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row118552015889"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p178558151383"><a name="p178558151383"></a><a name="p178558151383"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6855315888"><a name="p6855315888"></a><a name="p6855315888"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38555152811"><a name="p38555152811"></a><a name="p38555152811"></a>Provides image details.</p>
    </td>
    </tr>
    <tr id="row11856101517820"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p385541515815"><a name="p385541515815"></a><a name="p385541515815"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p148552015383"><a name="p148552015383"></a><a name="p148552015383"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1185671515819"><a name="p1185671515819"></a><a name="p1185671515819"></a>Lists the image tags.</p>
    </td>
    </tr>
    <tr id="row785618152816"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1856171520812"><a name="p1856171520812"></a><a name="p1856171520812"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1585621510812"><a name="p1585621510812"></a><a name="p1585621510812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p08564151882"><a name="p08564151882"></a><a name="p08564151882"></a>Specifies the image name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  resource\_tag field description

    <a name="table1526715341887"></a>
    <table><thead align="left"><tr id="row326753415816"><th class="cellrowborder" valign="top" width="34.03%" id="mcps1.2.4.1.1"><p id="p1026610341689"><a name="p1026610341689"></a><a name="p1026610341689"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.18%" id="mcps1.2.4.1.2"><p id="p1326611349812"><a name="p1326611349812"></a><a name="p1326611349812"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.79%" id="mcps1.2.4.1.3"><p id="p7267103411813"><a name="p7267103411813"></a><a name="p7267103411813"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32672342820"><td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.2.4.1.1 "><p id="p17267134382"><a name="p17267134382"></a><a name="p17267134382"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.18%" headers="mcps1.2.4.1.2 "><p id="p1226720348810"><a name="p1226720348810"></a><a name="p1226720348810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.79%" headers="mcps1.2.4.1.3 "><p id="p1526716341182"><a name="p1526716341182"></a><a name="p1526716341182"></a>Specifies the key of the tag.</p>
    </td>
    </tr>
    <tr id="row626718341888"><td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.2.4.1.1 "><p id="p126713420818"><a name="p126713420818"></a><a name="p126713420818"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.18%" headers="mcps1.2.4.1.2 "><p id="p826718341383"><a name="p826718341383"></a><a name="p826718341383"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.79%" headers="mcps1.2.4.1.3 "><p id="p1126723419820"><a name="p1126723419820"></a><a name="p1126723419820"></a>Specifies the value of the tag.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response bodies
    -   Example response when  **action**  is set to  **count**

        ```
        STATUS CODE 200
        ```

        ```
        {
           "total_count": 36
        }
        ```

    -   Example response when  **action**  is set to  **filter**

        ```
        STATUS CODE 200
        ```

        ```
        {
           "total_count": 36,
           "resources": [{
              "resource_name": "test10002",
              "resource_detail": {"status": "active"},
              "tags": [{
                 "value": "value4",
                 "key": "key4"
              },
              {
                 "value": "valueXX",
                 "key": "key3"
              },
              {
                 "value": "value2",
                 "key": "key2"
              },
              {
                 "value": "value5",
                 "key": "key5"
              },
              {
                 "value": "value8",
                 "key": "key8"
              },
              {
                 "value": "valueXX",
                 "key": "key6"
              },
              {
                 "value": "valueXX",
                 "key": "key0"
              },
              {
                 "value": "value1",
                 "key": "key1"
              },
              {
                 "value": "value7",
                 "key": "key7"
              },
              {
                 "value": "valueXX",
                 "key": "key9"
              }],
              "resource_id": "8693187d-1590-4f9f-ae34-eb9e3037cf68"
           }]
        }
        ```



## Returned Value<a name="section49133105173551"></a>

-   Normal

    200

-   Abnormal

    <a name="table26085635173551"></a>
    <table><thead align="left"><tr id="row48029464173551"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p65181382173551"><a name="p65181382173551"></a><a name="p65181382173551"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p45200629173551"><a name="p45200629173551"></a><a name="p45200629173551"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37372365173551"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p7262709173551"><a name="p7262709173551"></a><a name="p7262709173551"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p51408533173551"><a name="p51408533173551"></a><a name="p51408533173551"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row60023618173551"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p30074890173551"><a name="p30074890173551"></a><a name="p30074890173551"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p20147039173551"><a name="p20147039173551"></a><a name="p20147039173551"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row47105625173551"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p57459308173551"><a name="p57459308173551"></a><a name="p57459308173551"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p23692351173551"><a name="p23692351173551"></a><a name="p23692351173551"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row11904568173551"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p24745934173551"><a name="p24745934173551"></a><a name="p24745934173551"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p58263674173551"><a name="p58263674173551"></a><a name="p58263674173551"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row54611018173551"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p61416367173551"><a name="p61416367173551"></a><a name="p61416367173551"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p8669853173551"><a name="p8669853173551"></a><a name="p8669853173551"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row10919814173551"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p12089747173551"><a name="p12089747173551"></a><a name="p12089747173551"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p39745469173551"><a name="p39745469173551"></a><a name="p39745469173551"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


