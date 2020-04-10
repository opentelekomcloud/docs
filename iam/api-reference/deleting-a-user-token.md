# Deleting a User Token<a name="iam_02_0063"></a>

## Function Description<a name="s2f7665a32abf4492987e6dd3617bcb21"></a>

This interface is used to delete a token no matter whether the token has expired or not.

## URI<a name="s1c0fd353ed38459c8baeab25cc3c62d2"></a>

URI format

DELETE /v3/auth/tokens

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
    <td class="cellrowborder" valign="top" width="46.62533746625338%" headers="mcps1.1.5.1.4 "><p id="p1821614196437"><a name="p1821614196437"></a><a name="p1821614196437"></a>Obtained token</p>
    <a name="ul1963814299291"></a><a name="ul1963814299291"></a><ul id="ul1963814299291"><li>To delete your own token, specify your token. There are no special requirements on the permissions that your token must have.</li><li>To delete the token of another user under the same domain, use a token that has permissions of the <strong id="b1524464910379"><a name="b1524464910379"></a><a name="b1524464910379"></a>Security Administrator</strong> policy.</li></ul>
    </td>
    </tr>
    <tr id="r4ebaddfb83fe4bffa462094cc2834cf2"><td class="cellrowborder" valign="top" width="19.038096190380962%" headers="mcps1.1.5.1.1 "><p id="ae9df07c230354205b9c3cb76f08eadb4"><a name="ae9df07c230354205b9c3cb76f08eadb4"></a><a name="ae9df07c230354205b9c3cb76f08eadb4"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.578242175782425%" headers="mcps1.1.5.1.2 "><p id="a1100e03a09864240abecdff29c388bf8"><a name="a1100e03a09864240abecdff29c388bf8"></a><a name="a1100e03a09864240abecdff29c388bf8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.75832416758324%" headers="mcps1.1.5.1.3 "><p id="a667fee7780224b0d9e78b40c59beaccf"><a name="a667fee7780224b0d9e78b40c59beaccf"></a><a name="a667fee7780224b0d9e78b40c59beaccf"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.62533746625338%" headers="mcps1.1.5.1.4 "><p id="a3e67d6bcffd14d9cbbe0fbad423e13de"><a name="a3e67d6bcffd14d9cbbe0fbad423e13de"></a><a name="a3e67d6bcffd14d9cbbe0fbad423e13de"></a>Token to be deleted</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H "X-Subject-Token:$token" -X DELETE https://sample.domain.com/v3/auth/tokens
    ```


## Response<a name="section2098793814412"></a>

None

## Status Codes<a name="s5f49b0a31dfd4c0ba72af9d16199f092"></a>

<a name="en-us_topic_0031136109_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0031136109_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0031136109_p51565323"><a name="en-us_topic_0031136109_p51565323"></a><a name="en-us_topic_0031136109_p51565323"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0031136109_p16041657"><a name="en-us_topic_0031136109_p16041657"></a><a name="en-us_topic_0031136109_p16041657"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0031136109_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac58be25dfe6c4aaf9db2b9a3d7fbabca"><a name="ac58be25dfe6c4aaf9db2b9a3d7fbabca"></a><a name="ac58be25dfe6c4aaf9db2b9a3d7fbabca"></a>204</p>
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

