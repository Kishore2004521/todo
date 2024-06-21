todos = []
while True:
    user_action = input("Enter the  type add ,show ,edit, exit : ")
    match user_action:
        case 'add':
            todo = input("Enter the Todo : ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                list = f"{index+1} - {item}"
                print(list)
        case 'edit':
            number = int(input("Enter the list number to edit : "))
            number = number - 1
            todo_new = input("Enter the new todo : ")
            todos[number] = todo_new
        case 'exit':
            break
