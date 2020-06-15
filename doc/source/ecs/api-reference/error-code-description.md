# Error Code Description<a name="EN-US_TOPIC_0022067717"></a>

## Context<a name="section2270842516290"></a>

-   An error code returned by an API does not correspond to one error message. The following table lists only common error messages.
-   Most ECS APIs are asynchronous. Some error codes are displayed in the returned messages for task viewing requests. HTTP status codes may not be accurate.
-   The ECS service is strongly dependent on other services, such as network and storage. When error messages are provided for the ECS-depended services, contact technical support for troubleshooting.
-   If the system displays an error code when you perform operations on the management console, see "How Do I Handle Error Messages Displayed on the Management Console?" in  _Elastic Cloud Server User Guide_  for troubleshooting.

## Error Codes<a name="section59060991162916"></a>

<a name="table36210876112050"></a>
<table><thead align="left"><tr id="row60537118112050"><th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.1"><p id="p36247510141740"><a name="p36247510141740"></a><a name="p36247510141740"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.6.1.2"><p id="p4559511112050"><a name="p4559511112050"></a><a name="p4559511112050"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.1.6.1.3"><p id="p33776109112050"><a name="p33776109112050"></a><a name="p33776109112050"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.6.1.4"><p id="p1010742314195"><a name="p1010742314195"></a><a name="p1010742314195"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.1.6.1.5"><p id="p28762041141941"><a name="p28762041141941"></a><a name="p28762041141941"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row46722832155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p47395611142232"><a name="p47395611142232"></a><a name="p47395611142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p20402961155119"><a name="p20402961155119"></a><a name="p20402961155119"></a>Ecs.0000</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p42027136155119"><a name="p42027136155119"></a><a name="p42027136155119"></a>Request error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p7184421492"><a name="p7184421492"></a><a name="p7184421492"></a>An existing EIP cannot be assigned to the ECSs created in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p48023993141941"><a name="p48023993141941"></a><a name="p48023993141941"></a>Check the request body according to the returned error message.</p>
</td>
</tr>
<tr id="row38238148155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p57444540142232"><a name="p57444540142232"></a><a name="p57444540142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p36140742155119"><a name="p36140742155119"></a><a name="p36140742155119"></a>Ecs.0001</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p41718978155119"><a name="p41718978155119"></a><a name="p41718978155119"></a>The number of ECSs has reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p17120122982212"><a name="p17120122982212"></a><a name="p17120122982212"></a>The number of ECSs is beyond the quota limit.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p64738205141941"><a name="p64738205141941"></a><a name="p64738205141941"></a>Apply for a higher quota of the corresponding resource according to the returned error message.</p>
</td>
</tr>
<tr id="row349510116015"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p24961711807"><a name="p24961711807"></a><a name="p24961711807"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p749631111014"><a name="p749631111014"></a><a name="p749631111014"></a>Ecs.0002</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p2049661115014"><a name="p2049661115014"></a><a name="p2049661115014"></a>Failed to submit the task.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1349651120019"><a name="p1349651120019"></a><a name="p1349651120019"></a>Failed to submit the task.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p8496611700"><a name="p8496611700"></a><a name="p8496611700"></a>Contact technical support to locate the fault.</p>
</td>
</tr>
<tr id="row27089203155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1139140142232"><a name="p1139140142232"></a><a name="p1139140142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p61995949155119"><a name="p61995949155119"></a><a name="p61995949155119"></a>Ecs.0003</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p145875121945"><a name="p145875121945"></a><a name="p145875121945"></a>You do not have permission or your balance is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p3891899014195"><a name="p3891899014195"></a><a name="p3891899014195"></a>The token role contains <strong id="b1719621285014"><a name="b1719621285014"></a><a name="b1719621285014"></a>op_suspended</strong>. The current operation is not allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p9303246141941"><a name="p9303246141941"></a><a name="p9303246141941"></a>Check whether the account balance is insufficient and the account is frozen according to the returned error message.</p>
</td>
</tr>
<tr id="row1229355675511"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p3294185611552"><a name="p3294185611552"></a><a name="p3294185611552"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p15294056205513"><a name="p15294056205513"></a><a name="p15294056205513"></a>Ecs.0004</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p429418564557"><a name="p429418564557"></a><a name="p429418564557"></a>Authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p112942562559"><a name="p112942562559"></a><a name="p112942562559"></a>Failed to assign permissions: %s</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p72941456105517"><a name="p72941456105517"></a><a name="p72941456105517"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row12801543155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p25127069142232"><a name="p25127069142232"></a><a name="p25127069142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p32196421155119"><a name="p32196421155119"></a><a name="p32196421155119"></a>Ecs.0005</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p57773302155119"><a name="p57773302155119"></a><a name="p57773302155119"></a>Invalid parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2030613481588"><a name="p2030613481588"></a><a name="p2030613481588"></a>Invalid request body.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p15365427141941"><a name="p15365427141941"></a><a name="p15365427141941"></a>Check whether the request body is of the correct JSON structure according to the API reference.</p>
</td>
</tr>
<tr id="row57507975155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p64022522142232"><a name="p64022522142232"></a><a name="p64022522142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p39479476155119"><a name="p39479476155119"></a><a name="p39479476155119"></a>Ecs.0006</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p43721027155119"><a name="p43721027155119"></a><a name="p43721027155119"></a>No product ID in the Marketplace image.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p83481929414"><a name="p83481929414"></a><a name="p83481929414"></a>Marketplace image [%s] must have a product code.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p36640052141941"><a name="p36640052141941"></a><a name="p36640052141941"></a>Check image parameter.</p>
</td>
</tr>
<tr id="row10576055155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p31758230142232"><a name="p31758230142232"></a><a name="p31758230142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p63027797155119"><a name="p63027797155119"></a><a name="p63027797155119"></a>Ecs.0007</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p4977948155119"><a name="p4977948155119"></a><a name="p4977948155119"></a>Invalid image attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6109560514195"><a name="p6109560514195"></a><a name="p6109560514195"></a>ECS does not support Ironic image [%s].</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p15054267141941"><a name="p15054267141941"></a><a name="p15054267141941"></a>Adjust the specifications or image type.</p>
</td>
</tr>
<tr id="row63007434155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p66300660142232"><a name="p66300660142232"></a><a name="p66300660142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p5046052155119"><a name="p5046052155119"></a><a name="p5046052155119"></a>Ecs.0008</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p6077069155119"><a name="p6077069155119"></a><a name="p6077069155119"></a>Invalid flavor attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4979696614195"><a name="p4979696614195"></a><a name="p4979696614195"></a><strong id="b5457565174"><a name="b5457565174"></a><a name="b5457565174"></a>performancetype</strong> in extended flavor field [%s] is null.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p11436077141941"><a name="p11436077141941"></a><a name="p11436077141941"></a>Contact technical support to check whether the flavor registration is valid.</p>
</td>
</tr>
<tr id="row44423227155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p14799391142232"><a name="p14799391142232"></a><a name="p14799391142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p998950155119"><a name="p998950155119"></a><a name="p998950155119"></a>Ecs.0009</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p5508148219516"><a name="p5508148219516"></a><a name="p5508148219516"></a>Flavor conflict.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p28941349201214"><a name="p28941349201214"></a><a name="p28941349201214"></a>Another flavor must be used for resizing.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p53907060141941"><a name="p53907060141941"></a><a name="p53907060141941"></a>Change the flavor when modifying ECS specifications.</p>
</td>
</tr>
<tr id="row25883278155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p51338347142232"><a name="p51338347142232"></a><a name="p51338347142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p65443752155119"><a name="p65443752155119"></a><a name="p65443752155119"></a>Ecs.0010</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p66452564155119"><a name="p66452564155119"></a><a name="p66452564155119"></a>The private IP address is already in use.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p592153765419"><a name="p592153765419"></a><a name="p592153765419"></a>Private IP address %s is already in use.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p4395768141941"><a name="p4395768141941"></a><a name="p4395768141941"></a>Change the port.</p>
</td>
</tr>
<tr id="row45318156155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p46017841142232"><a name="p46017841142232"></a><a name="p46017841142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p58428543155119"><a name="p58428543155119"></a><a name="p58428543155119"></a>Ecs.0011</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p2766758919530"><a name="p2766758919530"></a><a name="p2766758919530"></a>Failed to meet password complexity requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p3735931514195"><a name="p3735931514195"></a><a name="p3735931514195"></a>The password length must range from 8 to 26.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p20512928141941"><a name="p20512928141941"></a><a name="p20512928141941"></a>Check the password length and change the password.</p>
</td>
</tr>
<tr id="row42828426155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p59683478142232"><a name="p59683478142232"></a><a name="p59683478142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p13272905155119"><a name="p13272905155119"></a><a name="p13272905155119"></a>Ecs.0012</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1363487155119"><a name="p1363487155119"></a><a name="p1363487155119"></a>The number of IP addresses in the subnet is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p620563714195"><a name="p620563714195"></a><a name="p620563714195"></a>Insufficient IP addresses.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p50934485141941"><a name="p50934485141941"></a><a name="p50934485141941"></a>Check whether the floating IP addresses of the subnet are used up.</p>
</td>
</tr>
<tr id="row50591778155116"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p22711876142232"><a name="p22711876142232"></a><a name="p22711876142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p54458281155119"><a name="p54458281155119"></a><a name="p54458281155119"></a>Ecs.0013</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p49044644155119"><a name="p49044644155119"></a><a name="p49044644155119"></a>Insufficient EIP quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p16458145017502"><a name="p16458145017502"></a><a name="p16458145017502"></a>Insufficient EIP quota.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p32052606141941"><a name="p32052606141941"></a><a name="p32052606141941"></a>Apply for a higher EIP quota because the EIP quota is insufficient.</p>
</td>
</tr>
<tr id="row1371015393613"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p10711753163616"><a name="p10711753163616"></a><a name="p10711753163616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p15711553183611"><a name="p15711553183611"></a><a name="p15711553183611"></a>Ecs.0014</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p171111537366"><a name="p171111537366"></a><a name="p171111537366"></a>Invalid VPC parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p14711135314367"><a name="p14711135314367"></a><a name="p14711135314367"></a>VPC parameters are invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p57114539361"><a name="p57114539361"></a><a name="p57114539361"></a>Check whether the subnets belong to the same VPC.</p>
</td>
</tr>
<tr id="row60541508191955"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p48177198142232"><a name="p48177198142232"></a><a name="p48177198142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p3066669419202"><a name="p3066669419202"></a><a name="p3066669419202"></a>Ecs.0015</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p97425619202"><a name="p97425619202"></a><a name="p97425619202"></a>The disk of this type is not applicable to the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4721729614195"><a name="p4721729614195"></a><a name="p4721729614195"></a>Flavor resource_type %s does not match volume_type %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p46124292141941"><a name="p46124292141941"></a><a name="p46124292141941"></a>Check whether the disk type matches the flavor.</p>
</td>
</tr>
<tr id="row101943719355"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1319153711357"><a name="p1319153711357"></a><a name="p1319153711357"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p9933154215356"><a name="p9933154215356"></a><a name="p9933154215356"></a>Ecs.0027</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p6191379353"><a name="p6191379353"></a><a name="p6191379353"></a>Private flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p11191937173514"><a name="p11191937173514"></a><a name="p11191937173514"></a>Flavor %s is private.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p5799432133812"><a name="p5799432133812"></a><a name="p5799432133812"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row1652419623317"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p652476123310"><a name="p652476123310"></a><a name="p652476123310"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p523662893516"><a name="p523662893516"></a><a name="p523662893516"></a>Ecs.0028</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p552456103310"><a name="p552456103310"></a><a name="p552456103310"></a>The blacklisted user configured in the flavor is not allowed to use the flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p96001648182513"><a name="p96001648182513"></a><a name="p96001648182513"></a>The user is contained in %s and is not allowed to use the flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p880983313810"><a name="p880983313810"></a><a name="p880983313810"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row169845390813"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p79841391983"><a name="p79841391983"></a><a name="p79841391983"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1998415396812"><a name="p1998415396812"></a><a name="p1998415396812"></a>Ecs.0021</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1498412391884"><a name="p1498412391884"></a><a name="p1498412391884"></a>Insufficient EVS disk quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1258222217504"><a name="p1258222217504"></a><a name="p1258222217504"></a>Failed to check the Cinder quota: The number of volumes is beyond the quota limit.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1798410399820"><a name="p1798410399820"></a><a name="p1798410399820"></a>Apply for a higher EVS disk quota.</p>
</td>
</tr>
<tr id="row19161448389"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p51616481987"><a name="p51616481987"></a><a name="p51616481987"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p3161448780"><a name="p3161448780"></a><a name="p3161448780"></a>Ecs.0022</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p15161348684"><a name="p15161348684"></a><a name="p15161348684"></a>The number of ECSs in the ECS group exceeded the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1016124816817"><a name="p1016124816817"></a><a name="p1016124816817"></a>The number of ECSs is beyond the ECS group quota limit.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p8161848183"><a name="p8161848183"></a><a name="p8161848183"></a>Apply for a higher ECS quota for an ECS group.</p>
</td>
</tr>
<tr id="row8303152516599"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p23031325105916"><a name="p23031325105916"></a><a name="p23031325105916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1230314258597"><a name="p1230314258597"></a><a name="p1230314258597"></a>Ecs.0023</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1830312253594"><a name="p1830312253594"></a><a name="p1830312253594"></a>Invalid token, or the project ID in the token is different from that in the URL.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2303525175914"><a name="p2303525175914"></a><a name="p2303525175914"></a>The project ID in token does not match that in URL.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p43031825155911"><a name="p43031825155911"></a><a name="p43031825155911"></a>Apply for a valid token or check the project ID in the URL.</p>
</td>
</tr>
<tr id="row4754179201411"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p197551298143"><a name="p197551298143"></a><a name="p197551298143"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1675510941416"><a name="p1675510941416"></a><a name="p1675510941416"></a>Ecs.0025</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p167551696140"><a name="p167551696140"></a><a name="p167551696140"></a>EVS is not authorized to obtain KMS keys for encrypting EVS disks.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p475514916147"><a name="p475514916147"></a><a name="p475514916147"></a>Failed to check the KMS role.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1375511912143"><a name="p1375511912143"></a><a name="p1375511912143"></a>Authorize EVS to obtain KMS keys for encrypting EVS disks.</p>
</td>
</tr>
<tr id="row11771535513"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1477223155118"><a name="p1477223155118"></a><a name="p1477223155118"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p277213375114"><a name="p277213375114"></a><a name="p277213375114"></a>Ecs.0029</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p277218365117"><a name="p277218365117"></a><a name="p277218365117"></a>The flavor does not exist or has been abandoned.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p187729314517"><a name="p187729314517"></a><a name="p187729314517"></a>Flavor [%s] does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p11111192318521"><a name="p11111192318521"></a><a name="p11111192318521"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row528015274427"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p12811927144212"><a name="p12811927144212"></a><a name="p12811927144212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p13281162764210"><a name="p13281162764210"></a><a name="p13281162764210"></a>Ecs.0030</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p17281112719429"><a name="p17281112719429"></a><a name="p17281112719429"></a>The ECS has been frozen.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p428111275428"><a name="p428111275428"></a><a name="p428111275428"></a>The ECS has been frozen.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p128132764213"><a name="p128132764213"></a><a name="p128132764213"></a>Check whether the account has been frozen or contact technical support.</p>
</td>
</tr>
<tr id="row13563611191211"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p18564141131211"><a name="p18564141131211"></a><a name="p18564141131211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p356491118125"><a name="p356491118125"></a><a name="p356491118125"></a>Ecs.0031</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p19564811161216"><a name="p19564811161216"></a><a name="p19564811161216"></a>The image does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p15641911171213"><a name="p15641911171213"></a><a name="p15641911171213"></a>Image [%s] does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1956415118125"><a name="p1956415118125"></a><a name="p1956415118125"></a>Change another image.</p>
</td>
</tr>
<tr id="row84131721217"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p742017111211"><a name="p742017111211"></a><a name="p742017111211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p34151718127"><a name="p34151718127"></a><a name="p34151718127"></a>Ecs.0032</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p7481741220"><a name="p7481741220"></a><a name="p7481741220"></a>The image is not in <strong id="b842352706141643"><a name="b842352706141643"></a><a name="b842352706141643"></a>Active</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p7461715126"><a name="p7461715126"></a><a name="p7461715126"></a>Image [%s] must be active.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p64617181215"><a name="p64617181215"></a><a name="p64617181215"></a>Change another image.</p>
</td>
</tr>
<tr id="row19418622181212"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p3418422161217"><a name="p3418422161217"></a><a name="p3418422161217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p17418722151214"><a name="p17418722151214"></a><a name="p17418722151214"></a>Ecs.0034</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p8160192581814"><a name="p8160192581814"></a><a name="p8160192581814"></a>The full-ECS backup does not exist or has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p18418222101213"><a name="p18418222101213"></a><a name="p18418222101213"></a>Backup %s does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p118021330181817"><a name="p118021330181817"></a><a name="p118021330181817"></a>Change another image.</p>
</td>
</tr>
<tr id="row690423175218"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p3911023145210"><a name="p3911023145210"></a><a name="p3911023145210"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p14911723205210"><a name="p14911723205210"></a><a name="p14911723205210"></a>Ecs.0036</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p5911023195210"><a name="p5911023195210"></a><a name="p5911023195210"></a>The flavor does not support automatic recovery.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1791323145210"><a name="p1791323145210"></a><a name="p1791323145210"></a>Flavor [%s] does not support auto recovery.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p16911423165211"><a name="p16911423165211"></a><a name="p16911423165211"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row1417332765212"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1485313121539"><a name="p1485313121539"></a><a name="p1485313121539"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p148531312185311"><a name="p148531312185311"></a><a name="p148531312185311"></a>Ecs.0037</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1117419270523"><a name="p1117419270523"></a><a name="p1117419270523"></a>The flavor does not support SCSI disks.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1817432785218"><a name="p1817432785218"></a><a name="p1817432785218"></a>ECS flavor %s does not support SCSI disks.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p12256229458"><a name="p12256229458"></a><a name="p12256229458"></a>Change another flavor or type.</p>
</td>
</tr>
<tr id="row6361530115213"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1368661355314"><a name="p1368661355314"></a><a name="p1368661355314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p166861413185320"><a name="p166861413185320"></a><a name="p166861413185320"></a>Ecs.0038</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1036130115210"><a name="p1036130115210"></a><a name="p1036130115210"></a>The subnet does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p93615301521"><a name="p93615301521"></a><a name="p93615301521"></a>Subnet [%s] does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p7371830115212"><a name="p7371830115212"></a><a name="p7371830115212"></a>Adjust network parameter settings.</p>
</td>
</tr>
<tr id="row1949953295218"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p164211314185319"><a name="p164211314185319"></a><a name="p164211314185319"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1742111415312"><a name="p1742111415312"></a><a name="p1742111415312"></a>Ecs.0039</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p13500163275213"><a name="p13500163275213"></a><a name="p13500163275213"></a>The specified IP address does not belong to the subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p550043210526"><a name="p550043210526"></a><a name="p550043210526"></a>Private IP address [%s] is not in subnet [%s].</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1950013323523"><a name="p1950013323523"></a><a name="p1950013323523"></a>Change the specified private IP address.</p>
</td>
</tr>
<tr id="row354664285218"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p12160101515311"><a name="p12160101515311"></a><a name="p12160101515311"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p16160101545313"><a name="p16160101545313"></a><a name="p16160101545313"></a>Ecs.0041</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p175461424527"><a name="p175461424527"></a><a name="p175461424527"></a>Invalid description field.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p195466428526"><a name="p195466428526"></a><a name="p195466428526"></a>Description field length cannot be greater than 85 characters and cannot contain characters &gt;&lt;.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p19546124214523"><a name="p19546124214523"></a><a name="p19546124214523"></a>Modify the service description field.</p>
</td>
</tr>
<tr id="row8514194511527"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p882851505320"><a name="p882851505320"></a><a name="p882851505320"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1082817155534"><a name="p1082817155534"></a><a name="p1082817155534"></a>Ecs.0042</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p951454515219"><a name="p951454515219"></a><a name="p951454515219"></a>The number of attached data disks exceeds the maximum allowed limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1951484545220"><a name="p1951484545220"></a><a name="p1951484545220"></a>The number of VBD disks is %s, but a KVM ECS supports a maximum of 24.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p95141245165213"><a name="p95141245165213"></a><a name="p95141245165213"></a>Adjust the number of attached data disks.</p>
</td>
</tr>
<tr id="row1876853485217"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p15975616185314"><a name="p15975616185314"></a><a name="p15975616185314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p19975121675314"><a name="p19975121675314"></a><a name="p19975121675314"></a>Ecs.0043</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p107691134115220"><a name="p107691134115220"></a><a name="p107691134115220"></a>The disk type does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p17691934125210"><a name="p17691934125210"></a><a name="p17691934125210"></a>Disk type [%s] does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p2076973413524"><a name="p2076973413524"></a><a name="p2076973413524"></a>Change the disk type.</p>
</td>
</tr>
<tr id="row1897743912529"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p10568145014536"><a name="p10568145014536"></a><a name="p10568145014536"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p13568145011536"><a name="p13568145011536"></a><a name="p13568145011536"></a>Ecs.0044</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p17978113918525"><a name="p17978113918525"></a><a name="p17978113918525"></a>The disk of this type has been sold out.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p129781539115212"><a name="p129781539115212"></a><a name="p129781539115212"></a>Disk type [%s] has been sold out in AZ [%s].</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p486819507612"><a name="p486819507612"></a><a name="p486819507612"></a>Change the disk type.</p>
</td>
</tr>
<tr id="row345413712527"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p515785645317"><a name="p515785645317"></a><a name="p515785645317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p141572565534"><a name="p141572565534"></a><a name="p141572565534"></a>Ecs.0045</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p8454193715214"><a name="p8454193715214"></a><a name="p8454193715214"></a>The bandwidth exceeds the maximum size allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p144541037175220"><a name="p144541037175220"></a><a name="p144541037175220"></a>Bandwidth size %d is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p7454173719527"><a name="p7454173719527"></a><a name="p7454173719527"></a>Adjust the bandwidth.</p>
</td>
</tr>
<tr id="row158226550567"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p7823195515615"><a name="p7823195515615"></a><a name="p7823195515615"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p13823855195619"><a name="p13823855195619"></a><a name="p13823855195619"></a>Ecs.0046</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p18823165595613"><a name="p18823165595613"></a><a name="p18823165595613"></a>The disk type of the ECS is different from that of the snapshot image.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p14823755145617"><a name="p14823755145617"></a><a name="p14823755145617"></a>The root disk type in the request is different from that of the snapshot image.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1882335514564"><a name="p1882335514564"></a><a name="p1882335514564"></a>Change the disk type.</p>
</td>
</tr>
<tr id="row19388103918571"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p18323757115714"><a name="p18323757115714"></a><a name="p18323757115714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1032305712579"><a name="p1032305712579"></a><a name="p1032305712579"></a>Ecs.0048</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p7388143912579"><a name="p7388143912579"></a><a name="p7388143912579"></a>The full-ECS image is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p13389173910572"><a name="p13389173910572"></a><a name="p13389173910572"></a>Image [%s] is error or associated backup [%s] is error.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p18389133916575"><a name="p18389133916575"></a><a name="p18389133916575"></a>Check the full-ECS image.</p>
</td>
</tr>
<tr id="row1285193419570"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p185541823145814"><a name="p185541823145814"></a><a name="p185541823145814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p11554182315810"><a name="p11554182315810"></a><a name="p11554182315810"></a>Ecs.0050</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p16851345571"><a name="p16851345571"></a><a name="p16851345571"></a>The number of NICs attached to the ECS exceeds the maximum value allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1485163418575"><a name="p1485163418575"></a><a name="p1485163418575"></a>The requested number of NICs is greater than the number available.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p11851334115715"><a name="p11851334115715"></a><a name="p11851334115715"></a>Adjust the number of NICs.</p>
</td>
</tr>
<tr id="row1856892845811"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p3457183015813"><a name="p3457183015813"></a><a name="p3457183015813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p8457203014586"><a name="p8457203014586"></a><a name="p8457203014586"></a>Ecs.0051</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p142988311417"><a name="p142988311417"></a><a name="p142988311417"></a>The attached disk is not of SCSI type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p256972895813"><a name="p256972895813"></a><a name="p256972895813"></a>Only SCSI disks can be attached to the ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p05691028195819"><a name="p05691028195819"></a><a name="p05691028195819"></a>Adjust the disk type.</p>
</td>
</tr>
<tr id="row14556521125814"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1672018401580"><a name="p1672018401580"></a><a name="p1672018401580"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1772084005811"><a name="p1772084005811"></a><a name="p1772084005811"></a>Ecs.0052</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1455772105819"><a name="p1455772105819"></a><a name="p1455772105819"></a>The attached system disk is not of SCSI type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1455732165813"><a name="p1455732165813"></a><a name="p1455732165813"></a>Only SCSI system disks can be attached to the ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p185575219580"><a name="p185575219580"></a><a name="p185575219580"></a>Change the system disk type.</p>
</td>
</tr>
<tr id="row1243316383585"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p13712349155812"><a name="p13712349155812"></a><a name="p13712349155812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p7712124965817"><a name="p7712124965817"></a><a name="p7712124965817"></a>Ecs.0053</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p104922171078"><a name="p104922171078"></a><a name="p104922171078"></a>The attached data disk is not of SCSI type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p5433113815814"><a name="p5433113815814"></a><a name="p5433113815814"></a>Only SCSI data disks can be attached to the ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1343443813586"><a name="p1343443813586"></a><a name="p1343443813586"></a>Change the data disk type.</p>
</td>
</tr>
<tr id="row1440213616118"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p12403761113"><a name="p12403761113"></a><a name="p12403761113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p2040316617112"><a name="p2040316617112"></a><a name="p2040316617112"></a>Ecs.0057</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p34031761713"><a name="p34031761713"></a><a name="p34031761713"></a>The disk has been attached to the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1440386115"><a name="p1440386115"></a><a name="p1440386115"></a>The disk has been attached to the ECS and cannot be attached again.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p5403661514"><a name="p5403661514"></a><a name="p5403661514"></a>Attach a new disk to the ECS.</p>
</td>
</tr>
<tr id="row1322513342379"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1122513413710"><a name="p1122513413710"></a><a name="p1122513413710"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p22251434143714"><a name="p22251434143714"></a><a name="p22251434143714"></a>Ecs.0062</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p322516346375"><a name="p322516346375"></a><a name="p322516346375"></a>The flavor does not support QingTian ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1422583413377"><a name="p1422583413377"></a><a name="p1422583413377"></a>The flavor does not support the driver mode.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p17225834203713"><a name="p17225834203713"></a><a name="p17225834203713"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row8454381277"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p201071243371"><a name="p201071243371"></a><a name="p201071243371"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p9107943975"><a name="p9107943975"></a><a name="p9107943975"></a>Ecs.0064</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p184514381979"><a name="p184514381979"></a><a name="p184514381979"></a>Inconsistent VPC ID in the request body from that in the primary NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p134553819713"><a name="p134553819713"></a><a name="p134553819713"></a>The VPC ID in the request body is different from that in the primary NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p12459388712"><a name="p12459388712"></a><a name="p12459388712"></a>Adjust the NIC parameter settings.</p>
</td>
</tr>
<tr id="row3702559515517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p23241551142232"><a name="p23241551142232"></a><a name="p23241551142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p9286251155119"><a name="p9286251155119"></a><a name="p9286251155119"></a>Ecs.0100</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p13988892155119"><a name="p13988892155119"></a><a name="p13988892155119"></a>The ECS status does not meet requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6650463214195"><a name="p6650463214195"></a><a name="p6650463214195"></a>Disks can be attached to ECS [%s] only in started or stopped state.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p52633290144640"><a name="p52633290144640"></a><a name="p52633290144640"></a>The ECS in the current state does not support this operation. Try again later.</p>
</td>
</tr>
<tr id="row236567215517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p31657066142232"><a name="p31657066142232"></a><a name="p31657066142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p64464511155119"><a name="p64464511155119"></a><a name="p64464511155119"></a>Ecs.0101</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p54242915155119"><a name="p54242915155119"></a><a name="p54242915155119"></a>Abnormal system disk status.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1816612514195"><a name="p1816612514195"></a><a name="p1816612514195"></a>Status error of the system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p27612868141941"><a name="p27612868141941"></a><a name="p27612868141941"></a>For details, contact technical support.</p>
</td>
</tr>
<tr id="row1001369315517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p59661002142232"><a name="p59661002142232"></a><a name="p59661002142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p15964174155119"><a name="p15964174155119"></a><a name="p15964174155119"></a>Ecs.0102</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p18029726155119"><a name="p18029726155119"></a><a name="p18029726155119"></a>The system disk status does not allow the disk to be detached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p10230317163310"><a name="p10230317163310"></a><a name="p10230317163310"></a>System disk status does not support uninstallation, serverId [%s]</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p22049872141941"><a name="p22049872141941"></a><a name="p22049872141941"></a>Check the status of the system disk.</p>
</td>
</tr>
<tr id="row2758469192023"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p6327043142232"><a name="p6327043142232"></a><a name="p6327043142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p47606054192035"><a name="p47606054192035"></a><a name="p47606054192035"></a>Ecs.0103</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p30885159192035"><a name="p30885159192035"></a><a name="p30885159192035"></a>The disk is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p283115271568"><a name="p283115271568"></a><a name="p283115271568"></a>The volume %s has been frozen and cannot be attached.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p41209175141941"><a name="p41209175141941"></a><a name="p41209175141941"></a>Check the disk status or contact technical support to change the disk status.</p>
</td>
</tr>
<tr id="row21472264192027"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p49011630142232"><a name="p49011630142232"></a><a name="p49011630142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p29937547192041"><a name="p29937547192041"></a><a name="p29937547192041"></a>Ecs.0104</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p9022282192041"><a name="p9022282192041"></a><a name="p9022282192041"></a>Insufficient number of ECS slots for attaching disks.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p973706214195"><a name="p973706214195"></a><a name="p973706214195"></a>The number of disks attached to server[%s] has exceeded the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p49608899141941"><a name="p49608899141941"></a><a name="p49608899141941"></a>Adjust the number of attached disks.</p>
</td>
</tr>
<tr id="row4586340515517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p27563056142232"><a name="p27563056142232"></a><a name="p27563056142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p57441957155119"><a name="p57441957155119"></a><a name="p57441957155119"></a>Ecs.0105</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p22286955155119"><a name="p22286955155119"></a><a name="p22286955155119"></a>Failed to query the system disk of the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p5050454014195"><a name="p5050454014195"></a><a name="p5050454014195"></a>Failed to view the details about the system volume: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p58897916141941"><a name="p58897916141941"></a><a name="p58897916141941"></a>Check whether the ECS has a system disk attached.</p>
</td>
</tr>
<tr id="row1532299515517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p27917683142232"><a name="p27917683142232"></a><a name="p27917683142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p6845529155119"><a name="p6845529155119"></a><a name="p6845529155119"></a>Ecs.0106</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p17617008155119"><a name="p17617008155119"></a><a name="p17617008155119"></a>Abnormal network status.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6433597614195"><a name="p6433597614195"></a><a name="p6433597614195"></a>Failed to create VLAN network %s because the network status is error.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p6001897141941"><a name="p6001897141941"></a><a name="p6001897141941"></a>Contact technical support for fault locating.</p>
</td>
</tr>
<tr id="row1157616287211"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1557662814212"><a name="p1557662814212"></a><a name="p1557662814212"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p95761628728"><a name="p95761628728"></a><a name="p95761628728"></a>Ecs.0110</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1057652815214"><a name="p1057652815214"></a><a name="p1057652815214"></a>Operations are prohibited on the client due to permissions.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p557615281824"><a name="p557615281824"></a><a name="p557615281824"></a>Token role %s is not allowed to perform this operation.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p957622818210"><a name="p957622818210"></a><a name="p957622818210"></a>You do not have the permission to perform such an operation. Check token permissions. For details, see the error message returned by the API.</p>
</td>
</tr>
<tr id="row84487522413"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p154503521441"><a name="p154503521441"></a><a name="p154503521441"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1645035210417"><a name="p1645035210417"></a><a name="p1645035210417"></a>Ecs.0111</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p24504521415"><a name="p24504521415"></a><a name="p24504521415"></a>The disk is not in the attachment list.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1045014521742"><a name="p1045014521742"></a><a name="p1045014521742"></a>Disk %s is not in the attachment list for ECS %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p24506521741"><a name="p24506521741"></a><a name="p24506521741"></a>Check whether the selected disk has been attached to the ECS, or replace the disk.</p>
</td>
</tr>
<tr id="row178521171316"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p10852478112"><a name="p10852478112"></a><a name="p10852478112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p158523713111"><a name="p158523713111"></a><a name="p158523713111"></a>Ecs.0112</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p198521718113"><a name="p198521718113"></a><a name="p198521718113"></a>The ECS is not of pay-per-use type, and it cannot be migrated.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p12852971416"><a name="p12852971416"></a><a name="p12852971416"></a>Create a pay-per-use ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p68522714110"><a name="p68522714110"></a><a name="p68522714110"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row222684318814"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p11226343887"><a name="p11226343887"></a><a name="p11226343887"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p192265431814"><a name="p192265431814"></a><a name="p192265431814"></a>Ecs.0114</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p182261143182"><a name="p182261143182"></a><a name="p182261143182"></a>The ECS cannot be detected.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1022613436815"><a name="p1022613436815"></a><a name="p1022613436815"></a>ECS [%s] could not be found.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p722619431485"><a name="p722619431485"></a><a name="p722619431485"></a>Check whether the ECS has been created.</p>
</td>
</tr>
<tr id="row1431718173334"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p8318141733310"><a name="p8318141733310"></a><a name="p8318141733310"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p126501126173318"><a name="p126501126173318"></a><a name="p126501126173318"></a>Ecs.0118</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p19318201793319"><a name="p19318201793319"></a><a name="p19318201793319"></a>The number of tasks in a batch is greater than the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p18318717183317"><a name="p18318717183317"></a><a name="p18318717183317"></a>The number of ECSs %s is greater than the maximum number %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p43184176334"><a name="p43184176334"></a><a name="p43184176334"></a>Check the number of ECSs in the batch.</p>
</td>
</tr>
<tr id="row1529633915517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p39534608142232"><a name="p39534608142232"></a><a name="p39534608142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p25005832155119"><a name="p25005832155119"></a><a name="p25005832155119"></a>Ecs.0201</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p12206488155119"><a name="p12206488155119"></a><a name="p12206488155119"></a>Failed to create the NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6069346714195"><a name="p6069346714195"></a><a name="p6069346714195"></a>Failed to create port in network %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p52656641141941"><a name="p52656641141941"></a><a name="p52656641141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1736475815517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p31026600142232"><a name="p31026600142232"></a><a name="p31026600142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p40160149155119"><a name="p40160149155119"></a><a name="p40160149155119"></a>Ecs.0202</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p31746650155119"><a name="p31746650155119"></a><a name="p31746650155119"></a>Failed to create the system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p16877132713582"><a name="p16877132713582"></a><a name="p16877132713582"></a>Failed to create volume %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p37329532141941"><a name="p37329532141941"></a><a name="p37329532141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row5073454515517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p3773816115046"><a name="p3773816115046"></a><a name="p3773816115046"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p57858863155119"><a name="p57858863155119"></a><a name="p57858863155119"></a>Ecs.0203</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p56056306155119"><a name="p56056306155119"></a><a name="p56056306155119"></a>Failed to create the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1281424005810"><a name="p1281424005810"></a><a name="p1281424005810"></a>Failed to create volume %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p3793227141941"><a name="p3793227141941"></a><a name="p3793227141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row5648918215517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p6359467715046"><a name="p6359467715046"></a><a name="p6359467715046"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p62857865155119"><a name="p62857865155119"></a><a name="p62857865155119"></a>Ecs.0204</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p58322341155119"><a name="p58322341155119"></a><a name="p58322341155119"></a>Failed to create the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6132109914195"><a name="p6132109914195"></a><a name="p6132109914195"></a>Failed to add a tag to ECS %s: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p38815959141941"><a name="p38815959141941"></a><a name="p38815959141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row51510279112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p2301327515058"><a name="p2301327515058"></a><a name="p2301327515058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p37075746155119"><a name="p37075746155119"></a><a name="p37075746155119"></a>Ecs.0205</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p50345472155119"><a name="p50345472155119"></a><a name="p50345472155119"></a>Failed to attach the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p132021258125820"><a name="p132021258125820"></a><a name="p132021258125820"></a>Failed to call the Nova API to attach disk %s to ECS %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p57084935141941"><a name="p57084935141941"></a><a name="p57084935141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row7081669112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1051790015058"><a name="p1051790015058"></a><a name="p1051790015058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p14279530155119"><a name="p14279530155119"></a><a name="p14279530155119"></a>Ecs.0207</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p15791306155119"><a name="p15791306155119"></a><a name="p15791306155119"></a>Failed to modify the ECS specifications.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1225353914195"><a name="p1225353914195"></a><a name="p1225353914195"></a>Failed to resize ECS %s: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p66798452141941"><a name="p66798452141941"></a><a name="p66798452141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row10174527112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1713883315058"><a name="p1713883315058"></a><a name="p1713883315058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p36246844155119"><a name="p36246844155119"></a><a name="p36246844155119"></a>Ecs.0208</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p50313212155119"><a name="p50313212155119"></a><a name="p50313212155119"></a>System error (failed to update metadata).</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p5301259114195"><a name="p5301259114195"></a><a name="p5301259114195"></a>Failed to update the metadata of image %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p41965570141941"><a name="p41965570141941"></a><a name="p41965570141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row37117476112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1196072515058"><a name="p1196072515058"></a><a name="p1196072515058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p36891919155119"><a name="p36891919155119"></a><a name="p36891919155119"></a>Ecs.0209</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p35455449155119"><a name="p35455449155119"></a><a name="p35455449155119"></a>Failed to confirm the ECS specifications modification.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6616143914195"><a name="p6616143914195"></a><a name="p6616143914195"></a>Failed to confirm the flavor change of ECS %s: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p43768020141941"><a name="p43768020141941"></a><a name="p43768020141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row41471361112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p6232527515058"><a name="p6232527515058"></a><a name="p6232527515058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p10110217155119"><a name="p10110217155119"></a><a name="p10110217155119"></a>Ecs.0210</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p13621272155119"><a name="p13621272155119"></a><a name="p13621272155119"></a>System error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p424864317595"><a name="p424864317595"></a><a name="p424864317595"></a>Failed to call the VPC API to assign an FIP to port %s: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p55548755141941"><a name="p55548755141941"></a><a name="p55548755141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row39973355112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p242487815058"><a name="p242487815058"></a><a name="p242487815058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p64904600155119"><a name="p64904600155119"></a><a name="p64904600155119"></a>Ecs.0211</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p22781237155119"><a name="p22781237155119"></a><a name="p22781237155119"></a>Failed to create the NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p18714115510591"><a name="p18714115510591"></a><a name="p18714115510591"></a>Failed to create QoS because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p3155302141941"><a name="p3155302141941"></a><a name="p3155302141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row33711807112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p2290614615058"><a name="p2290614615058"></a><a name="p2290614615058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p31632560155119"><a name="p31632560155119"></a><a name="p31632560155119"></a>Ecs.0212</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p12100533155119"><a name="p12100533155119"></a><a name="p12100533155119"></a>Failed to allocate the private IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p91191791401"><a name="p91191791401"></a><a name="p91191791401"></a>Failed to call the Neutron API to view private IP addresses because the response is null or invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p54252918141941"><a name="p54252918141941"></a><a name="p54252918141941"></a>For details, contact technical support.</p>
</td>
</tr>
<tr id="row65423971112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p5558228815058"><a name="p5558228815058"></a><a name="p5558228815058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p30027533155119"><a name="p30027533155119"></a><a name="p30027533155119"></a>Ecs.0213</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p16311141155119"><a name="p16311141155119"></a><a name="p16311141155119"></a>Failed to update the port attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6829202013012"><a name="p6829202013012"></a><a name="p6829202013012"></a>Failed to update allowed_address_pairs of port %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p32410218141941"><a name="p32410218141941"></a><a name="p32410218141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row31222658112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p5284348515058"><a name="p5284348515058"></a><a name="p5284348515058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p12553078155119"><a name="p12553078155119"></a><a name="p12553078155119"></a>Ecs.0214</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p10166426155119"><a name="p10166426155119"></a><a name="p10166426155119"></a>Failed to create the network.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1737521114195"><a name="p1737521114195"></a><a name="p1737521114195"></a>Failed to create VLAN network because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p7981995141941"><a name="p7981995141941"></a><a name="p7981995141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row52078675112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1418470915058"><a name="p1418470915058"></a><a name="p1418470915058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p29349879155119"><a name="p29349879155119"></a><a name="p29349879155119"></a>Ecs.0216</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p28530033155119"><a name="p28530033155119"></a><a name="p28530033155119"></a>Failed to create the subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4791118214195"><a name="p4791118214195"></a><a name="p4791118214195"></a>Failed to create the subnet for VLAN %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p24955697141941"><a name="p24955697141941"></a><a name="p24955697141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row51620992192122"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p588788615058"><a name="p588788615058"></a><a name="p588788615058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p10083176192125"><a name="p10083176192125"></a><a name="p10083176192125"></a>Ecs.0217</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p11430931192125"><a name="p11430931192125"></a><a name="p11430931192125"></a>Failed to attach the NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p44762914461"><a name="p44762914461"></a><a name="p44762914461"></a>Attached to server [%s] port [%s] failed. Cause: %s</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p8145608141941"><a name="p8145608141941"></a><a name="p8145608141941"></a>Contact technical support to locate the fault.</p>
</td>
</tr>
<tr id="row57693974163425"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p6441057715058"><a name="p6441057715058"></a><a name="p6441057715058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p49483723163425"><a name="p49483723163425"></a><a name="p49483723163425"></a>Ecs.0219</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p48758604163425"><a name="p48758604163425"></a><a name="p48758604163425"></a>Failed to create the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p164025413020"><a name="p164025413020"></a><a name="p164025413020"></a>Failed to quickly create server %s because the ECS status is error or %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p55814474141941"><a name="p55814474141941"></a><a name="p55814474141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1716412288545"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p19164182865416"><a name="p19164182865416"></a><a name="p19164182865416"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p131641528125418"><a name="p131641528125418"></a><a name="p131641528125418"></a>Ecs.0221</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p3164172817547"><a name="p3164172817547"></a><a name="p3164172817547"></a>Failed to migrate the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p10164152818541"><a name="p10164152818541"></a><a name="p10164152818541"></a>Cannot cold migrate from DeH [%s] to the same DeH.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p213507554"><a name="p213507554"></a><a name="p213507554"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row27776341616"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1377823131613"><a name="p1377823131613"></a><a name="p1377823131613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p5778133191613"><a name="p5778133191613"></a><a name="p5778133191613"></a>Ecs.0226</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p87786311610"><a name="p87786311610"></a><a name="p87786311610"></a>Failed to start the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p147786310161"><a name="p147786310161"></a><a name="p147786310161"></a>ECS [%s] action [%s] failed: [%s, %s]</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1577818361611"><a name="p1577818361611"></a><a name="p1577818361611"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row64245714112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p4621493715058"><a name="p4621493715058"></a><a name="p4621493715058"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p61755686155119"><a name="p61755686155119"></a><a name="p61755686155119"></a>Ecs.0301</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p36154640155119"><a name="p36154640155119"></a><a name="p36154640155119"></a>Failed to query the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p5829919214195"><a name="p5829919214195"></a><a name="p5829919214195"></a>The information, status, or metadata of ECS %s is null.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p24678561141941"><a name="p24678561141941"></a><a name="p24678561141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row48223492112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p618824731516"><a name="p618824731516"></a><a name="p618824731516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p50058078155119"><a name="p50058078155119"></a><a name="p50058078155119"></a>Ecs.0302</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p28172514155119"><a name="p28172514155119"></a><a name="p28172514155119"></a>Failed to query the ECS quota of the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p550911161714"><a name="p550911161714"></a><a name="p550911161714"></a>Failed to view the quota usage of tenant %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p52806453141941"><a name="p52806453141941"></a><a name="p52806453141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row52798518112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p151665631516"><a name="p151665631516"></a><a name="p151665631516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p2450949155119"><a name="p2450949155119"></a><a name="p2450949155119"></a>Ecs.0303</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p64309214155119"><a name="p64309214155119"></a><a name="p64309214155119"></a>Failed to query the specifications.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6805728210"><a name="p6805728210"></a><a name="p6805728210"></a>Failed to view flavor %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p49464301141941"><a name="p49464301141941"></a><a name="p49464301141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row23226941112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p505711191516"><a name="p505711191516"></a><a name="p505711191516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p39430345155119"><a name="p39430345155119"></a><a name="p39430345155119"></a>Ecs.0304</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p39741376155119"><a name="p39741376155119"></a><a name="p39741376155119"></a>Failed to query the image.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p19696388118"><a name="p19696388118"></a><a name="p19696388118"></a>Failed to view image %s because the image or image name is null.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p47185458141941"><a name="p47185458141941"></a><a name="p47185458141941"></a>Contact technical support to check whether the image has been correctly registered or to check other causes.</p>
</td>
</tr>
<tr id="row62757447112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p98990581516"><a name="p98990581516"></a><a name="p98990581516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1864769155119"><a name="p1864769155119"></a><a name="p1864769155119"></a>Ecs.0306</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p16828562155119"><a name="p16828562155119"></a><a name="p16828562155119"></a>Failed to query the backup.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4414535714195"><a name="p4414535714195"></a><a name="p4414535714195"></a>Failed to view the backup because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p10602369141941"><a name="p10602369141941"></a><a name="p10602369141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row13049308112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p357651421516"><a name="p357651421516"></a><a name="p357651421516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p54208758155119"><a name="p54208758155119"></a><a name="p54208758155119"></a>Ecs.0307</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p28833316155119"><a name="p28833316155119"></a><a name="p28833316155119"></a>Failed to query the port.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p13596160728"><a name="p13596160728"></a><a name="p13596160728"></a>Failed to view the port because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p53485531141941"><a name="p53485531141941"></a><a name="p53485531141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row4618217112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p345499931516"><a name="p345499931516"></a><a name="p345499931516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p14413389155119"><a name="p14413389155119"></a><a name="p14413389155119"></a>Ecs.0308</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p26633824155119"><a name="p26633824155119"></a><a name="p26633824155119"></a>Failed to query the ECS quota of the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p77479109211"><a name="p77479109211"></a><a name="p77479109211"></a>Failed to view limits because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p37360737141941"><a name="p37360737141941"></a><a name="p37360737141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row37829293112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p211213651516"><a name="p211213651516"></a><a name="p211213651516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p21596696155119"><a name="p21596696155119"></a><a name="p21596696155119"></a>Ecs.0309</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p4501932155119"><a name="p4501932155119"></a><a name="p4501932155119"></a>Failed to query the NIC QoS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p128215211210"><a name="p128215211210"></a><a name="p128215211210"></a>Failed to view QoS because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p6320893141941"><a name="p6320893141941"></a><a name="p6320893141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row63422060112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p295455491516"><a name="p295455491516"></a><a name="p295455491516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p60683253155119"><a name="p60683253155119"></a><a name="p60683253155119"></a>Ecs.0310</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p16396467155119"><a name="p16396467155119"></a><a name="p16396467155119"></a>System error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1487017351027"><a name="p1487017351027"></a><a name="p1487017351027"></a>Failed to view the network because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p42230292141941"><a name="p42230292141941"></a><a name="p42230292141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row5546987192158"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p638690041516"><a name="p638690041516"></a><a name="p638690041516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p66996147192159"><a name="p66996147192159"></a><a name="p66996147192159"></a>Ecs.0311</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p57978854192159"><a name="p57978854192159"></a><a name="p57978854192159"></a>Failed to query the disk type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1678912460220"><a name="p1678912460220"></a><a name="p1678912460220"></a>Failed to view the disk type of tenant %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p65210512141941"><a name="p65210512141941"></a><a name="p65210512141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row8552193919594"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1155315398594"><a name="p1155315398594"></a><a name="p1155315398594"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p85531339165914"><a name="p85531339165914"></a><a name="p85531339165914"></a>Ecs.0313</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p755317396595"><a name="p755317396595"></a><a name="p755317396595"></a>Failed to query the ECS group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1255311392594"><a name="p1255311392594"></a><a name="p1255311392594"></a>Failed to query ECS group: %s</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p4637173116215"><a name="p4637173116215"></a><a name="p4637173116215"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row20374163311012"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p12374163313108"><a name="p12374163313108"></a><a name="p12374163313108"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p15374433191017"><a name="p15374433191017"></a><a name="p15374433191017"></a>Ecs.0314</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1337443391011"><a name="p1337443391011"></a><a name="p1337443391011"></a>Failed to obtain the key pair.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2037416339108"><a name="p2037416339108"></a><a name="p2037416339108"></a>Failed to obtain the key pair. Reason: %s</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p11374633181018"><a name="p11374633181018"></a><a name="p11374633181018"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1439248191117"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p13936821110"><a name="p13936821110"></a><a name="p13936821110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p17393684119"><a name="p17393684119"></a><a name="p17393684119"></a>Ecs.0315</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p153931816119"><a name="p153931816119"></a><a name="p153931816119"></a>Failed to obtain the automatic recovery status.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p103931482118"><a name="p103931482118"></a><a name="p103931482118"></a>Failed to call the Nova API to obtain the automatic recovery status of tenant ID [%s] on server [%s]. The response is null or invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p8393168191115"><a name="p8393168191115"></a><a name="p8393168191115"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row19147711113"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p8151074116"><a name="p8151074116"></a><a name="p8151074116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p216137101110"><a name="p216137101110"></a><a name="p216137101110"></a>Ecs.0319</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p41617751114"><a name="p41617751114"></a><a name="p41617751114"></a>Insufficient flavor capacity.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p13164718114"><a name="p13164718114"></a><a name="p13164718114"></a>Check capacity: Capacity is not enough.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p81614761112"><a name="p81614761112"></a><a name="p81614761112"></a>Apply for expanding the flavor capacity.</p>
</td>
</tr>
<tr id="row66209459112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p540614611516"><a name="p540614611516"></a><a name="p540614611516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p7647370155119"><a name="p7647370155119"></a><a name="p7647370155119"></a>Ecs.0401</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p15457196155119"><a name="p15457196155119"></a><a name="p15457196155119"></a>Failed to undo the operation performed on the port.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2777522514195"><a name="p2777522514195"></a><a name="p2777522514195"></a>Failed to delete the port because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p47560153141941"><a name="p47560153141941"></a><a name="p47560153141941"></a>For details, see the returned error message or contact technical support</p>
</td>
</tr>
<tr id="row41294231112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p179023231516"><a name="p179023231516"></a><a name="p179023231516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p61116098155119"><a name="p61116098155119"></a><a name="p61116098155119"></a>Ecs.0402</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p51456915155119"><a name="p51456915155119"></a><a name="p51456915155119"></a>Failed to undo the operation performed on the system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p565317518520"><a name="p565317518520"></a><a name="p565317518520"></a>Failed to delete system volume [%s] because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p27167190141941"><a name="p27167190141941"></a><a name="p27167190141941"></a>Contact Cinder technical support to locate the fault.</p>
</td>
</tr>
<tr id="row49633526112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p316744901516"><a name="p316744901516"></a><a name="p316744901516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p65345300155119"><a name="p65345300155119"></a><a name="p65345300155119"></a>Ecs.0403</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p58477933155119"><a name="p58477933155119"></a><a name="p58477933155119"></a>Failed to undo the operation performed on the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p3269162814195"><a name="p3269162814195"></a><a name="p3269162814195"></a>Failed to delete ECS [%s] because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p53058800141941"><a name="p53058800141941"></a><a name="p53058800141941"></a>Contact technical support to locate the fault.</p>
</td>
</tr>
<tr id="row28333309112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p51151871516"><a name="p51151871516"></a><a name="p51151871516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1794303155119"><a name="p1794303155119"></a><a name="p1794303155119"></a>Ecs.0405</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p11120822155119"><a name="p11120822155119"></a><a name="p11120822155119"></a>Failed to undo the operation performed on the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p984689714195"><a name="p984689714195"></a><a name="p984689714195"></a>Failed to delete volume %s because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p25111705141941"><a name="p25111705141941"></a><a name="p25111705141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row58225360112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p318979531519"><a name="p318979531519"></a><a name="p318979531519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p46965266155119"><a name="p46965266155119"></a><a name="p46965266155119"></a>Ecs.0501</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p46090192155119"><a name="p46090192155119"></a><a name="p46090192155119"></a>Failed to delete the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4242172514313"><a name="p4242172514313"></a><a name="p4242172514313"></a>Failed to delete ECS %s because downloading the system disk data is in progress.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p53913684141941"><a name="p53913684141941"></a><a name="p53913684141941"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row49467410192220"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p339413751519"><a name="p339413751519"></a><a name="p339413751519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p30682157192236"><a name="p30682157192236"></a><a name="p30682157192236"></a>Ecs.0502</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p2226825192236"><a name="p2226825192236"></a><a name="p2226825192236"></a>Failed to delete the private IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1040320351317"><a name="p1040320351317"></a><a name="p1040320351317"></a>Failed to roll back the EIP [%s] unbinding: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p4932256141941"><a name="p4932256141941"></a><a name="p4932256141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row8149453192223"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p472006751519"><a name="p472006751519"></a><a name="p472006751519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p12742758192236"><a name="p12742758192236"></a><a name="p12742758192236"></a>Ecs.0503</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p25530500192236"><a name="p25530500192236"></a><a name="p25530500192236"></a>Failed to query the system volume.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p6354651214195"><a name="p6354651214195"></a><a name="p6354651214195"></a>Failed to view details about the volume because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p63968481141941"><a name="p63968481141941"></a><a name="p63968481141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row39510556192226"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p495537191519"><a name="p495537191519"></a><a name="p495537191519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p22579298192236"><a name="p22579298192236"></a><a name="p22579298192236"></a>Ecs.0507</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p16983868192236"><a name="p16983868192236"></a><a name="p16983868192236"></a>Failed to delete the NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4699383614195"><a name="p4699383614195"></a><a name="p4699383614195"></a>Resource VLAN NICs cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p14064511141941"><a name="p14064511141941"></a><a name="p14064511141941"></a>Check the NIC type.</p>
</td>
</tr>
<tr id="row2086731915451"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p365244181519"><a name="p365244181519"></a><a name="p365244181519"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1253128815451"><a name="p1253128815451"></a><a name="p1253128815451"></a>Ecs.0603</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p840140915451"><a name="p840140915451"></a><a name="p840140915451"></a>Other commands are being executed. Try again 1 minute later.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p63101025949"><a name="p63101025949"></a><a name="p63101025949"></a>The running state %s of ECS %s for tenant %s is unstable.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p7068947141941"><a name="p7068947141941"></a><a name="p7068947141941"></a>Try again 1 minute later.</p>
</td>
</tr>
<tr id="row14313646204319"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p531318466436"><a name="p531318466436"></a><a name="p531318466436"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p031313462431"><a name="p031313462431"></a><a name="p031313462431"></a>Ecs.0610</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p18313446154318"><a name="p18313446154318"></a><a name="p18313446154318"></a>Resetting the password failed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p11313204610438"><a name="p11313204610438"></a><a name="p11313204610438"></a>Failed to reset the password for logging in to ECS [%s].</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p34612379"><a name="p34612379"></a><a name="p34612379"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row915192773812"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p14151027113814"><a name="p14151027113814"></a><a name="p14151027113814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1415132783814"><a name="p1415132783814"></a><a name="p1415132783814"></a>Ecs.0611</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1315182717385"><a name="p1315182717385"></a><a name="p1315182717385"></a>Requesting for a batch operation failed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p11562713381"><a name="p11562713381"></a><a name="p11562713381"></a>Batch operation failed.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p131519274386"><a name="p131519274386"></a><a name="p131519274386"></a>Rectify the fault based on the returned error information and submit the request again.</p>
</td>
</tr>
<tr id="row113974431493"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p23972437490"><a name="p23972437490"></a><a name="p23972437490"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p339784319491"><a name="p339784319491"></a><a name="p339784319491"></a>Ecs.0614</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p118985814913"><a name="p118985814913"></a><a name="p118985814913"></a>The ECS cannot be detected.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2397164313494"><a name="p2397164313494"></a><a name="p2397164313494"></a>itemNotFound: Instance xxx could not be found.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p239764317494"><a name="p239764317494"></a><a name="p239764317494"></a>Check whether the ECS exists.</p>
</td>
</tr>
<tr id="row15669111214420"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p9669212164216"><a name="p9669212164216"></a><a name="p9669212164216"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p0669121217422"><a name="p0669121217422"></a><a name="p0669121217422"></a>Ecs.0615</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p666917129424"><a name="p666917129424"></a><a name="p666917129424"></a>An error has occurred in the request from an ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2669181284211"><a name="p2669181284211"></a><a name="p2669181284211"></a>The thread list is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p410321819812"><a name="p410321819812"></a><a name="p410321819812"></a>Contact technical support to locate the fault.</p>
</td>
</tr>
<tr id="row1783237155212"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p78321570528"><a name="p78321570528"></a><a name="p78321570528"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p13832147185217"><a name="p13832147185217"></a><a name="p13832147185217"></a>Ecs.0616</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1383267115212"><a name="p1383267115212"></a><a name="p1383267115212"></a>Failed to modify an ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p10832127145214"><a name="p10832127145214"></a><a name="p10832127145214"></a>Failed to change the name of ECS [%s].</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1363825514816"><a name="p1363825514816"></a><a name="p1363825514816"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row12421165716616"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1542115571168"><a name="p1542115571168"></a><a name="p1542115571168"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p94210571963"><a name="p94210571963"></a><a name="p94210571963"></a>Ecs.0811</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1342120571613"><a name="p1342120571613"></a><a name="p1342120571613"></a>The flavor cannot be switched from Xen to KVM.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p54211057468"><a name="p54211057468"></a><a name="p54211057468"></a>The flavor cannot be resized to a new one.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1342195711613"><a name="p1342195711613"></a><a name="p1342195711613"></a>Install a driver script.</p>
</td>
</tr>
<tr id="row161481754171812"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p2406440198"><a name="p2406440198"></a><a name="p2406440198"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p340114412194"><a name="p340114412194"></a><a name="p340114412194"></a>Ecs.0902</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p81495540189"><a name="p81495540189"></a><a name="p81495540189"></a>Spot ECSs do not support Marketplace images.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p11149454191810"><a name="p11149454191810"></a><a name="p11149454191810"></a>Marketplace images cannot be used to create spot ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p654111415477"><a name="p654111415477"></a><a name="p654111415477"></a>Change another image.</p>
</td>
</tr>
<tr id="row123409564180"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p12666154820194"><a name="p12666154820194"></a><a name="p12666154820194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p26661448121917"><a name="p26661448121917"></a><a name="p26661448121917"></a>Ecs.0903</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p123401356191814"><a name="p123401356191814"></a><a name="p123401356191814"></a>Spot ECSs do not support automatic recovery.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p12340175614183"><a name="p12340175614183"></a><a name="p12340175614183"></a>Spot ECSs do not support automatic recovery.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p33381826184715"><a name="p33381826184715"></a><a name="p33381826184715"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row335495810185"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p4665549161918"><a name="p4665549161918"></a><a name="p4665549161918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p166651449201911"><a name="p166651449201911"></a><a name="p166651449201911"></a>Ecs.0904</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p335545814189"><a name="p335545814189"></a><a name="p335545814189"></a>UEFI images cannot be used to create Xen ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p183554588185"><a name="p183554588185"></a><a name="p183554588185"></a>UEFI images cannot be used to create Xen ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p6500103244711"><a name="p6500103244711"></a><a name="p6500103244711"></a>Change another flavor.</p>
</td>
</tr>
<tr id="row014551211911"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p380115811190"><a name="p380115811190"></a><a name="p380115811190"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1980115891917"><a name="p1980115891917"></a><a name="p1980115891917"></a>Ecs.0905</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1614561214199"><a name="p1614561214199"></a><a name="p1614561214199"></a>The number of tags exceeds the maximum number allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p914601231914"><a name="p914601231914"></a><a name="p914601231914"></a>The number of tags cannot be greater than 10.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p51461512161913"><a name="p51461512161913"></a><a name="p51461512161913"></a>Decrease the number of tags.</p>
</td>
</tr>
<tr id="row9434514151912"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p189219587196"><a name="p189219587196"></a><a name="p189219587196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p7892358141918"><a name="p7892358141918"></a><a name="p7892358141918"></a>Ecs.0906</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1343421401916"><a name="p1343421401916"></a><a name="p1343421401916"></a>Invalid tag attribute.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p14434171413192"><a name="p14434171413192"></a><a name="p14434171413192"></a>Invalid tag key.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p943461471915"><a name="p943461471915"></a><a name="p943461471915"></a>Create a tag again.</p>
</td>
</tr>
<tr id="row17680991910"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p14544145913194"><a name="p14544145913194"></a><a name="p14544145913194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p254445914191"><a name="p254445914191"></a><a name="p254445914191"></a>Ecs.0907</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p176959141918"><a name="p176959141918"></a><a name="p176959141918"></a>Invalid tag character set.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p147691291198"><a name="p147691291198"></a><a name="p147691291198"></a>Tag key [%s] contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p16819164154819"><a name="p16819164154819"></a><a name="p16819164154819"></a>Create a tag again.</p>
</td>
</tr>
<tr id="row17811278196"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p141576016204"><a name="p141576016204"></a><a name="p141576016204"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p121574016207"><a name="p121574016207"></a><a name="p121574016207"></a>Ecs.0908</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p581120701910"><a name="p581120701910"></a><a name="p581120701910"></a>Duplicate tag key.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p88119781913"><a name="p88119781913"></a><a name="p88119781913"></a>The tag key cannot be duplicate.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p153142434485"><a name="p153142434485"></a><a name="p153142434485"></a>Create a tag again.</p>
</td>
</tr>
<tr id="row953320151910"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1486516011206"><a name="p1486516011206"></a><a name="p1486516011206"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p48654012015"><a name="p48654012015"></a><a name="p48654012015"></a>Ecs.0909</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p5533151201914"><a name="p5533151201914"></a><a name="p5533151201914"></a>The flavor does not support the disk type.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1053314110193"><a name="p1053314110193"></a><a name="p1053314110193"></a>Flavor %s does not support disk type %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p216214924812"><a name="p216214924812"></a><a name="p216214924812"></a>Change the flavor or disk type.</p>
</td>
</tr>
<tr id="row68791754197"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1679911202017"><a name="p1679911202017"></a><a name="p1679911202017"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1179911172015"><a name="p1179911172015"></a><a name="p1179911172015"></a>Ecs.0910</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p178801156199"><a name="p178801156199"></a><a name="p178801156199"></a>Invalid NIC parameters for creating a HANA ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p14880125151913"><a name="p14880125151913"></a><a name="p14880125151913"></a>The NIC parameters for creating a HANA ECS are invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p48801958197"><a name="p48801958197"></a><a name="p48801958197"></a>Adjust the NIC parameter settings.</p>
</td>
</tr>
<tr id="row1070393161916"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p225911011237"><a name="p225911011237"></a><a name="p225911011237"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p16259151012311"><a name="p16259151012311"></a><a name="p16259151012311"></a>Ecs.0911</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1170412311919"><a name="p1170412311919"></a><a name="p1170412311919"></a>Invalid dedicated storage type of the disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p76335052916"><a name="p76335052916"></a><a name="p76335052916"></a>Disks cluster type is different.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p870493171918"><a name="p870493171918"></a><a name="p870493171918"></a>Modify parameter settings for the dedicated storage type.</p>
</td>
</tr>
<tr id="row108631751192217"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p81771611112314"><a name="p81771611112314"></a><a name="p81771611112314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p6177811162313"><a name="p6177811162313"></a><a name="p6177811162313"></a>Ecs.0912</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p686305102217"><a name="p686305102217"></a><a name="p686305102217"></a>Invalid disk encryption attribute.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1086317515228"><a name="p1086317515228"></a><a name="p1086317515228"></a>Encrypted key ID [%s] contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1686345110225"><a name="p1686345110225"></a><a name="p1686345110225"></a>Modify parameter settings for the disk encryption attribute.</p>
</td>
</tr>
<tr id="row121920582316"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p15844311172315"><a name="p15844311172315"></a><a name="p15844311172315"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p4844411122319"><a name="p4844411122319"></a><a name="p4844411122319"></a>Ecs.0913</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p1722013510231"><a name="p1722013510231"></a><a name="p1722013510231"></a>The number of ECSs to be created exceeds the maximum allowed limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p3220185122315"><a name="p3220185122315"></a><a name="p3220185122315"></a>Invalid number of ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p112206582315"><a name="p112206582315"></a><a name="p112206582315"></a>Decrease the number of ECSs to be created.</p>
</td>
</tr>
<tr id="row345652112310"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p15555171232319"><a name="p15555171232319"></a><a name="p15555171232319"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p95551712132317"><a name="p95551712132317"></a><a name="p95551712132317"></a>Ecs.0914</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p94571329238"><a name="p94571329238"></a><a name="p94571329238"></a>The length of the ECS name exceeds the maximum allowed limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p10457122142310"><a name="p10457122142310"></a><a name="p10457122142310"></a>Invalid length of ECS [%d].</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p18457172142311"><a name="p18457172142311"></a><a name="p18457172142311"></a>Change the ECS name.</p>
</td>
</tr>
<tr id="row1881613597221"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p16278101320232"><a name="p16278101320232"></a><a name="p16278101320232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p32781013112319"><a name="p32781013112319"></a><a name="p32781013112319"></a>Ecs.0915</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p10816175962212"><a name="p10816175962212"></a><a name="p10816175962212"></a>The ECS name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p118161059142210"><a name="p118161059142210"></a><a name="p118161059142210"></a>ECS name [%s] contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p390693655111"><a name="p390693655111"></a><a name="p390693655111"></a>Change the ECS name.</p>
</td>
</tr>
<tr id="row28007516112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p511912741519"><a name="p511912741519"></a><a name="p511912741519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p45318356155119"><a name="p45318356155119"></a><a name="p45318356155119"></a>Ecs.1000</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p46908237155119"><a name="p46908237155119"></a><a name="p46908237155119"></a>Failed to access the OpenStack.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p8809141746"><a name="p8809141746"></a><a name="p8809141746"></a>Failed to call the Nova V21 API to view the details about the ECS because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p35713843141941"><a name="p35713843141941"></a><a name="p35713843141941"></a>Failed to call Nova APIs. Contact technical support.</p>
</td>
</tr>
<tr id="row52119288112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p59105451519"><a name="p59105451519"></a><a name="p59105451519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p37693078155119"><a name="p37693078155119"></a><a name="p37693078155119"></a>Ecs.1001</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p33240450155119"><a name="p33240450155119"></a><a name="p33240450155119"></a>OpenStack access error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p3119935314195"><a name="p3119935314195"></a><a name="p3119935314195"></a>Failed to delete the ECS because the ECS is being deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p7140151141941"><a name="p7140151141941"></a><a name="p7140151141941"></a>The abnormal ECS is caused by an OpenStack error. In such an event, contact technical support.</p>
</td>
</tr>
<tr id="row46490106112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p138205001519"><a name="p138205001519"></a><a name="p138205001519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p5988739155119"><a name="p5988739155119"></a><a name="p5988739155119"></a>Ecs.1002</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p15325870155119"><a name="p15325870155119"></a><a name="p15325870155119"></a>OpenStack access timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p4411968814195"><a name="p4411968814195"></a><a name="p4411968814195"></a>System timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p41481352141941"><a name="p41481352141941"></a><a name="p41481352141941"></a>The task timed out. For details, contact technical support.</p>
</td>
</tr>
<tr id="row39078525112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p88150601519"><a name="p88150601519"></a><a name="p88150601519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p32488274155119"><a name="p32488274155119"></a><a name="p32488274155119"></a>Ecs.1100</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p14304533155119"><a name="p14304533155119"></a><a name="p14304533155119"></a>Failed to access the IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p8406151415514"><a name="p8406151415514"></a><a name="p8406151415514"></a>Failed to call the IAM API because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p4546317141941"><a name="p4546317141941"></a><a name="p4546317141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row9553575112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p508373101519"><a name="p508373101519"></a><a name="p508373101519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p26131071155119"><a name="p26131071155119"></a><a name="p26131071155119"></a>Ecs.1200</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p36241988155119"><a name="p36241988155119"></a><a name="p36241988155119"></a>Failed to access the VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p153272251857"><a name="p153272251857"></a><a name="p153272251857"></a>Failed to view the EIP because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p32707374141941"><a name="p32707374141941"></a><a name="p32707374141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row11985638112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p163065641519"><a name="p163065641519"></a><a name="p163065641519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p46626191155119"><a name="p46626191155119"></a><a name="p46626191155119"></a>Ecs.1201</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p18625104155119"><a name="p18625104155119"></a><a name="p18625104155119"></a>VPC access timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p25662034552"><a name="p25662034552"></a><a name="p25662034552"></a>Operation timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p58521456155516"><a name="p58521456155516"></a><a name="p58521456155516"></a>The task timed out. For details, contact technical support.</p>
</td>
</tr>
<tr id="row9879854112050"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p16347791141740"><a name="p16347791141740"></a><a name="p16347791141740"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p21710927155119"><a name="p21710927155119"></a><a name="p21710927155119"></a>Ecs.1300</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p13754647155119"><a name="p13754647155119"></a><a name="p13754647155119"></a>EVS access timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p2278787214195"><a name="p2278787214195"></a><a name="p2278787214195"></a>Failed to call the Cinder API to create a volume because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p46048359141941"><a name="p46048359141941"></a><a name="p46048359141941"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row17620121115314"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p12620111133120"><a name="p12620111133120"></a><a name="p12620111133120"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1962031113116"><a name="p1962031113116"></a><a name="p1962031113116"></a>Pdp.0001</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p11620011173119"><a name="p11620011173119"></a><a name="p11620011173119"></a>API authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p3620101113315"><a name="p3620101113315"></a><a name="p3620101113315"></a>Policy does not allow %s to be performed.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p116203117315"><a name="p116203117315"></a><a name="p116203117315"></a>Add permissions on IAM. For details, see API permissions.</p>
</td>
</tr>
<tr id="row15966316192415"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p10967016112411"><a name="p10967016112411"></a><a name="p10967016112411"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p733310401244"><a name="p733310401244"></a><a name="p733310401244"></a>Common.0024</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p11333154022412"><a name="p11333154022412"></a><a name="p11333154022412"></a>Limited by traffic control.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1033554062419"><a name="p1033554062419"></a><a name="p1033554062419"></a>The traffic has exceeded the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p2335164022419"><a name="p2335164022419"></a><a name="p2335164022419"></a>The number of concurrent requests has exceeded the upper limit. Try again later.</p>
</td>
</tr>
<tr id="row12886446192418"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p189433811440"><a name="p189433811440"></a><a name="p189433811440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p69431980442"><a name="p69431980442"></a><a name="p69431980442"></a>Common.0002</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p69436864412"><a name="p69436864412"></a><a name="p69436864412"></a>Empty request body.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p189431883444"><a name="p189431883444"></a><a name="p189431883444"></a>Request body is null!</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p39438815445"><a name="p39438815445"></a><a name="p39438815445"></a>Check the request body.</p>
</td>
</tr>
<tr id="row3918817251"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p79432864419"><a name="p79432864419"></a><a name="p79432864419"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1194311816446"><a name="p1194311816446"></a><a name="p1194311816446"></a>Common.0011</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p6943198124410"><a name="p6943198124410"></a><a name="p6943198124410"></a>Invalid job ID.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p99439824411"><a name="p99439824411"></a><a name="p99439824411"></a>Failed to obtain the job.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p294398124413"><a name="p294398124413"></a><a name="p294398124413"></a>Check whether the source of the job ID is correct.</p>
</td>
</tr>
<tr id="row64694892515"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p189434824411"><a name="p189434824411"></a><a name="p189434824411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p139431894417"><a name="p139431894417"></a><a name="p139431894417"></a>Common.0018</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p69439884417"><a name="p69439884417"></a><a name="p69439884417"></a>Invalid token, or the project ID in the token is different from that in the URL.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p164235218234"><a name="p164235218234"></a><a name="p164235218234"></a>Tenant ID in token is not the same as that in URL.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p794318810447"><a name="p794318810447"></a><a name="p794318810447"></a>Check whether the tenant token is correct.</p>
</td>
</tr>
<tr id="row288172982518"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p159431581446"><a name="p159431581446"></a><a name="p159431581446"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p4943118184420"><a name="p4943118184420"></a><a name="p4943118184420"></a>Common.0020</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p5943286447"><a name="p5943286447"></a><a name="p5943286447"></a>Failed to retry the task.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1994319816447"><a name="p1994319816447"></a><a name="p1994319816447"></a>Failed to call the redo API.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p2094411811449"><a name="p2094411811449"></a><a name="p2094411811449"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row151122719252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1994428154410"><a name="p1994428154410"></a><a name="p1994428154410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p109448818447"><a name="p109448818447"></a><a name="p109448818447"></a>Common.0021</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p159441384442"><a name="p159441384442"></a><a name="p159441384442"></a>An error has occurred in job query.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p194413804415"><a name="p194413804415"></a><a name="p194413804415"></a>Failed to obtain the job.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p99447864410"><a name="p99447864410"></a><a name="p99447864410"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row899312492511"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p594415815448"><a name="p594415815448"></a><a name="p594415815448"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1394412844412"><a name="p1394412844412"></a><a name="p1394412844412"></a>Common.0022</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p494419819444"><a name="p494419819444"></a><a name="p494419819444"></a>An error has occurred in job submission.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1994411834418"><a name="p1994411834418"></a><a name="p1994411834418"></a>Job failed.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p594417814441"><a name="p594417814441"></a><a name="p594417814441"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row3833132215251"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p7944108164417"><a name="p7944108164417"></a><a name="p7944108164417"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p894419811449"><a name="p894419811449"></a><a name="p894419811449"></a>Common.0999</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p894411804416"><a name="p894411804416"></a><a name="p894411804416"></a>Task terminated.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p79448815449"><a name="p79448815449"></a><a name="p79448815449"></a>The system was down.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p494517810445"><a name="p494517810445"></a><a name="p494517810445"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row14841151815251"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p1294548194410"><a name="p1294548194410"></a><a name="p1294548194410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p594518804411"><a name="p594518804411"></a><a name="p594518804411"></a>Common.0025</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p17945128184411"><a name="p17945128184411"></a><a name="p17945128184411"></a>An error has occurred in job query.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p1394515894412"><a name="p1394515894412"></a><a name="p1394515894412"></a>Failed to obtain the job because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p2945128204410"><a name="p2945128204410"></a><a name="p2945128204410"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row17740161632519"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p169453814445"><a name="p169453814445"></a><a name="p169453814445"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p3945486446"><a name="p3945486446"></a><a name="p3945486446"></a>Common.0026</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p149451782443"><a name="p149451782443"></a><a name="p149451782443"></a>An error occurred in AZ query.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p18945168144418"><a name="p18945168144418"></a><a name="p18945168144418"></a>Fail to obtain the AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p1294515814446"><a name="p1294515814446"></a><a name="p1294515814446"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row162891492512"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p179455874415"><a name="p179455874415"></a><a name="p179455874415"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1945178174416"><a name="p1945178174416"></a><a name="p1945178174416"></a>Common.0013</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p159450813442"><a name="p159450813442"></a><a name="p159450813442"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p8945681445"><a name="p8945681445"></a><a name="p8945681445"></a>Do not perform this operation.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p199452815444"><a name="p199452815444"></a><a name="p199452815444"></a>Check whether the tenant token is correct.</p>
</td>
</tr>
<tr id="row33221112182519"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p794515811448"><a name="p794515811448"></a><a name="p794515811448"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p1594511874414"><a name="p1594511874414"></a><a name="p1594511874414"></a>Common.0001</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p159451586445"><a name="p159451586445"></a><a name="p159451586445"></a>A system exception occurred.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p29450834413"><a name="p29450834413"></a><a name="p29450834413"></a>System error.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p3945380444"><a name="p3945380444"></a><a name="p3945380444"></a>For details, see the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row491216412515"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="p8947168144418"><a name="p8947168144418"></a><a name="p8947168144418"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p199474844419"><a name="p199474844419"></a><a name="p199474844419"></a>Common.1503</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.6.1.3 "><p id="p18947168164417"><a name="p18947168164417"></a><a name="p18947168164417"></a>Limited by API traffic control.</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.6.1.4 "><p id="p12947887448"><a name="p12947887448"></a><a name="p12947887448"></a>An error has occurred in API traffic control because %s.</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.6.1.5 "><p id="p199471689444"><a name="p199471689444"></a><a name="p199471689444"></a>Too many APIs are being executed. Try again later.</p>
</td>
</tr>
</tbody>
</table>

