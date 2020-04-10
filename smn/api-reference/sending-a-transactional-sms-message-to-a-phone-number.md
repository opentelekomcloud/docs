# Sending a Transactional SMS Message to a Phone Number<a name="smn_api_55001"></a>

## Description<a name="section2841046616319"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Direct SMS messaging is not available to new users. If you want to use these APIs, go to  **Cloud Communications**  \>  **Message&SMS**.  

-   API name

    SmsPublish

-   Function

    Send a transactional SMS message to a specified phone number, usually used for verification code or notification.


## URI<a name="section5536839916319"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/sms

-   Parameter description

    <a name="table1545278516319"></a>
    <table><thead align="left"><tr id="row4866951016319"><th class="cellrowborder" valign="top" width="21.27787221277872%" id="mcps1.1.5.1.1"><p id="p4991624416319"><a name="p4991624416319"></a><a name="p4991624416319"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.688031196880313%" id="mcps1.1.5.1.2"><p id="p1668400316319"><a name="p1668400316319"></a><a name="p1668400316319"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.987901209879013%" id="mcps1.1.5.1.3"><p id="p922703516319"><a name="p922703516319"></a><a name="p922703516319"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.04619538046195%" id="mcps1.1.5.1.4"><p id="p919235516319"><a name="p919235516319"></a><a name="p919235516319"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4728262816319"><td class="cellrowborder" valign="top" width="21.27787221277872%" headers="mcps1.1.5.1.1 "><p id="p468766116319"><a name="p468766116319"></a><a name="p468766116319"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.688031196880313%" headers="mcps1.1.5.1.2 "><p id="p4415629516319"><a name="p4415629516319"></a><a name="p4415629516319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.987901209879013%" headers="mcps1.1.5.1.3 "><p id="p1989017016319"><a name="p1989017016319"></a><a name="p1989017016319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.1.5.1.4 "><p id="p682193315545"><a name="p682193315545"></a><a name="p682193315545"></a>Project ID</p>
    <p id="p49105316319"><a name="p49105316319"></a><a name="p49105316319"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section57419616319"></a>

-   Parameter description

    <a name="table920655716319"></a>
    <table><thead align="left"><tr id="row5615067816319"><th class="cellrowborder" valign="top" width="18.8%" id="mcps1.1.5.1.1"><p id="p5191106116319"><a name="p5191106116319"></a><a name="p5191106116319"></a><strong id="b237681975"><a name="b237681975"></a><a name="b237681975"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.869999999999997%" id="mcps1.1.5.1.2"><p id="p4404643716319"><a name="p4404643716319"></a><a name="p4404643716319"></a><strong id="b34394499562"><a name="b34394499562"></a><a name="b34394499562"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p1099166216319"><a name="p1099166216319"></a><a name="p1099166216319"></a><strong id="b44117074"><a name="b44117074"></a><a name="b44117074"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.5.1.4"><p id="p1790939916319"><a name="p1790939916319"></a><a name="p1790939916319"></a><strong id="b431519678"><a name="b431519678"></a><a name="b431519678"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6305495416319"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p717763616319"><a name="p717763616319"></a><a name="p717763616319"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.1.5.1.2 "><p id="p4451766316319"><a name="p4451766316319"></a><a name="p4451766316319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p4916096316319"><a name="p4916096316319"></a><a name="p4916096316319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.5.1.4 "><p id="p2261503016319"><a name="p2261503016319"></a><a name="p2261503016319"></a>Phone number</p>
    <p id="p1987817916319"><a name="p1987817916319"></a><a name="p1987817916319"></a>The phone number must be preceded by a plus sign (+) and a country code.</p>
    </td>
    </tr>
    <tr id="row4468588616319"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p6278699416319"><a name="p6278699416319"></a><a name="p6278699416319"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.1.5.1.2 "><p id="p5258174716319"><a name="p5258174716319"></a><a name="p5258174716319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p3126308016319"><a name="p3126308016319"></a><a name="p3126308016319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.5.1.4 "><p id="p4928152916319"><a name="p4928152916319"></a><a name="p4928152916319"></a>SMS message content</p>
    <p id="p3238094416319"><a name="p3238094416319"></a><a name="p3238094416319"></a>If the content exceeds 256 bytes, the system will divide it into multiple messages, each containing 256 bytes at most and send only the first two.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/notifications/sms
    { 
       "endpoint": "+00111****1990", 
       "message": "SMS message test"
    }
    ```


## Response<a name="section3660902116319"></a>

-   Parameter description

    <a name="table916581816319"></a>
    <table><thead align="left"><tr id="row1992556516319"><th class="cellrowborder" valign="top" width="30.366963303669635%" id="mcps1.1.4.1.1"><p id="p335807316319"><a name="p335807316319"></a><a name="p335807316319"></a><strong id="b1555646738"><a name="b1555646738"></a><a name="b1555646738"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.97650234976503%" id="mcps1.1.4.1.2"><p id="p356849316319"><a name="p356849316319"></a><a name="p356849316319"></a><strong id="b828517610"><a name="b828517610"></a><a name="b828517610"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.656534346565344%" id="mcps1.1.4.1.3"><p id="p2061254616319"><a name="p2061254616319"></a><a name="p2061254616319"></a><strong id="b1855168186"><a name="b1855168186"></a><a name="b1855168186"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1455838216319"><td class="cellrowborder" valign="top" width="30.366963303669635%" headers="mcps1.1.4.1.1 "><p id="p3837826016319"><a name="p3837826016319"></a><a name="p3837826016319"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.97650234976503%" headers="mcps1.1.4.1.2 "><p id="p2163135516319"><a name="p2163135516319"></a><a name="p2163135516319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.656534346565344%" headers="mcps1.1.4.1.3 "><p id="p730932216319"><a name="p730932216319"></a><a name="p730932216319"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row2689606416319"><td class="cellrowborder" valign="top" width="30.366963303669635%" headers="mcps1.1.4.1.1 "><p id="p3109756416319"><a name="p3109756416319"></a><a name="p3109756416319"></a>message_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.97650234976503%" headers="mcps1.1.4.1.2 "><p id="p3587471616319"><a name="p3587471616319"></a><a name="p3587471616319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.656534346565344%" headers="mcps1.1.4.1.3 "><p id="p2017085616319"><a name="p2017085616319"></a><a name="p2017085616319"></a>Message ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
       "message_id": "bf94b63a5dfb475994d3ac34664e24f2", 
       "request_id": "9974c07f6d554a6d827956acbeb4be5f" 
    }
    ```


## Returned Value<a name="section754533616319"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

