# Querying the Number of Shared File Systems Based on Tags<a name="sfs_02_0044"></a>

## Function<a name="section10684447163819"></a>

This API is used to query the number of shared file systems based on tags.

## URI<a name="section1665327514513"></a>

-   POST /v2/\{project\_id\}/sfs/resource\_instances/action
-   Parameter description

    <a name="table22021759152019"></a>
    <table><thead align="left"><tr id="row16139965152019"><th class="cellrowborder" valign="top" width="18.56%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.4%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.65%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.39%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55089343152019"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.1 "><p id="p1781134044818"><a name="p1781134044818"></a><a name="p1781134044818"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.1.5.1.2 "><p id="p59952126152019"><a name="p59952126152019"></a><a name="p59952126152019"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.1.5.1.3 "><p id="p24284048152019"><a name="p24284048152019"></a><a name="p24284048152019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.39%" headers="mcps1.1.5.1.4 "><p id="p20850895152019"><a name="p20850895152019"></a><a name="p20850895152019"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section5063604914513"></a>

-   Parameter description

    <a name="table1836815510524"></a>
    <table><thead align="left"><tr id="row1137265565217"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.1.5.1.1"><p id="p323182219356"><a name="p323182219356"></a><a name="p323182219356"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.2"><p id="p1823122103513"><a name="p1823122103513"></a><a name="p1823122103513"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.1.5.1.3"><p id="p22392211355"><a name="p22392211355"></a><a name="p22392211355"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.52525252525253%" id="mcps1.1.5.1.4"><p id="p923122210350"><a name="p923122210350"></a><a name="p923122210350"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row169449467189"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p79441546101814"><a name="p79441546101814"></a><a name="p79441546101814"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p10944446111819"><a name="p10944446111819"></a><a name="p10944446111819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p4944546111812"><a name="p4944546111812"></a><a name="p4944546111812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p2732171413197"><a name="p2732171413197"></a><a name="p2732171413197"></a>Specifies the operation identifier. Possible values are <strong id="b842352706194826"><a name="b842352706194826"></a><a name="b842352706194826"></a>filter</strong> and <strong id="b842352706194830"><a name="b842352706194830"></a><a name="b842352706194830"></a>count</strong>. </p>
    <p id="p117321414121911"><a name="p117321414121911"></a><a name="p117321414121911"></a>Use <strong id="b130008727820429"><a name="b130008727820429"></a><a name="b130008727820429"></a>count</strong> to query the number of share instances based on tags.</p>
    </td>
    </tr>
    <tr id="row1336510521186"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p1436585213188"><a name="p1436585213188"></a><a name="p1436585213188"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p14365165201817"><a name="p14365165201817"></a><a name="p14365165201817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p1678018581927"><a name="p1678018581927"></a><a name="p1678018581927"></a>Array of matchs</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p728211260546"><a name="p728211260546"></a><a name="p728211260546"></a>Specifies the share resource query field. If this parameter is left null, all shared file systems of the tenant are searched by default.</p>
    </td>
    </tr>
    <tr id="row113011219209"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p31307213203"><a name="p31307213203"></a><a name="p31307213203"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p181301524209"><a name="p181301524209"></a><a name="p181301524209"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p14130102182017"><a name="p14130102182017"></a><a name="p14130102182017"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p16333162443616"><a name="p16333162443616"></a><a name="p16333162443616"></a>Specifies the tag search field, which is a list of tags. Only shared file systems containing all the listed tags can be returned. Tags in this search criteria are in the AND relationship. Specifically, a shared file system can be searched only when it meets all the tag search criteria. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b10421153017244"><a name="b10421153017244"></a><a name="b10421153017244"></a>tags</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row128182814538"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p17989173462918"><a name="p17989173462918"></a><a name="p17989173462918"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p2993834172910"><a name="p2993834172910"></a><a name="p2993834172910"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p4650203210320"><a name="p4650203210320"></a><a name="p4650203210320"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p8191134114119"><a name="p8191134114119"></a><a name="p8191134114119"></a>Specifies the tag search field, which is a list of tags. Shared file systems that contain any listed tag will be returned. Tags in this search criteria are in the OR relationship. Specifically, a shared file system can be searched as long as it meets one tag search condition. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b217184119169"><a name="b217184119169"></a><a name="b217184119169"></a>tags_any</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row64553645313"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p102065115306"><a name="p102065115306"></a><a name="p102065115306"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p8200161814304"><a name="p8200161814304"></a><a name="p8200161814304"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p42796356319"><a name="p42796356319"></a><a name="p42796356319"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p46818135493"><a name="p46818135493"></a><a name="p46818135493"></a>Specifies the tag search field, which is a list of tags. Only shared file systems that contain none of the listed tags will be returned. Tags in this search criteria are in the NOR relationship. Specifically, a shared file system can be searched only when it does not meet any tag search criteria. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b132411321178"><a name="b132411321178"></a><a name="b132411321178"></a>not_tags</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row192681840145316"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p5651446302"><a name="p5651446302"></a><a name="p5651446302"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p19414193412306"><a name="p19414193412306"></a><a name="p19414193412306"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p209881837939"><a name="p209881837939"></a><a name="p209881837939"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p460582620498"><a name="p460582620498"></a><a name="p460582620498"></a>Specifies the tag search field, which is a list of tags. Shared file systems that do not contain any of the listed tags will be returned. Tags in this search criteria are in the NAND relationship. Specifically, a shared file system can be searched as long as it does not meet one tag search condition. In the key-values structure of each tag search condition, tag values are in the OR relationship. If the value of <strong id="b459375741812"><a name="b459375741812"></a><a name="b459375741812"></a>not_tags_any</strong> is not specified, all shared file systems meet the requirement of this tag search field. This field contains a maximum of 10 tag keys and each tag key has a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Tag keys must be unique. Tag values in a key-values structure must be unique.</p>
    </td>
    </tr>
    <tr id="row4821263355"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.1 "><p id="p15261303211"><a name="p15261303211"></a><a name="p15261303211"></a>sys_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="p1126110016219"><a name="p1126110016219"></a><a name="p1126110016219"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.1.5.1.3 "><p id="p528414314310"><a name="p528414314310"></a><a name="p528414314310"></a>Array of tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.1.5.1.4 "><p id="p4451840122313"><a name="p4451840122313"></a><a name="p4451840122313"></a>Only the op_service permission can use this field to filter resources.</p>
    <a name="ol1745740192319"></a><a name="ol1745740192319"></a><ol id="ol1745740192319"><li>Currently, TMS can invoke only one tag structure key, <strong id="b10282125172214"><a name="b10282125172214"></a><a name="b10282125172214"></a>_sys_enterprise_project_id</strong>.</li><li>Currently, <strong id="b16765732174211"><a name="b16765732174211"></a><a name="b16765732174211"></a>key</strong> contains only one value.</li><li><strong id="b635617586220"><a name="b635617586220"></a><a name="b635617586220"></a>sys_tags</strong> and tenant tag filtering conditions (<strong id="b153571858172213"><a name="b153571858172213"></a><a name="b153571858172213"></a>tags</strong>, <strong id="b1435719586221"><a name="b1435719586221"></a><a name="b1435719586221"></a>tags_any</strong>, <strong id="b23571458162218"><a name="b23571458162218"></a><a name="b23571458162218"></a>not_tags</strong>, and <strong id="b183581658172219"><a name="b183581658172219"></a><a name="b183581658172219"></a>not_tags_any</strong>) cannot be used at the same time.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-notice.gif) **NOTICE:**   
    >In the request parameters, tag search fields  **tags**,  **tags\_any**,  **not\_tags**, and  **not\_tags\_any**  are optional and can be combined with each other. Such tag search fields are in the AND relationship.  

-   Description of the  **match**  field

    <a name="table8700165114918"></a>
    <table><thead align="left"><tr id="row18704351184920"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.1.5.1.1"><p id="p12976164364810"><a name="p12976164364810"></a><a name="p12976164364810"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.270000000000001%" id="mcps1.1.5.1.2"><p id="p597674316485"><a name="p597674316485"></a><a name="p597674316485"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p1597694317485"><a name="p1597694317485"></a><a name="p1597694317485"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.1.5.1.4"><p id="p797616433489"><a name="p797616433489"></a><a name="p797616433489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5711851104916"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p1171285194914"><a name="p1171285194914"></a><a name="p1171285194914"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p9713651194915"><a name="p9713651194915"></a><a name="p9713651194915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p1271417518493"><a name="p1271417518493"></a><a name="p1271417518493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p15715105110494"><a name="p15715105110494"></a><a name="p15715105110494"></a>Specifies the key. The value is fixed to <strong id="b842352706195317"><a name="b842352706195317"></a><a name="b842352706195317"></a>resource_name</strong>.</p>
    </td>
    </tr>
    <tr id="row167164518492"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p197176519493"><a name="p197176519493"></a><a name="p197176519493"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p107191513491"><a name="p107191513491"></a><a name="p107191513491"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p572005134917"><a name="p572005134917"></a><a name="p572005134917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p6384205191014"><a name="p6384205191014"></a><a name="p6384205191014"></a>Specifies the value. <strong id="b84235270614626"><a name="b84235270614626"></a><a name="b84235270614626"></a>value</strong> indicates the name of a shared file system. An empty string specifies an exact match and only shared file systems whose names are empty can be queried. A non-empty string specifies a fuzzy query (case insensitive). The value can contain a maximum of 255 characters. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **tag**  field

    <a name="table14385185545214"></a>
    <table><thead align="left"><tr id="row5389135517522"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.1"><p id="p73318416536"><a name="p73318416536"></a><a name="p73318416536"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.5.1.2"><p id="p533154116533"><a name="p533154116533"></a><a name="p533154116533"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.3"><p id="p3331641105313"><a name="p3331641105313"></a><a name="p3331641105313"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.1.5.1.4"><p id="p133317414532"><a name="p133317414532"></a><a name="p133317414532"></a>Description</p>
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
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.3 "><p id="p4660194816310"><a name="p4660194816310"></a><a name="p4660194816310"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.1.5.1.4 "><p id="p240685517526"><a name="p240685517526"></a><a name="p240685517526"></a>Lists the values. Each value can contain a maximum of 255 characters. If the value is left empty, any value is matched. The values are in the OR relationship. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "action": "count",
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
        "action": "count",
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
        "action": "count",
        "matches": [{
            "key": "resource_name",
            "value": "share_name"
        }]
    }
    ```


-   Example request \(with the  **action**  field only\)

    ```
    {
        "action": "count"
    }
    ```


## Response<a name="section6408307814513"></a>

-   Parameter description

    <a name="table146375523240"></a>
    <table><thead align="left"><tr id="row1268155212411"><th class="cellrowborder" valign="top" width="26.31736826317368%" id="mcps1.1.4.1.1"><p id="p18129185585413"><a name="p18129185585413"></a><a name="p18129185585413"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.52644735526447%" id="mcps1.1.4.1.2"><p id="p171457558543"><a name="p171457558543"></a><a name="p171457558543"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.15618438156184%" id="mcps1.1.4.1.3"><p id="p0145185515546"><a name="p0145185515546"></a><a name="p0145185515546"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row166826528247"><td class="cellrowborder" valign="top" width="26.31736826317368%" headers="mcps1.1.4.1.1 "><p id="p19682145262413"><a name="p19682145262413"></a><a name="p19682145262413"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.52644735526447%" headers="mcps1.1.4.1.2 "><p id="p9682125212417"><a name="p9682125212417"></a><a name="p9682125212417"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.15618438156184%" headers="mcps1.1.4.1.3 "><p id="p1247417599262"><a name="p1247417599262"></a><a name="p1247417599262"></a>Specifies the total number of shared file systems that meet the query criteria.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
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


