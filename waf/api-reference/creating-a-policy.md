# Creating a Policy<a name="EN-US_TOPIC_0193631153"></a>

## Function Description<a name="section36087531"></a>

This API is used to create a policy.

## URI<a name="section56352327"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy

-   Parameter description

    **Table  1**  Path parameters

    <a name="table38977416"></a>
    <table><thead align="left"><tr id="row23967586"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p62326351"><a name="p62326351"></a><a name="p62326351"></a><strong id="b1395672019421"><a name="b1395672019421"></a><a name="b1395672019421"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p15269660"><a name="p15269660"></a><a name="p15269660"></a><strong id="b118925227429"><a name="b118925227429"></a><a name="b118925227429"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p28882929"><a name="p28882929"></a><a name="p28882929"></a><strong id="b179558232421"><a name="b179558232421"></a><a name="b179558232421"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p57815927"><a name="p57815927"></a><a name="p57815927"></a><strong id="b171782584215"><a name="b171782584215"></a><a name="b171782584215"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52578517"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p31001524"><a name="p31001524"></a><a name="p31001524"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p28095548"><a name="p28095548"></a><a name="p28095548"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p61146900"><a name="p61146900"></a><a name="p61146900"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p53951844"><a name="p53951844"></a><a name="p53951844"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section37408898"></a>

Request parameters

**Table  2**  Parameter description

<a name="table45903758"></a>
<table><thead align="left"><tr id="row10772591"><th class="cellrowborder" valign="top" width="26.52734726527347%" id="mcps1.2.5.1.1"><p id="p164661"><a name="p164661"></a><a name="p164661"></a><strong id="b7337434124216"><a name="b7337434124216"></a><a name="b7337434124216"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.2"><p id="p13337617"><a name="p13337617"></a><a name="p13337617"></a><strong id="b8180236154215"><a name="b8180236154215"></a><a name="b8180236154215"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p6605160"><a name="p6605160"></a><a name="p6605160"></a><strong id="b0399153704213"><a name="b0399153704213"></a><a name="b0399153704213"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p65255972"><a name="p65255972"></a><a name="p65255972"></a><strong id="b1968114443421"><a name="b1968114443421"></a><a name="b1968114443421"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row51242413"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p56994794"><a name="p56994794"></a><a name="p56994794"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p53175620"><a name="p53175620"></a><a name="p53175620"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p12257954"><a name="p12257954"></a><a name="p12257954"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p53370221"><a name="p53370221"></a><a name="p53370221"></a>Specifies the policy name. The maximum length is 256 characters. Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1135765"></a>

Response parameters

**Table  3**  Parameter description

<a name="table32111592"></a>
<table><thead align="left"><tr id="row35186131"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p31504373"><a name="p31504373"></a><a name="p31504373"></a><strong id="b1796265564210"><a name="b1796265564210"></a><a name="b1796265564210"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p1717444"><a name="p1717444"></a><a name="p1717444"></a><strong id="b38371056194211"><a name="b38371056194211"></a><a name="b38371056194211"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p4895271"><a name="p4895271"></a><a name="p4895271"></a><strong id="b441525834215"><a name="b441525834215"></a><a name="b441525834215"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row44057444"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p11883201"><a name="p11883201"></a><a name="p11883201"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p23015206"><a name="p23015206"></a><a name="p23015206"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p52292412"><a name="p52292412"></a><a name="p52292412"></a>Specifies the instance ID.</p>
</td>
</tr>
<tr id="row869665"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p3334018"><a name="p3334018"></a><a name="p3334018"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p1620073"><a name="p1620073"></a><a name="p1620073"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p64117051"><a name="p64117051"></a><a name="p64117051"></a>Specifies the policy name.</p>
</td>
</tr>
<tr id="row40182553"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p33561337"><a name="p33561337"></a><a name="p33561337"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p34113786"><a name="p34113786"></a><a name="p34113786"></a><a href="#table1272813819259">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p53051151171910"><a name="p53051151171910"></a><a name="p53051151171910"></a>Specifies whether a protection rule is enabled.</p>
</td>
</tr>
<tr id="row38670691"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p45318252"><a name="p45318252"></a><a name="p45318252"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p46899794"><a name="p46899794"></a><a name="p46899794"></a><a href="#table1231716412312">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p40786940"><a name="p40786940"></a><a name="p40786940"></a>Specifies the mode of Basic Web Protection. The default value is <strong id="b54379299012"><a name="b54379299012"></a><a name="b54379299012"></a>log</strong>.</p>
<a name="ul796714441001"></a><a name="ul796714441001"></a><ul id="ul796714441001"><li><span class="parmvalue" id="parmvalue1930613911303"><a name="parmvalue1930613911303"></a><a name="parmvalue1930613911303"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue17791124503213"><a name="parmvalue17791124503213"></a><a name="parmvalue17791124503213"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
<tr id="row31538142"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p4452714"><a name="p4452714"></a><a name="p4452714"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p25125550"><a name="p25125550"></a><a name="p25125550"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p834117720118"><a name="p834117720118"></a><a name="p834117720118"></a>Specifies the protection level.</p>
<a name="ul14573610126"></a><a name="ul14573610126"></a><ul id="ul14573610126"><li><span class="parmvalue" id="parmvalue125051145122118"><a name="parmvalue125051145122118"></a><a name="parmvalue125051145122118"></a><b>1</b></span>: low</li><li><span class="parmvalue" id="parmvalue0716114852113"><a name="parmvalue0716114852113"></a><a name="parmvalue0716114852113"></a><b>2</b></span>: medium</li><li><span class="parmvalue" id="parmvalue7398135211218"><a name="parmvalue7398135211218"></a><a name="parmvalue7398135211218"></a><b>3</b></span>: high</li></ul>
</td>
</tr>
<tr id="row62915569"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p62996362"><a name="p62996362"></a><a name="p62996362"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p2431703"><a name="p2431703"></a><a name="p2431703"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p18194437725"><a name="p18194437725"></a><a name="p18194437725"></a>Specifies the detection mode in Precise Protection.</p>
</td>
</tr>
<tr id="row27881548"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p43812907"><a name="p43812907"></a><a name="p43812907"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p59184603"><a name="p59184603"></a><a name="p59184603"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p29223556"><a name="p29223556"></a><a name="p29223556"></a>Specifies the domain IDs.</p>
</td>
</tr>
<tr id="row61685413"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p30462517"><a name="p30462517"></a><a name="p30462517"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p51544785"><a name="p51544785"></a><a name="p51544785"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p14378082"><a name="p14378082"></a><a name="p14378082"></a>Specifies the time when a policy is created.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **options**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b1694619039"><a name="b1694619039"></a><a name="b1694619039"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b1712272147"><a name="b1712272147"></a><a name="b1712272147"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b237077364"><a name="b237077364"></a><a name="b237077364"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177747172812"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p33504133"><a name="p33504133"></a><a name="p33504133"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p29480242"><a name="p29480242"></a><a name="p29480242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p2415193218263"><a name="p2415193218263"></a><a name="p2415193218263"></a>Specifies whether Basic Web Protection is enabled. By default, this function is enabled.</p>
<a name="ul1778444132612"></a><a name="ul1778444132612"></a><ul id="ul1778444132612"><li><strong id="b103131014234"><a name="b103131014234"></a><a name="b103131014234"></a>true</strong>: enabled.</li><li><strong id="b1954741362319"><a name="b1954741362319"></a><a name="b1954741362319"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1577720732819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p42476939"><a name="p42476939"></a><a name="p42476939"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p18080074"><a name="p18080074"></a><a name="p18080074"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p8672433268"><a name="p8672433268"></a><a name="p8672433268"></a>Specifies whether General Check in Basic Web Protection is enabled. By default, this function is enabled.</p>
<a name="ul4842171218268"></a><a name="ul4842171218268"></a><ul id="ul4842171218268"><li><strong id="b6741152452311"><a name="b6741152452311"></a><a name="b6741152452311"></a>true</strong>: enabled.</li><li><strong id="b1070132812236"><a name="b1070132812236"></a><a name="b1070132812236"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row8777157112811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p47260058"><a name="p47260058"></a><a name="p47260058"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2859499"><a name="p2859499"></a><a name="p2859499"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p825744922615"><a name="p825744922615"></a><a name="p825744922615"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled. By default, this function is enabled.</p>
<a name="ul2993535262"></a><a name="ul2993535262"></a><ul id="ul2993535262"><li><strong id="b682853652311"><a name="b682853652311"></a><a name="b682853652311"></a>true</strong>: enabled.</li><li><strong id="b112811940192314"><a name="b112811940192314"></a><a name="b112811940192314"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177515762814"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p42166705"><a name="p42166705"></a><a name="p42166705"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p60059924"><a name="p60059924"></a><a name="p60059924"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1718417589268"><a name="p1718417589268"></a><a name="p1718417589268"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled. By default, this function is disabled.</p>
<a name="ul172713111276"></a><a name="ul172713111276"></a><ul id="ul172713111276"><li><strong id="b31444814232"><a name="b31444814232"></a><a name="b31444814232"></a>true</strong>: enabled.</li><li><strong id="b141321751132310"><a name="b141321751132310"></a><a name="b141321751132310"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177751776289"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p55359439"><a name="p55359439"></a><a name="p55359439"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p54929604"><a name="p54929604"></a><a name="p54929604"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p20112962"><a name="p20112962"></a><a name="p20112962"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled. By default, this function is enabled.</p>
<a name="ul851114810278"></a><a name="ul851114810278"></a><ul id="ul851114810278"><li><strong id="b6559460241"><a name="b6559460241"></a><a name="b6559460241"></a>true</strong>: enabled.</li><li><strong id="b767579192419"><a name="b767579192419"></a><a name="b767579192419"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177577172811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p25118198"><a name="p25118198"></a><a name="p25118198"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21308157"><a name="p21308157"></a><a name="p21308157"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p48239148"><a name="p48239148"></a><a name="p48239148"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled. By default, this function is disabled.</p>
<a name="ul1296981219278"></a><a name="ul1296981219278"></a><ul id="ul1296981219278"><li><strong id="b19932163315246"><a name="b19932163315246"></a><a name="b19932163315246"></a>true</strong>: enabled.</li><li><strong id="b161438376244"><a name="b161438376244"></a><a name="b161438376244"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1773576281"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p11652645"><a name="p11652645"></a><a name="p11652645"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p4340158"><a name="p4340158"></a><a name="p4340158"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16008479"><a name="p16008479"></a><a name="p16008479"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled. By default, this function is disabled.</p>
<a name="ul8824161782711"></a><a name="ul8824161782711"></a><ul id="ul8824161782711"><li><strong id="b208542465242"><a name="b208542465242"></a><a name="b208542465242"></a>true</strong>: enabled.</li><li><strong id="b19283650192418"><a name="b19283650192418"></a><a name="b19283650192418"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177357102817"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6261339"><a name="p6261339"></a><a name="p6261339"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p37406470"><a name="p37406470"></a><a name="p37406470"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10025242"><a name="p10025242"></a><a name="p10025242"></a>Specifies whether webshell detection in Basic Web Protection is enabled. By default, this function is disabled.</p>
<a name="ul20574202914279"></a><a name="ul20574202914279"></a><ul id="ul20574202914279"><li><strong id="b188347592248"><a name="b188347592248"></a><a name="b188347592248"></a>true</strong>: enabled.</li><li><strong id="b57959310259"><a name="b57959310259"></a><a name="b57959310259"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row47721722816"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p8926362"><a name="p8926362"></a><a name="p8926362"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p51946711"><a name="p51946711"></a><a name="p51946711"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p46934044"><a name="p46934044"></a><a name="p46934044"></a>Specifies whether CC Attack Protection is enabled. By default, this function is enabled.</p>
<a name="ul8527033142710"></a><a name="ul8527033142710"></a><ul id="ul8527033142710"><li><strong id="b749112239257"><a name="b749112239257"></a><a name="b749112239257"></a>true</strong>: enabled.</li><li><strong id="b61515271259"><a name="b61515271259"></a><a name="b61515271259"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1977218711283"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p38799072"><a name="p38799072"></a><a name="p38799072"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p55717167"><a name="p55717167"></a><a name="p55717167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16796711"><a name="p16796711"></a><a name="p16796711"></a>Specifies whether Precise Protection is enabled. By default, this function is enabled.</p>
<a name="ul1043194117270"></a><a name="ul1043194117270"></a><ul id="ul1043194117270"><li><strong id="b2538153512519"><a name="b2538153512519"></a><a name="b2538153512519"></a>true</strong>: enabled.</li><li><strong id="b10913113813251"><a name="b10913113813251"></a><a name="b10913113813251"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row97728782819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p10468143"><a name="p10468143"></a><a name="p10468143"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p42613264"><a name="p42613264"></a><a name="p42613264"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p29122361"><a name="p29122361"></a><a name="p29122361"></a>Specifies whether Blacklist and Whitelist is enabled. By default, this function is enabled.</p>
<a name="ul1621718455274"></a><a name="ul1621718455274"></a><ul id="ul1621718455274"><li><strong id="b1982124832515"><a name="b1982124832515"></a><a name="b1982124832515"></a>true</strong>: enabled.</li><li><strong id="b14960165132512"><a name="b14960165132512"></a><a name="b14960165132512"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row10772157172818"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p51392996"><a name="p51392996"></a><a name="p51392996"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2083177"><a name="p2083177"></a><a name="p2083177"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p34519671"><a name="p34519671"></a><a name="p34519671"></a>Specifies whether Data Masking is enabled. By default, this function is enabled.</p>
<a name="ul2712175332710"></a><a name="ul2712175332710"></a><ul id="ul2712175332710"><li><strong id="b96825042617"><a name="b96825042617"></a><a name="b96825042617"></a>true</strong>: enabled.</li><li><strong id="b182717442618"><a name="b182717442618"></a><a name="b182717442618"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row14770678287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p58255435"><a name="p58255435"></a><a name="p58255435"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21069794"><a name="p21069794"></a><a name="p21069794"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p28931745"><a name="p28931745"></a><a name="p28931745"></a>Specifies whether False Alarm Masking is enabled. By default, this function is enabled.</p>
<a name="ul1371357192720"></a><a name="ul1371357192720"></a><ul id="ul1371357192720"><li><strong id="b8714191492620"><a name="b8714191492620"></a><a name="b8714191492620"></a>true</strong>: enabled.</li><li><strong id="b109641802612"><a name="b109641802612"></a><a name="b109641802612"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row167707717287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p37316794"><a name="p37316794"></a><a name="p37316794"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2761443"><a name="p2761443"></a><a name="p2761443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p22350292"><a name="p22350292"></a><a name="p22350292"></a>Specifies whether Web Tamper Protection is enabled. By default, this function is enabled.</p>
<a name="ul5509133182819"></a><a name="ul5509133182819"></a><ul id="ul5509133182819"><li><strong id="b19113192617266"><a name="b19113192617266"></a><a name="b19113192617266"></a>true</strong>: enabled.</li><li><strong id="b175932902614"><a name="b175932902614"></a><a name="b175932902614"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5** **action**

<a name="table1231716412312"></a>
<table><thead align="left"><tr id="row153241848236"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1532615432319"><a name="p1532615432319"></a><a name="p1532615432319"></a><strong id="b355493105"><a name="b355493105"></a><a name="b355493105"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p333054192311"><a name="p333054192311"></a><a name="p333054192311"></a><strong id="b1086898617"><a name="b1086898617"></a><a name="b1086898617"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p193322492311"><a name="p193322492311"></a><a name="p193322492311"></a><strong id="b159911468"><a name="b159911468"></a><a name="b159911468"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19763216142319"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1576317163239"><a name="p1576317163239"></a><a name="p1576317163239"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p117631516182318"><a name="p117631516182318"></a><a name="p117631516182318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p676312167234"><a name="p676312167234"></a><a name="p676312167234"></a>Specifies the mode of Basic Web Protection. The default value is <strong id="b1978312016217"><a name="b1978312016217"></a><a name="b1978312016217"></a>log</strong>.</p>
<a name="ul1133117412364"></a><a name="ul1133117412364"></a><ul id="ul1133117412364"><li><span class="parmvalue" id="parmvalue18902142662620"><a name="parmvalue18902142662620"></a><a name="parmvalue18902142662620"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue313811433316"><a name="parmvalue313811433316"></a><a name="parmvalue313811433316"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section10449017401"></a>

A policy named  **policy\_1**  is used as an example.

-   Request example

    ```
    {
      "name": "policy_1"
    }
    ```


-   Response example

    ```
    {
              "id": "xxxxxxxxxxxxxxxxxxxxxxxxx",
              "name": "policy_1",
              "action": {
                  "category": "block"
               },
               "options": {
                   "webattack": true,
                   "common": true,
                   "crawler": true,
                   "crawler_engine": true,
                   "crawler_scanner": true,
                   "crawler_script": true,
                   "crawler_other": true,
                   "webshell": true,
                   "cc": true,
                   "custom": true,
                   "whiteblackip": true,
                   "ignore": true,
                   "privacy": true,
                   "antitamper": true
                },
               "level": 1,
               "full_detection": false,
               "hosts": [],
               "timestamp": 1499817612
    }
    ```


## Status Code<a name="section10221889"></a>

[Table 6](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  6**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

