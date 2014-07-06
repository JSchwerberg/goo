def get_next_folders(path, folder_list):
	
    # This is the amount of characters to strip from the beginning of each folder
    strip = len(path)+ 1
    
    return_list = []

    for folder in folder_list:
        end_of_path = folder[strip:]
        split_folder = end_of_path.split('/')
        subfolder = split_folder[0]
        if subfolder not in return_list:
            return_list.append(subfolder)
    return sorted(return_list)
