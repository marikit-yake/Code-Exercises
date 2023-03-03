def delete_nth(order,max_e):    
    def delete(item):
        order.reverse()
        order.remove(item)
        order.reverse()
    
    for motif in order:
        while order.count(motif) > max_e:
            delete(motif)
    
    return order
