# Why Cannot I Use a Key File to Log In to an ECS?<a name="EN-US_TOPIC_0042018407"></a>

## Issue Description<a name="section19793926"></a>

When I used a key file to attempt to log in to an instance in an AS group, the login failed.

## Possible Causes<a name="section43927610"></a>

The image in the AS configuration of the AS group is your private one, and the Cloud-Init tool had not been installed when you created the private image.

If the Cloud-Init tool had not been installed when you created a private image, you would fail to customize the ECS configuration. In such a case, you can log in to the ECS only using the original image password or key pair.

## Handling Method<a name="section59804173"></a>

1.  Check whether the ECS must be logged in to.
    -   If yes, use the original image password or key pair to log in to this ECS.

        The original image password or key pair is the OS password or key pair configured when the private image was created.

    -   If no, go to step  [2](#li4126846117151).

2.  <a name="li4126846117151"></a>Modify the AS configuration of the AS group. For details, see  [Replacing AS Configuration in an AS Group](replacing-as-configuration-in-an-as-group.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Make sure that the Cloud-Init or Cloudbase-Init tool has been installed in the image of the modified AS configuration. For instructions about how to install the Cloud-Init or Cloudbase-Init tool, see  _Image Management Service User Guide_.  

After the AS configuration is modified, you can use the key file to log in to the new ECSs that are added when the AS action is performed in the AS group. In such a case, you do not need to use the original image password or key pair to log in to the new ECSs any more.

