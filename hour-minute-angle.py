Total_angle = 360

def findangle(hr,min):
    if hr < 0 or hr > 11:
        raise ValueError("invalid hours")

    if min < 0 or min > 59:
        raise ValueError ("invalid mins")

    angle_per_hour = Total_angle/12
    angle_per_min = Total_angle/60

    hour_hand_per_min_angle = float(angle_per_hour)/60

    hour_hand = (60*hr + min)* hour_hand_per_min_angle
    min_hand = min* angle_per_min

    res = abs(hour_hand-min_hand)
    if res > 180:
        res = 360 - res

    return res

print findangle(8,30)