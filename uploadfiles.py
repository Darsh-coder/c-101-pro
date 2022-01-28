import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    # craete the init method done
    def __init__(self, access_token):
        self.access_token = access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                print(relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print(dropbox_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    # put access_token 
    access_token = 'sl.BA9-C6ZUW7ygoE3PDnOiQGgNPfRTO8gILEHS2uXDyb58_zwK3OzjkFO6ZJXYd9v_IpChiI0fiy6NFUlBXZxHavxXKUCCyQQD0hezUEmTdQse6XBT6L_pV5aiiQHqQ75puChFDq4'
    transferData = TransferData(access_token)

    # craete object of transferData
    file_from = input("enter the file to upload on dropbox")
    file_to = input("enter the path in the dropbox") 
    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()