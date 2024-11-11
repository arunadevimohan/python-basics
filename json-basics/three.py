import json

FILEPATH='animal_score.json'





def read_tiger_json():

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
    zebra_score= 87
    score['zebra'] = zebra_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()
    write_2_json(score)

    
    

    print('[CREATE] zebra score added in the file')










def update_record():

    score = read_tiger_json()

    score['tiger'] = 94
    write_2_json(score)

    
    print('[UPDATE] tiger score updated in the file')

    



def delete_record():

    score = read_tiger_json()
    score.pop('giraffe')
    write_2_json(score)

    

    print('[DELETE] giraffe score deleted from the file')


def startpy():
    update_record()
    delete_record()
    read_record()
    create_new_record()
    print("Tact101")
    

if __name__ == '__main__':
    startpy()






   



