# Obtaining an Agency Token<a name="en-us_topic_0064274720"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to obtain an agency token. For example, after a trust relationship is established between A and B, A is the delegating party and B is the delegated party. Then B can use this interface to obtain the agency token. The agency token can be used to manage only the resources that B is delegated to manage. To manage its own resources, B needs to obtain a user token according to  [Obtaining a User Token](obtaining-a-user-token.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>A token is valid for 24 hours. If you use a token for authentication, cache it to avoid frequently calling this API.  

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

URI format

POST /v3/auth/tokens

## Request<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="21.42%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.22%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.42%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.22%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.42%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <span class="parmvalue" id="parmvalue167946497717"><a name="parmvalue167946497717"></a><a name="parmvalue167946497717"></a><b>application/json;charset=utf8</b></span> in this field.</p>
    </td>
    </tr>
    <tr id="row3481201482919"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="p4121821192918"><a name="p4121821192918"></a><a name="p4121821192918"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.1.5.1.2 "><p id="p104841714152913"><a name="p104841714152913"></a><a name="p104841714152913"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.22%" headers="mcps1.1.5.1.3 "><p id="p1484171415293"><a name="p1484171415293"></a><a name="p1484171415293"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.42%" headers="mcps1.1.5.1.4 "><p id="p7188184217297"><a name="p7188184217297"></a><a name="p7188184217297"></a>Token that assigns the permissions of the <strong id="b42161544194"><a name="b42161544194"></a><a name="b42161544194"></a>Agent Operator</strong> policy to user B</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table178290313599"></a>
    <table><thead align="left"><tr id="row178294318597"><th class="cellrowborder" valign="top" width="21.272127212721273%" id="mcps1.1.5.1.1"><p id="p682963165915"><a name="p682963165915"></a><a name="p682963165915"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.92169216921692%" id="mcps1.1.5.1.2"><p id="p1482903105920"><a name="p1482903105920"></a><a name="p1482903105920"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.261726172617262%" id="mcps1.1.5.1.3"><p id="p18829183145920"><a name="p18829183145920"></a><a name="p18829183145920"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.54445444544455%" id="mcps1.1.5.1.4"><p id="p982911375918"><a name="p982911375918"></a><a name="p982911375918"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row820912912437"><td class="cellrowborder" valign="top" width="21.272127212721273%" headers="mcps1.1.5.1.1 "><p id="p117271323403"><a name="p117271323403"></a><a name="p117271323403"></a>identity</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.2 "><p id="p07279236010"><a name="p07279236010"></a><a name="p07279236010"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.1.5.1.3 "><p id="p1072715231201"><a name="p1072715231201"></a><a name="p1072715231201"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54445444544455%" headers="mcps1.1.5.1.4 "><p id="p12733551037"><a name="p12733551037"></a><a name="p12733551037"></a>Authentication parameters, including: <strong id="b13737404101"><a name="b13737404101"></a><a name="b13737404101"></a>methods</strong> and <strong id="b77378014105"><a name="b77378014105"></a><a name="b77378014105"></a>assume_role</strong>.</p>
    <pre class="screen" id="screen4242448102819"><a name="screen4242448102819"></a><a name="screen4242448102819"></a>"identity": {
          "methods": ["assume_role"],
          "assume_role": {</pre>
    </td>
    </tr>
    <tr id="row118480418431"><td class="cellrowborder" valign="top" width="21.272127212721273%" headers="mcps1.1.5.1.1 "><p id="p81848145559"><a name="p81848145559"></a><a name="p81848145559"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.2 "><p id="p19184101415559"><a name="p19184101415559"></a><a name="p19184101415559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.1.5.1.3 "><p id="p8184131410553"><a name="p8184131410553"></a><a name="p8184131410553"></a>String Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54445444544455%" headers="mcps1.1.5.1.4 "><p id="p101851414175513"><a name="p101851414175513"></a><a name="p101851414175513"></a>Method for obtaining the token. Set this field to <strong id="b97361113191114"><a name="b97361113191114"></a><a name="b97361113191114"></a>assume_role</strong>.</p>
    </td>
    </tr>
    <tr id="row2315147387"><td class="cellrowborder" valign="top" width="21.272127212721273%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0056596910_p4770553481"><a name="en-us_topic_0056596910_p4770553481"></a><a name="en-us_topic_0056596910_p4770553481"></a>domain_name or domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0056596910_p97709531782"><a name="en-us_topic_0056596910_p97709531782"></a><a name="en-us_topic_0056596910_p97709531782"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0056596910_p07709531487"><a name="en-us_topic_0056596910_p07709531487"></a><a name="en-us_topic_0056596910_p07709531487"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54445444544455%" headers="mcps1.1.5.1.4 "><p id="a7d17f5dc348644e4a0356f6229a75ad4"><a name="a7d17f5dc348644e4a0356f6229a75ad4"></a><a name="a7d17f5dc348644e4a0356f6229a75ad4"></a>Domain name or domain ID of the delegating party A. Specify either <strong id="b177846217121"><a name="b177846217121"></a><a name="b177846217121"></a>domain_name</strong> or <strong id="b179995286123"><a name="b179995286123"></a><a name="b179995286123"></a>domain_id</strong>.</p>
    </td>
    </tr>
    <tr id="row983018318592"><td class="cellrowborder" valign="top" width="21.272127212721273%" headers="mcps1.1.5.1.1 "><p id="p883010311590"><a name="p883010311590"></a><a name="p883010311590"></a>xrole_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.2 "><p id="p1783014355918"><a name="p1783014355918"></a><a name="p1783014355918"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.1.5.1.3 "><p id="p583020375917"><a name="p583020375917"></a><a name="p583020375917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54445444544455%" headers="mcps1.1.5.1.4 "><p id="p19830834595"><a name="p19830834595"></a><a name="p19830834595"></a>Name of the agency created by A</p>
    </td>
    </tr>
    <tr id="row1283411395912"><td class="cellrowborder" valign="top" width="21.272127212721273%" headers="mcps1.1.5.1.1 "><p id="p5835133175915"><a name="p5835133175915"></a><a name="p5835133175915"></a>scope</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.2 "><p id="p14835338590"><a name="p14835338590"></a><a name="p14835338590"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.1.5.1.3 "><p id="p5835113195919"><a name="p5835113195919"></a><a name="p5835113195919"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54445444544455%" headers="mcps1.1.5.1.4 "><p id="p154910141527"><a name="p154910141527"></a><a name="p154910141527"></a>Usage scope of the token. The value can be <strong id="b167587433149"><a name="b167587433149"></a><a name="b167587433149"></a>project</strong> or <strong id="b4759124319146"><a name="b4759124319146"></a><a name="b4759124319146"></a>domain</strong>.</p>
    <a name="ul13491314628"></a><a name="ul13491314628"></a><ul id="ul13491314628"><li>If this field is set to <strong id="b1829114901411"><a name="b1829114901411"></a><a name="b1829114901411"></a>project</strong>, the token can only be used to access resources in the project of a specified ID or name.<pre class="screen" id="screen174911147216"><a name="screen174911147216"></a><a name="screen174911147216"></a>"scope": {
          "project": {
          "id": "0b95b78b67fa045b38104c12fb..."
          }
        }</pre>
    </li><li>If this field is set to <strong id="b1577485791411"><a name="b1577485791411"></a><a name="b1577485791411"></a>domain</strong>, the token can be used to access all resources under the domain of a specified ID or name.<pre class="screen" id="screen4501614421"><a name="screen4501614421"></a><a name="screen4501614421"></a>"scope": {
          "domain": {
          "id": "6b8eb224c76842e3ac2..."
          }
        }</pre>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    The following is a sample request for obtaining an agency token for  **domain A**. The name of the agency is  **agencytest**.

    ```
    {
        "auth":{
            "identity":{
                "methods":[
                    "assume_role"
                ],
                "assume_role":{
                    "domain_name":"domain A",
                    "xrole_name":"agencytest"
                    }
    
                }
            },
            "scope":{
                "domain":{
                    "name":"domain A"
                }
            }
    }
    ```


## Response<a name="s3a08e13bb5b34dc2ba4dcd84a0d51cf5"></a>

-   Response header parameter description

    <a name="en-us_topic_0026585112_table44962972"></a>
    <table><thead align="left"><tr id="en-us_topic_0026585112_row49143529"><th class="cellrowborder" valign="top" width="21.22%" id="mcps1.1.5.1.1"><p id="en-us_topic_0026585112_p21202951"><a name="en-us_topic_0026585112_p21202951"></a><a name="en-us_topic_0026585112_p21202951"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.78%" id="mcps1.1.5.1.2"><p id="p862619429218"><a name="p862619429218"></a><a name="p862619429218"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.1.5.1.3"><p id="en-us_topic_0026585112_p39717481"><a name="en-us_topic_0026585112_p39717481"></a><a name="en-us_topic_0026585112_p39717481"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.879999999999995%" id="mcps1.1.5.1.4"><p id="en-us_topic_0026585112_p62999416"><a name="en-us_topic_0026585112_p62999416"></a><a name="en-us_topic_0026585112_p62999416"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0026585112_row2679067"><td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0026585112_p15677883"><a name="en-us_topic_0026585112_p15677883"></a><a name="en-us_topic_0026585112_p15677883"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.78%" headers="mcps1.1.5.1.2 "><p id="p9626642329"><a name="p9626642329"></a><a name="p9626642329"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0026585112_p61948991"><a name="en-us_topic_0026585112_p61948991"></a><a name="en-us_topic_0026585112_p61948991"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.879999999999995%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585112_p51812368"><a name="en-us_topic_0026585112_p51812368"></a><a name="en-us_topic_0026585112_p51812368"></a>Agency token that is obtained</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Token format description

    <a name="t9aa18688b0f44302a45f87a865a4f9d7"></a>
    <table><thead align="left"><tr id="r4495c7bbf2c14d50a55a4ac402e189ca"><th class="cellrowborder" valign="top" width="21.26787321267873%" id="mcps1.1.5.1.1"><p id="a604782cae932448db4a5fe6032c0703e"><a name="a604782cae932448db4a5fe6032c0703e"></a><a name="a604782cae932448db4a5fe6032c0703e"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.728327167283272%" id="mcps1.1.5.1.2"><p id="a6175c8a318d24e39837027e182baaed9"><a name="a6175c8a318d24e39837027e182baaed9"></a><a name="a6175c8a318d24e39837027e182baaed9"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.24827517248275%" id="mcps1.1.5.1.3"><p id="a8ed9dc140ab940ae83066efac4a62450"><a name="a8ed9dc140ab940ae83066efac4a62450"></a><a name="a8ed9dc140ab940ae83066efac4a62450"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.755524447555246%" id="mcps1.1.5.1.4"><p id="a7926893fadf64b0cba9adac5489deefd"><a name="a7926893fadf64b0cba9adac5489deefd"></a><a name="a7926893fadf64b0cba9adac5489deefd"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rcc2f2253b42941d3976e9118b7899178"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="a07a6ef85698e438b842d000b6bcbb235"><a name="a07a6ef85698e438b842d000b6bcbb235"></a><a name="a07a6ef85698e438b842d000b6bcbb235"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="ab83556a39c894a0983c94c05bbe8a92d"><a name="ab83556a39c894a0983c94c05bbe8a92d"></a><a name="ab83556a39c894a0983c94c05bbe8a92d"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="a558b3430e0444f97a88d96cdc036401e"><a name="a558b3430e0444f97a88d96cdc036401e"></a><a name="a558b3430e0444f97a88d96cdc036401e"></a>Json Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="a7b9d6f974d1e4d44890be49309a0382f"><a name="a7b9d6f974d1e4d44890be49309a0382f"></a><a name="a7b9d6f974d1e4d44890be49309a0382f"></a>Method for obtaining the token</p>
    </td>
    </tr>
    <tr id="r952955421b3345d29a03350797976bef"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="aec3770aaf9384235aed7d5a3e9b61d34"><a name="aec3770aaf9384235aed7d5a3e9b61d34"></a><a name="aec3770aaf9384235aed7d5a3e9b61d34"></a>expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="a2d5989348dcc4c34ab87e762205e3e25"><a name="a2d5989348dcc4c34ab87e762205e3e25"></a><a name="a2d5989348dcc4c34ab87e762205e3e25"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="a06df05908d2046d6b318f3dbadcad5fa"><a name="a06df05908d2046d6b318f3dbadcad5fa"></a><a name="a06df05908d2046d6b318f3dbadcad5fa"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="af0c635100ad74b489f89c886e157e49b"><a name="af0c635100ad74b489f89c886e157e49b"></a><a name="af0c635100ad74b489f89c886e157e49b"></a>Expiration date of the token</p>
    </td>
    </tr>
    <tr id="r566af79660784b49a20126aeb8226599"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="a99ee5815381b446bab5b3b871f0cd77f"><a name="a99ee5815381b446bab5b3b871f0cd77f"></a><a name="a99ee5815381b446bab5b3b871f0cd77f"></a>issued_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="aa7051ea6df594043a3d18cfbdfb49dc8"><a name="aa7051ea6df594043a3d18cfbdfb49dc8"></a><a name="aa7051ea6df594043a3d18cfbdfb49dc8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="af1aa454ebf634d428c9498bb88dd9d45"><a name="af1aa454ebf634d428c9498bb88dd9d45"></a><a name="af1aa454ebf634d428c9498bb88dd9d45"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585112_p532161155713"><a name="en-us_topic_0026585112_p532161155713"></a><a name="en-us_topic_0026585112_p532161155713"></a>Time when the token was issued</p>
    </td>
    </tr>
    <tr id="r2bdea9cf4b4a40ea89733ee4ff3af64a"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="a313ab3f0623c4e57a9160a072e6a22c9"><a name="a313ab3f0623c4e57a9160a072e6a22c9"></a><a name="a313ab3f0623c4e57a9160a072e6a22c9"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="a87695b24819042c8afa89bf8867ebdf5"><a name="a87695b24819042c8afa89bf8867ebdf5"></a><a name="a87695b24819042c8afa89bf8867ebdf5"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="a27424032f78a40379dddacb5ab25166d"><a name="a27424032f78a40379dddacb5ab25166d"></a><a name="a27424032f78a40379dddacb5ab25166d"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="a220a5e088be14830a1e9db57ad7e9d50"><a name="a220a5e088be14830a1e9db57ad7e9d50"></a><a name="a220a5e088be14830a1e9db57ad7e9d50"></a>Detailed information about the delegating party. Example:</p>
    <pre class="screen" id="s94858990e5764505971cc869331632fc"><a name="s94858990e5764505971cc869331632fc"></a><a name="s94858990e5764505971cc869331632fc"></a>"user": { 
          "name": "<em id="i6335101061711"><a name="i6335101061711"></a><a name="i6335101061711"></a>user A</em>", 
          "id": "<em id="en-us_topic_0026585112_i433336816519"><a name="en-us_topic_0026585112_i433336816519"></a><a name="en-us_topic_0026585112_i433336816519"></a>userid</em>", 
          "password_expires_at":"2016-11-06T15:32:17.000000",
          "domain": { 
             "name": "<em id="en-us_topic_0026585112_i438354691645"><a name="en-us_topic_0026585112_i438354691645"></a><a name="en-us_topic_0026585112_i438354691645"></a>domain A</em>",
             "id": "<em id="en-us_topic_0026585112_i75268851664"><a name="en-us_topic_0026585112_i75268851664"></a><a name="en-us_topic_0026585112_i75268851664"></a>domainid</em>"
           } 
        }</pre>
    <a name="ul1414311427419"></a><a name="ul1414311427419"></a><ul id="ul1414311427419"><li><strong id="b119112038305"><a name="b119112038305"></a><a name="b119112038305"></a>user.name</strong>: Username of the delegating party</li><li><strong id="b57021753016"><a name="b57021753016"></a><a name="b57021753016"></a>user.id</strong>: User ID of the delegating party</li><li><strong id="b1601225133018"><a name="b1601225133018"></a><a name="b1601225133018"></a>domain.name</strong>: Name of the domain to which the delegating party belongs</li><li><strong id="b1889119340342"><a name="b1889119340342"></a><a name="b1889119340342"></a>domain.id</strong>: ID of the domain</li><li><strong id="b842352706101836"><a name="b842352706101836"></a><a name="b842352706101836"></a>password_expires_at</strong>: Time when the password will expire. <strong id="b84235270616517"><a name="b84235270616517"></a><a name="b84235270616517"></a>null</strong> indicates that the password will not expire. This parameter is optional.</li></ul>
    </td>
    </tr>
    <tr id="rd33372d927214527ac870bb11715c536"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="a66272c967cb547c09f7a7316b4ae754c"><a name="a66272c967cb547c09f7a7316b4ae754c"></a><a name="a66272c967cb547c09f7a7316b4ae754c"></a>domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="a9183943cbe59479691b60e9c95a74a0d"><a name="a9183943cbe59479691b60e9c95a74a0d"></a><a name="a9183943cbe59479691b60e9c95a74a0d"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="a06d0695f36184007ab70f95018c90a92"><a name="a06d0695f36184007ab70f95018c90a92"></a><a name="a06d0695f36184007ab70f95018c90a92"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="p1963811012015"><a name="p1963811012015"></a><a name="p1963811012015"></a>This parameter is returned only when the <strong id="b17393161915404"><a name="b17393161915404"></a><a name="b17393161915404"></a>scope</strong> parameter in the request body is set to <strong id="b43954198404"><a name="b43954198404"></a><a name="b43954198404"></a>domain</strong>.</p>
    <p id="a4a60927497a74911bd2ab640524d9633"><a name="a4a60927497a74911bd2ab640524d9633"></a><a name="a4a60927497a74911bd2ab640524d9633"></a>Example:</p>
    <pre class="screen" id="s6426dc53b2a4457ea51cc7ea9e64f456"><a name="s6426dc53b2a4457ea51cc7ea9e64f456"></a><a name="s6426dc53b2a4457ea51cc7ea9e64f456"></a>"domain": { 
          "name" : "<em id="i73871258304"><a name="i73871258304"></a><a name="i73871258304"></a>domain A</em>",     
          "id" : "<em id="i17061511305"><a name="i17061511305"></a><a name="i17061511305"></a>domainid</em>"
    }</pre>
    <a name="ul1274024713413"></a><a name="ul1274024713413"></a><ul id="ul1274024713413"><li><strong id="b27211127154019"><a name="b27211127154019"></a><a name="b27211127154019"></a>domain.name</strong>: Name of the domain to which the delegating party belongs</li><li><strong id="b5232123414011"><a name="b5232123414011"></a><a name="b5232123414011"></a>domain.id</strong>: ID of the domain</li></ul>
    </td>
    </tr>
    <tr id="r3a914bf0c52c43e390883648cbe964ff"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="a0e6de929a1ea4db0b88e97acb4287d5e"><a name="a0e6de929a1ea4db0b88e97acb4287d5e"></a><a name="a0e6de929a1ea4db0b88e97acb4287d5e"></a>project</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="a346f8467c2e24793ab55c120fc37852f"><a name="a346f8467c2e24793ab55c120fc37852f"></a><a name="a346f8467c2e24793ab55c120fc37852f"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="af6953054960f4c59903b92961b10b426"><a name="af6953054960f4c59903b92961b10b426"></a><a name="af6953054960f4c59903b92961b10b426"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="a41001b564477400f98aef711e86f0197"><a name="a41001b564477400f98aef711e86f0197"></a><a name="a41001b564477400f98aef711e86f0197"></a>This parameter is returned only when the <strong id="b3554133784015"><a name="b3554133784015"></a><a name="b3554133784015"></a>scope</strong> parameter in the request body is set to <strong id="b195571937184017"><a name="b195571937184017"></a><a name="b195571937184017"></a>project</strong>.</p>
    <p id="a2658c45981e64570b63c49c45cfdfac7"><a name="a2658c45981e64570b63c49c45cfdfac7"></a><a name="a2658c45981e64570b63c49c45cfdfac7"></a>Example:</p>
    <pre class="screen" id="s75cd01f2f3df45ada904958dc41f5307"><a name="s75cd01f2f3df45ada904958dc41f5307"></a><a name="s75cd01f2f3df45ada904958dc41f5307"></a>"project": { 
          "name": "<em id="af63ef597e10344ecaada944624eefa21"><a name="af63ef597e10344ecaada944624eefa21"></a><a name="af63ef597e10344ecaada944624eefa21"></a>projectname</em>", 
          "id": "<em id="en-us_topic_0026585112_i86520761696"><a name="en-us_topic_0026585112_i86520761696"></a><a name="en-us_topic_0026585112_i86520761696"></a>projectid</em>"
    }</pre>
    <a name="ul86769381572"></a><a name="ul86769381572"></a><ul id="ul86769381572"><li><strong id="b154981843154020"><a name="b154981843154020"></a><a name="b154981843154020"></a>project.name</strong>: Name of a project</li><li><strong id="b16203154584012"><a name="b16203154584012"></a><a name="b16203154584012"></a>project.id</strong>: ID of the project</li></ul>
    </td>
    </tr>
    <tr id="row31009604113628"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="p22717013113628"><a name="p22717013113628"></a><a name="p22717013113628"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="p54936595113628"><a name="p54936595113628"></a><a name="p54936595113628"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="p46529556113628"><a name="p46529556113628"></a><a name="p46529556113628"></a>Json Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="p45368001113628"><a name="p45368001113628"></a><a name="p45368001113628"></a>Endpoint information</p>
    <p id="p50787600113939"><a name="p50787600113939"></a><a name="p50787600113939"></a>Example:</p>
    <pre class="screen" id="screen17568328113914"><a name="screen17568328113914"></a><a name="screen17568328113914"></a>"catalog": [{
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
    </td>
    </tr>
    <tr id="r57913d5a1da24c699a412dced6a7b573"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="a45bd202186b249bfa8fc87bbcbf05bb9"><a name="a45bd202186b249bfa8fc87bbcbf05bb9"></a><a name="a45bd202186b249bfa8fc87bbcbf05bb9"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="ae5cf82a55c21452aa028ff59e6973404"><a name="ae5cf82a55c21452aa028ff59e6973404"></a><a name="ae5cf82a55c21452aa028ff59e6973404"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="aa1fb3d35fbda45208e6e58dbbbc00b01"><a name="aa1fb3d35fbda45208e6e58dbbbc00b01"></a><a name="aa1fb3d35fbda45208e6e58dbbbc00b01"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="a18bf24a442094153ab2a8f7391737d06"><a name="a18bf24a442094153ab2a8f7391737d06"></a><a name="a18bf24a442094153ab2a8f7391737d06"></a>Permissions information of the token</p>
    <p id="ace14d3d704ae4d41abdcfc9ae99def0f"><a name="ace14d3d704ae4d41abdcfc9ae99def0f"></a><a name="ace14d3d704ae4d41abdcfc9ae99def0f"></a>Example:</p>
    <pre class="screen" id="s71b72ebcaad84e58881c80352e028dff"><a name="s71b72ebcaad84e58881c80352e028dff"></a><a name="s71b72ebcaad84e58881c80352e028dff"></a>"roles" : [{ 
         "name" : "role1", 
         "id" : "roleid1" 
         }, { 
         "name" : "role2", 
         "id" : "roleid2" 
         } 
       ] </pre>
    </td>
    </tr>
    <tr id="row1930784083617"><td class="cellrowborder" valign="top" width="21.26787321267873%" headers="mcps1.1.5.1.1 "><p id="p3307174016361"><a name="p3307174016361"></a><a name="p3307174016361"></a>assumed_by</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.2 "><p id="p93071640163616"><a name="p93071640163616"></a><a name="p93071640163616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.1.5.1.3 "><p id="p16353154163614"><a name="p16353154163614"></a><a name="p16353154163614"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.755524447555246%" headers="mcps1.1.5.1.4 "><p id="p5760121404010"><a name="p5760121404010"></a><a name="p5760121404010"></a>Detailed information about the delegated party. Example:</p>
    <p id="p1855720205374"><a name="p1855720205374"></a><a name="p1855720205374"></a>Example:</p>
    <pre class="screen" id="screen171913204147"><a name="screen171913204147"></a><a name="screen171913204147"></a>"assumed_by": {
          "user": {
            "domain": {
              "name": "domain B",
              "id": "bfdd55e02a014894b5a2693f31..."
            },
            "name": "user B",
            "id": "ff5ea657f1dd45c4b8f398cab..."
          }
        }</pre>
    <a name="ul219615366138"></a><a name="ul219615366138"></a><ul id="ul219615366138"><li><strong id="b874418074515"><a name="b874418074515"></a><a name="b874418074515"></a>domain.name</strong>: Name of the domain to which the delegated party belongs</li><li><strong id="b1595117713458"><a name="b1595117713458"></a><a name="b1595117713458"></a>user.name</strong>: Username of the delegated party</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    Token information stored in the response header:
    X-Subject-Token:MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...
    
    X-Frame-Options: SAMEORIGIN
    
    Information included in the response body:
    {
      "token": {
        "methods": [
          "assume_role"
        ],
        "issued_at": "2017-05-18T11:44:05.232000Z",
        "expires_at": "2017-05-19T11:44:05.232000Z",
        "user": {
          "id": "93e12ecdad6f4abd84968741da...",
          "name": "user A/agencytest",
          "password_expires_at":"2016-11-06T15:32:17.000000",
          "domain": {
            "id": "ce925c42c25943bebba10ea64a...",
            "name": "domain A"
          }
        },
        "domain": {
          "id": "ce925c42c25943bebba10ea64a...",
          "name": "domain A"
        },
        "roles": [
          {
            "id": "c11c61319f08404eaf94f8030b9...",
            "name": "role1"
          },
          {
            "id": "d52dde35ijg62fex2ijhdc785sc3...",
            "name": "role2"
          },
          {
            "id": "d862dwd32dwhu854rdcs447ed1d7..."
            "name": "op_gated_tasssg6"
          }
        ],
        "assumed_by": {
          "user": {
            "domain": {
              "name": "domain B",
              "id": "c1a78a82d81c4a19b03bfe82d3ad..."
            },
            "id": "cdeb158dda854cc3bab77d8926ff...",
            "name": "User B"
          }
        }
      }
    }
    ```


## Status Codes<a name="sbfe93ca4c2b9427dbb2218a4e72da6a8"></a>

<a name="en-us_topic_0026585112_table34550710"></a>
<table><thead align="left"><tr id="en-us_topic_0026585112_row8352109"><th class="cellrowborder" valign="top" width="50.029999999999994%" id="mcps1.1.3.1.1"><p id="en-us_topic_0026585112_p5432205"><a name="en-us_topic_0026585112_p5432205"></a><a name="en-us_topic_0026585112_p5432205"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="49.97%" id="mcps1.1.3.1.2"><p id="en-us_topic_0026585112_p37355470"><a name="en-us_topic_0026585112_p37355470"></a><a name="en-us_topic_0026585112_p37355470"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0026585112_row5894231"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p7670737"><a name="en-us_topic_0026585112_p7670737"></a><a name="en-us_topic_0026585112_p7670737"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p17349988"><a name="en-us_topic_0026585112_p17349988"></a><a name="en-us_topic_0026585112_p17349988"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0026585112_row21932166"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p31674992"><a name="en-us_topic_0026585112_p31674992"></a><a name="en-us_topic_0026585112_p31674992"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p15537542"><a name="en-us_topic_0026585112_p15537542"></a><a name="en-us_topic_0026585112_p15537542"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="r22bf632ff3984ffbaa2734a029063cfb"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p947606916650"><a name="en-us_topic_0026585112_p947606916650"></a><a name="en-us_topic_0026585112_p947606916650"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="a3a62e2f9d6c84b4083dfb8b2ade8e14c"><a name="a3a62e2f9d6c84b4083dfb8b2ade8e14c"></a><a name="a3a62e2f9d6c84b4083dfb8b2ade8e14c"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="r41d0d854619349f898c16f7c61792083"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p762821816657"><a name="en-us_topic_0026585112_p762821816657"></a><a name="en-us_topic_0026585112_p762821816657"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="a0261fc1955104ca3b1f0a46388724624"><a name="a0261fc1955104ca3b1f0a46388724624"></a><a name="a0261fc1955104ca3b1f0a46388724624"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="rea66e1a745ee4e0882be6b9f5349ac4d"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p486971841676"><a name="en-us_topic_0026585112_p486971841676"></a><a name="en-us_topic_0026585112_p486971841676"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p521578261676"><a name="en-us_topic_0026585112_p521578261676"></a><a name="en-us_topic_0026585112_p521578261676"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="r230ba1b5ddec4cd0a41a5c37806e60f5"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="af8f4513c90d344e3b90952b53e3ee015"><a name="af8f4513c90d344e3b90952b53e3ee015"></a><a name="af8f4513c90d344e3b90952b53e3ee015"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="a19c27fd6b377464898ec6cae5778ec80"><a name="a19c27fd6b377464898ec6cae5778ec80"></a><a name="a19c27fd6b377464898ec6cae5778ec80"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="en-us_topic_0026585112_row6824316711"><td class="cellrowborder" valign="top" width="50.029999999999994%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p61418816711"><a name="en-us_topic_0026585112_p61418816711"></a><a name="en-us_topic_0026585112_p61418816711"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.3.1.2 "><p id="a4bc003bda05e465eb3a3f0f989888213"><a name="a4bc003bda05e465eb3a3f0f989888213"></a><a name="a4bc003bda05e465eb3a3f0f989888213"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

