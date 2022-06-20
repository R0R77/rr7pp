from rr7ppx.database.postgres.afk_sql import AFKSQL
from rr7ppx.database.postgres.notes_sql import NOTESSQL
from rr7ppx.database.postgres.pmpermit_sql import PMPERMITSQL
from rr7ppx.database.postgres.dv_sql import DVSQL
from rr7ppx.database.postgres.welcome_sql import WELCOMESQL
from rr7ppx.database.postgres.filters_sql import FILTERSSQL




class Database(
	AFKSQL,
	NOTESSQL,
	PMPERMITSQL,
	DVSQL,
	WELCOMESQL,
	FILTERSSQL
	):
	pass
	
