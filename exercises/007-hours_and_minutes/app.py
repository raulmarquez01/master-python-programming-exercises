def hours_minutes(seconds):
  # Your code here
  return seconds // 3600, (seconds % 3600) // 60

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
