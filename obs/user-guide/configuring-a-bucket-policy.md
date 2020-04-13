# Configuring a Bucket Policy<a name="en-us_topic_0045853707"></a>

A bucket policy defines the access control policy of resources \(buckets and objects\) in OBS.

## Procedure<a name="sa9ce61a965cf44278ecdea3220e325dd"></a>

1.  Log in to OBS Browser.
2.  Click the blank area in the row of the bucket for which you want to configure a bucket policy and choose  **More**  \>  **Configure Bucket Policy**.
3.  In the  **Configure Bucket Policy**  dialog box, input required parameters.

    The size of a bucket policy cannot exceed 20 KB.

    [Table 1](#t90f413f7432b4558b68c408483fd2be9)  describes the parameters of bucket policies. All fields except the  **Effect**  field are optional.

    **Table  1**  Parameters in bucket policies

    <a name="t90f413f7432b4558b68c408483fd2be9"></a>
    <table><thead align="left"><tr id="r76e46083a7d54583b866b710d57a869b"><th class="cellrowborder" valign="top" width="16.24%" id="mcps1.2.4.1.1"><p id="a9f330eae4b1445d9bd50f9aee100fedb"><a name="a9f330eae4b1445d9bd50f9aee100fedb"></a><a name="a9f330eae4b1445d9bd50f9aee100fedb"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76.24%" id="mcps1.2.4.1.2"><p id="ade48ab9c0cee409cb2d3be53e627432c"><a name="ade48ab9c0cee409cb2d3be53e627432c"></a><a name="ade48ab9c0cee409cb2d3be53e627432c"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.3"><p id="aa22db190a3b249858056287fa2a41496"><a name="aa22db190a3b249858056287fa2a41496"></a><a name="aa22db190a3b249858056287fa2a41496"></a>Mandatory or Not</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r37b6d3a82f2c41ab9f69396983c71926"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="a615391a7b87c446dbc6036f21444ec60"><a name="a615391a7b87c446dbc6036f21444ec60"></a><a name="a615391a7b87c446dbc6036f21444ec60"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="ae3b32b0875da4e6a8eabc2becb00a9e8"><a name="ae3b32b0875da4e6a8eabc2becb00a9e8"></a><a name="ae3b32b0875da4e6a8eabc2becb00a9e8"></a>The value can be <strong id="b1963142212265"><a name="b1963142212265"></a><a name="b1963142212265"></a>2008-10-17</strong> or <strong id="b18974284267"><a name="b18974284267"></a><a name="b18974284267"></a>2012-10-17</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="aa77b671e052e4e78b047b721a4f145a3"><a name="aa77b671e052e4e78b047b721a4f145a3"></a><a name="aa77b671e052e4e78b047b721a4f145a3"></a>Optional</p>
    </td>
    </tr>
    <tr id="rdbb1644385db43279b36f8a44dfa88b8"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="adc42ec63f7514e51979d28c0e5d1c5e9"><a name="adc42ec63f7514e51979d28c0e5d1c5e9"></a><a name="adc42ec63f7514e51979d28c0e5d1c5e9"></a>Id</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="a828a97a16dcb41efad1246d7534f2dbd"><a name="a828a97a16dcb41efad1246d7534f2dbd"></a><a name="a828a97a16dcb41efad1246d7534f2dbd"></a>The ID of the bucket policy. The value must be unique.</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="a13cb2f6bd41f4ef3ba7a5fce5941fe26"><a name="a13cb2f6bd41f4ef3ba7a5fce5941fe26"></a><a name="a13cb2f6bd41f4ef3ba7a5fce5941fe26"></a>Optional</p>
    </td>
    </tr>
    <tr id="r9b53ca8e1b774da29a1ce3808fff149c"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="abcbf9eb4a1054ad2a697318b6bd890e3"><a name="abcbf9eb4a1054ad2a697318b6bd890e3"></a><a name="abcbf9eb4a1054ad2a697318b6bd890e3"></a>Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="a6a5c216cd1aa40f0b60d5711b95cdef3"><a name="a6a5c216cd1aa40f0b60d5711b95cdef3"></a><a name="a6a5c216cd1aa40f0b60d5711b95cdef3"></a>The description of the bucket policy. The statement defines complete permission control. Each bucket policy can have multiple statements, and each statement contains the following parameters:</p>
    <a name="u1aecb422630444f9a819613f2cd1fcfd"></a><a name="u1aecb422630444f9a819613f2cd1fcfd"></a><ul id="u1aecb422630444f9a819613f2cd1fcfd"><li>Sid</li><li>Effect</li><li>Principal</li><li>NotPrincipal</li><li>Action</li><li>NotAction</li><li>Resource</li><li>NotResource</li><li>Condition</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="a6c3d65f385cb43019d9cff48552811d2"><a name="a6c3d65f385cb43019d9cff48552811d2"></a><a name="a6c3d65f385cb43019d9cff48552811d2"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="re811dabc0b744a9db97c15075b0666c2"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="adeea10edb32442ceb79834f2407894f3"><a name="adeea10edb32442ceb79834f2407894f3"></a><a name="adeea10edb32442ceb79834f2407894f3"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="abb507befc309403e973caed0ef17a9b5"><a name="abb507befc309403e973caed0ef17a9b5"></a><a name="abb507befc309403e973caed0ef17a9b5"></a>Effect of the bucket policy. The statement can be set to accept or reject requests. Possible values are <strong id="b95049285151227"><a name="b95049285151227"></a><a name="b95049285151227"></a>Allow</strong> and <strong id="b311781335151227"><a name="b311781335151227"></a><a name="b311781335151227"></a>Deny</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="a58481dae19464eb795944c0f77c1746f"><a name="a58481dae19464eb795944c0f77c1746f"></a><a name="a58481dae19464eb795944c0f77c1746f"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="rb4776c5d34994af39494c4853d4a05eb"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="acb40787b51ff475c88f9429d20931a7f"><a name="acb40787b51ff475c88f9429d20931a7f"></a><a name="acb40787b51ff475c88f9429d20931a7f"></a>Sid</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="a6b289a4511a34acda6967a3a29fde76d"><a name="a6b289a4511a34acda6967a3a29fde76d"></a><a name="a6b289a4511a34acda6967a3a29fde76d"></a>The statement ID.</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="ab10401c22da84465bff2559b47386704"><a name="ab10401c22da84465bff2559b47386704"></a><a name="ab10401c22da84465bff2559b47386704"></a>Optional</p>
    </td>
    </tr>
    <tr id="rd3c89d23a35f4f528c9cd1c343d9eb6c"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="a791a73fba0f141b497d21808d7ba4936"><a name="a791a73fba0f141b497d21808d7ba4936"></a><a name="a791a73fba0f141b497d21808d7ba4936"></a>Principal/NotPrincipal</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="aa07e0a51e82a4fd99937eb3071f6c437"><a name="aa07e0a51e82a4fd99937eb3071f6c437"></a><a name="aa07e0a51e82a4fd99937eb3071f6c437"></a>Users on whom the bucket policy statement takes effect</p>
    <p id="a13176cf37f534f75b1bb48a03c796c22"><a name="a13176cf37f534f75b1bb48a03c796c22"></a><a name="a13176cf37f534f75b1bb48a03c796c22"></a>Either <strong id="a5016ae9fe2e845f2b3b76c69e35fcbb4"><a name="a5016ae9fe2e845f2b3b76c69e35fcbb4"></a><a name="a5016ae9fe2e845f2b3b76c69e35fcbb4"></a>Principal</strong> or <strong id="en-us_topic_0068417483_b633253613238"><a name="en-us_topic_0068417483_b633253613238"></a><a name="en-us_topic_0068417483_b633253613238"></a>NotPrincipal</strong> must be selected to specify the user on whom the bucket policy statement takes effect or does not take effect.</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="ac66e9f7d22c048a78fc6bc19d85b3daa"><a name="ac66e9f7d22c048a78fc6bc19d85b3daa"></a><a name="ac66e9f7d22c048a78fc6bc19d85b3daa"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="re157b39294c34983a344bdd2c19d3867"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="ad301d40b837a4d808b3ade5e40303f19"><a name="ad301d40b837a4d808b3ade5e40303f19"></a><a name="ad301d40b837a4d808b3ade5e40303f19"></a>Action/NotAction</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="afe04e5f242e546bb9ba2d0527af3d34c"><a name="afe04e5f242e546bb9ba2d0527af3d34c"></a><a name="afe04e5f242e546bb9ba2d0527af3d34c"></a>OBS operations on which the bucket policy statement takes effect</p>
    <p id="af08cacea86e44fceb08b23dcef32a160"><a name="af08cacea86e44fceb08b23dcef32a160"></a><a name="af08cacea86e44fceb08b23dcef32a160"></a>Either <strong id="b208460462388"><a name="b208460462388"></a><a name="b208460462388"></a>Action</strong> or <strong id="b1386164993816"><a name="b1386164993816"></a><a name="b1386164993816"></a>NotAction</strong> must be selected to specify whether the bucket policy statement takes effect on the OBS operation.</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="a5cd8ed2c61f348de990ca923abf0b2ea"><a name="a5cd8ed2c61f348de990ca923abf0b2ea"></a><a name="a5cd8ed2c61f348de990ca923abf0b2ea"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="r1b58c573b77d42d6aadcd4321ea261ef"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="ae72aee7b2c02460e9cc37200a5e2ba8b"><a name="ae72aee7b2c02460e9cc37200a5e2ba8b"></a><a name="ae72aee7b2c02460e9cc37200a5e2ba8b"></a>Resource/NotResource</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="a851f0a72bf774eb8b15f76e4b054de25"><a name="a851f0a72bf774eb8b15f76e4b054de25"></a><a name="a851f0a72bf774eb8b15f76e4b054de25"></a>Objects on which the bucket policy statement takes effect</p>
    <p id="aaa19587fb1e14b49a31f4c9e9cc17200"><a name="aaa19587fb1e14b49a31f4c9e9cc17200"></a><a name="aaa19587fb1e14b49a31f4c9e9cc17200"></a>Either <strong id="b183645180397"><a name="b183645180397"></a><a name="b183645180397"></a>Resource</strong> or <strong id="b1999120223391"><a name="b1999120223391"></a><a name="b1999120223391"></a>NotResource</strong> must be selected to specify whether the bucket policy statement takes effect on the OBS resources.</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="a69e88c1bcd29489ea748671680a5d3cc"><a name="a69e88c1bcd29489ea748671680a5d3cc"></a><a name="a69e88c1bcd29489ea748671680a5d3cc"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="rc844bea9ce534b2d8897afa8961769a3"><td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.1 "><p id="a10df44ea04524424a173bf17d7de7aec"><a name="a10df44ea04524424a173bf17d7de7aec"></a><a name="a10df44ea04524424a173bf17d7de7aec"></a>Condition</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.24%" headers="mcps1.2.4.1.2 "><p id="adda00a6ecf9f45fcbb6fbcea7ea55f5f"><a name="adda00a6ecf9f45fcbb6fbcea7ea55f5f"></a><a name="adda00a6ecf9f45fcbb6fbcea7ea55f5f"></a>The conditions under which the bucket policy takes effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.3 "><p id="a0eef764f8bba4023be7c6aeb8f608e07"><a name="a0eef764f8bba4023be7c6aeb8f608e07"></a><a name="a0eef764f8bba4023be7c6aeb8f608e07"></a>Optional</p>
    </td>
    </tr>
    </tbody>
    </table>

    Example: Uploading objects to bucket  **bucket-example**  is not allowed.

    ```
    {
        "Version":"2008-10-17",
        "Id":"Policy1527928945090",
        "Statement":[
            {
                "Sid":"Stmt1527929149040",
                "Effect":"Deny",
                "Principal":
                {
                    "AWS":[
                        "*"
                    ]
                },
                "Action":[
                    "s3:Put*"
                ],
                "Resource":[
                    "arn:aws:s3:::bucket-example/*"
                ]
            }
        ]
    }
    ```

4.  Click  **Save**.
5.  In the displayed dialog box, click  **Close**  to close the dialog box.

