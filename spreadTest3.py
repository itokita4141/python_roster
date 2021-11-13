# 参考 https://tanuhack.com/library-gspread/
import gspread
import json
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならないtest
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('even-dream-331809-e915b10b7783.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

# #ここから下にスプレッドシートを操作する記述を書くよ
# 17行から下に、スプレッドシートを操作するプログラムを書きます。
#
# ワークブックを選択
# スプレッドシートの中身を操作するためには、まず『どのスプレッドシートを操作するのか』をPythonに記述しなければいけません。
#
# ですので、真っ先にしないといけないこととして、プログラムから操作するスプレッドシートのワークブックを選択する必要があります。
#
# ワークブックを選択する方法が全部で3つありますが、実際に記述するのはその中で1つで良いです。
#
# # １．ファイル名を指定してワークブックを選択
workbook = gc.open('excelRoster')

# ２．スプレッドシートキーを指定してワークブックを選択（おすすめ）
workbook = gc.open_by_key('1qj66WOF9XEMrXjBgHeoR5grXFi0vzh2nH74aqqITE94')

# ３．URLを指定してワークブックを選択を開く
workbook = gc.open_by_url('https://docs.google.com/spreadsheets/d/1qj66WOF9XEMrXjBgHeoR5grXFi0vzh2nH74aqqITE94/edit#gid=0')

#################################
# パラメータ
workbook.title	#スプレッドシートのタイトルを取得する
workbook.id		#スプレッドシートキーを取得する
# ワークブックを選択する
# gc.open('ファイル名')
# ：ファイル名を指定してワークブックを選択
# gc.open_by_key('スプレッドシートキー')
# ：スプレッドシートキーを指定してワークブックを選択
# gc.open_by_url('URL')
# ：URLを指定してワークブックを選択
# どれを使うかは完全に好みの問題なので、自分が指定しやすいものを選んで下さい。
#
# おすすめは2つ目のスプレッドシートキーを指定する方法です。
#
# 理由もちゃんとあって、IMPORTRANGE関数との親和性があって何かと便利なんですよね。
#
# 	【超便利】スプレッドシートで別シートから参照したり集計したりする方法まとめ
# とくに理由がなければ、ぜひスプレッドシートキーを取得してワークブックを選択してください。
#
# ワークシートの操作
# 前章で、ワークブックを選択することができました。
#
# 次にやるべき処理は、どのワークシートを選択してどういう処理をするのかという設定です。
#
# まず、どんなワークシートがワークブックに存在するのか知るために、ワークシート一覧を取得してみます。
#
# ワークシートの一覧を表示する
#### 前提条件 #######################
# workbook = gc.open_by_key('スプレッドシートキー')
####################################

# シートの一覧を一次元配列に格納する
worksheet_list = workbook.worksheets()

#################################
# パラメータや便利なチップス
worksheet_list[0].title	#一番最初のワークシートのタイトルを取得する
worksheet_list[0].id	#一番最初のワークシートIDを取得する
len(worksheet_list)		#ワークシートの一覧数を取得
# ワークシート一覧を一次元配列に格納する
workbook.worksheets()
# ワークシートを指定する
#### 前提条件 #######################
workbook = gc.open_by_key('1qj66WOF9XEMrXjBgHeoR5grXFi0vzh2nH74aqqITE94')
####################################

# １．最初のワークシートを指定
# [注意]workbook.sheet5のように、1以外の数字は指定できない
worksheet = workbook.sheet1

# ２．ワークシート名を直接指定
# worksheet = workbook.worksheet('excelRoster')

# ３．開きたいワークシートのインデックスを指定
# [補足]ワークシートのインデックスは0から始まる
# get_worksheet(4)は、5番目のワークシートを選択する
# worksheet = workbook.get_worksheet(1)
# [応用]最後のワークシートを指定：len(worksheet_list)でワークシートの一覧数を取得
# worksheet = workbook.get_worksheet(len(worksheet_list)-1)

# ####################################
# # パラメータ
# worksheet.title								# ワークシート名を取得する
# worksheet.update_title('新しいワークシート名')	# ワークシート名を変更する
# worksheet.id								# ワークシートIDを取得する
# # ワークシートを選択する
# workbook.sheet1 #：一番左のシートを選択
# workbook.worksheet('ワークシート名') #：ワークシート名を指定して選択
# # workbook.get_worksheet(index) #：index-1番目のシートを選択
# # ワークシートを作成・削除する
# #### 前提条件 #######################
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
# ####################################

# ワークシートを末尾に新規作成する
# [補足]100行26列の新しいワークシートを作成
# workbook.add_worksheet(title='ワークシート名', rows=100, cols=26)

# 指定したワークシートを削除する
# workbook.del_worksheet(worksheet)
# ワークシートを新規作成する
# workbook.add_worksheet(title='ワークシート名', rows=行数, cols=列数)
# ワークシートを削除する
# workbook.del_worksheet('選択したワークシート')
# セルの操作
# ワークブックを選択して、ワークシートを選択して。
#
# 次は、お待ちかねの『セルの操作』を行います。
#
# この章では、セルの値を取得したり、更新したり。検索したり、削除したりする方法を紹介します。
#
# セルの値を取得する
# その１：セルの番地を直接指定して、セルの値を取得する
#### 前提条件 #######################
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
####################################

# １．ラベルを指定してセルの値を取得する
cell_value = worksheet.acell('B1').value

# ２．行番号と列番号を指定してセルの値を取得する（左：行番号、右：列番号）
cell_value = worksheet.cell(1, 2).value

# ３．ラベルを指定して複数セルの値を一次元配列に格納する
range = worksheet.range('A1:B10')
# ラベルを指定してセルの値を取得する
# acell('B1').value
# 行番号(左)と列番号（右）を指定してセルの値を取得する
# cell(1, 2).value
# ラベルを指定して複数セルの値を一次元配列に格納する
# range('A1:B10')
# その２：指定した行や列、ワークシート単位で、セルの値を取得する
#### 前提条件 #######################
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
###################################

# １．行の値を全て一次元配列に格納する
# [第1引数]値を取得したい行番号
# row_list = worksheet.row_values(1)
# [補足]第2引数が2の場合、値ではなく数式を格納する
# row_list = worksheet.row_values(1,2)

# ２．列の値を全て一次元配列に格納する
# [第1引数]値を取得したい列番号
# col_list = worksheet.col_values(1)
# [補足]第2引数が2の場合、値ではなく数式を格納する
# col_list = worksheet.col_values(1,2)

# ３．ワークシートの値の全てを多次元配列に格納する
cell_list = worksheet.get_all_values()
print(cell_list)
# ４．ワークシートの値の全てを辞書型のリストに格納する
# [第1引数]empty2zero - 空のセルをゼロに変換するかどうかを指定する
# [第2引数]head - スプレッドシートの数値に従って1から始まるキーとして使用する行を決定する
# [第3引数]default_blank - 空のセルを空の文字列またはゼロ以外の何かに変換するかどうかを指定する
# cell_dict = worksheet.get_all_records(empty2zero=False、head=1、default_blank='')
# 行の値を全て一次元配列に格納する
# row_values(行番号)
# 列の値を全て一次元配列に格納する
# col_values(列番号)
# ワークシートの値の全てを多次元配列に格納する
# get_all_values()
# ワークシートの値の全てを辞書型のリストに格納する
# get_all_records(empty2zero=False、head=1、default_blank='')
# セルの値を更新する
#### 前提条件 #######################
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
# ####################################
#
# # １．ラベルを指定してセルの値を更新する
# worksheet.update_acell('B1','更新する値')
#
# # ２．行番号と列番号を指定してセルの値を更新する
# worksheet.update_cell(1, 2, '更新する値')
#
# # ３．セルの値をまとめて更新する（バッチ処理）
# cell_list = worksheet.range('A1:B10')
# for cell in cell_list:
# 	cell.value = '更新する値'
# worksheet.update_cells(cell_list)
# ラベルを指定してセルの値を更新する
# update_acell('B1','更新する値')
# 行番号と列番号を指定してセルの値を更新する
# update_cell(1, 2, '更新する値')
# セルの値をまとめて更新する（バッチ処理）
# update_cells(cell_list)
# 	[データI/O]スプレッドシート×DataFrameを一気に変換する方法
# セルの値を検索・置換する
# その１：単一のセルを検索・置換する
# 置換とは書いていますが、詳しく話すとセルを検索した後にその値を更新しているだけです。
#
# #### 前提条件 #######################
# import re	#Pythonで正規表現を使うライブラリ
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
# ####################################
#
# # １．検索
# # [補足]シート内に同じ文字列が複数ある場合、1番最初に出現したセルにマッチする
# cell = worksheet.find('検索したい文字列')
#
# # [応用]正規表現で検索
# value_re = re.compile(r'正規表現')
# cell = worksheet.find(value_re)
#
# ##パラメータ
# cell.row	# 行番号を取得
# cell.col	# 列番号を取得
#
# # ２．置換
# worksheet.update_cell(cell.row, cell.col, '更新する値')
# １つだけ検索
# find('検索したい文字列')
# その２：複数のセルを検索・置換する
# #### 前提条件 #######################
# import re	#Pythonで正規表現を使うライブラリ
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
# ####################################
#
# # １．検索
# # 一致したものは、一次元配列に格納する
# cell_list = worksheet.findall('検索したい文字列')
#
# # [応用]正規表現で検索
# value_re = re.compile(r'正規表現')
# cell_list = worksheet.findall(value_re)
#
# # ２．置換
# for cell in cell_list:
# 	cell.value = '更新する値'
# worksheet.update_cells(cell_list)
# すべて検索
# findall('検索したい文字列')
# その他の操作
# #### 前提条件 #######################
# workbook = gc.open_by_key('スプレッドシートキー')
# worksheet = workbook.sheet1
# ####################################
#
# worksheet.add_cols(col)		#col数だけ列を増やす
# worksheet.add_rows(row)		#row数だけ行を増やす
# worksheet.col_count 		#選択したワークシートの列数を取得
# worksheet.row_count 		#選択したワークシートの行数を取得
# worksheet.delete_row(row) 	#選択した行を削除する
# worksheet.clear() 			#選択したワークシートの値を全てクリアする

