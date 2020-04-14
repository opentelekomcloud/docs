# What Can I Do to Enable My Application to Be Automatically Deployed on an Instance?<a name="EN-US_TOPIC_0042018405"></a>

To enable automatic application deployment on instances automatically added to an AS group, you need to create a private image which contains application software and automatic startup settings. When creating an AS group, select the private image you have created for the AS configuration. In this way, applications will be automatically deployed on instances that are added to the AS group. The procedure is as follows:

1.  Before creating a private image, install the application and set it to automatically start upon system startup on the ECS which you will use to create the private image.
2.  Create a private image. For details, see  ___Image Management Service User Guide_.
3.  <a name="li6411253193514"></a>Create an AS configuration. For details, see  __[Using a New Specifications Template to Create an AS Configuration](using-a-new-specifications-template-to-create-an-as-configuration.md). Ensure that the image in the AS configuration is the created private image.
4.  Click the  **AS Groups**  tab and then click the name of the target AS group.
5.  Click  **Change Configuration**  on the right of  **Configuration Name**. In the displayed dialog box, select the AS configuration created in  [3](#li6411253193514)  and click  **OK**.

    After new instances are added to the AS group in the next scaling action, you can check whether the required application has been installed on the instances. If any issue occurs, contact technical support.


