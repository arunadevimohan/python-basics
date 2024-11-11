import json

FILEPATH='city_score.json'

def write_2_json(score):

    score_str = json.dumps(score)

    fileobj_write = open(FILEPATH, 'w')
    fileobj_write.write(score_str)
    fileobj_write.close()



def create_new_record():
    fileobj_write = open(FILEPATH,'r')
    score= json.load(fileobj_write)
    mississauga_score= 75
    score['mississauga'] = mississauga_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()
    write_2_json(score)
    

    
    

    print('[CREATE] mississauga score added in the file')
create_new_record()

def create_new_record():
    fileobj_write = open(FILEPATH,'r')
    score= json.load(fileobj_write)
    ottawa_score= 88
    score['ottawa'] = ottawa_score
    score_str= json.dumps(score)
    fileobj_write= open(FILEPATH,'w')
    fileobj_write.write(score_str)
    fileobj_write.close()
    write_2_json(score)

    
    

    print('[CREATE] ottawa score added in the file')
create_new_record()



def read_record():
    

    fileobj_read = open(FILEPATH, 'r')
    score_obj = json.load(fileobj_read)
    print(score_obj)

    
read_record()



    



   


    