help = """
Your project has been created!
__________________________________________________________________________
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣞⠛⠲⠇⠉⠻⠛⢧⡻⢿
⢟⡯⠽⠒⠒⠒⠺⣟⣿⢿⠯⢉⠥⣒⣭⣥⣬⣥⡈⠈⠋⣷
⡡⠐⠊⡉⠁⠈⣀⣈⠃⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⠀⢰⡣
⠀⠀⣴⣶⣿⣿⣿⣿⣿⣿⣦⣝⢿⣿⡿⢿⣟⠋⠁⢀⣈⡿
⠀⣠⣿⡿⡫⠑⡤⡍⠻⣿⣿⣿⣯⢻⠿⠛⠁⣀⣀⡻⣵⣾
⣿⣿⣿⣧⣃⣀⣀⠀⢀⣿⣿⣿⣿⣆⠀⠐⣤⠾⢿⣵⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⠋⠁⢐⢿⠬⡾⣻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢈⣀⡀⣿⢚⠳⠯⠒⠯⡿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢳⣮⣵⣦⣾⣿⣿⣿⡆⢹
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⣴⣶⣶⣮⣉⣶⣿⣿⡿⣡⢟
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣼⣿⣿⢰⢯⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⣉⣥⣈⡛⠿⠇⣜⣼⣿
__________________________________________________________________________

IF YOU HAVE NOT DONE SO ALREADY, CREATE A CONDA ENVIRONMENT FOR YOUR NEW PROJECT WITH:

cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}}
conda activate {{cookiecutter.repo_name}}

INSTALL YOUR NEW PROJECT IN YOUR LOCAL CONDA ENVIRONMENT WITH:

pip install -e .

HAVE FUN AND GOOD LUCK

“TRUE UNDERSTANDING COMES ONLY THROUGH THE PROCESS OF THINKING ON YOUR OWN.”
— 조훈현

"""
print(help)
