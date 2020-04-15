# Deleting a Message Template<a name="smn_api_53003"></a>

## Description<a name="section63379561"></a>

-   API name

    DeleteMessageTemplate


-   Function

    Delete a message template. After you delete the template, you cannot use it to publish messages any more.


## URI<a name="section33545144"></a>

-   URI format

    DELETE /v2/\{project\_id\}/notifications/message\_template/\{message\_template\_id\}


-   Parameter description

    <a name="table28042199"></a>
    <table><thead align="left"><tr id="row949529"><th class="cellrowborder" valign="top" width="29.299999999999997%" id="mcps1.1.5.1.1"><p id="p9803039"><a name="p9803039"></a><a name="p9803039"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.52%" id="mcps1.1.5.1.2"><p id="p55848701"><a name="p55848701"></a><a name="p55848701"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.91%" id="mcps1.1.5.1.3"><p id="p27450972"><a name="p27450972"></a><a name="p27450972"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.27%" id="mcps1.1.5.1.4"><p id="p8936292"><a name="p8936292"></a><a name="p8936292"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44975500"><td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.1.5.1.1 "><p id="p19136893"><a name="p19136893"></a><a name="p19136893"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.52%" headers="mcps1.1.5.1.2 "><p id="p6584502"><a name="p6584502"></a><a name="p6584502"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p63582688"><a name="p63582688"></a><a name="p63582688"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.27%" headers="mcps1.1.5.1.4 "><p id="p35042050155257"><a name="p35042050155257"></a><a name="p35042050155257"></a>Project ID</p>
    <p id="p49924131"><a name="p49924131"></a><a name="p49924131"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row21687383"><td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.1.5.1.1 "><p id="p11847581"><a name="p11847581"></a><a name="p11847581"></a>message_template_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.52%" headers="mcps1.1.5.1.2 "><p id="p20130041"><a name="p20130041"></a><a name="p20130041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p19920592"><a name="p19920592"></a><a name="p19920592"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.27%" headers="mcps1.1.5.1.4 "><p id="p2955276"><a name="p2955276"></a><a name="p2955276"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-message-templates.md">Querying Message Templates</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33470841"></a>

Request example

```
DELETE https://{SMN_Endpoint}/v2/{project_id}/notifications/message_template/b3ffa2cdda574168826316f0628f774e
```

## Response<a name="section32802119"></a>

-   Parameter description

    <a name="table29623765"></a>
    <table><thead align="left"><tr id="row55864401"><th class="cellrowborder" valign="top" width="32.28322832283228%" id="mcps1.1.4.1.1"><p id="p28722627"><a name="p28722627"></a><a name="p28722627"></a><strong id="b929850706"><a name="b929850706"></a><a name="b929850706"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.28322832283228%" id="mcps1.1.4.1.2"><p id="p44831437"><a name="p44831437"></a><a name="p44831437"></a><strong id="b433012975"><a name="b433012975"></a><a name="b433012975"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.433543354335434%" id="mcps1.1.4.1.3"><p id="p7467800"><a name="p7467800"></a><a name="p7467800"></a><strong id="b1815187841"><a name="b1815187841"></a><a name="b1815187841"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6769295"><td class="cellrowborder" valign="top" width="32.28322832283228%" headers="mcps1.1.4.1.1 "><p id="p11442060"><a name="p11442060"></a><a name="p11442060"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.28322832283228%" headers="mcps1.1.4.1.2 "><p id="p54391657"><a name="p54391657"></a><a name="p54391657"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.433543354335434%" headers="mcps1.1.4.1.3 "><p id="p43648078"><a name="p43648078"></a><a name="p43648078"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    { 
        "request_id": " 5fcba32bd2814ea39431829c22bda94b" 
    }
    ```


## Returned Value<a name="section26783618"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

