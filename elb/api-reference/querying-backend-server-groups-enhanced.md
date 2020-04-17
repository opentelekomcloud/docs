# Querying Backend Server Groups<a name="EN-US_TOPIC_0096561547"></a>

## Function<a name="section5542121110137"></a>

This API is used to query the backend server groups and display them in a list. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="section1834893819135"></a>

GET /v2.0/lbaas/pools

## Constraints<a name="section12943112511216"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="section1090013651111"></a>

**Table  1**  Request parameters

<a name="table7129721916"></a>
<table><thead align="left"><tr id="row538119214112"><th class="cellrowborder" valign="top" width="23.849999999999998%" id="mcps1.2.5.1.1"><p id="p738122119116"><a name="p738122119116"></a><a name="p738122119116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.86%" id="mcps1.2.5.1.2"><p id="p2381132120119"><a name="p2381132120119"></a><a name="p2381132120119"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.5%" id="mcps1.2.5.1.3"><p id="p1138132113114"><a name="p1138132113114"></a><a name="p1138132113114"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.79%" id="mcps1.2.5.1.4"><p id="p173811921118"><a name="p173811921118"></a><a name="p173811921118"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1638115211110"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p938117212112"><a name="p938117212112"></a><a name="p938117212112"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p538162110118"><a name="p538162110118"></a><a name="p538162110118"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p338162118117"><a name="p338162118117"></a><a name="p338162118117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p179681426923"><a name="p179681426923"></a><a name="p179681426923"></a>Specifies the ID of the backend server group from which pagination query starts, that is, the ID of the last backend server group on the previous page. If this parameter is not specified, the first page will be queried.</p>
<p id="p124032918214"><a name="p124032918214"></a><a name="p124032918214"></a>This parameter must be used together with <strong id="b622161652010"><a name="b622161652010"></a><a name="b622161652010"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row1538111211318"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p1538112211211"><a name="p1538112211211"></a><a name="p1538112211211"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p938117217112"><a name="p938117217112"></a><a name="p938117217112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p183816211113"><a name="p183816211113"></a><a name="p183816211113"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p814016314216"><a name="p814016314216"></a><a name="p814016314216"></a>Specifies the number of backend server groups on each page.</p>
<p id="p1414613319219"><a name="p1414613319219"></a><a name="p1414613319219"></a>The value ranges from <strong id="b9556184412015"><a name="b9556184412015"></a><a name="b9556184412015"></a>0</strong> to <strong id="b3541440102014"><a name="b3541440102014"></a><a name="b3541440102014"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row113818213111"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p19382162112117"><a name="p19382162112117"></a><a name="p19382162112117"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1138332110111"><a name="p1138332110111"></a><a name="p1138332110111"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p1738318219120"><a name="p1738318219120"></a><a name="p1738318219120"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p5902734022"><a name="p5902734022"></a><a name="p5902734022"></a>Specifies the page direction. The value can be <strong id="b5435947122015"><a name="b5435947122015"></a><a name="b5435947122015"></a>true</strong> or <strong id="b144361047112019"><a name="b144361047112019"></a><a name="b144361047112019"></a>false</strong>, and the default value is <strong id="b14438164717204"><a name="b14438164717204"></a><a name="b14438164717204"></a>false</strong>. The last page in the list requested with <strong id="b1943974772015"><a name="b1943974772015"></a><a name="b1943974772015"></a>page_reverse</strong> set to <strong id="b114401147192014"><a name="b114401147192014"></a><a name="b114401147192014"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b644134718200"><a name="b644134718200"></a><a name="b644134718200"></a>page_reverse</strong> set to <strong id="b74421475202"><a name="b74421475202"></a><a name="b74421475202"></a>true</strong> will not contain the "previous" link.</p>
<p id="p13879193614214"><a name="p13879193614214"></a><a name="p13879193614214"></a>This parameter must be used together with <strong id="b1195610588200"><a name="b1195610588200"></a><a name="b1195610588200"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row1038310211611"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p43834219115"><a name="p43834219115"></a><a name="p43834219115"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1738316218113"><a name="p1738316218113"></a><a name="p1738316218113"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p3196163614328"><a name="p3196163614328"></a><a name="p3196163614328"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p193834211015"><a name="p193834211015"></a><a name="p193834211015"></a>Specifies the ID of the backend server group.</p>
</td>
</tr>
<tr id="row1218512724616"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p88461695515"><a name="p88461695515"></a><a name="p88461695515"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1084618910518"><a name="p1084618910518"></a><a name="p1084618910518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p188466919514"><a name="p188466919514"></a><a name="p188466919514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p11846891258"><a name="p11846891258"></a><a name="p11846891258"></a>Specifies the ID of the project where the backend server group is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1738316211015"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p1938315214112"><a name="p1938315214112"></a><a name="p1938315214112"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p638322110119"><a name="p638322110119"></a><a name="p638322110119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p938342115116"><a name="p938342115116"></a><a name="p938342115116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p638312118113"><a name="p638312118113"></a><a name="p638312118113"></a>Specifies the backend server group name.</p>
<p id="p781531910400"><a name="p781531910400"></a><a name="p781531910400"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row63836212117"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p9383421217"><a name="p9383421217"></a><a name="p9383421217"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1038342114119"><a name="p1038342114119"></a><a name="p1038342114119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p43835215118"><a name="p43835215118"></a><a name="p43835215118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p8383142115117"><a name="p8383142115117"></a><a name="p8383142115117"></a>Provides supplementary information about the backend server group.</p>
<p id="p1351602224018"><a name="p1351602224018"></a><a name="p1351602224018"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row83831421311"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p1738342119119"><a name="p1738342119119"></a><a name="p1738342119119"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1838311211113"><a name="p1838311211113"></a><a name="p1838311211113"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p8383221516"><a name="p8383221516"></a><a name="p8383221516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p18384521816"><a name="p18384521816"></a><a name="p18384521816"></a>Specifies the ID of the health check configured for the backend server group.</p>
</td>
</tr>
<tr id="row153841821318"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p17384102120119"><a name="p17384102120119"></a><a name="p17384102120119"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p23841211112"><a name="p23841211112"></a><a name="p23841211112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p4384202112111"><a name="p4384202112111"></a><a name="p4384202112111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p1038413212016"><a name="p1038413212016"></a><a name="p1038413212016"></a>Specifies the ID of the load balancer associated with the backend server group.</p>
</td>
</tr>
<tr id="row4384421817"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p103844211014"><a name="p103844211014"></a><a name="p103844211014"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p738412214110"><a name="p738412214110"></a><a name="p738412214110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p13384112114116"><a name="p13384112114116"></a><a name="p13384112114116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p1323217399215"><a name="p1323217399215"></a><a name="p1323217399215"></a>Specifies the protocol that the backend server group uses to receive requests.</p>
<p id="p58331416213"><a name="p58331416213"></a><a name="p58331416213"></a>TCP, UDP, and HTTP are supported.</p>
</td>
</tr>
<tr id="row83841521313"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p18384112111113"><a name="p18384112111113"></a><a name="p18384112111113"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p17384182115111"><a name="p17384182115111"></a><a name="p17384182115111"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p33842021119"><a name="p33842021119"></a><a name="p33842021119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p132038451727"><a name="p132038451727"></a><a name="p132038451727"></a>Specifies the load balancing algorithm of the backend server group.</p>
<div class="p" id="p154275318216"><a name="p154275318216"></a><a name="p154275318216"></a>The value can be one of the following:<a name="ul142123811119"></a><a name="ul142123811119"></a><ul id="ul142123811119"><li><strong id="b17354545012"><a name="b17354545012"></a><a name="b17354545012"></a>ROUND_ROBIN</strong>: indicates the weighted round robin algorithm.</li><li><strong id="b6425185117117"><a name="b6425185117117"></a><a name="b6425185117117"></a>LEAST_CONNECTIONS</strong>: indicates the weighted least connections algorithm.</li><li><strong id="b9926452314"><a name="b9926452314"></a><a name="b9926452314"></a>SOURCE_IP</strong>: indicates the source IP hash algorithm.</li></ul>
</div>
<p id="p16826145612214"><a name="p16826145612214"></a><a name="p16826145612214"></a>When the value is <strong id="b151091917181820"><a name="b151091917181820"></a><a name="b151091917181820"></a>SOURCE_IP</strong>, the weights of backend servers in the server group are invalid. For details about parameter <strong id="b13109517181810"><a name="b13109517181810"></a><a name="b13109517181810"></a>weight</strong>, see <a href="querying-details-of-a-backend-server-enhanced.md#en-us_topic_0049139656_table63335993">Table 2</a>.</p>
</td>
</tr>
<tr id="row03845212012"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p1838410214111"><a name="p1838410214111"></a><a name="p1838410214111"></a>member_address</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p438515214117"><a name="p438515214117"></a><a name="p438515214117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p93851021514"><a name="p93851021514"></a><a name="p93851021514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p1848714119178"><a name="p1848714119178"></a><a name="p1848714119178"></a>Lists the IDs of backend servers in the backend server group.</p>
</td>
</tr>
<tr id="row20385112113112"><td class="cellrowborder" valign="top" width="23.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p1385921612"><a name="p1385921612"></a><a name="p1385921612"></a>member_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p83857219119"><a name="p83857219119"></a><a name="p83857219119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.3 "><p id="p638519217118"><a name="p638519217118"></a><a name="p638519217118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.79%" headers="mcps1.2.5.1.4 "><p id="p1970143121718"><a name="p1970143121718"></a><a name="p1970143121718"></a>Specifies the ID of the ECS corresponding to the backend server in the backend server group.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1454354431112"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0049139647_table37982174"></a>
<table><thead align="left"><tr id="en-us_topic_0049139647_row42245377"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139647_p66432381"><a name="en-us_topic_0049139647_p66432381"></a><a name="en-us_topic_0049139647_p66432381"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139647_p12313777"><a name="en-us_topic_0049139647_p12313777"></a><a name="en-us_topic_0049139647_p12313777"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139647_p58733156"><a name="en-us_topic_0049139647_p58733156"></a><a name="en-us_topic_0049139647_p58733156"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139647_row59765170"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139647_p9140568"><a name="en-us_topic_0049139647_p9140568"></a><a name="en-us_topic_0049139647_p9140568"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139647_p64845166"><a name="en-us_topic_0049139647_p64845166"></a><a name="en-us_topic_0049139647_p64845166"></a>Specifies the backend server group. For details, see <a href="#table92302230217">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **pools**  parameter description

<a name="table92302230217"></a>
<table><thead align="left"><tr id="row133851235215"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p538510231029"><a name="p538510231029"></a><a name="p538510231029"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="p113851723029"><a name="p113851723029"></a><a name="p113851723029"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="p238515231524"><a name="p238515231524"></a><a name="p238515231524"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1538515231928"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p10385112317212"><a name="p10385112317212"></a><a name="p10385112317212"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p9385152316217"><a name="p9385152316217"></a><a name="p9385152316217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p17385182318219"><a name="p17385182318219"></a><a name="p17385182318219"></a>Specifies the ID of the backend server group.</p>
</td>
</tr>
<tr id="row53853231821"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p93851623825"><a name="p93851623825"></a><a name="p93851623825"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p73854231622"><a name="p73854231622"></a><a name="p73854231622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p9691143585417"><a name="p9691143585417"></a><a name="p9691143585417"></a>Specifies the ID of the project where the backend server group is used.</p>
<p id="p79730154314"><a name="p79730154314"></a><a name="p79730154314"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row193851423226"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p638532316218"><a name="p638532316218"></a><a name="p638532316218"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p1238722315219"><a name="p1238722315219"></a><a name="p1238722315219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p11387123624"><a name="p11387123624"></a><a name="p11387123624"></a>Specifies the backend server group name.</p>
<p id="p542020217439"><a name="p542020217439"></a><a name="p542020217439"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row12387723624"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p143878239216"><a name="p143878239216"></a><a name="p143878239216"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p338702318217"><a name="p338702318217"></a><a name="p338702318217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p938714238216"><a name="p938714238216"></a><a name="p938714238216"></a>Provides supplementary information about the backend server group.</p>
<p id="p14495643437"><a name="p14495643437"></a><a name="p14495643437"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row03893231222"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p153891923426"><a name="p153891923426"></a><a name="p153891923426"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p15389102319217"><a name="p15389102319217"></a><a name="p15389102319217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p11911111812316"><a name="p11911111812316"></a><a name="p11911111812316"></a>Specifies the protocol that the backend server group uses to receive requests.</p>
<p id="p298812201438"><a name="p298812201438"></a><a name="p298812201438"></a>TCP, UDP, and HTTP are supported.</p>
</td>
</tr>
<tr id="row13904232218"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p3390223022"><a name="p3390223022"></a><a name="p3390223022"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p14390152311214"><a name="p14390152311214"></a><a name="p14390152311214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p10527152220310"><a name="p10527152220310"></a><a name="p10527152220310"></a>Specifies the load balancing algorithm of the backend server group.</p>
<div class="p" id="p1979132310314"><a name="p1979132310314"></a><a name="p1979132310314"></a>The value can be one of the following:<a name="ul12277910111012"></a><a name="ul12277910111012"></a><ul id="ul12277910111012"><li><strong id="b42661526159"><a name="b42661526159"></a><a name="b42661526159"></a>ROUND_ROBIN</strong>: indicates the weighted round robin algorithm.</li><li><strong id="b64232271156"><a name="b64232271156"></a><a name="b64232271156"></a>LEAST_CONNECTIONS</strong>: indicates the weighted least connections algorithm.</li><li><strong id="b13509828152"><a name="b13509828152"></a><a name="b13509828152"></a>SOURCE_IP</strong>: indicates the source IP hash algorithm.</li></ul>
</div>
<p id="p36516251039"><a name="p36516251039"></a><a name="p36516251039"></a>When the value is <strong id="b1523139192616"><a name="b1523139192616"></a><a name="b1523139192616"></a>SOURCE_IP</strong>, the weights of backend servers in the server group are invalid.</p>
</td>
</tr>
<tr id="row1939082310210"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p103901423524"><a name="p103901423524"></a><a name="p103901423524"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p64801132161311"><a name="p64801132161311"></a><a name="p64801132161311"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p37541017"><a name="p37541017"></a><a name="p37541017"></a>Lists the IDs of backend servers in the backend server group.</p>
</td>
</tr>
<tr id="row1239182319212"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p13911723427"><a name="p13911723427"></a><a name="p13911723427"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p10858161622019"><a name="p10858161622019"></a><a name="p10858161622019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p41358350"><a name="p41358350"></a><a name="p41358350"></a>Specifies the ID of the health check configured for the backend server group.</p>
</td>
</tr>
<tr id="row13391172316213"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p16391182319210"><a name="p16391182319210"></a><a name="p16391182319210"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p143914231223"><a name="p143914231223"></a><a name="p143914231223"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1659614271733"><a name="p1659614271733"></a><a name="p1659614271733"></a>Specifies the administrative status of the backend server group.</p>
<p id="p47273291316"><a name="p47273291316"></a><a name="p47273291316"></a>This parameter is reserved. The default value is <strong id="b554154520268"><a name="b554154520268"></a><a name="b554154520268"></a>true</strong>.</p>
</td>
</tr>
<tr id="row1739172320217"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p133919231922"><a name="p133919231922"></a><a name="p133919231922"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p1132853491316"><a name="p1132853491316"></a><a name="p1132853491316"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1539212231122"><a name="p1539212231122"></a><a name="p1539212231122"></a>Lists the IDs of listeners associated with the backend server group.</p>
</td>
</tr>
<tr id="row9392152314213"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p63921523925"><a name="p63921523925"></a><a name="p63921523925"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p188751622122010"><a name="p188751622122010"></a><a name="p188751622122010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1639219231026"><a name="p1639219231026"></a><a name="p1639219231026"></a>Lists the IDs of load balancers associated with the backend server group.</p>
</td>
</tr>
<tr id="row12392723325"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p1739219232210"><a name="p1739219232210"></a><a name="p1739219232210"></a>session_persistence</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p839212319212"><a name="p839212319212"></a><a name="p839212319212"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p181395331531"><a name="p181395331531"></a><a name="p181395331531"></a>Specifies whether to enable the sticky session feature. For details, see <a href="#table576515134510">Table 4</a>.</p>
<p id="p494963410315"><a name="p494963410315"></a><a name="p494963410315"></a>Once the sticky session feature is enabled, requests from the same client are sent to the same backend server within the specified period.</p>
<p id="p1576573519317"><a name="p1576573519317"></a><a name="p1576573519317"></a>When this feature is disabled, the parameter value is <strong id="b1247195715262"><a name="b1247195715262"></a><a name="b1247195715262"></a>null</strong>.</p>
</td>
</tr>
<tr id="row196193815354"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p142916435352"><a name="p142916435352"></a><a name="p142916435352"></a>pools_links</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p153691436171319"><a name="p153691436171319"></a><a name="p153691436171319"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p958115491633"><a name="p958115491633"></a><a name="p958115491633"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p27814512315"><a name="p27814512315"></a><a name="p27814512315"></a>This parameter exists only in the response body of pagination query. For details, see <a href="#table18892135113610">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **session\_persistence**  parameter description

<a name="table576515134510"></a>
<table><thead align="left"><tr id="en-us_topic_0096561549_row12652114216495"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561549_p8652134218493"><a name="en-us_topic_0096561549_p8652134218493"></a><a name="en-us_topic_0096561549_p8652134218493"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561549_p965284214496"><a name="en-us_topic_0096561549_p965284214496"></a><a name="en-us_topic_0096561549_p965284214496"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561549_p3652164264914"><a name="en-us_topic_0096561549_p3652164264914"></a><a name="en-us_topic_0096561549_p3652164264914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561549_row16652114264914"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p106528426495"><a name="en-us_topic_0096561549_p106528426495"></a><a name="en-us_topic_0096561549_p106528426495"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p665216429491"><a name="en-us_topic_0096561549_p665216429491"></a><a name="en-us_topic_0096561549_p665216429491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p1082720181618"><a name="en-us_topic_0096561549_p1082720181618"></a><a name="en-us_topic_0096561549_p1082720181618"></a>Specifies the sticky session type.</p>
<div class="p" id="en-us_topic_0096561549_p79701533165"><a name="en-us_topic_0096561549_p79701533165"></a><a name="en-us_topic_0096561549_p79701533165"></a>The value can be one of the following:<a name="en-us_topic_0096561549_ul258091011289"></a><a name="en-us_topic_0096561549_ul258091011289"></a><ul id="en-us_topic_0096561549_ul258091011289"><li><strong id="en-us_topic_0096561549_b13160219163613"><a name="en-us_topic_0096561549_b13160219163613"></a><a name="en-us_topic_0096561549_b13160219163613"></a>SOURCE_IP</strong>: Requests are distributed based on the client's IP address. Requests from the same IP address are sent to the same backend server.</li><li><strong id="en-us_topic_0096561549_b13123122818366"><a name="en-us_topic_0096561549_b13123122818366"></a><a name="en-us_topic_0096561549_b13123122818366"></a>HTTP_COOKIE</strong>: When the client sends a request for the first time, the load balancer automatically generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to the backend server that processes the first request.</li><li><strong id="en-us_topic_0096561549_b9757628366"><a name="en-us_topic_0096561549_b9757628366"></a><a name="en-us_topic_0096561549_b9757628366"></a>APP_COOKIE</strong>: When the client sends a request for the first time, the backend server that receives the request generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to this backend server.</li></ul>
</div>
<p id="en-us_topic_0096561549_p1382521641612"><a name="en-us_topic_0096561549_p1382521641612"></a><a name="en-us_topic_0096561549_p1382521641612"></a>When the backend server group protocol is TCP, only <strong id="en-us_topic_0096561549_b9575159612"><a name="en-us_topic_0096561549_b9575159612"></a><a name="en-us_topic_0096561549_b9575159612"></a>SOURCE_IP</strong> takes effect. When the backend server group protocol is HTTP, <strong id="en-us_topic_0096561549_b1758181519614"><a name="en-us_topic_0096561549_b1758181519614"></a><a name="en-us_topic_0096561549_b1758181519614"></a>HTTP_COOKIE</strong> or <strong id="en-us_topic_0096561549_b45814151266"><a name="en-us_topic_0096561549_b45814151266"></a><a name="en-us_topic_0096561549_b45814151266"></a>APP_COOKIE</strong> take effect.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row765217429490"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p26521442114916"><a name="en-us_topic_0096561549_p26521442114916"></a><a name="en-us_topic_0096561549_p26521442114916"></a>cookie_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p16653174214493"><a name="en-us_topic_0096561549_p16653174214493"></a><a name="en-us_topic_0096561549_p16653174214493"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p1184122312164"><a name="en-us_topic_0096561549_p1184122312164"></a><a name="en-us_topic_0096561549_p1184122312164"></a>Specifies the cookie name.</p>
<p id="en-us_topic_0096561549_p8672254169"><a name="en-us_topic_0096561549_p8672254169"></a><a name="en-us_topic_0096561549_p8672254169"></a>This parameter is mandatory when the sticky session type is <strong id="en-us_topic_0096561549_b567882366"><a name="en-us_topic_0096561549_b567882366"></a><a name="en-us_topic_0096561549_b567882366"></a>APP_COOKIE</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row268634152316"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p1190604118422"><a name="en-us_topic_0096561549_p1190604118422"></a><a name="en-us_topic_0096561549_p1190604118422"></a>persistence_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p19102413425"><a name="en-us_topic_0096561549_p19102413425"></a><a name="en-us_topic_0096561549_p19102413425"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p31964815179"><a name="en-us_topic_0096561549_p31964815179"></a><a name="en-us_topic_0096561549_p31964815179"></a>Specifies the sticky session timeout duration in minutes.</p>
<p id="en-us_topic_0096561549_p18281115101717"><a name="en-us_topic_0096561549_p18281115101717"></a><a name="en-us_topic_0096561549_p18281115101717"></a>This parameter is invalid when <strong id="en-us_topic_0096561549_b20486547017"><a name="en-us_topic_0096561549_b20486547017"></a><a name="en-us_topic_0096561549_b20486547017"></a>type</strong> is set to <strong id="en-us_topic_0096561549_b7485541101"><a name="en-us_topic_0096561549_b7485541101"></a><a name="en-us_topic_0096561549_b7485541101"></a>APP_COOKIE</strong>.</p>
<a name="en-us_topic_0096561549_ul460616103285"></a><a name="en-us_topic_0096561549_ul460616103285"></a><ul id="en-us_topic_0096561549_ul460616103285"><li>Optional value ranges are as follows:<a name="en-us_topic_0096561549_ul19618201052818"></a><a name="en-us_topic_0096561549_ul19618201052818"></a><ul id="en-us_topic_0096561549_ul19618201052818"><li>When the protocol of the backend server group is TCP or UDP, the value ranges from <strong id="en-us_topic_0096561549_b58831904373"><a name="en-us_topic_0096561549_b58831904373"></a><a name="en-us_topic_0096561549_b58831904373"></a>1</strong> to <strong id="en-us_topic_0096561549_b2883005377"><a name="en-us_topic_0096561549_b2883005377"></a><a name="en-us_topic_0096561549_b2883005377"></a>60</strong>.</li><li>When the protocol of the backend server group is HTTP, the value ranges from <strong id="en-us_topic_0096561549_b12263162193715"><a name="en-us_topic_0096561549_b12263162193715"></a><a name="en-us_topic_0096561549_b12263162193715"></a>1</strong> to <strong id="en-us_topic_0096561549_b1226418233720"><a name="en-us_topic_0096561549_b1226418233720"></a><a name="en-us_topic_0096561549_b1226418233720"></a>1440</strong>.</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5** **pools\_links**  parameter description

<a name="table18892135113610"></a>
<table><thead align="left"><tr id="row1594616518360"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p190555213201"><a name="p190555213201"></a><a name="p190555213201"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p294618543619"><a name="p294618543619"></a><a name="p294618543619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="p195711706214"><a name="p195711706214"></a><a name="p195711706214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8946175123611"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1994665173617"><a name="p1994665173617"></a><a name="p1994665173617"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p494635183615"><a name="p494635183615"></a><a name="p494635183615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p44564735"><a name="p44564735"></a><a name="p44564735"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="row16946155113619"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p189462503615"><a name="p189462503615"></a><a name="p189462503615"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1946857365"><a name="p1946857365"></a><a name="p1946857365"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p85234211272"><a name="p85234211272"></a><a name="p85234211272"></a>Specifies the prompt of the previous or next page. The value can be <strong id="b84235270693044"><a name="b84235270693044"></a><a name="b84235270693044"></a>next</strong> or <strong id="b84235270693047"><a name="b84235270693047"></a><a name="b84235270693047"></a>previous</strong>.</p>
<a name="ul577082711719"></a><a name="ul577082711719"></a><ul id="ul577082711719"><li><strong id="b49763372820"><a name="b49763372820"></a><a name="b49763372820"></a>next</strong>: indicates the URL of the next page.</li><li><strong id="b1396221919287"><a name="b1396221919287"></a><a name="b1396221919287"></a>previous</strong>: indicates the URL of the previous page.</li></ul>
</td>
</tr>
</tbody>
</table>

## **Example**<a name="section159431734111419"></a>

-   Example request 1: Querying all backend server groups

    ```
    GET https://{Endpoint}/v2.0/lbaas/pools
    ```


-   Example response

    ```
    {
        "pools": [
            {
                "lb_algorithm": "SOURCE_IP",
                "protocol": "TCP",
                "description": "",
                "admin_state_up": true,
                "loadbalancers": [
                    {
                        "id": "07d28d4a-4899-40a3-a939-5d09d69019e1"
                    }
                ],
                "tenant_id": "1867112d054b427e808cc6096d8193a1",
     
                "session_persistence": null,
                "healthmonitor_id": null,
                "listeners": [
                    {
                        "id": "1b421c2d-7e78-4a78-9ee4-c8ccba41f15b"
                    }
                ],
                "members": [
                    {
                        "id": "88f9c079-29cb-435a-b98f-0c5c0b90c2bd"
                    },
                    {
                        "id": "2f4c9644-d5d2-4cf8-a3c0-944239a4f58c"
                    }
                ],
                "id": "3a9f50bb-f041-4eac-a117-82472d8a0007",
                "name": "my-pool"
            }
        ]
    }
    ```


-   Example request 2: Filtering backend server groups whose load balancing algorithm is  **SOURCE\_IP**

    ```
    GET https://{Endpoint}/v2.0/lbaas/pools
    ```


-   Example response 2

    ```
    {
        "pools": [
            {
                "lb_algorithm": "SOURCE_IP",
                "protocol": "TCP",
                "description": "",
                "admin_state_up": true,
                "loadbalancers": [
                    {
                        "id": "07d28d4a-4899-40a3-a939-5d09d69019e1"
                    }
                ],
                "tenant_id": "1867112d054b427e808cc6096d8193a1",
                "session_persistence": null,
                "healthmonitor_id": null,
                "listeners": [
                    {
                        "id": "1b421c2d-7e78-4a78-9ee4-c8ccba41f15b"
                    }
                ],
                "members": [
                    {
                        "id": "88f9c079-29cb-435a-b98f-0c5c0b90c2bd"
                    },
                    {
                        "id": "2f4c9644-d5d2-4cf8-a3c0-944239a4f58c"
                    }
                ],
                "id": "3a9f50bb-f041-4eac-a117-82472d8a0007",
                "name": "my-pool"
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0049139647_section50145164"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

