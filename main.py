import os
import shutil

dir_path = r'C:\Users\hong0\PycharmProjects\image-scrapping\images'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def divide_set(file_names):
    file_names_len = len(file_names)

    for i in range(file_names_len):
        origin_file_name = file_names[i]
        file_name = file_names[i].split('_')[0]
        file_num = file_names[i].split('_')[1]
        print(file_name, file_num)

        if file_name == '고무줄':
            file_name = 'band'
        elif file_name == '리모컨':
            file_name = 'remoteControl'
        elif file_name == '멀티탭':
            file_name = 'multiOutlet'
        elif file_name == '반려동물':
            file_name = 'pet'
        elif file_name == '배변패드':
            file_name = 'pooPad'
        elif file_name == '빨래감':
            file_name = 'laundry'
        elif file_name == '빨래건조대':
            file_name = 'laundryBar'
        elif file_name == '실내슬리퍼':
            file_name = 'slipper'
        elif file_name == '의자다리':
            file_name = 'chairLegs'
        elif file_name == '장난감':
            file_name = 'toy'
        elif file_name == '전선':
            file_name = 'electricWire'
        elif file_name == '조명받침대':
            file_name = 'stand'
        elif file_name == '초코파이똥':
            file_name = 'poo'
        elif file_name == '커튼아랫단':
            file_name = 'curtain'
        elif file_name == '필기구':
            file_name = 'stationary'
        elif file_name == '핸드폰':
            file_name = 'smartPhone'

        jpg_name = file_name + '_' + file_num + '.jpg'
        xml_name = file_name + '_' + file_num + '.xml'
        origin_jpg_name = origin_file_name + '.jpg'
        origin_xml_name = origin_file_name + '.xml'
        shutil.copyfile(dir_path + '/' + origin_jpg_name, './to_english/' + jpg_name)
        shutil.copyfile(dir_path + '/' + origin_xml_name, './to_english/' + xml_name)


def main():
    os_files = os.listdir(dir_path)
    file_names = []

    for dir in os_files:
        if dir[:-4] not in file_names:
            file_names.append(dir[:-4])

    createFolder('./to_english')

    divide_set(file_names)

    print('done.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()