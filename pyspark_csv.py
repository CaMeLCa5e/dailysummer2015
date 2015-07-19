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
	