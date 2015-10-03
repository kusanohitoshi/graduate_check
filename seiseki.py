#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
def get_s(item):
	return item[1:len(item)-1]
argvs = sys.argv
f = open(argvs[1])
data1 = f.read()
f.close()
lines = data1.split('\n')
dict_subj ={}
hissyu = []
hissyu_comp = [
"情報科学序説"
,"情報科学基礎"
,"情報科学ＰＢＬ"
,"プログラミングＡ"
,"プログラミングＢ"
,"プログラミングＣ"
,"プログラミングＤ"
,"情報数学基礎"
,"電子回路"
,"情報解析Ａ"
,"データ構造とアルゴリズム"
,"情報技術者と社会"
,"基礎工学ＰＢＬ（情報工学Ａ）"
,"基礎工学ＰＢＬ（情報工学Ａ）"
,"情報科学演習Ｃ"
,"情報科学演習Ｄ"
,"情報科学実験Ａ"
,"情報科学実験Ｂ"
,"情報科学実験Ｃ"
,"情報科学ゼミナールＡ"
,"情報科学ゼミナールＢ"
,"論理設計"
,"計算機言語"
,"計算機アーキテクチャ"
,"オペレーティングシステム"
,"データベース"
,"情報ネットワーク"
,"言語処理工学Ａ"
,"防災特論"
,"特別研究"
,"スポーツ実習　Ａ"
,"統計学　Ｃ-I"
,"解析学Ａ"
,"解析学Ｂ"
,"線形代数学Ａ"
,"線形代数学Ｂ"
,"数学演習Ａ"
,"数学演習Ｂ"
,"情報活用基礎"]
for line in lines:
	items = line.split(',')
	if len(items) == 15:
		#print(items[13][1:len(items[13])-1])
		if get_s(items[13]) == "合":
			#print(items[5])
			subj = get_s(items[5])
			if get_s(items[5]) == "必修" or get_s(items[6]) == "スポーツ実習　Ａ" or get_s(items[5]) == "専門基礎教育科目必修" or get_s(items[5]) == "情報処理教育科目":
				hissyu = hissyu + [get_s(items[6])]
			if subj != "情報処理教育科目":
				if subj not in dict_subj:
					dict_subj[subj] = int(get_s(items[9]))
				else:
					dict_subj[subj] = dict_subj[subj] + int(get_s(items[9]))
			elif get_s(items[6]) == "情報社会と倫理" or get_s(items[6]) == "アドバンスド情報リテラシー":
				if subj not in dict_subj:
					dict_subj[subj] = int(get_s(items[9]))
				else:
					dict_subj[subj] = dict_subj[subj] + int(get_s(items[9]))
#print(dict_subj["選択Ａ群".decode('utf-8')])
for item in hissyu_comp:
	if item not in hissyu:
		print(item+"isn't learned")
if dict_subj["選択Ａ群"]<8:
	print("選択Ａ足りない")
if dict_subj["選択Ｂ群"]<8:
	print("選択B足りない")
if dict_subj["選択Ｃ群"]<6:
	print("選択C足りない")

if dict_subj["基礎教養１"]<2:
	print("基礎教養1足りない")

if dict_subj["基礎教養３"]<2:
	print("基礎教養3足りない")

if dict_subj["現代教養科目"]<2:
	print("現代教養科目足りない")
if dict_subj["国際教養２"]<4:
	print("国際教養２足りない")
if dict_subj["第１外国語"]<8:
	print("第１外国語足りない")
if dict_subj["第２外国語"]<3:
	print("第２外国語足りない")
if dict_subj["健康・スポーツ教育科目"]<2:
	print("健康・スポーツ教育科目足りない")
if dict_subj["専門基礎教育科目選択"]<6:
	print("専門基礎教育科目選択足りない")
jiyu = 0
if "先端教養科目" in dict_subj:
	jiyu = jiyu + dict_subj["先端教養科目"]
if "国際教養１" in dict_subj:
	jiyu = jiyu + dict_subj["国際教養１"]
if "情報処理教育科目" in dict_subj:
	jiyu = jiyu + dict_subj["情報処理教育科目"]
if "基礎セミナー" in dict_subj:
	jiyu = jiyu + dict_subj["基礎セミナー"]
if jiyu<6:
	print("自由科目足りない")