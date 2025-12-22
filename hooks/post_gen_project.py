#!/usr/bin/env python3

help = """
Your project has been created!

               . '@(@@@@@@@)@. (@@) `  .   '
     .  @@'((@@@@@@@@@@@)@@@@@)@@@@@@@)@ 
     @@(@@@@@@@@@@))@@@@@@@@@@@@@@@@)@@` .
  @.((@@@@@@@)(@@@@@@@@@@@@@@))@\@@@@@@@@@)@@@  .
 (@@@@@@@@@@@@@@@@@@)@@@@@@@@@@@\\@@)@@@@@@@@)
(@@@@@@@@)@@@@@@@@@@@@@(@@@@@@@@//@@@@@@@@@) ` 
 .@(@@@@)##&&&&&(@@@@@@@@)::_=(@\\@@@@)@@ .   .'
   @@`(@@)###&&&&&!!;;;;;;::-_=@@\\@)@`@.
   `   @@(@###&&&&!!;;;;;::-=_=@.@\\@@     '
      `  @.#####&&&!!;;;::=-_= .@  \\
            ####&&&!!;;::=_-        `
             ###&&!!;;:-_=
              ##&&!;::_=
             ##&&!;:=
            ##&&!:-
           #&!;:-
          #&!;=
          #&!-
           #&=
            #&-
            \\#/'

IF YOU HAVE NOT DONE SO ALREADY, CREATE A CONDA ENVIRONMENT FOR YOUR NEW PROJECT WITH:

cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}}
conda activate {{cookiecutter.repo_name}}

INSTALL YOUR NEW PROJECT IN YOUR LOCAL CONDA ENVIRONMENT WITH:

pip install -e .

HAVE FUN AND GOOD LUCK

- p

"""

#!/usr/bin/env python3

def main():
    print(help)


if __name__ == "__main__":
    main()