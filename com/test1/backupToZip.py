import zipfile, os


def backupToZip(folder):
    folder = os.path.abspath(folder)
    print(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # for foldername, subfolders, filenames in os.walk(folder):
    #     print('Adding files in %s...' % foldername)
    #     backupZip.write(foldername)
    # for filename in filenames:
    #     newBase = os.path.basename(folder) + '_'
    #     if filename.startswith(newBase) and filename.endswith('.zip'):
    #         continue
    #     backupZip.write(os.path.join(foldername, filename))
    # backupZip.close()

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))



        for subfolder in subfolders:
            print('SUBFOLDER OF '+foldername+": " + subfolder)
        for fileName in filenames:
            print('FILE INSIDE ' + foldername + ": " + fileName)


    backupZip.close()
    print('Done.')


if __name__ == '__main__':
    backupToZip('/Users/hanyouquan/PycharmProjects/test/com/test1')
