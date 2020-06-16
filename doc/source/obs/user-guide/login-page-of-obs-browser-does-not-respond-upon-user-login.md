# Login Page of OBS Browser Does Not Respond upon User Login<a name="obs_03_0440"></a>

## Question<a name="s66d8cfd6480c42f7b4ec7ece2c9336ab"></a>

When a user attempts to log in to OBS Browser, the login page does not respond.

## Answer<a name="s6d21c5d0d89f47149100d6f837e85244"></a>

Delete the  **obs**  folder in the  **AppData\\Local**  directory on the C drive to clear OBS Browser related data. Then log in to OBS Browser again and reconfigure required information. If you want to retain the account information, save the  **accounts**,  **setting**, and  **temp files**  in the  **obs**  folder before deleting the folder. Start OBS Browser again and overwrite the three files in the  **obs**  folder.

