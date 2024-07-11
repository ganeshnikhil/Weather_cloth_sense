
def write_to_file(data , path):
   with open(path , 'w') as file:
      file.write(data)
      print(f"{path} saved at backup..")
