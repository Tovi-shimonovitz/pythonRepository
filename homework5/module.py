import os

def create(src):
  os.mkdir(src)


def delete(src):
   if not os.listdir(src):
      os.rmdir(src)
   else:
       print("the folder is no empty")


def create_file(src,name):
    file_name = name
    file_src= os.path.join(src, file_name)
    with open(file_src,"w") as new_file:
        new_file.write("hello to my file")



def write(src):
    with open(src, "a") as file:
        file.write("hello world.")



def remove_file(src):
    os.remove(src)


def list_file(src):
    return os.listdir(src)


def full_src():
 
  return os.getcwd()



def example():
return null;