# Querying Message Templates<a name="smn_api_53004"></a>

## Description<a name="section27645849"></a>

-   API name

    ListMessageTemplates


-   Function

    Query the template list by page. The list is sorted by the template creation time in ascending order. If no template has been created, an empty list is returned. The parameters  **message\_template\_name**  and  **protocol**  are added.


>![](/images/icon-note.gif) **NOTE:**   
>The template list provides only brief information. To query the template details, see section  [Querying the Message Template Details](querying-the-message-template-details.md).  

## URI<a name="section47486057"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/message\_template?offset=\{offset\}&limit=\{limit\}&message\_template\_name=\{message\_template\_name\}&protocol=\{protocol\}


-   Parameter description

    <a name="table26295076"></a>
    <table><thead align="left"><tr id="row16170542"><th class="cellrowborder" valign="top" width="20.667933206679333%" id="mcps1.1.5.1.1"><p id="p34745524"><a name="p34745524"></a><a name="p34745524"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.597840215978405%" id="mcps1.1.5.1.2"><p id="p62924030"><a name="p62924030"></a><a name="p62924030"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.06729327067293%" id="mcps1.1.5.1.3"><p id="p63681652"><a name="p63681652"></a><a name="p63681652"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.666933306669332%" id="mcps1.1.5.1.4"><p id="p57940224"><a name="p57940224"></a><a name="p57940224"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41204595"><td class="cellrowborder" valign="top" width="20.667933206679333%" headers="mcps1.1.5.1.1 "><p id="p49237932"><a name="p49237932"></a><a name="p49237932"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.597840215978405%" headers="mcps1.1.5.1.2 "><p id="p28849561"><a name="p28849561"></a><a name="p28849561"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.06729327067293%" headers="mcps1.1.5.1.3 "><p id="p55113123"><a name="p55113123"></a><a name="p55113123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.666933306669332%" headers="mcps1.1.5.1.4 "><p id="p3312144215538"><a name="p3312144215538"></a><a name="p3312144215538"></a>Project ID</p>
    <p id="p34977969"><a name="p34977969"></a><a name="p34977969"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row64680333"><td class="cellrowborder" valign="top" width="20.667933206679333%" headers="mcps1.1.5.1.1 "><p id="p4615638"><a name="p4615638"></a><a name="p4615638"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.597840215978405%" headers="mcps1.1.5.1.2 "><p id="p38322367"><a name="p38322367"></a><a name="p38322367"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.06729327067293%" headers="mcps1.1.5.1.3 "><p id="p17103984"><a name="p17103984"></a><a name="p17103984"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.666933306669332%" headers="mcps1.1.5.1.4 "><p id="p146581828102110"><a name="p146581828102110"></a><a name="p146581828102110"></a>Offset</p>
    <p id="p21821344207"><a name="p21821344207"></a><a name="p21821344207"></a>If the value is an integer greater than 0 but less than the number of resources, all resources after this offset will be queried. The default value is <strong id="b115471822134"><a name="b115471822134"></a><a name="b115471822134"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row51881906"><td class="cellrowborder" valign="top" width="20.667933206679333%" headers="mcps1.1.5.1.1 "><p id="p41684868"><a name="p41684868"></a><a name="p41684868"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.597840215978405%" headers="mcps1.1.5.1.2 "><p id="p21031171"><a name="p21031171"></a><a name="p21031171"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.06729327067293%" headers="mcps1.1.5.1.3 "><p id="p25803286"><a name="p25803286"></a><a name="p25803286"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.666933306669332%" headers="mcps1.1.5.1.4 "><a name="ul38160342182720"></a><a name="ul38160342182720"></a><ul id="ul38160342182720"><li>Number of resources returned on each page</li><li>Value range: 1–100<p id="p3980022182720"><a name="p3980022182720"></a><a name="p3980022182720"></a>Commonly used values are <strong id="b152545771319"><a name="b152545771319"></a><a name="b152545771319"></a>10</strong>, <strong id="b122548791311"><a name="b122548791311"></a><a name="b122548791311"></a>20</strong>, and <strong id="b1325587131310"><a name="b1325587131310"></a><a name="b1325587131310"></a>50</strong>.</p>
    <p id="p4889152416011"><a name="p4889152416011"></a><a name="p4889152416011"></a>The default value is <strong id="b1713511181318"><a name="b1713511181318"></a><a name="b1713511181318"></a>100</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row18621933"><td class="cellrowborder" valign="top" width="20.667933206679333%" headers="mcps1.1.5.1.1 "><p id="p31981619"><a name="p31981619"></a><a name="p31981619"></a>message_template_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.597840215978405%" headers="mcps1.1.5.1.2 "><p id="p40374353"><a name="p40374353"></a><a name="p40374353"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.06729327067293%" headers="mcps1.1.5.1.3 "><p id="p49097200"><a name="p49097200"></a><a name="p49097200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.666933306669332%" headers="mcps1.1.5.1.4 "><p id="p17450296"><a name="p17450296"></a><a name="p17450296"></a>Template name</p>
    <p id="p6338272399"><a name="p6338272399"></a><a name="p6338272399"></a>The template name is a string of 1 to 64 characters. It must contain upper- or lower-case letters, digits, hyphens (-), and underscores (_), and must start with a letter or digit.</p>
    </td>
    </tr>
    <tr id="row37690705"><td class="cellrowborder" valign="top" width="20.667933206679333%" headers="mcps1.1.5.1.1 "><p id="p33048293"><a name="p33048293"></a><a name="p33048293"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.597840215978405%" headers="mcps1.1.5.1.2 "><p id="p59666077"><a name="p59666077"></a><a name="p59666077"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.06729327067293%" headers="mcps1.1.5.1.3 "><p id="p1114082"><a name="p1114082"></a><a name="p1114082"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.666933306669332%" headers="mcps1.1.5.1.4 "><p id="p23131803"><a name="p23131803"></a><a name="p23131803"></a>Protocol supported by the template</p>
    <p id="p15571735514"><a name="p15571735514"></a><a name="p15571735514"></a>Currently, the following protocols are supported:</p>
    <a name="ul1715273514576"></a><a name="ul1715273514576"></a><ul id="ul1715273514576"><li><strong id="smn_api_53001_b122581017374"><a name="smn_api_53001_b122581017374"></a><a name="smn_api_53001_b122581017374"></a>email</strong></li><li><strong id="smn_api_53001_b1938219133716"><a name="smn_api_53001_b1938219133716"></a><a name="smn_api_53001_b1938219133716"></a>default</strong></li><li><strong id="smn_api_53001_b23671526885"><a name="smn_api_53001_b23671526885"></a><a name="smn_api_53001_b23671526885"></a>sms</strong></li><li><strong id="smn_api_53001_b49701126897"><a name="smn_api_53001_b49701126897"></a><a name="smn_api_53001_b49701126897"></a>dms</strong></li><li><strong id="smn_api_53001_b185159332910"><a name="smn_api_53001_b185159332910"></a><a name="smn_api_53001_b185159332910"></a>http</strong> and <strong id="smn_api_53001_b25282033899"><a name="smn_api_53001_b25282033899"></a><a name="smn_api_53001_b25282033899"></a>https</strong></li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section24721334"></a>

Request example

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/message_template?offset=0&limit=2&message_template_name=test1&protocol=email
```

## Response<a name="section21165417"></a>

-   Parameter description

    <a name="table50427332"></a>
    <table><thead align="left"><tr id="row21494305"><th class="cellrowborder" valign="top" width="37.163716371637165%" id="mcps1.1.4.1.1"><p id="p63317164"><a name="p63317164"></a><a name="p63317164"></a><strong id="b1022306334"><a name="b1022306334"></a><a name="b1022306334"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.562156215621563%" id="mcps1.1.4.1.2"><p id="p28416672"><a name="p28416672"></a><a name="p28416672"></a><strong id="b87764883"><a name="b87764883"></a><a name="b87764883"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.27412741274127%" id="mcps1.1.4.1.3"><p id="p20049059"><a name="p20049059"></a><a name="p20049059"></a><strong id="b256550682"><a name="b256550682"></a><a name="b256550682"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8508925"><td class="cellrowborder" valign="top" width="37.163716371637165%" headers="mcps1.1.4.1.1 "><p id="p18134306"><a name="p18134306"></a><a name="p18134306"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.562156215621563%" headers="mcps1.1.4.1.2 "><p id="p59592696"><a name="p59592696"></a><a name="p59592696"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.27412741274127%" headers="mcps1.1.4.1.3 "><p id="p62279078"><a name="p62279078"></a><a name="p62279078"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row35856517"><td class="cellrowborder" valign="top" width="37.163716371637165%" headers="mcps1.1.4.1.1 "><p id="p18696727"><a name="p18696727"></a><a name="p18696727"></a>message_template_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.562156215621563%" headers="mcps1.1.4.1.2 "><p id="p38039934"><a name="p38039934"></a><a name="p38039934"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.27412741274127%" headers="mcps1.1.4.1.3 "><p id="p61335842"><a name="p61335842"></a><a name="p61335842"></a>Number of returned templates</p>
    </td>
    </tr>
    <tr id="row19325759"><td class="cellrowborder" valign="top" width="37.163716371637165%" headers="mcps1.1.4.1.1 "><p id="p21882681"><a name="p21882681"></a><a name="p21882681"></a>message_templates</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.562156215621563%" headers="mcps1.1.4.1.2 "><p id="p27666764"><a name="p27666764"></a><a name="p27666764"></a>Message template structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.27412741274127%" headers="mcps1.1.4.1.3 "><p id="p26415391"><a name="p26415391"></a><a name="p26415391"></a>For details, see <a href="#table52721373195752">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Message template structure

    <a name="table52721373195752"></a>
    <table><thead align="left"><tr id="row49890639195752"><th class="cellrowborder" valign="top" width="30.409999999999997%" id="mcps1.2.4.1.1"><p id="p14609979195752"><a name="p14609979195752"></a><a name="p14609979195752"></a><strong id="b1071973719112"><a name="b1071973719112"></a><a name="b1071973719112"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.2"><p id="p42557684195752"><a name="p42557684195752"></a><a name="p42557684195752"></a><strong id="b1669010173"><a name="b1669010173"></a><a name="b1669010173"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.699999999999996%" id="mcps1.2.4.1.3"><p id="p24620385195752"><a name="p24620385195752"></a><a name="p24620385195752"></a><strong id="b75384394116"><a name="b75384394116"></a><a name="b75384394116"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3315065195752"><td class="cellrowborder" valign="top" width="30.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p84852195752"><a name="p84852195752"></a><a name="p84852195752"></a>message_template_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p6873027195752"><a name="p6873027195752"></a><a name="p6873027195752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.699999999999996%" headers="mcps1.2.4.1.3 "><p id="p19844303195752"><a name="p19844303195752"></a><a name="p19844303195752"></a>Template ID</p>
    </td>
    </tr>
    <tr id="row38091128195752"><td class="cellrowborder" valign="top" width="30.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p65482522195752"><a name="p65482522195752"></a><a name="p65482522195752"></a>message_template_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p2484052195752"><a name="p2484052195752"></a><a name="p2484052195752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.699999999999996%" headers="mcps1.2.4.1.3 "><p id="p66990543195752"><a name="p66990543195752"></a><a name="p66990543195752"></a>Template name</p>
    </td>
    </tr>
    <tr id="row1830114116222"><td class="cellrowborder" valign="top" width="30.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p04063811611"><a name="p04063811611"></a><a name="p04063811611"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p18228205714104"><a name="p18228205714104"></a><a name="p18228205714104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.699999999999996%" headers="mcps1.2.4.1.3 "><p id="p14404381967"><a name="p14404381967"></a><a name="p14404381967"></a>Protocol supported by the template</p>
    <p id="p11456163572311"><a name="p11456163572311"></a><a name="p11456163572311"></a>Currently, the following protocols are supported:</p>
    <a name="ul045620357238"></a><a name="ul045620357238"></a><ul id="ul045620357238"><li><strong id="smn_api_53001_b122581017374_1"><a name="smn_api_53001_b122581017374_1"></a><a name="smn_api_53001_b122581017374_1"></a>email</strong></li><li><strong id="smn_api_53001_b1938219133716_1"><a name="smn_api_53001_b1938219133716_1"></a><a name="smn_api_53001_b1938219133716_1"></a>default</strong></li><li><strong id="smn_api_53001_b23671526885_1"><a name="smn_api_53001_b23671526885_1"></a><a name="smn_api_53001_b23671526885_1"></a>sms</strong></li><li><strong id="smn_api_53001_b49701126897_1"><a name="smn_api_53001_b49701126897_1"></a><a name="smn_api_53001_b49701126897_1"></a>dms</strong></li><li><strong id="smn_api_53001_b185159332910_1"><a name="smn_api_53001_b185159332910_1"></a><a name="smn_api_53001_b185159332910_1"></a>http</strong> and <strong id="smn_api_53001_b25282033899_1"><a name="smn_api_53001_b25282033899_1"></a><a name="smn_api_53001_b25282033899_1"></a>https</strong></li></ul>
    </td>
    </tr>
    <tr id="row31653440195752"><td class="cellrowborder" valign="top" width="30.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p13791810195752"><a name="p13791810195752"></a><a name="p13791810195752"></a>tag_names</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p43394841195752"><a name="p43394841195752"></a><a name="p43394841195752"></a>String array</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.699999999999996%" headers="mcps1.2.4.1.3 "><p id="p25321261195752"><a name="p25321261195752"></a><a name="p25321261195752"></a>Template variable list</p>
    </td>
    </tr>
    <tr id="row4262034195752"><td class="cellrowborder" valign="top" width="30.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p9680508195752"><a name="p9680508195752"></a><a name="p9680508195752"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p45923711195752"><a name="p45923711195752"></a><a name="p45923711195752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.699999999999996%" headers="mcps1.2.4.1.3 "><p id="p28833090195752"><a name="p28833090195752"></a><a name="p28833090195752"></a>Time when the template was created</p>
    <p id="p535731162417"><a name="p535731162417"></a><a name="p535731162417"></a>The UTC time is in <em id="i23501384310"><a name="i23501384310"></a><a name="i23501384310"></a>YYYY-MM-DDTHH:MM:SSZ</em> format.</p>
    </td>
    </tr>
    <tr id="row14248281195752"><td class="cellrowborder" valign="top" width="30.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p13260149195752"><a name="p13260149195752"></a><a name="p13260149195752"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p330252195752"><a name="p330252195752"></a><a name="p330252195752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.699999999999996%" headers="mcps1.2.4.1.3 "><p id="p26750472195752"><a name="p26750472195752"></a><a name="p26750472195752"></a>Last time when the template was updated</p>
    <p id="p25218464247"><a name="p25218464247"></a><a name="p25218464247"></a>The UTC time is in <em id="i176381520257"><a name="i176381520257"></a><a name="i176381520257"></a>YYYY-MM-DDTHH:MM:SSZ</em> format.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "message_templates":[
            {
                "message_template_name":"confirm_message",
                "update_time":"2016-08-02T08:22:18Z",
                "create_time":"2016-08-02T08:22:18Z",
                "tag_names":[
                    "topic_urn"
                ],
                "message_template_id":"79227dfdf88d4e52a1820ca1eb411635"
            },
            {
                "message_template_name":"confirm_message",
                "protocol":"email",
                "update_time":"2016-08-02T08:22:19Z",
                "create_time":"2016-08-02T08:22:19Z",
                "tag_names":[
                    "topic_id"
                ],
                "message_template_id":"ecf63465804a4b10a0573980be78ffba"
            },
            {
                "message_template_name":"confirm_message",
                "protocol":"https",
                "update_time":"2016-08-02T08:22:20Z",
                "create_time":"2016-08-02T08:22:20Z",
                "tag_names":[
                    "topic_id"
                ],
                "message_template_id":"57ba8dcecda844878c5dd5815b65d10f"
            }
        ],
        "request_id":"ce7f2f7343224f8c9597b05a9a0bcc2e",
        "message_template_count":3
    }
    ```


## Returned Value<a name="section56271027"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

