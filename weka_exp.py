'''
Ejecuta el entrenamiento sobre un arbol de decision J.48 tomando como parametro el numero minimo de instancias
por hoja
'''

import subprocess

wekapath = '~/Documents/weka/weka-3-8-4/weka.jar'
command_template = 'java -classpath {wekapath} weka.classifiers.trees.J48 -t {filepath} -C 0.25 -M {min_num_obj}'


def execute(filepath: str, min_num_obj: int) -> str:
    command = command_template.format(
        wekapath=wekapath, min_num_obj=min_num_obj, filepath=filepath)
    print(command)
    process = subprocess.run(
        command, capture_output=True, text=True, shell=True)

    return process.stdout, process.stderr


def main():
    stdout, stderr = execute('./data.arff', 1)
    print('-' * 15 + 'STDOUT' + '-' * 15)
    print(stdout)
    print('-' * 37)
    print('-' * 15 + 'STDERR' + '-' * 15)
    print(stderr)
    print('-' * 37)


if __name__ == '__main__':
    main()
