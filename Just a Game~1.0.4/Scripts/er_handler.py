import time
errors = []

def LoadError(day_var, cash_var, name_var, job_var):
    job_list = ['Discord Mod', 'Computer Programmer', 'Doctor', 'Cook', 'Graphics Developer']
    day_type = type(day_var)
    cash_type = type(cash_var)
    job_type = type(job_var)
    
    if day_type != int or day_var < -2 or day_var > 1:
        errors.append('Load Error: Invalid value for day_var: %s' % day_var)
    if cash_type != int or cash_var < 0 or cash_var > 150:
        errors.append('Load Error: Invalid value for cash_var: %s' % cash_var)
    if not isinstance(name_var, str) or name_var == '' or name_var not in ['Player#' + str(i) for i in range(1000, 10000)]:
        errors.append('Load Error: Invalid value for name_var: %s' % name_var)
    if job_type != str or (job_var == '' or job_var in job_list or job_var not in ['None']):
        errors.append('Load Error: Invalid value for job_var: %s' % job_var)
    
    if errors:
        with open('error_logs.txt', 'a') as f:
            f.write('\n'.join(errors) + ' : ' + time.strftime("%Y%m%d-%H%M%S") + '\n')
        raise ValueError(errors)
