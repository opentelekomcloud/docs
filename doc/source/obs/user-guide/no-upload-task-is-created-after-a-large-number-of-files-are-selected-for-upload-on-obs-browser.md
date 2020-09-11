# No Upload Task Is Created After a Large Number of Files Are Selected for Upload On OBS Browser<a name="obs_03_0441"></a>

## Question<a name="s94ab5c5019a54292a66843d1c1ef7341"></a>

Why is no upload task created and nothing displayed on the page after a large number of files are selected for upload using OBS Browser? For example, after a user logs in to OBS Browser and chooses  **Upload**  \>  **Upload File**  to select a large number of files from drive C for upload, no upload task is created and nothing is displayed on the page.

## Answer<a name="s66d08bb155f34325a807eda4c8d6cd76"></a>

Confirm the number of files to be uploaded. The  **Upload File**  function of OBS Browser allows 500 files to be uploaded at the same time. If more files need to be uploaded, place the files in a folder and use the  **Upload Folder**  function to upload the folder.

Confirm the total name length of all files to be uploaded cannot exceed approximately 25,500 characters. If the name length exceeds this threshold, the system stops responding to the upload request.

