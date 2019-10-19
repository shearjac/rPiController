from gps3 import gps3

def cls() : print("\n"*10)

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        cls()
        data_stream.unpack(new_data)
        print('Altitud'+"\t\t\t"+'= ', data_stream.TPV['alt'])
        print('Speed'+"\t\t\t"+'= ', data_stream.TPV['speed'])