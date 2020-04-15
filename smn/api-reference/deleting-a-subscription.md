# Deleting a Subscription<a name="smn_api_52004"></a>

## Description<a name="section66924213"></a>

-   API name

    Unsubscribe


-   Function

    Delete a specified subscription.


## URI<a name="section65447007"></a>

-   URI format

    DELETE /v2/\{project\_id\}/notifications/subscriptions/\{subscription\_urn\}


-   Parameter description

    <a name="table28631516"></a>
    <table><thead align="left"><tr id="row30400092"><th class="cellrowborder" valign="top" width="29.7%" id="mcps1.1.5.1.1"><p id="p46488363"><a name="p46488363"></a><a name="p46488363"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.3%" id="mcps1.1.5.1.2"><p id="p7461047"><a name="p7461047"></a><a name="p7461047"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p365031"><a name="p365031"></a><a name="p365031"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p29567523"><a name="p29567523"></a><a name="p29567523"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47906786"><td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.1.5.1.1 "><p id="p55244468"><a name="p55244468"></a><a name="p55244468"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.2 "><p id="p45616947"><a name="p45616947"></a><a name="p45616947"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p3985222"><a name="p3985222"></a><a name="p3985222"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p20960620155139"><a name="p20960620155139"></a><a name="p20960620155139"></a>Project ID</p>
    <p id="p54367574"><a name="p54367574"></a><a name="p54367574"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row39731869"><td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.1.5.1.1 "><p id="p64164835"><a name="p64164835"></a><a name="p64164835"></a>subscription_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.2 "><p id="p29969153"><a name="p29969153"></a><a name="p29969153"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p11582368"><a name="p11582368"></a><a name="p11582368"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p65756648"><a name="p65756648"></a><a name="p65756648"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-subscriptions.md">Querying Subscriptions</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section52152158"></a>

Request example

```
DELETE https://{SMN_Endpoint}/v2/{project_id}/notifications/subscriptions/urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1:2e778e84408e44058e6cbc6d3c377837
```

## Response<a name="section66716242"></a>

-   Parameter description

    <a name="table20831783"></a>
    <table><thead align="left"><tr id="row35093725"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p24019444"><a name="p24019444"></a><a name="p24019444"></a><strong id="b808139197"><a name="b808139197"></a><a name="b808139197"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p66526832"><a name="p66526832"></a><a name="p66526832"></a><strong id="b318690054"><a name="b318690054"></a><a name="b318690054"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p19964345"><a name="p19964345"></a><a name="p19964345"></a><strong id="b349226858"><a name="b349226858"></a><a name="b349226858"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56677584"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p27481582"><a name="p27481582"></a><a name="p27481582"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p11415673"><a name="p11415673"></a><a name="p11415673"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p52254296"><a name="p52254296"></a><a name="p52254296"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "request_id":"f3197b274a6b473a8007eed79e716c30"
    }
    ```


## Returned Value<a name="section63575268"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

