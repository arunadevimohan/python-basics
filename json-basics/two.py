import json

FILEPATH='product_score.json'

def read_tablet_json():

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
    smartwatch_score= 89
    score['smartwatch'] = smartwatch_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()

    
    write_2_json(score)

    print('[CREATE] smartwatch score added in the file')

def create_new_record():
    fileobj_write = open(FILEPATH,'r')
    score= json.load(fileobj_write)
    mobile_score= 70
    score['mobile'] = mobile_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()

    
    write_2_json(score)
    print('[CREATE] mobile score added in the file')


def read_record():
    

    fileobj_read = open(FILEPATH, 'r')
    score_obj = json.load(fileobj_read)
    smartphone_score= score_obj['smartphone']
    print(f'[READ] smartphone_score: {smartphone_score}')





def update_record():

    score = read_tablet_json()

    score['laptop'] = 100
    write_2_json(score)

    
    print('[UPDATE] laptop score updated in the file')

    



def delete_record():

    score = read_tablet_json()
    score.pop('tablet')
    write_2_json(score)

    

    print('[DELETE] tablet score deleted from the file')




def startpy():
    #update_record()
    #delete_record()
    read_record()
    #create_new_record()
    

    

if __name__ == '__main__':
    startpy()


   



