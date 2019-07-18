# Contents:
1. Text Classification


# 1. Text Classification

使用BERT微调实现中文文本分类
 

# 环境：

Python：3.6.4

框架：Pytorch

 

# Procedures

下面根目录均指01_Text_Classification/

## Step 1：准备

下载：

1. 预训练好的TensorFlow模型：[chinese_L-12_H-768_A-12](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)
2. 中文数据集：[Train and Dev](https://pan.baidu.com/s/1e-piSCvDz7To4HsZaulV-A)

将chinese_L-12_H-768_A-12.zip解压在根目录下；在根目录下建立文件夹：/glue_data/SouGou，上述数据集放在这里。

 

## Step 2：执行

### 1. 将TensorFlow预训练模型转换为PyTorch模型

在根目录下：

```
python convert_tf_to_pytorch/convert_tf_checkpoint_to_pytorch.py --tf_checkpoint_path ./chinese_L-12_H-768_A-12/bert_model.ckpt --bert_config_file ./chinese_L-12_H-768_A-12/bert_config.json --pytorch_dump_path ./chinese_L-12_H-768_A-12/pytorch_model.bin
```

生成的PyTorch模型 **pytorch_model.bin** 位于chinese_L-12_H-768_A-12文件夹下

 

### 2. Fine-Tuning

在根目录下：

```
python3 src/run_classifier_word.py --task_name NEWS --do_train --do_eval --data_dir ./glue_data/SouGou --vocab_file ./chinese_L-12_H-768_A-12/vocab.txt --bert_config_file ./chinese_L-12_H-768_A-12/bert_config.json --init_checkpoint ./chinese_L-12_H-768_A-12/pytorch_model.bin --max_seq_length 256 --train_batch_size 24 --learning_rate 2e-5 --num_train_epochs 3.0 --output_dir ./result/
```

产生的结果在result文件夹下

 

## Result

3个epoch后，得到结果：

![result.png](https://i.loli.net/2019/07/18/5d2fe90f6ddd463577.png)


