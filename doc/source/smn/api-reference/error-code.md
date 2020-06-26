# Error Code<a name="smn_api_64000"></a>

<a name="table107345271214"></a>
<table><thead align="left"><tr id="row678714281121"><th class="cellrowborder" valign="top" width="13.489999999999998%" id="mcps1.1.6.1.1"><p id="p478712286211"><a name="p478712286211"></a><a name="p478712286211"></a><strong id="b842352706174411"><a name="b842352706174411"></a><a name="b842352706174411"></a>Module</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.57%" id="mcps1.1.6.1.2"><p id="p167872281825"><a name="p167872281825"></a><a name="p167872281825"></a><strong id="b170187709114474"><a name="b170187709114474"></a><a name="b170187709114474"></a>HTTP Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.24%" id="mcps1.1.6.1.3"><p id="p578752819217"><a name="p578752819217"></a><a name="p578752819217"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="23.02%" id="mcps1.1.6.1.4"><p id="p878712286219"><a name="p878712286219"></a><a name="p878712286219"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="30.680000000000003%" id="mcps1.1.6.1.5"><p id="p18787102810211"><a name="p18787102810211"></a><a name="p18787102810211"></a>Handling Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="row378782816210"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p2953171861418"><a name="p2953171861418"></a><a name="p2953171861418"></a>Tag management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p129531318121411"><a name="p129531318121411"></a><a name="p129531318121411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p11953161817141"><a name="p11953161817141"></a><a name="p11953161817141"></a>SMN.0038</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p6953018101413"><a name="p6953018101413"></a><a name="p6953018101413"></a>Parameter: tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p695315186146"><a name="p695315186146"></a><a name="p695315186146"></a>Enter a valid value for <strong id="b84235270691457"><a name="b84235270691457"></a><a name="b84235270691457"></a>tag</strong>.</p>
</td>
</tr>
<tr id="row17871128323"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p14953918131414"><a name="p14953918131414"></a><a name="p14953918131414"></a>Tag management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1295331810142"><a name="p1295331810142"></a><a name="p1295331810142"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p20953818131412"><a name="p20953818131412"></a><a name="p20953818131412"></a>SMN.0075</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p79531618131415"><a name="p79531618131415"></a><a name="p79531618131415"></a>Parameter: tags are too many.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p11953151871411"><a name="p11953151871411"></a><a name="p11953151871411"></a>A message template can contain a maximum of 90 non-repeated variables.</p>
</td>
</tr>
<tr id="row10793132815216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p2957818141410"><a name="p2957818141410"></a><a name="p2957818141410"></a>Direct SMS messaging</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p195713188141"><a name="p195713188141"></a><a name="p195713188141"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p49577180141"><a name="p49577180141"></a><a name="p49577180141"></a>SMN.0057</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p4957318161416"><a name="p4957318161416"></a><a name="p4957318161416"></a>The number of SMS messages exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1150141195755"><a name="p1150141195755"></a><a name="p1150141195755"></a>You can send at most 60 SMS messages to a single phone number within one hour and 200 within 12 hours.</p>
<p id="p1472927717122"><a name="p1472927717122"></a><a name="p1472927717122"></a>This limit is applicable only to direct SMS message sending. There is no limit on the number of messages you can publish to a topic.</p>
</td>
</tr>
<tr id="row1080013281121"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p2959191871419"><a name="p2959191871419"></a><a name="p2959191871419"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p695916182146"><a name="p695916182146"></a><a name="p695916182146"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p159593181144"><a name="p159593181144"></a><a name="p159593181144"></a>SMN.0001</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p5960121810141"><a name="p5960121810141"></a><a name="p5960121810141"></a>No permission to request resources.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p11960418201419"><a name="p11960418201419"></a><a name="p11960418201419"></a>Add the required permission.</p>
</td>
</tr>
<tr id="row480015282028"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p296012182145"><a name="p296012182145"></a><a name="p296012182145"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p596018181145"><a name="p596018181145"></a><a name="p596018181145"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p296012181141"><a name="p296012181141"></a><a name="p296012181141"></a>SMN.0015</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p13960161851415"><a name="p13960161851415"></a><a name="p13960161851415"></a>Parameter: Offset or limit is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p169601618101417"><a name="p169601618101417"></a><a name="p169601618101417"></a>Enter a valid offset and limit.</p>
</td>
</tr>
<tr id="row108001228429"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1796081881420"><a name="p1796081881420"></a><a name="p1796081881420"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p18960191881410"><a name="p18960191881410"></a><a name="p18960191881410"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p4960121841411"><a name="p4960121841411"></a><a name="p4960121841411"></a>SMN.0016</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p59601518121414"><a name="p59601518121414"></a><a name="p59601518121414"></a>Database Exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p14674647174413"><a name="p14674647174413"></a><a name="p14674647174413"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row1180062810214"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p3960718161417"><a name="p3960718161417"></a><a name="p3960718161417"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1496081816146"><a name="p1496081816146"></a><a name="p1496081816146"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p196018183142"><a name="p196018183142"></a><a name="p196018183142"></a>SMN.0017</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p29602185146"><a name="p29602185146"></a><a name="p29602185146"></a>Parameter: Remark is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p159601718141413"><a name="p159601718141413"></a><a name="p159601718141413"></a>Enter a valid value for <strong id="b761344014208"><a name="b761344014208"></a><a name="b761344014208"></a>remark</strong>.</p>
</td>
</tr>
<tr id="row1980012289212"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p209605189149"><a name="p209605189149"></a><a name="p209605189149"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p13960151810145"><a name="p13960151810145"></a><a name="p13960151810145"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p15960131891410"><a name="p15960131891410"></a><a name="p15960131891410"></a>SMN.0018</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p396071811147"><a name="p396071811147"></a><a name="p396071811147"></a>Service internal error.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p648513152482"><a name="p648513152482"></a><a name="p648513152482"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row88007281725"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p18961101861415"><a name="p18961101861415"></a><a name="p18961101861415"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1961101816144"><a name="p1961101816144"></a><a name="p1961101816144"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p99618183145"><a name="p99618183145"></a><a name="p99618183145"></a>SMN.0022</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1196114187142"><a name="p1196114187142"></a><a name="p1196114187142"></a>Parameter: token is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p5961141811142"><a name="p5961141811142"></a><a name="p5961141811142"></a>Specify a valid token.</p>
</td>
</tr>
<tr id="row580012281425"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1796118180143"><a name="p1796118180143"></a><a name="p1796118180143"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p18961191816145"><a name="p18961191816145"></a><a name="p18961191816145"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p13961161811148"><a name="p13961161811148"></a><a name="p13961161811148"></a>SMN.0033</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p0961918141411"><a name="p0961918141411"></a><a name="p0961918141411"></a>Parameter: push_policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p18961131871417"><a name="p18961131871417"></a><a name="p18961131871417"></a>Enter a valid value for <strong id="b84235270691438"><a name="b84235270691438"></a><a name="b84235270691438"></a>push_policy</strong>.</p>
</td>
</tr>
<tr id="row1802102810215"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p17961201841414"><a name="p17961201841414"></a><a name="p17961201841414"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p696117184146"><a name="p696117184146"></a><a name="p696117184146"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p15961151812148"><a name="p15961151812148"></a><a name="p15961151812148"></a>SMN.0034</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p109611218161415"><a name="p109611218161415"></a><a name="p109611218161415"></a>Parameter: subscription_auth_policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p6961618151416"><a name="p6961618151416"></a><a name="p6961618151416"></a>Enter a valid value for <strong id="b84235270691457_1"><a name="b84235270691457_1"></a><a name="b84235270691457_1"></a>subscription_auth_policy</strong>.</p>
</td>
</tr>
<tr id="row178021628228"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1296114189142"><a name="p1296114189142"></a><a name="p1296114189142"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p9961201810142"><a name="p9961201810142"></a><a name="p9961201810142"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p196151815145"><a name="p196151815145"></a><a name="p196151815145"></a>SMN.0035</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p16961131881413"><a name="p16961131881413"></a><a name="p16961131881413"></a>Parameter: validation_policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p696119187142"><a name="p696119187142"></a><a name="p696119187142"></a>Enter a valid value for <strong id="b84235270691457_2"><a name="b84235270691457_2"></a><a name="b84235270691457_2"></a>validation_policy</strong>.</p>
</td>
</tr>
<tr id="row980222816215"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p7962161819148"><a name="p7962161819148"></a><a name="p7962161819148"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p199621418151418"><a name="p199621418151418"></a><a name="p199621418151418"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p20962618111413"><a name="p20962618111413"></a><a name="p20962618111413"></a>SMN.0036</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1396213188145"><a name="p1396213188145"></a><a name="p1396213188145"></a>Parameter: xdomain_type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p496291821416"><a name="p496291821416"></a><a name="p496291821416"></a>Enter a valid value for <strong id="b84235270691457_3"><a name="b84235270691457_3"></a><a name="b84235270691457_3"></a>xdomain_type</strong>.</p>
</td>
</tr>
<tr id="row15802162817211"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p15962518181410"><a name="p15962518181410"></a><a name="p15962518181410"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p17962121891415"><a name="p17962121891415"></a><a name="p17962121891415"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p29622186142"><a name="p29622186142"></a><a name="p29622186142"></a>SMN.0059</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p7962818131417"><a name="p7962818131417"></a><a name="p7962818131417"></a>Parameter: job_id is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p16456155213441"><a name="p16456155213441"></a><a name="p16456155213441"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row168026281428"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p296241881411"><a name="p296241881411"></a><a name="p296241881411"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1962218101413"><a name="p1962218101413"></a><a name="p1962218101413"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1896211182147"><a name="p1896211182147"></a><a name="p1896211182147"></a>SMN.0060</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1896261821411"><a name="p1896261821411"></a><a name="p1896261821411"></a>Job not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1496155534412"><a name="p1496155534412"></a><a name="p1496155534412"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row580211288218"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p39621718191412"><a name="p39621718191412"></a><a name="p39621718191412"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p11962818111410"><a name="p11962818111410"></a><a name="p11962818111410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p3962181817149"><a name="p3962181817149"></a><a name="p3962181817149"></a>SMN.0061</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p149626186148"><a name="p149626186148"></a><a name="p149626186148"></a>Parameter: Service name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p9391205774414"><a name="p9391205774414"></a><a name="p9391205774414"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row1803122817212"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p19621218171414"><a name="p19621218171414"></a><a name="p19621218171414"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p196291871418"><a name="p196291871418"></a><a name="p196291871418"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p596213180141"><a name="p596213180141"></a><a name="p596213180141"></a>SMN.0062</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p996319189142"><a name="p996319189142"></a><a name="p996319189142"></a>Parameter: Show name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p4611135994410"><a name="p4611135994410"></a><a name="p4611135994410"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row28031281429"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p8963318181417"><a name="p8963318181417"></a><a name="p8963318181417"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p496391861415"><a name="p496391861415"></a><a name="p496391861415"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p0963918111415"><a name="p0963918111415"></a><a name="p0963918111415"></a>SMN.0063</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p3963101861420"><a name="p3963101861420"></a><a name="p3963101861420"></a>Cloud service not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p39302154518"><a name="p39302154518"></a><a name="p39302154518"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row108031428224"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p9963171814147"><a name="p9963171814147"></a><a name="p9963171814147"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p696315187145"><a name="p696315187145"></a><a name="p696315187145"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1963018171413"><a name="p1963018171413"></a><a name="p1963018171413"></a>SMN.0065</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1796321871420"><a name="p1796321871420"></a><a name="p1796321871420"></a>The number of email messages exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p18424124144517"><a name="p18424124144517"></a><a name="p18424124144517"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row58031281826"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p9963101851420"><a name="p9963101851420"></a><a name="p9963101851420"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1396341819147"><a name="p1396341819147"></a><a name="p1396341819147"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p5963101891412"><a name="p5963101891412"></a><a name="p5963101891412"></a>SMN.0066</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p896311817149"><a name="p896311817149"></a><a name="p896311817149"></a>Parameter: System parameter name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p04115719458"><a name="p04115719458"></a><a name="p04115719458"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row0803102811218"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p19963171821412"><a name="p19963171821412"></a><a name="p19963171821412"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1396411817143"><a name="p1396411817143"></a><a name="p1396411817143"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p7964718111411"><a name="p7964718111411"></a><a name="p7964718111411"></a>SMN.0067</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p196461813146"><a name="p196461813146"></a><a name="p196461813146"></a>Parameter: System parameter value is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p3362101134510"><a name="p3362101134510"></a><a name="p3362101134510"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row180317281722"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p69641718181418"><a name="p69641718181418"></a><a name="p69641718181418"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p69641418141413"><a name="p69641418141413"></a><a name="p69641418141413"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1096411186148"><a name="p1096411186148"></a><a name="p1096411186148"></a>SMN.0068</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p396411881413"><a name="p396411881413"></a><a name="p396411881413"></a>System parameter not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p69741513104519"><a name="p69741513104519"></a><a name="p69741513104519"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row1280362813213"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p696431818143"><a name="p696431818143"></a><a name="p696431818143"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p16964191881415"><a name="p16964191881415"></a><a name="p16964191881415"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p19964141881413"><a name="p19964141881413"></a><a name="p19964141881413"></a>SMN.0069</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p396471841414"><a name="p396471841414"></a><a name="p396471841414"></a>Not authorized to subscribe internal endpoints.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1896461821420"><a name="p1896461821420"></a><a name="p1896461821420"></a>Enter a correct HTTP/HTTPS endpoint.</p>
</td>
</tr>
<tr id="row10803728826"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p17964718141414"><a name="p17964718141414"></a><a name="p17964718141414"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1896451831419"><a name="p1896451831419"></a><a name="p1896451831419"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p5964101820141"><a name="p5964101820141"></a><a name="p5964101820141"></a>SMN.0070</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1596413182141"><a name="p1596413182141"></a><a name="p1596413182141"></a>No permission to request resources. The role is op_restricted. Contact customer service.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p8964318121413"><a name="p8964318121413"></a><a name="p8964318121413"></a>Check the account balance and top up your account. If the fault persists, contact customer service.</p>
</td>
</tr>
<tr id="row1280311289218"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p2964171812149"><a name="p2964171812149"></a><a name="p2964171812149"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p796431813145"><a name="p796431813145"></a><a name="p796431813145"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1966191841418"><a name="p1966191841418"></a><a name="p1966191841418"></a>SMN.0071</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p16966161851411"><a name="p16966161851411"></a><a name="p16966161851411"></a>No permission to request resources. The role is op_suspended.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p139664183146"><a name="p139664183146"></a><a name="p139664183146"></a>Check whether your account has been frozen.</p>
</td>
</tr>
<tr id="row19803162811213"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p7966131871411"><a name="p7966131871411"></a><a name="p7966131871411"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p129661518131412"><a name="p129661518131412"></a><a name="p129661518131412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1896611188145"><a name="p1896611188145"></a><a name="p1896611188145"></a>SMN.0074</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p196641811142"><a name="p196641811142"></a><a name="p196641811142"></a>Failed to add permission.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p266571634612"><a name="p266571634612"></a><a name="p266571634612"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row8803122816216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p149661918181419"><a name="p149661918181419"></a><a name="p149661918181419"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p12966191891410"><a name="p12966191891410"></a><a name="p12966191891410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1096611881418"><a name="p1096611881418"></a><a name="p1096611881418"></a>SMN.0077</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p189668181142"><a name="p189668181142"></a><a name="p189668181142"></a>Parameter: Status is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p59661018161417"><a name="p59661018161417"></a><a name="p59661018161417"></a>Enter a valid value for <strong id="b7675953165514"><a name="b7675953165514"></a><a name="b7675953165514"></a>status</strong>.</p>
</td>
</tr>
<tr id="row1182017281213"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p49859187144"><a name="p49859187144"></a><a name="p49859187144"></a>Subscription management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p159851518121414"><a name="p159851518121414"></a><a name="p159851518121414"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1198541818141"><a name="p1198541818141"></a><a name="p1198541818141"></a>SMN.0011</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p898515182145"><a name="p898515182145"></a><a name="p898515182145"></a>Parameter: Protocol is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p199851618151415"><a name="p199851618151415"></a><a name="p199851618151415"></a>Specify a correct protocol.</p>
</td>
</tr>
<tr id="row1482017281521"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1698511185147"><a name="p1698511185147"></a><a name="p1698511185147"></a>Subscription management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p199856181146"><a name="p199856181146"></a><a name="p199856181146"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p129851418141415"><a name="p129851418141415"></a><a name="p129851418141415"></a>SMN.0012</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p298541841414"><a name="p298541841414"></a><a name="p298541841414"></a>Parameter: Endpoint is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1598518182141"><a name="p1598518182141"></a><a name="p1598518182141"></a>Specify a valid endpoint.</p>
</td>
</tr>
<tr id="row128201283215"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1298511184143"><a name="p1298511184143"></a><a name="p1298511184143"></a>Subscription management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p109851180149"><a name="p109851180149"></a><a name="p109851180149"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p998561841419"><a name="p998561841419"></a><a name="p998561841419"></a>SMN.0013</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p17985118121416"><a name="p17985118121416"></a><a name="p17985118121416"></a>Subscription resource not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p7985201851414"><a name="p7985201851414"></a><a name="p7985201851414"></a>Specify an existing subscription endpoint.</p>
</td>
</tr>
<tr id="row78211828729"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1985101811417"><a name="p1985101811417"></a><a name="p1985101811417"></a>Subscription management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p8985141816141"><a name="p8985141816141"></a><a name="p8985141816141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p16985181817147"><a name="p16985181817147"></a><a name="p16985181817147"></a>SMN.0014</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1898571891418"><a name="p1898571891418"></a><a name="p1898571891418"></a>Parameter: SubscriptionUrn is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1398531820147"><a name="p1398531820147"></a><a name="p1398531820147"></a>Enter a valid subscription URN.</p>
</td>
</tr>
<tr id="row1282116283214"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p298516189149"><a name="p298516189149"></a><a name="p298516189149"></a>Subscription management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1998514186141"><a name="p1998514186141"></a><a name="p1998514186141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p3985181841417"><a name="p3985181841417"></a><a name="p3985181841417"></a>SMN.0043</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1598516189140"><a name="p1598516189140"></a><a name="p1598516189140"></a>Parameter: subscription is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1598571810144"><a name="p1598571810144"></a><a name="p1598571810144"></a>Enter a valid value for <strong id="b84235270691457_4"><a name="b84235270691457_4"></a><a name="b84235270691457_4"></a>subscription</strong>.</p>
</td>
</tr>
<tr id="row19821132817216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p135972257203"><a name="p135972257203"></a><a name="p135972257203"></a>Subscription management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1798541814147"><a name="p1798541814147"></a><a name="p1798541814147"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p3985151810142"><a name="p3985151810142"></a><a name="p3985151810142"></a>SMN.0078</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1985111812148"><a name="p1985111812148"></a><a name="p1985111812148"></a>The maximum number of subscriptions has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p7985181814142"><a name="p7985181814142"></a><a name="p7985181814142"></a>The number of subscriptions has reached the limit.</p>
</td>
</tr>
<tr id="row12821202813210"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p898516183143"><a name="p898516183143"></a><a name="p898516183143"></a>Publishing a message</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p16985121831413"><a name="p16985121831413"></a><a name="p16985121831413"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1798641812148"><a name="p1798641812148"></a><a name="p1798641812148"></a>SMN.0008</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p159861718191418"><a name="p159861718191418"></a><a name="p159861718191418"></a>Parameter: Subject is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p7986518131418"><a name="p7986518131418"></a><a name="p7986518131418"></a>Enter a valid value for <strong id="b16129122920586"><a name="b16129122920586"></a><a name="b16129122920586"></a>subject</strong>.</p>
</td>
</tr>
<tr id="row12821172810219"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p10986118171413"><a name="p10986118171413"></a><a name="p10986118171413"></a>Publishing a message</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p18986918131418"><a name="p18986918131418"></a><a name="p18986918131418"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p998611188143"><a name="p998611188143"></a><a name="p998611188143"></a>SMN.0009</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p2986618151413"><a name="p2986618151413"></a><a name="p2986618151413"></a>Parameter: Message is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p698611189145"><a name="p698611189145"></a><a name="p698611189145"></a>Enter a valid message.</p>
</td>
</tr>
<tr id="row482110286216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p17986171861415"><a name="p17986171861415"></a><a name="p17986171861415"></a>Publishing a message</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p19986111871417"><a name="p19986111871417"></a><a name="p19986111871417"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p169867189141"><a name="p169867189141"></a><a name="p169867189141"></a>SMN.0019</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p3986218121412"><a name="p3986218121412"></a><a name="p3986218121412"></a>Producer Exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p89412618472"><a name="p89412618472"></a><a name="p89412618472"></a>Contact customer service for technical support.</p>
</td>
</tr>
<tr id="row1282110281325"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p16986161881419"><a name="p16986161881419"></a><a name="p16986161881419"></a>Publishing a message</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p798671831419"><a name="p798671831419"></a><a name="p798671831419"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p10986121814145"><a name="p10986121814145"></a><a name="p10986121814145"></a>SMN.0021</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p3986618161415"><a name="p3986618161415"></a><a name="p3986618161415"></a>MessageStructure is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p89861818181415"><a name="p89861818181415"></a><a name="p89861818181415"></a>Specify a correct message structure.</p>
</td>
</tr>
<tr id="row10822102816217"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p159881718131417"><a name="p159881718131417"></a><a name="p159881718131417"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p49891118121418"><a name="p49891118121418"></a><a name="p49891118121418"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1498951814145"><a name="p1498951814145"></a><a name="p1498951814145"></a>SMN.0024</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p119891318161419"><a name="p119891318161419"></a><a name="p119891318161419"></a>Parameter: content is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p179891218131418"><a name="p179891218131418"></a><a name="p179891218131418"></a>Enter valid message template content.</p>
</td>
</tr>
<tr id="row4822828024"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1398941818147"><a name="p1398941818147"></a><a name="p1398941818147"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p18989618191413"><a name="p18989618191413"></a><a name="p18989618191413"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p14989131871411"><a name="p14989131871411"></a><a name="p14989131871411"></a>SMN.0025</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p5989111821420"><a name="p5989111821420"></a><a name="p5989111821420"></a>Template already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p17989191813141"><a name="p17989191813141"></a><a name="p17989191813141"></a>You cannot create the same template twice.</p>
</td>
</tr>
<tr id="row28221528724"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p7989518171419"><a name="p7989518171419"></a><a name="p7989518171419"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p16989161871413"><a name="p16989161871413"></a><a name="p16989161871413"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p19989201812147"><a name="p19989201812147"></a><a name="p19989201812147"></a>SMN.0027</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p149891182144"><a name="p149891182144"></a><a name="p149891182144"></a>Template not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1798918189149"><a name="p1798918189149"></a><a name="p1798918189149"></a>Specify an existing message template.</p>
</td>
</tr>
<tr id="row98227282027"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p189891618131415"><a name="p189891618131415"></a><a name="p189891618131415"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1598901820142"><a name="p1598901820142"></a><a name="p1598901820142"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p15989191841412"><a name="p15989191841412"></a><a name="p15989191841412"></a>SMN.0031</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p098951801414"><a name="p098951801414"></a><a name="p098951801414"></a>Parameter: template_id is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1598951821415"><a name="p1598951821415"></a><a name="p1598951821415"></a>Enter a valid template ID.</p>
</td>
</tr>
<tr id="row158227286216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p79891818191416"><a name="p79891818191416"></a><a name="p79891818191416"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p13989161831418"><a name="p13989161831418"></a><a name="p13989161831418"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1989918111420"><a name="p1989918111420"></a><a name="p1989918111420"></a>SMN.0032</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p4989518131410"><a name="p4989518131410"></a><a name="p4989518131410"></a>Parameter: message_template_name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p299014185145"><a name="p299014185145"></a><a name="p299014185145"></a>Enter a valid value for <strong id="b84235270691457_5"><a name="b84235270691457_5"></a><a name="b84235270691457_5"></a>message_template_name</strong>.</p>
</td>
</tr>
<tr id="row1182442817218"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p19990818131420"><a name="p19990818131420"></a><a name="p19990818131420"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p2990141861410"><a name="p2990141861410"></a><a name="p2990141861410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p20990131817149"><a name="p20990131817149"></a><a name="p20990131817149"></a>SMN.0042</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1990191831412"><a name="p1990191831412"></a><a name="p1990191831412"></a>Parameter: Message_template_name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1399061816144"><a name="p1399061816144"></a><a name="p1399061816144"></a>Enter a valid value for <strong id="b84235270691457_6"><a name="b84235270691457_6"></a><a name="b84235270691457_6"></a>message_template_name</strong>.</p>
</td>
</tr>
<tr id="row58242285214"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p12990101819148"><a name="p12990101819148"></a><a name="p12990101819148"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p79901718141413"><a name="p79901718141413"></a><a name="p79901718141413"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1099013184142"><a name="p1099013184142"></a><a name="p1099013184142"></a>SMN.0044</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p3990161812148"><a name="p3990161812148"></a><a name="p3990161812148"></a>Exceeded template limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p15990121831420"><a name="p15990121831420"></a><a name="p15990121831420"></a>You can create a maximum of 100 text message templates.</p>
</td>
</tr>
<tr id="row158241028526"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p15990111891420"><a name="p15990111891420"></a><a name="p15990111891420"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p19990141820142"><a name="p19990141820142"></a><a name="p19990141820142"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p189901518191411"><a name="p189901518191411"></a><a name="p189901518191411"></a>SMN.0076</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p139902181146"><a name="p139902181146"></a><a name="p139902181146"></a>Default message template not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p49901718151412"><a name="p49901718151412"></a><a name="p49901718151412"></a>Create a default message template using the same template name.</p>
</td>
</tr>
<tr id="row1682515289210"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p7991618101413"><a name="p7991618101413"></a><a name="p7991618101413"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p11991118181415"><a name="p11991118181415"></a><a name="p11991118181415"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p19991161861416"><a name="p19991161861416"></a><a name="p19991161861416"></a>SMN.0002</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p15991818191414"><a name="p15991818191414"></a><a name="p15991818191414"></a>Parameter: Name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p17991818171410"><a name="p17991818171410"></a><a name="p17991818171410"></a>Enter a valid topic name.</p>
</td>
</tr>
<tr id="row188250281929"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p799118182141"><a name="p799118182141"></a><a name="p799118182141"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p16991718151413"><a name="p16991718151413"></a><a name="p16991718151413"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p109911518121413"><a name="p109911518121413"></a><a name="p109911518121413"></a>SMN.0003</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1899191816142"><a name="p1899191816142"></a><a name="p1899191816142"></a>Parameter: DisplayName is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p79921718201411"><a name="p79921718201411"></a><a name="p79921718201411"></a>Enter a valid topic display name.</p>
</td>
</tr>
<tr id="row12825102811215"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p5992111814145"><a name="p5992111814145"></a><a name="p5992111814145"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1699241801420"><a name="p1699241801420"></a><a name="p1699241801420"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p18992118141416"><a name="p18992118141416"></a><a name="p18992118141416"></a>SMN.0004</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p8992171814144"><a name="p8992171814144"></a><a name="p8992171814144"></a>Exceeded topic limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p189925187142"><a name="p189925187142"></a><a name="p189925187142"></a>You can create a maximum of 3000 topics.</p>
</td>
</tr>
<tr id="row182592810220"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p69925185142"><a name="p69925185142"></a><a name="p69925185142"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1699219184148"><a name="p1699219184148"></a><a name="p1699219184148"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p29921718201418"><a name="p29921718201418"></a><a name="p29921718201418"></a>SMN.0005</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p17992118161419"><a name="p17992118161419"></a><a name="p17992118161419"></a>Parameter: TopicUrn is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1992141813147"><a name="p1992141813147"></a><a name="p1992141813147"></a>Enter a valid topic URN.</p>
</td>
</tr>
<tr id="row68266289213"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p189921518121414"><a name="p189921518121414"></a><a name="p189921518121414"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p999212186143"><a name="p999212186143"></a><a name="p999212186143"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p69920187149"><a name="p69920187149"></a><a name="p69920187149"></a>SMN.0006</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p11992151851412"><a name="p11992151851412"></a><a name="p11992151851412"></a>Topic not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p7992191813140"><a name="p7992191813140"></a><a name="p7992191813140"></a>The topic does not exist.</p>
</td>
</tr>
<tr id="row178264281216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p16992618151410"><a name="p16992618151410"></a><a name="p16992618151410"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p13992171811145"><a name="p13992171811145"></a><a name="p13992171811145"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p209924181140"><a name="p209924181140"></a><a name="p209924181140"></a>SMN.0007</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1399221813148"><a name="p1399221813148"></a><a name="p1399221813148"></a>Exceeded subscription limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p5993018151412"><a name="p5993018151412"></a><a name="p5993018151412"></a>A maximum of 10,000 subscriptions can be added to a topic.</p>
</td>
</tr>
<tr id="row18826152812220"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p3993181819142"><a name="p3993181819142"></a><a name="p3993181819142"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p299321821419"><a name="p299321821419"></a><a name="p299321821419"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p139931018191413"><a name="p139931018191413"></a><a name="p139931018191413"></a>SMN.0045</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p179931818171415"><a name="p179931818171415"></a><a name="p179931818171415"></a>Attribute not found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1899331831410"><a name="p1899331831410"></a><a name="p1899331831410"></a>Specify an existing attribute.</p>
</td>
</tr>
<tr id="row1982718281218"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p5993161814146"><a name="p5993161814146"></a><a name="p5993161814146"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p59939181143"><a name="p59939181143"></a><a name="p59939181143"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p12993191831411"><a name="p12993191831411"></a><a name="p12993191831411"></a>SMN.0046</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p999381818141"><a name="p999381818141"></a><a name="p999381818141"></a>Parameter: Attribute name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p799341841410"><a name="p799341841410"></a><a name="p799341841410"></a>Enter a valid attribute name.</p>
</td>
</tr>
<tr id="row8827152817217"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p19993218111411"><a name="p19993218111411"></a><a name="p19993218111411"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p13993818161416"><a name="p13993818161416"></a><a name="p13993818161416"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p19993018101415"><a name="p19993018101415"></a><a name="p19993018101415"></a>SMN.0047</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p199931818151416"><a name="p199931818151416"></a><a name="p199931818151416"></a>Parameter: Value exceeds the maximum length.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p16993118201416"><a name="p16993118201416"></a><a name="p16993118201416"></a>Enter a valid value.</p>
</td>
</tr>
<tr id="row7828152814214"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1399391819147"><a name="p1399391819147"></a><a name="p1399391819147"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p159931718171411"><a name="p159931718171411"></a><a name="p159931718171411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1999371881419"><a name="p1999371881419"></a><a name="p1999371881419"></a>SMN.0048</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p13993118151412"><a name="p13993118151412"></a><a name="p13993118151412"></a>Parameter: Access policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p89931318181416"><a name="p89931318181416"></a><a name="p89931318181416"></a>Enter a valid value for <strong id="b255791691910"><a name="b255791691910"></a><a name="b255791691910"></a>access_policy</strong>. </p>
</td>
</tr>
<tr id="row1582817284217"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p1199361851410"><a name="p1199361851410"></a><a name="p1199361851410"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p299318185148"><a name="p299318185148"></a><a name="p299318185148"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p19993918151412"><a name="p19993918151412"></a><a name="p19993918151412"></a>SMN.0049</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p399315183141"><a name="p399315183141"></a><a name="p399315183141"></a>Parameter: Access policy version is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p149930189140"><a name="p149930189140"></a><a name="p149930189140"></a>Enter a valid access policy version. </p>
</td>
</tr>
<tr id="row1382852812219"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p8993121811143"><a name="p8993121811143"></a><a name="p8993121811143"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p6993818181417"><a name="p6993818181417"></a><a name="p6993818181417"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p9993111831412"><a name="p9993111831412"></a><a name="p9993111831412"></a>SMN.0050</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p4994518141419"><a name="p4994518141419"></a><a name="p4994518141419"></a>Parameter: Access policy ID is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p109941718101414"><a name="p109941718101414"></a><a name="p109941718101414"></a>Enter a valid policy ID. </p>
</td>
</tr>
<tr id="row128281280219"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p199948186144"><a name="p199948186144"></a><a name="p199948186144"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p39941918111420"><a name="p39941918111420"></a><a name="p39941918111420"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1299431861413"><a name="p1299431861413"></a><a name="p1299431861413"></a>SMN.0051</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p09941018181414"><a name="p09941018181414"></a><a name="p09941018181414"></a>Parameter: Access policy statement is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p299421861412"><a name="p299421861412"></a><a name="p299421861412"></a>Enter a valid policy statement. </p>
</td>
</tr>
<tr id="row178280286210"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p6994191881412"><a name="p6994191881412"></a><a name="p6994191881412"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1299401861417"><a name="p1299401861417"></a><a name="p1299401861417"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p19994111812146"><a name="p19994111812146"></a><a name="p19994111812146"></a>SMN.0052</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p99941818131415"><a name="p99941818131415"></a><a name="p99941818131415"></a>Parameter: Access policy statement ID is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1099414181143"><a name="p1099414181143"></a><a name="p1099414181143"></a>Enter a valid policy statement ID. </p>
</td>
</tr>
<tr id="row882913283216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p11994111861414"><a name="p11994111861414"></a><a name="p11994111861414"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1599491841411"><a name="p1599491841411"></a><a name="p1599491841411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p29941818111414"><a name="p29941818111414"></a><a name="p29941818111414"></a>SMN.0053</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p699418188145"><a name="p699418188145"></a><a name="p699418188145"></a>Parameter: Access policy statement resource is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p599471815144"><a name="p599471815144"></a><a name="p599471815144"></a>Enter a valid policy statement resource. </p>
</td>
</tr>
<tr id="row0829142812216"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p39941918141417"><a name="p39941918141417"></a><a name="p39941918141417"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1299441851419"><a name="p1299441851419"></a><a name="p1299441851419"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p99947186143"><a name="p99947186143"></a><a name="p99947186143"></a>SMN.0054</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p399471815143"><a name="p399471815143"></a><a name="p399471815143"></a>Parameter: Access policy statement effect is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p199947187140"><a name="p199947187140"></a><a name="p199947187140"></a>Enter a valid policy statement effect. </p>
</td>
</tr>
<tr id="row882917288219"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p2994121819140"><a name="p2994121819140"></a><a name="p2994121819140"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p299421841419"><a name="p299421841419"></a><a name="p299421841419"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1399416181148"><a name="p1399416181148"></a><a name="p1399416181148"></a>SMN.0055</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p799451861415"><a name="p799451861415"></a><a name="p799451861415"></a>Parameter: Access policy statement action is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p79951718101415"><a name="p79951718101415"></a><a name="p79951718101415"></a>Enter a valid policy statement action. </p>
</td>
</tr>
<tr id="row58296281821"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p2995131871411"><a name="p2995131871411"></a><a name="p2995131871411"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1995718101412"><a name="p1995718101412"></a><a name="p1995718101412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p29952182144"><a name="p29952182144"></a><a name="p29952182144"></a>SMN.0056</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p1099561851420"><a name="p1099561851420"></a><a name="p1099561851420"></a>Parameter: Access policy statement principal is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p1995161831416"><a name="p1995161831416"></a><a name="p1995161831416"></a>Enter a valid policy statement principal. </p>
</td>
</tr>
<tr id="row128305281522"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p699531810143"><a name="p699531810143"></a><a name="p699531810143"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p1699511851419"><a name="p1699511851419"></a><a name="p1699511851419"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p129951718141410"><a name="p129951718141410"></a><a name="p129951718141410"></a>SMN.0058</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p599521812141"><a name="p599521812141"></a><a name="p599521812141"></a>Parameter: Access policy statement condition is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p10995191818147"><a name="p10995191818147"></a><a name="p10995191818147"></a>Enter a valid policy statement condition. </p>
</td>
</tr>
<tr id="row88314284219"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p5995918101417"><a name="p5995918101417"></a><a name="p5995918101417"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p799514184149"><a name="p799514184149"></a><a name="p799514184149"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1799515181148"><a name="p1799515181148"></a><a name="p1799515181148"></a>SMN.0072</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p139951186147"><a name="p139951186147"></a><a name="p139951186147"></a>Parameter: Service is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p199513186147"><a name="p199513186147"></a><a name="p199513186147"></a>Enter a valid value for <strong id="b20948102014414"><a name="b20948102014414"></a><a name="b20948102014414"></a>service</strong>. </p>
</td>
</tr>
<tr id="row198316281525"><td class="cellrowborder" valign="top" width="13.489999999999998%" headers="mcps1.1.6.1.1 "><p id="p199541831418"><a name="p199541831418"></a><a name="p199541831418"></a>Topic management</p>
</td>
<td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.1.6.1.2 "><p id="p20995161816146"><a name="p20995161816146"></a><a name="p20995161816146"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.1.6.1.3 "><p id="p1699581831419"><a name="p1699581831419"></a><a name="p1699581831419"></a>SMN.0073</p>
</td>
<td class="cellrowborder" valign="top" width="23.02%" headers="mcps1.1.6.1.4 "><p id="p299581818141"><a name="p299581818141"></a><a name="p299581818141"></a>Parameter: Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.6.1.5 "><p id="p13995171817143"><a name="p13995171817143"></a><a name="p13995171817143"></a>Enter a valid value for <strong id="b17485195217489"><a name="b17485195217489"></a><a name="b17485195217489"></a>action</strong>. </p>
</td>
</tr>
</tbody>
</table>

