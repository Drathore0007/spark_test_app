import os 
import shutil
import sys

def createsbt( project, path='./',):
    
    if os.path.exists(path+project):
        shutil.rmtree(path+project)
        
    os.mkdir(path+project)
    os.mkdir(path+project+'/'+"project")
    os.mknod(path+project+'/'+"project"+'/build.properties')
    os.mkdir(path+project+'/'+"src")
    os.mknod(path+project+'/'+"build.sbt")

    path = path+project+'/src/'
    os.mkdir(path+'main')
    os.mkdir(path+'test')
    main = ['scala', 'resource', 'java']
    test = ['scala', 'resource', 'java']
    for folder in main:
        os.mkdir(os.path.join(path+'main', folder))

    for folder in test:
        os.mkdir(os.path.join(path+'test', folder))


if len(sys.argv) == 3:
    dir_path = sys.argv[1]
    project_name = sys.argv[2]
    createsbt(project_name, path= dir_path)
else:
    project_name = sys.argv[1]
    createsbt(project_name)

