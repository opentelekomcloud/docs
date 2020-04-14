# Querying Topic Attributes<a name="smn_api_51006"></a>

## Description<a name="section64935954"></a>

-   API name

    ListTopicAttributes


-   Function

    Query the topic attribute information.


## URI<a name="section47552675"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/attributes?name=\{name\}


-   Parameter description

    <a name="table60453091"></a>
    <table><thead align="left"><tr id="row31471768"><th class="cellrowborder" valign="top" width="23.69%" id="mcps1.1.5.1.1"><p id="p66185246"><a name="p66185246"></a><a name="p66185246"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.1.5.1.2"><p id="p59404709"><a name="p59404709"></a><a name="p59404709"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.64%" id="mcps1.1.5.1.3"><p id="p47052116"><a name="p47052116"></a><a name="p47052116"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.320000000000004%" id="mcps1.1.5.1.4"><p id="p53125076"><a name="p53125076"></a><a name="p53125076"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57297510"><td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.1.5.1.1 "><p id="p10586695"><a name="p10586695"></a><a name="p10586695"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.1.5.1.2 "><p id="p52215961"><a name="p52215961"></a><a name="p52215961"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.64%" headers="mcps1.1.5.1.3 "><p id="p1634435"><a name="p1634435"></a><a name="p1634435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.320000000000004%" headers="mcps1.1.5.1.4 "><p id="p5162792715506"><a name="p5162792715506"></a><a name="p5162792715506"></a>Project ID</p>
    <p id="p65280430"><a name="p65280430"></a><a name="p65280430"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row9249362"><td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.1.5.1.1 "><p id="p11000853"><a name="p11000853"></a><a name="p11000853"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.1.5.1.2 "><p id="p18653909"><a name="p18653909"></a><a name="p18653909"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.64%" headers="mcps1.1.5.1.3 "><p id="p34571641"><a name="p34571641"></a><a name="p34571641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.320000000000004%" headers="mcps1.1.5.1.4 "><p id="p48839530"><a name="p48839530"></a><a name="p48839530"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    <tr id="row28333568111935"><td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.1.5.1.1 "><p id="p13317684111935"><a name="p13317684111935"></a><a name="p13317684111935"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.1.5.1.2 "><p id="p4990583111935"><a name="p4990583111935"></a><a name="p4990583111935"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.64%" headers="mcps1.1.5.1.3 "><p id="p1584116111935"><a name="p1584116111935"></a><a name="p1584116111935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.320000000000004%" headers="mcps1.1.5.1.4 "><p id="p61204561111935"><a name="p61204561111935"></a><a name="p61204561111935"></a>Attribute name</p>
    <p id="p363615525300"><a name="p363615525300"></a><a name="p363615525300"></a>Only specified attribute names are supported. For details, see section <a href="topic-attribute-list.md">Topic Attribute List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the  **name**  parameter is not specified, all attribute values of the topic are queried. The supported attribute values are provided in section  [Topic Attribute List](topic-attribute-list.md).  


## Request<a name="section25320898"></a>

Request example

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId:8bad8a40e0f7462f8c1676e3f93a8183:test_create_topic_v2/attributes?name=access_policy
```

## Response<a name="section26561495"></a>

-   Parameter description

    <a name="table38552084"></a>
    <table><thead align="left"><tr id="row10058158"><th class="cellrowborder" valign="top" width="32.20322032203221%" id="mcps1.1.4.1.1"><p id="p9404449"><a name="p9404449"></a><a name="p9404449"></a><strong id="b1910858008"><a name="b1910858008"></a><a name="b1910858008"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.20322032203221%" id="mcps1.1.4.1.2"><p id="p23562876"><a name="p23562876"></a><a name="p23562876"></a><strong id="b591968115"><a name="b591968115"></a><a name="b591968115"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.5935593559356%" id="mcps1.1.4.1.3"><p id="p29544808"><a name="p29544808"></a><a name="p29544808"></a><strong id="b585962561"><a name="b585962561"></a><a name="b585962561"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33089041"><td class="cellrowborder" valign="top" width="32.20322032203221%" headers="mcps1.1.4.1.1 "><p id="p62966687"><a name="p62966687"></a><a name="p62966687"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.20322032203221%" headers="mcps1.1.4.1.2 "><p id="p27997"><a name="p27997"></a><a name="p27997"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5935593559356%" headers="mcps1.1.4.1.3 "><p id="p2267763"><a name="p2267763"></a><a name="p2267763"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row42586845"><td class="cellrowborder" valign="top" width="32.20322032203221%" headers="mcps1.1.4.1.1 "><p id="p266368914302"><a name="p266368914302"></a><a name="p266368914302"></a>attributes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.20322032203221%" headers="mcps1.1.4.1.2 "><p id="p38092711"><a name="p38092711"></a><a name="p38092711"></a>Map</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5935593559356%" headers="mcps1.1.4.1.3 "><p id="p65610739"><a name="p65610739"></a><a name="p65610739"></a>Attribute key-value pair</p>
    <p id="p87064812277"><a name="p87064812277"></a><a name="p87064812277"></a><strong id="b185226195816"><a name="b185226195816"></a><a name="b185226195816"></a>access_policy</strong>: topic access policy</p>
    <p id="p6701648192711"><a name="p6701648192711"></a><a name="p6701648192711"></a><strong id="b6230205945818"><a name="b6230205945818"></a><a name="b6230205945818"></a>introduction</strong>: description of a topic</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
       "request_id":"6837531fd3f54550927b930180a706bf",
       "attributes": {
       "access_policy": "{
             "Version": "2016-09-07", 
             "Id": "__default_policy_ID", 
             "Statement": [
                {
                  "Sid": "__user_pub_0",
                  "Effect": "Allow",
                  "Principal": {
                    "CSP": [
                             "urn:csp:iam::93dc1b4697ac493d9b7d089569f86b32:root"
                           ]
                     },
                  "Action": ["SMN:Publish","SMN:QueryTopicDetail"],
                  "Resource": "urn:smn:regionId:8bad8a40e0f7462f8c1676e3f93a8183:aaa"
                  },
                  {
                  "Sid": "__service_pub_0", 
                  "Effect": "Allow",
                  "Principal": {
                     "Service": ["obs"]
                     },
                  "Action": ["SMN:Publish","SMN:QueryTopicDetail"],
                  "Resource": "urn:smn:regionId:8bad8a40e0f7462f8c1676e3f93a8183:aaa"
                  }
                 ]
              }"
           }
      }
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The value of  **access\_policy**  is a JSON character string, which requires escape characters. While in the preceding example, the characters are not escaped. You need to escape them before using the policy.  


## Returned Value<a name="section37726867"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

