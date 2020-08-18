# Querying Resource Instances<a name="vpcep_06_0501"></a>

## Function<a name="section21621940163112"></a>

This API is used to query resources under the tenant using tags.

## URI<a name="section1916374019317"></a>

POST  /v1/\{project\_id\}/\{resource\_type\}/resource\_instances/action

[Table 1](#table51771440203117)  describes the required parameters.

**Table  1**  Parameters

<a name="table51771440203117"></a>
<table><thead align="left"><tr id="row1576512406311"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p177651840173113"><a name="p177651840173113"></a><a name="p177651840173113"></a><strong id="b1758745931312"><a name="b1758745931312"></a><a name="b1758745931312"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.2"><p id="p1076524083113"><a name="p1076524083113"></a><a name="p1076524083113"></a><strong id="b1541818141"><a name="b1541818141"></a><a name="b1541818141"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p276515401318"><a name="p276515401318"></a><a name="p276515401318"></a><strong id="b165618216149"><a name="b165618216149"></a><a name="b165618216149"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="p187651540103113"><a name="p187651540103113"></a><a name="p187651540103113"></a><strong id="b1954711311145"><a name="b1954711311145"></a><a name="b1954711311145"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6766114019315"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p16766940163116"><a name="p16766940163116"></a><a name="p16766940163116"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p1476634012318"><a name="p1476634012318"></a><a name="p1476634012318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p87665408315"><a name="p87665408315"></a><a name="p87665408315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p1476616408318"><a name="p1476616408318"></a><a name="p1476616408318"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row17661840143116"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p3766134093117"><a name="p3766134093117"></a><a name="p3766134093117"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p3766114023117"><a name="p3766114023117"></a><a name="p3766114023117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p1476634012315"><a name="p1476634012315"></a><a name="p1476634012315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p3766164043112"><a name="p3766164043112"></a><a name="p3766164043112"></a>Specifies the resource type. The value is <strong id="b1436771851415"><a name="b1436771851415"></a><a name="b1436771851415"></a>endpoint_service</strong> or <strong id="b33681818111414"><a name="b33681818111414"></a><a name="b33681818111414"></a>endpoint</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section15188194015318"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table516818404318"></a>
    <table><thead align="left"><tr id="row6764440163110"><th class="cellrowborder" valign="top" width="21.65%" id="mcps1.2.5.1.1"><p id="p8765134023112"><a name="p8765134023112"></a><a name="p8765134023112"></a><strong id="b18433103613147"><a name="b18433103613147"></a><a name="b18433103613147"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.2"><p id="p137656404310"><a name="p137656404310"></a><a name="p137656404310"></a><strong id="b10199165781416"><a name="b10199165781416"></a><a name="b10199165781416"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52%" id="mcps1.2.5.1.3"><p id="p776524043119"><a name="p776524043119"></a><a name="p776524043119"></a><strong id="b1711235851410"><a name="b1711235851410"></a><a name="b1711235851410"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.48%" id="mcps1.2.5.1.4"><p id="p117651340193116"><a name="p117651340193116"></a><a name="p117651340193116"></a><strong id="b84851939111315"><a name="b84851939111315"></a><a name="b84851939111315"></a>Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10765440143119"><td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.2.5.1.1 "><p id="p177651140183115"><a name="p177651140183115"></a><a name="p177651140183115"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.2 "><p id="p11765124053119"><a name="p11765124053119"></a><a name="p11765124053119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.3 "><p id="p12765240123118"><a name="p12765240123118"></a><a name="p12765240123118"></a>Specifies the MIME type of the entity sending the request.</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.2.5.1.4 "><p id="p576510408318"><a name="p576510408318"></a><a name="p576510408318"></a>application/json</p>
    </td>
    </tr>
    <tr id="row476514404315"><td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.2.5.1.1 "><p id="p1176514404316"><a name="p1176514404316"></a><a name="p1176514404316"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.2 "><p id="p1676514013113"><a name="p1676514013113"></a><a name="p1676514013113"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.3 "><p id="p876564053119"><a name="p876564053119"></a><a name="p876564053119"></a>Specifies the user token.</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.2.5.1.4 "><p id="p1876519401313"><a name="p1876519401313"></a><a name="p1876519401313"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Parameter description

    <a name="table62501540103117"></a>
    <table><thead align="left"><tr id="row676604023114"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p8766740193116"><a name="p8766740193116"></a><a name="p8766740193116"></a><strong id="b4208193541517"><a name="b4208193541517"></a><a name="b4208193541517"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.2"><p id="p1276674013113"><a name="p1276674013113"></a><a name="p1276674013113"></a><strong id="b1066993621512"><a name="b1066993621512"></a><a name="b1066993621512"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p5766340163116"><a name="p5766340163116"></a><a name="p5766340163116"></a><strong id="b1626224181513"><a name="b1626224181513"></a><a name="b1626224181513"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.5.1.4"><p id="p1766134023114"><a name="p1766134023114"></a><a name="p1766134023114"></a><strong id="b26652116163"><a name="b26652116163"></a><a name="b26652116163"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27661840193116"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p12766194073115"><a name="p12766194073115"></a><a name="p12766194073115"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p5766124013317"><a name="p5766124013317"></a><a name="p5766124013317"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p676654083115"><a name="p676654083115"></a><a name="p676654083115"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p67671340193115"><a name="p67671340193115"></a><a name="p67671340193115"></a>The resources to be queried contain tags listed in <strong id="b1382599853193448"><a name="b1382599853193448"></a><a name="b1382599853193448"></a>tags</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key and each tag value of the same tag key must be unique. The response returns resources containing all tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row157671540183120"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p19767194016319"><a name="p19767194016319"></a><a name="p19767194016319"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p37670409316"><a name="p37670409316"></a><a name="p37670409316"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1076715405313"><a name="p1076715405313"></a><a name="p1076715405313"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1176715406317"><a name="p1176715406317"></a><a name="p1176715406317"></a>The resources to be queried contain any tags listed in <strong id="b37901238142416"><a name="b37901238142416"></a><a name="b37901238142416"></a>tags_any</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key and each tag value of the same tag key must be unique. The response returns resources containing the tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row107671640133112"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p1276784053115"><a name="p1276784053115"></a><a name="p1276784053115"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p1376714010319"><a name="p1376714010319"></a><a name="p1376714010319"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1476764093111"><a name="p1476764093111"></a><a name="p1476764093111"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p20767174043118"><a name="p20767174043118"></a><a name="p20767174043118"></a>The resources to be queried do not contain tags listed in <strong id="b146599416244"><a name="b146599416244"></a><a name="b146599416244"></a>not_tags</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key and each tag value of the same tag key must be unique. The response returns resources containing no tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row207671640133120"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p107672401312"><a name="p107672401312"></a><a name="p107672401312"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p197671140193118"><a name="p197671140193118"></a><a name="p197671140193118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p11767144010312"><a name="p11767144010312"></a><a name="p11767144010312"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p157671440103117"><a name="p157671440103117"></a><a name="p157671440103117"></a>The resources to be queried do not contain any tags listed in <strong id="b18271148122418"><a name="b18271148122418"></a><a name="b18271148122418"></a>not_tags_any</strong>. Each resource to be queried contains a maximum of 10 keys. Each tag key can have a maximum of 10 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key and each tag value of the same tag key must be unique. The response returns resources containing no tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    </td>
    </tr>
    <tr id="row177671240153112"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p37679401317"><a name="p37679401317"></a><a name="p37679401317"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p1376724016314"><a name="p1376724016314"></a><a name="p1376724016314"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p7767144015319"><a name="p7767144015319"></a><a name="p7767144015319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p37674409310"><a name="p37674409310"></a><a name="p37674409310"></a>Sets the page size. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row13767204019319"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p4767104018319"><a name="p4767104018319"></a><a name="p4767104018319"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p576716406315"><a name="p576716406315"></a><a name="p576716406315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1976714073110"><a name="p1976714073110"></a><a name="p1976714073110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1767940153119"><a name="p1767940153119"></a><a name="p1767940153119"></a>Specifies the index position. This parameter is unavailable when <strong id="b842352706102654"><a name="b842352706102654"></a><a name="b842352706102654"></a>action</strong> is set to <strong id="b84235270610271"><a name="b84235270610271"></a><a name="b84235270610271"></a>count</strong>. If <strong id="b70205942519474"><a name="b70205942519474"></a><a name="b70205942519474"></a>offset</strong> is set to <em id="i84235269720751"><a name="i84235269720751"></a><a name="i84235269720751"></a>N</em>, the resource query starts from the N+1 piece of data. If <strong id="b842352706102717"><a name="b842352706102717"></a><a name="b842352706102717"></a>action</strong> is set to <strong id="b842352706102722"><a name="b842352706102722"></a><a name="b842352706102722"></a>filter</strong>, the value of <strong id="b84235270620648"><a name="b84235270620648"></a><a name="b84235270620648"></a>offset</strong> is <strong id="b84235270620630"><a name="b84235270620630"></a><a name="b84235270620630"></a>0</strong> by default, indicating that the query starts from the first piece of data. The <strong id="b84235270620744"><a name="b84235270620744"></a><a name="b84235270620744"></a>offset</strong> value must be a number and cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row7767040173119"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p1176710405313"><a name="p1176710405313"></a><a name="p1176710405313"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p187671740123119"><a name="p187671740123119"></a><a name="p187671740123119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p37671240163118"><a name="p37671240163118"></a><a name="p37671240163118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1876714010311"><a name="p1876714010311"></a><a name="p1876714010311"></a>Specifies the operation to perform. The value can only be <strong id="b842352706145527"><a name="b842352706145527"></a><a name="b842352706145527"></a>filter</strong> (filtering) or <strong id="b842352706145557"><a name="b842352706145557"></a><a name="b842352706145557"></a>count</strong> (querying the total number).</p>
    <p id="p117671040173115"><a name="p117671040173115"></a><a name="p117671040173115"></a>If <strong id="b8423527061184"><a name="b8423527061184"></a><a name="b8423527061184"></a>action</strong> is set to <strong id="b84235270611747"><a name="b84235270611747"></a><a name="b84235270611747"></a>filter</strong>, the query is performed based on the filter conditions. If <strong id="b1158078253111040"><a name="b1158078253111040"></a><a name="b1158078253111040"></a>action</strong> is set to <strong id="b1717869715111040"><a name="b1717869715111040"></a><a name="b1717869715111040"></a>count</strong>, only the total number of records is returned.</p>
    </td>
    </tr>
    <tr id="row276714093110"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p776774020314"><a name="p776774020314"></a><a name="p776774020314"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p19767114016313"><a name="p19767114016313"></a><a name="p19767114016313"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1676734073114"><a name="p1676734073114"></a><a name="p1676734073114"></a>List&lt;match&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p576884043118"><a name="p576884043118"></a><a name="p576884043118"></a>Specifies the search field. The tag key is the field to be matched, for example, <strong id="b1815994217155439"><a name="b1815994217155439"></a><a name="b1815994217155439"></a>resource_name</strong>. <strong id="b201314374336"><a name="b201314374336"></a><a name="b201314374336"></a>value</strong> indicates the matched value. The key is a fixed dictionary value and cannot contain duplicate keys or unsupported keys.</p>
    <p id="p77681140153116"><a name="p77681140153116"></a><a name="p77681140153116"></a>Check whether fuzzy match is required based on the <strong id="b842352706195738"><a name="b842352706195738"></a><a name="b842352706195738"></a>key</strong> value. For example, if <strong id="b842352706195830"><a name="b842352706195830"></a><a name="b842352706195830"></a>key</strong> is set to <strong id="b842352706195813"><a name="b842352706195813"></a><a name="b842352706195813"></a>resource_name</strong>, fuzzy search (case-insensitive) is performed by default. If <strong id="b842352706195917"><a name="b842352706195917"></a><a name="b842352706195917"></a>value</strong> is empty, exact match is performed. Most services do not have resources without names. In this case, an empty list is returned. If <strong id="b84235270622448"><a name="b84235270622448"></a><a name="b84235270622448"></a>key</strong> is <strong id="b842352706123558"><a name="b842352706123558"></a><a name="b842352706123558"></a>resource_id</strong>, exact match is used. Currently, only <strong id="b842352706123249"><a name="b842352706123249"></a><a name="b842352706123249"></a>resource_name</strong> for <strong id="b842352706195039"><a name="b842352706195039"></a><a name="b842352706195039"></a>key</strong> is supported. Other <strong id="b842352706195055"><a name="b842352706195055"></a><a name="b842352706195055"></a>key</strong> values will be available later.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of field  **tag**

    <a name="table1132474019312"></a>
    <table><thead align="left"><tr id="row97688406317"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p4768194017310"><a name="p4768194017310"></a><a name="p4768194017310"></a><strong id="b836775172915"><a name="b836775172915"></a><a name="b836775172915"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.2"><p id="p17768840113119"><a name="p17768840113119"></a><a name="p17768840113119"></a><strong id="b1825310814292"><a name="b1825310814292"></a><a name="b1825310814292"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p9768164012318"><a name="p9768164012318"></a><a name="p9768164012318"></a><strong id="b15586169162915"><a name="b15586169162915"></a><a name="b15586169162915"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.5.1.4"><p id="p276804018312"><a name="p276804018312"></a><a name="p276804018312"></a><strong id="b17875410162918"><a name="b17875410162918"></a><a name="b17875410162918"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1276824012317"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p197681340153120"><a name="p197681340153120"></a><a name="p197681340153120"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p127685400312"><a name="p127685400312"></a><a name="p127685400312"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p77681740123111"><a name="p77681740123111"></a><a name="p77681740123111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p8768240143116"><a name="p8768240143116"></a><a name="p8768240143116"></a>Specifies the tag key. Each tag key contains a maximum of 127 unicode characters but cannot be left blank. The system does not verify the character set of <strong id="b14679192572919"><a name="b14679192572919"></a><a name="b14679192572919"></a>key</strong> when searching for resources. <strong id="b166810258293"><a name="b166810258293"></a><a name="b166810258293"></a>key</strong> cannot be empty, an empty string, or spaces. Before using <strong id="b368202519296"><a name="b368202519296"></a><a name="b368202519296"></a>key</strong>, delete single-byte character (SBC) spaces before and after the value.</p>
    </td>
    </tr>
    <tr id="row2768740113110"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p2768114033112"><a name="p2768114033112"></a><a name="p2768114033112"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p4768154093113"><a name="p4768154093113"></a><a name="p4768154093113"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1676814013119"><a name="p1676814013119"></a><a name="p1676814013119"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p167681440123119"><a name="p167681440123119"></a><a name="p167681440123119"></a>Lists the tag values. Each value contains a maximum of 255 Unicode characters. Before using <strong id="b13350164318613"><a name="b13350164318613"></a><a name="b13350164318613"></a>values</strong>, delete SBC spaces before and after the value.</p>
    <p id="p11768184017316"><a name="p11768184017316"></a><a name="p11768184017316"></a>The value can be an empty array but cannot be left blank.</p>
    <p id="p177681740123119"><a name="p177681740123119"></a><a name="p177681740123119"></a>If the values are null, it indicates <strong id="b842352706175623"><a name="b842352706175623"></a><a name="b842352706175623"></a>any_value</strong> (querying any value). The values are in the OR relationship.</p>
    <p id="p1076812400317"><a name="p1076812400317"></a><a name="p1076812400317"></a>The system does not verify the character set of <strong id="b67441534387"><a name="b67441534387"></a><a name="b67441534387"></a>values</strong> when searching for resources, but only verifies the length.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of field  **match**

    <a name="table153401540163113"></a>
    <table><thead align="left"><tr id="row6768440123116"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p6768114023114"><a name="p6768114023114"></a><a name="p6768114023114"></a><strong id="b118842561467"><a name="b118842561467"></a><a name="b118842561467"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.2"><p id="p127680409316"><a name="p127680409316"></a><a name="p127680409316"></a><strong id="b562419581866"><a name="b562419581866"></a><a name="b562419581866"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p10768340203110"><a name="p10768340203110"></a><a name="p10768340203110"></a><strong id="b88336592613"><a name="b88336592613"></a><a name="b88336592613"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.5.1.4"><p id="p147684407317"><a name="p147684407317"></a><a name="p147684407317"></a><strong id="b111121611671"><a name="b111121611671"></a><a name="b111121611671"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1176834011318"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p57685402311"><a name="p57685402311"></a><a name="p57685402311"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p187681340143119"><a name="p187681340143119"></a><a name="p187681340143119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p197688408317"><a name="p197688408317"></a><a name="p197688408317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1768240113113"><a name="p1768240113113"></a><a name="p1768240113113"></a>Specifies the tag key. Currently, only <strong id="b380120610713"><a name="b380120610713"></a><a name="b380120610713"></a>resource_name</strong> for <strong id="b5802186373"><a name="b5802186373"></a><a name="b5802186373"></a>key</strong> is supported. Other <strong id="b58021461672"><a name="b58021461672"></a><a name="b58021461672"></a>key</strong> values will be available later.</p>
    </td>
    </tr>
    <tr id="row167695401310"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p47699401316"><a name="p47699401316"></a><a name="p47699401316"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p197691940163114"><a name="p197691940163114"></a><a name="p197691940163114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p7769124093119"><a name="p7769124093119"></a><a name="p7769124093119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p14769174043112"><a name="p14769174043112"></a><a name="p14769174043112"></a>Specifies the tag value. Each value contains a maximum of 255 Unicode characters. The character set of <strong id="b51301516870"><a name="b51301516870"></a><a name="b51301516870"></a>value</strong> is not verified.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://127.0.0.1:7443/v1/\{project\_id\}/endpoint\_service/resource\_instances/action

    or POST https://127.0.0.1:7443/v1/\{project\_id\}/endpoint/resource\_instances/action

    or POST https://127.0.0.1:7443/v1/\{project\_id\}/\{resource\_type\}/resource\_instances/action

    -   Request body when  **action**  is set to  **filter**

        ```
        {
            "offset": "100",
            "limit": "100",
            "action": "filter",
            "matches": [
                {
                    "key": "resource_name",
                    "value": "resource1"
                }
            ],
            "not_tags": [
                {
                    "key": "key1",
                    "values": [
                        "*value1",
                        "value2"
                    ]
                }
            ],
            "tags": [
                {
                    "key": "key1",
                    "values": [
                        "*value1",
                        "value2"
                    ]
                }
            ],
            "tags_any": [
                {
                    "key": "key1",
                    "values": [
                        "value1",
                        "value2"
                    ]
                }
            ],
            "not_tags_any": [
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

    -   Request body when  **action**  is set to  **count**

        ```
        {
            "action": "count",
            "not_tags": [
                {
                    "key": "key1",
                    "values": [
                        "value1",
                        "*value2"
                    ]
                }
            ],
            "tags": [
                {
                    "key": "key1",
                    "values": [
                        "value1",
                        "value2"
                    ]
                },
                {
                    "key": "key2",
                    "values": [
                        "value1",
                        "value2"
                    ]
                }
            ],
            "tags_any": [
                {
                    "key": "key1",
                    "values": [
                        "value1",
                        "value2"
                    ]
                }
            ],
            "not_tags_any": [
                {
                    "key": "key1",
                    "values": [
                        "value1",
                        "value2"
                    ]
                }
            ],
            "matches": [
                {
                    "key": "resource_name",
                    "value": "resource1"
                }
            ]
        }
        ```



## Response<a name="section183609409311"></a>

-   Parameter description

    **Table  6**  Parameter description

    <a name="table15367440153111"></a>
    <table><thead align="left"><tr id="row877012401316"><th class="cellrowborder" valign="top" width="25.002500250025%" id="mcps1.2.4.1.1"><p id="p0770154013120"><a name="p0770154013120"></a><a name="p0770154013120"></a><strong id="b201210239195"><a name="b201210239195"></a><a name="b201210239195"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.852685268526855%" id="mcps1.2.4.1.2"><p id="p377013403318"><a name="p377013403318"></a><a name="p377013403318"></a><strong id="b91611225181915"><a name="b91611225181915"></a><a name="b91611225181915"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.144814481448144%" id="mcps1.2.4.1.3"><p id="p13771134083116"><a name="p13771134083116"></a><a name="p13771134083116"></a><strong id="b106126191917"><a name="b106126191917"></a><a name="b106126191917"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13771144083120"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p14771114053110"><a name="p14771114053110"></a><a name="p14771114053110"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.852685268526855%" headers="mcps1.2.4.1.2 "><p id="p37711440133114"><a name="p37711440133114"></a><a name="p37711440133114"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.144814481448144%" headers="mcps1.2.4.1.3 "><p id="p17716401318"><a name="p17716401318"></a><a name="p17716401318"></a>N/A</p>
    </td>
    </tr>
    <tr id="row11771204019313"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p137711040153118"><a name="p137711040153118"></a><a name="p137711040153118"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.852685268526855%" headers="mcps1.2.4.1.2 "><p id="p1377117403310"><a name="p1377117403310"></a><a name="p1377117403310"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.144814481448144%" headers="mcps1.2.4.1.3 "><p id="p977119407314"><a name="p977119407314"></a><a name="p977119407314"></a>Specifies the total number of records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  Data structure description of the  **resource**  field

    <a name="table437413403312"></a>
    <table><thead align="left"><tr id="row67714403312"><th class="cellrowborder" valign="top" width="25.002500250025%" id="mcps1.2.4.1.1"><p id="p17771164023110"><a name="p17771164023110"></a><a name="p17771164023110"></a><strong id="b9822105611198"><a name="b9822105611198"></a><a name="b9822105611198"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.52265226522652%" id="mcps1.2.4.1.2"><p id="p19771154013113"><a name="p19771154013113"></a><a name="p19771154013113"></a><strong id="b3928958181912"><a name="b3928958181912"></a><a name="b3928958181912"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.47484748474848%" id="mcps1.2.4.1.3"><p id="p107711940133112"><a name="p107711940133112"></a><a name="p107711940133112"></a><strong id="b106941359181919"><a name="b106941359181919"></a><a name="b106941359181919"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7771164010311"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p13771144016315"><a name="p13771144016315"></a><a name="p13771144016315"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.52265226522652%" headers="mcps1.2.4.1.2 "><p id="p15771114033111"><a name="p15771114033111"></a><a name="p15771114033111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.47484748474848%" headers="mcps1.2.4.1.3 "><p id="p1771184083113"><a name="p1771184083113"></a><a name="p1771184083113"></a>Specifies the resource ID, which can be <strong id="b4894418162017"><a name="b4894418162017"></a><a name="b4894418162017"></a>Endpoint Service ID</strong> or <strong id="b2054402192015"><a name="b2054402192015"></a><a name="b2054402192015"></a>Endpoint ID</strong>.</p>
    </td>
    </tr>
    <tr id="row17771164016318"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p1771124093112"><a name="p1771124093112"></a><a name="p1771124093112"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.52265226522652%" headers="mcps1.2.4.1.2 "><p id="p9771194014313"><a name="p9771194014313"></a><a name="p9771194014313"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.47484748474848%" headers="mcps1.2.4.1.3 "><p id="p11771184019315"><a name="p11771184019315"></a><a name="p11771184019315"></a>Lists the tags. If no tag is matched, an empty array is returned.</p>
    </td>
    </tr>
    <tr id="row20771114063119"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p677111406315"><a name="p677111406315"></a><a name="p677111406315"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.52265226522652%" headers="mcps1.2.4.1.2 "><p id="p117711040153116"><a name="p117711040153116"></a><a name="p117711040153116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.47484748474848%" headers="mcps1.2.4.1.3 "><p id="p8772040133115"><a name="p8772040133115"></a><a name="p8772040133115"></a>Specifies the resource name. If the resource does not have a name, the ID is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  Data structure of the  **resource\_tag**  field

    <a name="table1539174012316"></a>
    <table><thead align="left"><tr id="row6772144083117"><th class="cellrowborder" valign="top" width="25.002500250025%" id="mcps1.2.4.1.1"><p id="p1577254043110"><a name="p1577254043110"></a><a name="p1577254043110"></a><strong id="b189571119201015"><a name="b189571119201015"></a><a name="b189571119201015"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.632663266326627%" id="mcps1.2.4.1.2"><p id="p14772174053115"><a name="p14772174053115"></a><a name="p14772174053115"></a><strong id="b27415218103"><a name="b27415218103"></a><a name="b27415218103"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.36483648364836%" id="mcps1.2.4.1.3"><p id="p15772154017315"><a name="p15772154017315"></a><a name="p15772154017315"></a><strong id="b19521222161010"><a name="b19521222161010"></a><a name="b19521222161010"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row877274073120"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p0772104011311"><a name="p0772104011311"></a><a name="p0772104011311"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.632663266326627%" headers="mcps1.2.4.1.2 "><p id="p877274012313"><a name="p877274012313"></a><a name="p877274012313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.4.1.3 "><p id="p07721340103117"><a name="p07721340103117"></a><a name="p07721340103117"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row177214013110"><td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.4.1.1 "><p id="p13772184016314"><a name="p13772184016314"></a><a name="p13772184016314"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.632663266326627%" headers="mcps1.2.4.1.2 "><p id="p157729401319"><a name="p157729401319"></a><a name="p157729401319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.4.1.3 "><p id="p17772340163114"><a name="p17772340163114"></a><a name="p17772340163114"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response
    -   Response body when  **action**  is set to  **filter**

        ```
        {
            "resources": [
                {
                    "resource_detail": null,
                    "resource_id": "cdfs_cefs_wesas_12_dsad",
                    "resource_name": "resouece1",
                    "tags": [
                        {
                            "key": "key1","value": "value1"
                        },
                        {
                            "key": "key2","value": "value1"
                        }
                    ]
                }
            ],
            "total_count": 1000
        }
        ```

    -   Response body when  **action**  is set to  **count**

        ```
        {
            "total_count": 1000
        }
        ```



## Status Code<a name="section7398640123111"></a>

For details about status codes, see  [Status Code](status-code.md).

