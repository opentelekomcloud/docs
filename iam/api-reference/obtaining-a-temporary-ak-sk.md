# Obtaining a Temporary AK/SK<a name="en-us_topic_0097949518"></a>

## Function Description<a name="s37f73fa9234e41d3aee73c75a47eabba"></a>

You can obtain a temporary AK/SK and security token \(offline AK/SK\) by using a user token, agency token, and federated token. A temporary AK/SK is a token with temporary permissions issued to users. It conforms to the principle of least privilege and can be used to temporarily access OBS.

## URI<a name="s6da80212b87341a6b73b416e9ceede6d"></a>

URI format

POST /v3.0/OS-CREDENTIAL/securitytokens

## Request<a name="s926b2080db4b47cc9d4dbc9ec412dcf1"></a>

-   Request header parameter description
    -   Obtaining a temporary AK/SK with an agency token \(**methods**  is set to  **assume\_role**\)

        <a name="tcca7117b1c2545d986645420ee8f54a5"></a>
        <table><thead align="left"><tr id="r07376d92a1ee46a18f3360824eed2f9b"><th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.1"><p id="af118850a64de44e2b010fed5065e5707"><a name="af118850a64de44e2b010fed5065e5707"></a><a name="af118850a64de44e2b010fed5065e5707"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_1"><a name="a173ae121cc9e48328ca613e72f2a1504_1"></a><a name="a173ae121cc9e48328ca613e72f2a1504_1"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="19.99%" id="mcps1.1.5.1.2"><p id="en-us_topic_0056596910_p253072461917"><a name="en-us_topic_0056596910_p253072461917"></a><a name="en-us_topic_0056596910_p253072461917"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_1"><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="22.49%" id="mcps1.1.5.1.3"><p id="ab2fc6c7c0f5d4d7e903959655b885c0d"><a name="ab2fc6c7c0f5d4d7e903959655b885c0d"></a><a name="ab2fc6c7c0f5d4d7e903959655b885c0d"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="38.629999999999995%" id="mcps1.1.5.1.4"><p id="en-us_topic_0056596910_p953052415195"><a name="en-us_topic_0056596910_p953052415195"></a><a name="en-us_topic_0056596910_p953052415195"></a><strong id="b1734705850163452_1"><a name="b1734705850163452_1"></a><a name="b1734705850163452_1"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="r47bae332297b4362a0f7570641efc4f4"><td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0056596910_p135304248194"><a name="en-us_topic_0056596910_p135304248194"></a><a name="en-us_topic_0056596910_p135304248194"></a>X-Auth-Token</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.1.5.1.2 "><p id="ac9badcbf3d6647519fd12dcbcc01affd"><a name="ac9badcbf3d6647519fd12dcbcc01affd"></a><a name="ac9badcbf3d6647519fd12dcbcc01affd"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.49%" headers="mcps1.1.5.1.3 "><p id="a5aa1683688ea4d948d326ceb30df1c26"><a name="a5aa1683688ea4d948d326ceb30df1c26"></a><a name="a5aa1683688ea4d948d326ceb30df1c26"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.629999999999995%" headers="mcps1.1.5.1.4 "><p id="p17691336175038"><a name="p17691336175038"></a><a name="p17691336175038"></a>Token with permissions of the <strong id="b28891254114313"><a name="b28891254114313"></a><a name="b28891254114313"></a>Agent Operator</strong> policy</p>
        </td>
        </tr>
        <tr id="r156b58bbc6044c8dacb4280d5d476f27"><td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.1 "><p id="a70d12cc0284a4cea9ed5e4d1f8091d84"><a name="a70d12cc0284a4cea9ed5e4d1f8091d84"></a><a name="a70d12cc0284a4cea9ed5e4d1f8091d84"></a>Content-Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.1.5.1.2 "><p id="a44eac6e555cc405c84239ee7423f313e"><a name="a44eac6e555cc405c84239ee7423f313e"></a><a name="a44eac6e555cc405c84239ee7423f313e"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.49%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0056596910_p125301245191"><a name="en-us_topic_0056596910_p125301245191"></a><a name="en-us_topic_0056596910_p125301245191"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.629999999999995%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0056596910_p185305242199"><a name="en-us_topic_0056596910_p185305242199"></a><a name="en-us_topic_0056596910_p185305242199"></a>Fill <strong id="b842352706161331_1"><a name="b842352706161331_1"></a><a name="b842352706161331_1"></a>application/json;charset=utf8</strong> in this field.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   Obtaining a temporary AK/SK with a user token or a federated token \(**methods**  is set to  **token**\)

        <a name="table117431052151715"></a>
        <table><thead align="left"><tr id="row10754152101713"><th class="cellrowborder" valign="top" width="18.891889188918892%" id="mcps1.1.5.1.1"><p id="p137571452151716"><a name="p137571452151716"></a><a name="p137571452151716"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_3"><a name="a173ae121cc9e48328ca613e72f2a1504_3"></a><a name="a173ae121cc9e48328ca613e72f2a1504_3"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="19.831983198319833%" id="mcps1.1.5.1.2"><p id="p8758205241713"><a name="p8758205241713"></a><a name="p8758205241713"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_3"><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="22.492249224922492%" id="mcps1.1.5.1.3"><p id="p4762165281715"><a name="p4762165281715"></a><a name="p4762165281715"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="38.78387838783878%" id="mcps1.1.5.1.4"><p id="p3766175211720"><a name="p3766175211720"></a><a name="p3766175211720"></a><strong id="b1734705850163452_3"><a name="b1734705850163452_3"></a><a name="b1734705850163452_3"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row67691052141713"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="p14770165210171"><a name="p14770165210171"></a><a name="p14770165210171"></a>Content-Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.831983198319833%" headers="mcps1.1.5.1.2 "><p id="p677385216175"><a name="p677385216175"></a><a name="p677385216175"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.492249224922492%" headers="mcps1.1.5.1.3 "><p id="p377610526177"><a name="p377610526177"></a><a name="p377610526177"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.78387838783878%" headers="mcps1.1.5.1.4 "><p id="p378095261710"><a name="p378095261710"></a><a name="p378095261710"></a>Fill <strong id="b842352706161331_3"><a name="b842352706161331_3"></a><a name="b842352706161331_3"></a>application/json;charset=utf8</strong> in this field.</p>
        </td>
        </tr>
        <tr id="row67811152191720"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="p7784195218170"><a name="p7784195218170"></a><a name="p7784195218170"></a>X-Auth-Token</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.831983198319833%" headers="mcps1.1.5.1.2 "><p id="p147851152171713"><a name="p147851152171713"></a><a name="p147851152171713"></a>No</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.492249224922492%" headers="mcps1.1.5.1.3 "><p id="p778845291718"><a name="p778845291718"></a><a name="p778845291718"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.78387838783878%" headers="mcps1.1.5.1.4 "><p id="p117911852141718"><a name="p117911852141718"></a><a name="p117911852141718"></a>User token or federated token required for obtaining a temporary AK/SK. You need to specify either this parameter or the token ID in the request body. This parameter takes the precedence.</p>
        </td>
        </tr>
        </tbody>
        </table>


-   Request body parameter description
    -   Obtaining a temporary AK/SK with an agency token \(**methods**  is set to  **assume\_role**\)

        <a name="t7f269af2050e4926afefd365e178465b"></a>
        <table><thead align="left"><tr id="rfa1f5a414e7649ccabd96455047cd3ec"><th class="cellrowborder" valign="top" width="18.891889188918892%" id="mcps1.1.5.1.1"><p id="a649ea58427784f7c8d86c5602b87104a"><a name="a649ea58427784f7c8d86c5602b87104a"></a><a name="a649ea58427784f7c8d86c5602b87104a"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_5"><a name="a173ae121cc9e48328ca613e72f2a1504_5"></a><a name="a173ae121cc9e48328ca613e72f2a1504_5"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="19.82198219821982%" id="mcps1.1.5.1.2"><p id="a52636b4d38214015a6e48784d5252467"><a name="a52636b4d38214015a6e48784d5252467"></a><a name="a52636b4d38214015a6e48784d5252467"></a><strong id="b842352706161749_1"><a name="b842352706161749_1"></a><a name="b842352706161749_1"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="22.59225922592259%" id="mcps1.1.5.1.3"><p id="afd0e518a88e24a4e96c697a7be19cbc2"><a name="afd0e518a88e24a4e96c697a7be19cbc2"></a><a name="afd0e518a88e24a4e96c697a7be19cbc2"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="38.693869386938694%" id="mcps1.1.5.1.4"><p id="ae12c862e63504aceac73f270bcbb9ef9"><a name="ae12c862e63504aceac73f270bcbb9ef9"></a><a name="ae12c862e63504aceac73f270bcbb9ef9"></a><strong id="b1734705850163452_5"><a name="b1734705850163452_5"></a><a name="b1734705850163452_5"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="r5ba29f30d0294f649c0261f5ee268550"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="ae5fb6c05f11245888a4a7a589ff026a7"><a name="ae5fb6c05f11245888a4a7a589ff026a7"></a><a name="ae5fb6c05f11245888a4a7a589ff026a7"></a>methods</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.82198219821982%" headers="mcps1.1.5.1.2 "><p id="ae26f131fe9d644aa83c2ad45d95fdb09"><a name="ae26f131fe9d644aa83c2ad45d95fdb09"></a><a name="ae26f131fe9d644aa83c2ad45d95fdb09"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.59225922592259%" headers="mcps1.1.5.1.3 "><p id="a58724c182f834f54a8f205ce939f82c9"><a name="a58724c182f834f54a8f205ce939f82c9"></a><a name="a58724c182f834f54a8f205ce939f82c9"></a>String Array</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.693869386938694%" headers="mcps1.1.5.1.4 "><p id="a01ebfabb039940b98c89b3bdd2a6afd6"><a name="a01ebfabb039940b98c89b3bdd2a6afd6"></a><a name="a01ebfabb039940b98c89b3bdd2a6afd6"></a>Fill <strong id="b57935728112411"><a name="b57935728112411"></a><a name="b57935728112411"></a>assume_role</strong> in this field.</p>
        </td>
        </tr>
        <tr id="r0d2ff120207942b89f88af082b9117b0"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="af4d55619f8a2469eaaf399b8834e518f"><a name="af4d55619f8a2469eaaf399b8834e518f"></a><a name="af4d55619f8a2469eaaf399b8834e518f"></a>agency_name</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.82198219821982%" headers="mcps1.1.5.1.2 "><p id="a5793c583ab0141fe972ccbf5facb7194"><a name="a5793c583ab0141fe972ccbf5facb7194"></a><a name="a5793c583ab0141fe972ccbf5facb7194"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.59225922592259%" headers="mcps1.1.5.1.3 "><p id="a3bdb8564f3174d0b993ece861ab5616f"><a name="a3bdb8564f3174d0b993ece861ab5616f"></a><a name="a3bdb8564f3174d0b993ece861ab5616f"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.693869386938694%" headers="mcps1.1.5.1.4 "><p id="a9ecdb84d5c71491b990a05b8ca924957"><a name="a9ecdb84d5c71491b990a05b8ca924957"></a><a name="a9ecdb84d5c71491b990a05b8ca924957"></a>Name of the agency created by a delegating party</p>
        </td>
        </tr>
        <tr id="r0c25bdcbbff040338d36adc023dd9f97"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0056596910_p4770553481"><a name="en-us_topic_0056596910_p4770553481"></a><a name="en-us_topic_0056596910_p4770553481"></a>domain_name or domain_id</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.82198219821982%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0056596910_p97709531782"><a name="en-us_topic_0056596910_p97709531782"></a><a name="en-us_topic_0056596910_p97709531782"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.59225922592259%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0056596910_p07709531487"><a name="en-us_topic_0056596910_p07709531487"></a><a name="en-us_topic_0056596910_p07709531487"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.693869386938694%" headers="mcps1.1.5.1.4 "><p id="p20786433672"><a name="p20786433672"></a><a name="p20786433672"></a><strong id="b1037264594613"><a name="b1037264594613"></a><a name="b1037264594613"></a>domain.name</strong>: Name of the domain to which the delegating party belongs</p>
        </td>
        </tr>
        <tr id="r97b524a758e644548a5bd34a3b932739"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="a3ece2697bd6d4562bed05c8f4e7f1223"><a name="a3ece2697bd6d4562bed05c8f4e7f1223"></a><a name="a3ece2697bd6d4562bed05c8f4e7f1223"></a>duration-seconds</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.82198219821982%" headers="mcps1.1.5.1.2 "><p id="a2d5bebeac9e9467aa26ee50af3fd5add"><a name="a2d5bebeac9e9467aa26ee50af3fd5add"></a><a name="a2d5bebeac9e9467aa26ee50af3fd5add"></a>No</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.59225922592259%" headers="mcps1.1.5.1.3 "><p id="af9d0db00c0434ce6a95dbfe36a10aeca"><a name="af9d0db00c0434ce6a95dbfe36a10aeca"></a><a name="af9d0db00c0434ce6a95dbfe36a10aeca"></a>Int</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.693869386938694%" headers="mcps1.1.5.1.4 "><p id="af31246a849e544a3991f0e364ab07f69"><a name="af31246a849e544a3991f0e364ab07f69"></a><a name="af31246a849e544a3991f0e364ab07f69"></a>Validity period (in seconds) of an AK/SK and security token. The value ranges from 15 minutes to 24 hours. The default value is 15 minutes.</p>
        </td>
        </tr>
        <tr id="rd6399e933eb2454e9a76a7fdfca8ab98"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="a4a5c49065d0a4094bb3c5dbeceee21fa"><a name="a4a5c49065d0a4094bb3c5dbeceee21fa"></a><a name="a4a5c49065d0a4094bb3c5dbeceee21fa"></a>scope</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.82198219821982%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0056596910_p294332614915"><a name="en-us_topic_0056596910_p294332614915"></a><a name="en-us_topic_0056596910_p294332614915"></a>No</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.59225922592259%" headers="mcps1.1.5.1.3 "><p id="a49000ad4482a4b75bc5b3979401126a4"><a name="a49000ad4482a4b75bc5b3979401126a4"></a><a name="a49000ad4482a4b75bc5b3979401126a4"></a>Object</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.693869386938694%" headers="mcps1.1.5.1.4 "><p id="a130c9be5ca064773977f5fb0438d9bbf"><a name="a130c9be5ca064773977f5fb0438d9bbf"></a><a name="a130c9be5ca064773977f5fb0438d9bbf"></a>AK/SK and security token. If this parameter is left blank, the generated security token does not contain the scope information. You are advised to leave this parameter blank. To set the scope of the temporary AK/SK and security token, specify a project or domain.</p>
        <a name="ul32091543195912"></a><a name="ul32091543195912"></a><ul id="ul32091543195912"><li>If this field is set to <strong id="b183251123124810"><a name="b183251123124810"></a><a name="b183251123124810"></a>project</strong>, the temporary AK/SK and security token can only be used to access resources in the project of a specified ID or name.<pre class="screen" id="screen842664845912"><a name="screen842664845912"></a><a name="screen842664845912"></a>"scope": {
              "project": {
              "id": "0b95b78b67fa045b38104c12fb..."
              }
            }</pre>
        </li><li>If this field is set to <strong id="b6738191914913"><a name="b6738191914913"></a><a name="b6738191914913"></a>domain</strong>, the temporary AK/SK and security token can be used to access all resources under the domain of a specified ID or name.<pre class="screen" id="screen59171740125811"><a name="screen59171740125811"></a><a name="screen59171740125811"></a>"scope": {
              "domain": {
              "name": " domain A"
              }
            }</pre>
        </li></ul>
        </td>
        </tr>
        </tbody>
        </table>

    -   Obtaining a temporary AK/SK with a user token or a federated token \(**methods**  is set to  **token**\)

        <a name="t0cc84c02310f4e9ead62efd457aee291"></a>
        <table><thead align="left"><tr id="r3dedc45671b342c18a7f17a5959c2c6d"><th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.1"><p id="a32881b797ceb4fd7bd9d1e95689a4b18"><a name="a32881b797ceb4fd7bd9d1e95689a4b18"></a><a name="a32881b797ceb4fd7bd9d1e95689a4b18"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_7"><a name="a173ae121cc9e48328ca613e72f2a1504_7"></a><a name="a173ae121cc9e48328ca613e72f2a1504_7"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="19.99%" id="mcps1.1.5.1.2"><p id="ab36ba8846cb94d62b7f5d8b60b38ea6e"><a name="ab36ba8846cb94d62b7f5d8b60b38ea6e"></a><a name="ab36ba8846cb94d62b7f5d8b60b38ea6e"></a><strong id="b842352706161749_3"><a name="b842352706161749_3"></a><a name="b842352706161749_3"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="22.43%" id="mcps1.1.5.1.3"><p id="en-us_topic_0056596910_p317413396472"><a name="en-us_topic_0056596910_p317413396472"></a><a name="en-us_topic_0056596910_p317413396472"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="38.690000000000005%" id="mcps1.1.5.1.4"><p id="a47c280f6407e4eb9aa2aea4f0a17fe5f"><a name="a47c280f6407e4eb9aa2aea4f0a17fe5f"></a><a name="a47c280f6407e4eb9aa2aea4f0a17fe5f"></a><strong id="b1734705850163452_7"><a name="b1734705850163452_7"></a><a name="b1734705850163452_7"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="r954d63fb5ea74e1ab584dcaf2647bbb6"><td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.1 "><p id="a48ec5a0484d541f8bea4918148ba5196"><a name="a48ec5a0484d541f8bea4918148ba5196"></a><a name="a48ec5a0484d541f8bea4918148ba5196"></a>methods</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.1.5.1.2 "><p id="a44e8a16c13df423fbc01aa468913ccb3"><a name="a44e8a16c13df423fbc01aa468913ccb3"></a><a name="a44e8a16c13df423fbc01aa468913ccb3"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.1.5.1.3 "><p id="a9555d192db1640e9bef878d59d74fbfe"><a name="a9555d192db1640e9bef878d59d74fbfe"></a><a name="a9555d192db1640e9bef878d59d74fbfe"></a>String Array</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0056596910_p21894397479"><a name="en-us_topic_0056596910_p21894397479"></a><a name="en-us_topic_0056596910_p21894397479"></a>Fill <strong id="a31662b8438c74691a674fd0082d0bd07"><a name="a31662b8438c74691a674fd0082d0bd07"></a><a name="a31662b8438c74691a674fd0082d0bd07"></a>token</strong> in this field.</p>
        </td>
        </tr>
        <tr id="r0f9953c7a6d3424aa0970d2040e217e4"><td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.1 "><p id="acaa2e64ab6fc49e68a46298439d441f9"><a name="acaa2e64ab6fc49e68a46298439d441f9"></a><a name="acaa2e64ab6fc49e68a46298439d441f9"></a>token</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.1.5.1.2 "><p id="a71cb30778b8942ee9047b5f39d87ee65"><a name="a71cb30778b8942ee9047b5f39d87ee65"></a><a name="a71cb30778b8942ee9047b5f39d87ee65"></a>No</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.1.5.1.3 "><p id="aa8d2a2f59cdd48fba1e9314e917c8ac3"><a name="aa8d2a2f59cdd48fba1e9314e917c8ac3"></a><a name="aa8d2a2f59cdd48fba1e9314e917c8ac3"></a>JSON object</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.1.5.1.4 "><p id="ac870e4fca7234a2f94746dffa8f632b3"><a name="ac870e4fca7234a2f94746dffa8f632b3"></a><a name="ac870e4fca7234a2f94746dffa8f632b3"></a>Common token or federated token required for obtaining a temporary AK/SK. You need to choose either the ID in this object or <strong id="b842352706135731"><a name="b842352706135731"></a><a name="b842352706135731"></a>X-Auth-Token</strong> in the request header. <strong id="b842352706172831_3"><a name="b842352706172831_3"></a><a name="b842352706172831_3"></a>X-Auth-Token</strong> takes priority over the ID in this object.</p>
        </td>
        </tr>
        <tr id="rb4e32f4fe494428f9ed9f658c259150f"><td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0056596910_p520553910477"><a name="en-us_topic_0056596910_p520553910477"></a><a name="en-us_topic_0056596910_p520553910477"></a>duration-seconds</p>
        </td>
        <td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0056596910_p720573919472"><a name="en-us_topic_0056596910_p720573919472"></a><a name="en-us_topic_0056596910_p720573919472"></a>No</p>
        </td>
        <td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.1.5.1.3 "><p id="abbf4b1dc17a44f2b8babcc21c7a179d3"><a name="abbf4b1dc17a44f2b8babcc21c7a179d3"></a><a name="abbf4b1dc17a44f2b8babcc21c7a179d3"></a>Int</p>
        </td>
        <td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.1.5.1.4 "><p id="aa2081311b8ac4113873c6dec1088c6ad"><a name="aa2081311b8ac4113873c6dec1088c6ad"></a><a name="aa2081311b8ac4113873c6dec1088c6ad"></a>Validity period (in seconds) of an AK/SK and security token. The value ranges from 15 minutes to 24 hours. The default value is 15 minutes.</p>
        </td>
        </tr>
        </tbody>
        </table>



-   Sample request
    -   When the  **methods**  parameter is set to  **assume\_role**

        ```
        {
            "auth": {
                "identity": {
                    "methods": [
                        "assume_role"
                    ],
                    "assume_role": {
                        "domain_id": "411edb4b634144f587ffc88f9bbdxxx",
                        "xrole_name": "testagency",
                        "duration-seconds": "3600"
                    }
                }
            }
        }
        
        ```

    -   When the  **methods**  parameter is set to  **token**

        ```
        {
            "auth": {
                "identity": {
                    "methods": [
                        "token"
                    ],
                    "token": {
                        "id": "MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...",
                        "duration-seconds": "900"
                    }
                }
            }
        }
        ```



## **Response**<a name="s987a5f64dbf0425e90492e131d91dd6f"></a>

-   Response body parameter description

    <a name="t71075bd9372146418f36f309206d546d"></a>
    <table><thead align="left"><tr id="rf7ba2ad3ea734fb189aae9eb6784fd91"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="ad370c33f356448bcb31af8e0a47fa4a7"><a name="ad370c33f356448bcb31af8e0a47fa4a7"></a><a name="ad370c33f356448bcb31af8e0a47fa4a7"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_9"><a name="a173ae121cc9e48328ca613e72f2a1504_9"></a><a name="a173ae121cc9e48328ca613e72f2a1504_9"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="a6b1db5c43430453cb2cfcfc6d048dfed"><a name="a6b1db5c43430453cb2cfcfc6d048dfed"></a><a name="a6b1db5c43430453cb2cfcfc6d048dfed"></a><strong id="b842352706161749_5"><a name="b842352706161749_5"></a><a name="b842352706161749_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="a7ad7e600531b40b3a8555205463593d3"><a name="a7ad7e600531b40b3a8555205463593d3"></a><a name="a7ad7e600531b40b3a8555205463593d3"></a><strong id="b842352706143526_9"><a name="b842352706143526_9"></a><a name="b842352706143526_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="ade5bee541a32463fa7012f60fcb3f63d"><a name="ade5bee541a32463fa7012f60fcb3f63d"></a><a name="ade5bee541a32463fa7012f60fcb3f63d"></a><strong id="b1734705850163452_9"><a name="b1734705850163452_9"></a><a name="b1734705850163452_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rf579990aecad486eac8bb7dfe74d6b74"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="a278f9d3ee45e4fb8a3cc5936ff19051c"><a name="a278f9d3ee45e4fb8a3cc5936ff19051c"></a><a name="a278f9d3ee45e4fb8a3cc5936ff19051c"></a>credential</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="aca41c717ac524f31a56378a2c8c4f51f"><a name="aca41c717ac524f31a56378a2c8c4f51f"></a><a name="aca41c717ac524f31a56378a2c8c4f51f"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="ac04d3c547d714a10b2f62d91aa41f664"><a name="ac04d3c547d714a10b2f62d91aa41f664"></a><a name="ac04d3c547d714a10b2f62d91aa41f664"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="a6411ff72d5ba4ea8ab677dc86ec0cced"><a name="a6411ff72d5ba4ea8ab677dc86ec0cced"></a><a name="a6411ff72d5ba4ea8ab677dc86ec0cced"></a>Authentication information.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description about the credential content.

    <a name="t157a41ad55344766b92133f6d3f67e5a"></a>
    <table><thead align="left"><tr id="r9d3a37aba7ce462182a7cd0239930a7a"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="en-us_topic_0056596910_p320143315838"><a name="en-us_topic_0056596910_p320143315838"></a><a name="en-us_topic_0056596910_p320143315838"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_11"><a name="a173ae121cc9e48328ca613e72f2a1504_11"></a><a name="a173ae121cc9e48328ca613e72f2a1504_11"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="ac1c056f03f83468cb805ca9df721dbe0"><a name="ac1c056f03f83468cb805ca9df721dbe0"></a><a name="ac1c056f03f83468cb805ca9df721dbe0"></a><strong id="b842352706161749_7"><a name="b842352706161749_7"></a><a name="b842352706161749_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0056596910_p83862915838"><a name="en-us_topic_0056596910_p83862915838"></a><a name="en-us_topic_0056596910_p83862915838"></a><strong id="b842352706143526_11"><a name="b842352706143526_11"></a><a name="b842352706143526_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="af0bf232ddbc7479499019d16557db9a0"><a name="af0bf232ddbc7479499019d16557db9a0"></a><a name="af0bf232ddbc7479499019d16557db9a0"></a><strong id="b1734705850163452_11"><a name="b1734705850163452_11"></a><a name="b1734705850163452_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rc7cc77854d024936aac9b583cfda4fe5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="a224f3f82590742e88e3374ce148016c1"><a name="a224f3f82590742e88e3374ce148016c1"></a><a name="a224f3f82590742e88e3374ce148016c1"></a>expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0056596910_p980353615838"><a name="en-us_topic_0056596910_p980353615838"></a><a name="en-us_topic_0056596910_p980353615838"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="af45ccde870e945cf85ab9f0d752a2280"><a name="af45ccde870e945cf85ab9f0d752a2280"></a><a name="af45ccde870e945cf85ab9f0d752a2280"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="ae308362385a643649affe75a07309253"><a name="ae308362385a643649affe75a07309253"></a><a name="ae308362385a643649affe75a07309253"></a>Expiration time.</p>
    </td>
    </tr>
    <tr id="r64d452b576404dafa65dacd8447b5aaa"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="ac3da1b0f861f418487ebd046cdb66b88"><a name="ac3da1b0f861f418487ebd046cdb66b88"></a><a name="ac3da1b0f861f418487ebd046cdb66b88"></a>access</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="a5f47e16e7ea041e89d0d104441960b63"><a name="a5f47e16e7ea041e89d0d104441960b63"></a><a name="a5f47e16e7ea041e89d0d104441960b63"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="a0bddf8bfa6144272b1e177b5309b0a52"><a name="a0bddf8bfa6144272b1e177b5309b0a52"></a><a name="a0bddf8bfa6144272b1e177b5309b0a52"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="aa5f31f411bf14cbd95be31d808218af1"><a name="aa5f31f411bf14cbd95be31d808218af1"></a><a name="aa5f31f411bf14cbd95be31d808218af1"></a>AK</p>
    </td>
    </tr>
    <tr id="r5e51a148bd4e408ca0685564b5cab2e0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="a0e433ade2cf44aff83d3c39384ba7099"><a name="a0e433ade2cf44aff83d3c39384ba7099"></a><a name="a0e433ade2cf44aff83d3c39384ba7099"></a>secret</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="acfbaff0b9ac74f40966e3cea0ed2a6d9"><a name="acfbaff0b9ac74f40966e3cea0ed2a6d9"></a><a name="acfbaff0b9ac74f40966e3cea0ed2a6d9"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="a9b62f5a5264a45daa918b775d6a41364"><a name="a9b62f5a5264a45daa918b775d6a41364"></a><a name="a9b62f5a5264a45daa918b775d6a41364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="a3b6f57d267a247389755c61ec5eab3f7"><a name="a3b6f57d267a247389755c61ec5eab3f7"></a><a name="a3b6f57d267a247389755c61ec5eab3f7"></a>SK</p>
    </td>
    </tr>
    <tr id="r0e1615b25cf94e3f9d31da428fd6f183"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="a03203c3fd4aa4562be555db0211fb280"><a name="a03203c3fd4aa4562be555db0211fb280"></a><a name="a03203c3fd4aa4562be555db0211fb280"></a>securitytoken</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="a4677aaac4a2d4eaa811fd7fc4af15f4c"><a name="a4677aaac4a2d4eaa811fd7fc4af15f4c"></a><a name="a4677aaac4a2d4eaa811fd7fc4af15f4c"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="a0aba3b9c8a554f9785fbd81db65c487e"><a name="a0aba3b9c8a554f9785fbd81db65c487e"></a><a name="a0aba3b9c8a554f9785fbd81db65c487e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0056596910_p299581715838"><a name="en-us_topic_0056596910_p299581715838"></a><a name="en-us_topic_0056596910_p299581715838"></a>Used for subsequent replacement of an SK or token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
      "credential": {
        "access": "NQC51NFINJS1JXX...",
        "secret": "EY74MByPZ46kTRJL9ay5DskqXX...",
        "expires_at": "2017-04-17T07:55:18.575000Z",
        "securitytoken": "gAAAAABY9GbWUaGtoa9DPj7_dE4qUSnAXXX..."
      }
    }
    ```


## **Status Codes**<a name="sf1bd0a17f1264315a1a57eb5a7071c36"></a>

<a name="t91b628302cf7421e82389201ba4efef3"></a>
<table><thead align="left"><tr id="re0457507a24943248c88a719663a909f"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a15db1e723300498ba8617cc58814d6d6"><a name="a15db1e723300498ba8617cc58814d6d6"></a><a name="a15db1e723300498ba8617cc58814d6d6"></a><strong id="b842352706183230_3"><a name="b842352706183230_3"></a><a name="b842352706183230_3"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a1a5e5610b8214de590cdd018dabefd62"><a name="a1a5e5610b8214de590cdd018dabefd62"></a><a name="a1a5e5610b8214de590cdd018dabefd62"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra1cb949214b145a785a6104d2b7c031c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae777b0ccd79c4a7abd06adbe666cf58d"><a name="ae777b0ccd79c4a7abd06adbe666cf58d"></a><a name="ae777b0ccd79c4a7abd06adbe666cf58d"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a2bcab7f854f649bc8340f67c6af52f11"><a name="a2bcab7f854f649bc8340f67c6af52f11"></a><a name="a2bcab7f854f649bc8340f67c6af52f11"></a>The request is successful.</p>
</td>
</tr>
<tr id="r27baf852d3024d6083962a8e171779d7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a87b2b54aeca74bf0a937231e459e9f82"><a name="a87b2b54aeca74bf0a937231e459e9f82"></a><a name="a87b2b54aeca74bf0a937231e459e9f82"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a096326a738fe46e7ab08a31fcafc07bc"><a name="a096326a738fe46e7ab08a31fcafc07bc"></a><a name="a096326a738fe46e7ab08a31fcafc07bc"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="r39eef0d38db74d6bbdc97157ff431207"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7d1f83e848ef4251a12c7dea6015c977"><a name="a7d1f83e848ef4251a12c7dea6015c977"></a><a name="a7d1f83e848ef4251a12c7dea6015c977"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac0ff9b21c5e64620b8a4c45cd6f028fb"><a name="ac0ff9b21c5e64620b8a4c45cd6f028fb"></a><a name="ac0ff9b21c5e64620b8a4c45cd6f028fb"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="r56e109619204490a8ac60a2823d869a3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae2eefb749ba14306b62424ca672248dd"><a name="ae2eefb749ba14306b62424ca672248dd"></a><a name="ae2eefb749ba14306b62424ca672248dd"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a605e2f64e1da4fc1a570f243a8629758"><a name="a605e2f64e1da4fc1a570f243a8629758"></a><a name="a605e2f64e1da4fc1a570f243a8629758"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="reb0e6b35be084cfc8ca80c6ff3187ae4"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a337aa80f74e34e5f80bd7dfb27912528"><a name="a337aa80f74e34e5f80bd7dfb27912528"></a><a name="a337aa80f74e34e5f80bd7dfb27912528"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae2f7f519962748728723158751d8697f"><a name="ae2f7f519962748728723158751d8697f"></a><a name="ae2f7f519962748728723158751d8697f"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

