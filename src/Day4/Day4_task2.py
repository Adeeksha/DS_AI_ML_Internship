raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(raw_logs)
unique_users=set(raw_logs)
print(unique_users)
verify="ID05"  in unique_users
print(verify)
print("length of raw_logs:",(len(raw_logs)))
print("length of unique_users:",(len(unique_users)))
