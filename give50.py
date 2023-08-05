# submit50 alternative (Python script) - 'give50'
# credits :
# 1)user:Ian Wetherbee on stackoverflow.com (ref:https://stackoverflow.com/questions/11113896/use-git-commands-within-python-code)
# 2)user:tripleee on stackoverflow.com (ref:https://stackoverflow.com/questions/4256107/running-bash-commands-in-python)

import subprocess
import sys

def git_push():
    '''calls 'git push' '''
    subprocess.call(['git','push'])

def git_commit(descprition):
    '''commits changes to repo with description "description"'''
    subprocess.call(['git','commit','-m',description])

def git_add():
    '''adds all changes to index'''
    subprocess.call(['git','add','*'])

def git_clone(username):
    '''clones the repo me50/<username> to current working directory'''
    ## alert - this uses the SSH format of repo access
    subprocess.call(['git','clone','git@github.com:me50/' +  username])

def move_files(destination_folder, source_floder):
    '''move all the files in source folder to destination folder'''
    subprocess.call(['mv', source_folder + "/*", destination_folder])

def mainloop():
    if len(sys.argv) != 4:
        sys.exit("ERROR: Requires three arguments; given less than three.")
        return None
    source = sys.argv[1]
    dest = sys.argv[2]
    username = sys.argv[3]
    print("Cloning repo....", end = ' ')
    git_clone(username) # clones the repo
    print("Done!")
    print("Ensure that the given input paths are part of the CWD...")
    print("Moving files....", end = ' ')
    move_files(dest, source)
    print("Done!")
    git_add()
    print("Added changes to index")
    git_commit(input("Enter a commit message:"))
    print("Committed changes")
    git_push()
    print("Pushed to repo.")

if __name__ == '__main__':
    mainloop()
    
    
    
    
