import json

FILEPATH='animal_score.json'
def read_record():
    

    fileobj_read = open(FILEPATH, 'r')
    score_obj = json.load(fileobj_read)
    print(score_obj)

    
read_record()

