# Key Operations on SMN<a name="en-us_topic_0100291678"></a>

Simple Message Notification \(SMN\) is a type of web service that a user can easily construct and maintain. SMN sends notifications from a cloud.

With CTS, you can record operations associated with SMN for future query, audit, and backtrack operations.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>In SMN, deleting a topic will delete all subscription information associated with the topic, and the subscription information deletion operation will not be recorded by CTS.  

**Table  1**  SMN operations that can be recorded by CTS

<a name="table2434760155120"></a>
<table><thead align="left"><tr id="r479d6fccec7a4b6aad95fabcd43d9253"><th class="cellrowborder" valign="top" width="32.6%" id="mcps1.2.4.1.1"><p id="accac60d22193461a9b377e83470add75"><a name="accac60d22193461a9b377e83470add75"></a><a name="accac60d22193461a9b377e83470add75"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="25.69%" id="mcps1.2.4.1.2"><p id="ae53fcdb307044569966e494faf6d65b9"><a name="ae53fcdb307044569966e494faf6d65b9"></a><a name="ae53fcdb307044569966e494faf6d65b9"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.71%" id="mcps1.2.4.1.3"><p id="aaa8a9eaef1664f9f94c8c95d2cc0e214"><a name="aaa8a9eaef1664f9f94c8c95d2cc0e214"></a><a name="aaa8a9eaef1664f9f94c8c95d2cc0e214"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="red19cbe647ca41ebb38af3a1613e6edf"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="aaceb91e26c764bff90554c4620077c21"><a name="aaceb91e26c764bff90554c4620077c21"></a><a name="aaceb91e26c764bff90554c4620077c21"></a>Creating a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="aede754f1e7d340c5b20dc3ef6f0d3be9"><a name="aede754f1e7d340c5b20dc3ef6f0d3be9"></a><a name="aede754f1e7d340c5b20dc3ef6f0d3be9"></a>topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a143292b3e5b74c5c91cd2b90fe8709fc"><a name="a143292b3e5b74c5c91cd2b90fe8709fc"></a><a name="a143292b3e5b74c5c91cd2b90fe8709fc"></a>createTopic</p>
</td>
</tr>
<tr id="r3cadf8696fc1412e8dbb1a72011f0082"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="aa1ed86da9ea24a568b35c1bca07f319e"><a name="aa1ed86da9ea24a568b35c1bca07f319e"></a><a name="aa1ed86da9ea24a568b35c1bca07f319e"></a>Deleting a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="ae418e5cde28a4c959bef08e84f5fba2a"><a name="ae418e5cde28a4c959bef08e84f5fba2a"></a><a name="ae418e5cde28a4c959bef08e84f5fba2a"></a>topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a52345eed68694e78b7a9babf420f8a62"><a name="a52345eed68694e78b7a9babf420f8a62"></a><a name="a52345eed68694e78b7a9babf420f8a62"></a>deleteTopic</p>
</td>
</tr>
<tr id="r05940953aafd469fb11aa346824938dd"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="aa7b8fb717734404bb9f10a5ed65d56d4"><a name="aa7b8fb717734404bb9f10a5ed65d56d4"></a><a name="aa7b8fb717734404bb9f10a5ed65d56d4"></a>Updating a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="a1eb690ebb9554c5ab1996fe7170127c7"><a name="a1eb690ebb9554c5ab1996fe7170127c7"></a><a name="a1eb690ebb9554c5ab1996fe7170127c7"></a>topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="aeb2c71bbb8274590826d64ef35575784"><a name="aeb2c71bbb8274590826d64ef35575784"></a><a name="aeb2c71bbb8274590826d64ef35575784"></a>updateTopic</p>
</td>
</tr>
<tr id="r38691cc9a01d4cdb8c9582a3ab3b3626"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="ac54ae46e9e4d4821b5e893c8035a4af4"><a name="ac54ae46e9e4d4821b5e893c8035a4af4"></a><a name="ac54ae46e9e4d4821b5e893c8035a4af4"></a>Updating attributes of a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="a014cb8189f9a4b0bb19d576414a4e5b4"><a name="a014cb8189f9a4b0bb19d576414a4e5b4"></a><a name="a014cb8189f9a4b0bb19d576414a4e5b4"></a>topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a92f46db7b6374698913e20b0540ab47f"><a name="a92f46db7b6374698913e20b0540ab47f"></a><a name="a92f46db7b6374698913e20b0540ab47f"></a>updateTopicAttribute</p>
</td>
</tr>
<tr id="r2dd38302c5264ad49df36d9a9f693273"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="a84aa282d3a474a35a1ae6176b3301214"><a name="a84aa282d3a474a35a1ae6176b3301214"></a><a name="a84aa282d3a474a35a1ae6176b3301214"></a>Deleting all topic attributes</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="ade0391b773254f108260db86712d52ab"><a name="ade0391b773254f108260db86712d52ab"></a><a name="ade0391b773254f108260db86712d52ab"></a>topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a4b438fa4ac6a440ba494fcd19dd3e6da"><a name="a4b438fa4ac6a440ba494fcd19dd3e6da"></a><a name="a4b438fa4ac6a440ba494fcd19dd3e6da"></a>deleteTopicAttributes</p>
</td>
</tr>
<tr id="r291dcceca2c8470796b3cf21c347e006"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="a93d67c69c6114e9dbd03c8108fa2645b"><a name="a93d67c69c6114e9dbd03c8108fa2645b"></a><a name="a93d67c69c6114e9dbd03c8108fa2645b"></a>Deleting a specified topic attribute</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="a6d2d1ace34214401abd0028c5c5b3a39"><a name="a6d2d1ace34214401abd0028c5c5b3a39"></a><a name="a6d2d1ace34214401abd0028c5c5b3a39"></a>topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="afcc80be3965c4f24a5ddfef1e2c4e8ab"><a name="afcc80be3965c4f24a5ddfef1e2c4e8ab"></a><a name="afcc80be3965c4f24a5ddfef1e2c4e8ab"></a>deleteTopicAttributeByName</p>
</td>
</tr>
<tr id="r8563fdbf73e743039e42dc7370951541"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="a269273023b5d4998972e805b26970183"><a name="a269273023b5d4998972e805b26970183"></a><a name="a269273023b5d4998972e805b26970183"></a>Adding a subscription</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="af67b33fec1334f93a6cf43671fcca285"><a name="af67b33fec1334f93a6cf43671fcca285"></a><a name="af67b33fec1334f93a6cf43671fcca285"></a>subscription</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="acd4198bee0e4407e8490275c066c73b6"><a name="acd4198bee0e4407e8490275c066c73b6"></a><a name="acd4198bee0e4407e8490275c066c73b6"></a>subscribe</p>
</td>
</tr>
<tr id="r48d9b9cc8a494c2e86a2ad61ccb7490c"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="a5a23619d5c3e4384a564e2b35a8f6820"><a name="a5a23619d5c3e4384a564e2b35a8f6820"></a><a name="a5a23619d5c3e4384a564e2b35a8f6820"></a>Deleting a subscription</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="ae8459524da884be7a286c06606f35282"><a name="ae8459524da884be7a286c06606f35282"></a><a name="ae8459524da884be7a286c06606f35282"></a>subscription</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a59b389335b7d4488b7e3f992e1e610a7"><a name="a59b389335b7d4488b7e3f992e1e610a7"></a><a name="a59b389335b7d4488b7e3f992e1e610a7"></a>unsubscribe</p>
</td>
</tr>
<tr id="r1288b408e14c42a9b8b0a2c8d641d070"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="acfccfff7312a4cada7e8d2e4cdcbf012"><a name="acfccfff7312a4cada7e8d2e4cdcbf012"></a><a name="acfccfff7312a4cada7e8d2e4cdcbf012"></a>Creating a message template</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="aa1c1348416734f7fabaa3c008584c98b"><a name="aa1c1348416734f7fabaa3c008584c98b"></a><a name="aa1c1348416734f7fabaa3c008584c98b"></a>message_template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a6f2a52b9b0394673b44347bf78250edc"><a name="a6f2a52b9b0394673b44347bf78250edc"></a><a name="a6f2a52b9b0394673b44347bf78250edc"></a>createMessageTemplate</p>
</td>
</tr>
<tr id="re7346640bd2542049cea23d0e987d06f"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="a8844f91c218c4e768453d1a32146e54f"><a name="a8844f91c218c4e768453d1a32146e54f"></a><a name="a8844f91c218c4e768453d1a32146e54f"></a>Creating message templates in batches</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="a5af936c9ecb54777b4395da103eefae8"><a name="a5af936c9ecb54777b4395da103eefae8"></a><a name="a5af936c9ecb54777b4395da103eefae8"></a>message_template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a0729192bd8ed446fab5e155204cc2538"><a name="a0729192bd8ed446fab5e155204cc2538"></a><a name="a0729192bd8ed446fab5e155204cc2538"></a>batchCreateMessageTemplate</p>
</td>
</tr>
<tr id="r8f4a7ce14b784680bacd17ca488dda74"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="aad9aa63964094b30b2bfda954df26315"><a name="aad9aa63964094b30b2bfda954df26315"></a><a name="aad9aa63964094b30b2bfda954df26315"></a>Modifying a message template</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="ab357ae60bd8d4fcea8a63088f955d9ad"><a name="ab357ae60bd8d4fcea8a63088f955d9ad"></a><a name="ab357ae60bd8d4fcea8a63088f955d9ad"></a>message_template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="a187c4bf62cb74aceaa63d4b2c9b55879"><a name="a187c4bf62cb74aceaa63d4b2c9b55879"></a><a name="a187c4bf62cb74aceaa63d4b2c9b55879"></a>updateMessageTemplate</p>
</td>
</tr>
<tr id="rde822e46a7d7456a85c097eafa7fb57e"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p150220155120"><a name="en-us_topic_0100240386_p150220155120"></a><a name="en-us_topic_0100240386_p150220155120"></a>Deleting a message template</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="aa5b8532d981d487d8fe598f643c5a06f"><a name="aa5b8532d981d487d8fe598f643c5a06f"></a><a name="aa5b8532d981d487d8fe598f643c5a06f"></a>message_template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="ab380cba692fa4c86b15b8ad4bffee2f5"><a name="ab380cba692fa4c86b15b8ad4bffee2f5"></a><a name="ab380cba692fa4c86b15b8ad4bffee2f5"></a>deleteMessageTemplate</p>
</td>
</tr>
</tbody>
</table>

