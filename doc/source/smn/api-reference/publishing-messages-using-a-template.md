# Publishing Messages Using a Template<a name="smn_api_54003"></a>

## Description<a name="section52611782195031"></a>

-   API name

    Publish


-   Function

    Use the message template to publish a message to a topic. After the message ID is returned, the message has been saved and is to be pushed to the subscribers of the topic. This API allows you to send messages to different types of subscribers using different template protocols with the same name.


## URI<a name="section34827906195031"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/publish


-   Parameter description

    <a name="table19750057195031"></a>
    <table><thead align="left"><tr id="row6202146195031"><th class="cellrowborder" valign="top" width="17.441744174417444%" id="mcps1.1.5.1.1"><p id="p32611809195031"><a name="p32611809195031"></a><a name="p32611809195031"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.6018601860186%" id="mcps1.1.5.1.2"><p id="p24310897195031"><a name="p24310897195031"></a><a name="p24310897195031"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.6018601860186%" id="mcps1.1.5.1.3"><p id="p23025658195031"><a name="p23025658195031"></a><a name="p23025658195031"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.35453545354536%" id="mcps1.1.5.1.4"><p id="p53138979195031"><a name="p53138979195031"></a><a name="p53138979195031"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14292854195031"><td class="cellrowborder" valign="top" width="17.441744174417444%" headers="mcps1.1.5.1.1 "><p id="p16870512195031"><a name="p16870512195031"></a><a name="p16870512195031"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6018601860186%" headers="mcps1.1.5.1.2 "><p id="p24334251195031"><a name="p24334251195031"></a><a name="p24334251195031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6018601860186%" headers="mcps1.1.5.1.3 "><p id="p24917327195031"><a name="p24917327195031"></a><a name="p24917327195031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.35453545354536%" headers="mcps1.1.5.1.4 "><p id="p44538588155357"><a name="p44538588155357"></a><a name="p44538588155357"></a>Project ID</p>
    <p id="p5037570195031"><a name="p5037570195031"></a><a name="p5037570195031"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row48510570195031"><td class="cellrowborder" valign="top" width="17.441744174417444%" headers="mcps1.1.5.1.1 "><p id="p37042078195031"><a name="p37042078195031"></a><a name="p37042078195031"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6018601860186%" headers="mcps1.1.5.1.2 "><p id="p47618335195031"><a name="p47618335195031"></a><a name="p47618335195031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6018601860186%" headers="mcps1.1.5.1.3 "><p id="p31879892195031"><a name="p31879892195031"></a><a name="p31879892195031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.35453545354536%" headers="mcps1.1.5.1.4 "><p id="p32134437195031"><a name="p32134437195031"></a><a name="p32134437195031"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45105086195031"></a>

-   Parameter description

    <a name="table51492393195031"></a>
    <table><thead align="left"><tr id="row30761845195031"><th class="cellrowborder" valign="top" width="23.627637236276374%" id="mcps1.1.5.1.1"><p id="p8681487195031"><a name="p8681487195031"></a><a name="p8681487195031"></a><strong id="b822464551"><a name="b822464551"></a><a name="b822464551"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.65793420657934%" id="mcps1.1.5.1.2"><p id="p32111829195031"><a name="p32111829195031"></a><a name="p32111829195031"></a><strong id="b2083279393642"><a name="b2083279393642"></a><a name="b2083279393642"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.1.5.1.3"><p id="p50921393195031"><a name="p50921393195031"></a><a name="p50921393195031"></a><strong id="b890199867"><a name="b890199867"></a><a name="b890199867"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.28657134286571%" id="mcps1.1.5.1.4"><p id="p30992136195031"><a name="p30992136195031"></a><a name="p30992136195031"></a><strong id="b544632927"><a name="b544632927"></a><a name="b544632927"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66660173195031"><td class="cellrowborder" valign="top" width="23.627637236276374%" headers="mcps1.1.5.1.1 "><p id="p30764938195031"><a name="p30764938195031"></a><a name="p30764938195031"></a>subject</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.65793420657934%" headers="mcps1.1.5.1.2 "><p id="p8932068195031"><a name="p8932068195031"></a><a name="p8932068195031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.3 "><p id="p52408898195031"><a name="p52408898195031"></a><a name="p52408898195031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.1.5.1.4 "><p id="p17262349195031"><a name="p17262349195031"></a><a name="p17262349195031"></a>Message subject, which is presented as the email subject when SMN sends massages to email subscribers</p>
    <p id="p56073004195031"><a name="p56073004195031"></a><a name="p56073004195031"></a>The message subject cannot exceed 512 bytes.</p>
    </td>
    </tr>
    <tr id="row34894991195031"><td class="cellrowborder" valign="top" width="23.627637236276374%" headers="mcps1.1.5.1.1 "><p id="p7921992195031"><a name="p7921992195031"></a><a name="p7921992195031"></a>message_template_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.65793420657934%" headers="mcps1.1.5.1.2 "><p id="p37701577195031"><a name="p37701577195031"></a><a name="p37701577195031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.3 "><p id="p33928891195031"><a name="p33928891195031"></a><a name="p33928891195031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.1.5.1.4 "><p id="p63885637195031"><a name="p63885637195031"></a><a name="p63885637195031"></a>Message template name, which can be obtained according to <a href="querying-message-templates.md">Querying Message Templates</a></p>
    <div class="note" id="note72738487427"><a name="note72738487427"></a><a name="note72738487427"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p27477201192714"><a name="p27477201192714"></a><a name="p27477201192714"></a>Three message formats are supported:</p>
    <a name="ul13774005193124"></a><a name="ul13774005193124"></a><ul id="ul13774005193124"><li>message</li><li>message_structure</li><li>message_template_name</li></ul>
    <p id="p4935176193233"><a name="p4935176193233"></a><a name="p4935176193233"></a>If the three formats are specified at the same time, they take effect in the following sequence:</p>
    <p id="p24212931193236"><a name="p24212931193236"></a><a name="p24212931193236"></a>message_structure&gt;message_template_name&gt;message</p>
    </div></div>
    </td>
    </tr>
    <tr id="row66187157195031"><td class="cellrowborder" valign="top" width="23.627637236276374%" headers="mcps1.1.5.1.1 "><p id="p59559524195031"><a name="p59559524195031"></a><a name="p59559524195031"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.65793420657934%" headers="mcps1.1.5.1.2 "><p id="p59592135195031"><a name="p59592135195031"></a><a name="p59592135195031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.3 "><p id="p62233639195031"><a name="p62233639195031"></a><a name="p62233639195031"></a>JSON key-value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.1.5.1.4 "><p id="p7759979195031"><a name="p7759979195031"></a><a name="p7759979195031"></a>Variable parameters and values</p>
    <p id="p755417206436"><a name="p755417206436"></a><a name="p755417206436"></a>The value cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row78834110147"><td class="cellrowborder" valign="top" width="23.627637236276374%" headers="mcps1.1.5.1.1 "><p id="p23681125515"><a name="p23681125515"></a><a name="p23681125515"></a>time_to_live</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.65793420657934%" headers="mcps1.1.5.1.2 "><p id="p23681626518"><a name="p23681626518"></a><a name="p23681626518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.3 "><p id="p18075392520"><a name="p18075392520"></a><a name="p18075392520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.1.5.1.4 "><p id="p66191571978"><a name="p66191571978"></a><a name="p66191571978"></a>TTL of a message, specifically, the maximum time period for retaining the message in the system</p>
    <p id="p73858218511"><a name="p73858218511"></a><a name="p73858218511"></a>If the period expires, the system will discard the message. The time period is measured in seconds, and the default TTL is <strong id="b84235270617311"><a name="b84235270617311"></a><a name="b84235270617311"></a>3600s</strong> (one hour).</p>
    <p id="p163851021156"><a name="p163851021156"></a><a name="p163851021156"></a>The value must be a positive integer less than or equal to 604,800 (3600 x 24 x 7).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId: f96188c7ccaf4ffba0c9aa149ab2bd57:test_create_topic_v2/publish
    ```

    ```
    {
        "subject": "test message template v2",
        "message_template_name": "confirm_message",
        "time_to_live":"3600",
        "tags": {
            "topic_urn": "topic_urn3331",
            "topic_id": "topic_id3332"
        }
    }
    ```


## Response<a name="section12227696195031"></a>

-   Parameter description

    <a name="table30822526195031"></a>
    <table><thead align="left"><tr id="row47162257195031"><th class="cellrowborder" valign="top" width="37.70622937706229%" id="mcps1.1.4.1.1"><p id="p62046506195031"><a name="p62046506195031"></a><a name="p62046506195031"></a><strong id="b175458084"><a name="b175458084"></a><a name="b175458084"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.257274272572747%" id="mcps1.1.4.1.2"><p id="p59711095195031"><a name="p59711095195031"></a><a name="p59711095195031"></a><strong id="b349188857"><a name="b349188857"></a><a name="b349188857"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.03649635036496%" id="mcps1.1.4.1.3"><p id="p4760545195031"><a name="p4760545195031"></a><a name="p4760545195031"></a><strong id="b128559554"><a name="b128559554"></a><a name="b128559554"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28316458195031"><td class="cellrowborder" valign="top" width="37.70622937706229%" headers="mcps1.1.4.1.1 "><p id="p11931737195031"><a name="p11931737195031"></a><a name="p11931737195031"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.257274272572747%" headers="mcps1.1.4.1.2 "><p id="p26946629195031"><a name="p26946629195031"></a><a name="p26946629195031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.03649635036496%" headers="mcps1.1.4.1.3 "><p id="p35193301195031"><a name="p35193301195031"></a><a name="p35193301195031"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row20330496195031"><td class="cellrowborder" valign="top" width="37.70622937706229%" headers="mcps1.1.4.1.1 "><p id="p36157466195031"><a name="p36157466195031"></a><a name="p36157466195031"></a>message_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.257274272572747%" headers="mcps1.1.4.1.2 "><p id="p43073653195031"><a name="p43073653195031"></a><a name="p43073653195031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.03649635036496%" headers="mcps1.1.4.1.3 "><p id="p66413881195031"><a name="p66413881195031"></a><a name="p66413881195031"></a>Message ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "message_id": "bf94b63a5dfb475994d3ac34664e24f2",
        "request_id": "9974c07f6d554a6d827956acbeb4be5f"
    }
    ```


## Returned Value<a name="section340897195031"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

