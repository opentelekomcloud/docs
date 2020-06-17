# Creating and Importing an SSH Key Pair \(Native OpenStack API\)<a name="EN-US_TOPIC_0060384660"></a>

## Function<a name="section46928615105534"></a>

This interface is used to create an SSH key pair or import a public key to generate a key pair.

After an SSH key is created, download the private key to a local directory. Then, you can use this private key to log in to the BMS. To ensure BMS security, the private key can be downloaded only once. Keep it secure.

## URI<a name="section3181044105534"></a>

POST /v2.1/\{project\_id\}/os-keypairs

[Table 1](#table137043339568)  lists the parameters.

**Table  1**  Parameter description

<a name="table137043339568"></a>
<table><thead align="left"><tr id="row6707133385614"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p16860355105534"><a name="p16860355105534"></a><a name="p16860355105534"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p23511481105534"><a name="p23511481105534"></a><a name="p23511481105534"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p25381808105534"><a name="p25381808105534"></a><a name="p25381808105534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1170718332563"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p32953279105534"><a name="p32953279105534"></a><a name="p32953279105534"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51969960105534"><a name="p51969960105534"></a><a name="p51969960105534"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48817201105534"><a name="p48817201105534"></a><a name="p48817201105534"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section61879170105534"></a>

-   Request parameters

    >![](/images/icon-note.gif) **NOTE:**   
    >When creating an SSH key pair, you only need to configure  **name**. When importing a public SSH key, you must also configure  **public\_key**.  

    <a name="table40018745105534"></a>
    <table><thead align="left"><tr id="row48164488105534"><th class="cellrowborder" valign="top" width="19.37%" id="mcps1.1.5.1.1"><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.09%" id="mcps1.1.5.1.2"><p id="p09341937982"><a name="p09341937982"></a><a name="p09341937982"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.93%" id="mcps1.1.5.1.3"><p id="p4546697"><a name="p4546697"></a><a name="p4546697"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.61%" id="mcps1.1.5.1.4"><p id="p32738149"><a name="p32738149"></a><a name="p32738149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6972410105534"><td class="cellrowborder" valign="top" width="19.37%" headers="mcps1.1.5.1.1 "><p id="p27894300105534"><a name="p27894300105534"></a><a name="p27894300105534"></a>keypair</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.2 "><p id="p993423719814"><a name="p993423719814"></a><a name="p993423719814"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.5.1.3 "><p id="p8634695105534"><a name="p8634695105534"></a><a name="p8634695105534"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.61%" headers="mcps1.1.5.1.4 "><p id="p28321695105534"><a name="p28321695105534"></a><a name="p28321695105534"></a>Specifies the created or imported SSH key pair. For details, see <a href="#table44094886105534">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **keypair**  field data structure description

    <a name="table44094886105534"></a>
    <table><thead align="left"><tr id="row40587827105534"><th class="cellrowborder" valign="top" width="20.59205920592059%" id="mcps1.2.5.1.1"><p id="p16104135417242"><a name="p16104135417242"></a><a name="p16104135417242"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.601560156015601%" id="mcps1.2.5.1.2"><p id="p14086419811"><a name="p14086419811"></a><a name="p14086419811"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.02240224022402%" id="mcps1.2.5.1.3"><p id="p1110685412246"><a name="p1110685412246"></a><a name="p1110685412246"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.78397839783978%" id="mcps1.2.5.1.4"><p id="p41093543243"><a name="p41093543243"></a><a name="p41093543243"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49263560105534"><td class="cellrowborder" valign="top" width="20.59205920592059%" headers="mcps1.2.5.1.1 "><p id="p30925442105534"><a name="p30925442105534"></a><a name="p30925442105534"></a>public_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.601560156015601%" headers="mcps1.2.5.1.2 "><p id="p9407741984"><a name="p9407741984"></a><a name="p9407741984"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.02240224022402%" headers="mcps1.2.5.1.3 "><p id="p31731563105534"><a name="p31731563105534"></a><a name="p31731563105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.78397839783978%" headers="mcps1.2.5.1.4 "><p id="p20119786105534"><a name="p20119786105534"></a><a name="p20119786105534"></a>Specifies the imported public key. The maximum size of the imported public key is 1024 bytes.</p>
    <p id="p46860349105534"><a name="p46860349105534"></a><a name="p46860349105534"></a>Note: If the length of the public key to be imported exceeds 1024 bytes, the public key import to the <span id="text10252131514405"><a name="text10252131514405"></a><a name="text10252131514405"></a>BMS</span><span id="text42529159407"><a name="text42529159407"></a><a name="text42529159407"></a></span> will fail.</p>
    </td>
    </tr>
    <tr id="row19089958105534"><td class="cellrowborder" valign="top" width="20.59205920592059%" headers="mcps1.2.5.1.1 "><p id="p2782726105534"><a name="p2782726105534"></a><a name="p2782726105534"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.601560156015601%" headers="mcps1.2.5.1.2 "><p id="p040720411810"><a name="p040720411810"></a><a name="p040720411810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.02240224022402%" headers="mcps1.2.5.1.3 "><p id="p3855315105534"><a name="p3855315105534"></a><a name="p3855315105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.78397839783978%" headers="mcps1.2.5.1.4 "><p id="p43845137105534"><a name="p43845137105534"></a><a name="p43845137105534"></a>Specifies the key pair name.</p>
    <p id="p59061918105534"><a name="p59061918105534"></a><a name="p59061918105534"></a>The new key pair name cannot be the same as an existing one.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs
    ```

    ```
    {
        "keypair": {
            "name": "keypair-7d7c3650-dabe-4eb0-b904-5c464453c043",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC9mC3WZN9UGLxgPBpP7H5jZMc6pKwOoSgre8yun6REFktn/Kz7DUt9jaR1UJyRzHxITfCfAIgSxPdGqB/oF1suMyWgu5i0625vavLB5z5kC8Hq3qZJ9zJO1poE1kyD+htiTtPWJ88e12xuH2XB/CZN9OpEiF98hAagiOE0EnOS5Q== Generated by Nova\n"
        }
    }
    ```


## Response Message<a name="section33789573105534"></a>

-   Response parameters

    <a name="table32814569105534"></a>
    <table><thead align="left"><tr id="row31072960105534"><th class="cellrowborder" valign="top" width="24.39%" id="mcps1.1.4.1.1"><p id="p104001675252"><a name="p104001675252"></a><a name="p104001675252"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.270000000000003%" id="mcps1.1.4.1.2"><p id="p840215762519"><a name="p840215762519"></a><a name="p840215762519"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.339999999999996%" id="mcps1.1.4.1.3"><p id="p1040516718253"><a name="p1040516718253"></a><a name="p1040516718253"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30545796105534"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p58290412105534"><a name="p58290412105534"></a><a name="p58290412105534"></a>keypair</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.1.4.1.2 "><p id="p23902945105534"><a name="p23902945105534"></a><a name="p23902945105534"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.1.4.1.3 "><p id="p57090378105534"><a name="p57090378105534"></a><a name="p57090378105534"></a>Specifies the SSH key pair. For details, see <a href="#table11390225105534">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **keypair**  field data structure description

    <a name="table11390225105534"></a>
    <table><thead align="left"><tr id="row13107196105534"><th class="cellrowborder" valign="top" width="24.39%" id="mcps1.2.4.1.1"><p id="p4172201014255"><a name="p4172201014255"></a><a name="p4172201014255"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.270000000000003%" id="mcps1.2.4.1.2"><p id="p10173141011254"><a name="p10173141011254"></a><a name="p10173141011254"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.339999999999996%" id="mcps1.2.4.1.3"><p id="p817617100257"><a name="p817617100257"></a><a name="p817617100257"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45769827105534"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.1 "><p id="p16368506105534"><a name="p16368506105534"></a><a name="p16368506105534"></a>fingerprint</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p50780601105534"><a name="p50780601105534"></a><a name="p50780601105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p19588041105534"><a name="p19588041105534"></a><a name="p19588041105534"></a>Specifies fingerprint information about the key pair.</p>
    </td>
    </tr>
    <tr id="row42074647105534"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.1 "><p id="p52603235105534"><a name="p52603235105534"></a><a name="p52603235105534"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p33003603105534"><a name="p33003603105534"></a><a name="p33003603105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p56046159105534"><a name="p56046159105534"></a><a name="p56046159105534"></a>Specifies the key pair name.</p>
    </td>
    </tr>
    <tr id="row34653390105534"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.1 "><p id="p55461192105534"><a name="p55461192105534"></a><a name="p55461192105534"></a>public_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p63171587105534"><a name="p63171587105534"></a><a name="p63171587105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p16624935105534"><a name="p16624935105534"></a><a name="p16624935105534"></a>Specifies the public key.</p>
    </td>
    </tr>
    <tr id="row15406687105534"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.1 "><p id="p39982130105534"><a name="p39982130105534"></a><a name="p39982130105534"></a>private_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p17327106105534"><a name="p17327106105534"></a><a name="p17327106105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p61318326105534"><a name="p61318326105534"></a><a name="p61318326105534"></a>Specifies the private key.</p>
    <a name="ul53408548183356"></a><a name="ul53408548183356"></a><ul id="ul53408548183356"><li>The information about the private key is contained in the response for creating an SSH key.</li><li>The information about the private key is not contained in the response for importing an SSH key.</li></ul>
    </td>
    </tr>
    <tr id="row14994025105534"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.1 "><p id="p6556527105534"><a name="p6556527105534"></a><a name="p6556527105534"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p61316685105534"><a name="p61316685105534"></a><a name="p61316685105534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p595628105534"><a name="p595628105534"></a><a name="p595628105534"></a>Specifies the ID of the user to which the key pair belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "keypair": {
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC9mC3WZN9UGLxgPBpP7H5jZMc6pKwOoSgre8yun6REFktn/Kz7DUt9jaR1UJyRzHxITfCfAIgSxPdGqB/oF1suMyWgu5i0625vavLB5z5kC8Hq3qZJ9zJO1poE1kyD+htiTtPWJ88e12xuH2XB/CZN9OpEiF98hAagiOE0EnOS5Q== Generated by Nova\n",
            "user_id": "f882feb345064e7d9392440a0f397c25",
            "name": "keypair-7d7c3650-dabe-4eb0-b904-5c464453c043",
            "fingerprint": "35:9d:d0:c3:4a:80:d3:d8:86:f1:ca:f7:df:c4:f9:d8"
        }
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

