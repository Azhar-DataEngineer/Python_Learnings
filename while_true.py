# i = 1

# while True:
#     answer = input("Do you want to continue? (yes/no): ").strip().lower()
#     if answer == "yes":
#         break
# print("Thank you for continuing!")


count=0

while True:
    answer = input("Do you agree ? yes/no:")
    if answer.lower() == "yes":
        print("You agreed!")
        break
    else:
        count += 1
        
        if count >= 3:
            print("3 strikes, you are out!")
            break













# print("\n" + "="*70)
# print("🚀 10 REAL-WORLD USE CASES FOR WHILE TRUE LOOPS")
# print("="*70)

# print("\n1️⃣ USER INPUT VALIDATION")
# print("-" * 30)
# print("Keep asking until valid input is provided:")

# def get_valid_age():
#     while True:
#         try:
#             age = int(input("Enter your age (18-120): "))
#             if 18 <= age <= 120:
#                 return age
#             else:
#                 print("❌ Age must be between 18 and 120. Try again.")
#         except ValueError:
#             print("❌ Please enter a valid number. Try again.")

# # Example usage (commented out for demo)
# # age = get_valid_age()
# # print(f"✅ Valid age entered: {age}")

# print("\n2️⃣ MENU SYSTEM / APPLICATION MAIN LOOP")
# print("-" * 40)
# print("Classic application menu that runs until user chooses to exit:")

# def banking_system():
#     balance = 1000.0
    
#     while True:
#         print(f"\n💰 BANK SYSTEM - Balance: ${balance:.2f}")
#         print("1. Check Balance")
#         print("2. Deposit Money")  
#         print("3. Withdraw Money")
#         print("4. Exit")
        
#         choice = input("Choose option (1-4): ").strip()
        
#         if choice == "1":
#             print(f"Current balance: ${balance:.2f}")
#         elif choice == "2":
#             try:
#                 amount = float(input("Deposit amount: $"))
#                 if amount > 0:
#                     balance += amount
#                     print(f"✅ Deposited ${amount:.2f}")
#                 else:
#                     print("❌ Amount must be positive")
#             except ValueError:
#                 print("❌ Invalid amount")
#         elif choice == "3":
#             try:
#                 amount = float(input("Withdraw amount: $"))
#                 if 0 < amount <= balance:
#                     balance -= amount
#                     print(f"✅ Withdrew ${amount:.2f}")
#                 else:
#                     print("❌ Invalid amount or insufficient funds")
#             except ValueError:
#                 print("❌ Invalid amount")
#         elif choice == "4":
#             print("👋 Thank you for using Bank System!")
#             break
#         else:
#             print("❌ Invalid choice. Please try again.")

# # Example: banking_system()  # Uncommented to run

# print("\n3️⃣ NETWORK CONNECTION RETRY MECHANISM")
# print("-" * 40)
# print("Keep trying to connect until successful:")

# import time
# import random

# def connect_to_server():
#     """Simulates connecting to a server with random failures"""
#     attempts = 0
#     max_attempts = 5
    
#     while True:
#         attempts += 1
#         print(f"🔌 Connection attempt {attempts}...")
        
#         # Simulate random connection success/failure
#         if random.random() > 0.6:  # 40% success rate
#             print("✅ Connected successfully!")
#             return True
        
#         if attempts >= max_attempts:
#             print("❌ Max attempts reached. Connection failed.")
#             return False
            
#         print(f"❌ Connection failed. Retrying in 2 seconds...")
#         time.sleep(0.5)  # Reduced for demo

# # Example: connect_to_server()

# print("\n4️⃣ FILE PROCESSING QUEUE")
# print("-" * 28)
# print("Continuously process files from a queue:")

# def file_processor():
#     """Simulates processing files from a queue"""
#     file_queue = ["document1.pdf", "image2.jpg", "data3.csv", "report4.docx"]
#     processed = 0
    
#     while True:
#         if not file_queue:
#             print("📁 No more files to process. Queue empty.")
#             break
            
#         current_file = file_queue.pop(0)
#         print(f"📄 Processing: {current_file}")
        
#         # Simulate processing time
#         time.sleep(0.3)
        
#         processed += 1
#         print(f"✅ Completed: {current_file}")
        
#         # Check if we should continue
#         if processed >= 10:  # Safety limit for demo
#             print("🛑 Processing limit reached.")
#             break
    
#     print(f"🎯 Total files processed: {processed}")

# # Example: file_processor()

# print("\n5️⃣ GAME MAIN LOOP")
# print("-" * 20)
# print("Classic game loop structure:")

# def number_guessing_game():
#     """Simple number guessing game"""
#     import random
    
#     target = random.randint(1, 100)
#     attempts = 0
#     max_attempts = 7
    
#     print("🎮 GUESS THE NUMBER GAME (1-100)")
#     print(f"You have {max_attempts} attempts!")
    
#     while True:
#         attempts += 1
        
#         try:
#             guess = int(input(f"Attempt {attempts}: Enter your guess: "))
            
#             if guess == target:
#                 print(f"🎉 Congratulations! You guessed {target} in {attempts} attempts!")
#                 break
#             elif guess < target:
#                 print("📈 Too low!")
#             else:
#                 print("📉 Too high!")
                
#             if attempts >= max_attempts:
#                 print(f"💔 Game Over! The number was {target}")
#                 break
                
#         except ValueError:
#             print("❌ Please enter a valid number")
#             attempts -= 1  # Don't count invalid input as attempt

# # Example: number_guessing_game()

# print("\n6️⃣ DATA STREAMING / REAL-TIME MONITORING")
# print("-" * 42)
# print("Monitor system resources continuously:")

# def system_monitor():
#     """Simulates system resource monitoring"""
#     import random
    
#     monitor_cycles = 0
    
#     while True:
#         monitor_cycles += 1
        
#         # Simulate system metrics
#         cpu_usage = random.uniform(10, 90)
#         memory_usage = random.uniform(30, 95)
#         disk_usage = random.uniform(40, 85)
        
#         print(f"\n📊 SYSTEM MONITOR - Cycle {monitor_cycles}")
#         print(f"CPU: {cpu_usage:.1f}%")
#         print(f"Memory: {memory_usage:.1f}%") 
#         print(f"Disk: {disk_usage:.1f}%")
        
#         # Alert on high usage
#         if cpu_usage > 80:
#             print("🚨 HIGH CPU USAGE ALERT!")
#         if memory_usage > 90:
#             print("🚨 HIGH MEMORY USAGE ALERT!")
            
#         # Safety exit for demo
#         if monitor_cycles >= 5:
#             print("🛑 Monitoring stopped (demo limit)")
#             break
            
#         time.sleep(0.5)  # Monitor every 0.5 seconds

# # Example: system_monitor()

# print("\n7️⃣ CHAT BOT / CONVERSATIONAL AI")
# print("-" * 35)
# print("Keep conversation going until user exits:")

# def simple_chatbot():
#     """Simple rule-based chatbot"""
    
#     responses = {
#         "hello": "👋 Hi there! How can I help you?",
#         "hi": "👋 Hello! What's on your mind?",
#         "how are you": "😊 I'm doing great! Thanks for asking.",
#         "weather": "🌤️ I don't have weather data, but I hope it's nice!",
#         "time": "⏰ I don't have access to current time, sorry!",
#         "help": "💡 I can chat about basic topics. Try saying hello!",
#     }
    
#     print("🤖 SIMPLE CHATBOT - Type 'quit', 'exit', or 'bye' to end")
    
#     while True:
#         user_input = input("\nYou: ").strip().lower()
        
#         if user_input in ['quit', 'exit', 'bye', 'goodbye']:
#             print("Bot: 👋 Goodbye! Have a great day!")
#             break
        
#         # Find response
#         response_found = False
#         for keyword, response in responses.items():
#             if keyword in user_input:
#                 print(f"Bot: {response}")
#                 response_found = True
#                 break
        
#         if not response_found:
#             print("Bot: 🤔 I don't understand that. Try asking about the weather or saying hello!")

# # Example: simple_chatbot()

# print("\n8️⃣ WEB SCRAPING / API POLLING")
# print("-" * 33)
# print("Continuously check for new data:")

# def api_poller():
#     """Simulates polling an API for new data"""
    
#     last_data_count = 0
#     poll_cycles = 0
    
#     while True:
#         poll_cycles += 1
        
#         # Simulate API call
#         print(f"🌐 Polling API... (Cycle {poll_cycles})")
        
#         # Simulate varying data counts
#         current_data_count = last_data_count + random.randint(0, 3)
        
#         if current_data_count > last_data_count:
#             new_items = current_data_count - last_data_count
#             print(f"📈 Found {new_items} new items!")
#             last_data_count = current_data_count
            
#             # Process new data
#             for i in range(new_items):
#                 print(f"  📝 Processing new item {last_data_count - new_items + i + 1}")
#         else:
#             print("📊 No new data available")
        
#         # Safety exit for demo
#         if poll_cycles >= 6:
#             print("🛑 Polling stopped (demo limit)")
#             break
            
#         print("⏳ Waiting 3 seconds before next poll...")
#         time.sleep(0.5)  # Reduced for demo

# # Example: api_poller()

# print("\n9️⃣ LOG FILE MONITORING")
# print("-" * 25)
# print("Watch log files for new entries:")

# def log_monitor():
#     """Simulates monitoring log files"""
    
#     log_entries = [
#         "INFO: User login successful",
#         "WARNING: High memory usage detected", 
#         "ERROR: Database connection failed",
#         "INFO: Backup completed successfully",
#         "CRITICAL: Security breach detected!",
#     ]
    
#     processed_logs = 0
    
#     while True:
#         if processed_logs < len(log_entries):
#             log_entry = log_entries[processed_logs]
#             processed_logs += 1
            
#             print(f"📝 New log: {log_entry}")
            
#             # Handle different log levels
#             if "CRITICAL" in log_entry or "ERROR" in log_entry:
#                 print("🚨 ALERT: Critical issue detected!")
#             elif "WARNING" in log_entry:
#                 print("⚠️ Warning logged")
            
#         else:
#             print("📋 No new log entries")
            
#         # Safety exit for demo
#         if processed_logs >= len(log_entries) + 2:
#             print("🛑 Log monitoring stopped (demo limit)")
#             break
            
#         time.sleep(0.4)

# # Example: log_monitor()

# print("\n🔟 BACKGROUND SERVICE / DAEMON")
# print("-" * 33)
# print("Service that runs continuously:")

# def background_service():
#     """Simulates a background service"""
    
#     service_cycles = 0
#     tasks_completed = 0
    
#     print("🔄 BACKGROUND SERVICE STARTED")
    
#     while True:
#         service_cycles += 1
        
#         # Simulate different types of background tasks
#         task_type = random.choice([
#             "cleanup_temp_files",
#             "update_cache", 
#             "send_notifications",
#             "backup_data",
#             "health_check"
#         ])
        
#         print(f"🛠️ Cycle {service_cycles}: Executing {task_type}")
        
#         # Simulate task execution
#         execution_time = random.uniform(0.1, 0.5)
#         time.sleep(execution_time)
        
#         tasks_completed += 1
#         print(f"✅ Task completed in {execution_time:.2f}s")
        
#         # Service health check
#         if service_cycles % 5 == 0:
#             print(f"💗 Service Health Check: {tasks_completed} tasks completed")
        
#         # Safety exit for demo
#         if service_cycles >= 8:
#             print("🛑 Service stopped (demo limit)")
#             break

# # Example: background_service()

# print("\n" + "="*70)
# print("📋 SUMMARY OF WHILE TRUE USE CASES")
# print("="*70)

# summary = """
# 1️⃣ Input Validation     - Keep asking until valid data
# 2️⃣ Menu Systems        - Application main loops  
# 3️⃣ Network Retries     - Keep trying until success
# 4️⃣ Queue Processing    - Process items continuously
# 5️⃣ Game Loops         - Main game execution cycle
# 6️⃣ Real-time Monitoring - System/resource tracking
# 7️⃣ Chat Applications  - Conversational interfaces
# 8️⃣ API Polling        - Check for updates regularly
# 9️⃣ Log Monitoring     - Watch files for changes
# 🔟 Background Services - Daemon-like processes
# """
# print(summary)

# print("\n🎯 COMMON PATTERNS:")
# print("-" * 18)
# print("• Always have a BREAK condition to exit the loop")
# print("• Use try/except for error handling in loops")
# print("• Add safety counters to prevent infinite loops")
# print("• Include sleep/delays in monitoring/polling loops")
# print("• Validate user input before processing")

# print("\n⚠️ IMPORTANT SAFETY TIPS:")
# print("-" * 25)
# print("• Never create truly infinite loops without exit conditions")
# print("• Always test break conditions thoroughly")
# print("• Use timeouts for network operations")
# print("• Monitor resource usage in long-running loops")
# print("• Implement graceful shutdown mechanisms")

# print("\n💡 WHEN TO USE WHILE TRUE:")
# print("-" * 27)
# print("✅ User interaction loops")
# print("✅ Event processing systems") 
# print("✅ Server/service applications")
# print("✅ Real-time data processing")
# print("✅ Retry mechanisms")
# print("❌ Simple iterations (use for loops instead)")
# print("❌ When you know exact iteration count")

# print("="*70)