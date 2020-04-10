# Deleting a User<a name="en-us_topic_0057845630"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to delete a user.

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

-   URI format

    DELETE /v3/users/\{user\_id\}

-   URI parameter description

    <a name="en-us_topic_0032920337_table29648085"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920337_row12693918"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920337_p21574462"><a name="en-us_topic_0032920337_p21574462"></a><a name="en-us_topic_0032920337_p21574462"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.56%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920337_p2701015"><a name="en-us_topic_0032920337_p2701015"></a><a name="en-us_topic_0032920337_p2701015"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.15%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920337_p17455632"><a name="en-us_topic_0032920337_p17455632"></a><a name="en-us_topic_0032920337_p17455632"></a><strong id="b84235270615026"><a name="b84235270615026"></a><a name="b84235270615026"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.67%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920337_p4620049"><a name="en-us_topic_0032920337_p4620049"></a><a name="en-us_topic_0032920337_p4620049"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920337_row38679683"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920337_p46046605"><a name="en-us_topic_0032920337_p46046605"></a><a name="en-us_topic_0032920337_p46046605"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920337_p38787544"><a name="en-us_topic_0032920337_p38787544"></a><a name="en-us_topic_0032920337_p38787544"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920337_p54783372"><a name="en-us_topic_0032920337_p54783372"></a><a name="en-us_topic_0032920337_p54783372"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.67%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920337_p8268111"><a name="en-us_topic_0032920337_p8268111"></a><a name="en-us_topic_0032920337_p8268111"></a>User ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="20.48795120487951%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><strong id="b427191154"><a name="b427191154"></a><a name="b427191154"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.558044195580443%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.41785821417858%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><strong id="b1171596115"><a name="b1171596115"></a><a name="b1171596115"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.53614638536146%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><strong id="b698326504"><a name="b698326504"></a><a name="b698326504"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.558044195580443%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41785821417858%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.53614638536146%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row29501427115257"><td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.1.5.1.1 "><p id="p6637478211538"><a name="p6637478211538"></a><a name="p6637478211538"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.558044195580443%" headers="mcps1.1.5.1.2 "><p id="p764826811538"><a name="p764826811538"></a><a name="p764826811538"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41785821417858%" headers="mcps1.1.5.1.3 "><p id="p1553001111538"><a name="p1553001111538"></a><a name="p1553001111538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.53614638536146%" headers="mcps1.1.5.1.4 "><p id="p3577810173953"><a name="p3577810173953"></a><a name="p3577810173953"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X DELETE https://172.30.48.86:31943/v3/users/2c1c6c54e59141b889c99e6fada5f19f
    ```


## Response<a name="section32534340162829"></a>

No response body.

## Status Codes<a name="sbfe93ca4c2b9427dbb2218a4e72da6a8"></a>

<a name="en-us_topic_0035544336_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0035544336_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035544336_p51565323"><a name="en-us_topic_0035544336_p51565323"></a><a name="en-us_topic_0035544336_p51565323"></a><strong id="b842352706104328"><a name="b842352706104328"></a><a name="b842352706104328"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035544336_p16041657"><a name="en-us_topic_0035544336_p16041657"></a><a name="en-us_topic_0035544336_p16041657"></a><strong id="b1922147876"><a name="b1922147876"></a><a name="b1922147876"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035544336_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p22613965"><a name="en-us_topic_0035544336_p22613965"></a><a name="en-us_topic_0035544336_p22613965"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p19791876"><a name="en-us_topic_0035544336_p19791876"></a><a name="en-us_topic_0035544336_p19791876"></a>The user is deleted successfully.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p66980994"><a name="en-us_topic_0035544336_p66980994"></a><a name="en-us_topic_0035544336_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p56751409"><a name="en-us_topic_0035544336_p56751409"></a><a name="en-us_topic_0035544336_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="rb99fbab78bc54ae4953661763b573830"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aef55745ff0834933af36d690e2e339b8"><a name="aef55745ff0834933af36d690e2e339b8"></a><a name="aef55745ff0834933af36d690e2e339b8"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a480215738ced4bf5a8feafa2681db93b"><a name="a480215738ced4bf5a8feafa2681db93b"></a><a name="a480215738ced4bf5a8feafa2681db93b"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p32717189"><a name="en-us_topic_0035544336_p32717189"></a><a name="en-us_topic_0035544336_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae678037f26d640f5a985c943e2ffb92e"><a name="ae678037f26d640f5a985c943e2ffb92e"></a><a name="ae678037f26d640f5a985c943e2ffb92e"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r1fd5c05b7b6b4c048f3f7b9ddbc755b0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5d7e2305922e4f9098442a900792dae1"><a name="a5d7e2305922e4f9098442a900792dae1"></a><a name="a5d7e2305922e4f9098442a900792dae1"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9edf299d0513460caaac8a2a19b76e9a"><a name="a9edf299d0513460caaac8a2a19b76e9a"></a><a name="a9edf299d0513460caaac8a2a19b76e9a"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rbb5133f150fd42eebde8dd6e390ecbd5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad1a2754016e44193a97043265cd611cf"><a name="ad1a2754016e44193a97043265cd611cf"></a><a name="ad1a2754016e44193a97043265cd611cf"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a81837d461ef445259c5a6e9e1ce0e32a"><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="r2cecff297b1a412f956a312d3cd7acc9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1f617621d1bc4a9facb1c84d1946002b"><a name="a1f617621d1bc4a9facb1c84d1946002b"></a><a name="a1f617621d1bc4a9facb1c84d1946002b"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac31ead3ee2db40eea8ae45b2779a09e9"><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="rd71e0e00759f4179a2dccaf345ba9f2f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1657c5ca5ebd4a2cbacbdb35fc9b7601"><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a88b4b14048564e12942b8151dc791b99"><a name="a88b4b14048564e12942b8151dc791b99"></a><a name="a88b4b14048564e12942b8151dc791b99"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="r5647e5fd26974514ac66cc3925f30601"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a16dfaa16ceac4a33a468c0ae158292fb"><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5635c1924d9648a8be89b1e5dcf0a87b"><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

