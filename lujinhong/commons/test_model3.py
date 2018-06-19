import os
import time
import random

def rsync_trainning_model_redis_game_model3(dateid=None,isCommon=True):
        dateid = '20180531'
        
        tempLocalDir = '/Users/ljhn1829/Desktop/model_format'

        model_id = '3'
        game_id = '1475'
        destFile = tempLocalDir + "/%s_%s_%s_%s_%s.la"%(dateid,str('%d'%(time.time()*1000+random.randint(0,999))),'h50',game_id,model_id)

        dFile = open(destFile,'a')

        input_file = open('/Users/ljhn1829/Desktop/model_format/813301waxios')
        
        res_dic = {}
        for line in input_file.readlines():
            line = line.strip()
            if ',,' in line:
                info = line.split(',,')
                if len(info) < 2:
                    continue
                label  = info[0]
                detail = info[1:]
                tagcat_info = ''
                for detail_info in detail:
                    temp = detail_info.split(':')
                    if len(temp) < 2:
                        continue
                    tagcat_info += temp[0] + ':' + temp[1] + ';'
                
                if res_dic.has_key(label):
                    dFile.write(label + '\x01' + res_dic[label] + '\x01' + tagcat_info)
                    dFile.write('\n')
                    del res_dic[label]
                else:
                    res_dic[label] = tagcat_info
            else:
                info = line.split('\t')
                if len(info) < 2:
                    continue
                label = info[0]
                value = info[1]
                if res_dic.has_key(label):
                    dFile.write(label + '\x01' + value + '\x01' + res_dic[label])
                    dFile.write('\n')
                    del res_dic[label]
                else:
                    res_dic[label] = value
                
                
        dFile.close()      
        
if __name__ == '__main__':
    rsync_trainning_model_redis_game_model3()