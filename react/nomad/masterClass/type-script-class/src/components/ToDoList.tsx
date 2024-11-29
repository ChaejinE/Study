import { useForm } from "react-hook-form";
import { atom, useRecoilState  } from "recoil";


interface IForm {
    toDo: string;
}

interface IToDo {
    text: string;
    category: "TO_DO" | "DOING" | "DONE"; // restrcit of string
    id: number;
}

const toDoState = atom<IToDo[]>({
    key: "toDo", 
    default: []
});

function ToDoList() {
    const [toDos, setToDos] = useRecoilState(toDoState); 

    // The handleSubmit func has reponsible for managing somthing like Preventing default, validation, etc...  
    const { register, handleSubmit, setValue } = useForm<IForm>();
    const handleValid = ({toDo}: IForm) => {
        setToDos(oldTodos => [{text: toDo, category: "TO_DO", id: Date.now() },  ...oldTodos])
        setValue("toDo", ""); 
    };
    console.log(toDos)

    return <div>
        <h1>To Dos</h1>
        <hr />
        <form onSubmit={handleSubmit(handleValid )}>
            <input {...register("toDo", {
                required: "Please write a To Do"
            })} placeholder="Write a to do" />
            <button>Add</button>
        </form>
        <ul>
            {toDos.map(toDo => <li key={toDo.id}>{toDo.text}</li>)}
        </ul>
    </div>;
}

export default ToDoList;
