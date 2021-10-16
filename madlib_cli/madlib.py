import re

def welcome_message():
    print(
        """
        *******************************
        *******************************
        **   Welcome to MadLib Game  **
        *******************************
        *******************************
        Please , answer all questions
        """
    )


def read_file(file_location):
    """
    function reads the file text 
    Input -->> the file path
    Output -->> the text in the file as string
    """
    try: 
        with open(file_location ,"r") as f:
            content = f.read()
            return content            
    except FileNotFoundError:
        print('The File is not found')
        raise FileNotFoundError



def user_input(content):
    """
    Input -->> content of template before as string 
    Output -->> return the users answers 
    """
    regex=r"\{([\w\s\d\'\-]+)\}"
    words_list=re.findall(regex,content)
    answers=[]
    for word in words_list:
        user_response=input(f"please, enter a {word} >>")
        answers.append(user_response) 
    return answers 



def merge(content,answers):
    """
    function merge the raw_content with user_answers ,then returns the new_content

    input -->> file content and the answers from the user
    output -->> merged string with answers
    """
    regex=r"\{([\w\s\d\'\-]+)\}"
    raw_content=re.sub(regex,"{}",content)
    new_content=raw_content.format(*answers)
    return new_content


def save(new_content):
    with open("assets/text.copy.txt","w") as new_file:
        new_file.write(new_content)



if __name__ == "__main__":

    welcome_message()
    path="assets/text.txt"
    content=read_file(path)
    answers=user_input(content)
    new_content=merge(content,answers)
    save(new_content)

