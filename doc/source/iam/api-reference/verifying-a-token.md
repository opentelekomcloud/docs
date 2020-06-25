# Verifying a Token<a name="en-us_topic_0057845585"></a>

## Function Description<a name="s2f7665a32abf4492987e6dd3617bcb21"></a>

This interface is used to check the validity of a specified token. If the token is valid, detailed information about the token will be returned.

## URI<a name="s1c0fd353ed38459c8baeab25cc3c62d2"></a>

URI format

GET /v3/auth/tokens

## Request<a name="s27bb6347561e424096c86cfc3d036e9e"></a>

-   Request header parameter description

    <a name="t14a8c0fedd2149129bd965b2a4d51c90"></a>
    <table><thead align="left"><tr id="rc0444c4b152b43768b629e845d90495e"><th class="cellrowborder" valign="top" width="19.038096190380962%" id="mcps1.1.5.1.1"><p id="a293da93d33fc404ea05b069800a7eb13"><a name="a293da93d33fc404ea05b069800a7eb13"></a><a name="a293da93d33fc404ea05b069800a7eb13"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.578242175782425%" id="mcps1.1.5.1.2"><p id="ac06ad3b3b5174f3ebd57a1661506970a"><a name="ac06ad3b3b5174f3ebd57a1661506970a"></a><a name="ac06ad3b3b5174f3ebd57a1661506970a"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.75832416758324%" id="mcps1.1.5.1.3"><p id="a924a03bda76a46648797189b78bdd715"><a name="a924a03bda76a46648797189b78bdd715"></a><a name="a924a03bda76a46648797189b78bdd715"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.62533746625338%" id="mcps1.1.5.1.4"><p id="ab17a839c16b94f1e83ff3a3f8ef3b308"><a name="ab17a839c16b94f1e83ff3a3f8ef3b308"></a><a name="ab17a839c16b94f1e83ff3a3f8ef3b308"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r6f5a057d2e2a48b6b1a71318684ba8b5"><td class="cellrowborder" valign="top" width="19.038096190380962%" headers="mcps1.1.5.1.1 "><p id="a927ddf565a2f45c0840a6e4ef3eab536"><a name="a927ddf565a2f45c0840a6e4ef3eab536"></a><a name="a927ddf565a2f45c0840a6e4ef3eab536"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.578242175782425%" headers="mcps1.1.5.1.2 "><p id="a4edeb0b0c00144319701c1460d210ea8"><a name="a4edeb0b0c00144319701c1460d210ea8"></a><a name="a4edeb0b0c00144319701c1460d210ea8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.75832416758324%" headers="mcps1.1.5.1.3 "><p id="a17c7fa87e9a54833a6064feb297b5e55"><a name="a17c7fa87e9a54833a6064feb297b5e55"></a><a name="a17c7fa87e9a54833a6064feb297b5e55"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.62533746625338%" headers="mcps1.1.5.1.4 "><a name="ul1963814299291"></a><a name="ul1963814299291"></a><ul id="ul1963814299291"><li>To verify your own token, specify your token. There are no special requirements on the permissions that your token must have.</li><li>To verify the token of another user under the same domain, use a token that has permissions of the <strong id="b2069775420254"><a name="b2069775420254"></a><a name="b2069775420254"></a>Security Administrator</strong> policy.</li></ul>
    </td>
    </tr>
    <tr id="r4ebaddfb83fe4bffa462094cc2834cf2"><td class="cellrowborder" valign="top" width="19.038096190380962%" headers="mcps1.1.5.1.1 "><p id="ae9df07c230354205b9c3cb76f08eadb4"><a name="ae9df07c230354205b9c3cb76f08eadb4"></a><a name="ae9df07c230354205b9c3cb76f08eadb4"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.578242175782425%" headers="mcps1.1.5.1.2 "><p id="a1100e03a09864240abecdff29c388bf8"><a name="a1100e03a09864240abecdff29c388bf8"></a><a name="a1100e03a09864240abecdff29c388bf8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.75832416758324%" headers="mcps1.1.5.1.3 "><p id="a667fee7780224b0d9e78b40c59beaccf"><a name="a667fee7780224b0d9e78b40c59beaccf"></a><a name="a667fee7780224b0d9e78b40c59beaccf"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.62533746625338%" headers="mcps1.1.5.1.4 "><p id="p956292518331"><a name="p956292518331"></a><a name="p956292518331"></a>Token to be verified</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Query parameter description

    <a name="tb63966ba606d4ce4b360f40a653abff8"></a>
    <table><thead align="left"><tr id="re1669fb2a3c9480bb3a00c0dd34cfc26"><th class="cellrowborder" valign="top" width="18.891889188918892%" id="mcps1.1.5.1.1"><p id="ad1f8f00641de4d56931fab6c023ee27c"><a name="ad1f8f00641de4d56931fab6c023ee27c"></a><a name="ad1f8f00641de4d56931fab6c023ee27c"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.64176417641764%" id="mcps1.1.5.1.2"><p id="a7a0e922d4ac64a23a8ee0149912e026c"><a name="a7a0e922d4ac64a23a8ee0149912e026c"></a><a name="a7a0e922d4ac64a23a8ee0149912e026c"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.581758175817583%" id="mcps1.1.5.1.3"><p id="a3fca62cae08b4adcaba323f7f3ad866e"><a name="a3fca62cae08b4adcaba323f7f3ad866e"></a><a name="a3fca62cae08b4adcaba323f7f3ad866e"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.88458845884588%" id="mcps1.1.5.1.4"><p id="a0cfd690722644009b8bc0cb94a5a9327"><a name="a0cfd690722644009b8bc0cb94a5a9327"></a><a name="a0cfd690722644009b8bc0cb94a5a9327"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd8377b31aedb40a6ac2c78ec645295bb"><td class="cellrowborder" valign="top" width="18.891889188918892%" headers="mcps1.1.5.1.1 "><p id="ab3f196e612a04b36898fca5391c8c71c"><a name="ab3f196e612a04b36898fca5391c8c71c"></a><a name="ab3f196e612a04b36898fca5391c8c71c"></a>nocatalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.2 "><p id="ab701027c99914d0aa8bb847a8df6dd5e"><a name="ab701027c99914d0aa8bb847a8df6dd5e"></a><a name="ab701027c99914d0aa8bb847a8df6dd5e"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.581758175817583%" headers="mcps1.1.5.1.3 "><p id="a5fee45d14b11467e90c3ae4231a1c771"><a name="a5fee45d14b11467e90c3ae4231a1c771"></a><a name="a5fee45d14b11467e90c3ae4231a1c771"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.88458845884588%" headers="mcps1.1.5.1.4 "><p id="a2c20ed7477cd4f059a3ea425cc7371d0"><a name="a2c20ed7477cd4f059a3ea425cc7371d0"></a><a name="a2c20ed7477cd4f059a3ea425cc7371d0"></a>If this parameter is set, no catalog information will be displayed in the response.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H "X-Subject-Token:$token" -X GET https://sample.domain.com/v3/auth/tokens
    ```


## Response<a name="sef91e8b0ca524132ac01532b7965e1e2"></a>

-   Response header parameter description

    <a name="table44659654142645"></a>
    <table><thead align="left"><tr id="row41981888142645"><th class="cellrowborder" valign="top" width="19.2019201920192%" id="mcps1.1.5.1.1"><p id="p45089776142645"><a name="p45089776142645"></a><a name="p45089776142645"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.2"><p id="p28393220142645"><a name="p28393220142645"></a><a name="p28393220142645"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.791779177917793%" id="mcps1.1.5.1.3"><p id="p18149477142645"><a name="p18149477142645"></a><a name="p18149477142645"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.83458345834583%" id="mcps1.1.5.1.4"><p id="p60821498142645"><a name="p60821498142645"></a><a name="p60821498142645"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3444779142645"><td class="cellrowborder" valign="top" width="19.2019201920192%" headers="mcps1.1.5.1.1 "><p id="p10591684142645"><a name="p10591684142645"></a><a name="p10591684142645"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.2 "><p id="p52620110142645"><a name="p52620110142645"></a><a name="p52620110142645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.791779177917793%" headers="mcps1.1.5.1.3 "><p id="p34370545142645"><a name="p34370545142645"></a><a name="p34370545142645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.1.5.1.4 "><p id="p669852604310"><a name="p669852604310"></a><a name="p669852604310"></a>Verified token</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response body parameter description

    <a name="t6d4ee42e5c8f4f45a85c17438155d3b2"></a>
    <table><thead align="left"><tr id="r4dd86b94125f407290b7fbf04ebe575c"><th class="cellrowborder" valign="top" width="19.46%" id="mcps1.1.5.1.1"><p id="a75d1f5112a70466ea4a5fe938cdf3cc8"><a name="a75d1f5112a70466ea4a5fe938cdf3cc8"></a><a name="a75d1f5112a70466ea4a5fe938cdf3cc8"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.29%" id="mcps1.1.5.1.2"><p id="p1558020561015"><a name="p1558020561015"></a><a name="p1558020561015"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.1.5.1.3"><p id="a7f33afb2227d4868b46829a830191f0c"><a name="a7f33afb2227d4868b46829a830191f0c"></a><a name="a7f33afb2227d4868b46829a830191f0c"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.7%" id="mcps1.1.5.1.4"><p id="aebca98d4b7494a6982128fb9f0efd2e1"><a name="aebca98d4b7494a6982128fb9f0efd2e1"></a><a name="aebca98d4b7494a6982128fb9f0efd2e1"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1e0a4bf8450b490197d5e660b327b925"><td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.1.5.1.1 "><p id="a9765f37463df4bc79062f17565117cd7"><a name="a9765f37463df4bc79062f17565117cd7"></a><a name="a9765f37463df4bc79062f17565117cd7"></a>token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.2 "><p id="p175801156906"><a name="p175801156906"></a><a name="p175801156906"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.1.5.1.3 "><p id="ac3168808fa994c8a848af4ec4c54d5a6"><a name="ac3168808fa994c8a848af4ec4c54d5a6"></a><a name="ac3168808fa994c8a848af4ec4c54d5a6"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.7%" headers="mcps1.1.5.1.4 "><p id="aaaa91a281c0245f1bdfbd2263749ab43"><a name="aaaa91a281c0245f1bdfbd2263749ab43"></a><a name="aaaa91a281c0245f1bdfbd2263749ab43"></a>Token information list.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Token format description

    <a name="tffc982d330f64c9ca0256e3a5e4ff5e7"></a>
    <table><thead align="left"><tr id="r5697a7ee0b854dde9ecbfdd51d69ef0c"><th class="cellrowborder" valign="top" width="19.21%" id="mcps1.1.5.1.1"><p id="aa3e27da3347d4f8facd0ce9d0e632ab9"><a name="aa3e27da3347d4f8facd0ce9d0e632ab9"></a><a name="aa3e27da3347d4f8facd0ce9d0e632ab9"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52%" id="mcps1.1.5.1.2"><p id="aead6892df91b4ede8f01e2eeb9df755a"><a name="aead6892df91b4ede8f01e2eeb9df755a"></a><a name="aead6892df91b4ede8f01e2eeb9df755a"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.5.1.3"><p id="a0bf1309201174445b94b761f3bdaffaf"><a name="a0bf1309201174445b94b761f3bdaffaf"></a><a name="a0bf1309201174445b94b761f3bdaffaf"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.410000000000004%" id="mcps1.1.5.1.4"><p id="add9e6449174841be9ef13474f307936e"><a name="add9e6449174841be9ef13474f307936e"></a><a name="add9e6449174841be9ef13474f307936e"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdb8b4121e4744630bf355a40cd5ebf95"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="a48286c452efa4c288e2a15a31254e63b"><a name="a48286c452efa4c288e2a15a31254e63b"></a><a name="a48286c452efa4c288e2a15a31254e63b"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="a7285bdf185e84758a9a0ecfa2ea64151"><a name="a7285bdf185e84758a9a0ecfa2ea64151"></a><a name="a7285bdf185e84758a9a0ecfa2ea64151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a7f8b4e429f8c4fab8ac7174ae0791872"><a name="a7f8b4e429f8c4fab8ac7174ae0791872"></a><a name="a7f8b4e429f8c4fab8ac7174ae0791872"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="a4e4d91d08dab407fa7c7afae3b845216"><a name="a4e4d91d08dab407fa7c7afae3b845216"></a><a name="a4e4d91d08dab407fa7c7afae3b845216"></a>Method of obtaining the token, for example, <strong id="b35616331285"><a name="b35616331285"></a><a name="b35616331285"></a>password</strong>.</p>
    </td>
    </tr>
    <tr id="r2400a775e1b5496ca08cc5db1ffb1c49"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="ac2344fb8014b4dc0ad27b9f34cb41ffb"><a name="ac2344fb8014b4dc0ad27b9f34cb41ffb"></a><a name="ac2344fb8014b4dc0ad27b9f34cb41ffb"></a>expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="a2071411444684e1295c813a9e8212725"><a name="a2071411444684e1295c813a9e8212725"></a><a name="a2071411444684e1295c813a9e8212725"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a9327addec5014201af1c7c660651ea56"><a name="a9327addec5014201af1c7c660651ea56"></a><a name="a9327addec5014201af1c7c660651ea56"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="a6c7c4e6c2940430abd01290f42a71992"><a name="a6c7c4e6c2940430abd01290f42a71992"></a><a name="a6c7c4e6c2940430abd01290f42a71992"></a>Expiration date of the token</p>
    </td>
    </tr>
    <tr id="r832448ca9e6b4a8fbd31107844e367f2"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="a9cf8f6059e1640e698466d21b30a650e"><a name="a9cf8f6059e1640e698466d21b30a650e"></a><a name="a9cf8f6059e1640e698466d21b30a650e"></a>issued_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="a65e402777c14464e9fd409f9febe5449"><a name="a65e402777c14464e9fd409f9febe5449"></a><a name="a65e402777c14464e9fd409f9febe5449"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="ae1066225c9364795a0d584e27e47625c"><a name="ae1066225c9364795a0d584e27e47625c"></a><a name="ae1066225c9364795a0d584e27e47625c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0031136109_p532161155713"><a name="en-us_topic_0031136109_p532161155713"></a><a name="en-us_topic_0031136109_p532161155713"></a>Time when the token was issued</p>
    </td>
    </tr>
    <tr id="re3fd3f96adb04f4f8a61fa9416666cf6"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="a1e60825270834834bffc89c1a5b12302"><a name="a1e60825270834834bffc89c1a5b12302"></a><a name="a1e60825270834834bffc89c1a5b12302"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="a1fa84a4af2694a9aba3535e6b5d1a4bd"><a name="a1fa84a4af2694a9aba3535e6b5d1a4bd"></a><a name="a1fa84a4af2694a9aba3535e6b5d1a4bd"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a24ae3bfbf525477ab52df4dda58371b3"><a name="a24ae3bfbf525477ab52df4dda58371b3"></a><a name="a24ae3bfbf525477ab52df4dda58371b3"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="aa091f76473d84b0990d9ebe12bdb8d58"><a name="aa091f76473d84b0990d9ebe12bdb8d58"></a><a name="aa091f76473d84b0990d9ebe12bdb8d58"></a>Example:</p>
    <pre class="screen" id="s5f7a0bf572bb482c992d7938df2ad417"><a name="s5f7a0bf572bb482c992d7938df2ad417"></a><a name="s5f7a0bf572bb482c992d7938df2ad417"></a>"user": { 
          "name": "<em id="a7637d31b94164601bffca012a08f28f3"><a name="a7637d31b94164601bffca012a08f28f3"></a><a name="a7637d31b94164601bffca012a08f28f3"></a>username</em>", 
          "id": "<em id="en-us_topic_0031136109_i433336816519"><a name="en-us_topic_0031136109_i433336816519"></a><a name="en-us_topic_0031136109_i433336816519"></a>userid</em>", 
          "password_expires_at":"2016-11-06T15:32:17.000000",
          "domain": { 
             "name": "<em id="en-us_topic_0031136109_i438354691645"><a name="en-us_topic_0031136109_i438354691645"></a><a name="en-us_topic_0031136109_i438354691645"></a>domainname</em>",
             "id": "<em id="en-us_topic_0031136109_i75268851664"><a name="en-us_topic_0031136109_i75268851664"></a><a name="en-us_topic_0031136109_i75268851664"></a>domainid</em>"
           } 
        }</pre>
    <a name="ul5441119421"></a><a name="ul5441119421"></a><ul id="ul5441119421"><li><strong id="b18525043132816"><a name="b18525043132816"></a><a name="b18525043132816"></a>user.name</strong>: Name of the user that owns the token</li><li><strong id="b19460350162817"><a name="b19460350162817"></a><a name="b19460350162817"></a>user.id</strong>: ID of the user</li><li><strong id="b266416917292"><a name="b266416917292"></a><a name="b266416917292"></a>domain.name</strong>: Name of the domain to which the user belongs</li><li><strong id="b2373202662920"><a name="b2373202662920"></a><a name="b2373202662920"></a>domain.id</strong>: ID of the domain</li><li><strong id="b1662172810293"><a name="b1662172810293"></a><a name="b1662172810293"></a>password_expires_at</strong>: Time when the password will expire. <strong id="b966317286299"><a name="b966317286299"></a><a name="b966317286299"></a>null</strong> indicates that the password will not expire. This parameter is optional.</li></ul>
    </td>
    </tr>
    <tr id="rd2b813ad52484c1bb6f776faff41f24e"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="a60103a37eec2447f91f0b5c1be69e796"><a name="a60103a37eec2447f91f0b5c1be69e796"></a><a name="a60103a37eec2447f91f0b5c1be69e796"></a>domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="ab3872b16cb6b43dc9859c6d47b23753f"><a name="ab3872b16cb6b43dc9859c6d47b23753f"></a><a name="ab3872b16cb6b43dc9859c6d47b23753f"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="adf0c78cdfb4443b7bfe893e568cf6e3c"><a name="adf0c78cdfb4443b7bfe893e568cf6e3c"></a><a name="adf0c78cdfb4443b7bfe893e568cf6e3c"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="a62354a3d06f44ba0b35920a8960377b8"><a name="a62354a3d06f44ba0b35920a8960377b8"></a><a name="a62354a3d06f44ba0b35920a8960377b8"></a>The system determines whether to return this field based on the scope contained in the request for obtaining the token.</p>
    <p id="a4851306d5e804606a8d6ff1fe676ffe2"><a name="a4851306d5e804606a8d6ff1fe676ffe2"></a><a name="a4851306d5e804606a8d6ff1fe676ffe2"></a>Example:</p>
    <pre class="screen" id="s5ff3f88773fa485ba0fbd9f0ec9f4e87"><a name="s5ff3f88773fa485ba0fbd9f0ec9f4e87"></a><a name="s5ff3f88773fa485ba0fbd9f0ec9f4e87"></a>"domain": { 
          "name" : "domainame",     
          "id" : "domainid"
    }</pre>
    <a name="ul42892719426"></a><a name="ul42892719426"></a><ul id="ul42892719426"><li><strong id="b948315019309"><a name="b948315019309"></a><a name="b948315019309"></a>domain_name</strong>: Domain name</li><li><strong id="b1281179173016"><a name="b1281179173016"></a><a name="b1281179173016"></a>domain.id</strong>: Domain ID</li></ul>
    </td>
    </tr>
    <tr id="r49eebdc20c3447e79e97f36423ae5934"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="a4a2c41d7a9e34398b44bd36829e6e527"><a name="a4a2c41d7a9e34398b44bd36829e6e527"></a><a name="a4a2c41d7a9e34398b44bd36829e6e527"></a>project</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="abc19800d1e1247d4ba54fe02645b0912"><a name="abc19800d1e1247d4ba54fe02645b0912"></a><a name="abc19800d1e1247d4ba54fe02645b0912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="ae5b0fdbdc9de485ba9ee16c4541a3d8f"><a name="ae5b0fdbdc9de485ba9ee16c4541a3d8f"></a><a name="ae5b0fdbdc9de485ba9ee16c4541a3d8f"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="a2659a34f291f467e8b5bf2d33f15129c"><a name="a2659a34f291f467e8b5bf2d33f15129c"></a><a name="a2659a34f291f467e8b5bf2d33f15129c"></a>The system determines whether to return this field based on the scope contained in the request for obtaining the token.</p>
    <p id="a62446cb5fca746d3824fe1d43530eefb"><a name="a62446cb5fca746d3824fe1d43530eefb"></a><a name="a62446cb5fca746d3824fe1d43530eefb"></a>Example:</p>
    <pre class="screen" id="s4c5b7b8fc0394e61817577d5049359db"><a name="s4c5b7b8fc0394e61817577d5049359db"></a><a name="s4c5b7b8fc0394e61817577d5049359db"></a>"project": { 
          "name": "<em id="a7730a018d3ea40d0ac223462281202e4"><a name="a7730a018d3ea40d0ac223462281202e4"></a><a name="a7730a018d3ea40d0ac223462281202e4"></a>projectname</em>", 
          "id": "<em id="en-us_topic_0031136109_i86520761696"><a name="en-us_topic_0031136109_i86520761696"></a><a name="en-us_topic_0031136109_i86520761696"></a>projectid</em>", 
    }</pre>
    <a name="ul16649104334215"></a><a name="ul16649104334215"></a><ul id="ul16649104334215"><li><strong id="b1232142083011"><a name="b1232142083011"></a><a name="b1232142083011"></a>project.name</strong>: Name of a project</li><li><strong id="b967662223015"><a name="b967662223015"></a><a name="b967662223015"></a>project.id</strong>: ID of the project</li></ul>
    </td>
    </tr>
    <tr id="row147105584397"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="p22717013113628"><a name="p22717013113628"></a><a name="p22717013113628"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="p54936595113628"><a name="p54936595113628"></a><a name="p54936595113628"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p46529556113628"><a name="p46529556113628"></a><a name="p46529556113628"></a>Json Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="p45368001113628"><a name="p45368001113628"></a><a name="p45368001113628"></a>Endpoint information</p>
    <p id="p50787600113939"><a name="p50787600113939"></a><a name="p50787600113939"></a>Example:</p>
    <pre class="screen" id="screen19141143191815"><a name="screen19141143191815"></a><a name="screen19141143191815"></a>"catalog": [{
        "type": "identity",
        "id": "1331e5cff2a74d76b03da1225910e31d",
        "name": "iam",
        "endpoints": [{
            "url": "<em id="i17055930114035"><a name="i17055930114035"></a><a name="i17055930114035"></a>www.example.com</em>/v3",
            "region": "*",
            "region_id": "*",
            "interface": "public",
            "id": "089d4a381d574308a703122d3ae738e9"
        }]
    }]</pre>
    <a name="ul243124664420"></a><a name="ul243124664420"></a><ul id="ul243124664420"><li><strong id="b112631933103018"><a name="b112631933103018"></a><a name="b112631933103018"></a>type</strong>: Type of the service to which the API belongs</li><li><strong id="b14577193511303"><a name="b14577193511303"></a><a name="b14577193511303"></a>id</strong>: ID of the service</li><li><strong id="b1450714014308"><a name="b1450714014308"></a><a name="b1450714014308"></a>name</strong>: Name of the service</li><li><strong id="b10141104203012"><a name="b10141104203012"></a><a name="b10141104203012"></a>endpoints</strong>: Endpoints that can be used to call the API</li><li><strong id="b193931144143014"><a name="b193931144143014"></a><a name="b193931144143014"></a>url</strong>: URL used to call the API</li><li><strong id="b1282215811327"><a name="b1282215811327"></a><a name="b1282215811327"></a>region</strong>: Region in which the service can be accessed</li><li><strong id="b1485219916329"><a name="b1485219916329"></a><a name="b1485219916329"></a>region_id</strong>: ID of the region</li><li><strong id="b102361115322"><a name="b102361115322"></a><a name="b102361115322"></a>interface</strong>: Type of the interface. The value <strong id="b32511193214"><a name="b32511193214"></a><a name="b32511193214"></a>public</strong> means that the API is open for access.</li><li><strong id="b15205101583210"><a name="b15205101583210"></a><a name="b15205101583210"></a>id</strong>: ID of the API</li></ul>
    </td>
    </tr>
    <tr id="r76860dcda39c46a9b78f96428dcbcb14"><td class="cellrowborder" valign="top" width="19.21%" headers="mcps1.1.5.1.1 "><p id="a86671885064746d781a2d581f1f7826c"><a name="a86671885064746d781a2d581f1f7826c"></a><a name="a86671885064746d781a2d581f1f7826c"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.2 "><p id="ae1c2c67daddd401abc13d680e5cda5ee"><a name="ae1c2c67daddd401abc13d680e5cda5ee"></a><a name="ae1c2c67daddd401abc13d680e5cda5ee"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a1b25331d8f1e4e65bacbc840dae50aed"><a name="a1b25331d8f1e4e65bacbc840dae50aed"></a><a name="a1b25331d8f1e4e65bacbc840dae50aed"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.410000000000004%" headers="mcps1.1.5.1.4 "><p id="a4046ff35c37e405c91f599bfafe3d182"><a name="a4046ff35c37e405c91f599bfafe3d182"></a><a name="a4046ff35c37e405c91f599bfafe3d182"></a>Permissions information of the token</p>
    <p id="a901e55a86b2448cab20381e6d06fc7fc"><a name="a901e55a86b2448cab20381e6d06fc7fc"></a><a name="a901e55a86b2448cab20381e6d06fc7fc"></a>Example:</p>
    <pre class="screen" id="s120c9eb390ab48df8b849e94fa1a2d1c"><a name="s120c9eb390ab48df8b849e94fa1a2d1c"></a><a name="s120c9eb390ab48df8b849e94fa1a2d1c"></a>"roles" : [{ 
         "name" : "role1", 
         "id" : "roleid1" 
         }, { 
         "name" : "role2", 
         "id" : "roleid2" 
         } 
       ] </pre>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
      "token" : {
        "methods" : ["password"],
        "expires_at" : "2015-11-09T01:42:57.527363Z",
        "issued_at" : "2015-11-09T00:42:57.527404Z",
        "user" : {
          "domain" : {
          "id" : "default",
          "name" : "Default"
          },
          "id" : "ee4dfb6e5540447cb3741905149XXX...",
          "password_expires_at":"2016-11-06T15:32:17.000000",
          "name" : "admin"
        },
        "domain" : {
           "name" : "Default",
           "id" : "default"
        },
        "roles" : [{
           "name" : "role1",
           "id" : "roleid1"
           }, {
           "name" : "role2",
           "id" : "roleid2"
           }
      ]
      }
    }
    ```


## Status Codes<a name="s5f49b0a31dfd4c0ba72af9d16199f092"></a>

<a name="en-us_topic_0031136109_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0031136109_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0031136109_p51565323"><a name="en-us_topic_0031136109_p51565323"></a><a name="en-us_topic_0031136109_p51565323"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0031136109_p16041657"><a name="en-us_topic_0031136109_p16041657"></a><a name="en-us_topic_0031136109_p16041657"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0031136109_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac58be25dfe6c4aaf9db2b9a3d7fbabca"><a name="ac58be25dfe6c4aaf9db2b9a3d7fbabca"></a><a name="ac58be25dfe6c4aaf9db2b9a3d7fbabca"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6e2de6a7a37947b5aef6f82b48011a03"><a name="a6e2de6a7a37947b5aef6f82b48011a03"></a><a name="a6e2de6a7a37947b5aef6f82b48011a03"></a>The request is successful.</p>
</td>
</tr>
<tr id="r7fc6a01de7944676924285967a1e5bc8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae582169a40d14518b8b1c9e774696af6"><a name="ae582169a40d14518b8b1c9e774696af6"></a><a name="ae582169a40d14518b8b1c9e774696af6"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a01d650708f044356a0e8711abade8518"><a name="a01d650708f044356a0e8711abade8518"></a><a name="a01d650708f044356a0e8711abade8518"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0031136109_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa1436dc96eeb4ecba5f1a6cf55c4e96d"><a name="aa1436dc96eeb4ecba5f1a6cf55c4e96d"></a><a name="aa1436dc96eeb4ecba5f1a6cf55c4e96d"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3c42a75c98a04c7b9efffdbcd6a0442b"><a name="a3c42a75c98a04c7b9efffdbcd6a0442b"></a><a name="a3c42a75c98a04c7b9efffdbcd6a0442b"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="rbe3685e5aeff47eb990a671b5857c0c7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3147c9b90baa43c8ad749a408a6d9b20"><a name="a3147c9b90baa43c8ad749a408a6d9b20"></a><a name="a3147c9b90baa43c8ad749a408a6d9b20"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae8403ffe26014f779b51914498b2335b"><a name="ae8403ffe26014f779b51914498b2335b"></a><a name="ae8403ffe26014f779b51914498b2335b"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="re1fee93942c94c99adf7dd268d6bc21c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9b3726f2a0fd4e9c99679f1f64a01170"><a name="a9b3726f2a0fd4e9c99679f1f64a01170"></a><a name="a9b3726f2a0fd4e9c99679f1f64a01170"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6fff1dadf47d4a6fb59c6e4274ffd613"><a name="a6fff1dadf47d4a6fb59c6e4274ffd613"></a><a name="a6fff1dadf47d4a6fb59c6e4274ffd613"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rd595ecff1f1047e9bd258da07fd41c0a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1ab42a838d1c473f967bbd05e9634618"><a name="a1ab42a838d1c473f967bbd05e9634618"></a><a name="a1ab42a838d1c473f967bbd05e9634618"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aedeaace596704f93813419fae71746d7"><a name="aedeaace596704f93813419fae71746d7"></a><a name="aedeaace596704f93813419fae71746d7"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

