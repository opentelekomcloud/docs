# Error Code<a name="kms_02_0302"></a>

## Introduction<a name="en-us_topic_0112992323_s6412adb7ceef44f4b3d63f4ffd957404"></a>

A customized message is returned when errors, such as 400 or 500 errors, occur in an extended API. This section describes error codes and their meanings.

## Response Format<a name="en-us_topic_0112992323_s6b20acbd16784da6b03f73a0f018c9f4"></a>

-   HTTP status code

    ```
    500
    ```

-   Response example

    ```
    {
        "error": {
            "error_code": "KMS.0101",
            "error_msg": "kms error."
        }
    }
    ```


## Error Code Description<a name="en-us_topic_0112992323_s3faebed263224531ae15dfe50861b292"></a>

<a name="en-us_topic_0112992323_table61298295154418"></a>
<table><thead align="left"><tr id="en-us_topic_0112992323_row40052093154418"><th class="cellrowborder" valign="top" width="29.060000000000002%" id="mcps1.1.4.1.1"><p id="en-us_topic_0112992323_p22994080154418"><a name="en-us_topic_0112992323_p22994080154418"></a><a name="en-us_topic_0112992323_p22994080154418"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="15.340000000000002%" id="mcps1.1.4.1.2"><p id="en-us_topic_0112992323_p50581163154418"><a name="en-us_topic_0112992323_p50581163154418"></a><a name="en-us_topic_0112992323_p50581163154418"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="55.60000000000001%" id="mcps1.1.4.1.3"><p id="en-us_topic_0112992323_p3433543154418"><a name="en-us_topic_0112992323_p3433543154418"></a><a name="en-us_topic_0112992323_p3433543154418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992323_row9681563154418"><td class="cellrowborder" rowspan="37" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p46009168154418"><a name="en-us_topic_0112992323_p46009168154418"></a><a name="en-us_topic_0112992323_p46009168154418"></a>Common</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p10886593154621"><a name="en-us_topic_0112992323_p10886593154621"></a><a name="en-us_topic_0112992323_p10886593154621"></a>KMS.0101</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p9398856154621"><a name="en-us_topic_0112992323_p9398856154621"></a><a name="en-us_topic_0112992323_p9398856154621"></a>KMS error.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row61001174154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p6662512154621"><a name="en-us_topic_0112992323_p6662512154621"></a><a name="en-us_topic_0112992323_p6662512154621"></a>KMS.0102</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p2792601154621"><a name="en-us_topic_0112992323_p2792601154621"></a><a name="en-us_topic_0112992323_p2792601154621"></a>Abnormal KMS I/O.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1023729154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p22540882154621"><a name="en-us_topic_0112992323_p22540882154621"></a><a name="en-us_topic_0112992323_p22540882154621"></a>KMS.0201</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p13872152154621"><a name="en-us_topic_0112992323_p13872152154621"></a><a name="en-us_topic_0112992323_p13872152154621"></a>Invalid request URL.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row559847154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p46469300154621"><a name="en-us_topic_0112992323_p46469300154621"></a><a name="en-us_topic_0112992323_p46469300154621"></a>KMS.0202</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p5916960154621"><a name="en-us_topic_0112992323_p5916960154621"></a><a name="en-us_topic_0112992323_p5916960154621"></a>The JSON format of the request message is invalid.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row24706121154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p18496875154621"><a name="en-us_topic_0112992323_p18496875154621"></a><a name="en-us_topic_0112992323_p18496875154621"></a>KMS.0203</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p21851927154621"><a name="en-us_topic_0112992323_p21851927154621"></a><a name="en-us_topic_0112992323_p21851927154621"></a>The request message length has exceeded the upper limit.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row39355822154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p25254677154621"><a name="en-us_topic_0112992323_p25254677154621"></a><a name="en-us_topic_0112992323_p25254677154621"></a>KMS.0204</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p32362923154621"><a name="en-us_topic_0112992323_p32362923154621"></a><a name="en-us_topic_0112992323_p32362923154621"></a>The request message lacks required parameters.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row9085627154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p37359957154621"><a name="en-us_topic_0112992323_p37359957154621"></a><a name="en-us_topic_0112992323_p37359957154621"></a>KMS.0205</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p6257680154621"><a name="en-us_topic_0112992323_p6257680154621"></a><a name="en-us_topic_0112992323_p6257680154621"></a>Invalid <strong id="en-us_topic_0112992323_b84235270615181_3"><a name="en-us_topic_0112992323_b84235270615181_3"></a><a name="en-us_topic_0112992323_b84235270615181_3"></a>key_id</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row28982612154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p65554970154621"><a name="en-us_topic_0112992323_p65554970154621"></a><a name="en-us_topic_0112992323_p65554970154621"></a>KMS.0206</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p8352323154621"><a name="en-us_topic_0112992323_p8352323154621"></a><a name="en-us_topic_0112992323_p8352323154621"></a>Invalid <strong id="en-us_topic_0112992323_b842352706151819_3"><a name="en-us_topic_0112992323_b842352706151819_3"></a><a name="en-us_topic_0112992323_b842352706151819_3"></a>sequence</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row51165061154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p49045719154621"><a name="en-us_topic_0112992323_p49045719154621"></a><a name="en-us_topic_0112992323_p49045719154621"></a>KMS.0207</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p13280328154621"><a name="en-us_topic_0112992323_p13280328154621"></a><a name="en-us_topic_0112992323_p13280328154621"></a>The key does not exist.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row64820116143054"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p66860179143249"><a name="en-us_topic_0112992323_p66860179143249"></a><a name="en-us_topic_0112992323_p66860179143249"></a>KMS.0208</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p378155143257"><a name="en-us_topic_0112992323_p378155143257"></a><a name="en-us_topic_0112992323_p378155143257"></a>Invalid <strong id="en-us_topic_0112992323_b842352706151838_3"><a name="en-us_topic_0112992323_b842352706151838_3"></a><a name="en-us_topic_0112992323_b842352706151838_3"></a>encryption_context</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row50858275143058"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p20035365143249"><a name="en-us_topic_0112992323_p20035365143249"></a><a name="en-us_topic_0112992323_p20035365143249"></a>KMS.0209</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p7239699143257"><a name="en-us_topic_0112992323_p7239699143257"></a><a name="en-us_topic_0112992323_p7239699143257"></a>The key has been disabled and cannot be used.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1437063314314"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p43157678143249"><a name="en-us_topic_0112992323_p43157678143249"></a><a name="en-us_topic_0112992323_p43157678143249"></a>KMS.0210</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p43249829143257"><a name="en-us_topic_0112992323_p43249829143257"></a><a name="en-us_topic_0112992323_p43249829143257"></a>The key is in the <span class="parmname" id="en-us_topic_0112992323_parmname532832406151857_3"><a name="en-us_topic_0112992323_parmname532832406151857_3"></a><a name="en-us_topic_0112992323_parmname532832406151857_3"></a><b>Pending deletion</b></span> status and cannot be used.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row12151184014483"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p615319406489"><a name="en-us_topic_0112992323_p615319406489"></a><a name="en-us_topic_0112992323_p615319406489"></a>KMS.0211</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p12153194094810"><a name="en-us_topic_0112992323_p12153194094810"></a><a name="en-us_topic_0112992323_p12153194094810"></a>Default Master Keys does not support this operation.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row43880750154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p17683403154621"><a name="en-us_topic_0112992323_p17683403154621"></a><a name="en-us_topic_0112992323_p17683403154621"></a>KMS.0301</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p23069551154621"><a name="en-us_topic_0112992323_p23069551154621"></a><a name="en-us_topic_0112992323_p23069551154621"></a>The value of <strong id="en-us_topic_0112992323_b842352706151926_3"><a name="en-us_topic_0112992323_b842352706151926_3"></a><a name="en-us_topic_0112992323_b842352706151926_3"></a>X-Auth-Token</strong> is null or invalid.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row41184432154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p40486714154621"><a name="en-us_topic_0112992323_p40486714154621"></a><a name="en-us_topic_0112992323_p40486714154621"></a>KMS.0302</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p58198410154621"><a name="en-us_topic_0112992323_p58198410154621"></a><a name="en-us_topic_0112992323_p58198410154621"></a>Invalid <strong id="en-us_topic_0112992323_b842352706151931_3"><a name="en-us_topic_0112992323_b842352706151931_3"></a><a name="en-us_topic_0112992323_b842352706151931_3"></a>X-Auth-Token</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row8562396154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p13839025154621"><a name="en-us_topic_0112992323_p13839025154621"></a><a name="en-us_topic_0112992323_p13839025154621"></a>KMS.0303</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p47219255154621"><a name="en-us_topic_0112992323_p47219255154621"></a><a name="en-us_topic_0112992323_p47219255154621"></a><strong id="en-us_topic_0112992323_b842352706151936_3"><a name="en-us_topic_0112992323_b842352706151936_3"></a><a name="en-us_topic_0112992323_b842352706151936_3"></a>X-Auth-Token</strong> has expired.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row18411563154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p45762004154621"><a name="en-us_topic_0112992323_p45762004154621"></a><a name="en-us_topic_0112992323_p45762004154621"></a>KMS.0305</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p15734820154621"><a name="en-us_topic_0112992323_p15734820154621"></a><a name="en-us_topic_0112992323_p15734820154621"></a>Invalid <strong id="en-us_topic_0112992323_b9138134485718"><a name="en-us_topic_0112992323_b9138134485718"></a><a name="en-us_topic_0112992323_b9138134485718"></a>X-Auth-Token Project Name</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row20807200154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p62177345154621"><a name="en-us_topic_0112992323_p62177345154621"></a><a name="en-us_topic_0112992323_p62177345154621"></a>KMS.0306</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p3200198154621"><a name="en-us_topic_0112992323_p3200198154621"></a><a name="en-us_topic_0112992323_p3200198154621"></a>The user has no permission to access the key.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row15295714154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p51243195154621"><a name="en-us_topic_0112992323_p51243195154621"></a><a name="en-us_topic_0112992323_p51243195154621"></a>KMS.0307</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p57058110154621"><a name="en-us_topic_0112992323_p57058110154621"></a><a name="en-us_topic_0112992323_p57058110154621"></a>The user role has no permission to access the API.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1863211871713"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p6012077510237"><a name="en-us_topic_0112992323_p6012077510237"></a><a name="en-us_topic_0112992323_p6012077510237"></a>KMS.0308</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p3794457810237"><a name="en-us_topic_0112992323_p3794457810237"></a><a name="en-us_topic_0112992323_p3794457810237"></a>Invalid <strong id="en-us_topic_0112992323_b842352706144012_1"><a name="en-us_topic_0112992323_b842352706144012_1"></a><a name="en-us_topic_0112992323_b842352706144012_1"></a><em id="en-us_topic_0112992323_i842352697144018_1"><a name="en-us_topic_0112992323_i842352697144018_1"></a><a name="en-us_topic_0112992323_i842352697144018_1"></a>XXX</em></strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row181681824191711"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1829519713182"><a name="en-us_topic_0112992323_p1829519713182"></a><a name="en-us_topic_0112992323_p1829519713182"></a>KMS.0309</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p1830217791813"><a name="en-us_topic_0112992323_p1830217791813"></a><a name="en-us_topic_0112992323_p1830217791813"></a>The key must be an imported one.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1766519212175"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p10319147181819"><a name="en-us_topic_0112992323_p10319147181819"></a><a name="en-us_topic_0112992323_p10319147181819"></a>KMS.0310</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p132617771815"><a name="en-us_topic_0112992323_p132617771815"></a><a name="en-us_topic_0112992323_p132617771815"></a>The key is not in the <strong id="en-us_topic_0112992323_b1413871042519"><a name="en-us_topic_0112992323_b1413871042519"></a><a name="en-us_topic_0112992323_b1413871042519"></a>Pending import</strong> status.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row116213584288"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p774716815306"><a name="en-us_topic_0112992323_p774716815306"></a><a name="en-us_topic_0112992323_p774716815306"></a>KMS.0401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p97571685307"><a name="en-us_topic_0112992323_p97571685307"></a><a name="en-us_topic_0112992323_p97571685307"></a>The tag list cannot be empty.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row169671378293"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p3770138103014"><a name="en-us_topic_0112992323_p3770138103014"></a><a name="en-us_topic_0112992323_p3770138103014"></a>KMS.0402</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p377819893018"><a name="en-us_topic_0112992323_p377819893018"></a><a name="en-us_topic_0112992323_p377819893018"></a>Invalid value for the <strong id="en-us_topic_0112992323_b842352706214947_1"><a name="en-us_topic_0112992323_b842352706214947_1"></a><a name="en-us_topic_0112992323_b842352706214947_1"></a>value</strong> field in the <strong id="en-us_topic_0112992323_b84235270621502_1"><a name="en-us_topic_0112992323_b84235270621502_1"></a><a name="en-us_topic_0112992323_b84235270621502_1"></a>match</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row13673635142918"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p27951285302"><a name="en-us_topic_0112992323_p27951285302"></a><a name="en-us_topic_0112992323_p27951285302"></a>KMS.0403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p6807168193016"><a name="en-us_topic_0112992323_p6807168193016"></a><a name="en-us_topic_0112992323_p6807168193016"></a>Invalid value for the <strong id="en-us_topic_0112992323_b842352706214947_3"><a name="en-us_topic_0112992323_b842352706214947_3"></a><a name="en-us_topic_0112992323_b842352706214947_3"></a>key</strong> field in the <strong id="en-us_topic_0112992323_b84235270621502_3"><a name="en-us_topic_0112992323_b84235270621502_3"></a><a name="en-us_topic_0112992323_b84235270621502_3"></a>match</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row81051227132914"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1282478163012"><a name="en-us_topic_0112992323_p1282478163012"></a><a name="en-us_topic_0112992323_p1282478163012"></a>KMS.0404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p10834088303"><a name="en-us_topic_0112992323_p10834088303"></a><a name="en-us_topic_0112992323_p10834088303"></a>Invalid value for the <strong id="en-us_topic_0112992323_b842352706215032_1"><a name="en-us_topic_0112992323_b842352706215032_1"></a><a name="en-us_topic_0112992323_b842352706215032_1"></a>action</strong> field.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row20443724132915"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p10852181302"><a name="en-us_topic_0112992323_p10852181302"></a><a name="en-us_topic_0112992323_p10852181302"></a>KMS.0405</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p158621886303"><a name="en-us_topic_0112992323_p158621886303"></a><a name="en-us_topic_0112992323_p158621886303"></a>Invalid value of the <strong id="en-us_topic_0112992323_b842352706214947_5"><a name="en-us_topic_0112992323_b842352706214947_5"></a><a name="en-us_topic_0112992323_b842352706214947_5"></a>value</strong> field in the <strong id="en-us_topic_0112992323_b842352706215129_1"><a name="en-us_topic_0112992323_b842352706215129_1"></a><a name="en-us_topic_0112992323_b842352706215129_1"></a>tag</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row16212022132912"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p087711853013"><a name="en-us_topic_0112992323_p087711853013"></a><a name="en-us_topic_0112992323_p087711853013"></a>KMS.0406</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p108879843019"><a name="en-us_topic_0112992323_p108879843019"></a><a name="en-us_topic_0112992323_p108879843019"></a>Invalid value for the <strong id="en-us_topic_0112992323_b842352706214947_7"><a name="en-us_topic_0112992323_b842352706214947_7"></a><a name="en-us_topic_0112992323_b842352706214947_7"></a>key</strong> field in the <strong id="en-us_topic_0112992323_b842352706215129_3"><a name="en-us_topic_0112992323_b842352706215129_3"></a><a name="en-us_topic_0112992323_b842352706215129_3"></a>tag</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row669715193292"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p6905128143013"><a name="en-us_topic_0112992323_p6905128143013"></a><a name="en-us_topic_0112992323_p6905128143013"></a>KMS.0407</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p1891717812305"><a name="en-us_topic_0112992323_p1891717812305"></a><a name="en-us_topic_0112992323_p1891717812305"></a>Invalid tag list length.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row127771452916"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p15933887305"><a name="en-us_topic_0112992323_p15933887305"></a><a name="en-us_topic_0112992323_p15933887305"></a>KMS.0408</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p1894413816308"><a name="en-us_topic_0112992323_p1894413816308"></a><a name="en-us_topic_0112992323_p1894413816308"></a>Invalid value for the <strong id="en-us_topic_0112992323_b842352706215032_3"><a name="en-us_topic_0112992323_b842352706215032_3"></a><a name="en-us_topic_0112992323_b842352706215032_3"></a>resourceType</strong> field.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1192717119296"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p11959283303"><a name="en-us_topic_0112992323_p11959283303"></a><a name="en-us_topic_0112992323_p11959283303"></a>KMS.0409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p1996911817308"><a name="en-us_topic_0112992323_p1996911817308"></a><a name="en-us_topic_0112992323_p1996911817308"></a>The total number of tags has exceeded the upper limit.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1152194296"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p59831086308"><a name="en-us_topic_0112992323_p59831086308"></a><a name="en-us_topic_0112992323_p59831086308"></a>KMS.0410</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p159925817302"><a name="en-us_topic_0112992323_p159925817302"></a><a name="en-us_topic_0112992323_p159925817302"></a>Invalid length of the <strong id="en-us_topic_0112992323_b84235270621535_1"><a name="en-us_topic_0112992323_b84235270621535_1"></a><a name="en-us_topic_0112992323_b84235270621535_1"></a>value</strong> field in the <strong id="en-us_topic_0112992323_b842352706215317_1"><a name="en-us_topic_0112992323_b842352706215317_1"></a><a name="en-us_topic_0112992323_b842352706215317_1"></a>tag</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row175266102920"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1315891306"><a name="en-us_topic_0112992323_p1315891306"></a><a name="en-us_topic_0112992323_p1315891306"></a>KMS.0411</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p52610973015"><a name="en-us_topic_0112992323_p52610973015"></a><a name="en-us_topic_0112992323_p52610973015"></a>Invalid length of the <strong id="en-us_topic_0112992323_b84235270621535_3"><a name="en-us_topic_0112992323_b84235270621535_3"></a><a name="en-us_topic_0112992323_b84235270621535_3"></a>key</strong> field in the <strong id="en-us_topic_0112992323_b842352706215317_3"><a name="en-us_topic_0112992323_b842352706215317_3"></a><a name="en-us_topic_0112992323_b842352706215317_3"></a>tag</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row199487113293"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p104119173019"><a name="en-us_topic_0112992323_p104119173019"></a><a name="en-us_topic_0112992323_p104119173019"></a>KMS.0412</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p95210903019"><a name="en-us_topic_0112992323_p95210903019"></a><a name="en-us_topic_0112992323_p95210903019"></a>Invalid length of the key list in the <strong id="en-us_topic_0112992323_b842352706215317_5"><a name="en-us_topic_0112992323_b842352706215317_5"></a><a name="en-us_topic_0112992323_b842352706215317_5"></a>tag</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row57849989141249"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p53156740141249"><a name="en-us_topic_0112992323_p53156740141249"></a><a name="en-us_topic_0112992323_p53156740141249"></a>KMS.0413</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p10728647141249"><a name="en-us_topic_0112992323_p10728647141249"></a><a name="en-us_topic_0112992323_p10728647141249"></a>Invalid length of the value list in the <strong id="en-us_topic_0112992323_b842352706215317_7"><a name="en-us_topic_0112992323_b842352706215317_7"></a><a name="en-us_topic_0112992323_b842352706215317_7"></a>tag</strong> parameter has exceeded the upper limit.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row52121731132712"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p42133318275"><a name="en-us_topic_0112992323_p42133318275"></a><a name="en-us_topic_0112992323_p42133318275"></a>KMS.0417</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p82135314275"><a name="en-us_topic_0112992323_p82135314275"></a><a name="en-us_topic_0112992323_p82135314275"></a>The value of <strong id="en-us_topic_0112992323_b107061748136"><a name="en-us_topic_0112992323_b107061748136"></a><a name="en-us_topic_0112992323_b107061748136"></a>offset</strong> must be greater than or equal to <strong id="en-us_topic_0112992323_b122935160133"><a name="en-us_topic_0112992323_b122935160133"></a><a name="en-us_topic_0112992323_b122935160133"></a>0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1861713514276"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1628258142911"><a name="en-us_topic_0112992323_p1628258142911"></a><a name="en-us_topic_0112992323_p1628258142911"></a>KMS.0418</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p15618335102714"><a name="en-us_topic_0112992323_p15618335102714"></a><a name="en-us_topic_0112992323_p15618335102714"></a><strong id="en-us_topic_0112992323_b174098475147"><a name="en-us_topic_0112992323_b174098475147"></a><a name="en-us_topic_0112992323_b174098475147"></a>offset</strong> is not required.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row62531316154418"><td class="cellrowborder" rowspan="5" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p31871856154418"><a name="en-us_topic_0112992323_p31871856154418"></a><a name="en-us_topic_0112992323_p31871856154418"></a>Creating a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p41820627154939"><a name="en-us_topic_0112992323_p41820627154939"></a><a name="en-us_topic_0112992323_p41820627154939"></a>KMS.1101</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p43873813154956"><a name="en-us_topic_0112992323_p43873813154956"></a><a name="en-us_topic_0112992323_p43873813154956"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152019_5"><a name="en-us_topic_0112992323_b842352706152019_5"></a><a name="en-us_topic_0112992323_b842352706152019_5"></a>key_alias</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row296556154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p19813420154939"><a name="en-us_topic_0112992323_p19813420154939"></a><a name="en-us_topic_0112992323_p19813420154939"></a>KMS.1102</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p40190699154956"><a name="en-us_topic_0112992323_p40190699154956"></a><a name="en-us_topic_0112992323_p40190699154956"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152027_3"><a name="en-us_topic_0112992323_b842352706152027_3"></a><a name="en-us_topic_0112992323_b842352706152027_3"></a>realm</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row63059321154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p15577956154939"><a name="en-us_topic_0112992323_p15577956154939"></a><a name="en-us_topic_0112992323_p15577956154939"></a>KMS.1103</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p39555005154956"><a name="en-us_topic_0112992323_p39555005154956"></a><a name="en-us_topic_0112992323_p39555005154956"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152032_5"><a name="en-us_topic_0112992323_b842352706152032_5"></a><a name="en-us_topic_0112992323_b842352706152032_5"></a>key_description</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row54537876154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p14932478154939"><a name="en-us_topic_0112992323_p14932478154939"></a><a name="en-us_topic_0112992323_p14932478154939"></a>KMS.1104</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p45896070154956"><a name="en-us_topic_0112992323_p45896070154956"></a><a name="en-us_topic_0112992323_p45896070154956"></a>Existing CMK alias.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row53984193154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p14141190154939"><a name="en-us_topic_0112992323_p14141190154939"></a><a name="en-us_topic_0112992323_p14141190154939"></a>KMS.1105</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p38020873154956"><a name="en-us_topic_0112992323_p38020873154956"></a><a name="en-us_topic_0112992323_p38020873154956"></a>The number of keys has reached the upper limit.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row41629776154418"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p16568659154418"><a name="en-us_topic_0112992323_p16568659154418"></a><a name="en-us_topic_0112992323_p16568659154418"></a>Enabling a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p66993040154418"><a name="en-us_topic_0112992323_p66993040154418"></a><a name="en-us_topic_0112992323_p66993040154418"></a>KMS.1201</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p57727149154418"><a name="en-us_topic_0112992323_p57727149154418"></a><a name="en-us_topic_0112992323_p57727149154418"></a>The key is not disabled.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row25191766154418"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p27267205154418"><a name="en-us_topic_0112992323_p27267205154418"></a><a name="en-us_topic_0112992323_p27267205154418"></a>Disabling a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p61160029154418"><a name="en-us_topic_0112992323_p61160029154418"></a><a name="en-us_topic_0112992323_p61160029154418"></a>KMS.1301</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p21928800155110"><a name="en-us_topic_0112992323_p21928800155110"></a><a name="en-us_topic_0112992323_p21928800155110"></a>The key is not enabled.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row25375662154418"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p42162770154418"><a name="en-us_topic_0112992323_p42162770154418"></a><a name="en-us_topic_0112992323_p42162770154418"></a>Scheduling the deletion of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p44662345155149"><a name="en-us_topic_0112992323_p44662345155149"></a><a name="en-us_topic_0112992323_p44662345155149"></a>KMS.1401</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p27759761155159"><a name="en-us_topic_0112992323_p27759761155159"></a><a name="en-us_topic_0112992323_p27759761155159"></a>The deletion of CMKs can be scheduled by 7 to 1096 days in advance.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row64798697154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p11050762155149"><a name="en-us_topic_0112992323_p11050762155149"></a><a name="en-us_topic_0112992323_p11050762155149"></a>KMS.1402</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p37097900155159"><a name="en-us_topic_0112992323_p37097900155159"></a><a name="en-us_topic_0112992323_p37097900155159"></a>The key is in the <span class="parmname" id="en-us_topic_0112992323_parmname101046398315219_3"><a name="en-us_topic_0112992323_parmname101046398315219_3"></a><a name="en-us_topic_0112992323_parmname101046398315219_3"></a><b>Pending deletion</b></span> status.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row19318344154418"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p21282014154418"><a name="en-us_topic_0112992323_p21282014154418"></a><a name="en-us_topic_0112992323_p21282014154418"></a>Canceling the scheduled deletion of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p6000159155214"><a name="en-us_topic_0112992323_p6000159155214"></a><a name="en-us_topic_0112992323_p6000159155214"></a>KMS.1501</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p7978169155228"><a name="en-us_topic_0112992323_p7978169155228"></a><a name="en-us_topic_0112992323_p7978169155228"></a>The key is not in the <span class="parmname" id="en-us_topic_0112992323_parmname3391520793953_3"><a name="en-us_topic_0112992323_parmname3391520793953_3"></a><a name="en-us_topic_0112992323_parmname3391520793953_3"></a><b>Pending deletion</b></span> status.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row15804323154418"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p5081805154418"><a name="en-us_topic_0112992323_p5081805154418"></a><a name="en-us_topic_0112992323_p5081805154418"></a>Querying the list of CMKs</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p4339915155311"><a name="en-us_topic_0112992323_p4339915155311"></a><a name="en-us_topic_0112992323_p4339915155311"></a>KMS.1601</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p49789199155326"><a name="en-us_topic_0112992323_p49789199155326"></a><a name="en-us_topic_0112992323_p49789199155326"></a>The value of <strong id="en-us_topic_0112992323_b842352706152131_3"><a name="en-us_topic_0112992323_b842352706152131_3"></a><a name="en-us_topic_0112992323_b842352706152131_3"></a>limit</strong> falls beyond the range.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row24009887155248"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p9682146155311"><a name="en-us_topic_0112992323_p9682146155311"></a><a name="en-us_topic_0112992323_p9682146155311"></a>KMS.1602</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p57540059155326"><a name="en-us_topic_0112992323_p57540059155326"></a><a name="en-us_topic_0112992323_p57540059155326"></a>The value of <strong id="en-us_topic_0112992323_b842352706152140_3"><a name="en-us_topic_0112992323_b842352706152140_3"></a><a name="en-us_topic_0112992323_b842352706152140_3"></a>marker</strong> must be greater than or equal to 0.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row15484320154418"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p46270416154418"><a name="en-us_topic_0112992323_p46270416154418"></a><a name="en-us_topic_0112992323_p46270416154418"></a>Creating a random number</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p13184635155431"><a name="en-us_topic_0112992323_p13184635155431"></a><a name="en-us_topic_0112992323_p13184635155431"></a>KMS.1801</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p47474976155439"><a name="en-us_topic_0112992323_p47474976155439"></a><a name="en-us_topic_0112992323_p47474976155439"></a><strong id="en-us_topic_0112992323_b842352706152148_3"><a name="en-us_topic_0112992323_b842352706152148_3"></a><a name="en-us_topic_0112992323_b842352706152148_3"></a>random_data_length</strong> must contain 512 bits.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row48741285154418"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p18114935143550"><a name="en-us_topic_0112992323_p18114935143550"></a><a name="en-us_topic_0112992323_p18114935143550"></a>Creating a DEK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p26042331155524"><a name="en-us_topic_0112992323_p26042331155524"></a><a name="en-us_topic_0112992323_p26042331155524"></a>KMS.1901</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p37548888155534"><a name="en-us_topic_0112992323_p37548888155534"></a><a name="en-us_topic_0112992323_p37548888155534"></a><strong id="en-us_topic_0112992323_b842352706152156_3"><a name="en-us_topic_0112992323_b842352706152156_3"></a><a name="en-us_topic_0112992323_b842352706152156_3"></a>datakey_length</strong> must contain 512 bits.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row21385139154418"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p63824153143531"><a name="en-us_topic_0112992323_p63824153143531"></a><a name="en-us_topic_0112992323_p63824153143531"></a>Creating a plaintext-free DEK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p21383760155556"><a name="en-us_topic_0112992323_p21383760155556"></a><a name="en-us_topic_0112992323_p21383760155556"></a>KMS.2001</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p2458187615568"><a name="en-us_topic_0112992323_p2458187615568"></a><a name="en-us_topic_0112992323_p2458187615568"></a><strong id="en-us_topic_0112992323_b84235270615225_3"><a name="en-us_topic_0112992323_b84235270615225_3"></a><a name="en-us_topic_0112992323_b84235270615225_3"></a>datakey_length</strong> must contain 512 bits.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row12716429154418"><td class="cellrowborder" rowspan="3" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p23397809154418"><a name="en-us_topic_0112992323_p23397809154418"></a><a name="en-us_topic_0112992323_p23397809154418"></a>Encrypting a DEK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p43886383143428"><a name="en-us_topic_0112992323_p43886383143428"></a><a name="en-us_topic_0112992323_p43886383143428"></a>KMS.2101</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p65136145143428"><a name="en-us_topic_0112992323_p65136145143428"></a><a name="en-us_topic_0112992323_p65136145143428"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152213_3"><a name="en-us_topic_0112992323_b842352706152213_3"></a><a name="en-us_topic_0112992323_b842352706152213_3"></a>plain_text</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row24730372155637"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p38283427143428"><a name="en-us_topic_0112992323_p38283427143428"></a><a name="en-us_topic_0112992323_p38283427143428"></a>KMS.2102</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p13949920143428"><a name="en-us_topic_0112992323_p13949920143428"></a><a name="en-us_topic_0112992323_p13949920143428"></a><strong id="en-us_topic_0112992323_b842352706152220_3"><a name="en-us_topic_0112992323_b842352706152220_3"></a><a name="en-us_topic_0112992323_b842352706152220_3"></a>datakey_plain_length</strong> must contain 64 bytes.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row47064576154418"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p36053479143428"><a name="en-us_topic_0112992323_p36053479143428"></a><a name="en-us_topic_0112992323_p36053479143428"></a>KMS.2103</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p34650680143428"><a name="en-us_topic_0112992323_p34650680143428"></a><a name="en-us_topic_0112992323_p34650680143428"></a>Hash verification of the data encryption key failed.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row3930497154418"><td class="cellrowborder" rowspan="3" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p49934856154418"><a name="en-us_topic_0112992323_p49934856154418"></a><a name="en-us_topic_0112992323_p49934856154418"></a>Decrypting a DEK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p65320562143451"><a name="en-us_topic_0112992323_p65320562143451"></a><a name="en-us_topic_0112992323_p65320562143451"></a>KMS.2201</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p56474176143451"><a name="en-us_topic_0112992323_p56474176143451"></a><a name="en-us_topic_0112992323_p56474176143451"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152237_3"><a name="en-us_topic_0112992323_b842352706152237_3"></a><a name="en-us_topic_0112992323_b842352706152237_3"></a>cipher_text</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row61123984155723"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p31941391143451"><a name="en-us_topic_0112992323_p31941391143451"></a><a name="en-us_topic_0112992323_p31941391143451"></a>KMS.2202</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p37115841143451"><a name="en-us_topic_0112992323_p37115841143451"></a><a name="en-us_topic_0112992323_p37115841143451"></a><strong id="en-us_topic_0112992323_b842352706152242_3"><a name="en-us_topic_0112992323_b842352706152242_3"></a><a name="en-us_topic_0112992323_b842352706152242_3"></a>datakey_cipher_length</strong> must contain 64 bytes.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row23019628155727"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p12576399143451"><a name="en-us_topic_0112992323_p12576399143451"></a><a name="en-us_topic_0112992323_p12576399143451"></a>KMS.2203</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p12055408143451"><a name="en-us_topic_0112992323_p12055408143451"></a><a name="en-us_topic_0112992323_p12055408143451"></a>Hash verification of the data encryption key failed.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row6132434142750"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p17842562142749"><a name="en-us_topic_0112992323_p17842562142749"></a><a name="en-us_topic_0112992323_p17842562142749"></a>Changing the alias of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p35961407142749"><a name="en-us_topic_0112992323_p35961407142749"></a><a name="en-us_topic_0112992323_p35961407142749"></a>KMS.1101</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p27192836142749"><a name="en-us_topic_0112992323_p27192836142749"></a><a name="en-us_topic_0112992323_p27192836142749"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152019_7"><a name="en-us_topic_0112992323_b842352706152019_7"></a><a name="en-us_topic_0112992323_b842352706152019_7"></a>key_alias</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row52877164142750"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p26463055142749"><a name="en-us_topic_0112992323_p26463055142749"></a><a name="en-us_topic_0112992323_p26463055142749"></a>KMS.1104</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p63132688142749"><a name="en-us_topic_0112992323_p63132688142749"></a><a name="en-us_topic_0112992323_p63132688142749"></a>Existing CMK alias.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row13331780142750"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p54158351142749"><a name="en-us_topic_0112992323_p54158351142749"></a><a name="en-us_topic_0112992323_p54158351142749"></a>Changing the description of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p24750295142749"><a name="en-us_topic_0112992323_p24750295142749"></a><a name="en-us_topic_0112992323_p24750295142749"></a>KMS.1103</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p58616855142749"><a name="en-us_topic_0112992323_p58616855142749"></a><a name="en-us_topic_0112992323_p58616855142749"></a>Invalid <strong id="en-us_topic_0112992323_b842352706152032_7"><a name="en-us_topic_0112992323_b842352706152032_7"></a><a name="en-us_topic_0112992323_b842352706152032_7"></a>key_description</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row62262159102228"><td class="cellrowborder" rowspan="5" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p10070129102228"><a name="en-us_topic_0112992323_p10070129102228"></a><a name="en-us_topic_0112992323_p10070129102228"></a>Creating a grant</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p10374144102228"><a name="en-us_topic_0112992323_p10374144102228"></a><a name="en-us_topic_0112992323_p10374144102228"></a>KMS.2401</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p34999331102228"><a name="en-us_topic_0112992323_p34999331102228"></a><a name="en-us_topic_0112992323_p34999331102228"></a><strong id="en-us_topic_0112992323_b84235270614419_1"><a name="en-us_topic_0112992323_b84235270614419_1"></a><a name="en-us_topic_0112992323_b84235270614419_1"></a>create-grant</strong> cannot be the only granted operation permission.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row18579138102233"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p28032430102233"><a name="en-us_topic_0112992323_p28032430102233"></a><a name="en-us_topic_0112992323_p28032430102233"></a>KMS.2402</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p56034324102233"><a name="en-us_topic_0112992323_p56034324102233"></a><a name="en-us_topic_0112992323_p56034324102233"></a>Invalid principal for creating/retiring a grant.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row48681745102237"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p29846104102237"><a name="en-us_topic_0112992323_p29846104102237"></a><a name="en-us_topic_0112992323_p29846104102237"></a>KMS.2403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p1615356102237"><a name="en-us_topic_0112992323_p1615356102237"></a><a name="en-us_topic_0112992323_p1615356102237"></a>Failed to create a grant.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row37343016102245"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p60178386102245"><a name="en-us_topic_0112992323_p60178386102245"></a><a name="en-us_topic_0112992323_p60178386102245"></a>KMS.2404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p42611132102245"><a name="en-us_topic_0112992323_p42611132102245"></a><a name="en-us_topic_0112992323_p42611132102245"></a>No more permissions can be granted for the CMK.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row51214308102249"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p2994290102249"><a name="en-us_topic_0112992323_p2994290102249"></a><a name="en-us_topic_0112992323_p2994290102249"></a>KMS.2405</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p41210942102249"><a name="en-us_topic_0112992323_p41210942102249"></a><a name="en-us_topic_0112992323_p41210942102249"></a>You cannot grant any more permissions to the principal.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row46118878102754"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p8479358103258"><a name="en-us_topic_0112992323_p8479358103258"></a><a name="en-us_topic_0112992323_p8479358103258"></a>Querying grants on a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p59200171102754"><a name="en-us_topic_0112992323_p59200171102754"></a><a name="en-us_topic_0112992323_p59200171102754"></a>KMS.1601</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p30484538102754"><a name="en-us_topic_0112992323_p30484538102754"></a><a name="en-us_topic_0112992323_p30484538102754"></a>The value of <strong id="en-us_topic_0112992323_b842352706152131_5"><a name="en-us_topic_0112992323_b842352706152131_5"></a><a name="en-us_topic_0112992323_b842352706152131_5"></a>limit</strong> falls beyond the range.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row2258532102759"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p54282792102759"><a name="en-us_topic_0112992323_p54282792102759"></a><a name="en-us_topic_0112992323_p54282792102759"></a>KMS.1602</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p34830071102759"><a name="en-us_topic_0112992323_p34830071102759"></a><a name="en-us_topic_0112992323_p34830071102759"></a>The value of <strong id="en-us_topic_0112992323_b842352706152140_5"><a name="en-us_topic_0112992323_b842352706152140_5"></a><a name="en-us_topic_0112992323_b842352706152140_5"></a>marker</strong> must be greater than or equal to 0.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row5497240910283"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1992632410333"><a name="en-us_topic_0112992323_p1992632410333"></a><a name="en-us_topic_0112992323_p1992632410333"></a>Querying grants that can be retired</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p3094278610283"><a name="en-us_topic_0112992323_p3094278610283"></a><a name="en-us_topic_0112992323_p3094278610283"></a>KMS.1601</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p2333771310283"><a name="en-us_topic_0112992323_p2333771310283"></a><a name="en-us_topic_0112992323_p2333771310283"></a>The value of <strong id="en-us_topic_0112992323_b842352706152131_7"><a name="en-us_topic_0112992323_b842352706152131_7"></a><a name="en-us_topic_0112992323_b842352706152131_7"></a>limit</strong> falls beyond the range.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row3775000510289"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p4608050110289"><a name="en-us_topic_0112992323_p4608050110289"></a><a name="en-us_topic_0112992323_p4608050110289"></a>KMS.1602</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p4153307710289"><a name="en-us_topic_0112992323_p4153307710289"></a><a name="en-us_topic_0112992323_p4153307710289"></a>The value of <strong id="en-us_topic_0112992323_b842352706152140_7"><a name="en-us_topic_0112992323_b842352706152140_7"></a><a name="en-us_topic_0112992323_b842352706152140_7"></a>marker</strong> must be greater than or equal to 0.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row35450369102815"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p6563532710338"><a name="en-us_topic_0112992323_p6563532710338"></a><a name="en-us_topic_0112992323_p6563532710338"></a>Revoking a grant</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p57659004102815"><a name="en-us_topic_0112992323_p57659004102815"></a><a name="en-us_topic_0112992323_p57659004102815"></a>KMS.2501</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p39867754102815"><a name="en-us_topic_0112992323_p39867754102815"></a><a name="en-us_topic_0112992323_p39867754102815"></a>The grant does not exist.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row3910842210317"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p3317542310317"><a name="en-us_topic_0112992323_p3317542310317"></a><a name="en-us_topic_0112992323_p3317542310317"></a>KMS.2502</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p285475810317"><a name="en-us_topic_0112992323_p285475810317"></a><a name="en-us_topic_0112992323_p285475810317"></a>The <strong id="en-us_topic_0112992323_b842352706144520_1"><a name="en-us_topic_0112992323_b842352706144520_1"></a><a name="en-us_topic_0112992323_b842352706144520_1"></a>grant_id</strong> value does not match the <strong id="en-us_topic_0112992323_b842352706144536_1"><a name="en-us_topic_0112992323_b842352706144536_1"></a><a name="en-us_topic_0112992323_b842352706144536_1"></a>key_id</strong> value.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row21268985103112"><td class="cellrowborder" rowspan="2" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p53960478103313"><a name="en-us_topic_0112992323_p53960478103313"></a><a name="en-us_topic_0112992323_p53960478103313"></a>Retiring a grant</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p26484289103112"><a name="en-us_topic_0112992323_p26484289103112"></a><a name="en-us_topic_0112992323_p26484289103112"></a>KMS.2501</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p64852674103112"><a name="en-us_topic_0112992323_p64852674103112"></a><a name="en-us_topic_0112992323_p64852674103112"></a>The grant does not exist.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row48457618103116"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p35747350103116"><a name="en-us_topic_0112992323_p35747350103116"></a><a name="en-us_topic_0112992323_p35747350103116"></a>KMS.2502</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p9854277103116"><a name="en-us_topic_0112992323_p9854277103116"></a><a name="en-us_topic_0112992323_p9854277103116"></a>The <strong id="en-us_topic_0112992323_b842352706144520_3"><a name="en-us_topic_0112992323_b842352706144520_3"></a><a name="en-us_topic_0112992323_b842352706144520_3"></a>grant_id</strong> value does not match the <strong id="en-us_topic_0112992323_b842352706144536_3"><a name="en-us_topic_0112992323_b842352706144536_3"></a><a name="en-us_topic_0112992323_b842352706144536_3"></a>key_id</strong> value.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row12656557181"><td class="cellrowborder" rowspan="6" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p282617162195"><a name="en-us_topic_0112992323_p282617162195"></a><a name="en-us_topic_0112992323_p282617162195"></a>Importing CMK material</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p8833181651911"><a name="en-us_topic_0112992323_p8833181651911"></a><a name="en-us_topic_0112992323_p8833181651911"></a>KMS.2601</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p1583917166198"><a name="en-us_topic_0112992323_p1583917166198"></a><a name="en-us_topic_0112992323_p1583917166198"></a>Invalid token.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1133631521910"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p484921651915"><a name="en-us_topic_0112992323_p484921651915"></a><a name="en-us_topic_0112992323_p484921651915"></a>KMS.2602</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p685831651916"><a name="en-us_topic_0112992323_p685831651916"></a><a name="en-us_topic_0112992323_p685831651916"></a>The expiration time of an imported key must be later than the current time.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row11823151251916"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p15868161681911"><a name="en-us_topic_0112992323_p15868161681911"></a><a name="en-us_topic_0112992323_p15868161681911"></a>KMS.2603</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p087721641914"><a name="en-us_topic_0112992323_p087721641914"></a><a name="en-us_topic_0112992323_p087721641914"></a>The <strong id="en-us_topic_0112992323_b842352706163344_1"><a name="en-us_topic_0112992323_b842352706163344_1"></a><a name="en-us_topic_0112992323_b842352706163344_1"></a>key_id</strong> does not match the <strong id="en-us_topic_0112992323_b842352706163348_1"><a name="en-us_topic_0112992323_b842352706163348_1"></a><a name="en-us_topic_0112992323_b842352706163348_1"></a>key_id</strong> value in the token.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1919810981916"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1788913163191"><a name="en-us_topic_0112992323_p1788913163191"></a><a name="en-us_topic_0112992323_p1788913163191"></a>KMS.2604</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p78975165197"><a name="en-us_topic_0112992323_p78975165197"></a><a name="en-us_topic_0112992323_p78975165197"></a>The length of the external key in plaintext must be 32 bits.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row1597519612199"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1491131631915"><a name="en-us_topic_0112992323_p1491131631915"></a><a name="en-us_topic_0112992323_p1491131631915"></a>KMS.2605</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p189166168192"><a name="en-us_topic_0112992323_p189166168192"></a><a name="en-us_topic_0112992323_p189166168192"></a>Token verification failed.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row15860174131912"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p792791691915"><a name="en-us_topic_0112992323_p792791691915"></a><a name="en-us_topic_0112992323_p792791691915"></a>KMS.2606</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p1793541621912"><a name="en-us_topic_0112992323_p1793541621912"></a><a name="en-us_topic_0112992323_p1793541621912"></a>When you re-import the material of a deleted CMK, the external key in plaintext must be consistent with that imported earlier.</p>
</td>
</tr>
<tr id="en-us_topic_0112992323_row92791726199"><td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0112992323_p1094591671914"><a name="en-us_topic_0112992323_p1094591671914"></a><a name="en-us_topic_0112992323_p1094591671914"></a>Deleting CMK material</p>
</td>
<td class="cellrowborder" valign="top" width="15.340000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0112992323_p10953171651912"><a name="en-us_topic_0112992323_p10953171651912"></a><a name="en-us_topic_0112992323_p10953171651912"></a>KMS.2701</p>
</td>
<td class="cellrowborder" valign="top" width="55.60000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0112992323_p896191614198"><a name="en-us_topic_0112992323_p896191614198"></a><a name="en-us_topic_0112992323_p896191614198"></a>CMK material can be deleted only when the CMK is in <strong id="en-us_topic_0112992323_b84235270616382_1"><a name="en-us_topic_0112992323_b84235270616382_1"></a><a name="en-us_topic_0112992323_b84235270616382_1"></a>Enabled</strong> or <strong id="en-us_topic_0112992323_b84235270616388_1"><a name="en-us_topic_0112992323_b84235270616388_1"></a><a name="en-us_topic_0112992323_b84235270616388_1"></a>Disabled</strong> status.</p>
</td>
</tr>
</tbody>
</table>

