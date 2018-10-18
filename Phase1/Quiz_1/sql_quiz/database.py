import sqlite3

class Database:
	def __init__(self,database_name):
		self.connection = sqlite3.connect(database_name,check_same_thread=False)
		self.cursor = self.connection.cursor()
	def __enter__(self):
		return self
	def __exit__(self,type,value,traceback):
		if self.connection:
			self.connection.commit()
			self.cursor.close()
			self.connection.close()
		else:
			pass
	
	def create_table(self,table_name,col1,col2):
		self.cursor.execute(
			"""CREATE TABLE {table_name}(
				pk INTEGER PRIMARY KEY AUTOINCREMENT
			);""".format(
				table_name=table_name
			)
		)

	def ass_column(self,table_name, column_name):
		self.cursor.execute(
			"""ALTER TABLE {table_name}
				ADD COLUMN {column_name}
			;""".format(
				table_name=table_name,
				column_name=column_name
			)
		)
	
	def add_row(self,array):
		col1=array[0]
		col2=array[1]
		col3=array[2]
		col4=array[3]
		col5=array[4]
		col6=array[5]
		self.cursor.execute(
			"""INSERT INTO TSLA(
				open,
            	high,
            	low,
            	closes,
            	adj_close,
            	volume
            	) VALUES(
					{col1},
					{col2},
					{col3},
					{col4},
					{col5},
					{col6}
				);""".format(
					col1=col1,
					col2=col2,
					col3=col3,
					col4=col4,
					col5=col5,
					col6=col6
				)
		)

		self.cursor.execute(
			"""INSERT INTO TSLA(
				open,
            	high,
            	low,
            	closes,
            	adj_close,
            	volume
            	) VALUES(
					?,
					?,
					?,
					?,
					?
				);""", (q, w, e, r, t)
		)