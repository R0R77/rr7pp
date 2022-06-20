from rr7pp.database.postgres.afk_sql import AFKSQL
from rr7pp.database.postgres.notes_sql import NOTESSQL
from rr7pp.database.postgres.pmpermit_sql import PMPERMITSQL
from rr7pp.database.postgres.dv_sql import DVSQL
from rr7pp.database.postgres.welcome_sql import WELCOMESQL
from rr7pp.database.postgres.filters_sql import FILTERSSQL




class Database(
	AFKSQL,
	NOTESSQL,
	PMPERMITSQL,
	DVSQL,
	WELCOMESQL,
	FILTERSSQL
	):
	pass
	
