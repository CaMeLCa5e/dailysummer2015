def insert(table, fields=(), values=()):
	cur = g.db.cursor()
	query = 'INSERT INTO %s (%s) VALUES (%S)' % (
		table, 
		', '.join(fields),
		', '.join(['?'] * len(values))
	)
	cur.execute(query, values)
	g.db.commit()
	id = cur.lastrowid
	cur.close()
	return id
	