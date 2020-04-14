# Encryption Key Management<a name="kms_02_0306"></a>

<a name="en-us_topic_0150789026_table15642105118238"></a>
<table><thead align="left"><tr id="en-us_topic_0150789026_row16642125122310"><th class="cellrowborder" valign="top" width="48.40484048404841%" id="mcps1.1.4.1.1"><p id="en-us_topic_0150789026_p18781717245"><a name="en-us_topic_0150789026_p18781717245"></a><a name="en-us_topic_0150789026_p18781717245"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="25.882588258825884%" id="mcps1.1.4.1.2"><p id="en-us_topic_0150789026_p48811517242"><a name="en-us_topic_0150789026_p48811517242"></a><a name="en-us_topic_0150789026_p48811517242"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="25.712571257125717%" id="mcps1.1.4.1.3"><p id="en-us_topic_0150789026_p988671152417"><a name="en-us_topic_0150789026_p988671152417"></a><a name="en-us_topic_0150789026_p988671152417"></a>Permission</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0150789026_row76421513237"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p8311193815241"><a name="en-us_topic_0150789026_p8311193815241"></a><a name="en-us_topic_0150789026_p8311193815241"></a>POST /v1.0/{project_id}/kms/create-key</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1793833014261"><a name="en-us_topic_0150789026_p1793833014261"></a><a name="en-us_topic_0150789026_p1793833014261"></a>Creates a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p196421651202310"><a name="en-us_topic_0150789026_p196421651202310"></a><a name="en-us_topic_0150789026_p196421651202310"></a>kms:cmk:create</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row202041242184413"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1570925614412"><a name="en-us_topic_0150789026_p1570925614412"></a><a name="en-us_topic_0150789026_p1570925614412"></a>POST /v1.0/{project_id}/kms/enable-key</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p771135654415"><a name="en-us_topic_0150789026_p771135654415"></a><a name="en-us_topic_0150789026_p771135654415"></a>Enables a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p1571375619443"><a name="en-us_topic_0150789026_p1571375619443"></a><a name="en-us_topic_0150789026_p1571375619443"></a>kms:cmk:enable</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row71614715444"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p82362119452"><a name="en-us_topic_0150789026_p82362119452"></a><a name="en-us_topic_0150789026_p82362119452"></a>POST /v1.0/{project_id}/kms/disable-key</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1123971194518"><a name="en-us_topic_0150789026_p1123971194518"></a><a name="en-us_topic_0150789026_p1123971194518"></a>Disables a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p10244416453"><a name="en-us_topic_0150789026_p10244416453"></a><a name="en-us_topic_0150789026_p10244416453"></a>kms:cmk:disable</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row7285027184511"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1925128104513"><a name="en-us_topic_0150789026_p1925128104513"></a><a name="en-us_topic_0150789026_p1925128104513"></a>POST /v1.0/{project_id}/kms/schedule-key-deletion</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p79311928174520"><a name="en-us_topic_0150789026_p79311928174520"></a><a name="en-us_topic_0150789026_p79311928174520"></a>Schedules the deletion of a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p149351128174512"><a name="en-us_topic_0150789026_p149351128174512"></a><a name="en-us_topic_0150789026_p149351128174512"></a>kms:cmk:update</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1610754234515"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p68051853124511"><a name="en-us_topic_0150789026_p68051853124511"></a><a name="en-us_topic_0150789026_p68051853124511"></a>POST /v1.0/{project_id}/kms/cancel-key-deletion</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p8807195316454"><a name="en-us_topic_0150789026_p8807195316454"></a><a name="en-us_topic_0150789026_p8807195316454"></a>Cancels the scheduled deletion of a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p180905312455"><a name="en-us_topic_0150789026_p180905312455"></a><a name="en-us_topic_0150789026_p180905312455"></a>kms:cmk:update</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row164225114236"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p20311638142417"><a name="en-us_topic_0150789026_p20311638142417"></a><a name="en-us_topic_0150789026_p20311638142417"></a>POST /v1.0/{project_id}/kms/list-keys</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1393816306264"><a name="en-us_topic_0150789026_p1393816306264"></a><a name="en-us_topic_0150789026_p1393816306264"></a>Queries the list of CMKs.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p56421151192319"><a name="en-us_topic_0150789026_p56421151192319"></a><a name="en-us_topic_0150789026_p56421151192319"></a>kms:cmk:list</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1642185182313"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p12311338162411"><a name="en-us_topic_0150789026_p12311338162411"></a><a name="en-us_topic_0150789026_p12311338162411"></a>POST /v1.0/{project_id}/kms/describe-key</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p7938103013265"><a name="en-us_topic_0150789026_p7938103013265"></a><a name="en-us_topic_0150789026_p7938103013265"></a>Queries the CMK information.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p16643351112317"><a name="en-us_topic_0150789026_p16643351112317"></a><a name="en-us_topic_0150789026_p16643351112317"></a>kms:cmk:get</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row7643115116233"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p18312183872413"><a name="en-us_topic_0150789026_p18312183872413"></a><a name="en-us_topic_0150789026_p18312183872413"></a>POST /v1.0/{project_id}/kms/gen-random</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p159415300264"><a name="en-us_topic_0150789026_p159415300264"></a><a name="en-us_topic_0150789026_p159415300264"></a>Generates a random number.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p9643135102314"><a name="en-us_topic_0150789026_p9643135102314"></a><a name="en-us_topic_0150789026_p9643135102314"></a>kms:cmk:generate</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row15643175119238"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p2312238192418"><a name="en-us_topic_0150789026_p2312238192418"></a><a name="en-us_topic_0150789026_p2312238192418"></a>POST /v1.0/{project_id}/kms/create-datakey</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p5941183014266"><a name="en-us_topic_0150789026_p5941183014266"></a><a name="en-us_topic_0150789026_p5941183014266"></a>Creates a DEK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p2643151162313"><a name="en-us_topic_0150789026_p2643151162313"></a><a name="en-us_topic_0150789026_p2643151162313"></a>kms:dek:create</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row16643551192319"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1331216384249"><a name="en-us_topic_0150789026_p1331216384249"></a><a name="en-us_topic_0150789026_p1331216384249"></a>POST /v1.0/{project_id}/kms/create-datakey-without-plaintext</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p199419308267"><a name="en-us_topic_0150789026_p199419308267"></a><a name="en-us_topic_0150789026_p199419308267"></a>Creates a plaintext-free DEK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p86431851112319"><a name="en-us_topic_0150789026_p86431851112319"></a><a name="en-us_topic_0150789026_p86431851112319"></a>kms:dek:create</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row19643351192319"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1312203872419"><a name="en-us_topic_0150789026_p1312203872419"></a><a name="en-us_topic_0150789026_p1312203872419"></a>POST /v1.0/{project_id}/kms/encrypt-datakey</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p99413305266"><a name="en-us_topic_0150789026_p99413305266"></a><a name="en-us_topic_0150789026_p99413305266"></a>Encrypts a DEK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p8766011122914"><a name="en-us_topic_0150789026_p8766011122914"></a><a name="en-us_topic_0150789026_p8766011122914"></a>kms:dek:crypto</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row16434516233"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1731283812243"><a name="en-us_topic_0150789026_p1731283812243"></a><a name="en-us_topic_0150789026_p1731283812243"></a>POST /v1.0/{project_id}/kms/decrypt-datakey</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p18941193012263"><a name="en-us_topic_0150789026_p18941193012263"></a><a name="en-us_topic_0150789026_p18941193012263"></a>Decrypts a DEK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p10766131112298"><a name="en-us_topic_0150789026_p10766131112298"></a><a name="en-us_topic_0150789026_p10766131112298"></a>kms:dek:crypto</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row0643115113238"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p3312038152411"><a name="en-us_topic_0150789026_p3312038152411"></a><a name="en-us_topic_0150789026_p3312038152411"></a>GET /v1.0/{project_id}/kms/user-instances</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p59411630102619"><a name="en-us_topic_0150789026_p59411630102619"></a><a name="en-us_topic_0150789026_p59411630102619"></a>Queries the number of instances.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p196432051132312"><a name="en-us_topic_0150789026_p196432051132312"></a><a name="en-us_topic_0150789026_p196432051132312"></a>kms:cmk:getInstance</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row36431351142310"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p031211386247"><a name="en-us_topic_0150789026_p031211386247"></a><a name="en-us_topic_0150789026_p031211386247"></a>GET /v1.0/{project_id}/kms/user-quotas</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p69411930192610"><a name="en-us_topic_0150789026_p69411930192610"></a><a name="en-us_topic_0150789026_p69411930192610"></a>Queries the user quota.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p864475102315"><a name="en-us_topic_0150789026_p864475102315"></a><a name="en-us_topic_0150789026_p864475102315"></a>kms:cmk:getQuota</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row164465114234"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1731213818242"><a name="en-us_topic_0150789026_p1731213818242"></a><a name="en-us_topic_0150789026_p1731213818242"></a>POST /v1.0/{project_id}/kms/update-key-alias</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p794193018265"><a name="en-us_topic_0150789026_p794193018265"></a><a name="en-us_topic_0150789026_p794193018265"></a>Modifies the CMK alias.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p8644195122315"><a name="en-us_topic_0150789026_p8644195122315"></a><a name="en-us_topic_0150789026_p8644195122315"></a>kms:cmk:update</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1964425192316"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p173121338142411"><a name="en-us_topic_0150789026_p173121338142411"></a><a name="en-us_topic_0150789026_p173121338142411"></a>POST /v1.0/{project_id}/kms/update-key-description</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p19941193082615"><a name="en-us_topic_0150789026_p19941193082615"></a><a name="en-us_topic_0150789026_p19941193082615"></a>Modifies the description of a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p56441512239"><a name="en-us_topic_0150789026_p56441512239"></a><a name="en-us_topic_0150789026_p56441512239"></a>kms:cmk:update</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row5644145119236"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1531316387246"><a name="en-us_topic_0150789026_p1531316387246"></a><a name="en-us_topic_0150789026_p1531316387246"></a>POST /v1.0/{project_id}/kms/create-grant</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1194120306265"><a name="en-us_topic_0150789026_p1194120306265"></a><a name="en-us_topic_0150789026_p1194120306265"></a>Creates a grant.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p106441351112313"><a name="en-us_topic_0150789026_p106441351112313"></a><a name="en-us_topic_0150789026_p106441351112313"></a>kms:grant:create</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row16644651122313"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p133135387240"><a name="en-us_topic_0150789026_p133135387240"></a><a name="en-us_topic_0150789026_p133135387240"></a>POST /v1.0/{project_id}/kms/revoke-grant</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p694113010268"><a name="en-us_topic_0150789026_p694113010268"></a><a name="en-us_topic_0150789026_p694113010268"></a>Revokes a grant.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p3644105110238"><a name="en-us_topic_0150789026_p3644105110238"></a><a name="en-us_topic_0150789026_p3644105110238"></a>kms:grant:revoke</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row364415517239"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p7313123815244"><a name="en-us_topic_0150789026_p7313123815244"></a><a name="en-us_topic_0150789026_p7313123815244"></a>POST /v1.0/{project_id}/kms/retire-grant</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1994119304261"><a name="en-us_topic_0150789026_p1994119304261"></a><a name="en-us_topic_0150789026_p1994119304261"></a>Retires a grant.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p1644105115232"><a name="en-us_topic_0150789026_p1644105115232"></a><a name="en-us_topic_0150789026_p1644105115232"></a>kms:grant:retire</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row9644165172313"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1731318388248"><a name="en-us_topic_0150789026_p1731318388248"></a><a name="en-us_topic_0150789026_p1731318388248"></a>POST /v1.0/{project_id}/kms/list-grants</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p494113032610"><a name="en-us_topic_0150789026_p494113032610"></a><a name="en-us_topic_0150789026_p494113032610"></a>Queries the grant list of a CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p9644135182314"><a name="en-us_topic_0150789026_p9644135182314"></a><a name="en-us_topic_0150789026_p9644135182314"></a>kms:grant:list</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1644205118231"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p8313238172418"><a name="en-us_topic_0150789026_p8313238172418"></a><a name="en-us_topic_0150789026_p8313238172418"></a>POST /v1.0/{project_id}/kms/list-retirable-grants</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p79411630152613"><a name="en-us_topic_0150789026_p79411630152613"></a><a name="en-us_topic_0150789026_p79411630152613"></a>Queries the list of grants that can be retired.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p6644051172315"><a name="en-us_topic_0150789026_p6644051172315"></a><a name="en-us_topic_0150789026_p6644051172315"></a>kms:grant:list</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1464419515236"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p6313838142417"><a name="en-us_topic_0150789026_p6313838142417"></a><a name="en-us_topic_0150789026_p6313838142417"></a>POST /v1.0/{project_id}/kms/encrypt-data</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1942530142616"><a name="en-us_topic_0150789026_p1942530142616"></a><a name="en-us_topic_0150789026_p1942530142616"></a>Encrypts data.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p346911919331"><a name="en-us_topic_0150789026_p346911919331"></a><a name="en-us_topic_0150789026_p346911919331"></a>kms:cmk:crypto</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row7644551162319"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p2315138112417"><a name="en-us_topic_0150789026_p2315138112417"></a><a name="en-us_topic_0150789026_p2315138112417"></a>POST /v1.0/{project_id}/kms/decrypt-data</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p794253019262"><a name="en-us_topic_0150789026_p794253019262"></a><a name="en-us_topic_0150789026_p794253019262"></a>Decrypts data.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p7469119113314"><a name="en-us_topic_0150789026_p7469119113314"></a><a name="en-us_topic_0150789026_p7469119113314"></a>kms:cmk:crypto</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row6644451132314"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p103151538112410"><a name="en-us_topic_0150789026_p103151538112410"></a><a name="en-us_topic_0150789026_p103151538112410"></a>POST /v1.0/{project_id}/kms/get-parameters-for-import</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p9942730182610"><a name="en-us_topic_0150789026_p9942730182610"></a><a name="en-us_topic_0150789026_p9942730182610"></a>Obtains parameters for importing a key.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p11644851182317"><a name="en-us_topic_0150789026_p11644851182317"></a><a name="en-us_topic_0150789026_p11644851182317"></a>kms:cmk:getMaterial</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row186451451172318"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p6315143822417"><a name="en-us_topic_0150789026_p6315143822417"></a><a name="en-us_topic_0150789026_p6315143822417"></a>POST /v1.0/{project_id}/kms/import-key-material</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1994218305262"><a name="en-us_topic_0150789026_p1994218305262"></a><a name="en-us_topic_0150789026_p1994218305262"></a>Imports key material.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p1064555116237"><a name="en-us_topic_0150789026_p1064555116237"></a><a name="en-us_topic_0150789026_p1064555116237"></a>kms:cmk:importMaterial</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1364575116232"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p1931516389246"><a name="en-us_topic_0150789026_p1931516389246"></a><a name="en-us_topic_0150789026_p1931516389246"></a>POST /v1.0/{project_id}/kms/delete-imported-key-material</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p1942130192613"><a name="en-us_topic_0150789026_p1942130192613"></a><a name="en-us_topic_0150789026_p1942130192613"></a>Deletes key material.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p15645951192310"><a name="en-us_topic_0150789026_p15645951192310"></a><a name="en-us_topic_0150789026_p15645951192310"></a>kms:cmk:deleteMaterial</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row12645105192319"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p83153387249"><a name="en-us_topic_0150789026_p83153387249"></a><a name="en-us_topic_0150789026_p83153387249"></a>POST /v1.0/{project_id}/kms/enable-key-rotation</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p4942193013266"><a name="en-us_topic_0150789026_p4942193013266"></a><a name="en-us_topic_0150789026_p4942193013266"></a>Enables key rotation.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p2645051172315"><a name="en-us_topic_0150789026_p2645051172315"></a><a name="en-us_topic_0150789026_p2645051172315"></a>kms:cmk:enableRotation</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row6179115364817"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p698930144918"><a name="en-us_topic_0150789026_p698930144918"></a><a name="en-us_topic_0150789026_p698930144918"></a>POST /v1.0/{project_id}/kms/update-key-rotation-interval</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p99911302493"><a name="en-us_topic_0150789026_p99911302493"></a><a name="en-us_topic_0150789026_p99911302493"></a>Modifies the rotation interval.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p79946016497"><a name="en-us_topic_0150789026_p79946016497"></a><a name="en-us_topic_0150789026_p79946016497"></a>kms:cmk:updateRotation</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row96451951182312"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p2031723816245"><a name="en-us_topic_0150789026_p2031723816245"></a><a name="en-us_topic_0150789026_p2031723816245"></a>POST /v1.0/{project_id}/kms/disable-key-rotation</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p20942113092611"><a name="en-us_topic_0150789026_p20942113092611"></a><a name="en-us_topic_0150789026_p20942113092611"></a>Disables key rotation.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p196451651132316"><a name="en-us_topic_0150789026_p196451651132316"></a><a name="en-us_topic_0150789026_p196451651132316"></a>kms:cmk:disableRotation</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row264535119236"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p33173381246"><a name="en-us_topic_0150789026_p33173381246"></a><a name="en-us_topic_0150789026_p33173381246"></a>POST /v1.0/{project_id}/kms/get-key-rotation-status</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p794211304261"><a name="en-us_topic_0150789026_p794211304261"></a><a name="en-us_topic_0150789026_p794211304261"></a>Queries the key rotation status.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p6645115142314"><a name="en-us_topic_0150789026_p6645115142314"></a><a name="en-us_topic_0150789026_p6645115142314"></a>kms:cmk:getRotation</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row364511511234"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p14769152214363"><a name="en-us_topic_0150789026_p14769152214363"></a><a name="en-us_topic_0150789026_p14769152214363"></a>POST /v1.0/{project_id}/kms/resource_instances/action</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p6942530122611"><a name="en-us_topic_0150789026_p6942530122611"></a><a name="en-us_topic_0150789026_p6942530122611"></a>Queries key resource instances.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p5645165132319"><a name="en-us_topic_0150789026_p5645165132319"></a><a name="en-us_topic_0150789026_p5645165132319"></a>kms:cmkTag:listInstance</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row106451751192320"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p13317638122416"><a name="en-us_topic_0150789026_p13317638122416"></a><a name="en-us_topic_0150789026_p13317638122416"></a>GET /v1.0/{project_id}/kms/{key_id}/tags</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p10942133019261"><a name="en-us_topic_0150789026_p10942133019261"></a><a name="en-us_topic_0150789026_p10942133019261"></a>Queries tags of a key.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p36451151112317"><a name="en-us_topic_0150789026_p36451151112317"></a><a name="en-us_topic_0150789026_p36451151112317"></a>kms:cmkTag:list</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row364515513234"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p156452514237"><a name="en-us_topic_0150789026_p156452514237"></a><a name="en-us_topic_0150789026_p156452514237"></a>GET /v1.0/{project_id}/kms/tags</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p36451151152315"><a name="en-us_topic_0150789026_p36451151152315"></a><a name="en-us_topic_0150789026_p36451151152315"></a>Queries the project tags.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p9645165172314"><a name="en-us_topic_0150789026_p9645165172314"></a><a name="en-us_topic_0150789026_p9645165172314"></a>kms:cmkTag:list</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row864565115234"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p11645115172317"><a name="en-us_topic_0150789026_p11645115172317"></a><a name="en-us_topic_0150789026_p11645115172317"></a>POST /v1.0/{project_id}/kms/{key_id}/tags/action</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p156452051152318"><a name="en-us_topic_0150789026_p156452051152318"></a><a name="en-us_topic_0150789026_p156452051152318"></a>Adds or deletes key tags in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p96465517233"><a name="en-us_topic_0150789026_p96465517233"></a><a name="en-us_topic_0150789026_p96465517233"></a>kms:cmkTag:batch</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row1064616512233"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p186462510238"><a name="en-us_topic_0150789026_p186462510238"></a><a name="en-us_topic_0150789026_p186462510238"></a>POST /v1.0/{project_id}/kms/{key_id}/tags</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p5646125182314"><a name="en-us_topic_0150789026_p5646125182314"></a><a name="en-us_topic_0150789026_p5646125182314"></a>Adds tags to a key.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p1764605111234"><a name="en-us_topic_0150789026_p1764605111234"></a><a name="en-us_topic_0150789026_p1764605111234"></a>kms:cmkTag:create</p>
</td>
</tr>
<tr id="en-us_topic_0150789026_row13646651182319"><td class="cellrowborder" valign="top" width="48.40484048404841%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0150789026_p86465517231"><a name="en-us_topic_0150789026_p86465517231"></a><a name="en-us_topic_0150789026_p86465517231"></a>POST /v1.0/{project_id}/kms/{ key_id }/tags/{key}</p>
</td>
<td class="cellrowborder" valign="top" width="25.882588258825884%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0150789026_p17646205119234"><a name="en-us_topic_0150789026_p17646205119234"></a><a name="en-us_topic_0150789026_p17646205119234"></a>Deletes tags of a key.</p>
</td>
<td class="cellrowborder" valign="top" width="25.712571257125717%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0150789026_p2064625119238"><a name="en-us_topic_0150789026_p2064625119238"></a><a name="en-us_topic_0150789026_p2064625119238"></a>kms:cmkTag:delete</p>
</td>
</tr>
</tbody>
</table>

