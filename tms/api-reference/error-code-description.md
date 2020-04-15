# Error Code Description<a name="EN-US_TOPIC_0170553651"></a>

## Function Description<a name="see857f4c2738499ab7a7d40641a73552"></a>

If the returned status code of a TMS API is  **400**, the customized error information will also be returned. This section describes the meaning of each TMS error code.

## Response Format<a name="s5fa02dddd07443fc999aa8b2be865c86"></a>

```
STATUS CODE 400
     {
       "error_code": "TMS.0009",
       "error_msg": "Key is invalid." 
     }
```

## Error Code Description<a name="sc7bedeee93f54142a8041449f3c4696d"></a>

<a name="table35611529112856"></a>
<table><thead align="left"><tr id="row17652632112856"><th class="cellrowborder" valign="top" width="10.760000000000002%" id="mcps1.1.7.1.1"><p id="p20577077112856"><a name="p20577077112856"></a><a name="p20577077112856"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="9.400000000000002%" id="mcps1.1.7.1.2"><p id="p56130522112856"><a name="p56130522112856"></a><a name="p56130522112856"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="14.230000000000004%" id="mcps1.1.7.1.3"><p id="p50278448112856"><a name="p50278448112856"></a><a name="p50278448112856"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="17.160000000000004%" id="mcps1.1.7.1.4"><p id="p46022494112856"><a name="p46022494112856"></a><a name="p46022494112856"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="20.520000000000003%" id="mcps1.1.7.1.5"><p id="p36834573112856"><a name="p36834573112856"></a><a name="p36834573112856"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="27.930000000000003%" id="mcps1.1.7.1.6"><p id="p30810469112856"><a name="p30810469112856"></a><a name="p30810469112856"></a>Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="row12620045112856"><td class="cellrowborder" rowspan="14" valign="top" width="10.760000000000002%" headers="mcps1.1.7.1.1 "><p id="p15590701112856"><a name="p15590701112856"></a><a name="p15590701112856"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="9.400000000000002%" headers="mcps1.1.7.1.2 "><p id="p54887278112856"><a name="p54887278112856"></a><a name="p54887278112856"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="14.230000000000004%" headers="mcps1.1.7.1.3 "><p id="p16684535112856"><a name="p16684535112856"></a><a name="p16684535112856"></a>TMS.0001</p>
</td>
<td class="cellrowborder" valign="top" width="17.160000000000004%" headers="mcps1.1.7.1.4 "><p id="p9270129112856"><a name="p9270129112856"></a><a name="p9270129112856"></a>System error</p>
</td>
<td class="cellrowborder" valign="top" width="20.520000000000003%" headers="mcps1.1.7.1.5 "><p id="p12683012112856"><a name="p12683012112856"></a><a name="p12683012112856"></a>System error.</p>
</td>
<td class="cellrowborder" valign="top" width="27.930000000000003%" headers="mcps1.1.7.1.6 "><p id="p20691031112856"><a name="p20691031112856"></a><a name="p20691031112856"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row52001552112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p51376166112856"><a name="p51376166112856"></a><a name="p51376166112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p719954112856"><a name="p719954112856"></a><a name="p719954112856"></a>TMS.0002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p58316281112856"><a name="p58316281112856"></a><a name="p58316281112856"></a>Invalid request from the client</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p25998341112856"><a name="p25998341112856"></a><a name="p25998341112856"></a>Bad request.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p25490910112856"><a name="p25490910112856"></a><a name="p25490910112856"></a>Enter correct parameters.</p>
</td>
</tr>
<tr id="row28091603112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p60827337112856"><a name="p60827337112856"></a><a name="p60827337112856"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p28067264112856"><a name="p28067264112856"></a><a name="p28067264112856"></a>TMS.0003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p58855903112856"><a name="p58855903112856"></a><a name="p58855903112856"></a>Authentication fails or the valid authentication information is not provided.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p2598863112856"><a name="p2598863112856"></a><a name="p2598863112856"></a>The user is unauthorized.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p9181368112856"><a name="p9181368112856"></a><a name="p9181368112856"></a>Check whether the username or password for obtaining the token is correct.</p>
</td>
</tr>
<tr id="row15523449112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p49439817112856"><a name="p49439817112856"></a><a name="p49439817112856"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p45202213112856"><a name="p45202213112856"></a><a name="p45202213112856"></a>TMS.0004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p37500662112856"><a name="p37500662112856"></a><a name="p37500662112856"></a>The authentication information is incorrect or the service invoker does not have sufficient permissions.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p17654820112856"><a name="p17654820112856"></a><a name="p17654820112856"></a>You do not have permissions to perform the operation.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p20754326112856"><a name="p20754326112856"></a><a name="p20754326112856"></a>Check whether the username, password, or the user permissions for obtaining the token are correct.</p>
</td>
</tr>
<tr id="row52571213112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p30409824112856"><a name="p30409824112856"></a><a name="p30409824112856"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p47276717112856"><a name="p47276717112856"></a><a name="p47276717112856"></a>TMS.0005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p4208858112856"><a name="p4208858112856"></a><a name="p4208858112856"></a>The requested resource cannot be found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p5373199112856"><a name="p5373199112856"></a><a name="p5373199112856"></a>The resources requested cannot be found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p32575989112856"><a name="p32575989112856"></a><a name="p32575989112856"></a>Provide a correct resource ID.</p>
</td>
</tr>
<tr id="row24748450112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p58467411112856"><a name="p58467411112856"></a><a name="p58467411112856"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p38239882112856"><a name="p38239882112856"></a><a name="p38239882112856"></a>TMS.0006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p10422700112856"><a name="p10422700112856"></a><a name="p10422700112856"></a>The numbers of requests are too many.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p38932387112856"><a name="p38932387112856"></a><a name="p38932387112856"></a>The request is <strong id="b8976165610372"><a name="b8976165610372"></a><a name="b8976165610372"></a>Too</strong> <strong id="b497685614374"><a name="b497685614374"></a><a name="b497685614374"></a>much</strong>, try again later.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p61770131112856"><a name="p61770131112856"></a><a name="p61770131112856"></a>Reduce the number of concurrent requests or wait for a retry.</p>
</td>
</tr>
<tr id="row19060271112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p378132112856"><a name="p378132112856"></a><a name="p378132112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p30628717112856"><a name="p30628717112856"></a><a name="p30628717112856"></a>TMS.0007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p65007011112856"><a name="p65007011112856"></a><a name="p65007011112856"></a><strong id="b84235270693614"><a name="b84235270693614"></a><a name="b84235270693614"></a>Limit</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p31076509112856"><a name="p31076509112856"></a><a name="p31076509112856"></a><strong id="b11253127112856"><a name="b11253127112856"></a><a name="b11253127112856"></a>Limit</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p39088099112856"><a name="p39088099112856"></a><a name="p39088099112856"></a>Enter a correct <strong id="b84235270694459"><a name="b84235270694459"></a><a name="b84235270694459"></a>Limit</strong> value.</p>
</td>
</tr>
<tr id="row16248575112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p41066166112856"><a name="p41066166112856"></a><a name="p41066166112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p38025170112856"><a name="p38025170112856"></a><a name="p38025170112856"></a>TMS.0008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p60139963112856"><a name="p60139963112856"></a><a name="p60139963112856"></a><strong id="b84235270693614_1"><a name="b84235270693614_1"></a><a name="b84235270693614_1"></a>Marker</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p39498840112856"><a name="p39498840112856"></a><a name="p39498840112856"></a><strong id="b19945246112856"><a name="b19945246112856"></a><a name="b19945246112856"></a>Marker</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p4952229112856"><a name="p4952229112856"></a><a name="p4952229112856"></a>Enter a correct <strong id="b84235270694459_1"><a name="b84235270694459_1"></a><a name="b84235270694459_1"></a>Marker</strong> value.</p>
</td>
</tr>
<tr id="row44570064112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p53405435112856"><a name="p53405435112856"></a><a name="p53405435112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p30872954112856"><a name="p30872954112856"></a><a name="p30872954112856"></a>TMS.0009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p17681334112856"><a name="p17681334112856"></a><a name="p17681334112856"></a><strong id="b84235270693614_2"><a name="b84235270693614_2"></a><a name="b84235270693614_2"></a>Key</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p22901910112856"><a name="p22901910112856"></a><a name="p22901910112856"></a><strong id="b4790599112856"><a name="b4790599112856"></a><a name="b4790599112856"></a>Key</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p52494233112856"><a name="p52494233112856"></a><a name="p52494233112856"></a>Enter a correct <strong id="b84235270694459_2"><a name="b84235270694459_2"></a><a name="b84235270694459_2"></a>Key</strong> value.</p>
</td>
</tr>
<tr id="row2686051112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p16243617112856"><a name="p16243617112856"></a><a name="p16243617112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p40664611112856"><a name="p40664611112856"></a><a name="p40664611112856"></a>TMS.0010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p5499218112856"><a name="p5499218112856"></a><a name="p5499218112856"></a><strong id="b84235270693614_3"><a name="b84235270693614_3"></a><a name="b84235270693614_3"></a>Value</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p42783509112856"><a name="p42783509112856"></a><a name="p42783509112856"></a><strong id="b179483123384"><a name="b179483123384"></a><a name="b179483123384"></a>Value</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p50665599112856"><a name="p50665599112856"></a><a name="p50665599112856"></a>Enter a correct <strong id="b84235270694459_3"><a name="b84235270694459_3"></a><a name="b84235270694459_3"></a>Value</strong> value.</p>
</td>
</tr>
<tr id="row53337209112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p25346666112856"><a name="p25346666112856"></a><a name="p25346666112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p39814031112856"><a name="p39814031112856"></a><a name="p39814031112856"></a>TMS.0011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p3711056112856"><a name="p3711056112856"></a><a name="p3711056112856"></a><strong id="b84235270693614_4"><a name="b84235270693614_4"></a><a name="b84235270693614_4"></a>Action</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p32160151112856"><a name="p32160151112856"></a><a name="p32160151112856"></a><strong id="b21005903112856"><a name="b21005903112856"></a><a name="b21005903112856"></a>Action</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p23756567112856"><a name="p23756567112856"></a><a name="p23756567112856"></a>Enter a correct <strong id="b84235270694459_4"><a name="b84235270694459_4"></a><a name="b84235270694459_4"></a>Action</strong> value.</p>
</td>
</tr>
<tr id="row12482512112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p4450580112856"><a name="p4450580112856"></a><a name="p4450580112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p24952700112856"><a name="p24952700112856"></a><a name="p24952700112856"></a>TMS.0012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p7902833112856"><a name="p7902833112856"></a><a name="p7902833112856"></a><strong id="b96116407695025"><a name="b96116407695025"></a><a name="b96116407695025"></a>Tags</strong> is an empty array.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p36149722112856"><a name="p36149722112856"></a><a name="p36149722112856"></a><strong id="b56912046112856"><a name="b56912046112856"></a><a name="b56912046112856"></a>Tags</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p46472993112856"><a name="p46472993112856"></a><a name="p46472993112856"></a>Enter a correct <strong id="b84235270694459_5"><a name="b84235270694459_5"></a><a name="b84235270694459_5"></a>Tags</strong> value.</p>
</td>
</tr>
<tr id="row15603754112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p55944544112856"><a name="p55944544112856"></a><a name="p55944544112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p35214252112856"><a name="p35214252112856"></a><a name="p35214252112856"></a>TMS.0013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p33782131112856"><a name="p33782131112856"></a><a name="p33782131112856"></a>Elements in <strong id="b84235270694828"><a name="b84235270694828"></a><a name="b84235270694828"></a>Tags</strong> are empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p51998111112856"><a name="p51998111112856"></a><a name="p51998111112856"></a>Empty element in <strong id="b16308331163813"><a name="b16308331163813"></a><a name="b16308331163813"></a>Tags</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p57224285112856"><a name="p57224285112856"></a><a name="p57224285112856"></a>Enter a correct <strong id="b84235270694459_6"><a name="b84235270694459_6"></a><a name="b84235270694459_6"></a>Tags</strong> value.</p>
</td>
</tr>
<tr id="row45256517112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p41899279112856"><a name="p41899279112856"></a><a name="p41899279112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p38398429112856"><a name="p38398429112856"></a><a name="p38398429112856"></a>TMS.0014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p23265048112856"><a name="p23265048112856"></a><a name="p23265048112856"></a><strong id="b84235270693614_5"><a name="b84235270693614_5"></a><a name="b84235270693614_5"></a>Values</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p5420711112856"><a name="p5420711112856"></a><a name="p5420711112856"></a><strong id="b19580203883812"><a name="b19580203883812"></a><a name="b19580203883812"></a>Values</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p59384459112856"><a name="p59384459112856"></a><a name="p59384459112856"></a>Enter a correct <strong id="b84235270694459_7"><a name="b84235270694459_7"></a><a name="b84235270694459_7"></a>Values</strong> value.</p>
</td>
</tr>
<tr id="row64698083112856"><td class="cellrowborder" rowspan="11" valign="top" width="10.760000000000002%" headers="mcps1.1.7.1.1 "><p id="p6053343112856"><a name="p6053343112856"></a><a name="p6053343112856"></a>Predefined tag</p>
</td>
<td class="cellrowborder" valign="top" width="9.400000000000002%" headers="mcps1.1.7.1.2 "><p id="p20558800112856"><a name="p20558800112856"></a><a name="p20558800112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="14.230000000000004%" headers="mcps1.1.7.1.3 "><p id="p54650142112856"><a name="p54650142112856"></a><a name="p54650142112856"></a>TMS.1001</p>
</td>
<td class="cellrowborder" valign="top" width="17.160000000000004%" headers="mcps1.1.7.1.4 "><p id="p64585392112856"><a name="p64585392112856"></a><a name="p64585392112856"></a>The number of predefined tags exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="20.520000000000003%" headers="mcps1.1.7.1.5 "><p id="p64034287112856"><a name="p64034287112856"></a><a name="p64034287112856"></a>The number of predefine tag exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="27.930000000000003%" headers="mcps1.1.7.1.6 "><p id="p19394754112856"><a name="p19394754112856"></a><a name="p19394754112856"></a>Reduce the number of predefined tags.</p>
</td>
</tr>
<tr id="row40335063112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p45914660112856"><a name="p45914660112856"></a><a name="p45914660112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p28099961112856"><a name="p28099961112856"></a><a name="p28099961112856"></a>TMS.1002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p61504383112856"><a name="p61504383112856"></a><a name="p61504383112856"></a><strong id="b84235270694956"><a name="b84235270694956"></a><a name="b84235270694956"></a>Old_tag</strong> cannot be found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p15799133112856"><a name="p15799133112856"></a><a name="p15799133112856"></a><strong id="b7974477112856"><a name="b7974477112856"></a><a name="b7974477112856"></a>Old_tag</strong> cannot be found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p41952932112856"><a name="p41952932112856"></a><a name="p41952932112856"></a>Check parameter <strong id="b15847958139532"><a name="b15847958139532"></a><a name="b15847958139532"></a>Old_tag</strong>.</p>
</td>
</tr>
<tr id="row42032068112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p49154332112856"><a name="p49154332112856"></a><a name="p49154332112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p22077932112856"><a name="p22077932112856"></a><a name="p22077932112856"></a>TMS.1003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p43482077112856"><a name="p43482077112856"></a><a name="p43482077112856"></a><strong id="b8423527069509"><a name="b8423527069509"></a><a name="b8423527069509"></a>New_tag</strong> already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p32387350112856"><a name="p32387350112856"></a><a name="p32387350112856"></a><strong id="b23050702112856"><a name="b23050702112856"></a><a name="b23050702112856"></a>New_tag</strong> already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p55167559112856"><a name="p55167559112856"></a><a name="p55167559112856"></a>Check parameter <strong id="b84235270693643"><a name="b84235270693643"></a><a name="b84235270693643"></a>New-tag</strong>.</p>
</td>
</tr>
<tr id="row26745987112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p18941318112856"><a name="p18941318112856"></a><a name="p18941318112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p57851761112856"><a name="p57851761112856"></a><a name="p57851761112856"></a>TMS.1004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p55481069112856"><a name="p55481069112856"></a><a name="p55481069112856"></a><strong id="b96116407695025_1"><a name="b96116407695025_1"></a><a name="b96116407695025_1"></a>Old_tag</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p64781601112856"><a name="p64781601112856"></a><a name="p64781601112856"></a><strong id="b46163504112856"><a name="b46163504112856"></a><a name="b46163504112856"></a>Old_tag</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p48256364112856"><a name="p48256364112856"></a><a name="p48256364112856"></a>Ensure that parameter <strong id="b842352706142422"><a name="b842352706142422"></a><a name="b842352706142422"></a>Old_tag</strong> is not empty.</p>
</td>
</tr>
<tr id="row31654100112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p13845282112856"><a name="p13845282112856"></a><a name="p13845282112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p47726024112856"><a name="p47726024112856"></a><a name="p47726024112856"></a>TMS.1005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p40602735112856"><a name="p40602735112856"></a><a name="p40602735112856"></a>The key in <strong id="b84235270695115"><a name="b84235270695115"></a><a name="b84235270695115"></a>Old_tag</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p487230112856"><a name="p487230112856"></a><a name="p487230112856"></a>Invalid key in <strong id="b3844716145640"><a name="b3844716145640"></a><a name="b3844716145640"></a>Old_tag.</strong></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p19646932112856"><a name="p19646932112856"></a><a name="p19646932112856"></a>Check whether the key in <strong id="b84235270695142"><a name="b84235270695142"></a><a name="b84235270695142"></a>Old_tag</strong> is valid.</p>
</td>
</tr>
<tr id="row42604663112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p28425648112856"><a name="p28425648112856"></a><a name="p28425648112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p20776113112856"><a name="p20776113112856"></a><a name="p20776113112856"></a>TMS.1006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p5143587112856"><a name="p5143587112856"></a><a name="p5143587112856"></a>The value in <strong id="b84235270695115_1"><a name="b84235270695115_1"></a><a name="b84235270695115_1"></a>Old_tag</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p13977389112856"><a name="p13977389112856"></a><a name="p13977389112856"></a>Invalid value in <strong id="b119245812452"><a name="b119245812452"></a><a name="b119245812452"></a>Old_tag</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p56078653112856"><a name="p56078653112856"></a><a name="p56078653112856"></a>Check whether the value in <strong id="b84235270695142_1"><a name="b84235270695142_1"></a><a name="b84235270695142_1"></a>Old_tag</strong> is valid.</p>
</td>
</tr>
<tr id="row34945836112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p12040431112856"><a name="p12040431112856"></a><a name="p12040431112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p35750892112856"><a name="p35750892112856"></a><a name="p35750892112856"></a>TMS.1007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p10141129112856"><a name="p10141129112856"></a><a name="p10141129112856"></a><strong id="b96116407695025_2"><a name="b96116407695025_2"></a><a name="b96116407695025_2"></a>New_tag</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p16125102112856"><a name="p16125102112856"></a><a name="p16125102112856"></a><strong id="b10908196112856"><a name="b10908196112856"></a><a name="b10908196112856"></a>New_tag</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p11148649112856"><a name="p11148649112856"></a><a name="p11148649112856"></a>Ensure that parameter <strong id="b842352706142422_1"><a name="b842352706142422_1"></a><a name="b842352706142422_1"></a>New_tag</strong> is not empty.</p>
</td>
</tr>
<tr id="row33228978112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p7192737112856"><a name="p7192737112856"></a><a name="p7192737112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p45740857112856"><a name="p45740857112856"></a><a name="p45740857112856"></a>TMS.1008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p14021921112856"><a name="p14021921112856"></a><a name="p14021921112856"></a>The key in <strong id="b84235270695115_2"><a name="b84235270695115_2"></a><a name="b84235270695115_2"></a>New_tag</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p62033793112856"><a name="p62033793112856"></a><a name="p62033793112856"></a>Invalid key in <strong id="b55883977145657"><a name="b55883977145657"></a><a name="b55883977145657"></a>New_tag.</strong></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p58370070112856"><a name="p58370070112856"></a><a name="p58370070112856"></a>Check whether the key in <strong id="b84235270695142_2"><a name="b84235270695142_2"></a><a name="b84235270695142_2"></a>New_tag</strong> is valid.</p>
</td>
</tr>
<tr id="row55568587112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p4761733112856"><a name="p4761733112856"></a><a name="p4761733112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p50156120112856"><a name="p50156120112856"></a><a name="p50156120112856"></a>TMS.1009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p36113899112856"><a name="p36113899112856"></a><a name="p36113899112856"></a>The value in <strong id="b84235270695115_3"><a name="b84235270695115_3"></a><a name="b84235270695115_3"></a>New_tag</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p39544678112856"><a name="p39544678112856"></a><a name="p39544678112856"></a>Invalid value in <strong id="b5849679014573"><a name="b5849679014573"></a><a name="b5849679014573"></a>New_tag</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p38368006112856"><a name="p38368006112856"></a><a name="p38368006112856"></a>Check whether the value in <strong id="b84235270695142_3"><a name="b84235270695142_3"></a><a name="b84235270695142_3"></a>New_tag</strong> is valid.</p>
</td>
</tr>
<tr id="row9767734112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p52989019112856"><a name="p52989019112856"></a><a name="p52989019112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p64252169112856"><a name="p64252169112856"></a><a name="p64252169112856"></a>TMS.1010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p37043175112856"><a name="p37043175112856"></a><a name="p37043175112856"></a><strong id="b84235270693614_6"><a name="b84235270693614_6"></a><a name="b84235270693614_6"></a>Order_field</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p47707165112856"><a name="p47707165112856"></a><a name="p47707165112856"></a><strong id="b26711305112856"><a name="b26711305112856"></a><a name="b26711305112856"></a>Order_field</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p16132087112856"><a name="p16132087112856"></a><a name="p16132087112856"></a>Check whether parameter <strong id="b84235270695142_4"><a name="b84235270695142_4"></a><a name="b84235270695142_4"></a>Order_field</strong> is valid.</p>
</td>
</tr>
<tr id="row10971059112856"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p16240611112856"><a name="p16240611112856"></a><a name="p16240611112856"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p40421132112856"><a name="p40421132112856"></a><a name="p40421132112856"></a>TMS.1011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p52886229112856"><a name="p52886229112856"></a><a name="p52886229112856"></a><strong id="b84235270693614_7"><a name="b84235270693614_7"></a><a name="b84235270693614_7"></a>Order_method</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p55926118112856"><a name="p55926118112856"></a><a name="p55926118112856"></a><strong id="b35979614467"><a name="b35979614467"></a><a name="b35979614467"></a>Order_method</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p35059882112856"><a name="p35059882112856"></a><a name="p35059882112856"></a>Check whether parameter <strong id="b84235270695142_5"><a name="b84235270695142_5"></a><a name="b84235270695142_5"></a>Order_method</strong> is valid.</p>
</td>
</tr>
</tbody>
</table>

