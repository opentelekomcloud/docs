# Querying the Password Strength Policy by Option<a name="iam_02_0113"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to query the password strength policy by  **option**. The option can be the regular expression and description of the password strength policy.

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

-   URI format

    GET /v3/domains/\{domain\_id\}/config/security\_compliance/\{option\}

-   URI parameter description

    <a name="table2671410511552"></a>
    <table><thead align="left"><tr id="row2181345411552"><th class="cellrowborder" valign="top" width="22.14%" id="mcps1.1.5.1.1"><p id="p4197580011552"><a name="p4197580011552"></a><a name="p4197580011552"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.09%" id="mcps1.1.5.1.2"><p id="p5555552611552"><a name="p5555552611552"></a><a name="p5555552611552"></a><strong id="ac429376f11ae472b87ff4be326afb9d8"><a name="ac429376f11ae472b87ff4be326afb9d8"></a><a name="ac429376f11ae472b87ff4be326afb9d8"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.11%" id="mcps1.1.5.1.3"><p id="p3157154611552"><a name="p3157154611552"></a><a name="p3157154611552"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.66%" id="mcps1.1.5.1.4"><p id="p4296341111552"><a name="p4296341111552"></a><a name="p4296341111552"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2571374511552"><td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.1.5.1.1 "><p id="p6330725211552"><a name="p6330725211552"></a><a name="p6330725211552"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p2212117911552"><a name="p2212117911552"></a><a name="p2212117911552"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.3 "><p id="p4769668011552"><a name="p4769668011552"></a><a name="p4769668011552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p928844211552"><a name="p928844211552"></a><a name="p928844211552"></a>ID of the domain whose password strength policy is to be queried.</p>
    </td>
    </tr>
    <tr id="row1416632711552"><td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.1.5.1.1 "><p id="p6660449211552"><a name="p6660449211552"></a><a name="p6660449211552"></a>option</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p4626117411552"><a name="p4626117411552"></a><a name="p4626117411552"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.3 "><p id="p5328411711552"><a name="p5328411711552"></a><a name="p5328411711552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p2702541811552"><a name="p2702541811552"></a><a name="p2702541811552"></a>Query option, which can be <strong id="b842352706151335"><a name="b842352706151335"></a><a name="b842352706151335"></a>password_regex</strong> or <strong id="b842352706151340"><a name="b842352706151340"></a><a name="b842352706151340"></a>password_regex_description</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="21.81218121812181%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><strong id="b1767617509"><a name="b1767617509"></a><a name="b1767617509"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.352035203520348%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a><strong id="b1635699317"><a name="b1635699317"></a><a name="b1635699317"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.092009200920092%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><strong id="b1247323078"><a name="b1247323078"></a><a name="b1247323078"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.743774377437745%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><strong id="b1447761883"><a name="b1447761883"></a><a name="b1447761883"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="21.81218121812181%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.352035203520348%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.092009200920092%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.743774377437745%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row29501427115257"><td class="cellrowborder" valign="top" width="21.81218121812181%" headers="mcps1.1.5.1.1 "><p id="p6637478211538"><a name="p6637478211538"></a><a name="p6637478211538"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.352035203520348%" headers="mcps1.1.5.1.2 "><p id="p764826811538"><a name="p764826811538"></a><a name="p764826811538"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.092009200920092%" headers="mcps1.1.5.1.3 "><p id="p1553001111538"><a name="p1553001111538"></a><a name="p1553001111538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.743774377437745%" headers="mcps1.1.5.1.4 "><p id="p3577810173953"><a name="p3577810173953"></a><a name="p3577810173953"></a>Authenticated user token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/domains/{domain_id}/config/security_compliance/password_regex
    ```


## **Response**<a name="s3a08e13bb5b34dc2ba4dcd84a0d51cf5"></a>

-   Response body parameter description

    <a name="t1266dd240c3649048c9f42af34a0686b"></a>
    <table><thead align="left"><tr id="rd8ac2cd80e4b47d684b61df4f3c570cf"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.1.5.1.1"><p id="ad167d1bf89ca443eac693ea562da12a3"><a name="ad167d1bf89ca443eac693ea562da12a3"></a><a name="ad167d1bf89ca443eac693ea562da12a3"></a><strong id="b587086282"><a name="b587086282"></a><a name="b587086282"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.2"><p id="aad08ea1f8c8e4a42a1a81112a74cb237"><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><strong id="b2009964419"><a name="b2009964419"></a><a name="b2009964419"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.349999999999998%" id="mcps1.1.5.1.3"><p id="a9b5fafff0348408893dcc06fbe0b1186"><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><strong id="b1909801102"><a name="b1909801102"></a><a name="b1909801102"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.480000000000004%" id="mcps1.1.5.1.4"><p id="ad002a0bf107a468884a5777e55f837f6"><a name="ad002a0bf107a468884a5777e55f837f6"></a><a name="ad002a0bf107a468884a5777e55f837f6"></a><strong id="b909565086"><a name="b909565086"></a><a name="b909565086"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ref3b81e8e64e418c961ca1bce6f25280"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.1.5.1.1 "><p id="abb2b4d81b907497da50ad4f12760f7dc"><a name="abb2b4d81b907497da50ad4f12760f7dc"></a><a name="abb2b4d81b907497da50ad4f12760f7dc"></a>config</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.2 "><p id="a7e49a4eaca054e36ba774b0cdc492081"><a name="a7e49a4eaca054e36ba774b0cdc492081"></a><a name="a7e49a4eaca054e36ba774b0cdc492081"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.1.5.1.3 "><p id="p9747112319316"><a name="p9747112319316"></a><a name="p9747112319316"></a>JSON</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.1.5.1.4 "><p id="a8ded0409c6d948dc82f7f779a4cfa5b8"><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a>Password strength policy of a domain.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the config format

    <a name="t3ef10d134105438f922a72ac36adbe13"></a>
    <table><thead align="left"><tr id="ra836795da3204436ad115c6d63f33cb3"><th class="cellrowborder" valign="top" width="21.462146214621463%" id="mcps1.1.5.1.1"><p id="a915f4fa2492a4fa3b5fc5b52cb975ed3"><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><strong id="b1293628936"><a name="b1293628936"></a><a name="b1293628936"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.642064206420642%" id="mcps1.1.5.1.2"><p id="aeb29128c8bc6489593aaf12297635c52"><a name="aeb29128c8bc6489593aaf12297635c52"></a><a name="aeb29128c8bc6489593aaf12297635c52"></a><strong id="b130154287"><a name="b130154287"></a><a name="b130154287"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.75207520752075%" id="mcps1.1.5.1.3"><p id="a367df15999ce47aa8fa2550bb2d3df9a"><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><strong id="b32128364"><a name="b32128364"></a><a name="b32128364"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.14371437143714%" id="mcps1.1.5.1.4"><p id="a16a6b7e4145e4fbabf25e75163ec3f95"><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><strong id="b954838767"><a name="b954838767"></a><a name="b954838767"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rb2ba995189ec478eb5d1181d3bb7be1c"><td class="cellrowborder" valign="top" width="21.462146214621463%" headers="mcps1.1.5.1.1 "><p id="aa1005da54f2c4746ae99676d14ab012d"><a name="aa1005da54f2c4746ae99676d14ab012d"></a><a name="aa1005da54f2c4746ae99676d14ab012d"></a>password_regex</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.642064206420642%" headers="mcps1.1.5.1.2 "><p id="a6d0540b177e34775b18c670cf5cd46bc"><a name="a6d0540b177e34775b18c670cf5cd46bc"></a><a name="a6d0540b177e34775b18c670cf5cd46bc"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.75207520752075%" headers="mcps1.1.5.1.3 "><p id="a65f6a6fc5a364d868072c58eeab90325"><a name="a65f6a6fc5a364d868072c58eeab90325"></a><a name="a65f6a6fc5a364d868072c58eeab90325"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.14371437143714%" headers="mcps1.1.5.1.4 "><p id="p7983029174658"><a name="p7983029174658"></a><a name="p7983029174658"></a>Regular expression of the password strength policy (When <strong id="b842352706151545"><a name="b842352706151545"></a><a name="b842352706151545"></a>option</strong> is set to <strong id="b842352706151552"><a name="b842352706151552"></a><a name="b842352706151552"></a>password_regex</strong>).</p>
    </td>
    </tr>
    <tr id="row3151341114012"><td class="cellrowborder" valign="top" width="21.462146214621463%" headers="mcps1.1.5.1.1 "><p id="p1415234119406"><a name="p1415234119406"></a><a name="p1415234119406"></a>password_regex_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.642064206420642%" headers="mcps1.1.5.1.2 "><p id="af10224f581d946cb91a49683adf34271"><a name="af10224f581d946cb91a49683adf34271"></a><a name="af10224f581d946cb91a49683adf34271"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.75207520752075%" headers="mcps1.1.5.1.3 "><p id="a0316e95fb756489a82f70ae562c523b4"><a name="a0316e95fb756489a82f70ae562c523b4"></a><a name="a0316e95fb756489a82f70ae562c523b4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.14371437143714%" headers="mcps1.1.5.1.4 "><p id="af5ce8c5c520f468895f28d74f6eb4540"><a name="af5ce8c5c520f468895f28d74f6eb4540"></a><a name="af5ce8c5c520f468895f28d74f6eb4540"></a>Description of the password strength policy (When <strong id="b1744148927"><a name="b1744148927"></a><a name="b1744148927"></a>option</strong> is set to <strong id="b295836432"><a name="b295836432"></a><a name="b295836432"></a>password_regex_description</strong>).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    When option is set to password_regex:
    {
      "config": {
        "password_regex": "^(?=.*\\d)(?=.*[a-zA-Z]).{7,}$"
      }
    }
    When option is set to password_regex_description:
    {
      "config": {
        "password_regex_description": "Passwords must contain at least 1 letter, 1 digit, and be a minimum length of 7 characters."
      }
    }
    ```


## **Status Code**<a name="sbfe93ca4c2b9427dbb2218a4e72da6a8"></a>

<a name="en-us_topic_0035544336_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0035544336_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035544336_p51565323"><a name="en-us_topic_0035544336_p51565323"></a><a name="en-us_topic_0035544336_p51565323"></a><strong>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035544336_p16041657"><a name="en-us_topic_0035544336_p16041657"></a><a name="en-us_topic_0035544336_p16041657"></a><strong id="b241740987"><a name="b241740987"></a><a name="b241740987"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035544336_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p22613965"><a name="en-us_topic_0035544336_p22613965"></a><a name="en-us_topic_0035544336_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p19791876"><a name="en-us_topic_0035544336_p19791876"></a><a name="en-us_topic_0035544336_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p66980994"><a name="en-us_topic_0035544336_p66980994"></a><a name="en-us_topic_0035544336_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p56751409"><a name="en-us_topic_0035544336_p56751409"></a><a name="en-us_topic_0035544336_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="rb99fbab78bc54ae4953661763b573830"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aef55745ff0834933af36d690e2e339b8"><a name="aef55745ff0834933af36d690e2e339b8"></a><a name="aef55745ff0834933af36d690e2e339b8"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a480215738ced4bf5a8feafa2681db93b"><a name="a480215738ced4bf5a8feafa2681db93b"></a><a name="a480215738ced4bf5a8feafa2681db93b"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p32717189"><a name="en-us_topic_0035544336_p32717189"></a><a name="en-us_topic_0035544336_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae678037f26d640f5a985c943e2ffb92e"><a name="ae678037f26d640f5a985c943e2ffb92e"></a><a name="ae678037f26d640f5a985c943e2ffb92e"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r1fd5c05b7b6b4c048f3f7b9ddbc755b0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5d7e2305922e4f9098442a900792dae1"><a name="a5d7e2305922e4f9098442a900792dae1"></a><a name="a5d7e2305922e4f9098442a900792dae1"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9edf299d0513460caaac8a2a19b76e9a"><a name="a9edf299d0513460caaac8a2a19b76e9a"></a><a name="a9edf299d0513460caaac8a2a19b76e9a"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rbb5133f150fd42eebde8dd6e390ecbd5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad1a2754016e44193a97043265cd611cf"><a name="ad1a2754016e44193a97043265cd611cf"></a><a name="ad1a2754016e44193a97043265cd611cf"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a81837d461ef445259c5a6e9e1ce0e32a"><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="r2cecff297b1a412f956a312d3cd7acc9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1f617621d1bc4a9facb1c84d1946002b"><a name="a1f617621d1bc4a9facb1c84d1946002b"></a><a name="a1f617621d1bc4a9facb1c84d1946002b"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac31ead3ee2db40eea8ae45b2779a09e9"><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="rd71e0e00759f4179a2dccaf345ba9f2f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1657c5ca5ebd4a2cbacbdb35fc9b7601"><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a88b4b14048564e12942b8151dc791b99"><a name="a88b4b14048564e12942b8151dc791b99"></a><a name="a88b4b14048564e12942b8151dc791b99"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="r5647e5fd26974514ac66cc3925f30601"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a16dfaa16ceac4a33a468c0ae158292fb"><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5635c1924d9648a8be89b1e5dcf0a87b"><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

