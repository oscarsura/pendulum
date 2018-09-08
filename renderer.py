def start(func):
    func()

def example():
    print('this is a parameterless function')

if __name__ == 'renderer':
    print('run as a module!')
    start(example)
