def main():
    time_str = input("What time is it? ").strip()
    time_float  = convert(time_str)

    if   7.0 <= time_float  <= 8.0:
        print("Breakfast Time")
    elif  12.0 <= time_float <= 13.0:
        print("Lunch Time")
    elif 18.0 <=  time_float <= 19.0:
        print("Dinner Time")
    else:
        print("No meal")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60.0

if __name__ == "__main__":
    main()