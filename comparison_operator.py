print(10==10)


print("a" == "A")


print(3 != 4)

# Let's demonstrate the difference:
print("\n--- String Comparison (ASCII/Unicode based) ---")
print(f"ASCII value of 'a': {ord('a')}")
print(f"ASCII value of 'A': {ord('A')}")
print(f"'a' == 'A': {'a' == 'A'}")

print("\n--- Integer Comparison (Numeric value based) ---")
print(f"Integer 3: {3}")
print(f"Integer 4: {4}")
print(f"3 != 4: {3 != 4}")

print("\n--- Interesting Cases ---")
print(f"'3' == 3: {'3' == 3}")  # String vs Integer
print(f"ord('3'): {ord('3')}")  # ASCII value of character '3'

# Chained Comparisons
print("\n--- Chained Comparisons ---")
print(f"1 < 2 < 3: {1 < 2 < 3}")
print(f"1 < 2 > 3: {1 < 2 > 3}")

print("\n" + "="*60)
print("REAL BUSINESS USE CASES - CHAINED COMPARISON OPERATORS")
print("="*60)

# 1. SALARY RANGE VALIDATION (HR/Payroll Systems)
print("\n1. 📊 SALARY RANGE VALIDATION")
min_salary = 50000
max_salary = 150000
employee_salary = 75000

# Traditional way (less readable)
if employee_salary >= min_salary and employee_salary <= max_salary:
    traditional_result = "Valid"
else:
    traditional_result = "Invalid"

# Chained comparison (more readable)
is_valid_salary = min_salary <= employee_salary <= max_salary
print(f"Employee Salary: ${employee_salary:,}")
print(f"Valid Range: ${min_salary:,} - ${max_salary:,}")
print(f"Is Valid Salary: {is_valid_salary}")

# 2. AGE-BASED INSURANCE PREMIUM (Insurance Industry)
print("\n2. 🏥 INSURANCE PREMIUM CALCULATION")
age = 35
# Different premium tiers based on age groups
def get_premium_tier(age):
    if 18 <= age <= 25:
        return "Young Adult - High Risk"
    elif 26 <= age <= 40:
        return "Prime - Standard Rate"
    elif 41 <= age <= 55:
        return "Middle Age - Moderate Rate"
    elif 56 <= age <= 70:
        return "Senior - Higher Rate"
    else:
        return "Outside Coverage Range"

print(f"Age: {age}")
print(f"Premium Tier: {get_premium_tier(age)}")

# 3. CREDIT SCORE EVALUATION (Banking/Finance)
print("\n3. 💳 CREDIT SCORE EVALUATION")
credit_score = 720
def evaluate_credit(score):
    if 800 <= score <= 850:
        return "Excellent - Best Rates"
    elif 740 <= score <= 799:
        return "Very Good - Good Rates"
    elif 670 <= score <= 739:
        return "Good - Fair Rates"
    elif 580 <= score <= 669:
        return "Fair - Higher Rates"
    else:
        return "Poor - Limited Options"

print(f"Credit Score: {credit_score}")
print(f"Rating: {evaluate_credit(credit_score)}")

# 4. INVENTORY MANAGEMENT (Supply Chain)
print("\n4. 📦 INVENTORY MANAGEMENT")
current_stock = 45
reorder_point = 20
max_stock = 100

# Multiple condition checks
needs_reorder = current_stock <= reorder_point
is_overstocked = current_stock >= max_stock
is_optimal_range = reorder_point < current_stock < max_stock

print(f"Current Stock: {current_stock}")
print(f"Needs Reorder: {needs_reorder}")
print(f"Is Overstocked: {is_overstocked}")
print(f"In Optimal Range: {is_optimal_range}")

# 5. PERFORMANCE RATING (Employee Management)
print("\n5. ⭐ EMPLOYEE PERFORMANCE RATING")
sales_target = 100000
actual_sales = 125000
performance_ratio = (actual_sales / sales_target) * 100

def get_performance_rating(ratio):
    if ratio >= 120:
        return "Exceeds Expectations - Bonus Eligible"
    elif 100 <= ratio < 120:
        return "Meets Expectations - Good Performance"
    elif 80 <= ratio < 100:
        return "Below Expectations - Needs Improvement"
    else:
        return "Unsatisfactory - Performance Plan Required"

print(f"Sales Target: ${sales_target:,}")
print(f"Actual Sales: ${actual_sales:,}")
print(f"Performance: {performance_ratio:.1f}%")
print(f"Rating: {get_performance_rating(performance_ratio)}")

# 6. DATA VALIDATION (Data Engineering/ETL)
print("\n6. 🔍 DATA QUALITY VALIDATION")
def validate_data_quality(completeness, accuracy, timeliness):
    """
    Validate data quality metrics (all should be percentages 0-100)
    """
    # Check if all metrics are in valid range
    if 0 <= completeness <= 100 and 0 <= accuracy <= 100 and 0 <= timeliness <= 100:
        # Determine overall quality
        if completeness >= 95 and accuracy >= 99 and timeliness >= 90:
            return "High Quality - Production Ready"
        elif completeness >= 85 and accuracy >= 95 and timeliness >= 80:
            return "Good Quality - Minor Issues"
        elif completeness >= 70 and accuracy >= 90 and timeliness >= 70:
            return "Fair Quality - Needs Attention"
        else:
            return "Poor Quality - Requires Immediate Action"
    else:
        return "Invalid Metrics - Check Data Source"

completeness = 98.5
accuracy = 99.2
timeliness = 92.0

print(f"Completeness: {completeness}%")
print(f"Accuracy: {accuracy}%")
print(f"Timeliness: {timeliness}%")
print(f"Quality Status: {validate_data_quality(completeness, accuracy, timeliness)}")

# 7. FINANCIAL RISK ASSESSMENT (Trading/Investment)
print("\n7. 📈 FINANCIAL RISK ASSESSMENT")
portfolio_value = 500000
daily_loss = 15000
risk_percentage = (daily_loss / portfolio_value) * 100

def assess_risk_level(risk_pct):
    if 0 <= risk_pct <= 1:
        return "Low Risk - Conservative"
    elif 1 < risk_pct <= 3:
        return "Moderate Risk - Balanced"
    elif 3 < risk_pct <= 5:
        return "High Risk - Aggressive"
    elif 5 < risk_pct <= 10:
        return "Very High Risk - Speculative"
    else:
        return "Extreme Risk - Immediate Action Required"

print(f"Portfolio Value: ${portfolio_value:,}")
print(f"Daily Loss: ${daily_loss:,}")
print(f"Risk Percentage: {risk_percentage:.2f}%")
print(f"Risk Level: {assess_risk_level(risk_percentage)}")

# 8. TEMPERATURE CONTROL (Manufacturing/IoT)
print("\n8. 🌡️ INDUSTRIAL TEMPERATURE MONITORING")
current_temp = 78.5
min_safe_temp = 65
max_safe_temp = 85
critical_low = 55
critical_high = 95

def get_temperature_status(temp):
    if critical_low <= temp <= critical_high:
        if min_safe_temp <= temp <= max_safe_temp:
            return "NORMAL - Within Safe Range"
        elif critical_low <= temp < min_safe_temp:
            return "WARNING - Below Safe Range"
        elif max_safe_temp < temp <= critical_high:
            return "WARNING - Above Safe Range"
    else:
        return "CRITICAL - Emergency Shutdown Required"

print(f"Current Temperature: {current_temp}°F")
print(f"Safe Range: {min_safe_temp}°F - {max_safe_temp}°F")
print(f"Status: {get_temperature_status(current_temp)}")

print("\n" + "="*60)
print("REAL EXAMPLES FROM GOOGLE & MICROSOFT PROJECTS")
print("="*60)

# 1. GOOGLE TENSORFLOW - Model Validation (Inspired by TensorFlow's input validation)
print("\n🤖 GOOGLE TENSORFLOW - Model Parameter Validation")
def validate_neural_network_params(learning_rate, batch_size, epochs):
    """
    Similar to TensorFlow's parameter validation in optimizers and training loops
    """
    # Learning rate validation (common in TensorFlow optimizers)
    if 0.0001 <= learning_rate <= 1.0:
        lr_status = "Valid"
    else:
        lr_status = "Invalid - Outside recommended range"
    
    # Batch size validation (power of 2, reasonable range)
    if 1 <= batch_size <= 1024 and (batch_size & (batch_size - 1)) == 0:
        batch_status = "Valid (Power of 2)"
    elif 1 <= batch_size <= 1024:
        batch_status = "Valid (Not optimal - consider power of 2)"
    else:
        batch_status = "Invalid"
    
    # Epochs validation
    epochs_status = "Valid" if 1 <= epochs <= 10000 else "Invalid"
    
    return lr_status, batch_status, epochs_status

# Test with typical ML parameters
lr = 0.001
batch_size = 32
epochs = 100

lr_result, batch_result, epoch_result = validate_neural_network_params(lr, batch_size, epochs)
print(f"Learning Rate ({lr}): {lr_result}")
print(f"Batch Size ({batch_size}): {batch_result}")
print(f"Epochs ({epochs}): {epoch_result}")

# 2. MICROSOFT AZURE - Resource Scaling (Based on Azure Functions scaling logic)
print("\n☁️ MICROSOFT AZURE - Auto-scaling Logic")
def azure_function_scaling_decision(cpu_usage, memory_usage, request_rate):
    """
    Simulates Azure Functions scaling decisions based on multiple metrics
    Similar to actual Azure scaling algorithms
    """
    # Scale up conditions (chained comparisons for readability)
    if 70 <= cpu_usage <= 100 and 60 <= memory_usage <= 100:
        if request_rate >= 100:
            return "SCALE UP AGGRESSIVE - High load detected"
        elif 50 <= request_rate < 100:
            return "SCALE UP MODERATE - Medium load"
    
    # Normal operation range
    if 20 <= cpu_usage <= 70 and 20 <= memory_usage <= 60:
        if 10 <= request_rate <= 50:
            return "MAINTAIN - Optimal performance"
    
    # Scale down conditions
    if 0 <= cpu_usage <= 20 and 0 <= memory_usage <= 30:
        if 0 <= request_rate <= 10:
            return "SCALE DOWN - Underutilized resources"
    
    return "MONITOR - Unusual pattern detected"

# Test Azure scaling scenarios
scenarios = [
    (85, 75, 120, "Peak Traffic"),
    (45, 40, 25, "Normal Operation"),
    (15, 20, 5, "Low Usage"),
    (95, 30, 200, "CPU Intensive Workload")
]

for cpu, memory, requests, scenario_name in scenarios:
    decision = azure_function_scaling_decision(cpu, memory, requests)
    print(f"{scenario_name}: CPU={cpu}%, Memory={memory}%, Requests={requests}/min")
    print(f"  → Decision: {decision}")

# 3. GOOGLE CHROME - Memory Management (Based on Chrome's memory pressure handling)
print("\n🌐 GOOGLE CHROME - Memory Pressure Detection")
def chrome_memory_pressure_level(available_memory_gb, memory_usage_percent, tab_count):
    """
    Simulates Chrome's memory pressure detection algorithm
    Based on Chromium's memory pressure monitoring
    """
    # Critical memory pressure (similar to Chrome's aggressive tab discarding)
    if 0 <= available_memory_gb <= 0.5 and 90 <= memory_usage_percent <= 100:
        return "CRITICAL - Aggressive tab discarding enabled"
    
    # High memory pressure (moderate tab management)
    elif 0.5 < available_memory_gb <= 2.0 and 80 <= memory_usage_percent <= 90:
        if tab_count >= 20:
            return "HIGH - Tab suspension recommended"
        else:
            return "HIGH - Monitor closely"
    
    # Moderate pressure (background tab optimization)
    elif 2.0 < available_memory_gb <= 4.0 and 60 <= memory_usage_percent <= 80:
        return "MODERATE - Background tab optimization"
    
    # Normal operation
    elif available_memory_gb > 4.0 and 0 <= memory_usage_percent <= 60:
        return "NORMAL - All features available"
    
    return "UNKNOWN - Check system status"

# Test Chrome memory scenarios
chrome_scenarios = [
    (0.3, 95, 25, "Gaming Laptop - Heavy Usage"),
    (1.5, 85, 30, "Work Laptop - Many Tabs"),
    (6.0, 45, 10, "High-end Desktop"),
    (0.8, 78, 15, "Tablet - Moderate Usage")
]

for mem_avail, mem_usage, tabs, device_type in chrome_scenarios:
    pressure = chrome_memory_pressure_level(mem_avail, mem_usage, tabs)
    print(f"{device_type}: {mem_avail}GB free, {mem_usage}% used, {tabs} tabs")
    print(f"  → Memory Pressure: {pressure}")

# 4. MICROSOFT SQL SERVER - Query Optimization (Based on SQL Server's cost-based optimizer)
print("\n🗄️ MICROSOFT SQL SERVER - Query Cost Analysis")
def sql_server_execution_plan_choice(estimated_rows, cpu_cost, io_cost):
    """
    Simulates SQL Server's query optimizer decision making
    Based on actual SQL Server cost-based optimization principles
    """
    total_cost = cpu_cost + io_cost
    
    # Index seek vs Table scan decision (simplified)
    if 1 <= estimated_rows <= 1000:
        if 0 <= total_cost <= 50:
            return "INDEX SEEK - Low cost, few rows"
        elif 50 < total_cost <= 100:
            return "INDEX SEEK with KEY LOOKUP - Moderate cost"
    
    # Consider parallel execution for large datasets
    elif 1000 < estimated_rows <= 100000:
        if 100 <= total_cost <= 1000:
            return "PARALLEL INDEX SCAN - Medium dataset"
        elif total_cost > 1000:
            return "PARALLEL TABLE SCAN - High cost justified"
    
    # Large dataset handling
    elif estimated_rows > 100000:
        if 500 <= total_cost <= 5000:
            return "PARALLEL EXECUTION - Large dataset optimization"
    
    return "TABLE SCAN - Default fallback"

# Test SQL optimization scenarios
sql_scenarios = [
    (500, 25, 15, "Small lookup query"),
    (50000, 300, 450, "Medium analytical query"),
    (2000000, 2000, 3000, "Large data warehouse query"),
    (10, 5, 8, "Primary key lookup")
]

for rows, cpu, io, query_type in sql_scenarios:
    plan = sql_server_execution_plan_choice(rows, cpu, io)
    total = cpu + io
    print(f"{query_type}: {rows:,} rows, Cost={total} (CPU:{cpu}, IO:{io})")
    print(f"  → Execution Plan: {plan}")

# 5. GOOGLE MAPS - Route Quality Assessment (Based on Google Maps routing algorithms)
print("\n🗺️ GOOGLE MAPS - Route Quality Scoring")
def google_maps_route_quality(distance_km, duration_min, traffic_factor, road_quality):
    """
    Simulates Google Maps route quality assessment
    Based on routing algorithm considerations
    """
    # Calculate efficiency metrics
    speed_kmh = (distance_km / duration_min) * 60 if duration_min > 0 else 0
    
    # Excellent routes (highways, optimal conditions)
    if 10 <= distance_km <= 500 and 0.8 <= traffic_factor <= 1.0:
        if 60 <= speed_kmh <= 120 and 8 <= road_quality <= 10:
            return "EXCELLENT - Fastest route recommended"
    
    # Good routes (mixed roads, decent traffic)
    elif 5 <= distance_km <= 200 and 0.6 <= traffic_factor <= 0.8:
        if 30 <= speed_kmh <= 70 and 6 <= road_quality <= 9:
            return "GOOD - Recommended route"
    
    # Fair routes (city driving, some congestion)
    elif 1 <= distance_km <= 50 and 0.4 <= traffic_factor <= 0.7:
        if 15 <= speed_kmh <= 40 and 5 <= road_quality <= 7:
            return "FAIR - Alternative available"
    
    # Poor routes (heavy traffic, bad roads)
    elif distance_km > 0 and 0.1 <= traffic_factor <= 0.5:
        if 5 <= speed_kmh <= 25 and 3 <= road_quality <= 6:
            return "POOR - Avoid if possible"
    
    return "CALCULATING - Route analysis in progress"

# Test Google Maps scenarios
maps_scenarios = [
    (45, 35, 0.9, 9, "Highway route - off peak"),
    (12, 25, 0.7, 7, "City route - moderate traffic"),
    (8, 35, 0.3, 5, "Downtown - rush hour"),
    (150, 90, 0.85, 8, "Interstate - good conditions")
]

for dist, time, traffic, quality, scenario in maps_scenarios:
    route_quality = google_maps_route_quality(dist, time, traffic, quality)
    speed = (dist / time) * 60 if time > 0 else 0
    print(f"{scenario}: {dist}km in {time}min ({speed:.1f} km/h)")
    print(f"  Traffic: {traffic:.1f}, Road Quality: {quality}/10")
    print(f"  → Route Rating: {route_quality}")

print("\n" + "="*60)
print("🎯 WHY GOOGLE & MICROSOFT USE CHAINED COMPARISONS:")
print("✅ Code readability in complex algorithms")
print("✅ Performance optimization (short-circuit evaluation)")
print("✅ Easier debugging and maintenance")
print("✅ Natural mathematical expression of ranges")
print("✅ Reduced cognitive load for developers")
print("✅ Fewer bugs in boundary condition handling")
print("="*60)