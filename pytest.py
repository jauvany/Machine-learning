def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    return launch_day - current_day
  
from compute_launch import days_until_launch

def test_days_until_launch_4():
    assert(days_until_launch(22, 26) == 4)

def test_days_until_launch_0():
    assert(days_until_launch(253, 253) == 0)

def test_days_until_launch_0_negative():
    assert(days_until_launch(83, 64) == 0)
    
def test_days_until_launch_1():
    assert(days_until_launch(9, 10) == 1)
    
    
