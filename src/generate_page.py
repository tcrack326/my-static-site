from mdtohtmlnode import markdown_to_html_node
from extracttitle import extract_title
from copytopublic import copy_static_to_public
import os

def create_directories(path):
    directories = path.split('/')
    start = ''
    print(f"the directories: {directories}")
    for directory in directories:
        print(f"checking directory {directory}")
        path = f"{start}/{directory}"
        print(f"the path {path}")
        if os.path.exists(directory) == False:
            print("directory does not exist creating in the correct place")



def generate_page(from_path, template_path, dest_path):
    print(f" Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_md_file = None 
    with open(from_path) as f:
        from_md_file = f.read()
    template_file = None
    with open(template_path) as f:
        template_file = f.read()
    #print(f"the from_md_file content {from_md_file}")
    html_string = markdown_to_html_node(from_md_file).to_html()
    #print(f"the html string: {html_string}")
    title = extract_title(from_md_file)
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html_string)
    #print(f"DEBUG: WHAT IS TEMPLATE FILE: {template_file}")
    print(f"DEBUG: THE DEST_PATH: {dest_path}")
    with open(dest_path, "w+") as f:
        f.write(template_file)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        full_path = f"{dir_path_content}/{content}"
        if os.path.isfile(full_path):
            print(f"DEBUG: content is file, calling generate_Page with {full_path}")
            dest_path = f"{dest_dir_path}/{content.replace('md', 'html')}"
            generate_page(full_path, template_path, dest_path)
        else:
            new_path = f"{dest_dir_path}/{content}"
            print(f"DEBUG: content is directory, calling recursive with {full_path}")
            print(f"DEBUG: THE DEST PATH: {new_path}")
            os.makedirs(new_path, exist_ok=True)
            generate_pages_recursive(full_path, template_path, new_path)
            