import argparse



#1.创建 ArgumentParser() 对象

parser = argparse.ArgumentParser()



#2.调用 add_argument() 方法添加参数

parser.add_argument('--integer', type=int, help='display an integer')
parser.add_argument('--bert', type=str, help='display a string')



#3.使用 parse_args() 解析添加的参数

args = parser.parse_args()



print(args.integer)   #打印出该参数
print(args.bert)   #打印出该参数
