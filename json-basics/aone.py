import json

FILEPATH='city_score.json'


def read_hyd_json():

    fileobj_read = open(FILEPATH, 'r')
    score_obj = json.load(fileobj_read)
    return score_obj

def write_2_json(score):

    score_str = json.dumps(score)

    fileobj_write = open(FILEPATH, 'w')
    fileobj_write.write(score_str)
    fileobj_write.close()

def create_new_record():
    fileobj_write = open(FILEPATH,'r')
    score= json.load(fileobj_write)
    scaborough_score= 90
    score['scaborough'] = scaborough_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()

    
    write_2_json(score)

    print('[CREATE] scaborough score added in the file')


def create_new_record():
    fileobj_write = open(FILEPATH,'r')
    score= json.load(fileobj_write)
    sivagangai_score= 82
    score['sivagangai'] = sivagangai_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()

    
    write_2_json(score)
    print('[CREATE] sivagangai score added in the file')




def read_record():
    

    fileobj_read = open(FILEPATH, 'r')
    score_obj = json.load(fileobj_read)
    chennai_score= score_obj['chennai']
    

    print(f'[READ] chennai_score: {chennai_score}')





def update_record():

    score =read_hyd_json()

    score['hyd'] = 90
    write_2_json(score)

    
    print('[UPDATE] hyd score updated in the file')

    



def delete_record():

    score = read_hyd_json()
    score.pop('hyd')
    write_2_json(score)

    

    print('[DELETE] hyd score deleted from the file')


def startpy():
    create_new_record()
    #read_record()
    #update_record()
    #delete_record()
print("Tact101")
    

if __name__ == '__main__':
    startpy()





   


    