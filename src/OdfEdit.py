import os
import sys

if __name__ == '__main__':
    if os.name == 'nt':
        from OdfEdit_windows import main
    else:
        from OdfEdit_linux import main
    
    main()