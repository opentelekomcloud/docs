# Operation Guide<a name="EN-US_TOPIC_0162985073"></a>

RTS helps you create and configure a collection of resources using a template and makes it easy to manage these resources.

## Compile a Template<a name="section16426617282"></a>

To create and manage a resource stack, you need to compile a template, and then RTS creates and configures a collection of resources based on the template.

During template compilation, you need to define and describe the required resources. For cloud resource types supported, you can log in to the RTS console and click  **Resource Types**  in the left pane to view cloud resource types that are supported. For more details, see  [Supported Resources](supported-resources.md).

For template syntax, see the following references:

-   [Template Structure](template-structure.md)
-   [Template Version](template-version.md)
-   [Template Description](template-description.md)
-   [Parameters](parameters.md)
-   [Resources](resources.md)
-   [Outputs](outputs.md)
-   [Conditions](conditions.md)
-   [Internal Function](internal-function.md)

We provide common templates in  [Example Templates](example_templates)  for your reference. These templates contain ECSs. If these templates meet your business scenarios, you can directly use them or modify some parameters.

## Creating a Stack Using a Template<a name="section11997101920283"></a>

If you have created a template, log in to the RTS console, click  **Create Stack**, upload a template file or manually enter template content, and perform subsequent operations as needed. Then, the system orchestrates cloud resources defined in the template and dependencies between them.

>![](/images/icon-note.gif) **NOTE:**   
>Before uploading a template, you need to package the template according to the required rules.  

The references are as follows:

-   [Preparing a Template or a Template Package](preparing_a_template_or_a_template_package)
-   [Creating a stack](creating-a-stack.md)

## Managing Stacks Using the Console<a name="section1841564262917"></a>

Except for creating stacks, you can also view all resources in your stack or update, re-create, or delete your stack based on your service requirements on the RTS console.

The references are as follows:

-   [Viewing Details of a Stack](viewing-details-of-a-stack.md)
-   [Updating a Stack](updating-a-stack.md)
-   [Deleting a Stack](deleting-a-stack.md)

