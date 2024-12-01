import { useRecoilState, useRecoilValue  } from "recoil";
import CreateToDo from "./CreateToDo";
import { categoryState, toDoSelector } from "../atoms";
import ToDo from "./ToDo";

function ToDoList() {
    const toDos = useRecoilValue(toDoSelector);
    console.log(toDos);
    const [category, setCategory] = useRecoilState(categoryState);
    const onInput = (e: React.FormEvent<HTMLSelectElement>) => {
        setCategory(e.currentTarget.value);
    }

    return (
        <div>
            <h1>To Dos</h1>
            <hr />
            <form>
                <select value={category} onInput={onInput}>
                    <option value="TO_DO">To Do</option>
                    <option value="DOING">Doing</option>
                    <option value="DONE">Done</option>
                </select>
            </form>
            <CreateToDo />
            {toDos?.map(toDo => <ToDo key={toDo.id} {...toDo}/> )}
        </div>
    );
}

export default ToDoList;
