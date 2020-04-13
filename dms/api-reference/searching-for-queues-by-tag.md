# Searching for Queues by Tag<a name="EN-US_TOPIC_0128036923"></a>

## Function<a name="section148619235516"></a>

This API is used to search for queues by tag.

## URI<a name="section84879218554"></a>

POST /v1.0/\{project\_id\}/queue/resource\_instances/action

**Table  1**  Request header

<a name="table14901626550"></a>
<table><thead align="left"><tr id="row4310325515"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p1231831551"><a name="p1231831551"></a><a name="p1231831551"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p7312319553"><a name="p7312319553"></a><a name="p7312319553"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p8311834552"><a name="p8311834552"></a><a name="p8311834552"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p23117365511"><a name="p23117365511"></a><a name="p23117365511"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row5317365518"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p7311338552"><a name="p7311338552"></a><a name="p7311338552"></a>Content-type</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p113113335519"><a name="p113113335519"></a><a name="p113113335519"></a>Indicates the MIME types of a request body.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p23114345520"><a name="p23114345520"></a><a name="p23114345520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p23163125520"><a name="p23163125520"></a><a name="p23163125520"></a>application/json</p>
</td>
</tr>
<tr id="row83114395511"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p113118315553"><a name="p113118315553"></a><a name="p113118315553"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p1931732558"><a name="p1931732558"></a><a name="p1931732558"></a>Indicates the user token.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p4311336555"><a name="p4311336555"></a><a name="p4311336555"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p731134551"><a name="p731134551"></a><a name="p731134551"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameters

<a name="table3501132135517"></a>
<table><thead align="left"><tr id="row1631332553"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p11310395513"><a name="p11310395513"></a><a name="p11310395513"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p103353145511"><a name="p103353145511"></a><a name="p103353145511"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p16339305518"><a name="p16339305518"></a><a name="p16339305518"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p83312316551"><a name="p83312316551"></a><a name="p83312316551"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row533835557"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1833113155518"><a name="p1833113155518"></a><a name="p1833113155518"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1332375516"><a name="p1332375516"></a><a name="p1332375516"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11331437559"><a name="p11331437559"></a><a name="p11331437559"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p63310319558"><a name="p63310319558"></a><a name="p63310319558"></a>Indicates the ID of a project.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
 /v1.0/67c01b92944144a19d2da968ef34a912/queue/resource_instances/action
```

## Request<a name="section65121729554"></a>

**Table  3**  Request parameters

<a name="table65521428555"></a>
<table><thead align="left"><tr id="row83411365510"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p534630553"><a name="p534630553"></a><a name="p534630553"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p15348365512"><a name="p15348365512"></a><a name="p15348365512"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p8341313559"><a name="p8341313559"></a><a name="p8341313559"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.52525252525253%" id="mcps1.2.5.1.4"><p id="p1534193145515"><a name="p1534193145515"></a><a name="p1534193145515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2345365513"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p12342317557"><a name="p12342317557"></a><a name="p12342317557"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p153418395519"><a name="p153418395519"></a><a name="p153418395519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p2341332554"><a name="p2341332554"></a><a name="p2341332554"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p919913521029"><a name="p919913521029"></a><a name="p919913521029"></a>Indicates a tag list in which all tags are matched.</p>
<p id="p32711510516"><a name="p32711510516"></a><a name="p32711510516"></a>A maximum of 10 tag keys can be specified for each search operation. The tag key cannot be left blank or set to an empty string. Each tag key can have a maximum of 10 values.</p>
<p id="p113411317554"><a name="p113411317554"></a><a name="p113411317554"></a>Each tag key and each value of a tag key must be unique.</p>
</td>
</tr>
<tr id="row234193125514"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p634133115520"><a name="p634133115520"></a><a name="p634133115520"></a>tags_any</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p193418311553"><a name="p193418311553"></a><a name="p193418311553"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p2291835829"><a name="p2291835829"></a><a name="p2291835829"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p1254562512518"><a name="p1254562512518"></a><a name="p1254562512518"></a>Indicates a tag list in which any tag is matched.</p>
<p id="p952815411653"><a name="p952815411653"></a><a name="p952815411653"></a>A maximum of 10 tag keys can be specified for each search operation. The tag key cannot be left blank or set to an empty string. Each tag key can have a maximum of 10 values.</p>
<p id="p12351633552"><a name="p12351633552"></a><a name="p12351633552"></a>Each tag key and each value of a tag key must be unique.</p>
</td>
</tr>
<tr id="row3354335514"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p135434553"><a name="p135434553"></a><a name="p135434553"></a>not_tags</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p53513105520"><a name="p53513105520"></a><a name="p53513105520"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p947013384219"><a name="p947013384219"></a><a name="p947013384219"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p173978111568"><a name="p173978111568"></a><a name="p173978111568"></a>Indicates a tag list in which no tags are matched.</p>
<p id="p4942192419619"><a name="p4942192419619"></a><a name="p4942192419619"></a>A maximum of 10 tag keys can be specified for each search operation. The tag key cannot be left blank or set to an empty string. Each tag key can have a maximum of 10 values.</p>
<p id="p1135139558"><a name="p1135139558"></a><a name="p1135139558"></a>Each tag key and each value of a tag key must be unique.</p>
</td>
</tr>
<tr id="row3359305513"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1235937559"><a name="p1235937559"></a><a name="p1235937559"></a>not_tags_any</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p123515335514"><a name="p123515335514"></a><a name="p123515335514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p1074964011210"><a name="p1074964011210"></a><a name="p1074964011210"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p910153711613"><a name="p910153711613"></a><a name="p910153711613"></a>Indicates a tag list in which any tag is not matched.</p>
<p id="p835103205512"><a name="p835103205512"></a><a name="p835103205512"></a>A maximum of 10 tag keys are allowed in each search operation. The tag key cannot be left blank or set to an empty string. The structure is required. Each tag key can have a maximum of 10 values. Each tag key and each value of a tag key must be unique.</p>
</td>
</tr>
<tr id="row1871313471084"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p33819315554"><a name="p33819315554"></a><a name="p33819315554"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p1938163115514"><a name="p1938163115514"></a><a name="p1938163115514"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p2381313551"><a name="p2381313551"></a><a name="p2381313551"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p127701312996"><a name="p127701312996"></a><a name="p127701312996"></a>Indicates an operation.</p>
<p id="p83883145515"><a name="p83883145515"></a><a name="p83883145515"></a><strong id="b7875150142714"><a name="b7875150142714"></a><a name="b7875150142714"></a>count</strong>: queries only the total number of queues.</p>
<p id="p205243918109"><a name="p205243918109"></a><a name="p205243918109"></a><strong id="b1571916752715"><a name="b1571916752715"></a><a name="b1571916752715"></a>filter</strong>: queries the details about queues and tags.</p>
<p id="p938635559"><a name="p938635559"></a><a name="p938635559"></a>When this parameter is set to <strong id="b1043714215273"><a name="b1043714215273"></a><a name="b1043714215273"></a>filter</strong>, a search is performed by page. When this parameter is set to <strong id="b139211021162711"><a name="b139211021162711"></a><a name="b139211021162711"></a>count</strong>, only the total number of queues is returned based on the search criteria.</p>
</td>
</tr>
<tr id="row4351138551"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p17351737558"><a name="p17351737558"></a><a name="p17351737558"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p33513318551"><a name="p33513318551"></a><a name="p33513318551"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p133516315551"><a name="p133516315551"></a><a name="p133516315551"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p1420580201211"><a name="p1420580201211"></a><a name="p1420580201211"></a>This parameter is valid only when <strong id="b20249143612717"><a name="b20249143612717"></a><a name="b20249143612717"></a>action</strong> is set to <strong id="b19186143182716"><a name="b19186143182716"></a><a name="b19186143182716"></a>filter</strong>.</p>
<p id="p153332717129"><a name="p153332717129"></a><a name="p153332717129"></a>This parameter indicates the number of matches in a single search operation.</p>
<p id="p97831319139"><a name="p97831319139"></a><a name="p97831319139"></a>Default value: <strong id="b182969102814"><a name="b182969102814"></a><a name="b182969102814"></a>1000</strong></p>
<p id="p65911543127"><a name="p65911543127"></a><a name="p65911543127"></a>Value range: 1–1000.</p>
</td>
</tr>
<tr id="row8351638559"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p03519345520"><a name="p03519345520"></a><a name="p03519345520"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p183515355520"><a name="p183515355520"></a><a name="p183515355520"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p10358314554"><a name="p10358314554"></a><a name="p10358314554"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p172311629151313"><a name="p172311629151313"></a><a name="p172311629151313"></a>This parameter is valid only when <strong id="b1851427192816"><a name="b1851427192816"></a><a name="b1851427192816"></a>action</strong> is set to <strong id="b915518992815"><a name="b915518992815"></a><a name="b915518992815"></a>filter</strong>.</p>
<p id="p113115115149"><a name="p113115115149"></a><a name="p113115115149"></a>This parameter indicates the index position. The search starts from the next data record of the specified offset position.</p>
<p id="p34802269144"><a name="p34802269144"></a><a name="p34802269144"></a>This parameter is not required when data on the first page is queried.</p>
<p id="p83516313559"><a name="p83516313559"></a><a name="p83516313559"></a>Default value: <strong id="b059754111278"><a name="b059754111278"></a><a name="b059754111278"></a>0</strong></p>
<p id="p158718912174"><a name="p158718912174"></a><a name="p158718912174"></a>Value range: an integer that is greater than or equals to zero</p>
</td>
</tr>
<tr id="row183819335518"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p638835552"><a name="p638835552"></a><a name="p638835552"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p14388314558"><a name="p14388314558"></a><a name="p14388314558"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p11381436557"><a name="p11381436557"></a><a name="p11381436557"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p238163185510"><a name="p238163185510"></a><a name="p238163185510"></a>Indicates a search criterion for fuzzy queue name match.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  tags parameter description

<a name="table86223211555"></a>
<table><thead align="left"><tr id="row23910312557"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p639103145511"><a name="p639103145511"></a><a name="p639103145511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.2"><p id="p123993165514"><a name="p123993165514"></a><a name="p123993165514"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.3"><p id="p6391733555"><a name="p6391733555"></a><a name="p6391733555"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.5.1.4"><p id="p20399317551"><a name="p20399317551"></a><a name="p20399317551"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5391639552"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p839238558"><a name="p839238558"></a><a name="p839238558"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p13916319559"><a name="p13916319559"></a><a name="p13916319559"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.3 "><p id="p1139931553"><a name="p1139931553"></a><a name="p1139931553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="p4421165211222"><a name="p4421165211222"></a><a name="p4421165211222"></a>Indicates the tag key, which can contain a maximum of 127 Unicode characters </p>
<p id="p1239193195510"><a name="p1239193195510"></a><a name="p1239193195510"></a>and cannot be left blank.</p>
</td>
</tr>
<tr id="row1839123115517"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p16394313556"><a name="p16394313556"></a><a name="p16394313556"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p43919313557"><a name="p43919313557"></a><a name="p43919313557"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.3 "><p id="p133916318554"><a name="p133916318554"></a><a name="p133916318554"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="p83918316554"><a name="p83918316554"></a><a name="p83918316554"></a>Indicates a list of tag values. A tag value can contain a maximum of 255 Unicode characters.</p>
<p id="p18219145692318"><a name="p18219145692318"></a><a name="p18219145692318"></a>If the value of this parameter is null, it indicates all the values.</p>
<p id="p1739739552"><a name="p1739739552"></a><a name="p1739739552"></a>All values of a tag key are in the OR relationship.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  matches parameter description

<a name="table1464042125517"></a>
<table><thead align="left"><tr id="row1741163175510"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p134163205518"><a name="p134163205518"></a><a name="p134163205518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p19418355517"><a name="p19418355517"></a><a name="p19418355517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p134111316559"><a name="p134111316559"></a><a name="p134111316559"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p7412335515"><a name="p7412335515"></a><a name="p7412335515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9417310556"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p3419335510"><a name="p3419335510"></a><a name="p3419335510"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p16416355511"><a name="p16416355511"></a><a name="p16416355511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p12419316556"><a name="p12419316556"></a><a name="p12419316556"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p1641183125520"><a name="p1641183125520"></a><a name="p1641183125520"></a>It must be <strong id="b246793152711"><a name="b246793152711"></a><a name="b246793152711"></a>resource_name</strong>.</p>
</td>
</tr>
<tr id="row114113320558"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p114143105511"><a name="p114143105511"></a><a name="p114143105511"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p17411033552"><a name="p17411033552"></a><a name="p17411033552"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p114114325512"><a name="p114114325512"></a><a name="p114114325512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p124103155518"><a name="p124103155518"></a><a name="p124103155518"></a>Indicates a queue name for fuzzy match. The value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

When  **action**  is set to  **filter**:

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
    "not_tags": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
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

When  **action**  is set to  **count**:

```
{
  "action": "count", 
  "not_tags": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
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
"matches":[
{
        "key": "resource_name", 
        "value": "resource1"
       }
]
}
```

## Response<a name="section49332166"></a>

**Response parameters**

**Table  6**  Response parameters

<a name="table16816155318325"></a>
<table><thead align="left"><tr id="row178251653133217"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p138305533321"><a name="p138305533321"></a><a name="p138305533321"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p183885315321"><a name="p183885315321"></a><a name="p183885315321"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p10845153203217"><a name="p10845153203217"></a><a name="p10845153203217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row884919531321"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p15851185313324"><a name="p15851185313324"></a><a name="p15851185313324"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p10857185316322"><a name="p10857185316322"></a><a name="p10857185316322"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14523133712375"><a name="p14523133712375"></a><a name="p14523133712375"></a>Indicates the queue list.</p>
<p id="p186225343215"><a name="p186225343215"></a><a name="p186225343215"></a>By default, both resources and resource tags are sorted by the time when they are created.</p>
</td>
</tr>
<tr id="row686475314320"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p6868105383217"><a name="p6868105383217"></a><a name="p6868105383217"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p5873155343217"><a name="p5873155343217"></a><a name="p5873155343217"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14876145333217"><a name="p14876145333217"></a><a name="p14876145333217"></a>Indicates the total number of records.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  resources parameter description

<a name="table076015673315"></a>
<table><thead align="left"><tr id="row97721765335"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p14775116163316"><a name="p14775116163316"></a><a name="p14775116163316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p107811665334"><a name="p107811665334"></a><a name="p107811665334"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p137856616333"><a name="p137856616333"></a><a name="p137856616333"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9787126173318"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1779017693319"><a name="p1779017693319"></a><a name="p1779017693319"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p108007612338"><a name="p108007612338"></a><a name="p108007612338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p178041067339"><a name="p178041067339"></a><a name="p178041067339"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row1980514612333"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p580912617336"><a name="p580912617336"></a><a name="p580912617336"></a>resouce_detail</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p7815106183314"><a name="p7815106183314"></a><a name="p7815106183314"></a>JSON object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p4564726193817"><a name="p4564726193817"></a><a name="p4564726193817"></a>Indicates resource details.</p>
</td>
</tr>
<tr id="row1482256163314"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p12825136173316"><a name="p12825136173316"></a><a name="p12825136173316"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1379271733517"><a name="p1379271733517"></a><a name="p1379271733517"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1683411623312"><a name="p1683411623312"></a><a name="p1683411623312"></a>Indicates a tag list. This parameter is an empty array by default if there is no tag.</p>
<p id="p1922233283718"><a name="p1922233283718"></a><a name="p1922233283718"></a>Resource tags are sorted by the time when they are created.</p>
</td>
</tr>
<tr id="row1283706183316"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p148391463336"><a name="p148391463336"></a><a name="p148391463336"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1084510623316"><a name="p1084510623316"></a><a name="p1084510623316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p128481764337"><a name="p128481764337"></a><a name="p128481764337"></a>Indicates the resource name. This parameter is an empty string by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  tags parameter description

<a name="table781012172338"></a>
<table><thead align="left"><tr id="row16820111712337"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p1782411178335"><a name="p1782411178335"></a><a name="p1782411178335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p4834141703319"><a name="p4834141703319"></a><a name="p4834141703319"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p083911172331"><a name="p083911172331"></a><a name="p083911172331"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19846121718333"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p7850171710334"><a name="p7850171710334"></a><a name="p7850171710334"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p12860201763314"><a name="p12860201763314"></a><a name="p12860201763314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p158631317153311"><a name="p158631317153311"></a><a name="p158631317153311"></a>Indicates the tag key, which can contain a maximum of 36 Unicode characters. It cannot be left blank, and cannot be left blank, and cannot contain nonprintable ASCII (0–31) characters and the following special characters: *&lt;&gt;\=</p>
</td>
</tr>
<tr id="row5865151719336"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p38679179334"><a name="p38679179334"></a><a name="p38679179334"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p387471719338"><a name="p387471719338"></a><a name="p387471719338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p19878141716336"><a name="p19878141716336"></a><a name="p19878141716336"></a>Indicates a tag value. A tag value can contain a maximum of 43 Unicode characters. It can be an empty string, but cannot contain the following characters: ASCII (0-31), equal signs (=), asterisks (*), left angle brackets (&lt;), right angle brackets (&gt;), backslashes (\), commas (,), vertical bars (|), and slashes (/).</p>
</td>
</tr>
</tbody>
</table>

**Example response**

When  **action**  is set to  **filter**:

```
    { 
      "resources": [
         {
            "resource_detail": null, 
            "resource_id": "cdfs_cefs_wesas_12_dsad", 
            "resource_name": "resouece1", 
            "tags": [
                {
                   "key": "key1",
                   "value": "value1"
                },
                {
                   "key": "key2",
                   "value": "value1"
                }
             ]
         }
       ], 
      "total_count": 1000
}
```

When  **action**  is set to  **count**:

```
{
    "total_count": 1000
}
```

## Status Code<a name="section971218211556"></a>

<a name="table1716124551"></a>
<table><thead align="left"><tr id="row175283105516"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1452123165511"><a name="p1452123165511"></a><a name="p1452123165511"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p16521831552"><a name="p16521831552"></a><a name="p16521831552"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1796019554285"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1764051102915"><a name="p1764051102915"></a><a name="p1764051102915"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p166402172915"><a name="p166402172915"></a><a name="p166402172915"></a>OK</p>
</td>
</tr>
<tr id="row11521339553"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p175210345518"><a name="p175210345518"></a><a name="p175210345518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p195215325514"><a name="p195215325514"></a><a name="p195215325514"></a>Invalid parameter.</p>
</td>
</tr>
<tr id="row18523318555"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p35243165513"><a name="p35243165513"></a><a name="p35243165513"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p65253165515"><a name="p65253165515"></a><a name="p65253165515"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row125215318558"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p85214375512"><a name="p85214375512"></a><a name="p85214375512"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p16529305517"><a name="p16529305517"></a><a name="p16529305517"></a>Insufficient permission.</p>
</td>
</tr>
<tr id="row1652632559"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p155214325517"><a name="p155214325517"></a><a name="p155214325517"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15210385515"><a name="p15210385515"></a><a name="p15210385515"></a>No queue found.</p>
</td>
</tr>
<tr id="row852183165519"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13521531554"><a name="p13521531554"></a><a name="p13521531554"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1529385514"><a name="p1529385514"></a><a name="p1529385514"></a>System error.</p>
</td>
</tr>
</tbody>
</table>

