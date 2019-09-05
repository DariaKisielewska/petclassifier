
import shutil
import os


def create_output_folder(PATH):
    '''
    Create directory where output parameters and plots will be stored.
    Move earlier results to folder named 'backup' 
    '''


    if os.path.isdir(PATH):
        if os.path.isdir('saved_models/backup'):
            shutil.rmtree('saved_models/backup')
        os.rename(PATH,'saved_models/backup')
        print('Folder '+PATH+' exists ! Moved to saved_models/backup')
    
    # create
    try:
        os.mkdir(PATH)
    except OSError:
        print("Creation of the directory %s failed" % PATH)
    else:
        print("Successfully created the directory %s " % PATH)
