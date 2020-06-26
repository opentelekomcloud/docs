# Adding a Subscription<a name="smn_api_52003"></a>

## Description<a name="section28602718"></a>

-   API name

    Subscribe


-   Function

    Add a subscription to a specified topic. If the status of the subscription is unconfirmed, a confirmation message is sent to the subscriber. After confirming the subscription, the subscriber can receive notification messages published to the topic.

    By default, 10000 subscriptions can be added to a topic. However, in a high-concurrency scenario, which is rare, extra subscriptions may be added successfully.

    The API is idempotent. If the added subscription already exists, a successful result and status code 200 are returned. Otherwise, the status code is 201.


## URI<a name="section56097870"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/subscriptions


-   Parameter description

    <a name="table33640543"></a>
    <table><thead align="left"><tr id="row18743339"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p41815528"><a name="p41815528"></a><a name="p41815528"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.650000000000002%" id="mcps1.1.5.1.2"><p id="p31614597"><a name="p31614597"></a><a name="p31614597"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.709999999999997%" id="mcps1.1.5.1.3"><p id="p10645546"><a name="p10645546"></a><a name="p10645546"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.64%" id="mcps1.1.5.1.4"><p id="p56982912"><a name="p56982912"></a><a name="p56982912"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1408093"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p46946741"><a name="p46946741"></a><a name="p46946741"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.1.5.1.2 "><p id="p44589661"><a name="p44589661"></a><a name="p44589661"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.709999999999997%" headers="mcps1.1.5.1.3 "><p id="p54992765"><a name="p54992765"></a><a name="p54992765"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.64%" headers="mcps1.1.5.1.4 "><p id="p11652542155129"><a name="p11652542155129"></a><a name="p11652542155129"></a>Project ID</p>
    <p id="p25228990"><a name="p25228990"></a><a name="p25228990"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row4105351"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p64098000"><a name="p64098000"></a><a name="p64098000"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.1.5.1.2 "><p id="p24555510"><a name="p24555510"></a><a name="p24555510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.709999999999997%" headers="mcps1.1.5.1.3 "><p id="p42839264"><a name="p42839264"></a><a name="p42839264"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.64%" headers="mcps1.1.5.1.4 "><p id="p47428342"><a name="p47428342"></a><a name="p47428342"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section35118788"></a>

-   Parameter description

    <a name="table66803845"></a>
    <table><thead align="left"><tr id="row57367087"><th class="cellrowborder" valign="top" width="19.24807519248075%" id="mcps1.1.5.1.1"><p id="p16222495"><a name="p16222495"></a><a name="p16222495"></a><strong id="b842352706191030_1"><a name="b842352706191030_1"></a><a name="b842352706191030_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.707929207079292%" id="mcps1.1.5.1.2"><p id="p38953736"><a name="p38953736"></a><a name="p38953736"></a><strong id="b86763093241"><a name="b86763093241"></a><a name="b86763093241"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.417558244175584%" id="mcps1.1.5.1.3"><p id="p1136017"><a name="p1136017"></a><a name="p1136017"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.626437356264375%" id="mcps1.1.5.1.4"><p id="p24908514"><a name="p24908514"></a><a name="p24908514"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14679294"><td class="cellrowborder" valign="top" width="19.24807519248075%" headers="mcps1.1.5.1.1 "><p id="p48172185"><a name="p48172185"></a><a name="p48172185"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.707929207079292%" headers="mcps1.1.5.1.2 "><p id="p9632925"><a name="p9632925"></a><a name="p9632925"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.417558244175584%" headers="mcps1.1.5.1.3 "><p id="p42069424"><a name="p42069424"></a><a name="p42069424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.626437356264375%" headers="mcps1.1.5.1.4 "><p id="p52180221"><a name="p52180221"></a><a name="p52180221"></a>Message endpoint</p>
    <div class="note" id="note1190810251344"><a name="note1190810251344"></a><a name="note1190810251344"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p65848362"><a name="p65848362"></a><a name="p65848362"></a>For an HTTP subscription, the endpoint starts with <strong id="b842352706152017"><a name="b842352706152017"></a><a name="b842352706152017"></a>http://</strong>.</p>
    <p id="p55764348"><a name="p55764348"></a><a name="p55764348"></a>For an HTTPS subscription, the endpoint starts with <strong id="b842352706152039"><a name="b842352706152039"></a><a name="b842352706152039"></a>https://</strong>.</p>
    <p id="p32117087"><a name="p32117087"></a><a name="p32117087"></a>For an email subscription, the endpoint is an email address.</p>
    <p id="p20618333"><a name="p20618333"></a><a name="p20618333"></a>For an SMS subscription, the endpoint is a phone number.</p>
    <p id="p65014107185812"><a name="p65014107185812"></a><a name="p65014107185812"></a>For a DMS subscription, the endpoint is a message queue.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row51347269"><td class="cellrowborder" valign="top" width="19.24807519248075%" headers="mcps1.1.5.1.1 "><p id="p65488131"><a name="p65488131"></a><a name="p65488131"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.707929207079292%" headers="mcps1.1.5.1.2 "><p id="p2938434"><a name="p2938434"></a><a name="p2938434"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.417558244175584%" headers="mcps1.1.5.1.3 "><p id="p36686634"><a name="p36686634"></a><a name="p36686634"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.626437356264375%" headers="mcps1.1.5.1.4 "><p id="p18827362"><a name="p18827362"></a><a name="p18827362"></a>Subscription protocol (Different protocols indicate different types of endpoints to receive messages.)</p>
    <p id="p1555972375816"><a name="p1555972375816"></a><a name="p1555972375816"></a>Currently, the following protocols are supported:</p>
    <a name="ul1777124019573"></a><a name="ul1777124019573"></a><ul id="ul1777124019573"><li><strong id="smn_api_52001_b65901133114410"><a name="smn_api_52001_b65901133114410"></a><a name="smn_api_52001_b65901133114410"></a>email</strong>: The endpoints are email address.</li><li><strong id="smn_api_52001_b99571741008"><a name="smn_api_52001_b99571741008"></a><a name="smn_api_52001_b99571741008"></a>sms</strong>: The endpoints are phone numbers.</li><li><strong id="smn_api_52001_b1099011287223"><a name="smn_api_52001_b1099011287223"></a><a name="smn_api_52001_b1099011287223"></a>http</strong> and <strong id="smn_api_52001_b577715331224"><a name="smn_api_52001_b577715331224"></a><a name="smn_api_52001_b577715331224"></a>https</strong>: The endpoints are URLs.</li></ul>
    </td>
    </tr>
    <tr id="row34938791"><td class="cellrowborder" valign="top" width="19.24807519248075%" headers="mcps1.1.5.1.1 "><p id="p11469823"><a name="p11469823"></a><a name="p11469823"></a>remark</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.707929207079292%" headers="mcps1.1.5.1.2 "><p id="p56640484"><a name="p56640484"></a><a name="p56640484"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.417558244175584%" headers="mcps1.1.5.1.3 "><p id="p24476477"><a name="p24476477"></a><a name="p24476477"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.626437356264375%" headers="mcps1.1.5.1.4 "><p id="p10287856125818"><a name="p10287856125818"></a><a name="p10287856125818"></a>Description of the subscription</p>
    <p id="p36437619"><a name="p36437619"></a><a name="p36437619"></a>The remarks must be a UTF-8-coded character string containing 128 bytes at most.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1/subscriptions
    ```

    ```
    {
        "protocol": "email", 
        "endpoint": "xxx@xxx.com", 
        "remark": "O&M"
    } 
    ```


## Response<a name="section47633640"></a>

-   Parameter description

    <a name="table58321122"></a>
    <table><thead align="left"><tr id="row60828573"><th class="cellrowborder" valign="top" width="28.910000000000004%" id="mcps1.1.4.1.1"><p id="p28167350"><a name="p28167350"></a><a name="p28167350"></a><strong id="b842352706191030_2"><a name="b842352706191030_2"></a><a name="b842352706191030_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.910000000000004%" id="mcps1.1.4.1.2"><p id="p66962839"><a name="p66962839"></a><a name="p66962839"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.18%" id="mcps1.1.4.1.3"><p id="p55280873"><a name="p55280873"></a><a name="p55280873"></a><strong id="b84235270619115_2"><a name="b84235270619115_2"></a><a name="b84235270619115_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41508862"><td class="cellrowborder" valign="top" width="28.910000000000004%" headers="mcps1.1.4.1.1 "><p id="p6774674"><a name="p6774674"></a><a name="p6774674"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.910000000000004%" headers="mcps1.1.4.1.2 "><p id="p11877685"><a name="p11877685"></a><a name="p11877685"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p22568466"><a name="p22568466"></a><a name="p22568466"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row10740297"><td class="cellrowborder" valign="top" width="28.910000000000004%" headers="mcps1.1.4.1.1 "><p id="p64657722"><a name="p64657722"></a><a name="p64657722"></a>subscription_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.910000000000004%" headers="mcps1.1.4.1.2 "><p id="p2784095"><a name="p2784095"></a><a name="p2784095"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p24185120"><a name="p24185120"></a><a name="p24185120"></a>Resource identifier of a subscription, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "request_id": "fdbabe38ead6482b8574f82a3d1168e9",
        "subscription_urn": "urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1:2e778e84408e44058e6cbc6d3c377837"
    }
    ```


## Returned Value<a name="section26049579"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

