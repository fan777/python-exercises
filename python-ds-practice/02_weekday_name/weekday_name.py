def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weekdays = [
      'Sunday',
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
    ]
    
    if day_of_week < 1 or day_of_week > 7:
      return None
    
    return weekdays[day_of_week - 1]

print('should expect Monday:', weekday_name(2))
print('should expect Saturday:', weekday_name(7))