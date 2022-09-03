import obd
import sys


def getEvoDiagnosticCodes(log_file_name, command):
	old_stdout = sys.stdout

	log_file = open(f"{log_file_name}","w")

	sys.stdout = log_file

	connection = obd.OBD()
	cmd = obd.commands[f"{command}"] # select an OBD command (sensor)

	response = connection.query(cmd) # send the command, and parse the response

	print(response.value) # returns unit-bearing values thanks to Pint

	sys.stdout = old_stdout

	log_file.close()