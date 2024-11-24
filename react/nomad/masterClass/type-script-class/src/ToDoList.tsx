import { useForm } from "react-hook-form";

interface IForm {
    toDo: string;
}

function ToDoList() {
    // The handleSubmit func has reponsible for managing somthing like Preventing default, validation, etc...  
    const { register, handleSubmit, setValue } = useForm<IForm>();
    const handleValid = (data: IForm) => {
        console.log(data.toDo)
        setValue("toDo", ""); // init after submitting
    };

    return <div>
        <form onSubmit={handleSubmit(handleValid )}>
            <input {...register("toDo", {
                required: "Please write a To Do"
            })} placeholder="Write a to do" />
            <button>Add</button>
        </form>
    </div>;
}

export default ToDoList;
