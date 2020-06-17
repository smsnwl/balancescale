import csv
import datetime

global T0,T1

# f = open('data.csv')                                                                                                                                                                                    
# L=list(csv.reader(f))                                                                                                                                                                                   
# # print(L)                                                                                                                                                                                              
# # print(len(L))                                                                                                                                                                                         
# print("请输入T0:其格式为：2020-02-16-10-10-10")                                                                                                                                                          
# T0 = input()                                                                                                                                                                                            
# print("请输入T1:其格式为：2020-02-17-10-10-10")                                                                                                                                                          
# T1 = input()                                                                                                                                                                                            

def Call_history_data():
     f = open('data.csv')
     L=list(csv.reader(f))
     # print(L)                                                                                                                                                                                           
     # print(len(L))                                                                                                                                                                                      
     print("请输入起始时间T0:其格式为：2020-02-16-08-00-00")
     T0 = input()
     print("请输入终止时间T1:其格式为：2020-02-17-08-00-00")
     T1 = input()


     n=g=W=ng=nW=t=sum_ng=sum_nW=0
     t0 = datetime.datetime.strptime(T0, "%Y-%m-%d-%H-%M-%S")
     t1 = datetime.datetime.strptime(T1, "%Y-%m-%d-%H-%M-%S")
     # t0 = datetime.datetime.strptime("2020-02-17-23-47-27", "%Y-%m-%d-%H-%M-%S")                                                                                                                        
     # t1 = datetime.datetime.strptime("2020-02-17-23-47-49", "%Y-%m-%d-%H-%M-%S")                                                                                                                        
     D = 400;T = 3.2;H = 32
     limt_g = 4; limt_dW = 4; bW = 896.4

     print("检查砂轮规格：直径：",D,"mm；厚度：",T,"mm，孔径：",H,"mm")
     print("控制标准：")
     print("不平衡控制克数<=：",limt_g,"g/mm;","重量标准：",bW,"g;","重量超差控制克数<=：",limt_dW,"g")
     print("查询起止时间:",t0,"~",t1)
     for j in range(1,len(L)):#第j行                                                                                                                                                                        
          if  t1 >= datetime.datetime.strptime(L[j][0], "%Y-%m-%d-%H-%M-%S") >= t0 :
               time = datetime.datetime.strptime(L[j][0], "%Y-%m-%d-%H-%M-%S")
               g = int(L[j][2])
               W = int(L[j][12])
               n += 1
               if g >= limt_g:
                    # print("不平衡超差砂轮:",time,g,W)                                                                                                                                                   
                    sum_ng +=1
               if abs(W - bW) >= limt_dW:
                    # print("重量超差砂轮:",time,g,W)                                                                                                                                                      
                    sum_nW +=1
          else:
               pass

     print("区间检测砂轮总数:",n,"片;","不平衡超差砂轮数量:",sum_ng,"片；","重量超差数量:",sum_nW)
     print("已检测全部砂轮累计数：",len(L))



     return n, sum_ng, sum_nW, len(L)

if __name__=='__main__':
     global T0,T1
     Call_history_data()


