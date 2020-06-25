# Querying Resources by Tag<a name="dws_02_0048"></a>

## Function<a name="section1828015651013"></a>

This API is used to query resource instances that meet the specified tag filtering criteria.

## URI<a name="section128135691019"></a>

-   URI format

    POST /v1.0/\{project\_id\}/clusters/resource\_instances/action

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table142911156131015"></a>
    <table><thead align="left"><tr id="row166405617107"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p186647562103"><a name="p186647562103"></a><a name="p186647562103"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p16642056141019"><a name="p16642056141019"></a><a name="p16642056141019"></a><strong id="b84235270684256"><a name="b84235270684256"></a><a name="b84235270684256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p866435616103"><a name="p866435616103"></a><a name="p866435616103"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p156641056121015"><a name="p156641056121015"></a><a name="p156641056121015"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10664115616100"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p7664856181014"><a name="p7664856181014"></a><a name="p7664856181014"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p8664195613104"><a name="p8664195613104"></a><a name="p8664195613104"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p156641956111020"><a name="p156641956111020"></a><a name="p156641956111020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p14202648155510"><a name="p14202648155510"></a><a name="p14202648155510"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section23016560109"></a>

-   Sample request when  **action**  is set to  **filter**

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/resource_instances/action
    {
      "offset": "100", 
      "limit": "100", 
      "action": "filter", 
      "matches":[
          {
            "key": "resource_name", 
            "value": "dws"
           }
      ], 
    
      "tags": [
        {
          "key": "Flower", 
          "values": [
            "rose", 
            "holly"
          ]
        }
      ],
      "tags_any": [
        {
          "key": "Food", 
          "values": [
            "pie"
          ]
        }
      ],
      "not_tags": [
        {
          "key": "juice", 
          "values": [
            "apple"
            
          ]
        }
      ],
      "not_tags_any": [
        {
          "key": "color", 
          "values": [
            "red", 
            "green"
          ]
        }
      ]
    
    }
    ```

-   Sample request when  **action**  is set to  **count**

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/resource_instances/action
    {
      "action": "count", 
    
      "tags": [
        {
          "key": "Flower", 
          "values": [
            "rose", 
            "holly"
          ]
    },
    {
          "key": "Food", 
          "values": [
            "pie", 
            "rice"
          ]
        }
      ], 
      "tags_any": [
        {
          "key": "Food", 
          "values": [
            "pie"
          ]
        }
      ],
      "not_tags": [
        {
          "key": "juice", 
          "values": [
            "apple"
            
          ]
        }
      ],
      "not_tags_any": [
        {
          "key": "color", 
          "values": [
            "red", 
            "green"
          ]
        }
      ], 
    
    "matches":[
    {
            "key": "resource_name", 
            "value": "dws"
           }
    ]
    }
    ```

-   Parameter description

    **Table  2**  Request parameter description

    <a name="table1932695621011"></a>
    <table><thead align="left"><tr id="row16664156131012"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="p16642056111010"><a name="p16642056111010"></a><a name="p16642056111010"></a><strong id="b841103987"><a name="b841103987"></a><a name="b841103987"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p966535631016"><a name="p966535631016"></a><a name="p966535631016"></a><strong id="b1286104708"><a name="b1286104708"></a><a name="b1286104708"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="p2665185641016"><a name="p2665185641016"></a><a name="p2665185641016"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.43564356435643%" id="mcps1.2.5.1.4"><p id="p6665356101011"><a name="p6665356101011"></a><a name="p6665356101011"></a><strong id="b986622748"><a name="b986622748"></a><a name="b986622748"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row146651256171015"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p566511566109"><a name="p566511566109"></a><a name="p566511566109"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p10665195601018"><a name="p10665195601018"></a><a name="p10665195601018"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p10665185619100"><a name="p10665185619100"></a><a name="p10665185619100"></a>List&lt;tag&gt; (For details, see <a href="#table22741648352">Table 3</a>.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p16665185616104"><a name="p16665185616104"></a><a name="p16665185616104"></a>The resources to be queried contain tags listed in <strong id="b1382599853193448"><a name="b1382599853193448"></a><a name="b1382599853193448"></a>tags</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing all tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row184094119580"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p7410201115810"><a name="p7410201115810"></a><a name="p7410201115810"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p841013185820"><a name="p841013185820"></a><a name="p841013185820"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p197602172012"><a name="p197602172012"></a><a name="p197602172012"></a>List&lt;tag&gt; (For details, see <a href="#table22741648352">Table 3</a>.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p841115135814"><a name="p841115135814"></a><a name="p841115135814"></a>The resources to be queried contain any tags listed in <strong id="b2119851361193951"><a name="b2119851361193951"></a><a name="b2119851361193951"></a>tags_any</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing the tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row1972413549010"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p472514541309"><a name="p472514541309"></a><a name="p472514541309"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p872575418012"><a name="p872575418012"></a><a name="p872575418012"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p1741714531014"><a name="p1741714531014"></a><a name="p1741714531014"></a>List&lt;tag&gt; (For details, see <a href="#table22741648352">Table 3</a>.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p1272715540019"><a name="p1272715540019"></a><a name="p1272715540019"></a>The resources to be queried do not contain tags listed in <strong id="b548729334194419"><a name="b548729334194419"></a><a name="b548729334194419"></a>not_tags</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing no tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row123221111816"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p123221216119"><a name="p123221216119"></a><a name="p123221216119"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p43232011412"><a name="p43232011412"></a><a name="p43232011412"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p1617956612"><a name="p1617956612"></a><a name="p1617956612"></a>List&lt;tag&gt; (For details, see <a href="#table22741648352">Table 3</a>.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p432412113114"><a name="p432412113114"></a><a name="p432412113114"></a>The resources to be queried do not contain any tags listed in <strong id="b842352706204523"><a name="b842352706204523"></a><a name="b842352706204523"></a>not_tags_any</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing no tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row3665165661013"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p11665125611012"><a name="p11665125611012"></a><a name="p11665125611012"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p19665756101010"><a name="p19665756101010"></a><a name="p19665756101010"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p17665456111014"><a name="p17665456111014"></a><a name="p17665456111014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p1066517568103"><a name="p1066517568103"></a><a name="p1066517568103"></a>Maximum number of records returned in the query result. This parameter is not displayed when <strong id="b842352706195922"><a name="b842352706195922"></a><a name="b842352706195922"></a>action</strong> is set to <strong id="b842352706195927"><a name="b842352706195927"></a><a name="b842352706195927"></a>count</strong>. If <strong id="b84235270692122"><a name="b84235270692122"></a><a name="b84235270692122"></a>action</strong> is set to <strong id="b84235270692134"><a name="b84235270692134"></a><a name="b84235270692134"></a>filter</strong>, this parameter takes effect. Its value ranges from 1 to 1000 (default).</p>
    </td>
    </tr>
    <tr id="row166545621016"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p156657561102"><a name="p156657561102"></a><a name="p156657561102"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p18665105651015"><a name="p18665105651015"></a><a name="p18665105651015"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p266510568101"><a name="p266510568101"></a><a name="p266510568101"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p9665175681011"><a name="p9665175681011"></a><a name="p9665175681011"></a>Start location of pagination query. The query starts from the next resource of the specified location. When querying the data on the first page, you do not need to specify this parameter. When querying the data on subsequent pages, set this parameter to the value in the response body returned by querying data of the previous page. This parameter is not displayed when <strong id="b84235270611518"><a name="b84235270611518"></a><a name="b84235270611518"></a>action</strong> is set to <strong id="b842352706115112"><a name="b842352706115112"></a><a name="b842352706115112"></a>count</strong>. If <strong id="b84235270692726"><a name="b84235270692726"></a><a name="b84235270692726"></a>action</strong> is set to <strong id="b84235270692731"><a name="b84235270692731"></a><a name="b84235270692731"></a>filter</strong>, this parameter takes effect. Its value can be 0 (default) or a positive integer.</p>
    </td>
    </tr>
    <tr id="row1666515618108"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p17665165611013"><a name="p17665165611013"></a><a name="p17665165611013"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p9665115651018"><a name="p9665115651018"></a><a name="p9665115651018"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p666595612108"><a name="p666595612108"></a><a name="p666595612108"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p37391512194320"><a name="p37391512194320"></a><a name="p37391512194320"></a>Identifies the operation. The value can be <strong id="b842352706112823"><a name="b842352706112823"></a><a name="b842352706112823"></a>filter</strong> or <strong id="b842352706112836"><a name="b842352706112836"></a><a name="b842352706112836"></a>count</strong>.</p>
    <a name="ul9651143712433"></a><a name="ul9651143712433"></a><ul id="ul9651143712433"><li><strong id="b842352706103947"><a name="b842352706103947"></a><a name="b842352706103947"></a>filter</strong>: indicates filtering. When both <strong id="b842352706115817"><a name="b842352706115817"></a><a name="b842352706115817"></a>limit</strong> and <strong id="b842352706115819"><a name="b842352706115819"></a><a name="b842352706115819"></a>offset</strong> are configured, the returned results are displayed in pages. If both <strong id="b174822274416525"><a name="b174822274416525"></a><a name="b174822274416525"></a>limit</strong> and <strong id="b79499450016525"><a name="b79499450016525"></a><a name="b79499450016525"></a>offset</strong> are not configured, the returned results are displayed in pages only when the number of result records exceeds 1000.</li><li><strong id="b84235270620460"><a name="b84235270620460"></a><a name="b84235270620460"></a>count</strong> indicates the total number of returned records that meet the query criteria. </li></ul>
    </td>
    </tr>
    <tr id="row1466545671016"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p6665156181018"><a name="p6665156181018"></a><a name="p6665156181018"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p5665195631013"><a name="p5665195631013"></a><a name="p5665195631013"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p86652056131020"><a name="p86652056131020"></a><a name="p86652056131020"></a>List&lt;match&gt; </p>
    </td>
    <td class="cellrowborder" valign="top" width="56.43564356435643%" headers="mcps1.2.5.1.4 "><p id="p066712561102"><a name="p066712561102"></a><a name="p066712561102"></a>Search field. <strong id="b842352706122740"><a name="b842352706122740"></a><a name="b842352706122740"></a>key</strong> indicates the field to be matched, for example, <strong id="b842352706122731"><a name="b842352706122731"></a><a name="b842352706122731"></a>resource_name</strong>. <strong id="b8423527061236"><a name="b8423527061236"></a><a name="b8423527061236"></a>value</strong> indicates the fuzzy match result. For details, see <a href="#table35821811616">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tag**  field description

    <a name="table22741648352"></a>
    <table><thead align="left"><tr id="row1129712481752"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p630274813518"><a name="p630274813518"></a><a name="p630274813518"></a><strong id="b509950657"><a name="b509950657"></a><a name="b509950657"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p230713483519"><a name="p230713483519"></a><a name="p230713483519"></a><strong id="b230853714"><a name="b230853714"></a><a name="b230853714"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p6312148855"><a name="p6312148855"></a><a name="p6312148855"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="p153173480515"><a name="p153173480515"></a><a name="p153173480515"></a><strong id="b413626565"><a name="b413626565"></a><a name="b413626565"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row173212481259"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p153272482518"><a name="p153272482518"></a><a name="p153272482518"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1033315481452"><a name="p1033315481452"></a><a name="p1033315481452"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p1534218481152"><a name="p1534218481152"></a><a name="p1534218481152"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p16990933201912"><a name="p16990933201912"></a><a name="p16990933201912"></a>Tag key. A tag key can contain a maximum of 127 Unicode characters, which cannot be null. The first and last characters cannot be spaces. </p>
    <p id="p922511632019"><a name="p922511632019"></a><a name="p922511632019"></a>It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1835014810517"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p14355348458"><a name="p14355348458"></a><a name="p14355348458"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p10359948450"><a name="p10359948450"></a><a name="p10359948450"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p8364448753"><a name="p8364448753"></a><a name="p8364448753"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p16368174816513"><a name="p16368174816513"></a><a name="p16368174816513"></a>Tag value. A tag value can contain a maximum of 255 Unicode characters, which can be null. The first and last characters cannot be spaces. It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of field  **match**

    <a name="table35821811616"></a>
    <table><thead align="left"><tr id="row1478318260"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p883718468"><a name="p883718468"></a><a name="p883718468"></a><strong id="b984821248"><a name="b984821248"></a><a name="b984821248"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p88915185615"><a name="p88915185615"></a><a name="p88915185615"></a><strong id="b679068619"><a name="b679068619"></a><a name="b679068619"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p1394111820615"><a name="p1394111820615"></a><a name="p1394111820615"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.5.1.4"><p id="p151005183619"><a name="p151005183619"></a><a name="p151005183619"></a><strong id="b1656988407"><a name="b1656988407"></a><a name="b1656988407"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1810719187610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1611431816610"><a name="p1611431816610"></a><a name="p1611431816610"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p7120121814615"><a name="p7120121814615"></a><a name="p7120121814615"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p151286181463"><a name="p151286181463"></a><a name="p151286181463"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p91361818561"><a name="p91361818561"></a><a name="p91361818561"></a>Key. Currently, it can only be <strong id="b842352706191718"><a name="b842352706191718"></a><a name="b842352706191718"></a>resource_name</strong>.</p>
    </td>
    </tr>
    <tr id="row714641818616"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p31491918669"><a name="p31491918669"></a><a name="p31491918669"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p8156318464"><a name="p8156318464"></a><a name="p8156318464"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p1016213183613"><a name="p1016213183613"></a><a name="p1016213183613"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p161671181265"><a name="p161671181265"></a><a name="p161671181265"></a>Key value. Each value can contain a maximum of 255 Unicode characters.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Response**<a name="section5386125681010"></a>

-   Sample response

    Response body when  **action**  is set to  **filter**

    ```
    { 
          "resources": [
             {
                "resource_detail": null, 
                "resource_id": "4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90", 
                "resource_name": "dws-Flower-Food", 
                "tags": [
                    {
                       "key": "Flower",
                       "value": "rose"
                    },
                    {
                       "key": "Flower",
                       "value": "holly"
                    }
                 ]
             }
           ], 
          "total_count": 1
    }
    ```

    Response body when  **action**  is set to  **count**

    ```
    {
           "total_count": 1
    }
    ```


-   Parameter description

    **Table  5**  Response parameter description

    <a name="table739185619102"></a>
    <table><thead align="left"><tr id="row116700566105"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p18670155611018"><a name="p18670155611018"></a><a name="p18670155611018"></a><strong id="b1745091463"><a name="b1745091463"></a><a name="b1745091463"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p1670756161018"><a name="p1670756161018"></a><a name="p1670756161018"></a><strong id="b1553565091"><a name="b1553565091"></a><a name="b1553565091"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p1671556201012"><a name="p1671556201012"></a><a name="p1671556201012"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="p4671155621010"><a name="p4671155621010"></a><a name="p4671155621010"></a><strong id="b1370565223"><a name="b1370565223"></a><a name="b1370565223"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1967118563100"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p567113563105"><a name="p567113563105"></a><a name="p567113563105"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1767125651019"><a name="p1767125651019"></a><a name="p1767125651019"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p7671135651010"><a name="p7671135651010"></a><a name="p7671135651010"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p5671135611019"><a name="p5671135611019"></a><a name="p5671135611019"></a>Resources that meet the search criteria. For details, see <a href="#table073674120717">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row136718565102"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p16671185620100"><a name="p16671185620100"></a><a name="p16671185620100"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p156711856161014"><a name="p156711856161014"></a><a name="p156711856161014"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p14671756131013"><a name="p14671756131013"></a><a name="p14671756131013"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p166712560100"><a name="p166712560100"></a><a name="p166712560100"></a>Total number of queried records</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Description of the  **resource**  field

    <a name="table073674120717"></a>
    <table><thead align="left"><tr id="row167771141274"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p177861341974"><a name="p177861341974"></a><a name="p177861341974"></a><strong id="b1086476746"><a name="b1086476746"></a><a name="b1086476746"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p1579074110712"><a name="p1579074110712"></a><a name="p1579074110712"></a><strong id="b1899792674"><a name="b1899792674"></a><a name="b1899792674"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p127991041876"><a name="p127991041876"></a><a name="p127991041876"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="p18065411079"><a name="p18065411079"></a><a name="p18065411079"></a><strong id="b1596689667"><a name="b1596689667"></a><a name="b1596689667"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row148169411974"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p18211411175"><a name="p18211411175"></a><a name="p18211411175"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1682918417719"><a name="p1682918417719"></a><a name="p1682918417719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p128331341678"><a name="p128331341678"></a><a name="p128331341678"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p7839144112716"><a name="p7839144112716"></a><a name="p7839144112716"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row1684354113714"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p17849164112718"><a name="p17849164112718"></a><a name="p17849164112718"></a>resouce_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p178551841074"><a name="p178551841074"></a><a name="p178551841074"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p19863541979"><a name="p19863541979"></a><a name="p19863541979"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p1869941571"><a name="p1869941571"></a><a name="p1869941571"></a>Resource details. The value is a resource object, used for extension. This value is left empty by default.</p>
    </td>
    </tr>
    <tr id="row6880204113718"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1988610411876"><a name="p1988610411876"></a><a name="p1988610411876"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1089313411470"><a name="p1089313411470"></a><a name="p1089313411470"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p590174111715"><a name="p590174111715"></a><a name="p590174111715"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p9910204110716"><a name="p9910204110716"></a><a name="p9910204110716"></a>List of tags. If no tag is matched, an empty array is returned. For details, see <a href="#table13501261386">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row491219411379"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p19174411070"><a name="p19174411070"></a><a name="p19174411070"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p69231741778"><a name="p69231741778"></a><a name="p69231741778"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p199312041576"><a name="p199312041576"></a><a name="p199312041576"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p12939134117710"><a name="p12939134117710"></a><a name="p12939134117710"></a>Resource name. This parameter is an empty string by default if the resource name is not specified.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **resource\_tag**  field description

    <a name="table13501261386"></a>
    <table><thead align="left"><tr id="row14389186189"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p2039936681"><a name="p2039936681"></a><a name="p2039936681"></a><strong id="b294725722"><a name="b294725722"></a><a name="b294725722"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p540986281"><a name="p540986281"></a><a name="p540986281"></a><strong id="b593851899"><a name="b593851899"></a><a name="b593851899"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p2041686386"><a name="p2041686386"></a><a name="p2041686386"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="p11425761884"><a name="p11425761884"></a><a name="p11425761884"></a><strong id="b593453975"><a name="b593453975"></a><a name="b593453975"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row343314610811"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p143786886"><a name="p143786886"></a><a name="p143786886"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1144776383"><a name="p1144776383"></a><a name="p1144776383"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p114561961388"><a name="p114561961388"></a><a name="p114561961388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p946810612810"><a name="p946810612810"></a><a name="p946810612810"></a>Tag key. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces. </p>
    <p id="p11228398620"><a name="p11228398620"></a><a name="p11228398620"></a>It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row7473361189"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p194821161788"><a name="p194821161788"></a><a name="p194821161788"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p204921961817"><a name="p204921961817"></a><a name="p204921961817"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p24991561689"><a name="p24991561689"></a><a name="p24991561689"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p15071619819"><a name="p15071619819"></a><a name="p15071619819"></a>Key value. A tag value can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces. It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="section342420568103"></a>

-   Normal

    **Table  8**  Returned value for successful requests

    <a name="table1742611562108"></a>
    <table><thead align="left"><tr id="row067575619107"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p967535615103"><a name="p967535615103"></a><a name="p967535615103"></a><strong id="b84235270615514"><a name="b84235270615514"></a><a name="b84235270615514"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p1967575613101"><a name="p1967575613101"></a><a name="p1967575613101"></a><strong id="b559229406"><a name="b559229406"></a><a name="b559229406"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1967512565100"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p106751156121011"><a name="p106751156121011"></a><a name="p106751156121011"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p13675145616108"><a name="p13675145616108"></a><a name="p13675145616108"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  9**  Returned value for failed requests

    <a name="table1428356201018"></a>
    <table><thead align="left"><tr id="row567585671011"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p166751856101011"><a name="p166751856101011"></a><a name="p166751856101011"></a><strong id="b2126801349"><a name="b2126801349"></a><a name="b2126801349"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p16754560108"><a name="p16754560108"></a><a name="p16754560108"></a><strong id="b630973449"><a name="b630973449"></a><a name="b630973449"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1267511564104"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p36751856131012"><a name="p36751856131012"></a><a name="p36751856131012"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p1167575612105"><a name="p1167575612105"></a><a name="p1167575612105"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row7675856181020"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1267585621013"><a name="p1267585621013"></a><a name="p1267585621013"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p1367518563103"><a name="p1367518563103"></a><a name="p1367518563103"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row1967517568108"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p16675145671016"><a name="p16675145671016"></a><a name="p16675145671016"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p26751356181014"><a name="p26751356181014"></a><a name="p26751356181014"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row12675175614102"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p367510560107"><a name="p367510560107"></a><a name="p367510560107"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p4675175611015"><a name="p4675175611015"></a><a name="p4675175611015"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1867595601010"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p15675195612104"><a name="p15675195612104"></a><a name="p15675195612104"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p96751856161019"><a name="p96751856161019"></a><a name="p96751856161019"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


