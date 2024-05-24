#בדקתי על המילה deep לא נתן לי כלום אחר כך רציתי לבדאה שכן עובד אז בדקתי על המילה vendors

import os
def find_deep(path):
    all_files = os.listdir(path)
    r=[file for file in all_files if file.startswith('vendors')]
    return r

if __name__ == '__main__':
    path = '/Users/louyhaib/PycharmProjects/thats_the_way.py/images_files'
    deep_count = find_deep(path)
    print(deep_count)


