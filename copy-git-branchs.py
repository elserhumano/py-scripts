from os import listdir, chdir, getcwd, popen, makedirs, system
from os.path import isfile, isdir, join

dir_dest = '\\_test'

# Get the list of the directories/repos
mypath = '.'
repolist = [f for f in listdir(mypath) if isdir(join(mypath, f))]


original_dir = getcwd()
# Get the branchs of the repos for each
for repo in repolist:
    chdir(repo)
    the_command = "git branch -r"
    branch_list = [f.replace('\n', '').replace(' ', '').replace('origin/', '') for f in popen(the_command).readlines() if not ('HEAD' in f)]

    print('This is the repo: ', repo,)
    print('This is the list of the branches: ', branch_list, '\n')

    #makedirs(dir_dest + '/' + repo)

    for branch in branch_list:

        #makedirs(dir_dest + '/' + repo + '/' + branch)

        destination = dir_dest + '\\' + repo + '\\' + branch + '\\'
        options = '/E /S /Y /Q'
        system('git checkout ' + branch)
        system('xcopy . '+ destination + options)

    chdir(original_dir)
