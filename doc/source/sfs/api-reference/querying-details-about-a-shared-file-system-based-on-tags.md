# Querying Details About a Shared File System Based on Tags<a name="sfs_02_0043"></a>

## Function<a name="section10684447163819"></a>

This API is used to query details about a shared file system based on tags.

## URI<a name="section1665327514513"></a>

-   POST /v2/\{project\_id\}/sfs/resource\_instances/action
-   Parameter description

    <a name="table22021759152019"></a>
    <table><thead align="left"><tr id="row16139965152019"><th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55089343152019"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p1781134044818"><a name="p1781134044818"></a><a name="p1781134044818"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p59952126152019"><a name="p59952126152019"></a><a name="p59952126152019"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="p24284048152019"><a name="p24284048152019"></a><a name="p24284048152019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p20850895152019"><a name="p20850895152019"></a><a name="p20850895152019"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section5063604914513"></a>

-   Parameter description

    <a name="table1836815510524"></a>
    <table><thead align="left"><tr id="row1137265565217"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.1.5.1.1"><p id="p450961573411"><a name="p450961573411"></a><a name="p450961573411"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.2"><p id="p125092153348"><a name="p125092153348"></a><a name="p125092153348"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.1.5.1.3"><p id="p1950918155341"><a name="p1950918155341"></a><a name="p1950918155341"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.52525252525253%" id="mcps1.1.5.1.4"><p id="p115091615173411"><a name="p115091615173411"></a><a name="p115091615173411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8379125520523"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p163764151018"><a name="p163764151018"></a><a name="p163764151018"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p175801621814"><a name="p175801621814"></a><a name="p175801621814"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p18383165518521"><a name="p18383165518521"></a><a name="p18383165518521"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p938455505218"><a name="p938455505218"></a><a name="p938455505218"></a>Specifies the index location. The value is a character string consisting of 0 and positive integers. The default value is <strong id="b842352706102044"><a name="b842352706102044"></a><a name="b842352706102044"></a>0</strong>. The first record in the query result is the offset+1 record that meets the query criteria. </p>
    </td>
    </tr>
    <tr id="row0237959107"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p72376592019"><a name="p72376592019"></a><a name="p72376592019"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p223765914017"><a name="p223765914017"></a><a name="p223765914017"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p22371591205"><a name="p22371591205"></a><a name="p22371591205"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p16788162213172"><a name="p16788162213172"></a><a name="p16788162213172"></a>Specifies the maximum number of query records. The value is a character string consisting of integers. The default value is <strong id="b84235270617408"><a name="b84235270617408"></a><a name="b84235270617408"></a>1000</strong>. The value ranges from <strong id="b926712171409"><a name="b926712171409"></a><a name="b926712171409"></a>1</strong> to <strong id="b10987519154014"><a name="b10987519154014"></a><a name="b10987519154014"></a>1000</strong>.</p>
    <p id="p183708303178"><a name="p183708303178"></a><a name="p183708303178"></a>The number of returned records does not exceed the value of <strong id="b842352706194753"><a name="b842352706194753"></a><a name="b842352706194753"></a>limit</strong>.</p>
    </td>
    </tr>
    <tr id="row169449467189"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p79441546101814"><a name="p79441546101814"></a><a name="p79441546101814"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p10944446111819"><a name="p10944446111819"></a><a name="p10944446111819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p4944546111812"><a name="p4944546111812"></a><a name="p4944546111812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p2732171413197"><a name="p2732171413197"></a><a name="p2732171413197"></a>Specifies the operation identifier. Possible values are <strong id="b842352706194826"><a name="b842352706194826"></a><a name="b842352706194826"></a>filter</strong> and <strong id="b842352706194830"><a name="b842352706194830"></a><a name="b842352706194830"></a>count</strong>. </p>
    <p id="p117321414121911"><a name="p117321414121911"></a><a name="p117321414121911"></a>Use <strong id="b1500963531194839"><a name="b1500963531194839"></a><a name="b1500963531194839"></a>filter</strong> to query details of a shared file system using tags.</p>
    </td>
    </tr>
    <tr id="row1336510521186"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p1436585213188"><a name="p1436585213188"></a><a name="p1436585213188"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p14365165201817"><a name="p14365165201817"></a><a name="p14365165201817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p936575219188"><a name="p936575219188"></a><a name="p936575219188"></a>Array of matchs</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p728211260546"><a name="p728211260546"></a><a name="p728211260546"></a>Specifies the share resource query field. If this parameter is left null, all shared file systems of the tenant are searched by default.</p>
    </td>
    </tr>
    <tr id="row113011219209"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p31307213203"><a name="p31307213203"></a><a name="p31307213203"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p181301524209"><a name="p181301524209"></a><a name="p181301524209"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p1673521118110"><a name="p1673521118110"></a><a name="p1673521118110"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p16333162443616"><a name="p16333162443616"></a><a name="p16333162443616"></a>Specifies the tag search field, which is a list of tags. Only shared file systems containing all the listed tags can be returned. Tags in this search criteria are in the AND relationship. Specifically, a shared file system can be searched only when it meets all the tag search criteria. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b97747015105"><a name="b97747015105"></a><a name="b97747015105"></a>tags</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row27613205290"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p17989173462918"><a name="p17989173462918"></a><a name="p17989173462918"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p2993834172910"><a name="p2993834172910"></a><a name="p2993834172910"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p1999623412911"><a name="p1999623412911"></a><a name="p1999623412911"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p8191134114119"><a name="p8191134114119"></a><a name="p8191134114119"></a>Specifies the tag search field, which is a list of tags. Shared file systems that contain any listed tag will be returned. Tags in this search criteria are in the OR relationship. Specifically, a shared file system can be searched as long as it meets one tag search condition. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b1468823103513"><a name="b1468823103513"></a><a name="b1468823103513"></a>tags_any</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row520617114308"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p102065115306"><a name="p102065115306"></a><a name="p102065115306"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p8200161814304"><a name="p8200161814304"></a><a name="p8200161814304"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p1794353214118"><a name="p1794353214118"></a><a name="p1794353214118"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p46818135493"><a name="p46818135493"></a><a name="p46818135493"></a>Specifies the tag search field, which is a list of tags. Only shared file systems that contain none of the listed tags will be returned. Tags in this search criteria are in the NOR relationship. Specifically, a shared file system can be searched only when it does not meet any tag search criteria. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b560215593352"><a name="b560215593352"></a><a name="b560215593352"></a>not_tags</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row5651747303"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p5651446302"><a name="p5651446302"></a><a name="p5651446302"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p19414193412306"><a name="p19414193412306"></a><a name="p19414193412306"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p619611362110"><a name="p619611362110"></a><a name="p619611362110"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p460582620498"><a name="p460582620498"></a><a name="p460582620498"></a>Specifies the tag search field, which is a list of tags. Shared file systems that do not contain any of the listed tags will be returned. Tags in this search criteria are in the NAND relationship. Specifically, a shared file system can be searched as long as it does not meet one tag search condition. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b988895881810"><a name="b988895881810"></a><a name="b988895881810"></a>not_tags_any</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row22616012115"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p15261303211"><a name="p15261303211"></a><a name="p15261303211"></a>sys_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p1126110016219"><a name="p1126110016219"></a><a name="p1126110016219"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p84989317238"><a name="p84989317238"></a><a name="p84989317238"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p4451840122313"><a name="p4451840122313"></a><a name="p4451840122313"></a>Only the op_service permission can use this field to filter resources.</p>
    <a name="ol1745740192319"></a><a name="ol1745740192319"></a><ol id="ol1745740192319"><li>Currently, TMS can invoke only one tag structure key, <strong id="b14988854174116"><a name="b14988854174116"></a><a name="b14988854174116"></a>_sys_enterprise_project_id</strong>.</li><li>Currently, <strong id="b13702142719416"><a name="b13702142719416"></a><a name="b13702142719416"></a>key</strong> contains only one value.</li><li><strong id="b11675804193"><a name="b11675804193"></a><a name="b11675804193"></a>sys_tags</strong> and tenant tag filtering conditions (<strong id="b171831943151919"><a name="b171831943151919"></a><a name="b171831943151919"></a>tags</strong>, <strong id="b14395134713191"><a name="b14395134713191"></a><a name="b14395134713191"></a>tags_any</strong>, <strong id="b1850712509192"><a name="b1850712509192"></a><a name="b1850712509192"></a>not_tags</strong>, and <strong id="b858795419195"><a name="b858795419195"></a><a name="b858795419195"></a>not_tags_any</strong>) cannot be used at the same time.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-notice.gif) **NOTICE:**   
    >In the request parameters, tag search fields  **tags**,  **tags\_any**,  **not\_tags**, and  **not\_tags\_any**  are optional and can be combined with each other. Such tag search fields are in the AND relationship.  

-   Description of the  **match**  field

    <a name="table8700165114918"></a>
    <table><thead align="left"><tr id="row18704351184920"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.1.5.1.1"><p id="p189162227348"><a name="p189162227348"></a><a name="p189162227348"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.270000000000001%" id="mcps1.1.5.1.2"><p id="p179169221348"><a name="p179169221348"></a><a name="p179169221348"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p16916162211347"><a name="p16916162211347"></a><a name="p16916162211347"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.1.5.1.4"><p id="p1891632243416"><a name="p1891632243416"></a><a name="p1891632243416"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5711851104916"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p1171285194914"><a name="p1171285194914"></a><a name="p1171285194914"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p9713651194915"><a name="p9713651194915"></a><a name="p9713651194915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p1271417518493"><a name="p1271417518493"></a><a name="p1271417518493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p15715105110494"><a name="p15715105110494"></a><a name="p15715105110494"></a>Specifies the key. The value is fixed to <strong id="b842352706195317"><a name="b842352706195317"></a><a name="b842352706195317"></a>resource_name</strong>. </p>
    </td>
    </tr>
    <tr id="row167164518492"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p197176519493"><a name="p197176519493"></a><a name="p197176519493"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p107191513491"><a name="p107191513491"></a><a name="p107191513491"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p572005134917"><a name="p572005134917"></a><a name="p572005134917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p6384205191014"><a name="p6384205191014"></a><a name="p6384205191014"></a>Specifies the value. <strong id="b782741862114"><a name="b782741862114"></a><a name="b782741862114"></a>value</strong> indicates the name of a shared file system. An empty string specifies an exact match and only shared file systems whose names are empty can be queried. A non-empty string specifies a fuzzy query (case insensitive). The value can contain a maximum of 255 characters. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **tag**  field

    <a name="table14385185545214"></a>
    <table><thead align="left"><tr id="row5389135517522"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.1"><p id="p210392663413"><a name="p210392663413"></a><a name="p210392663413"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.5.1.2"><p id="p610320267341"><a name="p610320267341"></a><a name="p610320267341"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.3"><p id="p181033266340"><a name="p181033266340"></a><a name="p181033266340"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.1.5.1.4"><p id="p20119162643420"><a name="p20119162643420"></a><a name="p20119162643420"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10396165515211"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p7397185512522"><a name="p7397185512522"></a><a name="p7397185512522"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p19398125516523"><a name="p19398125516523"></a><a name="p19398125516523"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.3 "><p id="p18399255165215"><a name="p18399255165215"></a><a name="p18399255165215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.1.5.1.4 "><p id="p14400185515528"><a name="p14400185515528"></a><a name="p14400185515528"></a>Specifies the key of the tag. A tag key consists of up to 127 characters. This parameter cannot be left empty. </p>
    </td>
    </tr>
    <tr id="row144011055105210"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p144021355135210"><a name="p144021355135210"></a><a name="p144021355135210"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p1640495512522"><a name="p1640495512522"></a><a name="p1640495512522"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.3 "><p id="p8759164412113"><a name="p8759164412113"></a><a name="p8759164412113"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.1.5.1.4 "><p id="p240685517526"><a name="p240685517526"></a><a name="p240685517526"></a>Lists the values. Each value can contain a maximum of 255 characters. If the value is left empty, any value is matched. The values are in the OR relationship. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "offset": "0",
        "limit": "100",
        "action": "filter",
        "matches": [{
            "key": "resource_name",
            "value": "share_name"
        }],
        "tags": [{
            "key": "key1",
            "values": ["value2"]
        }, {
            "key": "key2",
            "values": []
        }],
        "tags_any": [{
            "key": "key3",
            "values": ["value3"]
        }, {
            "key": "key4",
            "values": []
        }],
        "not_tags": [{
            "key": "key5",
            "values": ["value5"]
        }, {
            "key": "key6",
            "values": []
        }],
        "not_tags_any": [{
            "key": "key7",
            "values": ["value7", "value8"]
        }, {
            "key": "key9",
            "values": []
        }]
    }
    ```


-   Example request \(without passing  **matches**\)

    ```
    {
        "offset": "0",
        "limit": "100",
        "action": "filter",
        "tags": [{
            "key": "key1",
            "values": ["value2"]
        }, {
            "key": "key2",
            "values": []
        }]
    }
    ```

-   Example request \(without passing  **limit**  and  **offset**\)

    ```
    {
        "action": "filter",
        "matches": [{
            "key": "resource_name",
            "value": "share_name"
        }],
        "tags": [{
            "key": "key1",
            "values": ["value2"]
        }, {
            "key": "key2",
            "values": []
        }]
    }
    ```


-   Example request \(without passing  **tags**,  **not\_tags**,  **tags\_any**, and  **not\_tags\_any**\)

    ```
    {
        "offset": "0",
        "limit": "100",
        "action": "filter",
        "matches": [{
            "key": "resource_name",
            "value": "share_name"
        }]
    }
    ```


-   Example request \(with the  **action**  field only\)

    ```
    {
        "action": "filter"
    }
    ```


## Response<a name="section6408307814513"></a>

-   Parameter description

    <a name="table146375523240"></a>
    <table><thead align="left"><tr id="row1268155212411"><th class="cellrowborder" valign="top" width="26.58265826582658%" id="mcps1.1.4.1.1"><p id="p13509163313410"><a name="p13509163313410"></a><a name="p13509163313410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.44354435443544%" id="mcps1.1.4.1.2"><p id="p2525163316349"><a name="p2525163316349"></a><a name="p2525163316349"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.973797379737974%" id="mcps1.1.4.1.3"><p id="p95256339346"><a name="p95256339346"></a><a name="p95256339346"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4681152162413"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.1.4.1.1 "><p id="p19681152102419"><a name="p19681152102419"></a><a name="p19681152102419"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.44354435443544%" headers="mcps1.1.4.1.2 "><p id="p668112526243"><a name="p668112526243"></a><a name="p668112526243"></a>Array of resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.973797379737974%" headers="mcps1.1.4.1.3 "><p id="p158814432712"><a name="p158814432712"></a><a name="p158814432712"></a>Specifies the list of shared file systems that meet the query criteria.</p>
    </td>
    </tr>
    <tr id="row166826528247"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.1.4.1.1 "><p id="p19682145262413"><a name="p19682145262413"></a><a name="p19682145262413"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.44354435443544%" headers="mcps1.1.4.1.2 "><p id="p9682125212417"><a name="p9682125212417"></a><a name="p9682125212417"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.973797379737974%" headers="mcps1.1.4.1.3 "><p id="p20741102713270"><a name="p20741102713270"></a><a name="p20741102713270"></a>Specifies the total number of shared file systems that meet the query criteria.</p>
    <div class="note" id="note198964013326"><a name="note198964013326"></a><a name="note198964013326"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1698944013324"><a name="p1698944013324"></a><a name="p1698944013324"></a><strong id="b4652848917321"><a name="b4652848917321"></a><a name="b4652848917321"></a>total_count</strong> specifies the total number of shared file systems that meet the query criteria, instead of the number returned after you set <strong id="b8423527069364"><a name="b8423527069364"></a><a name="b8423527069364"></a>offset</strong> and <strong id="b8423527069368"><a name="b8423527069368"></a><a name="b8423527069368"></a>limit</strong>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Data structure of the  **resource**  field

    <a name="table871281418254"></a>
    <table><thead align="left"><tr id="row883611492519"><th class="cellrowborder" valign="top" width="26.31736826317368%" id="mcps1.1.4.1.1"><p id="p583614403340"><a name="p583614403340"></a><a name="p583614403340"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.52644735526447%" id="mcps1.1.4.1.2"><p id="p18527404345"><a name="p18527404345"></a><a name="p18527404345"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.15618438156184%" id="mcps1.1.4.1.3"><p id="p185274014345"><a name="p185274014345"></a><a name="p185274014345"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8836111452512"><td class="cellrowborder" valign="top" width="26.31736826317368%" headers="mcps1.1.4.1.1 "><p id="p9836131412510"><a name="p9836131412510"></a><a name="p9836131412510"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.52644735526447%" headers="mcps1.1.4.1.2 "><p id="p158361714142511"><a name="p158361714142511"></a><a name="p158361714142511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.15618438156184%" headers="mcps1.1.4.1.3 "><p id="p1383641472512"><a name="p1383641472512"></a><a name="p1383641472512"></a>Specifies the share ID.</p>
    </td>
    </tr>
    <tr id="row8836121472513"><td class="cellrowborder" valign="top" width="26.31736826317368%" headers="mcps1.1.4.1.1 "><p id="p08361814192510"><a name="p08361814192510"></a><a name="p08361814192510"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.52644735526447%" headers="mcps1.1.4.1.2 "><p id="p168365141256"><a name="p168365141256"></a><a name="p168365141256"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.15618438156184%" headers="mcps1.1.4.1.3 "><p id="p1783616142254"><a name="p1783616142254"></a><a name="p1783616142254"></a>Specifies the share details. The value is a resource object, used for extension. This value is left empty by default.</p>
    </td>
    </tr>
    <tr id="row20836614182515"><td class="cellrowborder" valign="top" width="26.31736826317368%" headers="mcps1.1.4.1.1 "><p id="p1883651492510"><a name="p1883651492510"></a><a name="p1883651492510"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.52644735526447%" headers="mcps1.1.4.1.2 "><p id="p8836314122515"><a name="p8836314122515"></a><a name="p8836314122515"></a>Array of resource_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.15618438156184%" headers="mcps1.1.4.1.3 "><p id="p1836131417255"><a name="p1836131417255"></a><a name="p1836131417255"></a>Specifies the list of tags. If no tags exist, the value is an empty array by default. </p>
    </td>
    </tr>
    <tr id="row1962112717255"><td class="cellrowborder" valign="top" width="26.31736826317368%" headers="mcps1.1.4.1.1 "><p id="p4621107162513"><a name="p4621107162513"></a><a name="p4621107162513"></a>sys_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.52644735526447%" headers="mcps1.1.4.1.2 "><p id="p462120752515"><a name="p462120752515"></a><a name="p462120752515"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.15618438156184%" headers="mcps1.1.4.1.3 "><p id="p678712042612"><a name="p678712042612"></a><a name="p678712042612"></a>Only the op_service permission can obtain this field.</p>
    <a name="ol2078702010263"></a><a name="ol2078702010263"></a><ol id="ol2078702010263"><li>Currently, only one tag structure key is used, <strong id="b175413154417"><a name="b175413154417"></a><a name="b175413154417"></a>_sys_enterprise_project_id</strong>.</li><li>Currently, <strong id="b59619143448"><a name="b59619143448"></a><a name="b59619143448"></a>key</strong> contains only one value.</li></ol>
    <p id="p1878752022615"><a name="p1878752022615"></a><a name="p1878752022615"></a>This field cannot be returned in non-op_service scenarios.</p>
    </td>
    </tr>
    <tr id="row128361914162515"><td class="cellrowborder" valign="top" width="26.31736826317368%" headers="mcps1.1.4.1.1 "><p id="p88361514202515"><a name="p88361514202515"></a><a name="p88361514202515"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.52644735526447%" headers="mcps1.1.4.1.2 "><p id="p8837141442520"><a name="p8837141442520"></a><a name="p8837141442520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.15618438156184%" headers="mcps1.1.4.1.3 "><p id="p17837014142513"><a name="p17837014142513"></a><a name="p17837014142513"></a>Specifies the resource name. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Data structure of the  **resource\_tag**  field

    <a name="table18728414112510"></a>
    <table><thead align="left"><tr id="row5838171442511"><th class="cellrowborder" valign="top" width="25.64%" id="mcps1.1.4.1.1"><p id="p941375293419"><a name="p941375293419"></a><a name="p941375293419"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.9%" id="mcps1.1.4.1.2"><p id="p1541385263417"><a name="p1541385263417"></a><a name="p1541385263417"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.46%" id="mcps1.1.4.1.3"><p id="p9413135218349"><a name="p9413135218349"></a><a name="p9413135218349"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row178381314142517"><td class="cellrowborder" valign="top" width="25.64%" headers="mcps1.1.4.1.1 "><p id="p168381714142520"><a name="p168381714142520"></a><a name="p168381714142520"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.1.4.1.2 "><p id="p083841419254"><a name="p083841419254"></a><a name="p083841419254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.46%" headers="mcps1.1.4.1.3 "><p id="p1883818148258"><a name="p1883818148258"></a><a name="p1883818148258"></a>Specifies the key of the tag. The value can contain a maximum of 36 characters. This parameter cannot be left empty. It can only contain letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row3838171492513"><td class="cellrowborder" valign="top" width="25.64%" headers="mcps1.1.4.1.1 "><p id="p48381714182519"><a name="p48381714182519"></a><a name="p48381714182519"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.1.4.1.2 "><p id="p583801412259"><a name="p583801412259"></a><a name="p583801412259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.46%" headers="mcps1.1.4.1.3 "><p id="p1083891414254"><a name="p1083891414254"></a><a name="p1083891414254"></a>Specifies the value of the tag. The value contains a maximum of 43 characters and can be an empty string. It can only contain letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "resources":[
            {
                "resource_detail":{},
                "resource_id":"b1f3f06f-344d-446b-a4bf-647a225debae",
                "resource_name":"share_name",
                "tags":[
                    {
                        "key":"key1", 
                        "value": "value1"
                    },
                    {
                        "key":"key2", 
                        "value": "value2"
                    }
                ]
            }
        ],
        "total_count":1
    }
    ```


## Status Codes<a name="section4959408514513"></a>

-   Normal

    200

-   Abnormal

    <a name="table6245403714513"></a>
    <table><thead align="left"><tr id="row1507735814513"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p1330652014513"><a name="p1330652014513"></a><a name="p1330652014513"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p408636314513"><a name="p408636314513"></a><a name="p408636314513"></a><strong id="b84235270615228"><a name="b84235270615228"></a><a name="b84235270615228"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3477393214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p6522508214513"><a name="p6522508214513"></a><a name="p6522508214513"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4874025614513"><a name="p4874025614513"></a><a name="p4874025614513"></a>Invalid value.</p>
    </td>
    </tr>
    <tr id="row3600912414513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3105792214513"><a name="p3105792214513"></a><a name="p3105792214513"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p3266375714513"><a name="p3266375714513"></a><a name="p3266375714513"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row2553835814513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p5534113514513"><a name="p5534113514513"></a><a name="p5534113514513"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5344692014513"><a name="p5344692014513"></a><a name="p5344692014513"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="row1126023214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3966357214513"><a name="p3966357214513"></a><a name="p3966357214513"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5863278914513"><a name="p5863278914513"></a><a name="p5863278914513"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1011562214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1405905414513"><a name="p1405905414513"></a><a name="p1405905414513"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6504160314513"><a name="p6504160314513"></a><a name="p6504160314513"></a>The request is not completed because of a service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


