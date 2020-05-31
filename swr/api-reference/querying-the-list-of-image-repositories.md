# Querying the List of Image Repositories<a name="EN-US_TOPIC_0198655153"></a>

## Function<a name="section14905762191056"></a>

Query the list of image repositories.

## URI<a name="section10482810165331"></a>

GET /v2/manage/repos?namespace=\{namespace\}&limit=\{limit\}&offset=\{offset\}&order\_column=\{order\_column\}&order\_type=\{order\_type\}

For details about parameters, see  [Table 1](#table11843162810214).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>GET /v2/manage/repos can be used to query all existing image repositories of all organizations.  

**Table  1**  Parameter description

<a name="table11843162810214"></a>
<table><thead align="left"><tr id="row20843172818213"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.1"><p id="p3843528621"><a name="p3843528621"></a><a name="p3843528621"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="20.830000000000002%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.82%" id="mcps1.2.5.1.4"><p id="p1584342811211"><a name="p1584342811211"></a><a name="p1584342811211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1084316281925"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p105058419438"><a name="p105058419438"></a><a name="p105058419438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p1142354513446"><a name="p1142354513446"></a><a name="p1142354513446"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p85037015469"><a name="p85037015469"></a><a name="p85037015469"></a>Organization name.</p>
</td>
</tr>
<tr id="row1319321944420"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p919315194441"><a name="p919315194441"></a><a name="p919315194441"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p9476122315105"><a name="p9476122315105"></a><a name="p9476122315105"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p13821184619446"><a name="p13821184619446"></a><a name="p13821184619446"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p13193201924411"><a name="p13193201924411"></a><a name="p13193201924411"></a>Image repository name.</p>
</td>
</tr>
<tr id="row50101825810"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p5001885812"><a name="p5001885812"></a><a name="p5001885812"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p447652371015"><a name="p447652371015"></a><a name="p447652371015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p549519442"><a name="p549519442"></a><a name="p549519442"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p70018135816"><a name="p70018135816"></a><a name="p70018135816"></a>Image repository category.</p>
</td>
</tr>
<tr id="row330110147461"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p130116149463"><a name="p130116149463"></a><a name="p130116149463"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p4476172381010"><a name="p4476172381010"></a><a name="p4476172381010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p14120512445"><a name="p14120512445"></a><a name="p14120512445"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p18972162624613"><a name="p18972162624613"></a><a name="p18972162624613"></a>Start index. Parameters <strong id="b165971487012"><a name="b165971487012"></a><a name="b165971487012"></a>offset</strong> and <strong id="b167681017905"><a name="b167681017905"></a><a name="b167681017905"></a>limit</strong> should always be used together.</p>
<p id="p8527601134"><a name="p8527601134"></a><a name="p8527601134"></a>The value is greater than or equal to 0.</p>
</td>
</tr>
<tr id="row1134483415461"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p13446343467"><a name="p13446343467"></a><a name="p13446343467"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p047682316102"><a name="p047682316102"></a><a name="p047682316102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p17223511447"><a name="p17223511447"></a><a name="p17223511447"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p5344173413460"><a name="p5344173413460"></a><a name="p5344173413460"></a>Number of returned records. Parameters <strong id="b66493111747"><a name="b66493111747"></a><a name="b66493111747"></a>offset</strong> and <strong id="b9661121116411"><a name="b9661121116411"></a><a name="b9661121116411"></a>limit</strong> should always be used together.</p>
<p id="p66072441311"><a name="p66072441311"></a><a name="p66072441311"></a>The value is greater than or equal to 0.</p>
</td>
</tr>
<tr id="row193902371288"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p17470141274715"><a name="p17470141274715"></a><a name="p17470141274715"></a>order_column</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p7391037088"><a name="p7391037088"></a><a name="p7391037088"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p83911137980"><a name="p83911137980"></a><a name="p83911137980"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p1847081212472"><a name="p1847081212472"></a><a name="p1847081212472"></a>Sorting by column. You can set this parameter to <strong id="b19235114715426"><a name="b19235114715426"></a><a name="b19235114715426"></a>name</strong>, <strong id="b1344749144220"><a name="b1344749144220"></a><a name="b1344749144220"></a>updated_time</strong>, and <strong id="b193123537429"><a name="b193123537429"></a><a name="b193123537429"></a>tag_count</strong>. The parameters <strong id="b133250715437"><a name="b133250715437"></a><a name="b133250715437"></a>order_column</strong> and <strong id="b95390916433"><a name="b95390916433"></a><a name="b95390916433"></a>order_type</strong> should always be used together.</p>
</td>
</tr>
<tr id="row1395919342812"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.1 "><p id="p1547061274718"><a name="p1547061274718"></a><a name="p1547061274718"></a>order_type</p>
</td>
<td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.5.1.2 "><p id="p14960734487"><a name="p14960734487"></a><a name="p14960734487"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.2.5.1.3 "><p id="p9960134988"><a name="p9960134988"></a><a name="p9960134988"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.82%" headers="mcps1.2.5.1.4 "><p id="p12470131294710"><a name="p12470131294710"></a><a name="p12470131294710"></a>Sorting type. You can set this parameter to <strong id="b11280182362417"><a name="b11280182362417"></a><a name="b11280182362417"></a>desc</strong> (descending sort) and <strong id="b1395172516244"><a name="b1395172516244"></a><a name="b1395172516244"></a>asc</strong> (ascending sort).</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

N/A

## Response<a name="section46271297104114"></a>

**Response parameters**

**Table  2**  Response header parameter description

<a name="table156464193424"></a>
<table><thead align="left"><tr id="row76531819144218"><th class="cellrowborder" valign="top" width="20.51%" id="mcps1.2.4.1.1"><p id="p36531719164213"><a name="p36531719164213"></a><a name="p36531719164213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.690000000000001%" id="mcps1.2.4.1.2"><p id="p186572196429"><a name="p186572196429"></a><a name="p186572196429"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63.800000000000004%" id="mcps1.2.4.1.3"><p id="p1966121915428"><a name="p1966121915428"></a><a name="p1966121915428"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18663141934215"><td class="cellrowborder" valign="top" width="20.51%" headers="mcps1.2.4.1.1 "><p id="p15664201917425"><a name="p15664201917425"></a><a name="p15664201917425"></a>Content-Range</p>
</td>
<td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.2.4.1.2 "><p id="p1566851954211"><a name="p1566851954211"></a><a name="p1566851954211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p442485393619"><a name="p442485393619"></a><a name="p442485393619"></a>Offset (Start index)–Count (Number of records on the current page)/Total (Total number of records)</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>When a request passes parameter  **offset**  and  **limit**,  **Content-Range**  will be added in the response header.  

**Table  3**  Response body parameter description

<a name="table45446245174724"></a>
<table><thead align="left"><tr id="row1412623174724"><th class="cellrowborder" valign="top" width="21.42214221422142%" id="mcps1.2.4.1.1"><p id="p47313663174724"><a name="p47313663174724"></a><a name="p47313663174724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.21182118211821%" id="mcps1.2.4.1.2"><p id="p7201512174724"><a name="p7201512174724"></a><a name="p7201512174724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.36603660366037%" id="mcps1.2.4.1.3"><p id="p4480706174724"><a name="p4480706174724"></a><a name="p4480706174724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40294727101415"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p42647463101415"><a name="p42647463101415"></a><a name="p42647463101415"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p19826194217101"><a name="p19826194217101"></a><a name="p19826194217101"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p988225101415"><a name="p988225101415"></a><a name="p988225101415"></a>Repository name.</p>
</td>
</tr>
<tr id="row98876365819"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p1624210616586"><a name="p1624210616586"></a><a name="p1624210616586"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p4826942191017"><a name="p4826942191017"></a><a name="p4826942191017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p6245963583"><a name="p6245963583"></a><a name="p6245963583"></a>Repository type.</p>
</td>
</tr>
<tr id="row1698135244113"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p5996521415"><a name="p5996521415"></a><a name="p5996521415"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p17827174217108"><a name="p17827174217108"></a><a name="p17827174217108"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p799165219417"><a name="p799165219417"></a><a name="p799165219417"></a>Repository description.</p>
</td>
</tr>
<tr id="row626682835815"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p1126642811589"><a name="p1126642811589"></a><a name="p1126642811589"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p1582784241016"><a name="p1582784241016"></a><a name="p1582784241016"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p2266162865816"><a name="p2266162865816"></a><a name="p2266162865816"></a>Image repository size.</p>
</td>
</tr>
<tr id="row1286171411597"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p54433257594"><a name="p54433257594"></a><a name="p54433257594"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p1882794261013"><a name="p1882794261013"></a><a name="p1882794261013"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p944519257591"><a name="p944519257591"></a><a name="p944519257591"></a>Whether the image is public. When the value is <strong id="b08248301369"><a name="b08248301369"></a><a name="b08248301369"></a>true</strong>, it indicates the image is public. When the value is <strong id="b1808121485116"><a name="b1808121485116"></a><a name="b1808121485116"></a>false</strong>, it indicates the image is private.</p>
</td>
</tr>
<tr id="row38403527599"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p1984085216595"><a name="p1984085216595"></a><a name="p1984085216595"></a>num_images</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p11377144981012"><a name="p11377144981012"></a><a name="p11377144981012"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p17840175285913"><a name="p17840175285913"></a><a name="p17840175285913"></a>Number of image tags in a repository.</p>
</td>
</tr>
<tr id="row15637848145911"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p166384486595"><a name="p166384486595"></a><a name="p166384486595"></a>num_download</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p537794991019"><a name="p537794991019"></a><a name="p537794991019"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p763834825915"><a name="p763834825915"></a><a name="p763834825915"></a>Download times.</p>
</td>
</tr>
<tr id="row65154041101837"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p42985951101837"><a name="p42985951101837"></a><a name="p42985951101837"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p153785494103"><a name="p153785494103"></a><a name="p153785494103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p35094394113433"><a name="p35094394113433"></a><a name="p35094394113433"></a>Time when a repository is created, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row57344470102311"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p14390475102311"><a name="p14390475102311"></a><a name="p14390475102311"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p6378174921013"><a name="p6378174921013"></a><a name="p6378174921013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p29749998102311"><a name="p29749998102311"></a><a name="p29749998102311"></a>Time when a repository is updated, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row1877408195412"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p67751489548"><a name="p67751489548"></a><a name="p67751489548"></a>logo</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p193782049191010"><a name="p193782049191010"></a><a name="p193782049191010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p157751685549"><a name="p157751685549"></a><a name="p157751685549"></a>Repository logo (reserved).</p>
</td>
</tr>
<tr id="row1037174225"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p173714629"><a name="p173714629"></a><a name="p173714629"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p1524565791013"><a name="p1524565791013"></a><a name="p1524565791013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p15371642213"><a name="p15371642213"></a><a name="p15371642213"></a>URL of the repository logo (reserved).</p>
</td>
</tr>
<tr id="row1952451421"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p195242115212"><a name="p195242115212"></a><a name="p195242115212"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p124575721020"><a name="p124575721020"></a><a name="p124575721020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p1752461723"><a name="p1752461723"></a><a name="p1752461723"></a>Image address for docker pull.</p>
</td>
</tr>
<tr id="row6684191311448"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p176851313124412"><a name="p176851313124412"></a><a name="p176851313124412"></a>internal_path</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p1124565711102"><a name="p1124565711102"></a><a name="p1124565711102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p1268512134443"><a name="p1268512134443"></a><a name="p1268512134443"></a>Intra-cluster image address for docker pull.</p>
</td>
</tr>
<tr id="row552719404114"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p15110411915"><a name="p15110411915"></a><a name="p15110411915"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p11245185771012"><a name="p11245185771012"></a><a name="p11245185771012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p6514184115111"><a name="p6514184115111"></a><a name="p6514184115111"></a>Username.</p>
</td>
</tr>
<tr id="row1690219211219"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p114951323118"><a name="p114951323118"></a><a name="p114951323118"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p1324555712100"><a name="p1324555712100"></a><a name="p1324555712100"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p174981723714"><a name="p174981723714"></a><a name="p174981723714"></a>Organization name.</p>
</td>
</tr>
<tr id="row6523217145617"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p3525817135615"><a name="p3525817135615"></a><a name="p3525817135615"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p12246195719109"><a name="p12246195719109"></a><a name="p12246195719109"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p13494291588"><a name="p13494291588"></a><a name="p13494291588"></a>Image tag list.</p>
</td>
</tr>
<tr id="row1715815815558"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p141581358115514"><a name="p141581358115514"></a><a name="p141581358115514"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p16246185761017"><a name="p16246185761017"></a><a name="p16246185761017"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p171587588558"><a name="p171587588558"></a><a name="p171587588558"></a>Status (reserved).</p>
</td>
</tr>
<tr id="row183529195181"><td class="cellrowborder" valign="top" width="21.42214221422142%" headers="mcps1.2.4.1.1 "><p id="p1327583410124"><a name="p1327583410124"></a><a name="p1327583410124"></a>total_range</p>
</td>
<td class="cellrowborder" valign="top" width="18.21182118211821%" headers="mcps1.2.4.1.2 "><p id="p1727583451216"><a name="p1727583451216"></a><a name="p1727583451216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.36603660366037%" headers="mcps1.2.4.1.3 "><p id="p727517346122"><a name="p727517346122"></a><a name="p727517346122"></a>Total number of repositories.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
[
    {
        "name": "nginx",
        "category": "linux",
        "size": 200977474,
        "is_public": false,
        "num_images": 2,
        "num_download": 0,
        "created_at": "2017-01-01T00:00:00Z",
        "updated_at": "2017-09-11T03:00:02.542841141Z",
        "logo": "",
        "url": "",
        "path": "192.158.24.86/namespace/repository",
        "internal_path": "10.125.0.198:20202/namespace/repository",
        "domain_name": "root",
        "namespace": "root",
        "tags": [
            "latest",
            "log"
        ],
        "status": false
        "total_range": 1
    }
]
```

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 4](#table1327183872417).

**Table  4**  Status code

<a name="table1327183872417"></a>
<table><thead align="left"><tr id="row127115381244"><th class="cellrowborder" valign="top" width="27.150000000000002%" id="mcps1.2.3.1.1"><p id="p2027103812240"><a name="p2027103812240"></a><a name="p2027103812240"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="72.85000000000001%" id="mcps1.2.3.1.2"><p id="p8271638162420"><a name="p8271638162420"></a><a name="p8271638162420"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13271143832414"><td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.2.3.1.1 "><p id="p52711438162416"><a name="p52711438162416"></a><a name="p52711438162416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="72.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p16271143817245"><a name="p16271143817245"></a><a name="p16271143817245"></a>Request sent successfully.</p>
</td>
</tr>
<tr id="row527119386242"><td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.2.3.1.1 "><p id="p927263882412"><a name="p927263882412"></a><a name="p927263882412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="72.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p7272738132420"><a name="p7272738132420"></a><a name="p7272738132420"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row10272123812412"><td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.2.3.1.1 "><p id="p22721838162418"><a name="p22721838162418"></a><a name="p22721838162418"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="72.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p32721383247"><a name="p32721383247"></a><a name="p32721383247"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row1827243852412"><td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.2.3.1.1 "><p id="p12272153822415"><a name="p12272153822415"></a><a name="p12272153822415"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="72.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p327203862414"><a name="p327203862414"></a><a name="p327203862414"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

