import { useForm } from "react-hook-form";

function ToDoList() {
    const { register, watch }= useForm();
    console.log(watch());

    return <div>
        <form>
            <input {...register("Email")}  placeholder="Email"></input>
            <input {...register("firstName")}  placeholder="firstName"></input>
            <input {...register("lastName")}  placeholder="lastName"></input>
            <input {...register("username")}  placeholder="username"></input>
            <input {...register("password")}  placeholder="password"></input>
            <button >Add</button>
        </form>
    </div>;
}

export default ToDoList;
