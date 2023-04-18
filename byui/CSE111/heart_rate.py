"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# Get age from user
age = int(input("Enter your age: "))

# Calculate maximum heart rate
max_heart_rate = 220 - age

# Calculate slowest and fastest heart rates
slowest_heart_rate = int(0.65 * max_heart_rate)
fastest_heart_rate = int(0.85 * max_heart_rate)

# Output the results
print("To strengthen your heart, maintain your heart rate between", slowest_heart_rate, "and", fastest_heart_rate, "beats per minute.")