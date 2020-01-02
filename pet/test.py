from os import listdir
def get_pet_labels(image_dir):
    filename_list = listdir(image_dir)
    # for name in filename_list:
    #     if name[0].isdigit():
    #         print(name)
    # print(len(filename_list))

    for idx in range(0, len(filename_list)):
        image_name= filename_list[idx].lower().replace('_', ' ' )
        pet_label = ""
        results_dic = dict()
        print(image_name)
        for word in image_name:
            if word.isalpha():
                pet_label += word
        #print(pet_label)
    # for pet in filename_list:
    #     print(pet.lower().split("_").)

    # for idx in range(0, 10, 1):
    #     print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )


get_pet_labels("pet_images")    