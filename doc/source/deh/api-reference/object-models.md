# Object Models<a name="EN-US_TOPIC_0087389274"></a>

## Objects<a name="section1210700"></a>

DeH management includes querying the DeH list, viewing DeH details, modifying DeH attributes, allocating a DeH, and releasing a DeH.

## Object Models<a name="page_link"></a>

**Table  1**  dedicated\_host

<a name="dedicated_host"></a>
<table><thead align="left"><tr id="row33200047"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.7.1.1"><p id="p4849307"><a name="p4849307"></a><a name="p4849307"></a><strong id="b04644160347"><a name="b04644160347"></a><a name="b04644160347"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.7.1.2"><p id="p57249620"><a name="p57249620"></a><a name="p57249620"></a><strong id="b84235270610297"><a name="b84235270610297"></a><a name="b84235270610297"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.2.7.1.3"><p id="p6707649"><a name="p6707649"></a><a name="p6707649"></a><strong id="b842352706102913"><a name="b842352706102913"></a><a name="b842352706102913"></a>CRUD</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.7.1.4"><p id="p6448715"><a name="p6448715"></a><a name="p6448715"></a><strong id="b10725132853415"><a name="b10725132853415"></a><a name="b10725132853415"></a>Default Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.7.1.5"><p id="p52583897"><a name="p52583897"></a><a name="p52583897"></a><strong id="b44644268114611"><a name="b44644268114611"></a><a name="b44644268114611"></a>Constraint</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.2.7.1.6"><p id="p31437268"><a name="p31437268"></a><a name="p31437268"></a><strong id="b8571191812411"><a name="b8571191812411"></a><a name="b8571191812411"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14499957"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p33645886"><a name="p33645886"></a><a name="p33645886"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p40962215"><a name="p40962215"></a><a name="p40962215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p29605080"><a name="p29605080"></a><a name="p29605080"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p49201274"><a name="p49201274"></a><a name="p49201274"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p25880244"><a name="p25880244"></a><a name="p25880244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p15925039"><a name="p15925039"></a><a name="p15925039"></a>N/A</p>
</td>
</tr>
<tr id="row9107628"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p66629291"><a name="p66629291"></a><a name="p66629291"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p28263486"><a name="p28263486"></a><a name="p28263486"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p7641038"><a name="p7641038"></a><a name="p7641038"></a>CUR</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p14944322"><a name="p14944322"></a><a name="p14944322"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p2530563"><a name="p2530563"></a><a name="p2530563"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p3649016"><a name="p3649016"></a><a name="p3649016"></a>Specifies the DeH name.</p>
<p id="p13664115735719"><a name="p13664115735719"></a><a name="p13664115735719"></a>The name can contain a maximum of 255 characters and cannot start or end with spaces.</p>
</td>
</tr>
<tr id="row32841145"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p42887128"><a name="p42887128"></a><a name="p42887128"></a>auto_placement</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p51305376"><a name="p51305376"></a><a name="p51305376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p62094776"><a name="p62094776"></a><a name="p62094776"></a>CUR</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p63620936"><a name="p63620936"></a><a name="p63620936"></a>on</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p53022201"><a name="p53022201"></a><a name="p53022201"></a>The value can be <strong id="b3493335105119"><a name="b3493335105119"></a><a name="b3493335105119"></a>on</strong> or <strong id="b9715137105110"><a name="b9715137105110"></a><a name="b9715137105110"></a>off</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p985165241917"><a name="p985165241917"></a><a name="p985165241917"></a>Specifies whether to allow an ECS to be placed on any available DeH if its DeH ID is not specified during its creation.</p>
</td>
</tr>
<tr id="row11036355"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p21529561"><a name="p21529561"></a><a name="p21529561"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p66172851"><a name="p66172851"></a><a name="p66172851"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p58400697"><a name="p58400697"></a><a name="p58400697"></a>CR</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p32836053"><a name="p32836053"></a><a name="p32836053"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p42474604"><a name="p42474604"></a><a name="p42474604"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="OLE_LINK29"><a name="OLE_LINK29"></a><a name="OLE_LINK29"></a>Specifies the AZ to which the DeH belongs.</p>
</td>
</tr>
<tr id="row26800560"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p23361726"><a name="p23361726"></a><a name="p23361726"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p13251620"><a name="p13251620"></a><a name="p13251620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p66748299"><a name="p66748299"></a><a name="p66748299"></a>CR</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="OLE_LINK101"><a name="OLE_LINK101"></a><a name="OLE_LINK101"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p50254714"><a name="p50254714"></a><a name="p50254714"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="OLE_LINK109"><a name="OLE_LINK109"></a><a name="OLE_LINK109"></a>Specifies the tenant who owns the DeH.</p>
</td>
</tr>
<tr id="row61356140"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p3791404"><a name="p3791404"></a><a name="p3791404"></a>host_properties</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p118075491772"><a name="p118075491772"></a><a name="p118075491772"></a>Dict</p>
<p id="p38668280"><a name="p38668280"></a><a name="p38668280"></a>For details, see <a href="#host_property">Table 2</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p3453833"><a name="p3453833"></a><a name="p3453833"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p11325076"><a name="p11325076"></a><a name="p11325076"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p44915976"><a name="p44915976"></a><a name="p44915976"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p14315403"><a name="p14315403"></a><a name="p14315403"></a>Specifies the DeH properties.</p>
</td>
</tr>
<tr id="row61729771"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p34055563"><a name="p34055563"></a><a name="p34055563"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p7037199"><a name="p7037199"></a><a name="p7037199"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p33142240"><a name="p33142240"></a><a name="p33142240"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p166885"><a name="p166885"></a><a name="p166885"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p13517702"><a name="p13517702"></a><a name="p13517702"></a>The value can be <strong id="b8159193061216"><a name="b8159193061216"></a><a name="b8159193061216"></a>available</strong>, <strong id="b9185114717124"><a name="b9185114717124"></a><a name="b9185114717124"></a>fault</strong>, or <strong id="b12161113015126"><a name="b12161113015126"></a><a name="b12161113015126"></a>released</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p14008765"><a name="p14008765"></a><a name="p14008765"></a>Specifies the DeH status.</p>
</td>
</tr>
<tr id="row58970022"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p11842506"><a name="p11842506"></a><a name="p11842506"></a>available_vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p19718930"><a name="p19718930"></a><a name="p19718930"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p53729511"><a name="p53729511"></a><a name="p53729511"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p57123120"><a name="p57123120"></a><a name="p57123120"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p63570006"><a name="p63570006"></a><a name="p63570006"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p48896832"><a name="p48896832"></a><a name="p48896832"></a>Specifies the number of available vCPUs for the DeH.</p>
</td>
</tr>
<tr id="row37418306"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p10983950"><a name="p10983950"></a><a name="p10983950"></a>available_memory</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p17284754"><a name="p17284754"></a><a name="p17284754"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p57887863"><a name="p57887863"></a><a name="p57887863"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p58405349"><a name="p58405349"></a><a name="p58405349"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p33212803"><a name="p33212803"></a><a name="p33212803"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p5882489"><a name="p5882489"></a><a name="p5882489"></a>Specifies the available memory size of the DeH.</p>
</td>
</tr>
<tr id="row52942405"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p60476403"><a name="p60476403"></a><a name="p60476403"></a>allocated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p66750478"><a name="p66750478"></a><a name="p66750478"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p38079613"><a name="p38079613"></a><a name="p38079613"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p64549801"><a name="p64549801"></a><a name="p64549801"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p61151353"><a name="p61151353"></a><a name="p61151353"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p54312533"><a name="p54312533"></a><a name="p54312533"></a>Specifies the time when the DeH is allocated.</p>
</td>
</tr>
<tr id="row19050756"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p66716254"><a name="p66716254"></a><a name="p66716254"></a>released_at</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p35307513"><a name="p35307513"></a><a name="p35307513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p41336317"><a name="p41336317"></a><a name="p41336317"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p59907344"><a name="p59907344"></a><a name="p59907344"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p20656733"><a name="p20656733"></a><a name="p20656733"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p62582666"><a name="p62582666"></a><a name="p62582666"></a>Specifies the time when the DeH is released.</p>
</td>
</tr>
<tr id="row26373084"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p55845053"><a name="p55845053"></a><a name="p55845053"></a>instance_total</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p27155410"><a name="p27155410"></a><a name="p27155410"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p52104579"><a name="p52104579"></a><a name="p52104579"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p59721402"><a name="p59721402"></a><a name="p59721402"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p5595356"><a name="p5595356"></a><a name="p5595356"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p50570707"><a name="p50570707"></a><a name="p50570707"></a>Specifies the total number of ECSs on the DeH.</p>
</td>
</tr>
<tr id="row52483186"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p23279683"><a name="p23279683"></a><a name="p23279683"></a>instance_uuids</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p6606172"><a name="p6606172"></a><a name="p6606172"></a>List &lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p65337958"><a name="p65337958"></a><a name="p65337958"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p57883273"><a name="p57883273"></a><a name="p57883273"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="OLE_LINK117"><a name="OLE_LINK117"></a><a name="OLE_LINK117"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="OLE_LINK57"><a name="OLE_LINK57"></a><a name="OLE_LINK57"></a>Specifies the UUIDs of the ECSs running on the DeH.</p>
<p id="p27848947"><a name="p27848947"></a><a name="p27848947"></a>This parameter is not displayed on the interface for <a href="querying-dehs.md">querying DeHs</a>.</p>
</td>
</tr>
<tr id="row139181081714"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p139188018173"><a name="p139188018173"></a><a name="p139188018173"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p20918160131716"><a name="p20918160131716"></a><a name="p20918160131716"></a>Dict(str:str)</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p1191814001711"><a name="p1191814001711"></a><a name="p1191814001711"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p491812011177"><a name="p491812011177"></a><a name="p491812011177"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p1491813091715"><a name="p1491813091715"></a><a name="p1491813091715"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p39185081711"><a name="p39185081711"></a><a name="p39185081711"></a>Specifies the DeH tags.</p>
</td>
</tr>
<tr id="row81921846121916"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.1 "><p id="p16192246151910"><a name="p16192246151910"></a><a name="p16192246151910"></a>sys_tags</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.2 "><p id="p31927464191"><a name="p31927464191"></a><a name="p31927464191"></a>Dict(str:str)</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.7.1.3 "><p id="p14192194620191"><a name="p14192194620191"></a><a name="p14192194620191"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.4 "><p id="p119244618192"><a name="p119244618192"></a><a name="p119244618192"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.5 "><p id="p1419244617198"><a name="p1419244617198"></a><a name="p1419244617198"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.7.1.6 "><p id="p1019234620195"><a name="p1019234620195"></a><a name="p1019234620195"></a>Specifies the DeH system tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  host\_property

<a name="host_property"></a>
<table><thead align="left"><tr id="row2289152"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.7.1.1"><p id="p541512715561"><a name="p541512715561"></a><a name="p541512715561"></a><strong id="b138515143432"><a name="b138515143432"></a><a name="b138515143432"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.7.1.2"><p id="p3416112775617"><a name="p3416112775617"></a><a name="p3416112775617"></a><strong id="b752173508"><a name="b752173508"></a><a name="b752173508"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.7.1.3"><p id="p14418192713564"><a name="p14418192713564"></a><a name="p14418192713564"></a><strong id="b1420502666"><a name="b1420502666"></a><a name="b1420502666"></a>CRUD</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.7.1.4"><p id="p14421162719566"><a name="p14421162719566"></a><a name="p14421162719566"></a><strong id="b454487285"><a name="b454487285"></a><a name="b454487285"></a>Default Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.7.1.5"><p id="p942314279563"><a name="p942314279563"></a><a name="p942314279563"></a><strong id="b2018018345"><a name="b2018018345"></a><a name="b2018018345"></a>Constraint</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.7.1.6"><p id="p1342572714562"><a name="p1342572714562"></a><a name="p1342572714562"></a><strong id="b151579311143"><a name="b151579311143"></a><a name="b151579311143"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5379216"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p33063388"><a name="p33063388"></a><a name="p33063388"></a>host_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p60888739"><a name="p60888739"></a><a name="p60888739"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p33040847"><a name="p33040847"></a><a name="p33040847"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p59062984"><a name="p59062984"></a><a name="p59062984"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="p19372405"><a name="p19372405"></a><a name="p19372405"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="p25660991"><a name="p25660991"></a><a name="p25660991"></a>Specifies the DeH type.</p>
</td>
</tr>
<tr id="row29622330"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p50598521"><a name="p50598521"></a><a name="p50598521"></a>host_type_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p4839561"><a name="p4839561"></a><a name="p4839561"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p56460178"><a name="p56460178"></a><a name="p56460178"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p9871675"><a name="p9871675"></a><a name="p9871675"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="p61408172"><a name="p61408172"></a><a name="p61408172"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="p8006030"><a name="p8006030"></a><a name="p8006030"></a>Specifies the name of the DeH type.</p>
</td>
</tr>
<tr id="row4945408"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p65033806"><a name="p65033806"></a><a name="p65033806"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p33246944"><a name="p33246944"></a><a name="p33246944"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p8647967"><a name="p8647967"></a><a name="p8647967"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p29396722"><a name="p29396722"></a><a name="p29396722"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="p32324290"><a name="p32324290"></a><a name="p32324290"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="p1021814"><a name="p1021814"></a><a name="p1021814"></a>Specifies the number of vCPUs on the DeH.</p>
</td>
</tr>
<tr id="row9196329"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p6705199"><a name="p6705199"></a><a name="p6705199"></a>cores</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p6250253"><a name="p6250253"></a><a name="p6250253"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p36508524"><a name="p36508524"></a><a name="p36508524"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p4400500"><a name="p4400500"></a><a name="p4400500"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="OLE_LINK94"><a name="OLE_LINK94"></a><a name="OLE_LINK94"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="OLE_LINK55"><a name="OLE_LINK55"></a><a name="OLE_LINK55"></a>Specifies the number of physical cores on the DeH.</p>
</td>
</tr>
<tr id="row66729601"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p36388601"><a name="p36388601"></a><a name="p36388601"></a>sockets</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p61795582"><a name="p61795582"></a><a name="p61795582"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p39386231"><a name="p39386231"></a><a name="p39386231"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p36168141"><a name="p36168141"></a><a name="p36168141"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="p43938279"><a name="p43938279"></a><a name="p43938279"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="OLE_LINK30"><a name="OLE_LINK30"></a><a name="OLE_LINK30"></a>Specifies the number of physical sockets on the DeH.</p>
</td>
</tr>
<tr id="row20077469"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p15662289"><a name="p15662289"></a><a name="p15662289"></a>memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p60685926"><a name="p60685926"></a><a name="p60685926"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p16612996"><a name="p16612996"></a><a name="p16612996"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p3475410"><a name="p3475410"></a><a name="p3475410"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="p13072760"><a name="p13072760"></a><a name="p13072760"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="p52260639"><a name="p52260639"></a><a name="p52260639"></a>Specifies the size of physical memory on the DeH.</p>
</td>
</tr>
<tr id="row583706"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.1 "><p id="p47280229"><a name="p47280229"></a><a name="p47280229"></a>available_instance_capacities</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.2 "><p id="p1413333912811"><a name="p1413333912811"></a><a name="p1413333912811"></a>List</p>
<p id="p4493316"><a name="p4493316"></a><a name="p4493316"></a>For details, see <a href="#table61747774">Table 3</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.3 "><p id="p54402144"><a name="p54402144"></a><a name="p54402144"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.7.1.4 "><p id="p44497505"><a name="p44497505"></a><a name="p44497505"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.7.1.5 "><p id="p47528147"><a name="p47528147"></a><a name="p47528147"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.7.1.6 "><p id="p24574685"><a name="p24574685"></a><a name="p24574685"></a>Specifies the flavors of ECSs placed on the DeH.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  available\_instance\_capacity

<a name="table61747774"></a>
<table><thead align="left"><tr id="row35285314"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.1"><p id="p1514612242568"><a name="p1514612242568"></a><a name="p1514612242568"></a><strong id="b1556914917434"><a name="b1556914917434"></a><a name="b1556914917434"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.2"><p id="p21481024125620"><a name="p21481024125620"></a><a name="p21481024125620"></a><strong id="b1714222493"><a name="b1714222493"></a><a name="b1714222493"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.7.1.3"><p id="p11502024195612"><a name="p11502024195612"></a><a name="p11502024195612"></a><strong id="b1379522040"><a name="b1379522040"></a><a name="b1379522040"></a>CRUD</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.7.1.4"><p id="p1715217247563"><a name="p1715217247563"></a><a name="p1715217247563"></a><strong id="b1406904004"><a name="b1406904004"></a><a name="b1406904004"></a>Default Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.7.1.5"><p id="p19154192495615"><a name="p19154192495615"></a><a name="p19154192495615"></a><strong id="b1972469435"><a name="b1972469435"></a><a name="b1972469435"></a>Constraint</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.7.1.6"><p id="p1815617248567"><a name="p1815617248567"></a><a name="p1815617248567"></a><strong id="b1931110212148"><a name="b1931110212148"></a><a name="b1931110212148"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row38788755"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p54881489"><a name="p54881489"></a><a name="p54881489"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="p16215635"><a name="p16215635"></a><a name="p16215635"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.3 "><p id="p38398082"><a name="p38398082"></a><a name="p38398082"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p23236933"><a name="p23236933"></a><a name="p23236933"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.5 "><p id="p3143429"><a name="p3143429"></a><a name="p3143429"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.7.1.6 "><p id="OLE_LINK104"><a name="OLE_LINK104"></a><a name="OLE_LINK104"></a>Specifies the number of supported flavors.</p>
</td>
</tr>
</tbody>
</table>

