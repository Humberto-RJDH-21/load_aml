# IMPORTS
import os
import pyodbc
import random
import numpy as np
from string_fn import randomStringDigits, randomDigits
from constants import PRODUCTO, INSTR_MONETARIO, MONEDA, CONCEPTO, CONTRATANTE, FECHAS


# VARS FOR DB
database = 'STP_UAT'
# Obtiene el username desde una variable de ambiente [AML_USERNAME], 
# si no le asigna por default: STP_USERNAME
username = os.environ.get('AML_USERNAME','STP_USERNAME')
# Obtiene el password desde una variable de ambiente [AML_PASSWORD], 
# si no le asigna por default: STP_PSW
password = os.environ.get('AML_PASSWORD','STP_PSW')
# CREATE CONNECTION
cnxn = pyodbc.connect('DSN=MYMSSQL;DATABASE='+database +
                      ';UID='+username+';PWD='+password)
# CREATE CURSOR
cursor = cnxn.cursor()

# Número de registros a insertar
NO_REGISTROS=200
for x in range(NO_REGISTROS):
    # print("====================================================")
    # GETTING CONSTANTS
    CONTR_ID = CONTRATANTE[random.randrange(0, 72)]
    # poliza
    #print("POLIZA:", CONTR_ID[0])
    POLIZA = CONTR_ID[0]
    # Contratante
    #print("CONTRATANTECD:", CONTR_ID[1])
    CONTRATCD = CONTR_ID[1]
    # CODOPER
    #print("CODOPER:", randomDigits(8))
    CODOPER = randomDigits(8)
    # TIPOOPERACIONID
    CONCEPT = CONCEPTO[random.randrange(0, 6)]
    #print("TIPOOPERACIONID:", CONCEPT[0])
    TIPOOPERACIONID = CONCEPT[0]
    # INSTRMONETARIOID
    #print("INSTRMONETARIOID", random.choice(INSTR_MONETARIO))
    INSTRMONETID = random.choice(INSTR_MONETARIO)
    # MONEDAID
    MON_VAR = MONEDA[random.randrange(0, 4)]
    #print("MONEDAID:", MON_VAR[0])
    MONEDAID = MON_VAR[0]
    # PRODUCTO
    #print("PRODUCTOID:", random.choice(PRODUCTO))
    PRODUCTOID = random.choice(PRODUCTO)
    # MONTOCNTR
    if MON_VAR[0] == 'MXN':
        MONTO = random.randrange(10, 5000)
    else:
        MONTO = random.randrange(100, 2500)
    #print("MONTOCNTR:", MONTO)
    MONTOCNTR = MONTO
    # TIPOCAMBIOCNTR
    #print("TIPOCAMBIOCNTR:", MON_VAR[1])
    TIPOCAMBIO = MON_VAR[1]
    # MONTOMNCNTR
    FIRST = int(MONTO)
    SECND = float(MON_VAR[1])
    MONTOMNCNTR = (FIRST*SECND)
    #print("MONTOMNCNTR:", MONTOMNCNTR)

    # MONTOUSD
    if MON_VAR[0] == 'MXN':
        MONTOUSD = MONTOMNCNTR/19.16
    else:
        MONTOUSD = MONTO
    #print("MONTOUSD:", MONTOUSD)
    # DS_CONCEPTO_OPERACION
    DSCONCEPTOPER = CONCEPT[1]
    #print("DS_CONCEPTO_OPERACION:", CONCEPT[1])
    # DS_CONCEPTO_PAGO
    DSCONCEPTOPAGO = CONCEPT[2]

    FECHA=FECHAS[random.randrange(0, 9)]
    ROW=(CONTRATCD, POLIZA, CODOPER, TIPOOPERACIONID, INSTRMONETID, MONEDAID, PRODUCTOID, MONTOCNTR, TIPOCAMBIO, MONTOMNCNTR, MONTOUSD,DSCONCEPTOPER, DSCONCEPTOPAGO, 'N', 'N', 'O', 0, 'S', '3', 'ADMIN', '00:00:00', FECHA[0], FECHA[1], FECHA[2], FECHA[3])    
    cursor.execute('''INSERT INTO STP_UAT.IFT.MTS_HOPERACIONESCNTR(CONTRATANTECD, NUMPOLIZACNTR, CODOPER, TIPOOPERACIONID, INSTRMONETARIOID, MONEDAID, PRODUCTOID, MONTOCNTR, TIPOCAMBIOCNTR, MONTOMNCNTR, MONTOUSD, DS_CONCEPTO_OPERACION,
                                                              DS_CONCEPTO_PAGO, VIGENTE_CANCELACION, SW_TRANSACCION_MANUAL, STATUS_PROV, ID_PROCESO, SWSINCRONIZADO, CVE_ESTADO, CREADO_POR, HORA_OPERACION, FECHAOPERACIONCNTR,
                                                              FEC_CREACION, FEC_APERTURA_PRODUCTO, FEC_FIN_PRODUCTO)
               VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',ROW)
    cnxn.commit()