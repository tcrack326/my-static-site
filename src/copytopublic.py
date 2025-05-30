import shutil,os

def copy_static_to_public(dir=None):
    if dir == None:
        # remove contents of public
        shutil.rmtree('public')
        os.mkdir('public')
    directory = dir if dir != None else 'static'
    # list static content
    contents = os.listdir(directory)
    #print(contents)
    for content in contents:
        original_path = f"{directory}/{content}"
        new_path = f"{directory.replace('static', 'public')}/{content}"
        if os.path.isfile(original_path):
            #print(f"{content} is file and will be moved")
            shutil.copy(original_path, new_path)
        else:
            # create the new directory in public
            os.mkdir(new_path)
            #print(f"Creating {content} directory in public")
            # send directory to copy contents
            copy_static_to_public(original_path)