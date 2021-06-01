import os
import dropbox
from dropbox.files import WriteMode

class UploadFolder:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFolders(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                print(local_path)
                relative_path = os.path.relpath(local_path, file_from)
                print(relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print(dropbox_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))


def main():
    print("Go to https://www.dropbox.com/developers/apps and create app\n")
    access_token = input("Enter your access token:- ")
    uploadFolder = UploadFolder(access_token)

    file_from = input("\n\nEnter the location of FOLDER:- ")
    # print("Go to C drive > Users > select ur username > Dropbox > create new folder here.")
    file_to = input("\n\nEnter the dropbox folder path:- ")

    uploadFolder.uploadFolders(file_from, file_to)
    print("Folder uploaded successfully !")

main()   