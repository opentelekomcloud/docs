# Querying All Policies<a name="EN-US_TOPIC_0193631159"></a>

## Function Description<a name="section28622093"></a>

This API is used to query the list of policies.

## URI<a name="section56272247"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy?policyname=\{policyname\}&offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table37883884"></a>
    <table><thead align="left"><tr id="row23757768"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45331073"><a name="p45331073"></a><a name="p45331073"></a><strong id="b2482145517489"><a name="b2482145517489"></a><a name="b2482145517489"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p47938266"><a name="p47938266"></a><a name="p47938266"></a><strong id="b1854525617485"><a name="b1854525617485"></a><a name="b1854525617485"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p57794299"><a name="p57794299"></a><a name="p57794299"></a><strong id="b1545275714486"><a name="b1545275714486"></a><a name="b1545275714486"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p50826637"><a name="p50826637"></a><a name="p50826637"></a><strong id="b10248958134815"><a name="b10248958134815"></a><a name="b10248958134815"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23316919"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p9622306"><a name="p9622306"></a><a name="p9622306"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41209334"><a name="p41209334"></a><a name="p41209334"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p49621721"><a name="p49621721"></a><a name="p49621721"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p59936502"><a name="p59936502"></a><a name="p59936502"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row11211381519"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42119389119"><a name="p42119389119"></a><a name="p42119389119"></a>policyname</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p9218381610"><a name="p9218381610"></a><a name="p9218381610"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p202103812118"><a name="p202103812118"></a><a name="p202103812118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p182119380119"><a name="p182119380119"></a><a name="p182119380119"></a>Specifies the policy name.</p>
    </td>
    </tr>
    <tr id="row11348153413310"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5348123414331"><a name="p5348123414331"></a><a name="p5348123414331"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p16348534203314"><a name="p16348534203314"></a><a name="p16348534203314"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p133481934113314"><a name="p133481934113314"></a><a name="p133481934113314"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b117610326338"><a name="b117610326338"></a><a name="b117610326338"></a>0</strong> to <strong id="b676118325331"><a name="b676118325331"></a><a name="b676118325331"></a>65535</strong>. The default value is <strong id="b137611324331"><a name="b137611324331"></a><a name="b137611324331"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row643410397338"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2043413395331"><a name="p2043413395331"></a><a name="p2043413395331"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p14344392332"><a name="p14344392332"></a><a name="p14344392332"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p14341539143310"><a name="p14341539143310"></a><a name="p14341539143310"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b922013353335"><a name="b922013353335"></a><a name="b922013353335"></a>0</strong> to <strong id="b2220535183314"><a name="b2220535183314"></a><a name="b2220535183314"></a>50</strong>. The default value is <strong id="b6220143518334"><a name="b6220143518334"></a><a name="b6220143518334"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36688176"></a>

Request parameters

None

## Response<a name="section61758129"></a>

Response parameters

**Table  2**  Parameter description

<a name="table29324718"></a>
<table><thead align="left"><tr id="row1824515"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p13568011"><a name="p13568011"></a><a name="p13568011"></a><strong id="b183191255133414"><a name="b183191255133414"></a><a name="b183191255133414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.889999999999997%" id="mcps1.2.4.1.2"><p id="p25267083"><a name="p25267083"></a><a name="p25267083"></a><strong id="b14490145610343"><a name="b14490145610343"></a><a name="b14490145610343"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.620000000000005%" id="mcps1.2.4.1.3"><p id="p33367852"><a name="p33367852"></a><a name="p33367852"></a><strong id="b15381857123414"><a name="b15381857123414"></a><a name="b15381857123414"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row31875216"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p31755717"><a name="p31755717"></a><a name="p31755717"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p22076270"><a name="p22076270"></a><a name="p22076270"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.620000000000005%" headers="mcps1.2.4.1.3 "><p id="p43347444"><a name="p43347444"></a><a name="p43347444"></a>Specifies the total number of policies.</p>
</td>
</tr>
<tr id="row54582677"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p59120688"><a name="p59120688"></a><a name="p59120688"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p24046428"><a name="p24046428"></a><a name="p24046428"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="48.620000000000005%" headers="mcps1.2.4.1.3 "><p id="p1603648"><a name="p1603648"></a><a name="p1603648"></a>Specifies the policy objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="24.317568243175682%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b1499244423911"><a name="b1499244423911"></a><a name="b1499244423911"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.44715528447155%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b1464347932"><a name="b1464347932"></a><a name="b1464347932"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.235276472352766%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b829091164210"><a name="b829091164210"></a><a name="b829091164210"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row194014521190"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p7293351101918"><a name="p7293351101918"></a><a name="p7293351101918"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p172941251111914"><a name="p172941251111914"></a><a name="p172941251111914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p18296155114199"><a name="p18296155114199"></a><a name="p18296155114199"></a>Specifies the instance ID.</p>
</td>
</tr>
<tr id="row14400165214191"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p16298451151910"><a name="p16298451151910"></a><a name="p16298451151910"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p10301145141917"><a name="p10301145141917"></a><a name="p10301145141917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p630115191919"><a name="p630115191919"></a><a name="p630115191919"></a>Specifies the policy name.</p>
</td>
</tr>
<tr id="row4399125231910"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p030425113191"><a name="p030425113191"></a><a name="p030425113191"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p230513514195"><a name="p230513514195"></a><a name="p230513514195"></a><a href="#table1272813819259">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p53051151171910"><a name="p53051151171910"></a><a name="p53051151171910"></a>Specifies whether a protection rule is enabled.</p>
</td>
</tr>
<tr id="row2039965210196"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p730815119192"><a name="p730815119192"></a><a name="p730815119192"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p113117519190"><a name="p113117519190"></a><a name="p113117519190"></a><a href="#table1231716412312">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p15312145131919"><a name="p15312145131919"></a><a name="p15312145131919"></a>Specifies the mode of Basic Web Protection.</p>
<a name="ul796714441001"></a><a name="ul796714441001"></a><ul id="ul796714441001"><li><span class="parmvalue" id="parmvalue159619421115"><a name="parmvalue159619421115"></a><a name="parmvalue159619421115"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue1516014017161"><a name="parmvalue1516014017161"></a><a name="parmvalue1516014017161"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
<tr id="row15398165221918"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p14314451101911"><a name="p14314451101911"></a><a name="p14314451101911"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p19315195115194"><a name="p19315195115194"></a><a name="p19315195115194"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p63171351161911"><a name="p63171351161911"></a><a name="p63171351161911"></a>Specifies the protection level.</p>
<a name="ul1581418916465"></a><a name="ul1581418916465"></a><ul id="ul1581418916465"><li><span class="parmvalue" id="parmvalue679391714614"><a name="parmvalue679391714614"></a><a name="parmvalue679391714614"></a><b>1</b></span>: low<p id="p2704173810911"><a name="p2704173810911"></a><a name="p2704173810911"></a>WAF detects wget, cURL, and more but does not detect XSS and command injection attacks in the header, so you may miss more vulnerabilities that in fact exist. If you find out that configured protection rules are affecting your services, adjust the protection level to <strong id="b9925740102218"><a name="b9925740102218"></a><a name="b9925740102218"></a>1</strong>.</p>
</li><li><span class="parmvalue" id="parmvalue182811934154613"><a name="parmvalue182811934154613"></a><a name="parmvalue182811934154613"></a><b>2</b></span>: medium<p id="p2954125761410"><a name="p2954125761410"></a><a name="p2954125761410"></a>By default, <strong id="b66847143116"><a name="b66847143116"></a><a name="b66847143116"></a>2</strong> is selected. In this level, WAF detects remote file inclusion, third-party software vulnerabilities, webshell, and cp and ftp commands.</p>
</li><li><span class="parmvalue" id="parmvalue161671854125317"><a name="parmvalue161671854125317"></a><a name="parmvalue161671854125317"></a><b>3</b></span>: high<p id="p1170119411103"><a name="p1170119411103"></a><a name="p1170119411103"></a>WAF detects Netcat, Nmap, kill commands, and more. If you need stricter protection, select <strong id="b12577117105015"><a name="b12577117105015"></a><a name="b12577117105015"></a>3</strong> to avoid unreported vulnerabilities but you may see more vulnerabilities that in fact unlikely exist.</p>
</li></ul>
</td>
</tr>
<tr id="row93971052141920"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p2032145161915"><a name="p2032145161915"></a><a name="p2032145161915"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p15324185118193"><a name="p15324185118193"></a><a name="p15324185118193"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p29333486463"><a name="p29333486463"></a><a name="p29333486463"></a>Specifies the detection mode in Precise Protection.</p>
<a name="ul38041853194616"></a><a name="ul38041853194616"></a><ul id="ul38041853194616"><li><strong id="b1755019491619"><a name="b1755019491619"></a><a name="b1755019491619"></a>true</strong>: full detection. Full detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.</li><li><strong id="b17686122792016"><a name="b17686122792016"></a><a name="b17686122792016"></a>false</strong>: instant detection. Instant detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.</li></ul>
</td>
</tr>
<tr id="row12397175219190"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p2033015513197"><a name="p2033015513197"></a><a name="p2033015513197"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p1333111513192"><a name="p1333111513192"></a><a name="p1333111513192"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p133317514190"><a name="p133317514190"></a><a name="p133317514190"></a>Specifies the domain IDs.</p>
</td>
</tr>
<tr id="row10396152101911"><td class="cellrowborder" valign="top" width="24.317568243175682%" headers="mcps1.2.4.1.1 "><p id="p1033511516193"><a name="p1033511516193"></a><a name="p1033511516193"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p7337551141917"><a name="p7337551141917"></a><a name="p7337551141917"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="47.235276472352766%" headers="mcps1.2.4.1.3 "><p id="p733813519190"><a name="p733813519190"></a><a name="p733813519190"></a>Specifies the time when a policy is created.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **options**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b103701112153414"><a name="b103701112153414"></a><a name="b103701112153414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b51471089"><a name="b51471089"></a><a name="b51471089"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b03231114173410"><a name="b03231114173410"></a><a name="b03231114173410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177747172812"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p33504133"><a name="p33504133"></a><a name="p33504133"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p29480242"><a name="p29480242"></a><a name="p29480242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p2415193218263"><a name="p2415193218263"></a><a name="p2415193218263"></a>Specifies whether Basic Web Protection is enabled.</p>
<a name="ul1778444132612"></a><a name="ul1778444132612"></a><ul id="ul1778444132612"><li><strong id="b54581648130"><a name="b54581648130"></a><a name="b54581648130"></a>true</strong>: enabled.</li><li><strong id="b334971114131"><a name="b334971114131"></a><a name="b334971114131"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1577720732819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p42476939"><a name="p42476939"></a><a name="p42476939"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p18080074"><a name="p18080074"></a><a name="p18080074"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p8672433268"><a name="p8672433268"></a><a name="p8672433268"></a>Specifies whether General Check in Basic Web Protection is enabled.</p>
<a name="ul4842171218268"></a><a name="ul4842171218268"></a><ul id="ul4842171218268"><li><strong id="b288694691319"><a name="b288694691319"></a><a name="b288694691319"></a>true</strong>: enabled.</li><li><strong id="b1646225071312"><a name="b1646225071312"></a><a name="b1646225071312"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row8777157112811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p47260058"><a name="p47260058"></a><a name="p47260058"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2859499"><a name="p2859499"></a><a name="p2859499"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p825744922615"><a name="p825744922615"></a><a name="p825744922615"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled.</p>
<a name="ul2993535262"></a><a name="ul2993535262"></a><ul id="ul2993535262"><li><strong id="b146041519171410"><a name="b146041519171410"></a><a name="b146041519171410"></a>true</strong>: enabled.</li><li><strong id="b18213235142"><a name="b18213235142"></a><a name="b18213235142"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177515762814"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p42166705"><a name="p42166705"></a><a name="p42166705"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p60059924"><a name="p60059924"></a><a name="p60059924"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1718417589268"><a name="p1718417589268"></a><a name="p1718417589268"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled.</p>
<a name="ul172713111276"></a><a name="ul172713111276"></a><ul id="ul172713111276"><li><strong id="b9432945171419"><a name="b9432945171419"></a><a name="b9432945171419"></a>true</strong>: enabled.</li><li><strong id="b47998487142"><a name="b47998487142"></a><a name="b47998487142"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177751776289"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p55359439"><a name="p55359439"></a><a name="p55359439"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p54929604"><a name="p54929604"></a><a name="p54929604"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p20112962"><a name="p20112962"></a><a name="p20112962"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled.</p>
<a name="ul851114810278"></a><a name="ul851114810278"></a><ul id="ul851114810278"><li><strong id="b75571644161511"><a name="b75571644161511"></a><a name="b75571644161511"></a>true</strong>: enabled.</li><li><strong id="b13881151121514"><a name="b13881151121514"></a><a name="b13881151121514"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177577172811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p25118198"><a name="p25118198"></a><a name="p25118198"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21308157"><a name="p21308157"></a><a name="p21308157"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p48239148"><a name="p48239148"></a><a name="p48239148"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled.</p>
<a name="ul1296981219278"></a><a name="ul1296981219278"></a><ul id="ul1296981219278"><li><strong id="b26179159164"><a name="b26179159164"></a><a name="b26179159164"></a>true</strong>: enabled.</li><li><strong id="b193422199167"><a name="b193422199167"></a><a name="b193422199167"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1773576281"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p11652645"><a name="p11652645"></a><a name="p11652645"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p4340158"><a name="p4340158"></a><a name="p4340158"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16008479"><a name="p16008479"></a><a name="p16008479"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled.</p>
<a name="ul8824161782711"></a><a name="ul8824161782711"></a><ul id="ul8824161782711"><li><strong id="b186981542191619"><a name="b186981542191619"></a><a name="b186981542191619"></a>true</strong>: enabled.</li><li><strong id="b058004671610"><a name="b058004671610"></a><a name="b058004671610"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177357102817"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6261339"><a name="p6261339"></a><a name="p6261339"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p37406470"><a name="p37406470"></a><a name="p37406470"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10025242"><a name="p10025242"></a><a name="p10025242"></a>Specifies whether webshell detection in Basic Web Protection is enabled.</p>
<a name="ul20574202914279"></a><a name="ul20574202914279"></a><ul id="ul20574202914279"><li><strong id="b66691125176"><a name="b66691125176"></a><a name="b66691125176"></a>true</strong>: enabled.</li><li><strong id="b1429131619175"><a name="b1429131619175"></a><a name="b1429131619175"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row47721722816"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p8926362"><a name="p8926362"></a><a name="p8926362"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p51946711"><a name="p51946711"></a><a name="p51946711"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p46934044"><a name="p46934044"></a><a name="p46934044"></a>Specifies whether CC Attack Protection is enabled.</p>
<a name="ul8527033142710"></a><a name="ul8527033142710"></a><ul id="ul8527033142710"><li><strong id="b126301931141717"><a name="b126301931141717"></a><a name="b126301931141717"></a>true</strong>: enabled.</li><li><strong id="b10708137151720"><a name="b10708137151720"></a><a name="b10708137151720"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1977218711283"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p38799072"><a name="p38799072"></a><a name="p38799072"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p55717167"><a name="p55717167"></a><a name="p55717167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16796711"><a name="p16796711"></a><a name="p16796711"></a>Specifies whether Precise Protection is enabled.</p>
<a name="ul1043194117270"></a><a name="ul1043194117270"></a><ul id="ul1043194117270"><li><strong id="b19858155619174"><a name="b19858155619174"></a><a name="b19858155619174"></a>true</strong>: enabled.</li><li><strong id="b15460120111811"><a name="b15460120111811"></a><a name="b15460120111811"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row97728782819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p10468143"><a name="p10468143"></a><a name="p10468143"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p42613264"><a name="p42613264"></a><a name="p42613264"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p29122361"><a name="p29122361"></a><a name="p29122361"></a>Specifies whether Blacklist and Whitelist is enabled.</p>
<a name="ul1621718455274"></a><a name="ul1621718455274"></a><ul id="ul1621718455274"><li><strong id="b10631111615186"><a name="b10631111615186"></a><a name="b10631111615186"></a>true</strong>: enabled.</li><li><strong id="b129671319131820"><a name="b129671319131820"></a><a name="b129671319131820"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row10772157172818"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p51392996"><a name="p51392996"></a><a name="p51392996"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2083177"><a name="p2083177"></a><a name="p2083177"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p34519671"><a name="p34519671"></a><a name="p34519671"></a>Specifies whether Data Masking is enabled.</p>
<a name="ul2712175332710"></a><a name="ul2712175332710"></a><ul id="ul2712175332710"><li><strong id="b6452335189"><a name="b6452335189"></a><a name="b6452335189"></a>true</strong>: enabled.</li><li><strong id="b765412362186"><a name="b765412362186"></a><a name="b765412362186"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row14770678287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p58255435"><a name="p58255435"></a><a name="p58255435"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21069794"><a name="p21069794"></a><a name="p21069794"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p28931745"><a name="p28931745"></a><a name="p28931745"></a>Specifies whether False Alarm Masking is enabled.</p>
<a name="ul1371357192720"></a><a name="ul1371357192720"></a><ul id="ul1371357192720"><li><strong id="b15443134613184"><a name="b15443134613184"></a><a name="b15443134613184"></a>true</strong>: enabled.</li><li><strong id="b871624911820"><a name="b871624911820"></a><a name="b871624911820"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row167707717287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p37316794"><a name="p37316794"></a><a name="p37316794"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2761443"><a name="p2761443"></a><a name="p2761443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p22350292"><a name="p22350292"></a><a name="p22350292"></a>Specifies whether Web Tamper Protection is enabled.</p>
<a name="ul5509133182819"></a><a name="ul5509133182819"></a><ul id="ul5509133182819"><li><strong id="b1049758141814"><a name="b1049758141814"></a><a name="b1049758141814"></a>true</strong>: enabled.</li><li><strong id="b1158001141914"><a name="b1158001141914"></a><a name="b1158001141914"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5** **action**

<a name="table1231716412312"></a>
<table><thead align="left"><tr id="row153241848236"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1532615432319"><a name="p1532615432319"></a><a name="p1532615432319"></a><strong id="b1843092017"><a name="b1843092017"></a><a name="b1843092017"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p333054192311"><a name="p333054192311"></a><a name="p333054192311"></a><strong id="b1597955974"><a name="b1597955974"></a><a name="b1597955974"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p193322492311"><a name="p193322492311"></a><a name="p193322492311"></a><strong id="b607660346"><a name="b607660346"></a><a name="b607660346"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19763216142319"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1576317163239"><a name="p1576317163239"></a><a name="p1576317163239"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p117631516182318"><a name="p117631516182318"></a><a name="p117631516182318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p676312167234"><a name="p676312167234"></a><a name="p676312167234"></a>Specifies the mode of Basic Web Protection.</p>
<a name="ul1638352216361"></a><a name="ul1638352216361"></a><ul id="ul1638352216361"><li><span class="parmvalue" id="parmvalue103251837112518"><a name="parmvalue103251837112518"></a><a name="parmvalue103251837112518"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue577183311619"><a name="parmvalue577183311619"></a><a name="parmvalue577183311619"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section145741224193916"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
    "total": 2,
    "items": [
        {
          "id": "xxxxxxxxxxxxxxxxxxxxxxxxx",
          "name": "policy_1",
          "action": {
              "category ": "block"
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
           "hosts": ["11111111111111111", "2222222222222222222"],
           "timestamp": 1499817612
        }, {
          "id": "xxxxxxxxxxxxxxxxxxxxxxxxx",
          "name": "policy_2",
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
           "hosts": ["11111111111111111", "2222222222222222222"],
           "timestamp": 1499817612
        }
     ]
}

```

## Status Code<a name="section18952251"></a>

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

