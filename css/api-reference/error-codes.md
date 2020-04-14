# Error Codes<a name="css_03_0013"></a>

If an error occurs in API calling, no result is returned. Identify the cause of error based on the error codes of each API. When the API calling fails, HTTPS status code 4_xx_  or 5_xx_  is returned. The returned message body contains the specific error code and error information. If you are unable to identify the cause of an error, contact  customer service and provide the error code so that we can help you solve the problem as soon as possible.

<a name="table65737292"></a>
<table><thead align="left"><tr id="row27077540"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.1"><p id="p18580737"><a name="p18580737"></a><a name="p18580737"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.2"><p id="p45797138"><a name="p45797138"></a><a name="p45797138"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="36.980000000000004%" id="mcps1.1.5.1.3"><p id="p28644761"><a name="p28644761"></a><a name="p28644761"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="37.019999999999996%" id="mcps1.1.5.1.4"><p id="p17603144772714"><a name="p17603144772714"></a><a name="p17603144772714"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row38524289"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p25879650"><a name="p25879650"></a><a name="p25879650"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p33459681"><a name="p33459681"></a><a name="p33459681"></a>ES.0001</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p15876907"><a name="p15876907"></a><a name="p15876907"></a>Parameter error</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p360374772715"><a name="p360374772715"></a><a name="p360374772715"></a>Check the parameter settings according to the returned information.</p>
</td>
</tr>
<tr id="row8059334"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p62618006"><a name="p62618006"></a><a name="p62618006"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p48826322"><a name="p48826322"></a><a name="p48826322"></a>ES.0005</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p38893755"><a name="p38893755"></a><a name="p38893755"></a>Server error</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1660364710271"><a name="p1660364710271"></a><a name="p1660364710271"></a>Contact </p>
</td>
</tr>
<tr id="row14499481"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p37840511"><a name="p37840511"></a><a name="p37840511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p33607346"><a name="p33607346"></a><a name="p33607346"></a>ES.0006</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p45182569"><a name="p45182569"></a><a name="p45182569"></a>The request body is empty. Enter a request parameter.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p14603114782711"><a name="p14603114782711"></a><a name="p14603114782711"></a>Enter the request parameters.</p>
</td>
</tr>
<tr id="row3989940"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p5541955"><a name="p5541955"></a><a name="p5541955"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p976543314611"><a name="p976543314611"></a><a name="p976543314611"></a>ES.0011</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p46245228"><a name="p46245228"></a><a name="p46245228"></a>This operation cannot be performed because another operation is being performed on the instance or the instance is faulty. Please try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1160314762712"><a name="p1160314762712"></a><a name="p1160314762712"></a>Try again later.</p>
</td>
</tr>
<tr id="row13553869"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p7689721"><a name="p7689721"></a><a name="p7689721"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p24121565"><a name="p24121565"></a><a name="p24121565"></a>ES.0015</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p18887690"><a name="p18887690"></a><a name="p18887690"></a>Resource not found or permission denied.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p46039473274"><a name="p46039473274"></a><a name="p46039473274"></a>Change the resource ID or check the access permission.</p>
</td>
</tr>
<tr id="row35771490"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p17053313"><a name="p17053313"></a><a name="p17053313"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p11809597"><a name="p11809597"></a><a name="p11809597"></a>ES.0022</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p39141076"><a name="p39141076"></a><a name="p39141076"></a>The instance does not exist or has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1560364710271"><a name="p1560364710271"></a><a name="p1560364710271"></a>Change the instance ID.</p>
</td>
</tr>
<tr id="row14746191935316"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p760102914537"><a name="p760102914537"></a><a name="p760102914537"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p460629115318"><a name="p460629115318"></a><a name="p460629115318"></a>ES.0032</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p14601929105316"><a name="p14601929105316"></a><a name="p14601929105316"></a>The current user has no operation permissions.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1574172965313"><a name="p1574172965313"></a><a name="p1574172965313"></a>Check the permissions.</p>
</td>
</tr>
<tr id="row68880101345"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p38891510123417"><a name="p38891510123417"></a><a name="p38891510123417"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p78891410163418"><a name="p78891410163418"></a><a name="p78891410163418"></a>ES.0045</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p1288931013341"><a name="p1288931013341"></a><a name="p1288931013341"></a>The token is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1960314717273"><a name="p1960314717273"></a><a name="p1960314717273"></a>Obtain the token again.</p>
</td>
</tr>
<tr id="row66059488"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p27263117"><a name="p27263117"></a><a name="p27263117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p49218346"><a name="p49218346"></a><a name="p49218346"></a>ES.1112</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p60828848"><a name="p60828848"></a><a name="p60828848"></a>The number of instances has reached the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p196036474271"><a name="p196036474271"></a><a name="p196036474271"></a>Delete some clusters or increase the quota.</p>
</td>
</tr>
<tr id="row1419913432337"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p11199643173319"><a name="p11199643173319"></a><a name="p11199643173319"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p919994313310"><a name="p919994313310"></a><a name="p919994313310"></a>ES.3011</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p12199343173315"><a name="p12199343173315"></a><a name="p12199343173315"></a>Invalid retention duration of the backup</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1860324712714"><a name="p1860324712714"></a><a name="p1860324712714"></a>Change the allowed retention duration.</p>
</td>
</tr>
<tr id="row10333431825"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p733194317213"><a name="p733194317213"></a><a name="p733194317213"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p4331843425"><a name="p4331843425"></a><a name="p4331843425"></a>ES.3027</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p833114317216"><a name="p833114317216"></a><a name="p833114317216"></a>The cluster does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p11603164714273"><a name="p11603164714273"></a><a name="p11603164714273"></a>Check whether the cluster ID is correct.</p>
</td>
</tr>
<tr id="row16452903"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p36446461"><a name="p36446461"></a><a name="p36446461"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p57616766"><a name="p57616766"></a><a name="p57616766"></a>ES.5007</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p66482253"><a name="p66482253"></a><a name="p66482253"></a>The selected flavor does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p126031147132720"><a name="p126031147132720"></a><a name="p126031147132720"></a>Check whether the specifications are correct.</p>
</td>
</tr>
<tr id="row913632734211"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p181362278423"><a name="p181362278423"></a><a name="p181362278423"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p2013632744216"><a name="p2013632744216"></a><a name="p2013632744216"></a>ES.5009</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p213614273425"><a name="p213614273425"></a><a name="p213614273425"></a>The hard disk size is beyond the valid range.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p660310471273"><a name="p660310471273"></a><a name="p660310471273"></a>Change the disk size.</p>
</td>
</tr>
<tr id="row16928338"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p1657863"><a name="p1657863"></a><a name="p1657863"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p29018124"><a name="p29018124"></a><a name="p29018124"></a>ES.5014</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p69227"><a name="p69227"></a><a name="p69227"></a>Invalid VPC ID.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p960314712279"><a name="p960314712279"></a><a name="p960314712279"></a>Check whether the VPC ID is correct.</p>
</td>
</tr>
<tr id="row623043"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p61256166"><a name="p61256166"></a><a name="p61256166"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p50466518"><a name="p50466518"></a><a name="p50466518"></a>ES.5015</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p62802394"><a name="p62802394"></a><a name="p62802394"></a>Invalid subnet ID.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1603144772716"><a name="p1603144772716"></a><a name="p1603144772716"></a>Check whether the subnet ID is correct.</p>
</td>
</tr>
<tr id="row51718129"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p20228817"><a name="p20228817"></a><a name="p20228817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p28418891"><a name="p28418891"></a><a name="p28418891"></a>ES.5021</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p27921517"><a name="p27921517"></a><a name="p27921517"></a>The VPC does not exist or does not belong to the user.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p2603647162714"><a name="p2603647162714"></a><a name="p2603647162714"></a>Check whether the VPC is correct.</p>
</td>
</tr>
<tr id="row2854726"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p6488958"><a name="p6488958"></a><a name="p6488958"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p29906272"><a name="p29906272"></a><a name="p29906272"></a>ES.5023</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p55843593"><a name="p55843593"></a><a name="p55843593"></a>The security group does not exist or does not belong to the VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p26031947152714"><a name="p26031947152714"></a><a name="p26031947152714"></a>Check whether the security group is correct.</p>
</td>
</tr>
<tr id="row15370329161420"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p3370102981417"><a name="p3370102981417"></a><a name="p3370102981417"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p1037062911149"><a name="p1037062911149"></a><a name="p1037062911149"></a>ES.5157</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p113701529191418"><a name="p113701529191418"></a><a name="p113701529191418"></a>The CIDR does not exist or is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1937062961413"><a name="p1937062961413"></a><a name="p1937062961413"></a>Check whether there are subnets in the VPC.</p>
</td>
</tr>
<tr id="row17267710154517"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p9267181014512"><a name="p9267181014512"></a><a name="p9267181014512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p6267310184511"><a name="p6267310184511"></a><a name="p6267310184511"></a>ES.5036</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p226711074510"><a name="p226711074510"></a><a name="p226711074510"></a>The engine does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p26031947132715"><a name="p26031947132715"></a><a name="p26031947132715"></a>Check whether the <span class="parmname" id="parmname520017231173"><a name="parmname520017231173"></a><a name="parmname520017231173"></a><b>datastore</b></span> parameter setting is correct.</p>
</td>
</tr>
<tr id="row49919034710"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p799150194717"><a name="p799150194717"></a><a name="p799150194717"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p189930154711"><a name="p189930154711"></a><a name="p189930154711"></a>ES.5047</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p69910020471"><a name="p69910020471"></a><a name="p69910020471"></a>The number of instances is beyond the valid range.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1960310477273"><a name="p1960310477273"></a><a name="p1960310477273"></a>Check whether the number of instances is within the range.</p>
</td>
</tr>
<tr id="row65870306"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p61105663"><a name="p61105663"></a><a name="p61105663"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a>ES.5050</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p50611656"><a name="p50611656"></a><a name="p50611656"></a>The cluster name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p16031747202716"><a name="p16031747202716"></a><a name="p16031747202716"></a>Change the cluster name.</p>
</td>
</tr>
<tr id="row52851724"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p8662426"><a name="p8662426"></a><a name="p8662426"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p53131231"><a name="p53131231"></a><a name="p53131231"></a>ES.5052</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p30567910"><a name="p30567910"></a><a name="p30567910"></a>Invalid value of the AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p66031247122710"><a name="p66031247122710"></a><a name="p66031247122710"></a>Change the AZ.</p>
</td>
</tr>
<tr id="row61529894"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p37818817"><a name="p37818817"></a><a name="p37818817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p17865493"><a name="p17865493"></a><a name="p17865493"></a>ES.5055</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p43425297"><a name="p43425297"></a><a name="p43425297"></a>Invalid flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p17603194713276"><a name="p17603194713276"></a><a name="p17603194713276"></a>Modify the specifications.</p>
</td>
</tr>
<tr id="row13875810"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p39571581"><a name="p39571581"></a><a name="p39571581"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p50198807"><a name="p50198807"></a><a name="p50198807"></a>ES.5061</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p51181499"><a name="p51181499"></a><a name="p51181499"></a>The hard disk type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p18603124732716"><a name="p18603124732716"></a><a name="p18603124732716"></a>Change the hard disk type.</p>
</td>
</tr>
<tr id="row11709955"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p56478042"><a name="p56478042"></a><a name="p56478042"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p8982304"><a name="p8982304"></a><a name="p8982304"></a>ES.5071</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p11318680"><a name="p11318680"></a><a name="p11318680"></a>The disk type does not match that in the XML configuration file.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1460324715277"><a name="p1460324715277"></a><a name="p1460324715277"></a>Change the hard disk type.</p>
</td>
</tr>
<tr id="row34759260"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p19590229"><a name="p19590229"></a><a name="p19590229"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p64036700"><a name="p64036700"></a><a name="p64036700"></a>ES.5072</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p43304686"><a name="p43304686"></a><a name="p43304686"></a>The security group ID is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p15603647182720"><a name="p15603647182720"></a><a name="p15603647182720"></a>Change the security group ID.</p>
</td>
</tr>
<tr id="row54197854"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p49359659"><a name="p49359659"></a><a name="p49359659"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p27950026"><a name="p27950026"></a><a name="p27950026"></a>ES.5074</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p38709481"><a name="p38709481"></a><a name="p38709481"></a>The subnet does not belong to the VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p20603154710275"><a name="p20603154710275"></a><a name="p20603154710275"></a>Change the subnet ID.</p>
</td>
</tr>
<tr id="row184311510124912"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p9431181054913"><a name="p9431181054913"></a><a name="p9431181054913"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p17431171054919"><a name="p17431171054919"></a><a name="p17431171054919"></a>ES.5077</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p743112109491"><a name="p743112109491"></a><a name="p743112109491"></a>Invalid cluster name.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p460374792720"><a name="p460374792720"></a><a name="p460374792720"></a>Change the cluster name.</p>
</td>
</tr>
<tr id="row165124406493"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p1151216407493"><a name="p1151216407493"></a><a name="p1151216407493"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p7512174034916"><a name="p7512174034916"></a><a name="p7512174034916"></a>ES.5078</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p1551284084912"><a name="p1551284084912"></a><a name="p1551284084912"></a>The hard disk size is beyond the valid range.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p4603144792710"><a name="p4603144792710"></a><a name="p4603144792710"></a>Change the disk size.</p>
</td>
</tr>
<tr id="row35455590"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p24807479"><a name="p24807479"></a><a name="p24807479"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p53330552"><a name="p53330552"></a><a name="p53330552"></a>ES.5092</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p63248778"><a name="p63248778"></a><a name="p63248778"></a>Invalid hard disk information.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p66031147112713"><a name="p66031147112713"></a><a name="p66031147112713"></a>Modify the hard disk information.</p>
</td>
</tr>
<tr id="row193291113165110"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p83295138517"><a name="p83295138517"></a><a name="p83295138517"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p532916137519"><a name="p532916137519"></a><a name="p532916137519"></a>ES.5093</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p63291131513"><a name="p63291131513"></a><a name="p63291131513"></a>Invalid specification information.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p116031247112710"><a name="p116031247112710"></a><a name="p116031247112710"></a>Modify the specification information.</p>
</td>
</tr>
<tr id="row65126334341"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p251218336347"><a name="p251218336347"></a><a name="p251218336347"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p12512183313411"><a name="p12512183313411"></a><a name="p12512183313411"></a>ES.5130</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p19512133363414"><a name="p19512133363414"></a><a name="p19512133363414"></a>The agency name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1560314471279"><a name="p1560314471279"></a><a name="p1560314471279"></a>Change the agency name.</p>
</td>
</tr>
<tr id="row184021113558"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p1340310119554"><a name="p1340310119554"></a><a name="p1340310119554"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p14403813556"><a name="p14403813556"></a><a name="p14403813556"></a>ES.5156</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p1640317115551"><a name="p1640317115551"></a><a name="p1640317115551"></a>Invalid key ID.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p440491155510"><a name="p440491155510"></a><a name="p440491155510"></a>Change the key ID.</p>
</td>
</tr>
<tr id="row134275474555"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p5427124715516"><a name="p5427124715516"></a><a name="p5427124715516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p3427347135518"><a name="p3427347135518"></a><a name="p3427347135518"></a>ES.5158</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p3219829113314"><a name="p3219829113314"></a><a name="p3219829113314"></a>Invalid value for the parameter related to disk encryption.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p774518155343"><a name="p774518155343"></a><a name="p774518155343"></a>Change the value of the parameter related to disk encryption to <strong id="b187053520317"><a name="b187053520317"></a><a name="b187053520317"></a>0</strong> or <strong id="b1276501234"><a name="b1276501234"></a><a name="b1276501234"></a>1</strong>.</p>
</td>
</tr>
<tr id="row55160823"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.1 "><p id="p59167590"><a name="p59167590"></a><a name="p59167590"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p38841670"><a name="p38841670"></a><a name="p38841670"></a>ES.9999</p>
</td>
<td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.1.5.1.3 "><p id="p27845503"><a name="p27845503"></a><a name="p27845503"></a>Request processing failed.</p>
</td>
<td class="cellrowborder" valign="top" width="37.019999999999996%" headers="mcps1.1.5.1.4 "><p id="p1560313479274"><a name="p1560313479274"></a><a name="p1560313479274"></a>Contact customer service</p>
</td>
</tr>
</tbody>
</table>

