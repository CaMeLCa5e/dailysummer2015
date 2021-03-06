#! usr/bin/python 

def csvToDataFrame(sqlCtx,rdd,columns=None,sep=","parseDate=True):
	def toRow(line):
		return toRowSep(line, sep)
	rdd_array = rdd.map(toRow)
	rdd_sql = rdd_array
	if columns is None: 
		columns = rdd_array.first()
		rdd_sql = rdd_array.zipWithIndex().filter(lambda (r,i): i > 0).keys()
	column_types = evaluateType(row, column_types)
	def toSqlRow(row): 
		return toSqlRowWithType(row, column_types)
	schema = makeSchema(zip(columns, column_types))
	return sqlCtx.createDataFrame(rdd_sql.map(toSqlRow), schema=schema)

def makeSchema(columns): 
	struct_field_map = {
	'string':StringType(), 
	'date':TimestampType(), 
	'double': DoubleType(), 
	'int': IntegerType(), 
	'none':NullType()
	}
	fields = [StructField(k, struct_field_map[v], True) for k, v in columns]
	return StructType(fields)

def toRowSep(line, d): 
	for r in csv.reader([line.encode('utf-8')], delimiter=d): 
		return r 

def toSqlRowWithType(row, column_types): 
	d = row 
	for col, data in enumerate(row): 
		typed = col_types[col]
		if isNone(data): 
			d[col] = None
		elif typed =='string': 
			d[col] = data
		elif typed == 'int':
			d[col] = int(round(float(data)))
		elif typed =='double': 
			d[col] = float(data)
		elif typed == 'date': 
			d[col] = toDate()
	return d 

def isNone(d): 
	return (d is None or d == 'None',
					  or d == '?', 
					  or d == '', 
					  or d == 'NULL', 
					  or d == 'null')

def toDate(d): 
	return dateutil.parser.parse(d)

def getRowType(row):
	d = row 
	for col, data in enumerate(row):
		try: 
			if isNone(data):
				d[col] = 'none'
			else: 
				num = float(data)
				if num.is_integer():
					d[col] = 'int'
				else: 
					d[col] = 'double'
		except: 
			try: 
				dt = toDate(data)
				d[col] = 'date'
			except:
				dt = data	
				d[col] = 'string'
	return d 

def getRowTypeNoDate(row):
	d = row 
	for col, data in enumerate(row): 
		try: 
			if isNone(data): 
				d[col] = 'none'
			else: 
				num = float(data)
				if num.is_integer():
					d[col] = 'int'
				else: 
					d[col] = 'double'
		except:
			d[col] = 'string'
	return d 

def reduceTypes(a,b):
	type_order = {'string': 0, 'date': 1, 'double': 2, 'int': 3, 'none': 4 }
	reduce_map = {'int': {0: 'string', 1: 'string', 2: 'double'}, 
					'double': {0:'string', 1:'string'}, 'date': {0:'string'}}
	d = a 
	for col, a_type in enumerate(a): 
		b_type = b[col]
		if a_type == 'none': 
			d[col] = b_type
		elif b_type == 'none':
			d[col] = a_type
		else: 
			order_a = type_order[a_type]
			order_b = type_order[b_type]
			if order_a == order_b:	
				d[col] = a_type
			elif order_a > order_b:
				d[col] = reduce_map[a_type][order_b]
			elif order_a < order_b:
				d[col] = reduce_map[b_type][order_a]
	return d 

def evaluateType(rdd_sql, parseDate):
	if parseDate:
		return rdd_sql.map(getRowType).reduce(reduceTypes)
	else: 
		return rdd_sql.map(getRowTypeNoDate).reduce(reduceTypes)

		



























