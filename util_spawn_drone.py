
def create_drone(drone_func, ttl = None):
    def inner_func():
        if ttl != None:
            for _ in range(ttl):
                drone_func()
        else:
            while True:
                drone_func()
                
    spawn_drone(inner_func)