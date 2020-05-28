# Querying the List of Shared Images<a name="EN-US_TOPIC_0198655141"></a>

## Function<a name="section563520319418"></a>

Query the list of images shared by you and the list of images shared with you by others.

## URI<a name="section84235172429"></a>

GET /v2/manage/shared-repositories?center=\{center\}&name=\{name\}&limit=\{limit\}&offset=\{offset\}

For details about parameters, see  [Table 1](#table591824984318).

**Table  1**  Parameter description

<a name="table591824984318"></a>
<table><thead align="left"><tr id="row1997534904312"><th class="cellrowborder" valign="top" width="17.18%" id="mcps1.2.5.1.1"><p id="p14975114984317"><a name="p14975114984317"></a><a name="p14975114984317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.4%" id="mcps1.2.5.1.2"><p id="p4845145816388"><a name="p4845145816388"></a><a name="p4845145816388"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.09%" id="mcps1.2.5.1.3"><p id="p997713492436"><a name="p997713492436"></a><a name="p997713492436"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.33%" id="mcps1.2.5.1.4"><p id="p9977144910431"><a name="p9977144910431"></a><a name="p9977144910431"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20919850124820"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.5.1.1 "><p id="p890218517481"><a name="p890218517481"></a><a name="p890218517481"></a>center</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.2 "><p id="p1690235112481"><a name="p1690235112481"></a><a name="p1690235112481"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.3 "><p id="p190211510487"><a name="p190211510487"></a><a name="p190211510487"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.2.5.1.4 "><p id="p290215518485"><a name="p290215518485"></a><a name="p290215518485"></a><strong id="b1490225117484"><a name="b1490225117484"></a><a name="b1490225117484"></a>self</strong>: images shared by you</p>
<p id="p169021251144815"><a name="p169021251144815"></a><a name="p169021251144815"></a><strong id="b2902195104811"><a name="b2902195104811"></a><a name="b2902195104811"></a>thirdparty</strong>: images shared with you by others</p>
</td>
</tr>
<tr id="row13901011165316"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.5.1.1 "><p id="p139779499438"><a name="p139779499438"></a><a name="p139779499438"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.2 "><p id="p20980132718193"><a name="p20980132718193"></a><a name="p20980132718193"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.3 "><p id="p18977449104318"><a name="p18977449104318"></a><a name="p18977449104318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.2.5.1.4 "><p id="p1197784915436"><a name="p1197784915436"></a><a name="p1197784915436"></a>Image repository name.</p>
</td>
</tr>
<tr id="row1297710495438"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.5.1.1 "><p id="p1992562395311"><a name="p1992562395311"></a><a name="p1992562395311"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.2 "><p id="p360215315712"><a name="p360215315712"></a><a name="p360215315712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.3 "><p id="p16101155163513"><a name="p16101155163513"></a><a name="p16101155163513"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.2.5.1.4 "><p id="p14899423155320"><a name="p14899423155320"></a><a name="p14899423155320"></a>Number of returned records Parameters <strong id="b16732222124317"><a name="b16732222124317"></a><a name="b16732222124317"></a>offset</strong> and <strong id="b1574542215438"><a name="b1574542215438"></a><a name="b1574542215438"></a>limit</strong> should always be used together.</p>
<p id="p886861412119"><a name="p886861412119"></a><a name="p886861412119"></a>The value is greater than or equal to 0.</p>
</td>
</tr>
<tr id="row1094719159531"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.5.1.1 "><p id="p1694710157531"><a name="p1694710157531"></a><a name="p1694710157531"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.2 "><p id="p1568252172015"><a name="p1568252172015"></a><a name="p1568252172015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.3 "><p id="p0965151043516"><a name="p0965151043516"></a><a name="p0965151043516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.2.5.1.4 "><p id="p994720159536"><a name="p994720159536"></a><a name="p994720159536"></a>Start index. Parameters <strong id="b944534154310"><a name="b944534154310"></a><a name="b944534154310"></a>offset</strong> and <strong id="b104514341433"><a name="b104514341433"></a><a name="b104514341433"></a>limit</strong> should always be used together.</p>
<p id="p12118223171111"><a name="p12118223171111"></a><a name="p12118223171111"></a>The value is greater than or equal to 0.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section684103419566"></a>

N/A

## Response<a name="section02053705819"></a>

**Response parameters**

**Table  2**  Response header parameter description

<a name="table1424310301435"></a>
<table><thead align="left"><tr id="row735116303316"><th class="cellrowborder" valign="top" width="17.568243175682433%" id="mcps1.2.4.1.1"><p id="p8351730635"><a name="p8351730635"></a><a name="p8351730635"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.57874212578742%" id="mcps1.2.4.1.2"><p id="p1535183015315"><a name="p1535183015315"></a><a name="p1535183015315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.85301469853015%" id="mcps1.2.4.1.3"><p id="p1335118301137"><a name="p1335118301137"></a><a name="p1335118301137"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row183524301839"><td class="cellrowborder" valign="top" width="17.568243175682433%" headers="mcps1.2.4.1.1 "><p id="p103521030935"><a name="p103521030935"></a><a name="p103521030935"></a>Content-Range</p>
</td>
<td class="cellrowborder" valign="top" width="12.57874212578742%" headers="mcps1.2.4.1.2 "><p id="p935214305319"><a name="p935214305319"></a><a name="p935214305319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.85301469853015%" headers="mcps1.2.4.1.3 "><p id="p163521730337"><a name="p163521730337"></a><a name="p163521730337"></a>Offset (Start index)–Count (Number of records on the current page)/Total (Total number of records)</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>When a request passes the parameters  **offset**  and  **limit**,  **Content-Range**  will be added in the response header.  

**Table  3**  Response body parameter description

<a name="table45446245174724"></a>
<table><thead align="left"><tr id="row1412623174724"><th class="cellrowborder" valign="top" width="21.52215221522152%" id="mcps1.2.4.1.1"><p id="p47313663174724"><a name="p47313663174724"></a><a name="p47313663174724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.75197519751975%" id="mcps1.2.4.1.2"><p id="p7201512174724"><a name="p7201512174724"></a><a name="p7201512174724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.725872587258735%" id="mcps1.2.4.1.3"><p id="p4480706174724"><a name="p4480706174724"></a><a name="p4480706174724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40294727101415"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p42647463101415"><a name="p42647463101415"></a><a name="p42647463101415"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p658717815145"><a name="p658717815145"></a><a name="p658717815145"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p988225101415"><a name="p988225101415"></a><a name="p988225101415"></a>Repository name.</p>
</td>
</tr>
<tr id="row98876365819"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1624210616586"><a name="p1624210616586"></a><a name="p1624210616586"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p258810818144"><a name="p258810818144"></a><a name="p258810818144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p6245963583"><a name="p6245963583"></a><a name="p6245963583"></a>Repository type.</p>
</td>
</tr>
<tr id="row3367184810392"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p16368174813396"><a name="p16368174813396"></a><a name="p16368174813396"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p19588148151418"><a name="p19588148151418"></a><a name="p19588148151418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p036834817394"><a name="p036834817394"></a><a name="p036834817394"></a>Repository description.</p>
</td>
</tr>
<tr id="row626682835815"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1126642811589"><a name="p1126642811589"></a><a name="p1126642811589"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p1658828191410"><a name="p1658828191410"></a><a name="p1658828191410"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p2266162865816"><a name="p2266162865816"></a><a name="p2266162865816"></a>Image repository size.</p>
</td>
</tr>
<tr id="row1286171411597"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p54433257594"><a name="p54433257594"></a><a name="p54433257594"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p145883812142"><a name="p145883812142"></a><a name="p145883812142"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p944519257591"><a name="p944519257591"></a><a name="p944519257591"></a>Whether the image is public. When the value is <strong id="b5463125381710"><a name="b5463125381710"></a><a name="b5463125381710"></a>true</strong>, it indicates the image is public. When the value is <strong id="b94126209515"><a name="b94126209515"></a><a name="b94126209515"></a>false</strong>, it indicates the image is private.</p>
</td>
</tr>
<tr id="row38403527599"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1984085216595"><a name="p1984085216595"></a><a name="p1984085216595"></a>num_images</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p07801756165414"><a name="p07801756165414"></a><a name="p07801756165414"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p17840175285913"><a name="p17840175285913"></a><a name="p17840175285913"></a>Number of image tags in a repository.</p>
</td>
</tr>
<tr id="row15637848145911"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p166384486595"><a name="p166384486595"></a><a name="p166384486595"></a>num_download</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p197861656195414"><a name="p197861656195414"></a><a name="p197861656195414"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p763834825915"><a name="p763834825915"></a><a name="p763834825915"></a>Download times.</p>
</td>
</tr>
<tr id="row65154041101837"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p42985951101837"><a name="p42985951101837"></a><a name="p42985951101837"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p1743014144140"><a name="p1743014144140"></a><a name="p1743014144140"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p35094394113433"><a name="p35094394113433"></a><a name="p35094394113433"></a>Time when a repository is created, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row57344470102311"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p14390475102311"><a name="p14390475102311"></a><a name="p14390475102311"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p13430171491418"><a name="p13430171491418"></a><a name="p13430171491418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p29749998102311"><a name="p29749998102311"></a><a name="p29749998102311"></a>Time when a repository is updated, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row1037174225"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p173714629"><a name="p173714629"></a><a name="p173714629"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p19430181417142"><a name="p19430181417142"></a><a name="p19430181417142"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p15371642213"><a name="p15371642213"></a><a name="p15371642213"></a>URL of the repository logo (reserved).</p>
</td>
</tr>
<tr id="row96289175419"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1962815171412"><a name="p1962815171412"></a><a name="p1962815171412"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p525820238140"><a name="p525820238140"></a><a name="p525820238140"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p46296170410"><a name="p46296170410"></a><a name="p46296170410"></a>Image address for docker pull.</p>
</td>
</tr>
<tr id="row1952451421"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p195242115212"><a name="p195242115212"></a><a name="p195242115212"></a>internal_path</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p225818234148"><a name="p225818234148"></a><a name="p225818234148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p1752461723"><a name="p1752461723"></a><a name="p1752461723"></a>Intra-cluster image address for docker pull.</p>
</td>
</tr>
<tr id="row552719404114"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p15110411915"><a name="p15110411915"></a><a name="p15110411915"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p17258323111412"><a name="p17258323111412"></a><a name="p17258323111412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p6514184115111"><a name="p6514184115111"></a><a name="p6514184115111"></a>Domain name.</p>
</td>
</tr>
<tr id="row1690219211219"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p114951323118"><a name="p114951323118"></a><a name="p114951323118"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p52580236146"><a name="p52580236146"></a><a name="p52580236146"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p174981723714"><a name="p174981723714"></a><a name="p174981723714"></a>Organization name.</p>
</td>
</tr>
<tr id="row526812354412"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p4268153174414"><a name="p4268153174414"></a><a name="p4268153174414"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p1525812235148"><a name="p1525812235148"></a><a name="p1525812235148"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p62688354419"><a name="p62688354419"></a><a name="p62688354419"></a>Image tag list.</p>
</td>
</tr>
<tr id="row10524198121716"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p65241089174"><a name="p65241089174"></a><a name="p65241089174"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p1925832301413"><a name="p1925832301413"></a><a name="p1925832301413"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p4524683178"><a name="p4524683178"></a><a name="p4524683178"></a>Query the images shared by others: Check whether the image has expired.</p>
<p id="p6673735121810"><a name="p6673735121810"></a><a name="p6673735121810"></a>Query the images shared by you: The default value is <strong id="b2498195134412"><a name="b2498195134412"></a><a name="b2498195134412"></a>false</strong>, which has no specific meaning.</p>
</td>
</tr>
<tr id="row105011049115614"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p67751489548"><a name="p67751489548"></a><a name="p67751489548"></a>logo</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p20775108175419"><a name="p20775108175419"></a><a name="p20775108175419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p157751685549"><a name="p157751685549"></a><a name="p157751685549"></a>Repository logo (reserved).</p>
</td>
</tr>
<tr id="row155451514105717"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1327583410124"><a name="p1327583410124"></a><a name="p1327583410124"></a>total_range</p>
</td>
<td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.2.4.1.2 "><p id="p1727583451216"><a name="p1727583451216"></a><a name="p1727583451216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.725872587258735%" headers="mcps1.2.4.1.3 "><p id="p727517346122"><a name="p727517346122"></a><a name="p727517346122"></a>Total number of repositories (reserved).</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
[
    {
        "name": "otc",
        "category": "other",
        "description": "",
        "size": 115645792,
        "is_public": false,
        "num_images": 1,
        "num_download": 0,
        "created_at": "2018-03-21T12:22:37Z",
        "updated_at": "2018-03-21T12:22:37Z",
        "logo": "",
        "url": "",
        "path": "192.158.24.86/namespace/otc",
        "internal_path": "10.125.0.198:20202/namespace/otc",
        "domain_name": "domian",
        "namespace": "namespace",
        "tags": [
            "latest"
        ],
        "status": true,
        "total_range": 0
    }
]
```

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 4](#table1327183872417).

**Table  4**  Status code

<a name="table1327183872417"></a>
<table><thead align="left"><tr id="row127115381244"><th class="cellrowborder" valign="top" width="22.39%" id="mcps1.2.3.1.1"><p id="p2027103812240"><a name="p2027103812240"></a><a name="p2027103812240"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="77.61%" id="mcps1.2.3.1.2"><p id="p8271638162420"><a name="p8271638162420"></a><a name="p8271638162420"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13271143832414"><td class="cellrowborder" valign="top" width="22.39%" headers="mcps1.2.3.1.1 "><p id="p52711438162416"><a name="p52711438162416"></a><a name="p52711438162416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="77.61%" headers="mcps1.2.3.1.2 "><p id="p16271143817245"><a name="p16271143817245"></a><a name="p16271143817245"></a>Request sent successfully.</p>
</td>
</tr>
<tr id="row527119386242"><td class="cellrowborder" valign="top" width="22.39%" headers="mcps1.2.3.1.1 "><p id="p927263882412"><a name="p927263882412"></a><a name="p927263882412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="77.61%" headers="mcps1.2.3.1.2 "><p id="p7272738132420"><a name="p7272738132420"></a><a name="p7272738132420"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row10272123812412"><td class="cellrowborder" valign="top" width="22.39%" headers="mcps1.2.3.1.1 "><p id="p22721838162418"><a name="p22721838162418"></a><a name="p22721838162418"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="77.61%" headers="mcps1.2.3.1.2 "><p id="p32721383247"><a name="p32721383247"></a><a name="p32721383247"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row1827243852412"><td class="cellrowborder" valign="top" width="22.39%" headers="mcps1.2.3.1.1 "><p id="p12272153822415"><a name="p12272153822415"></a><a name="p12272153822415"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="77.61%" headers="mcps1.2.3.1.2 "><p id="p327203862414"><a name="p327203862414"></a><a name="p327203862414"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

