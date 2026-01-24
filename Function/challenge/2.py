def moon_phase(phase):
    if phase == 'New Moon':
        return '🌑'
    elif phase == 'Waphaseing Crescent':
        return '🌒'
    elif phase == 'First Quarter':
        return '🌓'
    elif phase == 'Waphaseing Gibbous':
        return '🌔'
    elif phase == 'Full Moon':
        return '🌕'
    elif phase == 'Waning Gibbous':
        return '🌖'
    elif phase == 'Last Quarter':
        return '🌗'
    elif phase == 'Waning Crescent':
        return '🌘'
    else: 
        return 'Invalid moon phase'
    
def main():
    answer = moon_phase('New Moon')
    print(answer)

if __name__ == "__main__":
    main()