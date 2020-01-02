from os import listdir

def get_pet_labels(image_dir):

    in_files = listdir(image_dir)
    # print(in_files)
    results_dic = {}

    for file in in_files:
        image_name = file.split("_")

        pet_label = ""

        for word in image_name:
            if word.isalpha():
                pet_label += word.lower() + " "

        pet_label.strip()
        if file not in results_dic:
            results_dic[file] = pet_label
        else:
            print("** Warning: Key=", file,
                  "already exists in results_dic with value =",
                  results_dic[file])
                
    print(results_dic)
get_pet_labels("pet_images")        