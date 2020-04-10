# Obtaining a Scoped Token in Federated Identity Authentication Mode<a name="en-us_topic_0057845636"></a>

## Function Description<a name="section42419535165356"></a>

This interface is used to obtain a scoped token in federated identity authentication mode.

## URI<a name="section53764282165356"></a>

URI format

POST /v3/auth/tokens

## Request<a name="section27720749165356"></a>

-   Request header parameter description

    <a name="table30788231165356"></a>
    <table><thead align="left"><tr id="row30649228165356"><th class="cellrowborder" valign="top" width="18.801880188018803%" id="mcps1.1.5.1.1"><p id="p66668440165356"><a name="p66668440165356"></a><a name="p66668440165356"></a><strong id="b842352706183148_1"><a name="b842352706183148_1"></a><a name="b842352706183148_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.921892189218923%" id="mcps1.1.5.1.2"><p id="p31434527165356"><a name="p31434527165356"></a><a name="p31434527165356"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.31183118311831%" id="mcps1.1.5.1.3"><p id="p63168779165356"><a name="p63168779165356"></a><a name="p63168779165356"></a><strong id="b842352706112524_1"><a name="b842352706112524_1"></a><a name="b842352706112524_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.96439643964396%" id="mcps1.1.5.1.4"><p id="p16397508165356"><a name="p16397508165356"></a><a name="p16397508165356"></a><strong id="a76acf34e8e7b48948763ec1b460ad92f"><a name="a76acf34e8e7b48948763ec1b460ad92f"></a><a name="a76acf34e8e7b48948763ec1b460ad92f"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53129777165356"><td class="cellrowborder" valign="top" width="18.801880188018803%" headers="mcps1.1.5.1.1 "><p id="p8544699165356"><a name="p8544699165356"></a><a name="p8544699165356"></a>identity</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.921892189218923%" headers="mcps1.1.5.1.2 "><p id="p21032009165356"><a name="p21032009165356"></a><a name="p21032009165356"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.31183118311831%" headers="mcps1.1.5.1.3 "><p id="p25871172165356"><a name="p25871172165356"></a><a name="p25871172165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.96439643964396%" headers="mcps1.1.5.1.4 "><p id="p15190163165356"><a name="p15190163165356"></a><a name="p15190163165356"></a>Authentication information, such as user passwords.</p>
    </td>
    </tr>
    <tr id="row2493742165356"><td class="cellrowborder" valign="top" width="18.801880188018803%" headers="mcps1.1.5.1.1 "><p id="p666519165356"><a name="p666519165356"></a><a name="p666519165356"></a>scope</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.921892189218923%" headers="mcps1.1.5.1.2 "><p id="p53988040165356"><a name="p53988040165356"></a><a name="p53988040165356"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.31183118311831%" headers="mcps1.1.5.1.3 "><p id="p10955114165356"><a name="p10955114165356"></a><a name="p10955114165356"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.96439643964396%" headers="mcps1.1.5.1.4 "><p id="p14949028165356"><a name="p14949028165356"></a><a name="p14949028165356"></a>Scope of a token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the identity format

    <a name="table27471026124712"></a>
    <table><thead align="left"><tr id="row19745112634711"><th class="cellrowborder" valign="top" width="18.828117188281173%" id="mcps1.1.5.1.1"><p id="p374315264471"><a name="p374315264471"></a><a name="p374315264471"></a><strong id="b842352706183154"><a name="b842352706183154"></a><a name="b842352706183154"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.938106189381063%" id="mcps1.1.5.1.2"><p id="p77441262478"><a name="p77441262478"></a><a name="p77441262478"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.098190180981902%" id="mcps1.1.5.1.3"><p id="p127441426154710"><a name="p127441426154710"></a><a name="p127441426154710"></a><strong id="b842352706112524_3"><a name="b842352706112524_3"></a><a name="b842352706112524_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.13558644135587%" id="mcps1.1.5.1.4"><p id="p1674414264474"><a name="p1674414264474"></a><a name="p1674414264474"></a><strong id="b33659860164859_1"><a name="b33659860164859_1"></a><a name="b33659860164859_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1274672684715"><td class="cellrowborder" valign="top" width="18.828117188281173%" headers="mcps1.1.5.1.1 "><p id="p174572624718"><a name="p174572624718"></a><a name="p174572624718"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.938106189381063%" headers="mcps1.1.5.1.2 "><p id="p0745152644712"><a name="p0745152644712"></a><a name="p0745152644712"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.098190180981902%" headers="mcps1.1.5.1.3 "><p id="p107451826104714"><a name="p107451826104714"></a><a name="p107451826104714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.13558644135587%" headers="mcps1.1.5.1.4 "><p id="p874672694719"><a name="p874672694719"></a><a name="p874672694719"></a>The value of this parameter is <strong id="b842352706171814"><a name="b842352706171814"></a><a name="b842352706171814"></a>token</strong>.</p>
    </td>
    </tr>
    <tr id="row9747162684713"><td class="cellrowborder" valign="top" width="18.828117188281173%" headers="mcps1.1.5.1.1 "><p id="p974632614716"><a name="p974632614716"></a><a name="p974632614716"></a>token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.938106189381063%" headers="mcps1.1.5.1.2 "><p id="p18746102613478"><a name="p18746102613478"></a><a name="p18746102613478"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.098190180981902%" headers="mcps1.1.5.1.3 "><p id="p137461226154713"><a name="p137461226154713"></a><a name="p137461226154713"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.13558644135587%" headers="mcps1.1.5.1.4 "><p id="p6747626184710"><a name="p6747626184710"></a><a name="p6747626184710"></a>Unscoped token obtained in federated identity authentication mode.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the token format

    <a name="table58557049165356"></a>
    <table><thead align="left"><tr id="row57181345165356"><th class="cellrowborder" valign="top" width="18.5%" id="mcps1.1.5.1.1"><p id="p1177374165356"><a name="p1177374165356"></a><a name="p1177374165356"></a><strong id="b842352706183148_3"><a name="b842352706183148_3"></a><a name="b842352706183148_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.15%" id="mcps1.1.5.1.2"><p id="p28258488165356"><a name="p28258488165356"></a><a name="p28258488165356"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.3"><p id="p7236182165356"><a name="p7236182165356"></a><a name="p7236182165356"></a><strong id="b842352706112524_5"><a name="b842352706112524_5"></a><a name="b842352706112524_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.12%" id="mcps1.1.5.1.4"><p id="p49259873165356"><a name="p49259873165356"></a><a name="p49259873165356"></a><strong id="b58136869164859"><a name="b58136869164859"></a><a name="b58136869164859"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30626752165356"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.5.1.1 "><p id="p64847836165356"><a name="p64847836165356"></a><a name="p64847836165356"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.1.5.1.2 "><p id="p18183324165356"><a name="p18183324165356"></a><a name="p18183324165356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.3 "><p id="p63563112165356"><a name="p63563112165356"></a><a name="p63563112165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.12%" headers="mcps1.1.5.1.4 "><p id="p48338473165356"><a name="p48338473165356"></a><a name="p48338473165356"></a>ID of an unscoped token obtained in federated identity authentication mode for authentication.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the scope format

    <a name="table885236173217"></a>
    <table><thead align="left"><tr id="row685112653213"><th class="cellrowborder" valign="top" width="18.51814818518148%" id="mcps1.1.5.1.1"><p id="p16851136173217"><a name="p16851136173217"></a><a name="p16851136173217"></a><strong id="b842352706183159"><a name="b842352706183159"></a><a name="b842352706183159"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.868113188681132%" id="mcps1.1.5.1.2"><p id="p10851176113213"><a name="p10851176113213"></a><a name="p10851176113213"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_7"><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.528147185281473%" id="mcps1.1.5.1.3"><p id="p198511162322"><a name="p198511162322"></a><a name="p198511162322"></a><strong id="b842352706112524_7"><a name="b842352706112524_7"></a><a name="b842352706112524_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.085591440855914%" id="mcps1.1.5.1.4"><p id="p10851186113210"><a name="p10851186113210"></a><a name="p10851186113210"></a><strong id="b3315065164859"><a name="b3315065164859"></a><a name="b3315065164859"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1285117612323"><td class="cellrowborder" valign="top" width="18.51814818518148%" headers="mcps1.1.5.1.1 "><p id="p19851186123215"><a name="p19851186123215"></a><a name="p19851186123215"></a>project</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.868113188681132%" headers="mcps1.1.5.1.2 "><p id="p17851196103215"><a name="p17851196103215"></a><a name="p17851196103215"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.1.5.1.3 "><p id="p78517663212"><a name="p78517663212"></a><a name="p78517663212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.085591440855914%" headers="mcps1.1.5.1.4 "><p id="p198511263325"><a name="p198511263325"></a><a name="p198511263325"></a>Project. Select either <strong id="b62485687816342"><a name="b62485687816342"></a><a name="b62485687816342"></a>project</strong> or <strong id="b111203407816342"><a name="b111203407816342"></a><a name="b111203407816342"></a>domain</strong>.</p>
    </td>
    </tr>
    <tr id="row1185218612327"><td class="cellrowborder" valign="top" width="18.51814818518148%" headers="mcps1.1.5.1.1 "><p id="p1785156133220"><a name="p1785156133220"></a><a name="p1785156133220"></a>domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.868113188681132%" headers="mcps1.1.5.1.2 "><p id="p9851562322"><a name="p9851562322"></a><a name="p9851562322"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.1.5.1.3 "><p id="p148514693210"><a name="p148514693210"></a><a name="p148514693210"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.085591440855914%" headers="mcps1.1.5.1.4 "><p id="p6852769329"><a name="p6852769329"></a><a name="p6852769329"></a>Domain. Select either <strong id="b183910003616351"><a name="b183910003616351"></a><a name="b183910003616351"></a>project</strong> or <strong id="b10108941616351"><a name="b10108941616351"></a><a name="b10108941616351"></a>domain</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the project format

    <a name="table185213613324"></a>
    <table><thead align="left"><tr id="row58523623213"><th class="cellrowborder" valign="top" width="18.64%" id="mcps1.1.5.1.1"><p id="p148524618329"><a name="p148524618329"></a><a name="p148524618329"></a><strong id="b84235270618326"><a name="b84235270618326"></a><a name="b84235270618326"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.96%" id="mcps1.1.5.1.2"><p id="p108529614329"><a name="p108529614329"></a><a name="p108529614329"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_9"><a name="a703d34a49a2f4162bc1a1a439f655f95_9"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.04%" id="mcps1.1.5.1.3"><p id="p2085206143211"><a name="p2085206143211"></a><a name="p2085206143211"></a><strong id="b842352706112524_9"><a name="b842352706112524_9"></a><a name="b842352706112524_9"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.36%" id="mcps1.1.5.1.4"><p id="p085266183215"><a name="p085266183215"></a><a name="p085266183215"></a><strong id="b9680508164859_1"><a name="b9680508164859_1"></a><a name="b9680508164859_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row188527614325"><td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.1 "><p id="p48521765325"><a name="p48521765325"></a><a name="p48521765325"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p1085206113220"><a name="p1085206113220"></a><a name="p1085206113220"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.3 "><p id="p1852136113217"><a name="p1852136113217"></a><a name="p1852136113217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.5.1.4 "><p id="p1085215673210"><a name="p1085215673210"></a><a name="p1085215673210"></a>Project name. Select either <strong id="b4927124741645"><a name="b4927124741645"></a><a name="b4927124741645"></a>name</strong> or <strong id="b12892450111645"><a name="b12892450111645"></a><a name="b12892450111645"></a>id</strong>.</p>
    </td>
    </tr>
    <tr id="row178523693219"><td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.1 "><p id="p13852156173216"><a name="p13852156173216"></a><a name="p13852156173216"></a>domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p11852566322"><a name="p11852566322"></a><a name="p11852566322"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.3 "><p id="p1785214618321"><a name="p1785214618321"></a><a name="p1785214618321"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.5.1.4 "><p id="p14852968329"><a name="p14852968329"></a><a name="p14852968329"></a>Domain to which a project belongs. This parameter is mandatory when the <strong id="b182466741716414"><a name="b182466741716414"></a><a name="b182466741716414"></a>name</strong> parameter is used.</p>
    </td>
    </tr>
    <tr id="row1185216653210"><td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.1 "><p id="p2085256163212"><a name="p2085256163212"></a><a name="p2085256163212"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p16852869327"><a name="p16852869327"></a><a name="p16852869327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04%" headers="mcps1.1.5.1.3 "><p id="p185218614324"><a name="p185218614324"></a><a name="p185218614324"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.5.1.4 "><p id="p20852106173210"><a name="p20852106173210"></a><a name="p20852106173210"></a>Project ID. Select either <strong id="b52656080716423"><a name="b52656080716423"></a><a name="b52656080716423"></a>name</strong> or <strong id="b160866423916423"><a name="b160866423916423"></a><a name="b160866423916423"></a>id</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the domain format

    <a name="table385317643214"></a>
    <table><thead align="left"><tr id="row185313613214"><th class="cellrowborder" valign="top" width="18.5%" id="mcps1.1.5.1.1"><p id="p9853106143216"><a name="p9853106143216"></a><a name="p9853106143216"></a><strong id="b842352706183212"><a name="b842352706183212"></a><a name="b842352706183212"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.96%" id="mcps1.1.5.1.2"><p id="p1485315673214"><a name="p1485315673214"></a><a name="p1485315673214"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_11"><a name="a703d34a49a2f4162bc1a1a439f655f95_11"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.9%" id="mcps1.1.5.1.3"><p id="p985346193217"><a name="p985346193217"></a><a name="p985346193217"></a><strong id="b842352706112524_11"><a name="b842352706112524_11"></a><a name="b842352706112524_11"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.64%" id="mcps1.1.5.1.4"><p id="p1285317613325"><a name="p1285317613325"></a><a name="p1285317613325"></a><strong id="b9680508164859_3"><a name="b9680508164859_3"></a><a name="b9680508164859_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1185313653210"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.5.1.1 "><p id="p4853062327"><a name="p4853062327"></a><a name="p4853062327"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p385346123219"><a name="p385346123219"></a><a name="p385346123219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p285317643214"><a name="p285317643214"></a><a name="p285317643214"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.64%" headers="mcps1.1.5.1.4 "><p id="p108532611328"><a name="p108532611328"></a><a name="p108532611328"></a>Domain name. Select either <strong id="b44508169216437"><a name="b44508169216437"></a><a name="b44508169216437"></a>name</strong> or <strong id="b33726575916437"><a name="b33726575916437"></a><a name="b33726575916437"></a>id</strong>.</p>
    </td>
    </tr>
    <tr id="row185313663214"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.5.1.1 "><p id="p48531966327"><a name="p48531966327"></a><a name="p48531966327"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p108533612325"><a name="p108533612325"></a><a name="p108533612325"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p185386183218"><a name="p185386183218"></a><a name="p185386183218"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.64%" headers="mcps1.1.5.1.4 "><p id="p168532067324"><a name="p168532067324"></a><a name="p168532067324"></a>Domain ID. Select either <strong id="b17855492916445"><a name="b17855492916445"></a><a name="b17855492916445"></a>name</strong> or <strong id="b162318248016445"><a name="b162318248016445"></a><a name="b162318248016445"></a>id</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    POST /v3/auth/tokens
    {
    "auth": {
    "identity": {
    "methods": [
    "token"
    ],
    "token": {
    "id": "--federated-token-id--"
    }
    },
    "scope": {
    "domain": {
    "id": "e31ac82d778b4d128cb6fed37fd72cdb"
    }
    }
    }
    }
    ```


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You are not advised to obtain a token by directly calling this interface. You are advised to obtain a token using OpenStackClient.  

## Response<a name="section43835291165356"></a>

-   Response body parameter description

    <a name="table60997658165356"></a>
    <table><thead align="left"><tr id="row28280121165356"><th class="cellrowborder" valign="top" width="18.44%" id="mcps1.1.5.1.1"><p id="p8988451165356"><a name="p8988451165356"></a><a name="p8988451165356"></a><strong id="b842352706183221"><a name="b842352706183221"></a><a name="b842352706183221"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.12%" id="mcps1.1.5.1.2"><p id="p56975950165356"><a name="p56975950165356"></a><a name="p56975950165356"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_13"><a name="a703d34a49a2f4162bc1a1a439f655f95_13"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.1.5.1.3"><p id="p51649250165356"><a name="p51649250165356"></a><a name="p51649250165356"></a><strong id="b842352706112524_13"><a name="b842352706112524_13"></a><a name="b842352706112524_13"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.519999999999996%" id="mcps1.1.5.1.4"><p id="p22839685165356"><a name="p22839685165356"></a><a name="p22839685165356"></a><strong id="b33659860164859_3"><a name="b33659860164859_3"></a><a name="b33659860164859_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38075234165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p64195103165356"><a name="p64195103165356"></a><a name="p64195103165356"></a>methods</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p32420836165356"><a name="p32420836165356"></a><a name="p32420836165356"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p8842074165356"><a name="p8842074165356"></a><a name="p8842074165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p45119400165356"><a name="p45119400165356"></a><a name="p45119400165356"></a>Authentication method used when you obtain a token.</p>
    </td>
    </tr>
    <tr id="row3421424165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p8699959165356"><a name="p8699959165356"></a><a name="p8699959165356"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p33608041165356"><a name="p33608041165356"></a><a name="p33608041165356"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p37896816165356"><a name="p37896816165356"></a><a name="p37896816165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p49743284165356"><a name="p49743284165356"></a><a name="p49743284165356"></a>Role of a user in a project or domain who obtains a token.</p>
    </td>
    </tr>
    <tr id="row45036376165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p24067841165356"><a name="p24067841165356"></a><a name="p24067841165356"></a>expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p3338139165356"><a name="p3338139165356"></a><a name="p3338139165356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p1953870165356"><a name="p1953870165356"></a><a name="p1953870165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p24045761165356"><a name="p24045761165356"></a><a name="p24045761165356"></a>Time when a token expires.</p>
    </td>
    </tr>
    <tr id="row15085258165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p13946368165356"><a name="p13946368165356"></a><a name="p13946368165356"></a>project</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p55914060165356"><a name="p55914060165356"></a><a name="p55914060165356"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p32744979165356"><a name="p32744979165356"></a><a name="p32744979165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p35097663165356"><a name="p35097663165356"></a><a name="p35097663165356"></a>Project to which a token belongs.</p>
    </td>
    </tr>
    <tr id="row47443519165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p17719805165356"><a name="p17719805165356"></a><a name="p17719805165356"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p26018067165356"><a name="p26018067165356"></a><a name="p26018067165356"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p27088682165356"><a name="p27088682165356"></a><a name="p27088682165356"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p46699625165356"><a name="p46699625165356"></a><a name="p46699625165356"></a>Service and endpoint address information.</p>
    </td>
    </tr>
    <tr id="row17643448165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p19833159165356"><a name="p19833159165356"></a><a name="p19833159165356"></a>extras</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p62982035165356"><a name="p62982035165356"></a><a name="p62982035165356"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p1271171165356"><a name="p1271171165356"></a><a name="p1271171165356"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p35855999165356"><a name="p35855999165356"></a><a name="p35855999165356"></a>Extra token information.</p>
    </td>
    </tr>
    <tr id="row54268542165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p33675768165356"><a name="p33675768165356"></a><a name="p33675768165356"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p43382707165356"><a name="p43382707165356"></a><a name="p43382707165356"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p24338391165356"><a name="p24338391165356"></a><a name="p24338391165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p25252618165356"><a name="p25252618165356"></a><a name="p25252618165356"></a>User to which a token belongs.</p>
    </td>
    </tr>
    <tr id="row25946978165356"><td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.1.5.1.1 "><p id="p21330482165356"><a name="p21330482165356"></a><a name="p21330482165356"></a>issued_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p50047462165356"><a name="p50047462165356"></a><a name="p50047462165356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p27312615165356"><a name="p27312615165356"></a><a name="p27312615165356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p64838172165356"><a name="p64838172165356"></a><a name="p64838172165356"></a>Time when a token is generated.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    X-Subject-Token: MIIFwAYJKoZIhvcNAQcCoIIFsTCCBa0CAQExDTALBXXX... 
    {
        "token": {
            "domain": {
                "xdomain_type": "TSI",
                "id": "e31ac82d778b4d128cb6fed37fd72cdb",
                "xdomain_id": "xdomainid006958149039445714459323",
                "name": "exampledomain"
            },
            "methods": [
                "token"
            ],
            "roles": [
                {
                    "id": "eae826684d77462482d8158c0fc7b161",
                    "name": "te_admin"
                },
                {
                    "id": "007b73b229f14c3d8e71f5dccf9669a6",
                    "name": "secu_admin"
                },
                {
                    "id": "93bc5753e0fc4f01a6fd69f45a15c126",
                    "name": "te_agency"
                },
                {
                    "id": "0",
                    "name": "op_gated_stone"
                },
                {
                    "id": "0",
                    "name": "op_gated_tasssg1"
                },
                {
                    "id": "0",
                    "name": "op_gated_tasssg2"
                },
                {
                    "id": "0",
                    "name": "op_gated_tasssg4"
                },
                {
                    "id": "0",
                    "name": "op_gated_tasssg5"
                },
                {
                    "id": "0",
                    "name": "op_gated_tasssg6"
                }
            ],
            "expires_at": "2017-05-24T06:54:12.508000Z",
            "catalog": [
                {
                    "endpoints": [
                        {
                            "url": "https://sample.domain.com/v3",
                            "interface": "public",
                            "region": "*",
                            "region_id": "*",
                            "id": "f2a24165ecf14efeb5fcb2682ebc4cde"
                        }
                    ],
                    "type": "identity",
                    "id": "90ded4a66ee14ecea72266ee2fdc2b0a",
                    "name": "keystone"
                }
            ],
            "user": {
                "OS-FEDERATION": {
                    "identity_provider": {
                        "id": "stoneidp01"
                    },
                    "protocol": {
                        "id": "saml"
                    },
                    "groups": [
                        {
                            "id": "b40189e26ea44f959877621b4b298db5"
                        }
                    ]
                },
                "domain": {
                    "xdomain_type": "TSI",
                    "id": "e31ac82d778b4d128cb6fed37fd72cdb",
                    "xdomain_id": "xdomainid006958149039445714459323",
                    "name": "exampledomain"
                },
                "id": "RMQTgtjjSNGDcKy7oUmI3AZg7GgsWG0Z",
                "name": "exampleuser"
            },
            "issued_at": "2017-05-23T06:54:12.508000Z"
        }
    }
    ```


## Status Codes<a name="section48834236165356"></a>

<a name="en-us_topic_0026585112_table34550710"></a>
<table><thead align="left"><tr id="en-us_topic_0026585112_row8352109"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0026585112_p5432205"><a name="en-us_topic_0026585112_p5432205"></a><a name="en-us_topic_0026585112_p5432205"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0026585112_p37355470"><a name="en-us_topic_0026585112_p37355470"></a><a name="en-us_topic_0026585112_p37355470"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0026585112_row5894231"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p7670737"><a name="en-us_topic_0026585112_p7670737"></a><a name="en-us_topic_0026585112_p7670737"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p17349988"><a name="en-us_topic_0026585112_p17349988"></a><a name="en-us_topic_0026585112_p17349988"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0026585112_row21932166"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p31674992"><a name="en-us_topic_0026585112_p31674992"></a><a name="en-us_topic_0026585112_p31674992"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p15537542"><a name="en-us_topic_0026585112_p15537542"></a><a name="en-us_topic_0026585112_p15537542"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="r22bf632ff3984ffbaa2734a029063cfb"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p947606916650"><a name="en-us_topic_0026585112_p947606916650"></a><a name="en-us_topic_0026585112_p947606916650"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3a62e2f9d6c84b4083dfb8b2ade8e14c"><a name="a3a62e2f9d6c84b4083dfb8b2ade8e14c"></a><a name="a3a62e2f9d6c84b4083dfb8b2ade8e14c"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="r41d0d854619349f898c16f7c61792083"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p762821816657"><a name="en-us_topic_0026585112_p762821816657"></a><a name="en-us_topic_0026585112_p762821816657"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0261fc1955104ca3b1f0a46388724624"><a name="a0261fc1955104ca3b1f0a46388724624"></a><a name="a0261fc1955104ca3b1f0a46388724624"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="rea66e1a745ee4e0882be6b9f5349ac4d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p486971841676"><a name="en-us_topic_0026585112_p486971841676"></a><a name="en-us_topic_0026585112_p486971841676"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0026585112_p521578261676"><a name="en-us_topic_0026585112_p521578261676"></a><a name="en-us_topic_0026585112_p521578261676"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="r230ba1b5ddec4cd0a41a5c37806e60f5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af8f4513c90d344e3b90952b53e3ee015"><a name="af8f4513c90d344e3b90952b53e3ee015"></a><a name="af8f4513c90d344e3b90952b53e3ee015"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a19c27fd6b377464898ec6cae5778ec80"><a name="a19c27fd6b377464898ec6cae5778ec80"></a><a name="a19c27fd6b377464898ec6cae5778ec80"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="en-us_topic_0026585112_row6824316711"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0026585112_p61418816711"><a name="en-us_topic_0026585112_p61418816711"></a><a name="en-us_topic_0026585112_p61418816711"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a4bc003bda05e465eb3a3f0f989888213"><a name="a4bc003bda05e465eb3a3f0f989888213"></a><a name="a4bc003bda05e465eb3a3f0f989888213"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

