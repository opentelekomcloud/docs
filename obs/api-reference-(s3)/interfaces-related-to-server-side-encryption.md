# Interfaces Related to Server-Side Encryption<a name="EN-US_TOPIC_0125560285"></a>

This section lists the interfaces related to server-side encryption and describes transfer protocols and authentication applicable to the interfaces.

The following tables describe transfer protocols and authentication applicable to the interfaces related to server-side encryption.

**Table  1**  Transfer protocols and authentication applicable to SSE-C-related interfaces

<a name="table23204599113657"></a>
<table><thead align="left"><tr id="row26797416113657"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p23107077113657"><a name="p23107077113657"></a><a name="p23107077113657"></a>Interface</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p59733930113657"><a name="p59733930113657"></a><a name="p59733930113657"></a>Transfer Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6610176113657"><a name="p6610176113657"></a><a name="p6610176113657"></a>Authentication</p>
</th>
</tr>
</thead>
<tbody><tr id="row65662254113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17042397113657"><a name="p17042397113657"></a><a name="p17042397113657"></a>PUT Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p38256949113657"><a name="p38256949113657"></a><a name="p38256949113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11805149113657"><a name="p11805149113657"></a><a name="p11805149113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row39137478113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16019178113657"><a name="p16019178113657"></a><a name="p16019178113657"></a>POST Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p22485042113657"><a name="p22485042113657"></a><a name="p22485042113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9349127113657"><a name="p9349127113657"></a><a name="p9349127113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row17033281113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37518548113657"><a name="p37518548113657"></a><a name="p37518548113657"></a>Initiate Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19103527113657"><a name="p19103527113657"></a><a name="p19103527113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3881826113657"><a name="p3881826113657"></a><a name="p3881826113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row34936438113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11279266113657"><a name="p11279266113657"></a><a name="p11279266113657"></a>HEAD Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41205321113657"><a name="p41205321113657"></a><a name="p41205321113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49296725113657"><a name="p49296725113657"></a><a name="p49296725113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row41017349113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p34070947113657"><a name="p34070947113657"></a><a name="p34070947113657"></a>GET Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8283289113657"><a name="p8283289113657"></a><a name="p8283289113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66966672113657"><a name="p66966672113657"></a><a name="p66966672113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row65829139113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30560046113657"><a name="p30560046113657"></a><a name="p30560046113657"></a>Upload Part</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p59444637113657"><a name="p59444637113657"></a><a name="p59444637113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p50286281113657"><a name="p50286281113657"></a><a name="p50286281113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row49923345113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17259106113657"><a name="p17259106113657"></a><a name="p17259106113657"></a>Complete Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55810340113657"><a name="p55810340113657"></a><a name="p55810340113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p24343678113657"><a name="p24343678113657"></a><a name="p24343678113657"></a>V2 or V4</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Transfer protocols and authentication applicable to SSE-KMS-related interfaces

<a name="table25680921113657"></a>
<table><thead align="left"><tr id="row20607080113657"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p58560764113657"><a name="p58560764113657"></a><a name="p58560764113657"></a>Interface</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p20431013114142"><a name="p20431013114142"></a><a name="p20431013114142"></a>Transfer Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18928882113657"><a name="p18928882113657"></a><a name="p18928882113657"></a>Authentication</p>
</th>
</tr>
</thead>
<tbody><tr id="row56844451113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p40997850113657"><a name="p40997850113657"></a><a name="p40997850113657"></a>PUT Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32491516113657"><a name="p32491516113657"></a><a name="p32491516113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14567155113657"><a name="p14567155113657"></a><a name="p14567155113657"></a>V4</p>
</td>
</tr>
<tr id="row63995538113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16256099113657"><a name="p16256099113657"></a><a name="p16256099113657"></a>POST Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41675644113657"><a name="p41675644113657"></a><a name="p41675644113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p20284038113657"><a name="p20284038113657"></a><a name="p20284038113657"></a>V4</p>
</td>
</tr>
<tr id="row48338621113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23114227113657"><a name="p23114227113657"></a><a name="p23114227113657"></a>Initiate Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60313069113657"><a name="p60313069113657"></a><a name="p60313069113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53520403113657"><a name="p53520403113657"></a><a name="p53520403113657"></a>V4</p>
</td>
</tr>
<tr id="row11921587113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26124487113657"><a name="p26124487113657"></a><a name="p26124487113657"></a>HEAD Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35708732113657"><a name="p35708732113657"></a><a name="p35708732113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6726202113657"><a name="p6726202113657"></a><a name="p6726202113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row60535819113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4454312113657"><a name="p4454312113657"></a><a name="p4454312113657"></a>GET Object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25255010113657"><a name="p25255010113657"></a><a name="p25255010113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32389920113657"><a name="p32389920113657"></a><a name="p32389920113657"></a>V4</p>
</td>
</tr>
<tr id="row23073828113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57040804113657"><a name="p57040804113657"></a><a name="p57040804113657"></a>Upload Part</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56902429113657"><a name="p56902429113657"></a><a name="p56902429113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p45694006113657"><a name="p45694006113657"></a><a name="p45694006113657"></a>V4</p>
</td>
</tr>
<tr id="row8592870113657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24933842113657"><a name="p24933842113657"></a><a name="p24933842113657"></a>Complete Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6375347113657"><a name="p6375347113657"></a><a name="p6375347113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46641137113657"><a name="p46641137113657"></a><a name="p46641137113657"></a>V2 or V4</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Transfer protocols and authentication applicable to PUT Object - Copy interfaces

<a name="table19835763113657"></a>
<table><thead align="left"><tr id="row59346377113657"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p42327226113657"><a name="p42327226113657"></a><a name="p42327226113657"></a>Source Object</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p5953247113657"><a name="p5953247113657"></a><a name="p5953247113657"></a>Target Object</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p7830834114146"><a name="p7830834114146"></a><a name="p7830834114146"></a>Transfer Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1896167113657"><a name="p1896167113657"></a><a name="p1896167113657"></a>Authentication</p>
</th>
</tr>
</thead>
<tbody><tr id="row19371801113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25612064113657"><a name="p25612064113657"></a><a name="p25612064113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p61311332113657"><a name="p61311332113657"></a><a name="p61311332113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p161996113657"><a name="p161996113657"></a><a name="p161996113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13121729113657"><a name="p13121729113657"></a><a name="p13121729113657"></a>V4</p>
</td>
</tr>
<tr id="row50986699113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p36281982113657"><a name="p36281982113657"></a><a name="p36281982113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p53159409113657"><a name="p53159409113657"></a><a name="p53159409113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p10944844113657"><a name="p10944844113657"></a><a name="p10944844113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14117176113657"><a name="p14117176113657"></a><a name="p14117176113657"></a>V4</p>
</td>
</tr>
<tr id="row59945724113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p23765443113657"><a name="p23765443113657"></a><a name="p23765443113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p45952751113657"><a name="p45952751113657"></a><a name="p45952751113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p31185384113657"><a name="p31185384113657"></a><a name="p31185384113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p42988181113657"><a name="p42988181113657"></a><a name="p42988181113657"></a>V4</p>
</td>
</tr>
<tr id="row51349315113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p65653850113657"><a name="p65653850113657"></a><a name="p65653850113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p16361625113657"><a name="p16361625113657"></a><a name="p16361625113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p50223273113657"><a name="p50223273113657"></a><a name="p50223273113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p41553330113657"><a name="p41553330113657"></a><a name="p41553330113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row38435651113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p26279987113657"><a name="p26279987113657"></a><a name="p26279987113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p48304175113657"><a name="p48304175113657"></a><a name="p48304175113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p20324128113657"><a name="p20324128113657"></a><a name="p20324128113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p35641710113657"><a name="p35641710113657"></a><a name="p35641710113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row52339939113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11676679113657"><a name="p11676679113657"></a><a name="p11676679113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6286906113657"><a name="p6286906113657"></a><a name="p6286906113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p39477415113657"><a name="p39477415113657"></a><a name="p39477415113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p43554036113657"><a name="p43554036113657"></a><a name="p43554036113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row56442006113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8399767113657"><a name="p8399767113657"></a><a name="p8399767113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9292492113657"><a name="p9292492113657"></a><a name="p9292492113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p14494365113657"><a name="p14494365113657"></a><a name="p14494365113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p33192948113657"><a name="p33192948113657"></a><a name="p33192948113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row30301076113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p38468076113657"><a name="p38468076113657"></a><a name="p38468076113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p28906428113657"><a name="p28906428113657"></a><a name="p28906428113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p59719341113657"><a name="p59719341113657"></a><a name="p59719341113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5428454113657"><a name="p5428454113657"></a><a name="p5428454113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row48856094113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p65029527113657"><a name="p65029527113657"></a><a name="p65029527113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p32900333113657"><a name="p32900333113657"></a><a name="p32900333113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p47681287113657"><a name="p47681287113657"></a><a name="p47681287113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p36979021113657"><a name="p36979021113657"></a><a name="p36979021113657"></a>V2 or V4</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Transfer protocols and authentication applicable to Upload Part - Copy interfaces

<a name="table42510761113657"></a>
<table><thead align="left"><tr id="row8314754113657"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p2406492113657"><a name="p2406492113657"></a><a name="p2406492113657"></a>Source Object</p>
</th>
<th class="cellrowborder" valign="top" width="24.740000000000002%" id="mcps1.2.5.1.2"><p id="p60708154113657"><a name="p60708154113657"></a><a name="p60708154113657"></a>Target Part</p>
</th>
<th class="cellrowborder" valign="top" width="25.259999999999998%" id="mcps1.2.5.1.3"><p id="p56860468114154"><a name="p56860468114154"></a><a name="p56860468114154"></a>Transfer Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p15094052113657"><a name="p15094052113657"></a><a name="p15094052113657"></a>Authentication</p>
</th>
</tr>
</thead>
<tbody><tr id="row14658688113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p46503040113657"><a name="p46503040113657"></a><a name="p46503040113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p8649868113657"><a name="p8649868113657"></a><a name="p8649868113657"></a>Part encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p29550733113657"><a name="p29550733113657"></a><a name="p29550733113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p44799211113657"><a name="p44799211113657"></a><a name="p44799211113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row539720113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p43717372113657"><a name="p43717372113657"></a><a name="p43717372113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p51446207113657"><a name="p51446207113657"></a><a name="p51446207113657"></a>Part encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p6393276113657"><a name="p6393276113657"></a><a name="p6393276113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p48093337113657"><a name="p48093337113657"></a><a name="p48093337113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row30186851113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p29215860113657"><a name="p29215860113657"></a><a name="p29215860113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p17674425113657"><a name="p17674425113657"></a><a name="p17674425113657"></a>Part encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p22342298113657"><a name="p22342298113657"></a><a name="p22342298113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p64895745113657"><a name="p64895745113657"></a><a name="p64895745113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row47190793113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p64357873113657"><a name="p64357873113657"></a><a name="p64357873113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p45605201113657"><a name="p45605201113657"></a><a name="p45605201113657"></a>Part encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p3033810113657"><a name="p3033810113657"></a><a name="p3033810113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p44412059113657"><a name="p44412059113657"></a><a name="p44412059113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row64164219113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p29919236113657"><a name="p29919236113657"></a><a name="p29919236113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p7539050113657"><a name="p7539050113657"></a><a name="p7539050113657"></a>Part encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p6683284113657"><a name="p6683284113657"></a><a name="p6683284113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p4475114113657"><a name="p4475114113657"></a><a name="p4475114113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row40276034113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p41133318113657"><a name="p41133318113657"></a><a name="p41133318113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p43464491113657"><a name="p43464491113657"></a><a name="p43464491113657"></a>Part encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p30962905113657"><a name="p30962905113657"></a><a name="p30962905113657"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p24967351113657"><a name="p24967351113657"></a><a name="p24967351113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row23379567113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14696793113657"><a name="p14696793113657"></a><a name="p14696793113657"></a>Non-encrypted object</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p49589575113657"><a name="p49589575113657"></a><a name="p49589575113657"></a>Non-encrypted part</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p57332642113657"><a name="p57332642113657"></a><a name="p57332642113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13432401113657"><a name="p13432401113657"></a><a name="p13432401113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row53782748113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61435301113657"><a name="p61435301113657"></a><a name="p61435301113657"></a>Object encrypted using SSE-KMS</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p10203446113657"><a name="p10203446113657"></a><a name="p10203446113657"></a>Non-encrypted part</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p21172792113657"><a name="p21172792113657"></a><a name="p21172792113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37274578113657"><a name="p37274578113657"></a><a name="p37274578113657"></a>V2 or V4</p>
</td>
</tr>
<tr id="row67035752113657"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61186842113657"><a name="p61186842113657"></a><a name="p61186842113657"></a>Object encrypted using SSE-C</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p57187193113657"><a name="p57187193113657"></a><a name="p57187193113657"></a>Non-encrypted part</p>
</td>
<td class="cellrowborder" valign="top" width="25.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p1651052113657"><a name="p1651052113657"></a><a name="p1651052113657"></a>HTTP or HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p66626396113657"><a name="p66626396113657"></a><a name="p66626396113657"></a>V2 or V4</p>
</td>
</tr>
</tbody>
</table>

