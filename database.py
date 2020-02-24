import sqlite3

conn = sqlite3.connect('Production.db', check_same_thread=False)
from datetime import date, timedelta


def db_creation():
	yesterday = date.today() - timedelta(1)
	ydate = yesterday.strftime('%Y-%m-%d')
	ydate = '%s' % ydate

	conn.execute('''CREATE TABLE Production_Data
         (Material       CHAR(50),
         Date           date,
         Actual_Value   INT,
         Daily_Quota    INT);''')
	print("Table created successfully")
	print(ydate)

	# Today
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-05-13', 3000, 2000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Lean Gas', '2019-05-13', 1000, 1200)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Raw Gas', '2019-05-13', 5000, 4000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Sales Gas', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Injection Gas', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('LNG', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Sulphur', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Condensate', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C3 AGP', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C3 LNG', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C4 AGP', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C4 LNG', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C5 LNG', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C5+ AGP','2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Propylene', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('LPG', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Naptha', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Gasoline', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('JET A1', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Gasoil', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Fuel Oil', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Ethylene', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('PolyEthylene', '2019-05-13', 5000, 300)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('PolyProylene', '2019-05-13', 5000, 300)");

	# Yesterday
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-05-12', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Lean Gas', '2019-05-12', 20000, 15000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Raw Gas', '2019-05-12', 3000, 2000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Sales Gas', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Injection Gas', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('LNG', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Sulphur', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Condensate', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C3 AGP', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C3 LNG', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C4 AGP', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C4 LNG', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C5 LNG', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('C5+ AGP','2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Propylene', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('LPG', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Naptha', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Gasoline', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('JET A1', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Gasoil', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Fuel Oil', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Ethylene', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('PolyEthylene', '2019-05-12', 320000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('PolyProylene', '2019-05-12', 320000, 350000)");
	## Feb Month
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-01', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-02', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-03', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-04', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-05', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-06', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-07', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-08', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-09', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-10', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-11', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-12', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-13', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-14', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-15', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-16', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-17', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-18', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-19', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-20', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-21', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-22', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-29', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-24', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-25', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-26', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-27', 370000, 350000)");
	conn.execute(
		"INSERT INTO Production_Data (Material,Date,Actual_Value,Daily_Quota) VALUES ('Crude', '2019-02-28', 370000, 350000)");

	conn.commit()
	print("Records created successfully")

	cursor = conn.execute("SELECT Material,Date,Actual_Value,Daily_Quota from Production_Data")
	for row in cursor:
		print("Material = ", row[0])
		print("Date = ", row[1])
		print("Actual_Value = ", row[2])
		print("Daily_Quota = ", row[3], "\n")

	print("Operation done successfully")
	conn.close()

#db_creation()
def fetch_data(product, actual_planned, req_day):
	import sqlite3
	conn = sqlite3.connect('Production.db', check_same_thread=False)
	from datetime import date, timedelta

	if product == "crude oil":
		product = "Crude"
	elif product in ('logos', 'rockers', 'rock', 'ragas', 'rogers', 'rojas'):
		product = "Raw Gas"
	elif product in ('lean gas'):
		product = "Lean Gas"
	elif product in ('sales'):
		product = "Sales Gas"
	elif product in ('injection gas'):
		product = "Injection Gas"
	elif product in ('sulphur'):
		product = "Sulphur"
	elif product in ('condensate'):
		product = "Condensate"
	elif product in ('polypropylene'):
		product = "PolyProylene"
	elif product in ('polyethylene'):
		product = "PolyEthylene"
	elif product in ('ethylene'):
		product = "Ethylene"
	elif product in ('fuel oil', 'fuel'):
		product = "Fuel Oil"
	elif product in ('a1', 'jet a1', 'jet'):
		product = "JET A1"
	elif product in ('gasoline'):
		product = "Gasoline"
	elif product in ('gasoil'):
		product = "Gasoil"
	elif product in ('naptha', 'naphtha'):
		product = "Naptha"
	elif product in ('propylene'):
		product = "Propylene"

	if req_day == 'yesterday':
		yesterday = date.today() - timedelta(1)
		ydate = yesterday.strftime('%Y-%m-%d')
		ydate = '%s' % ydate
	elif req_day == 'today':
		ydate = date.today()
		ydate = ydate.strftime('%Y-%m-%d')
		ydate = '%s' % ydate

	prd = '%s' % product
	if actual_planned == "planned":
		cursor = conn.execute(
			"Select Daily_Quota from Production_Data where Material ='" + prd + "' and Date ='" + ydate + "'")
		try:
			for row in cursor:
				row_data = row[0]
				conn.close()
				return row_data
		except:
			pass


	elif actual_planned == "actual":
		cursor = conn.execute(
			"Select Actual_Value from Production_Data where Material ='" + prd + "' and Date ='" + ydate + "'")
		try:
			for row in cursor:
				row_data = row[0]
				conn.close()
				return row_data
		except:
			pass
