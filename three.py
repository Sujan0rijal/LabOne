'7. You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each'
'of the 10 stops on the way.How long will the bus journey take? Alternatively, you could run to university.'
'You jog the first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again.'
'Will this be quicker or slower than the bus?'

bus_distance= float(input('enter the distance travelled by bus:'))
man_jogging1=float(input('enter the jogging distance of man in first time:'))
man_jogging2=float(input('enter the jogging distance of man in second time:'))
man_running=float(input('enter the running distance by man:'))

speed_bus=float(input('enter the speed od bus:'))
speed_jog=float(input('enter the speed of man in jogging:'))
speed_running=float(input('enter the speed of man in running'))
bus_stops=float(input('enter the total bus stops:'))
bus_stops_time= float(input('enter the time of bus stops:'))

time_bus= bus_distance/speed_bus
totaltime_bus=time_bus+bus_stops_time*bus_stops
print(f'the time taken by bus to travelled is{totaltime_bus}')

time_jog1=man_jogging1/speed_jog
time_jog2=man_jogging2/speed_jog
time_running=man_running/speed_running
totaltime_man=time_jog2+time_jog2+time_running
print(f'the total time taken by man is {totaltime_man}')

if totaltime_man < totaltime_bus:
    print(f'man is faster than bus')
else:
    print(f'bus is faster than man')

