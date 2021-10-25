import os
import sys # Or import os.sys


class Explainer:
    def show_me_what_you_got(self) -> dict:
        '''Returns all the object attributes'''
        return {k: v for k, v in self.__dict__.items() if k[:1] != '_'}


class OSExplained(Explainer):
    '''
    OS module
    ---------
    This module allows the developer to interact with the
    underlying operating system.
    '''

    def __init__(self) -> None:
        self.cwd = os.getcwd()          # Get the current directory
        self.ls  = os.listdir(self.cwd) # Get the list of all the files and folders
        self.env = os.environ           # Get the environment

    def change_dir(self, new_path:str) -> str:
        ''' Changes the CWD
        
        Changes the current working directory.

        ARGS:
            new_path: str, the new CWD

        RETURNS:
            path_string: str, the new CWD
        '''
        if not os.path.isabs(new_path):
            new_path = os.path.join(self.cwd, new_path)
        
        if os.path.exists(new_path):
            os.chdir(new_path)
            self.cwd = os.getcwd()
        else:
            raise TypeError('You must specify an existing path')

        return self.cwd

    def create_folder(self, folder_path:str) -> str:
        '''Creates a folder at the specified path
        
        Creates a folder at the specified path and creates
        any missing folder in between.

        ARGS:
            folder_path: str, the name or the path of the new folder
        
        RETURNS:
            path_string: str, the path of the new folder
        '''
        folder_path = os.path.normpath(folder_path)
        if not os.path.isabs(folder_path):
            folder_path = os.path.join(self.cwd, folder_path)

        os.makedirs(folder_path)
        self.ls = os.listdir(self.cwd)
        return folder_path
        
    def death_ray(self, target_path:str)->None:
        '''The death ray
        
        Delete either a file or a folder,
        since this is the death ray it returns nothing

        ARGS:
            target_path: str, the path to the thing you want to kill

        RETURNS
            none: None, just dust if you're lucky
        '''
        target_path = os.path.normpath(target_path)
        if not os.path.isabs(target_path):
            target_path = os.path.join(self.cwd, target_path)

        if os.path.exists(target_path):
            if os.path.isfile(target_path):
                os.remove(target_path)
            elif os.path.isdir(target_path):
                os.rmdir(target_path)
        else:
            raise TypeError('You must specify an existing path')


class SysExplained(Explainer):
    '''
    Sys module
    ---------
    This module allows the developer to interact with the underlying system
    (actually the python execution environment, the interpreter).
    '''
    
    def __init__(self) -> None:
        self.version    = sys.version              # Get the version
        self.executable = sys.executable           # Get python interpreter path
        self.bmn        = sys.builtin_module_names # Get the builtin module names
        self.platform   = sys.platform             # Get the platform name
        self.argv       = sys.argv                 # If you used args while
                                                   #   calling this script,
                                                   #   you'll get them here

    def stop_this_script(self) -> None:
        '''Stops the script. Yes, Python supports seppoku'''
        sys.exit(0)

    def tell_me_what_happened(self) -> tuple:
        '''Returns what went in, what went out and what went wrong'''
        return sys.stdin, sys.stdout, sys.stderr


def main():
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    
    print('---\n')
    print('OS explained:')
    
    pp.pprint(OSExplained().show_me_what_you_got())

    print('\n')
    print('Sys explained:')
    pp.pprint(SysExplained().show_me_what_you_got())

    print('\n---')

if __name__ == '__main__':
    main()