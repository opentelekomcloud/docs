# Policy Language<a name="iam_01_0017"></a>

This section describes the policy language specifications, including the policy structure, policy elements, example policies, and policy evaluation logic.

## Policy Structure<a name="section106463610252"></a>

A fine-grained authorization policy includes the policy version \(the **Version** field\) and statements \(the **Statement** field\).

-   The value of the **Version** field for custom policies is fixed at **1.1**.
-   The **Statement** field contains the **Effect** and **Action** elements. **Effect** indicates whether the policy allows or denies access. **Action** indicates authorization items.

![](figures/en-us_image_0126272126.jpg)

## Policy Elements<a name="section24920662173152"></a>

The **Statement** field provides detailed information about a policy and contains the **Effect** and **Action** elements.

-   Effect

    The value can be **Allow** and **Deny**. If both **Allow** and **Deny** are found in statements, the policy evaluation starts with Deny.

-   Action

    The value can be one or more resource authorization items.

    The value format is *Service name*:*Resource type*:*Action*, for example, **vpc:ports:create**.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > -   *Service name*: indicates the product name, such as **ecs**, **evs**, or **vpc**. Only lowercase letters are allowed.
    > -   *Resource type* and *Action*: The values are case-insensitive, and the wildcard \(\*\) are allowed. A wildcard \(\*\) can represent all or part of information about resource types and actions for the specific service.
    > -   Policies support only API-level authorization. You need to fill the **Action** field with the permissions in the API permissions table of the specific service. IAM then implements fine-grained authorization by calling the corresponding APIs in the table.

        For details about the API permissions of each service, see:


## Example Policies<a name="section44276331103751"></a>

-   A policy can define a single permission, such as the permission to query ECS details.

    ```
    {
        "Version": "1.1",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ecs:servers:list",
                    "ecs:servers:get",
                    "ecs:serverVolumes:use",
                    "ecs:diskConfigs:use",
                    "ecs:securityGroups:use",
                    "ecs:serverKeypairs:get",
                    "ecs:serverKeypairs:use",
                    "vpc:securityGroups:list",
                    "vpc:securityGroups:get"'
                    "vpc:securityGroupRules:get"'
                    "vpc:networks:get"'
                    "vpc:subnets:get"'
                    "vpc:ports:get"'
                    "vpc:routers:get"'
                ]
            }
        ]
    }
    ```

-   A policy can define multiple permissions, such as the permissions to lock ECSs and create EVS disks.

    ```
    {
        "Version": "1.1",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ecs:servers:lock",
                    "evs:volumes:create"
                ]
            }
        ]
    }
    ```

-   The following example shows how to use the wildcard \(\*\) in a policy, which defines the **Tenant Guest** permission for ECS resources.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > To grant the **Tenant Guest** permission for ECS, you must also grant this permission for EVS, VPC, and IMS.

    ```
    > {
    >     "Version": "1.1",
    >     "Statement": [
    >         {
    >             "Effect": "Allow",
    >             "Action": [
    >                 "ecs:*:get",
    >                 "ecs:*:list",
    >                 "ecs:serverGroups:manage",
    >                 "evs:*:get",
    >                 "evs:*:list",
    >                 "vpc:*:get",
    >                 "vpc:*:list",
    >                 "ims:*:get",
    >                 "ims:*:list"
    >             ]
    >         }
    >     ]
    > }
    ```


## Policy Syntax<a name="section1479310270352"></a>

A policy can be verified only when its syntax is correct. The following policy is used as an example:

```
Policy = {
<version_block>,
<statement_block>
}

<version_block> = "Version" : "1.1"

<statement_block> = "Statement": [<statement>,<statement>, ...]

<statement> = {
<effect_block>,
<action_block>
}

<effect_block> = "Effect" : ("Allow" | "Deny")

<action_block> = "Action": ("*" | [<action_string>, <action_string>,...])
```

-   If an element allows multiple values, it is indicated using repeated values, a comma delimiter, and an ellipsis \(...\). Example: **\[<statement\>,<statement\>, ...\]** or **\[<action\_string\>, <action\_string\>,...\]**
-   A vertical bar \(|\) between elements indicates alternatives. Example: **\("Allow" | "Deny"\)**
-   If the value of an element is a number, the value must be enclosed in double quotation marks \("\). Example: **<version\_block\> = "Version" : "1.1"**
-   If the value of an element is a string, the wildcard \(\*\) can be used to represent zero or more letters for fuzzy match.

For more information about the syntax of the JSON policy language, visit:

[https://tools.ietf.org/html/rfc7159?spm=a2c4g.11186623.2.12.M8YmXV](https://tools.ietf.org/html/rfc7159?spm=a2c4g.11186623.2.12.M8YmXV)

## Policy Evaluation Logic<a name="section565017773111"></a>

A policy may consist of multiple statements. If both **Allow** and **Deny** are found in statements, the policy evaluation starts with Deny.

When users make a request for accessing resources, the policy evaluation starts. The following figure shows the policy evaluation logic.

**Figure 1** Policy evaluation logic<a name="fig11089053175940"></a>
![](figures/policy-evaluation-logic.png "Policy evaluation logic")

> ![](public_sys-resources/icon-note.gif) **NOTE:** 

> Multiple actions in each policy bear the OR relationship.

1.  When a user makes a request, the evaluation starts.
2.  IAM evaluates all policies that are applicable to the request. In all those policies, IAM looks for an explicit deny instruction. If IAM finds even one explicit deny that applies, it returns a decision of Deny and the evaluation ends.
3.  If no explicit deny is found, IAM looks for any Allow instructions that would apply to the request.
    -   If it finds even one explicit allow, it returns a decision of Allow and the service continues to process the request.
    -   If no explicit allow is found, the final decision is Deny.
4.  If the code encounters an error at any point during the evaluation, it will generate an exception and close.

