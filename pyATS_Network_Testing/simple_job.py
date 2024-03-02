from pyats.easypy import run

def main():
    run("version_testcase.py")
    run("image_test.py")

'''
To run this pyats job use command: pyats run job simple_job.py --testbed-file testbed.yml 
'''
