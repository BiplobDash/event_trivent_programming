import glob
import shutil
import os 
import zipfile
import runpy



source='../source/*'
destination='../destination'
prefix_path=[1,2,3]

while True:
    source_path=glob.glob(source)
    if len(source_path)>0:
        for file_itme in range(0,len(source_path)):
            object_path=source_path[file_itme].split('/')[1].split('\\')[1].split('.')
            # print(object_path)
            if object_path[1]=='txt':
                list_file_name=[]
                for item in prefix_path:
                    file_name=object_path[0]+'_'+str(item)+'.'+object_path[1]
                    list_file_name.append(file_name)
                    
                    with open(f'../source/{object_path[0]}.{object_path[1]}','r') as file:
                        lines=file.readlines()
                    if item==1:
                        with open (f'../source/{file_name}','w') as write_file:
                            write_file.writelines(lines[0:10])
                        write_file.close()

                    elif item==2:
                            with open (f'../source/{file_name}','w') as write_file:
                                write_file.writelines(lines[0:20])
                            write_file.close()
                    else:
                            with open (f'../source/{file_name}','w') as write_file:
                                write_file.writelines(lines[0:30])
                            write_file.close()

                path_zip_file='Back_up.zip'
                handle=zipfile.ZipFile(path_zip_file,'w')
                for target in list_file_name:
                    t=f'../source/{target}'
                    handle.write(t,compress_type=zipfile.ZIP_DEFLATED)
                    os.remove(t)
                handle.close()

                # destination path file copy 
                shutil.copy(path_zip_file,destination)
                os.remove(path_zip_file)
                os.remove(f'../source/{object_path[0]}.{object_path[1]}')

                # start destination work 
                destination_zip_file='../destination/Back_up.zip'
                # souorce_zip_file='../source/Back_up.zip'

                with zipfile.ZipFile(destination_zip_file,'r') as readfile:
                    readfile.extractall('../destination')
                readfile.close()
                os.remove(destination_zip_file)
            
            elif object_path[1]=='py':
                try:
                    runpy.run_path(f'../source/{object_path[0]}.{object_path[1]}')
                    os.remove(f'../source/{object_path[0]}.{object_path[1]}')
                except Exception as e:
                    print(e)
                    os.remove(f'../source/{object_path[0]}.{object_path[1]}')
                

