# Obtaining a User Token<a name="en-us_topic_0057845583"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to obtain a token through username/password authentication. A token is a system object encapsulating the identity and permissions of a user. When calling the APIs of IAM or other cloud services, you can use this interface to obtain a token for authentication.

>![](/images/icon-note.gif) **NOTE:**   
>The validity period of a token is 24 hours. If you want to use a token for authentication, cache it to avoid frequently calling the IAM API.  

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

URI format

POST /v3/auth/tokens

## Request<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="17.818218178182182%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.568243175682433%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.108189181081894%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.5053494650535%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="17.818218178182182%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.568243175682433%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.108189181081894%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.5053494650535%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <span class="parmvalue" id="parmvalue17621591774"><a name="parmvalue17621591774"></a><a name="parmvalue17621591774"></a><b>application/json;charset=utf8</b></span> in this field.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table1472672314012"></a>
    <table><thead align="left"><tr id="row372613231901"><th class="cellrowborder" valign="top" width="18.04%" id="mcps1.1.5.1.1"><p id="p127271523609"><a name="p127271523609"></a><a name="p127271523609"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.51%" id="mcps1.1.5.1.2"><p id="p10727523607"><a name="p10727523607"></a><a name="p10727523607"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.07%" id="mcps1.1.5.1.3"><p id="p672717232020"><a name="p672717232020"></a><a name="p672717232020"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.379999999999995%" id="mcps1.1.5.1.4"><p id="p4727142310020"><a name="p4727142310020"></a><a name="p4727142310020"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row117274231708"><td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.1 "><p id="p117271323403"><a name="p117271323403"></a><a name="p117271323403"></a>identity</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.2 "><p id="p07279236010"><a name="p07279236010"></a><a name="p07279236010"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p1072715231201"><a name="p1072715231201"></a><a name="p1072715231201"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p12733551037"><a name="p12733551037"></a><a name="p12733551037"></a>Authentication parameters, including: <strong id="b1092964216403"><a name="b1092964216403"></a><a name="b1092964216403"></a>methods</strong> and <strong id="b3319240124015"><a name="b3319240124015"></a><a name="b3319240124015"></a>password</strong>.</p>
    <pre class="screen" id="screen4242448102819"><a name="screen4242448102819"></a><a name="screen4242448102819"></a>"identity": {
          "methods": ["password"],
          "password": {</pre>
    </td>
    </tr>
    <tr id="row14766951175411"><td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.1 "><p id="p81848145559"><a name="p81848145559"></a><a name="p81848145559"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.2 "><p id="p19184101415559"><a name="p19184101415559"></a><a name="p19184101415559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p8184131410553"><a name="p8184131410553"></a><a name="p8184131410553"></a>String Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p101851414175513"><a name="p101851414175513"></a><a name="p101851414175513"></a>Authentication method. The value of this field is <strong id="b144441101418"><a name="b144441101418"></a><a name="b144441101418"></a>password</strong>. If virtual MFA–based login authentication is enabled, the value of this field is <strong id="b227184080213039"><a name="b227184080213039"></a><a name="b227184080213039"></a>["password","totp"]</strong>.</p>
    </td>
    </tr>
    <tr id="row102161954175410"><td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.1 "><p id="p31853141551"><a name="p31853141551"></a><a name="p31853141551"></a>password</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.2 "><p id="p41851214175516"><a name="p41851214175516"></a><a name="p41851214175516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p6185514205514"><a name="p6185514205514"></a><a name="p6185514205514"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p171859142556"><a name="p171859142556"></a><a name="p171859142556"></a>Authentication information. Example:</p>
    <pre class="screen" id="screen19185191413550"><a name="screen19185191413550"></a><a name="screen19185191413550"></a>"password": {
            "user": {
              "name": "<em id="i43811531261"><a name="i43811531261"></a><a name="i43811531261"></a>user A</em>",
              "password": "<em id="i1233817361"><a name="i1233817361"></a><a name="i1233817361"></a>**********</em>",
              "domain": {
                "name": "<em id="i33810151372"><a name="i33810151372"></a><a name="i33810151372"></a>domain A</em>"</pre>
    <a name="ul2147135719418"></a><a name="ul2147135719418"></a><ul id="ul2147135719418"><li><strong id="b1749944084213"><a name="b1749944084213"></a><a name="b1749944084213"></a>user.name</strong>: Name of the user that wants to obtain the token. Obtain the username on the <strong id="b0207101810433"><a name="b0207101810433"></a><a name="b0207101810433"></a>My Credentials</strong> page.</li><li><strong id="b181311636194319"><a name="b181311636194319"></a><a name="b181311636194319"></a>password</strong>: Login password of the user.</li><li><strong id="b15949115334320"><a name="b15949115334320"></a><a name="b15949115334320"></a>domain.name</strong>: Name of the domain that created the user. Obtain the domain name on the <strong id="b87551617445"><a name="b87551617445"></a><a name="b87551617445"></a>My Credentials</strong> page.</li></ul>
    </td>
    </tr>
    <tr id="row1135014915519"><td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.1 "><p id="p618618143556"><a name="p618618143556"></a><a name="p618618143556"></a>totp</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.2 "><p id="p1818641419559"><a name="p1818641419559"></a><a name="p1818641419559"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p618651417559"><a name="p618651417559"></a><a name="p618651417559"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p4186114115512"><a name="p4186114115512"></a><a name="p4186114115512"></a>Authentication information. This parameter is mandatory only when virtual MFA–based login authentication is enabled.</p>
    <p id="p10186414155519"><a name="p10186414155519"></a><a name="p10186414155519"></a>Example:</p>
    <pre class="screen" id="screen01571135184615"><a name="screen01571135184615"></a><a name="screen01571135184615"></a>"totp": {
            "user": {
              "id": "b95b78b67fa045b38104c12fb...",
              "passcode": "******"</pre>
    <a name="ul85041943518"></a><a name="ul85041943518"></a><ul id="ul85041943518"><li><strong id="b139021043194611"><a name="b139021043194611"></a><a name="b139021043194611"></a>user.id</strong>: User ID, which can be obtained on the <strong id="b8821233194619"><a name="b8821233194619"></a><a name="b8821233194619"></a>My Credentials</strong> page.</li><li><strong id="b11809102184814"><a name="b11809102184814"></a><a name="b11809102184814"></a>passcode</strong>: Virtual MFA device verification code, which can be obtained on the MFA app.</li></ul>
    </td>
    </tr>
    <tr id="row77278232020"><td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.1 "><p id="p124182557111"><a name="p124182557111"></a><a name="p124182557111"></a>scope</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.2 "><p id="p144209551918"><a name="p144209551918"></a><a name="p144209551918"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p144236557120"><a name="p144236557120"></a><a name="p144236557120"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p8397345145417"><a name="p8397345145417"></a><a name="p8397345145417"></a>Usage scope of the token. The value can be <strong id="b03311514506"><a name="b03311514506"></a><a name="b03311514506"></a>project</strong> or <strong id="b466092125010"><a name="b466092125010"></a><a name="b466092125010"></a>domain</strong>.</p>
    <a name="ul32091543195912"></a><a name="ul32091543195912"></a><ul id="ul32091543195912"><li>If this field is set to <strong id="b36701747175113"><a name="b36701747175113"></a><a name="b36701747175113"></a>project</strong>, the token can only be used to access resources in the project of a specified ID or name.<pre class="screen" id="screen842664845912"><a name="screen842664845912"></a><a name="screen842664845912"></a>"scope": {
          "project": {
          "id": "0b95b78b67fa045b38104c12fb..."
          }
        }</pre>
    </li><li>If this field is set to <strong id="b14284532115213"><a name="b14284532115213"></a><a name="b14284532115213"></a>domain</strong>, the token can be used to access all resources under the domain of a specified ID or name.<pre class="screen" id="screen59171740125811"><a name="screen59171740125811"></a><a name="screen59171740125811"></a>"scope": {
          "domain": {
          "name": " domain A"
          }
        }</pre>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    The following is a sample request for obtaining a token for  **user A**. The login password of the user is  **\*\*\*\*\*\*\*\*\*\***  and the domain name is  **domain A**. The scope of the token is  **domain**.

    ```
    {
      "auth": {
        "identity": {
          "methods": ["password"],
          "password": {
            "user": {
              "name": "user A",
              "password": "**********",
              "domain": {
                "name": "domain A"
              }
            }
          }
        },
        "scope": {
          "domain": {
            "name": "domain A"
          }
        }
      }
    }
    ```

    The following is a sample request for obtaining a token when virtual MFA–based login authentication is enabled.

    ```
    {
    	"auth": {
    		"identity": {
    			"methods": ["password", "totp"],
    			"password": {
    				"user": {
    					"name": "user A",
    					"password": "********",
    					"domain": {
    						"name": "domain A"
    					}
    				}
    			},
    			"totp" : {
    				"user": {
    					"id": "dfsafdfsaf....",
    					"passcode": "******"
    				}
    			}
    		},
    		"scope": {
    			"domain": {
    				"name": "domain A"
    			}
    		}
    	}
    }
    ```


## Response<a name="s3a08e13bb5b34dc2ba4dcd84a0d51cf5"></a>

-   Response header parameter description

    <a name="en-us_topic_0026585112_table44962972"></a>
    <table><thead align="left"><tr id="en-us_topic_0026585112_row49143529"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.1"><p id="en-us_topic_0026585112_p21202951"><a name="en-us_topic_0026585112_p21202951"></a><a name="en-us_topic_0026585112_p21202951"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.759999999999998%" id="mcps1.1.5.1.2"><p id="p1354817920213"><a name="p1354817920213"></a><a name="p1354817920213"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.1.5.1.3"><p id="en-us_topic_0026585112_p39717481"><a name="en-us_topic_0026585112_p39717481"></a><a name="en-us_topic_0026585112_p39717481"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.18%" id="mcps1.1.5.1.4"><p id="en-us_topic_0026585112_p62999416"><a name="en-us_topic_0026585112_p62999416"></a><a name="en-us_topic_0026585112_p62999416"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0026585112_row2679067"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0026585112_p15677883"><a name="en-us_topic_0026585112_p15677883"></a><a name="en-us_topic_0026585112_p15677883"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.1.5.1.2 "><p id="p954817912217"><a name="p954817912217"></a><a name="p954817912217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0026585112_p61948991"><a name="en-us_topic_0026585112_p61948991"></a><a name="en-us_topic_0026585112_p61948991"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.18%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585112_p51812368"><a name="en-us_topic_0026585112_p51812368"></a><a name="en-us_topic_0026585112_p51812368"></a>Obtained token</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Token format description

    <a name="t9aa18688b0f44302a45f87a865a4f9d7"></a>
    <table><thead align="left"><tr id="r4495c7bbf2c14d50a55a4ac402e189ca"><th class="cellrowborder" valign="top" width="22.06220622062206%" id="mcps1.1.5.1.1"><p id="a604782cae932448db4a5fe6032c0703e"><a name="a604782cae932448db4a5fe6032c0703e"></a><a name="a604782cae932448db4a5fe6032c0703e"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.01200120012001%" id="mcps1.1.5.1.2"><p id="a6175c8a318d24e39837027e182baaed9"><a name="a6175c8a318d24e39837027e182baaed9"></a><a name="a6175c8a318d24e39837027e182baaed9"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.711771177117715%" id="mcps1.1.5.1.3"><p id="a8ed9dc140ab940ae83066efac4a62450"><a name="a8ed9dc140ab940ae83066efac4a62450"></a><a name="a8ed9dc140ab940ae83066efac4a62450"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.21402140214022%" id="mcps1.1.5.1.4"><p id="a7926893fadf64b0cba9adac5489deefd"><a name="a7926893fadf64b0cba9adac5489deefd"></a><a name="a7926893fadf64b0cba9adac5489deefd"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rcc2f2253b42941d3976e9118b7899178"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="a07a6ef85698e438b842d000b6bcbb235"><a name="a07a6ef85698e438b842d000b6bcbb235"></a><a name="a07a6ef85698e438b842d000b6bcbb235"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="ab83556a39c894a0983c94c05bbe8a92d"><a name="ab83556a39c894a0983c94c05bbe8a92d"></a><a name="ab83556a39c894a0983c94c05bbe8a92d"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="a558b3430e0444f97a88d96cdc036401e"><a name="a558b3430e0444f97a88d96cdc036401e"></a><a name="a558b3430e0444f97a88d96cdc036401e"></a>Json Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="a7b9d6f974d1e4d44890be49309a0382f"><a name="a7b9d6f974d1e4d44890be49309a0382f"></a><a name="a7b9d6f974d1e4d44890be49309a0382f"></a>Method for obtaining a token</p>
    </td>
    </tr>
    <tr id="r952955421b3345d29a03350797976bef"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="aec3770aaf9384235aed7d5a3e9b61d34"><a name="aec3770aaf9384235aed7d5a3e9b61d34"></a><a name="aec3770aaf9384235aed7d5a3e9b61d34"></a>expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="a2d5989348dcc4c34ab87e762205e3e25"><a name="a2d5989348dcc4c34ab87e762205e3e25"></a><a name="a2d5989348dcc4c34ab87e762205e3e25"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="a06df05908d2046d6b318f3dbadcad5fa"><a name="a06df05908d2046d6b318f3dbadcad5fa"></a><a name="a06df05908d2046d6b318f3dbadcad5fa"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="af0c635100ad74b489f89c886e157e49b"><a name="af0c635100ad74b489f89c886e157e49b"></a><a name="af0c635100ad74b489f89c886e157e49b"></a>Expiration date of the token</p>
    </td>
    </tr>
    <tr id="r566af79660784b49a20126aeb8226599"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="a99ee5815381b446bab5b3b871f0cd77f"><a name="a99ee5815381b446bab5b3b871f0cd77f"></a><a name="a99ee5815381b446bab5b3b871f0cd77f"></a>issued_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="aa7051ea6df594043a3d18cfbdfb49dc8"><a name="aa7051ea6df594043a3d18cfbdfb49dc8"></a><a name="aa7051ea6df594043a3d18cfbdfb49dc8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="af1aa454ebf634d428c9498bb88dd9d45"><a name="af1aa454ebf634d428c9498bb88dd9d45"></a><a name="af1aa454ebf634d428c9498bb88dd9d45"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585112_p532161155713"><a name="en-us_topic_0026585112_p532161155713"></a><a name="en-us_topic_0026585112_p532161155713"></a>Time when the token was issued</p>
    </td>
    </tr>
    <tr id="r2bdea9cf4b4a40ea89733ee4ff3af64a"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="a313ab3f0623c4e57a9160a072e6a22c9"><a name="a313ab3f0623c4e57a9160a072e6a22c9"></a><a name="a313ab3f0623c4e57a9160a072e6a22c9"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="a87695b24819042c8afa89bf8867ebdf5"><a name="a87695b24819042c8afa89bf8867ebdf5"></a><a name="a87695b24819042c8afa89bf8867ebdf5"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="a27424032f78a40379dddacb5ab25166d"><a name="a27424032f78a40379dddacb5ab25166d"></a><a name="a27424032f78a40379dddacb5ab25166d"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="a220a5e088be14830a1e9db57ad7e9d50"><a name="a220a5e088be14830a1e9db57ad7e9d50"></a><a name="a220a5e088be14830a1e9db57ad7e9d50"></a>Example:</p>
    <pre class="screen" id="s94858990e5764505971cc869331632fc"><a name="s94858990e5764505971cc869331632fc"></a><a name="s94858990e5764505971cc869331632fc"></a>"user": { 
          "name": "user A", 
          "id": "b95b78b67fa045b38104...", 
          "password_expires_at":"2016-11-06T15:32:17.000000",
          "domain": { 
             "name": "domain A",
             "id": "fdec73ffea524aa1b373e40..."
           } 
        }</pre>
    <a name="ul10538192315141"></a><a name="ul10538192315141"></a><ul id="ul10538192315141"><li><strong id="b1364916619591"><a name="b1364916619591"></a><a name="b1364916619591"></a>user.name</strong>: Name of the user that wants to obtain the token</li><li><strong id="b7680648115912"><a name="b7680648115912"></a><a name="b7680648115912"></a>user.id</strong>: ID of the user</li><li><strong id="b12342155618598"><a name="b12342155618598"></a><a name="b12342155618598"></a>domain.name</strong>: Name of the domain that created the user</li><li><strong id="b25431719204"><a name="b25431719204"></a><a name="b25431719204"></a>domain.id</strong>: ID of the domain</li><li><strong id="b1275313386016"><a name="b1275313386016"></a><a name="b1275313386016"></a>password_expires_at</strong>: Coordinated Universal Time (UTC) that the password will expire. <strong id="b1483686226114627"><a name="b1483686226114627"></a><a name="b1483686226114627"></a>null</strong> indicates that the password will not expire.</li></ul>
    </td>
    </tr>
    <tr id="rd33372d927214527ac870bb11715c536"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="a66272c967cb547c09f7a7316b4ae754c"><a name="a66272c967cb547c09f7a7316b4ae754c"></a><a name="a66272c967cb547c09f7a7316b4ae754c"></a>domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="a9183943cbe59479691b60e9c95a74a0d"><a name="a9183943cbe59479691b60e9c95a74a0d"></a><a name="a9183943cbe59479691b60e9c95a74a0d"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="a06d0695f36184007ab70f95018c90a92"><a name="a06d0695f36184007ab70f95018c90a92"></a><a name="a06d0695f36184007ab70f95018c90a92"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="a72f97dddf8204ffb93f87e0d6ae2111f"><a name="a72f97dddf8204ffb93f87e0d6ae2111f"></a><a name="a72f97dddf8204ffb93f87e0d6ae2111f"></a>This parameter is returned only when the <strong id="b1252212593912"><a name="b1252212593912"></a><a name="b1252212593912"></a>scope</strong> parameter in the request body is set to <strong id="b045115318101"><a name="b045115318101"></a><a name="b045115318101"></a>domain</strong>.</p>
    <p id="a4a60927497a74911bd2ab640524d9633"><a name="a4a60927497a74911bd2ab640524d9633"></a><a name="a4a60927497a74911bd2ab640524d9633"></a>Example:</p>
    <pre class="screen" id="s6426dc53b2a4457ea51cc7ea9e64f456"><a name="s6426dc53b2a4457ea51cc7ea9e64f456"></a><a name="s6426dc53b2a4457ea51cc7ea9e64f456"></a>"domain": { 
          "name" : "domain A"     
          "id" : "fdec73ffea524aa1b373e40..."</pre>
    <a name="ul4940103212141"></a><a name="ul4940103212141"></a><ul id="ul4940103212141"><li><strong id="b165889173109"><a name="b165889173109"></a><a name="b165889173109"></a>domain.name</strong>: Name of the domain that created the user</li><li><strong id="b67031141141018"><a name="b67031141141018"></a><a name="b67031141141018"></a>domain.id</strong>: ID of the domain</li></ul>
    </td>
    </tr>
    <tr id="r3a914bf0c52c43e390883648cbe964ff"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="a0e6de929a1ea4db0b88e97acb4287d5e"><a name="a0e6de929a1ea4db0b88e97acb4287d5e"></a><a name="a0e6de929a1ea4db0b88e97acb4287d5e"></a>project</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="a346f8467c2e24793ab55c120fc37852f"><a name="a346f8467c2e24793ab55c120fc37852f"></a><a name="a346f8467c2e24793ab55c120fc37852f"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="af6953054960f4c59903b92961b10b426"><a name="af6953054960f4c59903b92961b10b426"></a><a name="af6953054960f4c59903b92961b10b426"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="a41001b564477400f98aef711e86f0197"><a name="a41001b564477400f98aef711e86f0197"></a><a name="a41001b564477400f98aef711e86f0197"></a>This parameter is returned only when the <strong id="b4989146181018"><a name="b4989146181018"></a><a name="b4989146181018"></a>scope</strong> parameter in the request body is set to <strong id="b15990164620102"><a name="b15990164620102"></a><a name="b15990164620102"></a>project</strong>.</p>
    <p id="a2658c45981e64570b63c49c45cfdfac7"><a name="a2658c45981e64570b63c49c45cfdfac7"></a><a name="a2658c45981e64570b63c49c45cfdfac7"></a>Example:</p>
    <pre class="screen" id="s75cd01f2f3df45ada904958dc41f5307"><a name="s75cd01f2f3df45ada904958dc41f5307"></a><a name="s75cd01f2f3df45ada904958dc41f5307"></a>"project": { 
          "name": "project A", 
          "id": "34c77f3eaf84c00aaf54...", 
          "domain": { 
             "name": "domain A",
             "id": "fdec73ffea524aa1b373e40..."
           } 
       }</pre>
    <a name="ul198562416149"></a><a name="ul198562416149"></a><ul id="ul198562416149"><li><strong id="b348834111119"><a name="b348834111119"></a><a name="b348834111119"></a>project.name</strong>: Name of a project</li><li><strong id="b1376491921110"><a name="b1376491921110"></a><a name="b1376491921110"></a>project.id</strong>: ID of the project</li><li><strong id="b13383123191115"><a name="b13383123191115"></a><a name="b13383123191115"></a>domain.name</strong>: Domain name of the project</li><li><strong id="b143171418111215"><a name="b143171418111215"></a><a name="b143171418111215"></a>domain.id</strong>: Domain ID of the project</li></ul>
    </td>
    </tr>
    <tr id="row31009604113628"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="p22717013113628"><a name="p22717013113628"></a><a name="p22717013113628"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="p54936595113628"><a name="p54936595113628"></a><a name="p54936595113628"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="p46529556113628"><a name="p46529556113628"></a><a name="p46529556113628"></a>Json Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="p45368001113628"><a name="p45368001113628"></a><a name="p45368001113628"></a>Endpoint information</p>
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
    <a name="ul243124664420"></a><a name="ul243124664420"></a><ul id="ul243124664420"><li><strong id="b448017569144"><a name="b448017569144"></a><a name="b448017569144"></a>type</strong>: Type of the service to which the API belongs</li><li><strong id="b9629121215162"><a name="b9629121215162"></a><a name="b9629121215162"></a>id</strong>: ID of the service</li><li><strong id="b433910179168"><a name="b433910179168"></a><a name="b433910179168"></a>name</strong>: Name of the service</li><li><strong id="b21941141620"><a name="b21941141620"></a><a name="b21941141620"></a>endpoints</strong>: Endpoints that can be used to call the API</li><li><strong id="b2160141311715"><a name="b2160141311715"></a><a name="b2160141311715"></a>url</strong>: URL used to call the API</li><li><strong id="b565712652115"><a name="b565712652115"></a><a name="b565712652115"></a>region</strong>: Region in which the service can be accessed</li><li><strong id="b73317352212"><a name="b73317352212"></a><a name="b73317352212"></a>region_id</strong>: ID of the region</li><li><strong id="b4280125332216"><a name="b4280125332216"></a><a name="b4280125332216"></a>interface</strong>: Type of the interface. The value <strong id="b6806182019239"><a name="b6806182019239"></a><a name="b6806182019239"></a>public</strong> means that the API is open for access.</li><li><strong id="b1174116495233"><a name="b1174116495233"></a><a name="b1174116495233"></a>id</strong>: ID of the API</li></ul>
    </td>
    </tr>
    <tr id="r57913d5a1da24c699a412dced6a7b573"><td class="cellrowborder" valign="top" width="22.06220622062206%" headers="mcps1.1.5.1.1 "><p id="a45bd202186b249bfa8fc87bbcbf05bb9"><a name="a45bd202186b249bfa8fc87bbcbf05bb9"></a><a name="a45bd202186b249bfa8fc87bbcbf05bb9"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.2 "><p id="ae5cf82a55c21452aa028ff59e6973404"><a name="ae5cf82a55c21452aa028ff59e6973404"></a><a name="ae5cf82a55c21452aa028ff59e6973404"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.711771177117715%" headers="mcps1.1.5.1.3 "><p id="aa1fb3d35fbda45208e6e58dbbbc00b01"><a name="aa1fb3d35fbda45208e6e58dbbbc00b01"></a><a name="aa1fb3d35fbda45208e6e58dbbbc00b01"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.21402140214022%" headers="mcps1.1.5.1.4 "><p id="a18bf24a442094153ab2a8f7391737d06"><a name="a18bf24a442094153ab2a8f7391737d06"></a><a name="a18bf24a442094153ab2a8f7391737d06"></a>Permissions information of the token</p>
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
    </tbody>
    </table>

-   Sample response

    ```
    Token information stored in the response header:
    X-Subject-Token:MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...
    
    Token information stored in the response body:
    {
      "token" : {
        "methods" : ["password"],
        "expires_at" : "2015-11-09T01:42:57.527363Z",
        "issued_at" : "2015-11-09T00:42:57.527404Z",
        "user" : {
          "domain" : {
          "id" : "ded485def148s4e7d2se41d5se...",
          "name" : "domain A"
          },
          "id" : "ee4dfb6e5540447cb37419051...",
          "name" : "user A",
          "password_expires_at":"2016-11-06T15:32:17.000000",
        },
        "domain" : {
           "name" : "domain A",
           "id" : "dod4ed5e8d4e8d2e8e8d5d2d..."
        },
        "catalog": [{
            "type": "identity",
            "id": "1331e5cff2a74d76b03da12259...",
            "name": "iam",
            "endpoints": [{
                "url": "www.example.com/v3",
                "region": "*",
                "region_id": "*",
               "interface": "public",
                 "id": "089d4a381d574308a703122d3a..."
           }]
        }], 
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


## Status Codes<a name="sbfe93ca4c2b9427dbb2218a4e72da6a8"></a>

<a name="en-us_topic_0026585112_table34550710"></a>
<table><thead align="left"><tr id="en-us_topic_0026585112_row8352109"><th class="cellrowborder" valign="top" width="48.15%" id="mcps1.1.3.1.1"><p id="en-us_topic_0026585112_p5432205"><a name="en-us_topic_0026585112_p5432205"></a><a name="en-us_topic_0026585112_p5432205"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="51.849999999999994%" id="mcps1.1.3.1.2"><p id="en-us_topic_0026585112_p37355470"><a name="en-us_topic_0026585112_p37355470"></a><a name="en-us_topic_0026585112_p37355470"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0026585112_row5894231"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p7670737"><a name="en-us_topic_0026585112_p7670737"></a><a name="en-us_topic_0026585112_p7670737"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p17349988"><a name="en-us_topic_0026585112_p17349988"></a><a name="en-us_topic_0026585112_p17349988"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0026585112_row21932166"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p31674992"><a name="en-us_topic_0026585112_p31674992"></a><a name="en-us_topic_0026585112_p31674992"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p15537542"><a name="en-us_topic_0026585112_p15537542"></a><a name="en-us_topic_0026585112_p15537542"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="r22bf632ff3984ffbaa2734a029063cfb"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p947606916650"><a name="en-us_topic_0026585112_p947606916650"></a><a name="en-us_topic_0026585112_p947606916650"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="a3a62e2f9d6c84b4083dfb8b2ade8e14c"><a name="a3a62e2f9d6c84b4083dfb8b2ade8e14c"></a><a name="a3a62e2f9d6c84b4083dfb8b2ade8e14c"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="r41d0d854619349f898c16f7c61792083"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p762821816657"><a name="en-us_topic_0026585112_p762821816657"></a><a name="en-us_topic_0026585112_p762821816657"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="a0261fc1955104ca3b1f0a46388724624"><a name="a0261fc1955104ca3b1f0a46388724624"></a><a name="a0261fc1955104ca3b1f0a46388724624"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="rea66e1a745ee4e0882be6b9f5349ac4d"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p486971841676"><a name="en-us_topic_0026585112_p486971841676"></a><a name="en-us_topic_0026585112_p486971841676"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p521578261676"><a name="en-us_topic_0026585112_p521578261676"></a><a name="en-us_topic_0026585112_p521578261676"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="r230ba1b5ddec4cd0a41a5c37806e60f5"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="af8f4513c90d344e3b90952b53e3ee015"><a name="af8f4513c90d344e3b90952b53e3ee015"></a><a name="af8f4513c90d344e3b90952b53e3ee015"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="a19c27fd6b377464898ec6cae5778ec80"><a name="a19c27fd6b377464898ec6cae5778ec80"></a><a name="a19c27fd6b377464898ec6cae5778ec80"></a>Failed to complete the request because of an internal service error. The format may be incorrect.</p>
</td>
</tr>
<tr id="en-us_topic_0026585112_row6824316711"><td class="cellrowborder" valign="top" width="48.15%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p61418816711"><a name="en-us_topic_0026585112_p61418816711"></a><a name="en-us_topic_0026585112_p61418816711"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="51.849999999999994%" headers="mcps1.1.3.1.2 "><p id="a4bc003bda05e465eb3a3f0f989888213"><a name="a4bc003bda05e465eb3a3f0f989888213"></a><a name="a4bc003bda05e465eb3a3f0f989888213"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

