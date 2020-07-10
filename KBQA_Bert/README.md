### 环境说明
	python--3.5
	tensorflow--1.12
	
### 目录及文件说明
	Bert
		github地址下载的bert程序代码，里边是python文件
	Data
		NLPCC	原始语料库（问题、三元组、答案）
		NER_Data	NER任务数据集
		Sim_Data	属性链接任务数据集
		- construct_dataset.py	生成NER_Data的数据
		- construct_dataset_attribute.py	生成Sim_Data的数据
	ModelParams				
		cased_L12_H768_A12文件夹：github地址下载的bert预训练模型
	Output
		TensorFlow训练模型输出文件夹
	基于Bert的实体识别模块
		- run_ner.py	main函数
		- lstm_crf_layer.py
		- conlleval.py
		- colleval.pl
		- run_ner.sh
	基于Bert的属性链接（句子相似度）
		- run_similarity.py	main函数
		- args.py	run_similarity配置
	问答模块
		- kbqa_predict.py	问答main函数
		- answer_search.py	根据question和entity进行cypher查询
		- min_distance.py	实体间最小距离计算
### 使用说明
	- answer_search.py	修改neo4j连接配置
    - kbqa_predict.py	运行KBQA主程序
    
