import obd
import os

#Debug Flags
DEBUG_printToConsole = True

#Establish connection to OBD scanner
##Set scanner to MS mode for vehicles excluding Ford
##Set scanner to HS mode for Ford vehicles
###Mark down all vehicle information for vehicles that do not follow these rules
connection = obd.OBD()

#All commands to be grabbed from the vehicle
commandList = [obd.commands.RPM,
               obd.commands.RUN_TIME,
               obd.commands.SPEED,
               obd.commands.FUEL_LEVEL,
               obd.commands.GET_DTC]

#Go through the base command list to make sure all are supported
for cmd in commandList:
    if not connection.supports(cmd): commandList.remove(cmd)

def query():
    
    #For each command in the command list...
    for command in commandList:
        
        #Grab a reponse
        response = connection.query( command )
        
        #If the response is not null, then work on it
        if not response.is_null():
            
            #if debug printing is enabled, then print
            if DEBUG_printToConsole:
                print( cmd.name + ":" )
                print( "/t" + str( resp.value ) )
            

######### MAIN SEQUENCE
query()